# HO4 Sample 5 — Study Assistant

**Domain:** Course study materials and syllabus

A grounded Q&A assistant that helps students study using **only** the provided course notes. It
shows the difference between Claude drawing on its full ML knowledge (BEFORE — potentially
overwhelming and beyond the syllabus) and explaining concepts strictly from the current chapter
notes (AFTER — scoped to what the student was actually taught).

## Use it with your Claude.ai subscription
No API key needed. Just your normal Claude.ai login (Projects is available on Claude Pro
or Team). A richer click-by-click walkthrough is in this folder's **`index.html`** (open it in
a browser).

1. Open **claude.ai** and sign in.
2. In the left sidebar click **Projects**, then **+ New Project**. Name it `ML101 Study Assistant`.
3. Click **Add content** → **Upload files** and upload **`context/policy.txt`** from this folder.
4. Click **Set project instructions** and paste the example prompt below. Click **Save**.
5. Start a new chat **inside the project** and ask the questions in **`test_questions.txt`**.
   Answers should cite the chapter; a topic not in the notes should get the "check the textbook
   or ask your lecturer" reply.

## The example prompt
Paste this into the Project's **instructions** field (it's the content of
`context/instructions.txt`):

```
You are a Study Assistant for the ML101 Introduction to Machine Learning course.

You help students understand the course material by answering questions using ONLY the provided course study notes.

Rules you must follow:
1. If the answer is in the course notes, give a clear explanation in your own words that helps the student understand, and cite the chapter (e.g. "Chapter 2 explains...").
2. If the answer is NOT in the course notes, say: "That topic isn't covered in the current chapter notes. I'd recommend checking the full textbook or asking your lecturer."
3. Never introduce concepts, algorithms, or definitions not present in the provided study materials.
4. Use simple, student-friendly language. When explaining formulas, give a plain-English interpretation as well.
5. Encourage the student — learning ML takes time, and that's okay.
```

## Before vs after
**Question:** "How is precision different from recall?"

- **BEFORE (ungrounded):** a deep dive into information retrieval, sensitivity, ROC curves… →
  correct but beyond the course and overwhelming.
- **AFTER (grounded):** "Chapter 3 explains it: Precision = TP/(TP+FP) (few false alarms),
  Recall = TP/(TP+FN) (few misses); F1 combines them." → scoped to the syllabus, exam-ready.

## Make it your own
- Replace `context/policy.txt` with your own course notes or lecture slides (as text).
- Add a file per chapter and upload past papers to the Project.
- Update the course name and code in the instructions.

## Optional — automate it with the API (advanced)
You do **not** need this for the course. The `grounded_qa.py` script in this folder runs the
same BEFORE/AFTER demo from Python. It needs an Anthropic API key (separate from your Claude.ai
subscription, so it costs money) and is only for developers who want to script the pattern.

```bash
cd samples/sample-05
pip install -r requirements.txt
cp .env.example .env          # add your ANTHROPIC_API_KEY
export ANTHROPIC_API_KEY=your_key_here
python grounded_qa.py
```

## Key concept demonstrated
**Grounding controls the scope of answers.** For a study tool, an all-knowing AI is less useful
than one constrained to the curriculum — the grounded version helps students revise what they
were actually taught.
