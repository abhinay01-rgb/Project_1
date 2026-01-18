from langchain_openai import ChatOpenAI
from app.config import MODEL_FAST

llm = ChatOpenAI(model=MODEL_FAST, temperature=0)

def query_agent(state):
    prompt = f'''
    You are an academic query refinement agent.
    Convert the question into a precise academic search query.

    Question: {state.user_query}
    '''
    response = llm.invoke(prompt)
    state.refined_query = response.content
    return state