"""HTTP API so the FinNova app can talk to the assistant.

Run:  uvicorn server:app --port 8001
POST /ask         {"question": "..."}  ->  {"answer": "...", "sources": [{"file", "section"}]}
POST /ask/stream  same request, answer streamed as lines of JSON:
                  {"token": "..."} ... then {"sources": [...]}
"""
import asyncio
import json
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field

from finnova_rag import config
from finnova_rag.rag import FinNovaAssistant

_bot: FinNovaAssistant | None = None


def bot() -> FinNovaAssistant:
    global _bot
    if _bot is None:
        _bot = FinNovaAssistant()
    return _bot


@asynccontextmanager
async def lifespan(_: FastAPI):
    # Load the models in the background so the first real question is fast.
    async def warm() -> None:
        try:
            await asyncio.to_thread(lambda: bot().warm_up())
        except Exception:
            pass  # Ollama not running yet: questions will report it

    task = asyncio.create_task(warm())
    yield
    task.cancel()


app = FastAPI(title="FinNova Bank Assistant", version="1.1.0", lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080", "http://127.0.0.1:8080", "https://tngfranklin.github.io"],
    allow_origin_regex=r"http://(localhost|127\.0\.0\.1)(:\d+)?",
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


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


@app.post("/ask/stream")
def ask_stream(request: AskRequest) -> StreamingResponse:
    question = request.question.strip()

    def lines():
        stream = bot().stream(question)
        sources: list = []
        try:
            while True:
                yield json.dumps({"token": next(stream)}) + "\n"
        except StopIteration as done:
            sources = done.value or []
        except Exception as error:
            yield json.dumps({"error": f"Assistant unavailable: {error}"}) + "\n"
            return
        yield json.dumps({"sources": sources}) + "\n"

    return StreamingResponse(lines(), media_type="application/x-ndjson")
