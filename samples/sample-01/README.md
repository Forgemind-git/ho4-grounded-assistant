# HO4 Sample 1 — HR Policy Assistant

**Domain:** HR leave and expense policies

A grounded Q&A assistant that answers employee questions using **only** the company HR policy
documents. It shows the difference between Claude guessing from general knowledge (BEFORE) and
citing the actual policy (AFTER) — so every answer traces back to a real rule, and questions
the policy doesn't cover get an honest "I don't have that" instead of an invented one.

## Use it with your Claude.ai subscription
No API key needed. Just your normal Claude.ai login (Projects is available on Claude Pro
or Team). A richer click-by-click walkthrough is in this folder's **`index.html`** (open it in
a browser).

1. Open **claude.ai** and sign in.
2. In the left sidebar click **Projects**, then **+ New Project**. Name it `HR Policy Assistant`.
3. Click **Add content** → **Upload files** and upload **`context/policy.txt`** from this folder.
4. Click **Set project instructions** and paste the example prompt below. Click **Save**.
5. Start a new chat **inside the project** and ask the questions in **`test_questions.txt`**.
   Each answer should cite the specific policy rule; anything not in the policy should get the
   "contact HR" reply.

## The example prompt
Paste this into the Project's **instructions** field (it's the content of
`context/instructions.txt`):

```
You are an HR Policy Assistant for ACME Corp.

You answer questions ONLY using the HR policy documents provided in your context.

Rules you must follow:
1. If the answer is in the context, give a clear, specific answer and cite the relevant policy section.
2. If the answer is NOT in the context, say: "I don't have information about that in the current HR policy documents. Please contact HR directly for assistance."
3. Never guess, invent, or use general HR knowledge not present in the provided documents.
4. Keep answers concise and employee-friendly.
5. Always quote or paraphrase the specific policy rule that supports your answer.
```

## Before vs after
**Question:** "Do I need a receipt for a $20 lunch?"

- **BEFORE (ungrounded):** "Most companies require receipts for business expenses, though the
  threshold varies — often around $25–$75. Check your company's policy for the exact cutoff."
  → generic, vague, possibly wrong for your company.
- **AFTER (grounded):** "No — per the Expense Claims section, receipts are only required for
  claims over $25, and $20 is under that threshold." → exact, cited, correct.

## Make it your own
- Replace `context/policy.txt` with your real HR policy document.
- Adjust the company name and tone in the instructions.
- Add more files to the Project (e.g. benefits, code of conduct) — the assistant uses all of them.

## Optional — automate it with the API (advanced)
You do **not** need this for the course. The `grounded_qa.py` script in this folder runs the
same BEFORE/AFTER demo from Python. It needs an Anthropic API key (separate from your Claude.ai
subscription, so it costs money) and is only for developers who want to script the pattern.

```bash
cd samples/sample-01
pip install -r requirements.txt
cp .env.example .env          # add your ANTHROPIC_API_KEY
export ANTHROPIC_API_KEY=your_key_here
python grounded_qa.py
```

## Key concept demonstrated
**Grounding** = giving Claude the authoritative documents (here, via a Project) so it answers
from facts, not guesses. The model cannot contradict the context or hallucinate policies that
aren't there.
