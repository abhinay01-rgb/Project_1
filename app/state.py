from typing import List, Dict, Optional
from pydantic import BaseModel

class AgentState(BaseModel):
    user_query: str
    refined_query: Optional[str] = None
    documents: List[Dict] = []
    answer: Optional[str] = None
    citations: List[str] = []
    faithfulness_score: Optional[float] = None
    is_valid: bool = False