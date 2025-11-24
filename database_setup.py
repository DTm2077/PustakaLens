from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 1. CONFIGURATION
DATABASE_URL = "sqlite:///./heritage.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# 2. DEFINE THE TABLE
class CulturalItem(Base):
    __tablename__ = "cultural_items"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    title = Column(String)
    category = Column(String)
    place_of_discovery = Column(String)
    origin = Column(String)
    description = Column(Text)
    fun_fact = Column(Text)
    image_url = Column(String)

# 3. THE DATA TO INSERT
initial_data = [
    {
        "name": "Batik_Salvia_batik",
        "title": "Batik Salvia",
        "category": "Batik",
        "place_of_discovery": "Pekalongan, Central Java",
        "origin": "Modern Contemporary Motif",
        "description": "This batik motif is inspired by the Salvia flower. It represents healing, wisdom, and the blossoming of the soul.",
        "fun_fact": "Salvia comes from the Latin 'salvere', meaning 'to feel well'.",
        "image_url": "assets/batik_salvia.jpg"
    },
    {
        "name": "Garuda_Wisnu_Kencana",
        "title": "Garuda Wisnu Kencana",
        "category": "Statue",
        "place_of_discovery": "Ungasan, Bali",
        "origin": "Nyoman Nuarta (2018)",
        "description": "A colossal statue of the Hindu god Vishnu riding his mount, the eagle Garuda. It symbolizes the mission to save the world.",
        "fun_fact": "It is composed of 754 modules and is taller than the Statue of Liberty.",
        "image_url": "assets/gwk.jpg"
    },
    {
        "name": "Patung_Dirgantara",
        "title": "Patung Dirgantara",
        "category": "Statue",
        "place_of_discovery": "Pancoran, Jakarta",
        "origin": "Edhi Sunarso (1964)",
        "description": "Also known as the Pancoran Monument, this statue depicts a man reaching for the sky, representing the spirit of Indonesian aerospace.",
        "fun_fact": "President Soekarno posed for the statue to show the sculptor the gesture.",
        "image_url": "assets/dirgantara.jpg"
    },
    {
        "name": "patung_surabaya", 
        "title": "Sura & Baya Monument",
        "category": "Statue",
        "place_of_discovery": "Surabaya, East Java",
        "origin": "City Symbol (1952)",
        "description": "The symbol of Surabaya, depicting a battle between a Shark (Sura) and a Crocodile (Baya).",
        "fun_fact": "Surabaya literally translates to 'bravely facing danger'.",
        "image_url": "assets/surabaya.jpg"
    },
    {
        "name": "Peksi_batik",
        "title": "Batik Peksi (Bird)",
        "category": "Batik",
        "place_of_discovery": "Yogyakarta",
        "origin": "Traditional Royal Motif",
        "description": "Peksi is the refined Javanese word for Bird. This motif symbolizes freedom and the connection between earth and sky.",
        "fun_fact": "In the past, certain wing motifs were reserved only for the King.",
        "image_url": "assets/peksi.jpg"
    },
    {
        "name": "wayang_madya",
        "title": "Wayang Madya",
        "category": "Wayang",
        "place_of_discovery": "Surakarta (Solo)",
        "origin": "Mangkunegara IV",
        "description": "Wayang puppets that bridge the gap between ancient myths (Purwa) and modern history. They tell stories of Javanese kings.",
        "fun_fact": "These are very rare compared to the standard Wayang Purwa.",
        "image_url": "assets/madya.jpg"
    },
    {
        "name": "Wayang_Purwa",
        "title": "Wayang Purwa",
        "category": "Wayang",
        "place_of_discovery": "Java",
        "origin": "Ancient Tradition (10th Century)",
        "description": "The classic shadow puppets used to tell the Ramayana and Mahabharata epics.",
        "fun_fact": "The puppeteer (Dalang) controls all characters and voices alone.",
        "image_url": "assets/purwa.jpg"
    },
    {
        "name": "Wayang_Rama",
        "title": "Sri Rama",
        "category": "Wayang",
        "place_of_discovery": "Java / Bali",
        "origin": "Ramayana Epic",
        "description": "The protagonist of the Ramayana. He represents the ideal man: virtuous, brave, and loyal.",
        "fun_fact": "In Wayang, Rama's face is usually green or black to show inner calm.",
        "image_url": "assets/rama.jpg"
    }
]

# 4. EXECUTE SETUP
if __name__ == "__main__":
    print("--- SETUP STARTED ---")
    print("1. Creating Database Tables...")
    Base.metadata.create_all(bind=engine)
    
    print("2. Populating Data...")
    db = SessionLocal()
    try:
        for item in initial_data:
            # Check if exists
            exists = db.query(CulturalItem).filter_by(name=item['name']).first()
            if not exists:
                new_entry = CulturalItem(**item)
                db.add(new_entry)
                print(f"   [+] Added: {item['name']}")
            else:
                print(f"   [=] Exists: {item['name']}")
        
        db.commit()
        print("--- SETUP COMPLETE: heritage.db created successfully ---")
    except Exception as e:
        print(f"Error during population: {e}")
    finally:
        db.close()