# HO4 Sample 4 — Compliance SOP Grounded Assistant

## Your task

You own a regulated SOP where a wrong answer has real consequences. Build a compliance assistant grounded only in your SOP documents.

## What you will build

A Claude Project that answers compliance questions ONLY from your official SOP documents — exact citations, no guessing at regulatory requirements.

## Step-by-step

1. Open claude.ai → click "Projects" → "New Project"
2. Name it: "Compliance SOP Assistant"
3. Fill in the context files in the `context/` folder with your real SOP content
4. Upload all files from the `context/` folder into the Project
5. Paste the contents of `context/instructions.txt` into the Project instructions field
6. Test with the questions in `context/test-questions.txt`

## What to do now

1. **Fill in `context/sop-document.txt`** — your official SOP with section names and rules
2. **Fill in `context/compliance-checklist.txt`** — step-by-step checklists for regulated processes
3. **Fill in `context/escalation-guide.txt`** — who to escalate to and under what conditions
4. **Edit `context/instructions.txt`** — update the TODO lines for your compliance domain
5. **Fill in `context/test-questions.txt`** — write questions that test compliance edge cases

## Files in this sample

```
sample-04/
├── README.md                          ← You are here
└── context/
    ├── sop-document.txt               ← TODO: your official SOP rules and procedures
    ├── compliance-checklist.txt       ← TODO: step-by-step compliance checklists
    ├── escalation-guide.txt           ← TODO: escalation contacts and thresholds
    ├── instructions.txt               ← TODO: edit for your compliance domain
    └── test-questions.txt             ← TODO: add compliance test questions
```

## Success criteria

- Questions covered by the SOP get precise, section-cited answers
- Questions NOT in the SOP escalate clearly rather than guessing
- Potential violations are flagged with the correct procedure
