from flask import Flask, request, jsonify
import os
from flask_cors import CORS
from pymongo import MongoClient
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model
from sklearn.metrics.pairwise import cosine_similarity
from PIL import Image
import numpy as np
import requests
import io
import traceback

app = Flask(__name__)
CORS(app)

# ------------------ MongoDB ------------------
uri = "mongodb+srv://snehaghosh2903_db_user:SN2903%40%239osh@visual-matcher-cluster.jzawms2.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client["visual_matcher"]
collection = db["products"]

# ------------------ Model ------------------
print("🔄 Loading MobileNetV2 model...")
model = MobileNetV2(weights="imagenet", include_top=False, pooling="avg")
print("✅ Model loaded successfully!")

def extract_features(img: Image.Image):
    """Extract feature embedding using MobileNetV2"""
    img = img.resize((224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    features = model.predict(img_array)
    return features.flatten()

@app.route("/")
def home():
    return jsonify({"message": "✅ Flask API running successfully!"})

# ------------------ MATCH ROUTE ------------------
@app.route("/match", methods=["POST"])
def match_products():
    try:
        img = None

        # CASE 1: File upload
        if "image" in request.files:
            file = request.files["image"]
            if not file:
                return jsonify({"error": "Empty file"}), 400
            img_bytes = file.read()
            img = Image.open(io.BytesIO(img_bytes)).convert("RGB")

        # CASE 2: URL upload
        elif "imageUrl" in request.form and request.form["imageUrl"]:
            img_url = request.form["imageUrl"]
            response = requests.get(img_url, timeout=10)
            if response.status_code != 200:
                return jsonify({"error": "Could not download image"}), 400
            img = Image.open(io.BytesIO(response.content)).convert("RGB")

        # Missing image case
        else:
            return jsonify({"error": "No image provided"}), 400

        # Generate embedding for query image
        query_vector = extract_features(img)

        # Get products with embeddings
        products = list(collection.find({"embedding": {"$exists": True}}))

        if not products:
            return jsonify({"error": "No product embeddings found"}), 500

        similarities = []
        for p in products:
            emb = np.array(p["embedding"])
            score = float(cosine_similarity([query_vector], [emb])[0][0])
            similarities.append((p, score))

        # Sort by similarity
        similarities.sort(key=lambda x: x[1], reverse=True)

        # Apply filters
        filters = {
            "category": request.form.get("category"),
            "brand": request.form.get("brand"),
            "color": request.form.get("color"),
            "gender": request.form.get("gender"),
            "minPrice": request.form.get("minPrice"),
            "maxPrice": request.form.get("maxPrice"),
        }

        results = []
        for p, score in similarities[:10]:  # top 10 results
            price = p.get("price", 0)

            if filters["category"] and p.get("category") != filters["category"]:
                continue
            if filters["brand"] and p.get("brand") != filters["brand"]:
                continue
            if filters["color"] and p.get("color") != filters["color"]:
                continue
            if filters["gender"] and p.get("gender") != filters["gender"]:
                continue
            if filters["minPrice"] and price < int(filters["minPrice"]):
                continue
            if filters["maxPrice"] and price > int(filters["maxPrice"]):
                continue

            p["_id"] = str(p["_id"])
            p["similarity"] = round(score, 3)
            results.append(p)

        # ✅ Handle no matches gracefully
        if not results:
            return jsonify({
                "results": [],
                "message": "No similar products found. Try uploading another image or different filters."
            }), 200

        return jsonify({"results": results, "message": "Matches found!"})

    except Exception as e:
        print("❌ /match ERROR:", e)
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

# ------------------ FILTER ROUTE ------------------
@app.route("/filters", methods=["GET"])
def get_filters():
    try:
        return jsonify({
            "categories": sorted(collection.distinct("category")),
            "brands": sorted(collection.distinct("brand")),
            "colors": sorted(collection.distinct("color")),
            "genders": sorted(collection.distinct("gender"))
        })
    except Exception as e:
        print("❌ /filters ERROR:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
