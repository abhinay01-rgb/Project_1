from langchain_openai import OpenAIEmbeddings
from app.config import EMBEDDING_MODEL

embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)