# Sample 05 — Study Assistant

**Domain:** Course study materials and syllabus

A grounded Q&A assistant that helps students study using only the provided course notes. Shows the difference between Claude drawing on its full ML knowledge (BEFORE — potentially overwhelming) vs. explaining concepts strictly from the current chapter notes (AFTER — scoped to the syllabus).

## Problem Statement

When a student in an intro ML course asks "What is backpropagation?" an ungrounded Claude may explain autodiff, computational graphs, and advanced optimisers — far beyond what Chapter 2 covers. The grounded version explains it in the terms and depth of the actual course notes, which is what the student needs for their exam. This sample shows how to scope an AI tutor to the curriculum.

## What's in this sample

```
sample-05/
├── grounded_qa.py       # Main script — runs BEFORE and AFTER demo
├── test_questions.txt   # 6 study questions to test the assistant
├── requirements.txt     # anthropic
├── .env.example         # Copy to .env and add your API key
└── context/
    ├── policy.txt       # ML101 course notes: Chapters 1-3
    └── instructions.txt # System instructions scoping Claude to the syllabus
```

## Quick start

```bash
cd samples/sample-05
pip install -r requirements.txt
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY
export ANTHROPIC_API_KEY=your_key_here
python grounded_qa.py
```

## Expected output

```
QUESTION 3: How is precision different from recall?

[BEFORE] Without course notes (Claude draws on its full ML knowledge):
  Precision and recall are two fundamental metrics in information
  retrieval and classification. Precision measures the accuracy of
  positive predictions: TP/(TP+FP). It answers "when the model
  predicts positive, how often is it right?" Recall (also called
  sensitivity or true positive rate) measures coverage: TP/(TP+FN)...

[AFTER]  With course study materials loaded (stays within the syllabus):
  Chapter 3 of your course notes explains it this way:

  Precision = TP / (TP + FP) — of all the samples the model predicted
  as positive, how many were actually positive? High precision = few
  false alarms.

  Recall = TP / (TP + FN) — of all the samples that were actually
  positive, how many did the model find? High recall = few missed cases.

  The F1 Score combines both: 2 * (Precision * Recall) / (Precision + Recall).
```

## How to extend this

1. Replace `context/policy.txt` with your actual course notes or lecture slides (converted to text).
2. Add one file per chapter: `context/chapter1.txt`, `context/chapter2.txt`.
3. Update `test_questions.txt` with questions from past exams or practice sheets.
4. Add more chapters as the course progresses — the assistant automatically stays within what's loaded.

## Key concept demonstrated

**Grounding controls the scope of answers.** For a study tool, an all-knowing AI is less useful than one constrained to the curriculum. The grounded version helps students revise what they were actually taught — not what exists in the wider field.
