# Sample 02 — Product Support Assistant

**Domain:** SaaS product documentation

A grounded Q&A assistant that answers user support questions using only the product documentation. Shows the difference between Claude giving generic SaaS advice (BEFORE) vs. citing the exact steps from your docs (AFTER).

## Problem Statement

When users ask "How do I get an API key?" an ungrounded Claude will describe a generic process — but your product's steps, URL paths, and edge cases (like "the key is only shown once") are product-specific facts that must come from your actual docs. This sample shows how to ground Claude so it answers accurately using your documentation.

## What's in this sample

```
sample-02/
├── grounded_qa.py       # Main script — runs BEFORE and AFTER demo
├── test_questions.txt   # 6 support questions to test the assistant
├── requirements.txt     # anthropic
├── .env.example         # Copy to .env and add your API key
└── context/
    ├── policy.txt       # Acme SaaS product documentation
    └── instructions.txt # System instructions grounding Claude to the docs
```

## Quick start

```bash
cd samples/sample-02
pip install -r requirements.txt
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY
export ANTHROPIC_API_KEY=your_key_here
python grounded_qa.py
```

## Expected output

```
QUESTION 3: How do I get an API key?

[BEFORE] Without product documentation (Claude guesses generically):
  To get an API key, you typically need to navigate to your account
  settings or developer portal. Look for an "API" or "Developer" section...

[AFTER]  With product documentation loaded:
  To get an API key in Acme SaaS:
  1. Go to Settings > Integrations > API Keys.
  2. Click Generate New Key.
  3. Copy the key immediately — it is shown only once and cannot be
     retrieved again.
  4. Store it securely (e.g. in an environment variable or secrets manager).
```

## How to extend this

1. Replace `context/policy.txt` with your actual product help docs.
2. Add more files to `context/` (e.g. `billing.txt`, `troubleshooting.txt`).
3. Update `test_questions.txt` with real questions from your support tickets.
4. Adjust `context/instructions.txt` to match your product name and support email.

## Key concept demonstrated

**Grounding** forces Claude to answer from your specific documentation rather than generic software knowledge. Critical product details — exact navigation paths, one-time actions, processing times — only appear correctly when the model has the actual source.
