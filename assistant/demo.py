"""Runs a fixed set of questions and writes the transcript to DEMO.md.  Run: python demo.py"""
import time
from datetime import date

from finnova_rag import config
from finnova_rag.rag import FinNovaAssistant

QUESTIONS = [
    "What is the fee for adding money with a card?",
    "How much does it cost to pay a 40 euro bill?",
    "What happens after I enter the wrong password five times?",
    "Which currencies can I hold in my FinNova account?",
    "How do I send money to an M-Pesa number, and what does it cost?",
    "Can I connect MetaMask inside the Android app?",
    "What are the common reasons a payment is declined?",
    "Do you offer mortgages?",
    "What is the capital of France?",
]


def main() -> None:
    bot = FinNovaAssistant()
    lines = [
        "# FinNova Bank Assistant: chatbot demo",
        "",
        f"Generated {date.today()} with `{config.CHAT_MODEL}` (chat) and `{config.EMBED_MODEL}` "
        "(embeddings) running locally in Ollama. Answers come only from the policy documents in `docs/`.",
        "",
    ]
    for number, question in enumerate(QUESTIONS, 1):
        start = time.time()
        answer = bot.ask(question)
        seconds = time.time() - start
        print(f"[{number}/{len(QUESTIONS)}] {question} ({seconds:.0f}s)")
        sources = "; ".join(f"{s['file']} > {s['section']}" for s in answer.sources)
        lines += [
            f"## {number}. {question}",
            "",
            answer.text,
            "",
            f"*Sources: {sources}. Answered in {seconds:.0f} s.*",
            "",
        ]
    with open("DEMO.md", "w", encoding="utf-8") as out:
        out.write("\n".join(lines))
    print("Wrote DEMO.md")


if __name__ == "__main__":
    main()
