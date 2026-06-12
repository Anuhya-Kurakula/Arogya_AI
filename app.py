import streamlit as st

from src.loader import load_documents
from src.splitter import split_documents
from src.vector_db import create_vector_db
from src.rag_chain import ask_question

from utils.helper import save_uploaded_files
from utils.ui_components import load_css


# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Arogya AI",
    page_icon="assets/logo.png",
    layout="wide"
)

load_css()


# ---------------- SESSION STATE ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "last_answer" not in st.session_state:
    st.session_state.last_answer = ""

if "selected_question" not in st.session_state:
    st.session_state.selected_question = None


# ---------------- SIDEBAR ----------------
with st.sidebar:

    try:
        st.image("assets/logo.png", width=120)
    except:
        pass

    st.title("🌿 Arogya AI")
    st.caption("Healthcare Assistant for Rural Communities")

    st.markdown("---")

    st.subheader("💡 Example Questions")

    # Health Questions
    with st.expander("🏥 Health Questions"):

        health_questions = [

            "What are symptoms of diabetes?",
            "What causes malaria?",
            "What is dengue?",
            "What are symptoms of hypertension?",
            "How can dengue be prevented?",
            "What are symptoms of tuberculosis?",
            "What causes fever?",
            "What is anemia?",
            "What foods are healthy?",
            "How to prevent COVID-19?",
            "How much sleep do adults need?",
            "How to improve immunity?"
        ]

        for q in health_questions:

            if st.button(q, key=q, use_container_width=True):
                st.session_state.selected_question = q


    # Medical Tools
    with st.expander("⚕ Medical Tool Questions"):

        medical_questions = [

            "Calculate BMI for 70 kg and 1.75 m",
            "BMI for 80 kg and 1.68 m",

            "My BP is 150/95",
            "Blood pressure 120/80",

            "Diabetes risk",
            "Tell me diabetes risk factors",

            "I have fever and cough",

            "Tell me about paracetamol",
            "What is ibuprofen used for?",
            "Uses of metformin",

            "Heart rate is 110",
            "My heart rate is 55",

            "Daily water intake",
            "How much water should I drink?",

            "Daily calories",

            "Pregnancy BMI",

            "Temperature is 38.5",
            "My body temperature is 36.8"
        ]

        for q in medical_questions:

            if st.button(q, key="tool_" + q, use_container_width=True):
                st.session_state.selected_question = q


    # Telugu
    with st.expander("🇮🇳 Telugu Questions"):

        telugu_questions = [

            "డెంగ్యూ లక్షణాలు ఏమిటి?",
            "మధుమేహం అంటే ఏమిటి?",
            "జ్వరం ఎందుకు వస్తుంది?",
            "రక్తపోటు అంటే ఏమిటి?",
            "మలేరియా లక్షణాలు ఏమిటి?",
            "నీరు ఎంత తాగాలి?"
        ]

        for q in telugu_questions:

            if st.button(q, key="te_" + q, use_container_width=True):
                st.session_state.selected_question = q


    # Hindi
    with st.expander("🇮🇳 Hindi Questions"):

        hindi_questions = [

            "डायबिटीज के लक्षण क्या हैं?",
            "बुखार क्यों आता है?",
            "डेंगू क्या है?",
            "मलेरिया के लक्षण क्या हैं?"
        ]

        for q in hindi_questions:

            if st.button(q, key="hi_" + q, use_container_width=True):
                st.session_state.selected_question = q


    st.markdown("---")

    uploaded_files = st.file_uploader(
        "📄 Upload WHO PDFs",
        type=["pdf"],
        accept_multiple_files=True
    )

    if uploaded_files:

        save_uploaded_files(uploaded_files)

        st.success("PDFs uploaded successfully")


    st.markdown("---")

    if st.button("🔄 Create Vector Database"):

        with st.spinner("Creating embeddings..."):

            docs = load_documents()
            chunks = split_documents(docs)
            create_vector_db(chunks)

        st.success("Vector Database Created")


    st.markdown("---")

    if st.button("🗑 Clear Chat"):

        st.session_state.messages = []
        st.session_state.last_answer = ""

        st.rerun()


# ---------------- HEADER ----------------
st.markdown(
"""
# 🌿 Arogya AI

### Multilingual Healthcare Assistant
"""
)

st.markdown(
"""
<div class="hero-box">

📚 WHO PDFs • ⚕ Medical Tools • 🤖 Groq AI

</div>
""",
unsafe_allow_html=True
)


# ---------------- CHAT HISTORY ----------------
for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        st.markdown(msg["content"])


# ---------------- INPUT ----------------
question = st.chat_input(
    "Ask your health question..."
)

if st.session_state.selected_question:

    question = st.session_state.selected_question

    st.session_state.selected_question = None


# ---------------- QUESTION PROCESSING ----------------
if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):

        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                answer = ask_question(question)

            except Exception as e:

                answer = f"Error: {str(e)}"

            st.markdown(answer)

            st.session_state.last_answer = answer

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )


# ---------------- SPEAK ANSWER ----------------
if st.session_state.last_answer:

    if st.button("🔊 Speak Last Answer"):

        text = st.session_state.last_answer.replace("`", "'")

        st.components.v1.html(
            f"""
            <script>
            var msg = new SpeechSynthesisUtterance(`{text}`);
            msg.rate = 1;
            msg.pitch = 1;
            msg.volume = 1;
            window.speechSynthesis.speak(msg);
            </script>
            """,
            height=0
        )


# ---------------- FOOTER ----------------
st.markdown("---")

st.markdown(
"""
<div class="disclaimer">

⚠ Educational purposes only • Consult a doctor for emergencies.

</div>

<div class="footer">

Powered by Streamlit • LangChain • Groq • FAISS

</div>
""",
unsafe_allow_html=True
)