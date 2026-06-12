from src.vector_db import load_vector_db


def get_retriever():

    db = load_vector_db()

    return db.as_retriever(search_kwargs={"k": 3})