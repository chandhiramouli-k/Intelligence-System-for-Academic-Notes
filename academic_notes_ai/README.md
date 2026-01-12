# Academic Notes AI Assistant 🧠🤖

An intelligent RAG (Retrieval-Augmented Generation) system built to help students chat with their academic notes. This project uses **Groq** for lightning-fast inference and **HuggingFace** for local embeddings, ensuring high performance without hitting strict API limits.

## 🚀 Features
- **Ultra-Fast Responses:** Powered by Groq's LPU technology and Llama 3.
- **Cost-Efficient:** Uses local HuggingFace embeddings (`all-MiniLM-L6-v2`) to avoid Google Cloud/OpenAI costs.
- **Smart Retrieval:** Only pulls relevant sections from your `notes.txt` to answer questions.
- **Local Memory:** Saves processed notes in a `faiss_index` for instant loading on subsequent runs.

## 🛠️ Tech Stack
- **LLM:** Groq (Llama-3.3-70b)
- **Embeddings:** HuggingFace (Local)
- **Vector Store:** FAISS
- **Framework:** LangChain

## 📋 Prerequisites
- Python 3.10 or higher
- A Groq API Key (Get it at [console.groq.com](https://console.groq.com/))

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/academic_notes_ai.git](https://github.com/your-username/academic_notes_ai.git)
   cd academic_notes_ai
Install dependencies:

Bash

pip install langchain-groq langchain-huggingface sentence-transformers faiss-cpu python-dotenv
Configure Environment Variables: Create a .env file in the root directory and add your Groq API key:

Plaintext

GROQ_API_KEY=gsk_your_actual_key_here
Add Your Notes: Place your study material in data/notes.txt.

🏃 Usage
Run the application using the following command:

Bash

python -m app.main
Note: If you update your notes.txt, delete the faiss_index folder to allow the system to re-index your new content.