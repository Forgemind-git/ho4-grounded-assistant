# HO4 Sample 4 — Compliance SOP Grounded Assistant

## What you'll build
A compliance assistant that answers staff questions using **only** your approved Standard
Operating Procedure — and *refuses* to guess when the SOP doesn't cover something, which is
exactly what you want when a wrong answer has real consequences. Ask "Can I store customer
data on a US server?" and it quotes the exact rule; ask something off-procedure and it tells
you to escalate to the DPO instead of inventing an answer. This folder ships a complete,
working example (a fictional data-protection SOP) you can build in minutes, then swap in your
own procedure.

## Use it with your Claude.ai subscription
No API key needed. Just your normal Claude.ai login (Projects is available on Claude Pro
or Team).

1. Open **claude.ai** and sign in.
2. In the left sidebar click **Projects**, then **+ New Project**. Name it `Compliance SOP Assistant`.
3. Click **Add content** → upload the three doc files from this folder's `context/` folder:
   **`sop-document.txt`**, **`compliance-checklist.txt`**, and **`escalation-guide.txt`**.
4. Click **Set project instructions** and paste the example prompt below. Click **Save**.
5. Start a new chat **inside the project** and ask the questions in
   **`context/test-questions.txt`** — including the ones that are *not* in the SOP. It should
   quote exact figures and deadlines, and refuse + escalate when something isn't covered.

No code, no terminal — a grounded compliance helper.

## The example prompt
Paste this into the Project's **instructions** field (it's the content of
`context/instructions.txt`):

```
You are a Compliance SOP Assistant for the Data Protection team.

You answer compliance questions ONLY using the Standard Operating Procedure documents provided in this Project.

Rules you must follow:
1. If the answer is in the SOP, give a precise answer and always cite the section name and rule (e.g. "Per the Access Control section of SOP-DPC-001...").
2. If the answer is NOT in the SOP, say: "This is not covered in the current SOP documents. Please escalate to the DPO directly for guidance."
3. Never guess at regulatory requirements or invent compliance rules not in the documents.
4. Quote exact figures and deadlines from the SOP — do not paraphrase in a way that changes the meaning.
5. If a described action appears to violate the SOP, say so clearly and explain the correct procedure.
```

Then ask, for example: **"When must I report a security incident?"** — it should answer "to
the DPO within 2 hours of detection", citing the Security Incidents section.

## Make it your own
- Replace the example SOP, checklists, and escalation guide with your real, approved documents.
- Update the SOP reference number, the escalation contact, and the tone in the instructions.
- Because guessing is unacceptable here, keep rule 2 strict — the refusal is the whole point.

## Optional — automate it with the API (advanced)
You do **not** need this for the course. If you later want to run the before/after demo from
code, the `main` branch includes a `grounded_qa.py` script. It needs an Anthropic API key,
which is separate from your Claude.ai subscription (so it costs money) and is not part of the
hands-on.
