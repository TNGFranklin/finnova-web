"""Settings for the FinNova assistant. Override any of them with environment variables."""
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Where the banking policy documents live, and where the vector database is stored.
DOCS_DIR = Path(os.getenv("FINNOVA_DOCS_DIR", ROOT / "docs"))
VECTOR_DIR = Path(os.getenv("FINNOVA_VECTOR_DIR", ROOT / "chroma_db"))
COLLECTION = "finnova_policies"

# Local models served by Ollama.
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
CHAT_MODEL = os.getenv("FINNOVA_CHAT_MODEL", "llama3.2:3b")
EMBED_MODEL = os.getenv("FINNOVA_EMBED_MODEL", "nomic-embed-text")

# Chunking and retrieval.
CHUNK_SIZE = 900
CHUNK_OVERLAP = 120
TOP_K = 6
