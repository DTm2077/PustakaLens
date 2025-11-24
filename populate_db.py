from database import SessionLocal, CulturalItem, init_db
import artifact_data  # Your existing dictionary file

# Ensure tables exist
init_db()

db = SessionLocal()

print("Populating database...")

# Loop through your dictionary and add to SQL
for filename, data in artifact_data.DATABASE.items():
    # Check if exists to avoid duplicates
    exists = db.query(CulturalItem).filter_by(filename=filename).first()
    if not exists:
        item = CulturalItem(
            filename=filename,
            title=data["title"],
            category="Heritage", # You can customize this later
            place_of_discovery=data["place_of_discovery"],
            origin=data["origin"],
            description=data["summary"], # Note: Mapping 'summary' to 'description'
            fun_fact=data["fun_fact"],
            image_url="" # Optional
        )
        db.add(item)
        print(f"Added: {data['title']}")

db.commit()
db.close()
print("Database populated successfully!")