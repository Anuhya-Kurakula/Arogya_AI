import os


def save_uploaded_files(uploaded_files):

    os.makedirs("data/documents", exist_ok=True)

    for file in uploaded_files:

        file_path = os.path.join(
            "data/documents",
            file.name
        )

        with open(file_path, "wb") as f:
            f.write(file.getbuffer())