from app.agents.orchestrator import build_graph
from app.state import AgentState

if __name__ == "__main__":
    graph = build_graph()

    state = AgentState(
        user_query="Explain backpropagation in neural networks"
    )

    result = graph.invoke(state)

    print("\nAnswer:\n", result.answer)
    print("\nCitations:", result.citations)
    print("\nFaithfulness:", result.faithfulness_score)