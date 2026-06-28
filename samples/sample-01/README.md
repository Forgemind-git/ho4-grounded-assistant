# HO4 Sample 1 — HR Policy Grounded Assistant

## Your task

Your HR inbox keeps getting the same leave and expense questions. Build an assistant grounded only in your HR policy document — no guessing allowed.

## What you will build

A Claude Project that answers employee HR questions ONLY from the documents you upload — no generic HR advice, no invented rules.

## Step-by-step

1. Open claude.ai → click "Projects" → "New Project"
2. Name it: "HR Policy Assistant"
3. Fill in the context files in the `context/` folder with your real HR policy content
4. Upload all files from the `context/` folder into the Project
5. Paste the contents of `context/instructions.txt` into the Project instructions field
6. Test with the questions in `context/test-questions.txt`

## What to do now

1. **Fill in `context/leave-policy.txt`** — your company's actual leave entitlements
2. **Fill in `context/expense-policy.txt`** — your company's expense rules and limits
3. **Fill in `context/instructions.txt`** — edit the TODO lines to match your domain
4. **Fill in `context/test-questions.txt`** — write 3–5 questions that test your assistant

## Files in this sample

```
sample-01/
├── README.md                      ← You are here
└── context/
    ├── leave-policy.txt           ← TODO: add your leave policy content
    ├── expense-policy.txt         ← TODO: add your expense rules
    ├── instructions.txt           ← TODO: edit to match your company
    └── test-questions.txt         ← TODO: add your test questions
```

## Success criteria

- Questions covered by the policy get specific, cited answers
- Questions NOT in the policy get: "I don't have that information in my knowledge base."
- No made-up rules or generic HR advice
