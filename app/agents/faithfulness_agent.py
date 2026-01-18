from langchain_openai import ChatOpenAI
from app.config import MODEL_FAST

llm = ChatOpenAI(model=MODEL_FAST, temperature=0)

def faithfulness_agent(state):
    prompt = f'''
    Check whether the answer is fully grounded in the provided documents.
    Score between 0 and 1.

    Answer:
    {state.answer}

    Documents:
    {state.documents}
    '''

    response = llm.invoke(prompt)
    try:
        score = float(response.content.strip())
    except:
        score = 0.0

    state.faithfulness_score = score
    state.is_valid = score >= 0.95
    return state