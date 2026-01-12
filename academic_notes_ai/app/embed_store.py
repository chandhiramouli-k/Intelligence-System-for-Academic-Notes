import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# This runs LOCALLY on your CPU. No API keys needed, no limits!
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def create_vector_store(chunks):
    vector_db = FAISS.from_texts(chunks, embeddings)
    vector_db.save_local("faiss_index")
    return vector_db

def load_vector_store():
    return FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)