# Sample 04 — Compliance SOP Assistant

**Domain:** Regulatory compliance standard operating procedure

A grounded Q&A assistant that answers compliance questions using only the organisation's SOP documents. Shows the difference between Claude citing generic regulatory knowledge (BEFORE) vs. citing the specific organisational rule, owner, and timeline (AFTER).

## Problem Statement

When an employee asks "How long must I keep audit logs?" an ungrounded Claude will cite general regulatory frameworks — which may be accurate in general, but your SOP may specify a stricter or different requirement (e.g. 7 years). In compliance, the answer must come from the actual internal document, not from Claude's training data. This sample shows how to enforce that.

## What's in this sample

```
sample-04/
├── grounded_qa.py       # Main script — runs BEFORE and AFTER demo
├── test_questions.txt   # 6 compliance questions to test the assistant
├── requirements.txt     # anthropic
├── .env.example         # Copy to .env and add your API key
└── context/
    ├── policy.txt       # SOP-DPC-001 Data Protection & Compliance SOP
    └── instructions.txt # System instructions grounding Claude to the SOP
```

## Quick start

```bash
cd samples/sample-04
pip install -r requirements.txt
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY
export ANTHROPIC_API_KEY=your_key_here
python grounded_qa.py
```

## Expected output

```
QUESTION 4: When must I report a security incident?

[BEFORE] Without SOP context (Claude guesses from general GDPR knowledge):
  Under GDPR, you are required to report personal data breaches to the
  relevant supervisory authority within 72 hours of becoming aware of
  the breach, where feasible...

[AFTER]  With SOP documents loaded (cites the actual organisational rule):
  Per the Security Incidents section of SOP-DPC-001: security incidents
  involving personal data must be reported to the DPO within 2 hours of
  detection, regardless of the time of day. The 72-hour supervisory
  authority notification window is assessed by the DPO after your report.
```

The BEFORE answer cites the general GDPR 72-hour rule. The AFTER answer gives the internal 2-hour escalation window that employees must actually hit.

## How to extend this

1. Replace `context/policy.txt` with your actual compliance SOP.
2. Add separate files per policy area: `context/access_control.txt`, `context/incident_response.txt`.
3. Update `test_questions.txt` with real compliance questions from your team.
4. Adjust instructions to reference your DPO's contact details.

## Important disclaimer

This demo is for educational purposes. Always consult your Data Protection Officer for actual compliance decisions. Never rely solely on an AI assistant for regulatory compliance.

## Key concept demonstrated

**Grounding is safety-critical in compliance contexts.** An ungrounded Claude gives legally correct but generically framed answers. A grounded Claude gives the specific internal deadline, owner, and procedure — the things your employees actually need to follow.
