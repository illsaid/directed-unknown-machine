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

Run 1 manually exercised the scenario against the starter `machine.py`. The original report did identify the inferred problem, expected outcome, unknown actual outcome, failure points, next improvement, and hypothesis pressure. It did not yet produce a crisp decision label or a directly named recommended action, so the output was useful but still too soft for an autonomous loop.

After Run 1, `machine.py` now emits both `Decision:` and `Recommended action:` fields. For this scenario's current partial state, the decision should be `hold-but-improve` and the recommendation should point back to the recorded gap instead of encouraging new generic features.

## Whether the system helped

partial

## What broke

The starter report pressured the hypothesis in prose but did not give the next autonomous run a compact decision label or explicit action. That made it too easy for the agent to keep adding features instead of deciding whether the hypothesis strengthened, weakened, or merely stayed alive.

## What would make the result more useful

Next, run a comparative scenario against a plain checklist. If `machine.py` cannot produce a sharper decision than a checklist, weaken H1 and strengthen or test H2.
