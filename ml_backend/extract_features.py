import os
import pickle
import numpy as np
from PIL import Image
from tqdm import tqdm

# --- FUNGSI EKSTRAKSI FITUR BARU (Ganti logika yang hilang) ---
def extract_color_features(image_path):
    """Mengekstrak fitur rata-rata warna dan histogram sederhana."""
    try:
        img = Image.open(image_path).convert('RGB')
        
        # 1. Fitur Rata-rata Warna (RGB Mean)
        img_np = np.array(img)
        r_mean, g_mean, b_mean = np.mean(img_np, axis=(0, 1))
        
        # 2. Histogram (Sederhana: 8 bins per channel)
        hist = []
        for channel in range(3):
            hist_channel, _ = np.histogram(img_np[:,:,channel], bins=8, range=(0, 256))
            hist.extend(hist_channel)
            
        # Gabungkan fitur mean dan histogram
        return np.array([r_mean, g_mean, b_mean] + hist, dtype=np.float32)
    
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return None
# -----------------------------------------------------------------

# [ASUMSI: Bagian ini adalah kode utama skrip extract_features.py Anda]
dataset_path = 'dataset'  # Pastikan path ini benar!
features_database = []

print("Memulai ekstraksi fitur dari dataset (Mode Scikit-learn)...")
for root, _, files in os.walk(dataset_path):
    for file_name in tqdm(files):
        if file_name.lower().endswith(('.jpg', '.jpeg', '.png')):
            image_path = os.path.join(root, file_name)
            
            # 🚨 Panggil fungsi fitur baru
            features = extract_color_features(image_path)
            
            if features is not None:
                # Simpan (fitur, path relatif)
                relative_path = os.path.relpath(image_path, start=dataset_path)
                features_database.append((features, relative_path))

# Simpan hasilnya
features_list, path_list = zip(*features_database)
with open('features_database.pkl', 'wb') as f:
    pickle.dump((features_list, path_list), f)
print("\n✅ Ekstraksi fitur selesai. File features_database.pkl baru telah dibuat.")