




#uvicorn app.main:app --reload




from fastapi import FastAPI
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from app.routes import router  # Import your routes after loading env

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(title="Roleplay Interview Coach")

# Environment variables
MONGO_URI = os.getenv("MONGO_URI")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# MongoDB client
try:
    client = MongoClient(MONGO_URI)
    db = client["interview_coach_db"]
    print("✅ Connected to MongoDB successfully.")
    mongo_status = "connected"
except Exception as e:
    print("❌ MongoDB connection failed:", e)
    mongo_status = "not connected"

# Add a root route (optional but useful for testing)
@app.get("/")
def read_root():
    return {
        "message": "✅ FastAPI is running.",
        "mongo_status": mongo_status,
        "gemini_key_loaded": True if GEMINI_API_KEY else False
    }

# Include other routes
app.include_router(router)
