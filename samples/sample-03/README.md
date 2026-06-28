# HO4 Sample 3 — Team Onboarding Grounded Assistant

## What you'll build
An onboarding buddy that answers a new joiner's setup questions using **only** your team's
wiki and runbooks — so it points them to the real process and the right person, instead of
guessing. Ask "How do I set up my local environment?" and it gives your actual steps; ask
"Who do I contact for a design review?" and it names the right person from the wiki. This
folder ships a complete, working example (a fictional "Orbit Engineering" team) you can build
in minutes, then swap in your own docs.

## Use it with your Claude.ai subscription
No API key needed. Just your normal Claude.ai login (Projects is available on Claude Pro
or Team).

1. Open **claude.ai** and sign in.
2. In the left sidebar click **Projects**, then **+ New Project**. Name it `Team Onboarding Buddy`.
3. Click **Add content** → upload the three doc files from this folder's `context/` folder:
   **`team-wiki.txt`**, **`setup-runbook.txt`**, and **`tools-guide.txt`**.
4. Click **Set project instructions** and paste the example prompt below. Click **Save**.
5. Start a new chat **inside the project** and ask the questions in
   **`context/test-questions.txt`**. Answers should cite the wiki or runbook; anything not in
   the docs should send the new joiner to your team Slack channel.

No code, no terminal — a grounded onboarding helper.

## The example prompt
Paste this into the Project's **instructions** field (it's the content of
`context/instructions.txt`):

```
You are a Team Onboarding Buddy for the Orbit Engineering team.

You help new team members get up to speed using ONLY the team wiki, runbooks, and tools guides provided in this Project.

Rules you must follow:
1. If the answer is in the documents, give a clear, helpful answer and cite the section (e.g. "According to the Setup Runbook...").
2. If the answer is NOT in the documents, say: "I don't have that information in my knowledge base. I'd recommend asking in #orbit-eng on Slack or checking with your team lead."
3. Never invent tools, processes, or people not mentioned in the documents.
4. Be friendly and welcoming — the reader is brand new to the team.
5. When referencing Slack channels, use the # prefix (e.g. #deploys).
```

Then ask, for example: **"How do I join the on-call rotation?"** — it should tell you to
message @oncall-admin in Slack, straight from the tools guide.

## Make it your own
- Replace the three example docs with your real wiki pages, runbooks, and tools guide.
- Update the team name and the Slack channel in the instructions.
- Add an architecture overview or a glossary — the assistant will use everything you upload.

## Optional — automate it with the API (advanced)
You do **not** need this for the course. If you later want to run the before/after demo from
code, the `main` branch includes a `grounded_qa.py` script. It needs an Anthropic API key,
which is separate from your Claude.ai subscription (so it costs money) and is not part of the
hands-on.
