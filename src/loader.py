from langchain_community.document_loaders import PyPDFDirectoryLoader


def load_documents():

    loader = PyPDFDirectoryLoader(
        "data/documents"
    )

    documents = loader.load()

    return documents