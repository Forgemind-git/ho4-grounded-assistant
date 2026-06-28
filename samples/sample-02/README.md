# HO4 Sample 2 — Product Docs Grounded Assistant

## Your task

Support agents waste time digging through manuals mid-chat. Build an assistant grounded only in your product documentation.

## What you will build

A Claude Project that answers product support questions ONLY from your uploaded documentation — no invented features, no generic SaaS advice.

## Step-by-step

1. Open claude.ai → click "Projects" → "New Project"
2. Name it: "Product Support Assistant"
3. Fill in the context files in the `context/` folder with your real product docs
4. Upload all files from the `context/` folder into the Project
5. Paste the contents of `context/instructions.txt` into the Project instructions field
6. Test with the questions in `context/test-questions.txt`

## What to do now

1. **Fill in `context/product-manual.txt`** — core product features and how-to steps
2. **Fill in `context/faq.txt`** — common questions and official answers
3. **Fill in `context/troubleshooting-guide.txt`** — known errors and fixes
4. **Edit `context/instructions.txt`** — update the TODO lines for your product
5. **Fill in `context/test-questions.txt`** — write questions that cover and miss your docs

## Files in this sample

```
sample-02/
├── README.md                          ← You are here
└── context/
    ├── product-manual.txt             ← TODO: add product features and instructions
    ├── faq.txt                        ← TODO: add frequently asked questions
    ├── troubleshooting-guide.txt      ← TODO: add error codes and fixes
    ├── instructions.txt               ← TODO: edit for your product
    └── test-questions.txt             ← TODO: add your test questions
```

## Success criteria

- Questions covered by the docs get step-by-step, cited answers
- Questions NOT in the docs get: "I don't have that information in my knowledge base."
- No invented UI flows or features
