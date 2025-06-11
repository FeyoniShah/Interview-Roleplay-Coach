from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Connect to local MongoDB
client = MongoClient(os.getenv("MONGO_URI"))

# Create or connect to database and collection
db = client["interview_coach"]        
collection = db["sessions"]           

# Save one interview interaction
def save_interaction(user_id, question, answer, score, feedback):
    collection.insert_one({
        "user_id": user_id,
        "question": question,
        "answer": answer,
        "score": score,
        "feedback": feedback
    })
