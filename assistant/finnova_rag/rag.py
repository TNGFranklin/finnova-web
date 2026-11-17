"""Retrieval augmented generation: find relevant policy passages, then let the
local LLM answer using only those passages."""
from dataclasses import dataclass, field

from langchain_chroma import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

from . import config
from .ingest import embeddings

SYSTEM_PROMPT = """You are the FinNova Bank assistant. You answer customer questions about FinNova \
Wallet's banking policies and services.

Rules:
- Use ONLY the context below. Do not use outside knowledge and do not guess.
- If the context does not contain the answer, say: "I don't have that information in the FinNova \
policy documents." and suggest contacting support. Do not invent fees, limits or features.
- Quote exact numbers (fees, limits, times) from the context.
- When the question asks for reasons or options, list every one that the context gives.
- Be short and clear: a direct answer first, then any detail that helps. Use a short list for steps.
- You cannot see or change the customer's account, and you give no personal investment advice.
- Never ask for passwords, one-time codes or seed phrases.

Context:
{context}"""

PROMPT = ChatPromptTemplate.from_messages([("system", SYSTEM_PROMPT), ("human", "{question}")])


@dataclass
class Answer:
    text: str
    sources: list[dict] = field(default_factory=list)


class FinNovaAssistant:
    def __init__(self) -> None:
        self.store = Chroma(
            collection_name=config.COLLECTION,
            embedding_function=embeddings(),
            persist_directory=str(config.VECTOR_DIR),
        )
        self.llm = ChatOllama(
            model=config.CHAT_MODEL, base_url=config.OLLAMA_URL, temperature=0, num_ctx=4096
        )
        self.chain = PROMPT | self.llm | StrOutputParser()

    def retrieve(self, question: str):
        return self.store.similarity_search(question, k=config.TOP_K)

    @staticmethod
    def _context(docs) -> str:
        return "\n\n---\n\n".join(d.page_content for d in docs)

    @staticmethod
    def _sources(docs) -> list[dict]:
        seen, out = set(), []
        for d in docs:
            key = (d.metadata["source"], d.metadata.get("section", ""))
            if key not in seen:
                seen.add(key)
                out.append({"file": key[0], "section": key[1]})
        return out

    def ask(self, question: str) -> Answer:
        docs = self.retrieve(question)
        text = self.chain.invoke({"context": self._context(docs), "question": question})
        return Answer(text.strip(), self._sources(docs))

    def stream(self, question: str):
        """Yield answer text pieces as the model writes them, then return the sources."""
        docs = self.retrieve(question)
        for piece in self.chain.stream({"context": self._context(docs), "question": question}):
            yield piece
        return self._sources(docs)
