"""Load the policy documents, split them, embed them and store them in ChromaDB."""
import shutil
import sys

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter

from . import config


def embeddings() -> OllamaEmbeddings:
    return OllamaEmbeddings(model=config.EMBED_MODEL, base_url=config.OLLAMA_URL)


def load_chunks() -> list[Document]:
    """Split every markdown file by heading first, then into size-bounded chunks.

    Each chunk keeps its source file and section heading in metadata, and the
    heading is repeated at the top of the chunk text so the embedding knows
    what the passage is about.
    """
    by_heading = MarkdownHeaderTextSplitter(
        headers_to_split_on=[("#", "title"), ("##", "section")], strip_headers=False
    )
    by_size = RecursiveCharacterTextSplitter(
        chunk_size=config.CHUNK_SIZE, chunk_overlap=config.CHUNK_OVERLAP
    )
    chunks: list[Document] = []
    for path in sorted(config.DOCS_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        for section in by_heading.split_text(text):
            title = section.metadata.get("title", path.stem)
            heading = section.metadata.get("section", "")
            for piece in by_size.split_text(section.page_content):
                label = f"{title} > {heading}" if heading else title
                chunks.append(
                    Document(
                        page_content=f"[{label}]\n{piece}",
                        metadata={"source": path.name, "title": title, "section": heading},
                    )
                )
    return chunks


def build_index(reset: bool = True) -> int:
    """(Re)build the vector database. Returns the number of chunks stored."""
    chunks = load_chunks()
    if not chunks:
        raise SystemExit(f"No .md documents found in {config.DOCS_DIR}")
    if reset and config.VECTOR_DIR.exists():
        shutil.rmtree(config.VECTOR_DIR)
    Chroma.from_documents(
        chunks,
        embeddings(),
        collection_name=config.COLLECTION,
        persist_directory=str(config.VECTOR_DIR),
    )
    return len(chunks)


def main() -> None:
    files = len(list(config.DOCS_DIR.glob("*.md")))
    print(f"Reading {files} documents from {config.DOCS_DIR}")
    count = build_index()
    print(f"Stored {count} chunks in {config.VECTOR_DIR} using {config.EMBED_MODEL}")


if __name__ == "__main__":
    sys.exit(main())
