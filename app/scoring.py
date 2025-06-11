# app/scoring.py

def score_answer(answer: str):
    # Very basic scoring logic using simple heuristics
    clarity = 70 if len(answer.split()) > 20 else 40

    # Check for confident phrasing
    confidence = 60 if any(phrase in answer.lower() for phrase in ["i led", "i decided", "i initiated", "i proposed"]) else 40

    # Check for keywords indicating relevance to typical interview topics
    relevance = 80 if any(keyword in answer.lower() for keyword in ["project", "team", "conflict", "deadline", "goal"]) else 50

    return {
        "clarity": clarity,
        "confidence": confidence,
        "relevance": relevance
    }
