# 💬 Roleplay Interview Coach

> An AI-powered mock interview trainer that simulates realistic HR, Tech, and Manager interviews, scores your answers, provides constructive feedback, and helps you improve over time.

---

## 🧠 Problem Statement

Candidates often struggle with:
- Lack of realistic mock interviews
- No structured feedback or scoring
- Difficulty improving soft skills (clarity, confidence)

This project solves that by acting as a **roleplay interviewer** powered by **Gemini API**, providing:
- Dynamic, persona-based questions
- Answer evaluation (Relevance, Clarity, Confidence)
- Contextual feedback and tips
- Session tracking with MongoDB

---

## 🔧 Tech Stack

| Component     | Tool / Library            | Purpose                                 |
|--------------|---------------------------|-----------------------------------------|
| LLM          | Gemini 1.5 Flash API      | Ask questions & generate feedback       |
| Backend API  | FastAPI                   | Build RESTful APIs                      |
| UI           | Streamlit                 | Simple, interactive front-end           |
| Database     | MongoDB (via PyMongo)     | Store answers, scores, feedback         |
| Env Mgmt     | Conda / python-dotenv     | Manage dependencies and secrets         |
| Dev Tools    | Curl, Uvicorn, VS Code    | API testing and development             |

---

## ✅ Features

- 🎭 Persona-based interview questions (HR, Tech, Manager)
- 📝 Real-time answer scoring and feedback
- 📊 Tracks user sessions and weak answers
- 🔁 Suggests follow-up for improvement
- 🖥️ User-friendly Streamlit UI

---
