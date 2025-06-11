


import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

print("GEMINI_API_KEY =", os.getenv("GEMINI_API_KEY"))


api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not loaded from environment.")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_question(persona: str):
    prompt = f"Act as a {persona} interviewer. Ask a behavioral interview question."
    try:
        response = model.generate_content(prompt)
        print(" Gemini raw response:", response)
        return response.text if response.text else "Sorry, Gemini returned empty content."
    except Exception as e:
        print("Gemini API error:", repr(e))  # Print full error
        return "Sorry, I couldn't generate a question at the moment."


def generate_feedback(answer: str, score: dict):
    prompt = f"This answer scored {score}. Give feedback for improvement: \"{answer}\""
    try:
        response = model.generate_content(prompt)
        return response.text if response.text else "Gemini did not return feedback."
    except Exception as e:
        print(" Gemini API error (feedback):", e)
        return "Sorry, I couldn't generate feedback."
