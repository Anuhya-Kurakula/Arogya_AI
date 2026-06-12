from langchain_community.vectorstores import FAISS
from src.embeddings import get_embeddings


def create_vector_db(chunks):

    embeddings = get_embeddings()

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )

    vectorstore.save_local("vectorstore/faiss_index")


def load_vector_db():

    embeddings = get_embeddings()

    return FAISS.load_local(
        "vectorstore/faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )