from database import SessionLocal, CulturalItem, init_db
import artifact_data  # Your existing dictionary file

# Ensure tables exist
init_db()

db = SessionLocal()

print("Populating database...")

# Loop through your dictionary and add to SQL
for raw_key, data in artifact_data.DATABASE.items():
    
    # 1. CLEAN THE NAME (Remove .jpg if it exists in the key)
    # This ensures "Peksi_batik.jpg" and "Peksi_batik" both become "Peksi_batik"
    clean_name = raw_key.replace(".jpg", "").replace(".jpeg", "")
    
    # 2. CREATE THE FINAL FILENAME
    # This ensures we always have exactly one ".jpg"
    final_filename = f"{clean_name}.jpg"

    # Check if exists to avoid duplicates
    exists = db.query(CulturalItem).filter_by(name=clean_name).first()
    
    if not exists:
        item = CulturalItem(
            name=clean_name,    # This matches Keras output (e.g., "Peksi_batik")
            title=data["title"],
            category=data.get("category", "Heritage"),
            place_of_discovery=data["place_of_discovery"],
            origin=data["origin"],
            description=data["summary"], 
            fun_fact=data["fun_fact"],
            
            # 3. SAVE THE CORRECT FILENAME
            image_url=final_filename 
        )
        db.add(item)
        print(f"Added: {data['title']} -> (DB Image: {final_filename})")

db.commit()
db.close()
print("Database populated successfully!")