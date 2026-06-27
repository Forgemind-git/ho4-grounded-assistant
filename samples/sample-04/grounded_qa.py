"""
Compliance SOP Assistant — Grounded Q&A Demo
=============================================
Demonstrates the difference between asking Claude with no context (BEFORE)
vs. grounding it in the organisation's Standard Operating Procedure (AFTER).

Compliance answers MUST come from the actual SOP document — not from Claude's
general knowledge of GDPR or data protection law. This demo shows the difference.

Usage:
    pip install anthropic
    export ANTHROPIC_API_KEY=your_key_here
    python grounded_qa.py
"""

import os
import sys
from pathlib import Path

try:
    import anthropic
except ImportError:
    print("ERROR: anthropic package not installed. Run: pip install anthropic")
    sys.exit(1)

MODEL = "claude-haiku-3-5-20251001"
CONTEXT_DIR = Path(__file__).parent / "context"
QUESTIONS_FILE = Path(__file__).parent / "test_questions.txt"


def load_context(context_dir: Path) -> tuple[str, str]:
    """
    Load all .txt files from the context directory.
    Returns (content_context, instructions) as a tuple.
    instructions.txt is the system prompt; all other files are context documents.
    """
    if not context_dir.exists():
        raise FileNotFoundError(f"Context directory not found: {context_dir}")

    txt_files = sorted(context_dir.glob("*.txt"))
    if not txt_files:
        raise ValueError(f"No .txt files found in {context_dir}")

    print(f"Loading SOP documents from {len(txt_files)} file(s):")

    instructions = ""
    content_parts = []

    for filepath in txt_files:
        content = filepath.read_text(encoding="utf-8").strip()
        print(f"  - {filepath.name} ({len(content)} chars)")
        if filepath.name == "instructions.txt":
            instructions = content
        else:
            content_parts.append(f"=== {filepath.name} ===\n{content}")

    return "\n\n".join(content_parts), instructions


def load_questions(questions_file: Path) -> list[str]:
    """Load test questions from file, one per line."""
    if not questions_file.exists():
        raise FileNotFoundError(f"Questions file not found: {questions_file}")
    lines = questions_file.read_text(encoding="utf-8").splitlines()
    return [line.strip() for line in lines if line.strip()]


def ask_without_context(client: anthropic.Anthropic, question: str) -> str:
    """Ask Claude a question with NO SOP context (the BEFORE demo)."""
    try:
        response = client.messages.create(
            model=MODEL,
            max_tokens=300,
            messages=[{"role": "user", "content": question}],
        )
        return response.content[0].text.strip()
    except anthropic.APIError as e:
        return f"[API Error: {e}]"


def ask_with_context(
    client: anthropic.Anthropic, question: str, context: str, instructions: str
) -> str:
    """Ask Claude a question grounded in the SOP documents (the AFTER demo)."""
    system_prompt = f"""{instructions}

--- COMPLIANCE SOP DOCUMENTS ---
{context}
--- END OF SOP DOCUMENTS ---
"""
    try:
        response = client.messages.create(
            model=MODEL,
            max_tokens=300,
            system=system_prompt,
            messages=[{"role": "user", "content": question}],
        )
        return response.content[0].text.strip()
    except anthropic.APIError as e:
        return f"[API Error: {e}]"


def print_separator(char: str = "─", width: int = 70) -> None:
    print(char * width)


def run_demo() -> None:
    """Run the BEFORE/AFTER grounded Q&A demonstration."""
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY environment variable not set.")
        print("Copy .env.example to .env and add your key, or export it directly.")
        sys.exit(1)

    print()
    print_separator("═")
    print("  COMPLIANCE SOP ASSISTANT — Grounded Q&A Demo")
    print_separator("═")
    print()

    print("Initialising...")
    try:
        full_context, instructions = load_context(CONTEXT_DIR)
        questions = load_questions(QUESTIONS_FILE)
    except (FileNotFoundError, ValueError) as e:
        print(f"ERROR: {e}")
        sys.exit(1)

    if not instructions:
        instructions = (
            "You are a Compliance SOP Assistant. Answer questions using ONLY "
            "the provided SOP documents. If the answer is not in the documents, "
            "escalate to the DPO. Never guess at regulatory requirements."
        )

    client = anthropic.Anthropic(api_key=api_key)

    print(f"\nRunning demo on {len(questions)} question(s) using model: {MODEL}")
    print()

    for i, question in enumerate(questions, start=1):
        print_separator()
        print(f"QUESTION {i}: {question}")
        print_separator()

        print("\n[BEFORE] Without SOP context (Claude guesses from general GDPR knowledge):")
        before_answer = ask_without_context(client, question)
        for line in before_answer.split("\n"):
            print(f"  {line}")

        print("\n[AFTER]  With SOP documents loaded (cites the actual organisational rule):")
        after_answer = ask_with_context(client, question, full_context, instructions)
        for line in after_answer.split("\n"):
            print(f"  {line}")
        print()

    print_separator("═")
    print("  Demo complete.")
    print("  BEFORE: Claude cites general GDPR law — accurate but not your SOP.")
    print("  AFTER:  Claude cites your specific SOP rules, timelines, and owners.")
    print()
    print("  WARNING: This demo is for educational purposes only.")
    print("  Always consult your DPO for actual compliance decisions.")
    print_separator("═")
    print()


if __name__ == "__main__":
    run_demo()
