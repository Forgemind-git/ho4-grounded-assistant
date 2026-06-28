# HO4 Sample 2 — Product Support Assistant

**Domain:** SaaS product documentation

A grounded Q&A assistant that answers user support questions using **only** your product
documentation. It shows the difference between Claude giving generic SaaS advice (BEFORE) and
citing the exact steps from your docs (AFTER) — so it never invents a feature, a menu path, or
a setting that doesn't exist.

## Use it with your Claude.ai subscription
No API key needed. Just your normal Claude.ai login (Projects is available on Claude Pro
or Team). A richer click-by-click walkthrough is in this folder's **`index.html`** (open it in
a browser).

1. Open **claude.ai** and sign in.
2. In the left sidebar click **Projects**, then **+ New Project**. Name it `Product Support Assistant`.
3. Click **Add content** → **Upload files** and upload **`context/policy.txt`** from this folder.
4. Click **Set project instructions** and paste the example prompt below. Click **Save**.
5. Start a new chat **inside the project** and ask the questions in **`test_questions.txt`**.
   Answers should be step-by-step and cite the doc section; anything not in the docs should get
   the "contact support" reply.

## The example prompt
Paste this into the Project's **instructions** field (it's the content of
`context/instructions.txt`):

```
You are a Product Support Assistant for Acme SaaS.

You answer user questions ONLY using the product documentation provided in your context.

Rules you must follow:
1. If the answer is in the documentation, give a clear step-by-step answer citing the relevant section.
2. If the answer is NOT in the documentation, say: "I don't have information about that in the current documentation. Please contact our support team at support@acme.example.com."
3. Never invent features, settings, or procedures that are not described in the documents.
4. Be friendly and precise — users may be non-technical, so keep instructions simple.
5. When giving steps, use a numbered list for clarity.
```

## Before vs after
**Question:** "How do I get an API key?"

- **BEFORE (ungrounded):** "You typically navigate to account settings or a developer portal;
  look for an 'API' or 'Developer' section…" → generic and possibly wrong.
- **AFTER (grounded):** "Go to Settings > Integrations > API Keys, click Generate New Key, and
  copy it immediately — it is shown only once and cannot be retrieved again." → exact, cited.

## Make it your own
- Replace `context/policy.txt` with your real help docs.
- Add more files to the Project (e.g. billing, troubleshooting, release notes).
- Update the support email and tone in the instructions.

## Optional — automate it with the API (advanced)
You do **not** need this for the course. The `grounded_qa.py` script in this folder runs the
same BEFORE/AFTER demo from Python. It needs an Anthropic API key (separate from your Claude.ai
subscription, so it costs money) and is only for developers who want to script the pattern.

```bash
cd samples/sample-02
pip install -r requirements.txt
cp .env.example .env          # add your ANTHROPIC_API_KEY
export ANTHROPIC_API_KEY=your_key_here
python grounded_qa.py
```

## Key concept demonstrated
**Grounding** forces Claude to answer from your specific documentation rather than generic
software knowledge. Critical details — exact navigation paths, one-time actions, processing
times — only appear correctly when the model has the actual source.
