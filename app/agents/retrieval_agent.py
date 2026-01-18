from app.rag.retriever import hybrid_retriever

def retrieval_agent(state):
    docs = hybrid_retriever(state.refined_query)
    state.documents = docs
    return state