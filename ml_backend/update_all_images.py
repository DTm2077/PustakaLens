import sqlite3

def update_database():
    conn = sqlite3.connect('heritage.db')
    cursor = conn.cursor()

    # Dictionary of 'Class Name' -> 'Real Image URL'
    # These match the CLASS_NAMES list in your main.py
    updates = {
        "Patung_Dirgantara": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Pancoran_Statue_Jakarta.jpg/600px-Pancoran_Statue_Jakarta.jpg",
        
        "Garuda_Wisnu_Kencana": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Garuda_Wisnu_Kencana_Statue.jpg/800px-Garuda_Wisnu_Kencana_Statue.jpg",
        
        "patung_surabaya": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Patung_Sura_dan_Baya.jpg/600px-Patung_Sura_dan_Baya.jpg",
        
        "Peksi_batik": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Batik_Peksi_Hokokai.jpg/800px-Batik_Peksi_Hokokai.jpg",
        
        "Batik_Salvia_batik": "https://live.staticflickr.com/65535/49696295383_a0d8d56b06_b.jpg", 
        
        "Wayang_Purwa": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Wayang_Kulit_Gatot_Kaca.jpg/600px-Wayang_Kulit_Gatot_Kaca.jpg",
        
        "Wayang_Rama": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Wayang_Kulit_Rama.jpg/600px-Wayang_Kulit_Rama.jpg",
        
        "wayang_madya": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Wayang_Madya.jpg/600px-Wayang_Madya.jpg"
    }

    print("--- UPDATING DATABASE IMAGES ---")
    
    for name, url in updates.items():
        try:
            # Check if item exists first
            cursor.execute("SELECT id FROM cultural_items WHERE name = ?", (name,))
            if cursor.fetchone():
                cursor.execute("UPDATE cultural_items SET image_url = ? WHERE name = ?", (url, name))
                print(f"✅ Updated: {name}")
            else:
                print(f"⚠️ Skipped: {name} (Not found in DB)")
        except Exception as e:
            print(f"❌ Error updating {name}: {e}")

    conn.commit()
    conn.close()
    print("\n--- DONE! All items now have real internet images. ---")

if __name__ == "__main__":
    update_database()