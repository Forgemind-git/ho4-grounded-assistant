# HO4 Sample 1 — HR Policy Grounded Assistant

## What you'll build
A chat assistant that answers staff HR questions using **only** your company's HR policy —
no guessing, no generic internet advice. Ask "Do I need a receipt for a $20 lunch?" and it
answers from the real policy and tells you the exact rule. If something isn't in the policy,
it says so instead of making it up. This folder already contains a complete, working example
(a fictional company, "Northwind Trading Co.") so you can build it in a couple of minutes and
then swap in your own policy.

## Use it with your Claude.ai subscription
No API key needed. Just your normal Claude.ai login (Projects is available on Claude Pro
or Team).

1. Open **claude.ai** and sign in.
2. In the left sidebar click **Projects**, then **+ New Project**. Name it `HR Policy Assistant`.
3. In the project, click **Add content** → upload the two files from this folder's `context/`
   folder: **`leave-policy.txt`** and **`expense-policy.txt`**.
4. Click **Set project instructions** (or "Edit") and paste the example prompt below.
   Click **Save**.
5. Start a new chat **inside the project** and ask the questions from
   **`context/test-questions.txt`**. Each answer should quote the real policy rule. When you
   ask something not in the policy, it should say it doesn't have that information.

That's it — a grounded HR assistant, no code.

## The example prompt
Paste this into the Project's **instructions** field (it's the content of
`context/instructions.txt`):

```
You are an HR Policy Assistant for Northwind Trading Co.

You answer questions ONLY using the HR policy documents provided in this Project.

Rules you must follow:
1. If the answer is in the documents, give a clear, specific answer and cite the relevant policy section (e.g. "Per the Annual Leave section...").
2. If the answer is NOT in the documents, say: "I don't have that information in my knowledge base. Please contact HR directly for assistance."
3. Never guess, invent, or use general HR knowledge that is not in the provided documents.
4. Keep answers concise and employee-friendly.
5. Always quote or paraphrase the specific policy rule that supports your answer.
```

Then ask, for example: **"Do I need a receipt for a $20 lunch?"** — a grounded assistant
replies that you don't, because receipts are only required over $25.

## Make it your own
- Replace `leave-policy.txt` and `expense-policy.txt` with your real HR documents (drag the
  new files into the Project and remove the examples).
- Change the company name and tone in the instructions to match your organisation.
- Add more documents (benefits, code of conduct) — the assistant will use all of them.

## Optional — automate it with the API (advanced)
You do **not** need this for the course. If you later want to run the same before/after
demo from code, the `main` branch of this repo includes a `grounded_qa.py` script. It needs
an Anthropic API key, which is separate from your Claude.ai subscription (so it costs money)
and is not part of the hands-on.
