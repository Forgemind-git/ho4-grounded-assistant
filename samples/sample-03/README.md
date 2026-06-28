# HO4 Sample 3 — Team Onboarding Buddy

**Domain:** Team wiki and runbooks

A grounded Q&A assistant that helps new engineers get answers from the team wiki — not from
generic internet knowledge. It shows the difference between Claude guessing a generic process
(BEFORE) and giving the actual team-specific steps, tools, and people (AFTER).

## Use it with your Claude.ai subscription
No API key needed. Just your normal Claude.ai login (Projects is available on Claude Pro
or Team). A richer click-by-click walkthrough is in this folder's **`index.html`** (open it in
a browser).

1. Open **claude.ai** and sign in.
2. In the left sidebar click **Projects**, then **+ New Project**. Name it `Team Onboarding Buddy`.
3. Click **Add content** → **Upload files** and upload **`context/policy.txt`** from this folder.
4. Click **Set project instructions** and paste the example prompt below. Click **Save**.
5. Start a new chat **inside the project** and ask the questions in **`test_questions.txt`**.
   Answers should cite the wiki or runbook; anything not in the docs should send the joiner to
   your team Slack channel.

## The example prompt
Paste this into the Project's **instructions** field (it's the content of
`context/instructions.txt`):

```
You are a Team Onboarding Buddy for the engineering team.

You help new team members get up to speed by answering questions using ONLY the team wiki and runbooks provided in your context.

Rules you must follow:
1. If the answer is in the wiki, give a clear and helpful answer, citing the relevant section (e.g. "According to the Deployment runbook...").
2. If the answer is NOT in the wiki, say: "That's not covered in the current team wiki. I'd recommend asking in #engineering on Slack or checking with your team lead."
3. Never invent tooling, processes, or people that are not mentioned in the documents.
4. Be friendly and welcoming — the reader is new to the team.
5. When referencing Slack channels, use the # prefix (e.g. #on-call).
```

## Before vs after
**Question:** "Where are the database credentials?"

- **BEFORE (ungrounded):** "Credentials are typically stored in environment variables or a
  secrets manager like AWS Secrets Manager, Vault, or a .env file…" → generic, not actionable.
- **AFTER (grounded):** "Per the Database Access runbook, connect with TablePlus or psql;
  credentials are in the team 1Password vault under 'Dev DB' — ask your team lead for vault
  access on day one." → the real, usable answer.

## Make it your own
- Replace `context/policy.txt` with your actual wiki pages and runbooks.
- Add more files to the Project (deployments, on-call, tools).
- Update the team name and Slack channel in the instructions.

## Optional — automate it with the API (advanced)
You do **not** need this for the course. The `grounded_qa.py` script in this folder runs the
same BEFORE/AFTER demo from Python. It needs an Anthropic API key (separate from your Claude.ai
subscription, so it costs money) and is only for developers who want to script the pattern.

```bash
cd samples/sample-03
pip install -r requirements.txt
cp .env.example .env          # add your ANTHROPIC_API_KEY
export ANTHROPIC_API_KEY=your_key_here
python grounded_qa.py
```

## Key concept demonstrated
**Grounding** is critical for internal tools where the "right answer" is team-specific. Generic
LLM knowledge produces plausible but wrong details; the grounded version cites your actual tool
names, hosts, vaults, and channel names.
