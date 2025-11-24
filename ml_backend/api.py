from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database URL (using SQLite for simplicity)
DATABASE_URL = "sqlite:///./test.db"

# Create the engine and session
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define the base class for the models
Base = declarative_base()

# Define the cultural item model
class CulturalItem(Base):
    __tablename__ = "cultural_items"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)  # Name of the item (e.g., Batik type)
    category = Column(String)          # Category like Batik, Wayang, etc.
    description = Column(Text)        # Description of the item
    image_url = Column(String)        # Path or URL to the item's image

# Create tables in the database
Base.metadata.create_all(bind=engine)
