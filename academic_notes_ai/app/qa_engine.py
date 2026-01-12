from langchain_google_genai import ChatGoogleGenerativeAI
# NEW
from langchain_classic.chains import RetrievalQA
from .prompt import get_custom_prompt

def get_qa_chain(vector_store):
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)
    
    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vector_store.as_retriever(),
        chain_type_kwargs={"prompt": get_custom_prompt()}
    )
