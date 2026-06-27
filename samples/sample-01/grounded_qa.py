"""
HR Policy Assistant — Grounded Q&A Demo
========================================
Demonstrates the difference between asking Claude with no context (BEFORE)
vs. grounding it in the company HR policy documents (AFTER).

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


def load_context(context_dir: Path) -> str:
    """Load all .txt files from the context directory into a single string."""
    if not context_dir.exists():
        raise FileNotFoundError(f"Context directory not found: {context_dir}")

    context_parts = []
    txt_files = sorted(context_dir.glob("*.txt"))

    if not txt_files:
        raise ValueError(f"No .txt files found in {context_dir}")

    print(f"Loading context from {len(txt_files)} file(s):")
    for filepath in txt_files:
        content = filepath.read_text(encoding="utf-8").strip()
        context_parts.append(f"=== {filepath.name} ===\n{content}")
        print(f"  - {filepath.name} ({len(content)} chars)")

    return "\n\n".join(context_parts)


def load_questions(questions_file: Path) -> list[str]:
    """Load test questions from file, one per line."""
    if not questions_file.exists():
        raise FileNotFoundError(f"Questions file not found: {questions_file}")

    lines = questions_file.read_text(encoding="utf-8").splitlines()
    questions = [line.strip() for line in lines if line.strip()]
    return questions


def ask_without_context(client: anthropic.Anthropic, question: str) -> str:
    """Ask Claude a question with NO company context (the BEFORE demo)."""
    try:
        response = client.messages.create(
            model=MODEL,
            max_tokens=300,
            messages=[
                {
                    "role": "user",
                    "content": question,
                }
            ],
        )
        return response.content[0].text.strip()
    except anthropic.APIError as e:
        return f"[API Error: {e}]"


def ask_with_context(client: anthropic.Anthropic, question: str, context: str, instructions: str) -> str:
    """Ask Claude a question WITH company context grounded in the system prompt (the AFTER demo)."""
    system_prompt = f"""{instructions}

--- COMPANY DOCUMENTS ---
{context}
--- END OF DOCUMENTS ---
"""
    try:
        response = client.messages.create(
            model=MODEL,
            max_tokens=300,
            system=system_prompt,
            messages=[
                {
                    "role": "user",
                    "content": question,
                }
            ],
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
    print("  HR POLICY ASSISTANT — Grounded Q&A Demo")
    print_separator("═")
    print()

    # Load context and instructions
    print("Initialising...")
    try:
        full_context = load_context(CONTEXT_DIR)
        questions = load_questions(QUESTIONS_FILE)

        # Load instructions separately (instructions.txt is part of context dir)
        instructions_path = CONTEXT_DIR / "instructions.txt"
        if instructions_path.exists():
            instructions = instructions_path.read_text(encoding="utf-8").strip()
            # Remove instructions from the context block so they aren't duplicated
            full_context = "\n\n".join(
                part for part in full_context.split("\n\n")
                if "instructions.txt" not in part.split("\n")[0]
            )
        else:
            instructions = (
                "You are an HR Policy Assistant. Answer questions using only the "
                "provided company documents. If the answer is not in the documents, "
                "say so clearly."
            )
    except (FileNotFoundError, ValueError) as e:
        print(f"ERROR: {e}")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)

    print(f"\nRunning demo on {len(questions)} question(s) using model: {MODEL}")
    print()

    for i, question in enumerate(questions, start=1):
        print_separator()
        print(f"QUESTION {i}: {question}")
        print_separator()

        print("\n[BEFORE] Without company context (Claude guesses from general knowledge):")
        before_answer = ask_without_context(client, question)
        print(f"  {before_answer}")

        print("\n[AFTER]  With HR policy documents loaded:")
        after_answer = ask_with_context(client, question, full_context, instructions)
        print(f"  {after_answer}")
        print()

    print_separator("═")
    print("  Demo complete.")
    print("  The AFTER answers are grounded in the actual company policy,")
    print("  while the BEFORE answers are generic guesses from Claude's training data.")
    print_separator("═")
    print()


if __name__ == "__main__":
    run_demo()
