"""HTTP API so the FinNova app can talk to the assistant.

Run:  uvicorn server:app --port 8001
POST /ask  {"question": "..."}  ->  {"answer": "...", "sources": [{"file", "section"}]}
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from finnova_rag import config
from finnova_rag.rag import FinNovaAssistant

app = FastAPI(title="FinNova Bank Assistant", version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080", "http://127.0.0.1:8080", "https://tngfranklin.github.io"],
    allow_origin_regex=r"http://(localhost|127\.0\.0\.1)(:\d+)?",
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

_bot: FinNovaAssistant | None = None


def bot() -> FinNovaAssistant:
    global _bot
    if _bot is None:
        _bot = FinNovaAssistant()
    return _bot


class AskRequest(BaseModel):
    question: str = Field(min_length=2, max_length=500)


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "chat_model": config.CHAT_MODEL, "embed_model": config.EMBED_MODEL}


@app.post("/ask")
def ask(request: AskRequest) -> dict:
    try:
        answer = bot().ask(request.question.strip())
    except Exception as error:  # Ollama stopped, or the index was never built
        raise HTTPException(status_code=503, detail=f"Assistant unavailable: {error}") from error
    return {"answer": answer.text, "sources": answer.sources}
