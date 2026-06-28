# HO4 Sample 3 — Team Onboarding Grounded Assistant

## Your task

New joiners ask the same setup questions for weeks. Build an onboarding buddy grounded only in your team wiki and runbooks.

## What you will build

A Claude Project that answers new-joiner questions ONLY from your team's actual wiki and runbooks — no guessing about tools, processes, or people.

## Step-by-step

1. Open claude.ai → click "Projects" → "New Project"
2. Name it: "Team Onboarding Buddy"
3. Fill in the context files in the `context/` folder with your real team docs
4. Upload all files from the `context/` folder into the Project
5. Paste the contents of `context/instructions.txt` into the Project instructions field
6. Test with the questions in `context/test-questions.txt`

## What to do now

1. **Fill in `context/team-wiki.txt`** — team structure, key contacts, channels, norms
2. **Fill in `context/setup-runbook.txt`** — environment setup steps and access requests
3. **Fill in `context/tools-guide.txt`** — which tools you use and how to use them
4. **Edit `context/instructions.txt`** — update the TODO lines for your team
5. **Fill in `context/test-questions.txt`** — write questions a new joiner would actually ask

## Files in this sample

```
sample-03/
├── README.md                      ← You are here
└── context/
    ├── team-wiki.txt              ← TODO: team structure, contacts, channels
    ├── setup-runbook.txt          ← TODO: environment setup and access steps
    ├── tools-guide.txt            ← TODO: tools, logins, how-tos
    ├── instructions.txt           ← TODO: edit for your team
    └── test-questions.txt         ← TODO: add real new-joiner questions
```

## Success criteria

- Setup and access questions get specific, step-by-step answers
- "Who do I ask about X?" questions cite the right person or channel
- Questions not in the docs redirect to the right Slack channel or team lead
