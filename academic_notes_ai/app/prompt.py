# NEW
from langchain_core.prompts import PromptTemplate

def get_custom_prompt():
    template = """
    You are an Academic AI. Use ONLY the notes provided below.
    
    Rules:
    - If the answer isn't in the context, say "Information not available in notes."
    - Do not use your own internal knowledge.
    - Be precise and academic.

    Context: {context}
    Question: {question}

    Answer:"""
    return PromptTemplate(template=template, input_variables=["context", "question"])