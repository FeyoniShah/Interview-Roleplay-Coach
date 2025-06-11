# app/models.py

from pydantic import BaseModel

# Used by POST /start-interview
class InterviewRequest(BaseModel):
    user_id: str
    persona: str  # Example: "HR", "Tech", "Manager"

# Used by POST /submit-answer
class AnswerRequest(BaseModel):
    user_id: str
    question: str
    answer: str

# Response model used by /submit-answer
class FeedbackResponse(BaseModel):
    score: dict
    feedback: str
