import numpy as np
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input
from tensorflow.keras.preprocessing import image

# Load model once globally (without top classification layer)
model = MobileNetV2(weights="imagenet", include_top=False, pooling="avg")

def extract_features(img):
    """Extract feature vector (1280-dim) from image."""
    img = img.resize((224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    features = model.predict(img_array)
    return features.flatten().tolist()
