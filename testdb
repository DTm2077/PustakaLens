import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# --- 1. Import the necessary structure from your main setup ---
# NOTE: We need the full class definition from your database setup file.
try:
    # Assuming you kept the CulturalItem class definition in a file called database_setup.py
    from database_setup import Base, CulturalItem, DATABASE_URL
except ImportError:
    print("FATAL ERROR: Could not import database structure.")
    print("Ensure your database setup file is named 'database_setup.py' and contains the CulturalItem class.")
    sys.exit(1)

# --- 2. Setup Connection ---
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def read_artifact_data(artifact_name):
    """Retrieves and prints all details for a given artifact name."""
    print(f"\n--- QUERYING DATABASE FOR: {artifact_name} ---")

    # Query the database
    # SELECT * FROM cultural_items WHERE name = 'artifact_name'
    item = session.query(CulturalItem).filter(CulturalItem.name == artifact_name).first()

    if item:
        print("✅ DATA CHECK SUCCESSFUL")
        print(f"ID: {item.id}")
        print(f"TITLE: {item.title}")
        print(f"CATEGORY: {item.category}")
        print(f"LOCATION: {item.place_of_discovery}")
        print(f"ORIGIN: {item.origin}")
        print("-" * 35)
        print(f"SUMMARY: {item.description}")
        print(f"FUN FACT: {item.fun_fact}")
        print("-" * 35)
    else:
        print(f"❌ ERROR: Artifact '{artifact_name}' not found in the database.")

# --- 3. Run the Tests ---
if __name__ == "__main__":
    # You can change these names to test your other entries
    read_artifact_data("Garuda_Wisnu_Kencana") 
    read_artifact_data("Peksi_batik") 
    read_artifact_data("wayang_madya") 
    session.close()