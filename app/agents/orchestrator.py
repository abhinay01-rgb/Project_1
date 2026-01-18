from langgraph.graph import StateGraph
from app.state import AgentState

from app.agents.query_agent import query_agent
from app.agents.retrieval_agent import retrieval_agent
from app.agents.synthesis_agent import synthesis_agent
from app.agents.faithfulness_agent import faithfulness_agent
from app.agents.citation_agent import citation_agent

def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("query", query_agent)
    graph.add_node("retrieve", retrieval_agent)
    graph.add_node("synthesize", synthesis_agent)
    graph.add_node("faithfulness", faithfulness_agent)
    graph.add_node("citation", citation_agent)

    graph.set_entry_point("query")
    graph.add_edge("query", "retrieve")
    graph.add_edge("retrieve", "synthesize")
    graph.add_edge("synthesize", "faithfulness")
    graph.add_edge("faithfulness", "citation")

    graph.set_finish_point("citation")
    return graph.compile()