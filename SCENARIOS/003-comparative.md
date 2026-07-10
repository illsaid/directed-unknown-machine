# 003 — Comparative: beat a plain checklist

## Type

comparative

## User

A solo builder deciding whether the current system is better than a simple manual checklist.

## Situation

The user can already read a scenario and ask: Who is this for? What is the expected outcome? What broke? What next? The system must prove it adds something beyond restating those questions.

## Input

The friendly scenario from `SCENARIOS/001-friendly.md`.

## Expected useful outcome

Compared with a manual checklist, the system should add useful pressure: hypothesis movement, concrete failure points, and a next implementation step tied to the scenario.

## Actual outcome

Run 2 compared the current report with a plain checklist. The report adds some value because it gives a decision and recommended action instead of only restating the scenario fields. The advantage is still thin because it does not name the baseline difference directly.

## Whether the system helped

partial

## What broke

The report is sharper than a checklist, but not yet distinctive enough.

## What would make the result more useful

Next, test the vague-input scenario and see whether the system can produce one bounded task.
