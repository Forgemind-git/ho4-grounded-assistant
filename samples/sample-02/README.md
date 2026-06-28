# HO4 Sample 2 — Product Support Grounded Assistant

## What you'll build
A support assistant that answers customer "how do I…?" questions using **only** your product
documentation — so it never invents a feature or a setting that doesn't exist. Ask "How do I
reset my password?" and it gives the real steps from your manual; ask about something you
don't support and it says so and points to your support email. This folder ships a complete,
working example for a fictional helpdesk product ("Brightdesk") that you can run in minutes,
then swap in your own docs.

## Use it with your Claude.ai subscription
No API key needed. Just your normal Claude.ai login (Projects is available on Claude Pro
or Team).

1. Open **claude.ai** and sign in.
2. In the left sidebar click **Projects**, then **+ New Project**. Name it `Product Support Assistant`.
3. Click **Add content** → upload the three doc files from this folder's `context/` folder:
   **`product-manual.txt`**, **`faq.txt`**, and **`troubleshooting-guide.txt`**.
4. Click **Set project instructions** and paste the example prompt below. Click **Save**.
5. Start a new chat **inside the project** and ask the questions in
   **`context/test-questions.txt`**. Answers should be step-by-step and cite the doc section;
   anything not in the docs should get the "contact support" reply.

No code, no terminal — a grounded support bot.

## The example prompt
Paste this into the Project's **instructions** field (it's the content of
`context/instructions.txt`):

```
You are a Product Support Assistant for Brightdesk.

You answer user questions ONLY using the product documentation provided in this Project.

Rules you must follow:
1. If the answer is in the documentation, give a clear step-by-step answer and cite the relevant section (e.g. "See the Data and Exports section...").
2. If the answer is NOT in the documentation, say: "I don't have that information in my knowledge base. Please contact our support team at support@brightdesk.example.com."
3. Never invent features, settings, or procedures that are not described in the documents.
4. Be friendly and precise — users may be non-technical, so keep instructions simple.
5. When giving steps, use a numbered list.
```

Then ask, for example: **"Why did my export fail?"** — it should explain the cause (empty
date range or too-large export) and how to fix it, straight from the troubleshooting guide.

## Make it your own
- Replace the three example docs with your real manual, FAQ, and troubleshooting pages.
- Update the support email and tone in the instructions.
- Add release notes or a "known issues" file — the assistant will draw on all of them.

## Optional — automate it with the API (advanced)
You do **not** need this for the course. If you later want to run the before/after demo from
code, the `main` branch includes a `grounded_qa.py` script. It needs an Anthropic API key,
which is separate from your Claude.ai subscription (so it costs money) and is not part of the
hands-on.
