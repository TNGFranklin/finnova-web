# FinNova Bank Assistant (RAG on a local LLM)

An AI financial assistant that answers customer questions about FinNova Bank's policies and services. It uses Retrieval Augmented Generation: the banking policy documents are split, embedded and stored in a vector database, the passages most relevant to a question are retrieved, and a local LLM writes an answer from those passages only. Nothing leaves the computer.

| Part | Choice |
|------|--------|
| Orchestration | LangChain (LCEL prompt, model and parser chain) |
| Vector database | ChromaDB (persisted in `chroma_db/`) |
| Embeddings | `nomic-embed-text` through Ollama |
| LLM | `llama3.2:3b` through Ollama (runs on CPU) |
| API | FastAPI (`server.py`) |

## How it works

```
docs/*.md ──split by heading, then by size──> chunks ──nomic-embed-text──> ChromaDB
question ──embed──> top 6 similar chunks ──> prompt (rules + context + question) ──> llama3.2 ──> answer + sources
```

1. `finnova_rag/ingest.py` reads the 7 policy documents in `docs/`, splits each by Markdown heading and then into chunks of about 900 characters (120 overlap), prefixes each chunk with its heading, and stores the embeddings.
2. `finnova_rag/rag.py` embeds the question, retrieves the 6 closest chunks, and asks the LLM to answer using only that context. The system prompt tells it to quote exact numbers, to say "I don't have that information" when the documents do not cover a question, and never to ask for passwords or one-time codes.
3. Every answer returns the source files and sections it was based on.

## Setup (Windows)

```bash
winget install Ollama.Ollama
ollama pull llama3.2:3b
ollama pull nomic-embed-text
cd assistant
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
```

ChromaDB needs the Microsoft Visual C++ runtime (`winget install Microsoft.VCRedist.2015+.x64`).

## Run

```bash
.venv\Scripts\python -m finnova_rag.ingest     # build the vector database (re-run after editing docs/)
.venv\Scripts\python chat.py                   # chat in the terminal
.venv\Scripts\python demo.py                   # run the demo questions and write DEMO.md
.venv\Scripts\python -m uvicorn server:app --port 8001   # HTTP API for the app
```

API: `POST http://localhost:8001/ask` with `{"question": "..."}` returns `{"answer": "...", "sources": [{"file", "section"}]}`. `GET /health` reports the models in use.

Settings (models, folders, Ollama address) can be changed with environment variables listed in `finnova_rag/config.py`, for example `FINNOVA_CHAT_MODEL=qwen2.5:3b`.

## Demo

`DEMO.md` holds a recorded Q&A run: fees, limits, sign-in rules, currencies, mobile money, the blockchain limitation on Android, a question the documents answer only by omission (mortgages), and an unrelated question the assistant correctly declines.

## Limits

- It answers from the documents only. It cannot see a customer's balance or transactions.
- A 3B model on CPU takes 10 to 35 seconds per answer. A larger model or a GPU would be faster or more accurate.
- The policy documents describe the FinNova Wallet demo app, which runs in sandbox mode.
