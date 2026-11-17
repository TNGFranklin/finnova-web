"""Terminal chat with the FinNova Bank assistant.  Run: python chat.py"""
from finnova_rag.rag import FinNovaAssistant


def main() -> None:
    bot = FinNovaAssistant()
    print("FinNova Bank Assistant (local LLM). Type a question, or 'exit' to quit.\n")
    while True:
        try:
            question = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if question.lower() in {"exit", "quit", "q"}:
            break
        if not question:
            continue
        print("Assistant: ", end="", flush=True)
        stream = bot.stream(question)
        sources = []
        try:
            while True:
                print(next(stream), end="", flush=True)
        except StopIteration as done:
            sources = done.value or []
        print("\n  Sources: " + "; ".join(f"{s['file']} > {s['section']}" for s in sources) + "\n")


if __name__ == "__main__":
    main()
