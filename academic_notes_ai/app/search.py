from .embed_store import load_vector_store

def get_relevant_context(query, k=3):
    """
    Searches the vector database for the top 'k' most relevant 
    text chunks based on the user's query.
    """
    try:
        # 1. Load the FAISS database from the 'embeddings/' folder
        vector_db = load_vector_store()

        # 2. Perform Similarity Search
        # This converts the query into a vector and finds the nearest neighbors
        docs = vector_db.similarity_search(query, k=k)

        return docs
        
    except Exception as e:
        print(f"Error during search: {e}")
        return []

if __name__ == "__main__":
    # Testing the search independently
    test_query = "What is the main topic of the first chapter?"
    results = get_relevant_context(test_query)
    
    print(f"Found {len(results)} relevant chunks:")
    for i, doc in enumerate(results):
        print(f"\nChunk {i+1}:")
        print(doc.page_content[:200] + "...") # Print first 200 chars