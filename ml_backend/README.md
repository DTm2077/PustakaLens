UPDATE:
order untuk menjalankan file dan pembuatan api: find_bad_images.py untuk cek foto-foto yang corrupt atau beda format -> main.py -> train_batik_model.py
PASTIKAN SUDAH DOWNLOAD DATASET BATIK DAN DISIMPAN DI FOLDER YANG SAMA

###########################################################
PREV VERSION:
pip install scikit-learn Pillow
instal tensorflow, numpy, dan matplotlib

Nama folder datasetnya batik_motif
Kode untuk Ekstraksi Fitur (extract_features.py_)
Kode untuk Mencari Gambar Mirip (find_similar.py)

Step by step
Letak file extract_features.py dan folder batik_motif di direktori yang sama
Buka terminal, jalankan python extract_features.py
Tunggu prosesnya selesai, akan ada file features_database.pkl

Simpan gambar batik yang ingin dites di komputer
Jalankan skrip python find_similar.py
Terminal akan meminta untuk memasukkan path ke gambar. Contoh: C:\Users\User\Downloads\test_batik.jpg atau ./test_batik.jpg
Enter dan akan tampil dua gambar, gambar di foto dan gambar yang paling mirip dari dataset
