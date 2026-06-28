# HO4 Sample 5 — Study Grounded Assistant

## What you'll build
A study assistant that answers your revision questions using **only** your course materials —
so you can trust it before an exam instead of worrying it made something up. Ask "What is
backpropagation?" and it explains it from your chapter notes and cites the chapter; ask about
a topic the course doesn't cover and it tells you to check the textbook rather than inventing
an answer. This folder ships a complete, working example (a fictional "ML101" course) you can
build in minutes, then swap in your own notes.

## Use it with your Claude.ai subscription
No API key needed. Just your normal Claude.ai login (Projects is available on Claude Pro
or Team).

1. Open **claude.ai** and sign in.
2. In the left sidebar click **Projects**, then **+ New Project**. Name it `ML101 Study Assistant`.
3. Click **Add content** → upload the three doc files from this folder's `context/` folder:
   **`syllabus.txt`**, **`chapter-notes.txt`**, and **`past-paper-questions.txt`**.
4. Click **Set project instructions** and paste the example prompt below. Click **Save**.
5. Start a new chat **inside the project** and ask the questions in
   **`context/test-questions.txt`**. Answers should cite the chapter; a topic not in the notes
   should get the "check the textbook or ask your lecturer" reply.

No code, no terminal — a grounded revision buddy.

## The example prompt
Paste this into the Project's **instructions** field (it's the content of
`context/instructions.txt`):

```
You are a Study Assistant for the ML101 Introduction to Machine Learning course.

You help students understand the material using ONLY the syllabus, chapter notes, and past papers provided in this Project.

Rules you must follow:
1. If the answer is in the notes, explain it clearly in your own words and cite the chapter (e.g. "Chapter 2 explains...").
2. If the answer is NOT in the notes, say: "That topic isn't covered in the current chapter notes. I'd recommend checking the full textbook or asking your lecturer."
3. Never introduce concepts, algorithms, or definitions that are not in the provided notes.
4. Use simple, student-friendly language; when explaining a formula, give a plain-English interpretation too.
5. For a past-paper question, show step-by-step working and be encouraging — learning ML takes time.
```

Then ask, for example: **"How is precision different from recall?"** — it should explain both
formulas in plain English and cite Chapter 3.

## Make it your own
- Replace the example syllabus, notes, and past papers with your own course materials.
- Update the course name and code in the instructions.
- Upload lecture slides or your own summaries — the more notes you add, the more it can help.

## Optional — automate it with the API (advanced)
You do **not** need this for the course. If you later want to run the before/after demo from
code, the `main` branch includes a `grounded_qa.py` script. It needs an Anthropic API key,
which is separate from your Claude.ai subscription (so it costs money) and is not part of the
hands-on.
