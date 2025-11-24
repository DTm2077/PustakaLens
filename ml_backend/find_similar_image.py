import os
import numpy as np
import pickle
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from sklearn.metrics.pairwise import cosine_similarity

# --- Load Model hanya sekali ---
base_model = VGG16(weights='imagenet', include_top=False, pooling='avg')

# --- Load Database fitur ---
with open('features_database.pkl', 'rb') as f:
    data = pickle.load(f)

dataset_features = data['features']
dataset_paths = data['paths']


def extract_features(img_path, model):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    expanded_img_array = np.expand_dims(img_array, axis=0)
    preprocessed_img = preprocess_input(expanded_img_array)
    features = model.predict(preprocessed_img, verbose=0)
    return features.flatten()


# ====== FUNGSI UTAMA UNTUK FASTAPI ======
def find_similar_image(image_path):
    if not os.path.exists(image_path):
        return {"error": "File tidak ditemukan"}

    # 1. Ekstrak fitur input
    input_features = extract_features(image_path, base_model)
    input_features = input_features.reshape(1, -1)

    # 2. Hitung similarity
    similarities = cosine_similarity(input_features, dataset_features)

    # 3. Ambil gambar paling mirip
    idx = np.argmax(similarities)
    best_match = dataset_paths[idx]
    confidence = float(similarities[0][idx])

    # 4. Return sebagai JSON
    return {
        "input_image": image_path,
        "matched_image": best_match,
        "confidence": confidence,
    }
