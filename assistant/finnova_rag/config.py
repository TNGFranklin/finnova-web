"""Settings for the FinNova assistant. Override any of them with environment variables."""
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Where the banking policy documents live, and where the vector database is stored.
DOCS_DIR = Path(os.getenv("FINNOVA_DOCS_DIR", ROOT / "docs"))
VECTOR_DIR = Path(os.getenv("FINNOVA_VECTOR_DIR", ROOT / "chroma_db"))
COLLECTION = "finnova_policies"

# Local models served by Ollama.
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://127.0.0.1:11434")
CHAT_MODEL = os.getenv("FINNOVA_CHAT_MODEL", "llama3.2:3b")
EMBED_MODEL = os.getenv("FINNOVA_EMBED_MODEL", "nomic-embed-text")

# Chunking and retrieval.
CHUNK_SIZE = 900
CHUNK_OVERLAP = 120
TOP_K = 5

# Speed. On a CPU most of the wait is the model reading the prompt, so a
# shorter prompt and a capped answer length matter most. Keeping the models in
# memory avoids reloading them for every question.
NUM_CTX = 3072
MAX_ANSWER_TOKENS = 300
KEEP_ALIVE = 1800  # seconds
