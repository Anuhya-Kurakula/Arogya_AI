from langchain.prompts import PromptTemplate


prompt = PromptTemplate(
    template="""
Answer the question only from the provided context.

Context:
{context}

Question:
{question}

Answer:
""",
    input_variables=["context", "question"]
)