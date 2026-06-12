from src.retriever import get_retriever
from src.llm import get_llm
from tools.medical_tools import check_medical_tools


def ask_question(question):

    # WHO PDFs
    try:

        retriever = get_retriever()

        docs = retriever.invoke(question)

        if docs:

            context = "\n\n".join(
                [doc.page_content for doc in docs]
            )

            llm = get_llm()

            prompt = f"""
You are Arogya AI.

IMPORTANT:
- Answer in the SAME language used by the user.
- Use simple language.
- Use only the context below.

Context:
{context}

Question:
{question}

Answer:
"""

            response = llm.invoke(prompt)

            answer = response.content

            if "I could not find" not in answer:

                return f"📚 WHO Documents\n\n{answer}"

    except Exception as e:

        print("RAG Error:", e)

    # Medical tools
    try:

        tool_response = check_medical_tools(question)

        if tool_response:

            return f"⚕ Medical Tool\n\n{tool_response}"

    except Exception as e:

        print("Tool Error:", e)

    # Groq fallback
    llm = get_llm()

    prompt = f"""
You are Arogya AI.

IMPORTANT:
- Reply in the SAME language as the user.
- Use easy words suitable for rural communities.
- Do not diagnose diseases.
- Suggest visiting a doctor for serious symptoms.

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    return f"🤖 AI Assistant\n\n{response.content}"