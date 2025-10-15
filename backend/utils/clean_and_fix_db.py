from pymongo import MongoClient
import numpy as np

# --------------------------------------------------------------------
# 1️⃣ Connect to MongoDB Atlas
# --------------------------------------------------------------------
uri = "mongodb+srv://snehaghosh2903_db_user:SN2903%40%239osh@visual-matcher-cluster.jzawms2.mongodb.net/?retryWrites=true&w=majority&appName=visual-matcher-cluster"
client = MongoClient(uri)
db = client["visual_matcher"]
collection = db["products"]

# --------------------------------------------------------------------
# 2️⃣ Remove duplicates (keep first one based on name + imageUrl)
# --------------------------------------------------------------------
print("🔍 Checking for duplicates in 'products' collection...")

pipeline = [
    {
        "$group": {
            "_id": {"name": "$name", "imageUrl": "$imageUrl"},
            "ids": {"$addToSet": "$_id"},
            "count": {"$sum": 1}
        }
    },
    {"$match": {"count": {"$gt": 1}}}
]

duplicates = list(collection.aggregate(pipeline))
print(f"Found {len(duplicates)} duplicate groups.")

deleted_count = 0
for dup in duplicates:
    ids = dup["ids"]
    ids.pop(0)  # keep the first
    result = collection.delete_many({"_id": {"$in": ids}})
    deleted_count += result.deleted_count

print(f"🧹 Removed {deleted_count} duplicate documents successfully.\n")

# --------------------------------------------------------------------
# 3️⃣ Check embedding status
# --------------------------------------------------------------------
missing_embeddings = list(collection.find({"embedding": {"$exists": False}}))
print(f"🔎 Products missing embeddings: {len(missing_embeddings)}")

# --------------------------------------------------------------------
# 4️⃣ Add embeddings using MobileNetV2 (only if missing)
# --------------------------------------------------------------------
if missing_embeddings:
    from tensorflow.keras.applications import MobileNetV2, preprocess_input
    from tensorflow.keras.preprocessing import image
    import requests
    from io import BytesIO
    from PIL import Image
    import tensorflow as tf

    print("🔄 Loading MobileNetV2 model for embedding generation...")
    model = MobileNetV2(weights="imagenet", include_top=False, pooling="avg")
    print("✅ Model loaded successfully!\n")

    for product in missing_embeddings:
        try:
            img_url = product.get("imageUrl")
            if not img_url:
                continue

            # Fetch and preprocess image
            response = requests.get(img_url, timeout=5)
            img = Image.open(BytesIO(response.content)).convert("RGB")
            img = img.resize((224, 224))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array = preprocess_input(img_array)

            # Extract embedding
            features = model.predict(img_array, verbose=0)[0].tolist()

            # Update in MongoDB
            collection.update_one(
                {"_id": product["_id"]},
                {"$set": {"embedding": features}}
            )
            print(f"✅ Added embedding for {product.get('name', 'Unknown Product')}")

        except Exception as e:
            print(f"⚠️ Error processing {product.get('name', 'Unknown')}: {e}")

    print("\n🎯 Embedding update completed!")

else:
    print("✅ All products already have embeddings. No action needed.")

# --------------------------------------------------------------------
# 5️⃣ Create a unique index (to prevent duplicates forever)
# --------------------------------------------------------------------
try:
    collection.create_index(
        [("name", 1), ("imageUrl", 1)],
        unique=True,
        name="unique_name_image"
    )
    print("🔒 Unique index created — future duplicates prevented!")
except Exception as e:
    print(f"(ℹ️ Index creation info): {e}")

print("\n✅ Database cleanup and validation complete.")
