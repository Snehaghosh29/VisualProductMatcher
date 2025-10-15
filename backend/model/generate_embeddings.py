import numpy as np
from pymongo import MongoClient
from PIL import Image
import requests
from io import BytesIO
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input
from tensorflow.keras.preprocessing import image as keras_image

# -----------------------------------------------------------------------------
# MongoDB Connection
# -----------------------------------------------------------------------------
uri = "mongodb+srv://snehaghosh2903_db_user:SN2903%40%239osh@visual-matcher-cluster.jzawms2.mongodb.net/?retryWrites=true&w=majority&appName=visual-matcher-cluster"
client = MongoClient(uri)
db = client["visual_matcher"]
collection = db["products"]

# -----------------------------------------------------------------------------
# Load MobileNetV2 for Feature Extraction
# -----------------------------------------------------------------------------
print("🔄 Loading MobileNetV2 model...")
model = MobileNetV2(weights="imagenet", include_top=False, pooling="avg")
print("✅ Model loaded successfully!")

def extract_features(img):
    """Extract normalized feature vector (1280-dim) from image."""
    img = img.resize((224, 224))
    img_array = keras_image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    features = model.predict(img_array)
    features = features.flatten()
    features = features / np.linalg.norm(features)
    return features.tolist()

# -----------------------------------------------------------------------------
# Generate and Save Embeddings
# -----------------------------------------------------------------------------
count = 0
for product in collection.find():
    try:
        url = product.get("imageUrl")
        if not url:
            print(f"⚠️ Skipping {product.get('name', 'Unknown')} (no image URL)")
            continue

        response = requests.get(url, timeout=8)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content)).convert("RGB")

        features = extract_features(img)
        collection.update_one({"_id": product["_id"]}, {"$set": {"embedding": features}})
        count += 1
        print(f"✅ Processed {product.get('name', 'Unnamed')}")

    except Exception as e:
        print(f"❌ Error processing {product.get('name', 'Unknown')}: {e}")

print(f"\n🎯 Completed! Generated embeddings for {count} products.")
