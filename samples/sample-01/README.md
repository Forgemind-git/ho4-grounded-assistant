# Sample 01 — HR Policy Assistant

**Domain:** HR leave and expense policies

A grounded Q&A assistant that answers employee questions using only the company HR policy documents. Shows the difference between Claude guessing from general knowledge (BEFORE) vs. citing the actual policy (AFTER).

## Problem Statement

When employees ask HR questions like "Can I carry over leave?" or "Do I need a receipt for lunch?", an ungrounded LLM will guess based on generic HR norms — which may be wrong for your company. This sample shows how to ground Claude in your specific policy documents so every answer traces back to a real rule.

## What's in this sample

```
sample-01/
├── grounded_qa.py       # Main script — runs BEFORE and AFTER demo
├── test_questions.txt   # 6 questions to test the assistant
├── requirements.txt     # anthropic
├── .env.example         # Copy to .env and add your API key
└── context/
    ├── policy.txt       # ACME Corp HR leave and expense policy
    └── instructions.txt # System instructions grounding Claude to the docs
```

## Quick start

```bash
cd samples/sample-01
pip install -r requirements.txt
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY
export ANTHROPIC_API_KEY=your_key_here
python grounded_qa.py
```

## Expected output

For each test question you will see two answers side by side:

```
QUESTION 1: How many days annual leave do I get?

[BEFORE] Without company context (Claude guesses from general knowledge):
  The typical standard in many companies is around 10–15 days of paid
  annual leave, but this varies widely by employer and country...

[AFTER]  With HR policy documents loaded:
  According to the ACME Corp HR Policy, you are entitled to 18 days of
  paid annual leave per calendar year. [policy.txt — Annual Leave]
```

The BEFORE answer is a generic guess. The AFTER answer cites the exact rule from the loaded document.

## How to extend this

1. Replace `context/policy.txt` with your real HR policy document.
2. Adjust `context/instructions.txt` to match your company's tone.
3. Add more `.txt` files to `context/` (e.g. `benefits.txt`, `code_of_conduct.txt`) — the script loads all of them automatically.
4. Update `test_questions.txt` with questions your employees actually ask.

## Key concept demonstrated

**Grounding** = loading authoritative documents into the system prompt so Claude answers from facts, not guesses. The model cannot contradict the context or hallucinate policies that aren't there.
