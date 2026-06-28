# HO4 Sample 5 — Study Grounded Assistant

## Your task

You are a student revising from a syllabus and dense readings. Build a study assistant grounded only in your course materials.

## What you will build

A Claude Project that answers revision questions ONLY from your uploaded course materials — no concepts beyond what was taught, no outside knowledge.

## Step-by-step

1. Open claude.ai → click "Projects" → "New Project"
2. Name it: "[Course Name] Study Assistant"
3. Fill in the context files in the `context/` folder with your real course materials
4. Upload all files from the `context/` folder into the Project
5. Paste the contents of `context/instructions.txt` into the Project instructions field
6. Test with the questions in `context/test-questions.txt`

## What to do now

1. **Fill in `context/syllabus.txt`** — the official course syllabus (topics, weeks, learning objectives)
2. **Fill in `context/chapter-notes.txt`** — your study notes or lecture summaries
3. **Fill in `context/past-paper-questions.txt`** — past exam questions and model answers
4. **Edit `context/instructions.txt`** — update the TODO lines for your course
5. **Fill in `context/test-questions.txt`** — write questions to test the assistant covers your syllabus

## Files in this sample

```
sample-05/
├── README.md                          ← You are here
└── context/
    ├── syllabus.txt                   ← TODO: course topics and learning objectives
    ├── chapter-notes.txt              ← TODO: your lecture notes and summaries
    ├── past-paper-questions.txt       ← TODO: past exam questions and answers
    ├── instructions.txt               ← TODO: edit for your course
    └── test-questions.txt             ← TODO: add revision test questions
```

## Success criteria

- Questions on syllabus topics get clear, chapter-cited explanations
- Questions outside the course notes redirect to the textbook or lecturer
- Answers use student-friendly language, not just copied definitions
