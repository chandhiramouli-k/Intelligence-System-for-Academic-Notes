import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_classic.chains import RetrievalQA
from .chunking import load_notes, split_notes
from .embed_store import create_vector_store, load_vector_store

load_dotenv()

# Initialize Groq (Lightning fast, much higher limits than Google)
llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    temperature=0,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

def run_system():
    index_path = "faiss_index"
    notes_path = "data/notes.txt"
    
    if os.path.exists(index_path):
        print("📂 Loading index...")
        vector_db = load_vector_store()
    else:
        print("🆕 Building local index...")
        text = load_notes(notes_path)
        chunks = split_notes(text)
        vector_db = create_vector_store(chunks)

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vector_db.as_retriever()
    )

    print("\n--- Groq Intelligence System Ready ---")
    while True:
        query = input("\nQuestion (or 'exit'): ")
        if query.lower() in ['exit', 'quit']: break
        if not query.strip(): continue

        response = qa_chain.invoke({"query": query})
        print(f"\nAI Answer: {response['result']}")

if __name__ == "__main__":
    run_system()