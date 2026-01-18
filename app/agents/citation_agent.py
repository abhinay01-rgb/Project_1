def citation_agent(state):
    if not state.citations:
        state.is_valid = False
    return state