from fastapi import APIRouter
from app.llm_service import generate_question, generate_feedback
from app.scoring import score_answer
from app.database import save_interaction
from app.models import InterviewRequest, AnswerRequest, FeedbackResponse

router = APIRouter()


@router.post("/start-interview")
def start_interview(request: InterviewRequest):
    question = generate_question(request.persona)
    return {"question": question}


@router.post("/submit-answer", response_model=FeedbackResponse)
def submit_answer(answer: AnswerRequest):
    score = score_answer(answer.answer)  # NLP scoring logic
    feedback = generate_feedback(answer.answer, score)  # Gemini
    save_interaction(answer.user_id, answer.question, answer.answer, score, feedback)  # Mongo
    return {"score": score, "feedback": feedback}

