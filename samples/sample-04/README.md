# HO4 Sample 4 — Compliance SOP Assistant

**Domain:** Regulatory compliance standard operating procedure

A grounded Q&A assistant that answers compliance questions using **only** the organisation's
SOP documents — and *refuses* to guess when the SOP doesn't cover something. It shows the
difference between Claude citing generic regulatory knowledge (BEFORE) and citing the specific
organisational rule, owner, and timeline (AFTER), which is exactly what matters when a wrong
answer has real consequences.

## Use it with your Claude.ai subscription
No API key needed. Just your normal Claude.ai login (Projects is available on Claude Pro
or Team). A richer click-by-click walkthrough is in this folder's **`index.html`** (open it in
a browser).

1. Open **claude.ai** and sign in.
2. In the left sidebar click **Projects**, then **+ New Project**. Name it `Compliance SOP Assistant`.
3. Click **Add content** → **Upload files** and upload **`context/policy.txt`** from this folder.
4. Click **Set project instructions** and paste the example prompt below. Click **Save**.
5. Start a new chat **inside the project** and ask the questions in **`test_questions.txt`** —
   including ones *not* in the SOP. It should quote exact figures and deadlines, and refuse +
   escalate when something isn't covered.

## The example prompt
Paste this into the Project's **instructions** field (it's the content of
`context/instructions.txt`):

```
You are a Compliance SOP Assistant for the Data Protection team.

You answer compliance questions ONLY using the Standard Operating Procedure documents provided in your context.

Rules you must follow:
1. If the answer is in the SOP, give a precise and clear answer, always citing the relevant section name and rule (e.g. "Per the Access Control section of SOP-DPC-001...").
2. If the answer is NOT in the SOP, say: "This is not covered in the current SOP documents. Please escalate to the DPO directly for guidance."
3. Never guess at regulatory requirements or invent compliance rules not present in the documents.
4. Compliance answers must be exact — avoid paraphrasing in a way that changes the meaning.
5. If an action described by the user appears to violate the SOP, say so clearly and explain the correct procedure.
```

## Before vs after
**Question:** "When must I report a security incident?"

- **BEFORE (ungrounded):** "Under GDPR, breaches are reported to the supervisory authority
  within 72 hours…" → legally generic, misses your internal deadline.
- **AFTER (grounded):** "Per the Security Incidents section of SOP-DPC-001, report to the DPO
  within 2 hours of detection; the DPO then assesses the 72-hour authority notification." → the
  internal rule employees must actually hit.

## Make it your own
- Replace `context/policy.txt` with your real, approved SOP.
- Update the SOP reference number and the escalation contact in the instructions.
- Keep rule 2 strict — the refusal when something isn't covered is the whole point here.

## Important disclaimer
This demo is for education. Always consult your Data Protection Officer for actual compliance
decisions. Never rely solely on an AI assistant for regulatory compliance.

## Optional — automate it with the API (advanced)
You do **not** need this for the course. The `grounded_qa.py` script in this folder runs the
same BEFORE/AFTER demo from Python. It needs an Anthropic API key (separate from your Claude.ai
subscription, so it costs money) and is only for developers who want to script the pattern.

```bash
cd samples/sample-04
pip install -r requirements.txt
cp .env.example .env          # add your ANTHROPIC_API_KEY
export ANTHROPIC_API_KEY=your_key_here
python grounded_qa.py
```

## Key concept demonstrated
**Grounding is safety-critical in compliance contexts.** An ungrounded Claude gives generically
framed answers; a grounded Claude gives the specific internal deadline, owner, and procedure —
the things your employees actually need to follow.
