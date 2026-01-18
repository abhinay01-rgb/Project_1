from langchain_openai import ChatOpenAI
from app.config import MODEL_REASONING

llm = ChatOpenAI(model=MODEL_REASONING, temperature=0)

def synthesis_agent(state):
    context = "\n\n".join(
        [f"[{i}] {doc['content']}" for i, doc in enumerate(state.documents)]
    )

    prompt = f'''
    Answer the question using ONLY the provided sources.
    Provide clear explanations suitable for students.

    Question: {state.user_query}

    Sources:
    {context}
    '''

    response = llm.invoke(prompt)
    state.answer = response.content
    state.citations = [f"[{i}]" for i in range(len(state.documents))]
    return state