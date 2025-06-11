
import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"  #  FastAPI backend URL

st.set_page_config(page_title="Interview Coach", layout="centered")
st.title(" Roleplay Interview Coach")

# --- Session State Initialization ---
if "user_id" not in st.session_state:
    st.session_state.user_id = "user001"

if "persona" not in st.session_state:
    st.session_state.persona = "HR"

if "question" not in st.session_state:
    st.session_state.question = ""

if "qa_log" not in st.session_state:
    st.session_state.qa_log = []

# --- Sidebar for Persona Selection ---
st.sidebar.header("🎭 Choose Interview Persona")
persona = st.sidebar.radio("Select persona:", ["HR", "Technical", "Manager"])
st.session_state.persona = persona

# --- Start Interview ---
if st.button("🟢 Start Interview"):
    res = requests.post(f"{API_URL}/start-interview", json={
        "user_id": st.session_state.user_id,
        "persona": st.session_state.persona
    })
    if res.status_code == 200:
        st.session_state.question = res.json()["question"]
        st.success(" Interview Started!")
    else:
        st.error("❌ Failed to start interview.")

# --- Chat Interface ---
if st.session_state.question:
    st.subheader("🧠 Interviewer:")
    st.info(st.session_state.question)

    answer = st.text_area("✍️ Your Answer:", height=150, key="current_answer")

    if st.button("✅ Submit Answer"):
        res = requests.post(f"{API_URL}/submit-answer", json={
            "user_id": st.session_state.user_id,
            "question": st.session_state.question,
            "answer": answer
        })

        if res.status_code == 200:
            data = res.json()
            qa = {
                "question": st.session_state.question,
                "answer": answer,
                "score": data["score"],
                "feedback": data["feedback"]
            }
            st.session_state.qa_log.append(qa)
            st.session_state.question = ""  # Clear current question
            st.experimental_rerun()
        else:
            st.error("❌ Failed to submit answer.")

# --- Q&A History Chat Format ---
if st.session_state.qa_log:
    st.subheader("📜 Chat History")
    for idx, qa in enumerate(st.session_state.qa_log[::-1], 1):
        with st.container():
            st.markdown(f"**🧠 Q{len(st.session_state.qa_log)-idx+1}:** {qa['question']}")
            st.markdown(f"**🧑‍💼 You:** {qa['answer']}")
            st.markdown(f"**📊 Score:** `{qa['score']}`")
            st.markdown(f"**💡 Feedback:** {qa['feedback']}")
            st.markdown("---")

