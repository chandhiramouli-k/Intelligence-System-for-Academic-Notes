from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_notes(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def split_notes(text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=80
    )
    return text_splitter.split_text(text)