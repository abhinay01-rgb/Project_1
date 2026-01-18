import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

MODEL_REASONING = "gpt-4.1"
MODEL_FAST = "gpt-4o-mini"
EMBEDDING_MODEL = "text-embedding-3-large"