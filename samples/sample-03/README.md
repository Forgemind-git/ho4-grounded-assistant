# Sample 03 — Team Onboarding Buddy

**Domain:** Team wiki and runbooks

A grounded Q&A assistant that helps new engineers get answers from the team wiki — not from generic internet knowledge. Shows the difference between Claude guessing a generic process (BEFORE) vs. giving the actual team-specific steps (AFTER).

## Problem Statement

When a new engineer asks "How do I deploy to staging?" they need the team's specific command sequence, timing, and monitoring channel — not a generic CI/CD tutorial. An ungrounded LLM will invent plausible but wrong details. This sample shows how to ground Claude in your team wiki so it gives answers your team can actually use on day one.

## What's in this sample

```
sample-03/
├── grounded_qa.py       # Main script — runs BEFORE and AFTER demo
├── test_questions.txt   # 6 onboarding questions to test the assistant
├── requirements.txt     # anthropic
├── .env.example         # Copy to .env and add your API key
└── context/
    ├── policy.txt       # Engineering team wiki and runbooks
    └── instructions.txt # System instructions grounding Claude to the wiki
```

## Quick start

```bash
cd samples/sample-03
pip install -r requirements.txt
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY
export ANTHROPIC_API_KEY=your_key_here
python grounded_qa.py
```

## Expected output

```
QUESTION 2: Where are the database credentials?

[BEFORE] Without team wiki (Claude gives generic engineering advice):
  Database credentials should never be hardcoded. They are typically
  stored in environment variables or a secrets manager like AWS Secrets
  Manager, HashiCorp Vault, or a .env file...

[AFTER]  With team wiki and runbooks loaded:
  According to the Database Access runbook, connect using TablePlus
  (preferred) or psql. Credentials are stored in the team 1Password
  vault under "Dev DB". Ask your team lead for vault access on your
  first day. Production DB requires a separate "Prod DB" entry — request
  from the CTO.
```

## How to extend this

1. Replace `context/policy.txt` with your actual team wiki pages.
2. Add separate files per topic: `context/deployments.txt`, `context/oncall.txt`, `context/tools.txt`.
3. Update `test_questions.txt` with questions your new joiners actually ask.
4. The assistant will always point to your real Slack channels, tools, and people — not hypothetical ones.

## Key concept demonstrated

**Grounding** is critical for internal tools where the "right answer" is team-specific. Generic LLM knowledge produces plausible but wrong details. The grounded version cites your actual tool names, hosts, vaults, and channel names.
