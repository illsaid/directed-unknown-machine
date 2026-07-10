# 001 — Friendly: rough idea needs a usefulness test

## Type

friendly

## User

A solo builder with one afternoon to decide whether a rough software idea deserves another implementation cycle.

## Situation

The user has a small runnable prototype, but the project is drifting toward generic features. They need a concrete test that says whether the prototype is becoming useful for a real task.

## Input

A scenario file describing a user, situation, input, expected useful outcome, actual outcome, whether the system helped, what broke, and what would make the result more useful.

## Expected useful outcome

The system should produce a structured report that identifies the inferred problem, compares expected vs. actual outcome, highlights failure points, and recommends the next small improvement without inventing a broad product direction.

## Actual outcome

Not yet recorded. Run `python machine.py run SCENARIOS/001-friendly.md` and paste or summarize the result here.

## Whether the system helped

unknown

## What broke

Not yet tested.

## What would make the result more useful

The report should pressure the agent toward a concrete next implementation step or toward weakening the current hypothesis.
