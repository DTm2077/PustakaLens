import os
from PIL import Image

# Tentukan path ke folder dataset utama Anda
dataset_path = 'batik_motif'
corrupted_files = []

print(f"Memindai file gambar di dalam folder: {dataset_path}...")

# Loop melalui setiap folder dan file di dalam dataset_path
for root, _, files in os.walk(dataset_path):
    for filename in files:
        # Cek hanya file dengan ekstensi gambar umum
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            filepath = os.path.join(root, filename)
            try:
                # Coba buka gambar
                img = Image.open(filepath)
                # Lakukan verifikasi integritas file
                img.verify()
            except (IOError, SyntaxError) as e:
                # Jika gagal, file tersebut rusak atau bukan gambar
                print(f"Ditemukan file rusak: {filepath}")
                corrupted_files.append(filepath)

print("\nPemindaian selesai.")

if not corrupted_files:
    print("✅ Tidak ada file gambar yang rusak ditemukan.")
else:
    print("\n❌ Silakan HAPUS file-file rusak di atas dari folder dataset Anda, lalu coba training kembali.")