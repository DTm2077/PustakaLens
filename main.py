import io
import numpy as np
import tensorflow as tf
from PIL import Image
from fastapi import FastAPI, UploadFile, File, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware  # <--- NEW IMPORT
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
import uvicorn # <--- NEW IMPORT (For running directly)

# ==========================================
# 1. SETUP DATABASE & MODELS
# ==========================================
DATABASE_URL = "sqlite:///./heritage.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define the Table Structure
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

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ==========================================
# 2. SETUP AI MODEL & APP
# ==========================================
app = FastAPI()

# --- FIX START: ADD CORS MIDDLEWARE ---
# This allows your Flutter Web app (localhost) to talk to this Python API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (POST, GET, etc.)
    allow_headers=["*"],
)
# --- FIX END ---

MODEL_PATH = 'artifact_classifier.keras'

print("Loading Keras Model...")
try:
    model = tf.keras.models.load_model(MODEL_PATH)
    print("Model loaded successfully.")
except Exception as e:
    print(f"ERROR LOADING MODEL: {e}")
    model = None

# IMPORTANT: This list matches the order of your training folders
CLASS_NAMES = [
    'Batik_Salvia_batik', 
    'Garuda_Wisnu_Kencana', 
    'Patung_Dirgantara',
    'patung_surabaya', 
    'Peksi_batik', 
    'wayang_madya', 
    'Wayang_Purwa', 
    'Wayang_Rama'
]

# Helper to process image
def process_image(image_bytes: bytes) -> np.ndarray:
    IMG_SIZE = 180
    img = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    img = img.resize((IMG_SIZE, IMG_SIZE))
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)
    return img_array

# ==========================================
# 3. API RESPONSE SCHEMAS (For Flutter)
# ==========================================
class ItemDetailsSchema(BaseModel):
    title: str
    category: str
    place_of_discovery: str
    origin: str
    description: str
    fun_fact: str
    image_url: str

    class Config:
        orm_mode = True

class PredictionResponseSchema(BaseModel):
    motif: str
    confidence: float
    item_details: ItemDetailsSchema

# ==========================================
# 4. THE ENDPOINT
# ==========================================
@app.post("/scan_predict", response_model=PredictionResponseSchema)
async def scan_predict(image: UploadFile = File(...), db: Session = Depends(get_db)):
    
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded.")

    # A. Predict with Keras
    image_bytes = await image.read()
    processed_image = process_image(image_bytes)
    predictions = model.predict(processed_image)
    score = tf.nn.softmax(predictions[0])
    
    predicted_class_index = np.argmax(score)
    predicted_motif = CLASS_NAMES[predicted_class_index]
    confidence = float(100 * np.max(score))

    print(f"Predicted: {predicted_motif} ({confidence:.2f}%)")

    # B. Query Database
    # SELECT * FROM cultural_items WHERE name = 'predicted_motif'
    item_details = db.query(CulturalItem).filter(CulturalItem.name == predicted_motif).first()

    if item_details is None:
        # Fallback if Keras predicts a class but DB has no info
        raise HTTPException(status_code=404, detail=f"Item '{predicted_motif}' identified, but details not found in database.")

    # C. Return Combined Data
    return {
        "motif": predicted_motif,
        "confidence": confidence,
        "item_details": item_details
    }

# ==========================================
# 5. RUN SERVER (Specific Port)
# ==========================================
if __name__ == "__main__":
    # This forces the app to run on port 5000 to match your Flutter code
    uvicorn.run(app, host="0.0.0.0", port=5000)