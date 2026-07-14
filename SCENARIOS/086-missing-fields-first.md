# 086 — Lead incomplete repair with the missing fields

## Type

hostile-regression

## User

An operator who supplied three explicit decision-contract fields and needs the repair output to identify the single missing field immediately.

## Situation

The input is a concrete rollout decision with `Decision`, `Evidence`, and `Constraints`, but no `Success`. The test is whether repair can begin with the missing-field fact itself instead of a generic contract diagnosis.

## Input

Decision: Decide whether to roll out the new checkout.
Evidence: Paid conversion is 23 percent and p95 latency is 480 milliseconds.
Constraints: Conversion must be at least 20 percent and latency must be below 500 milliseconds.

## Expected useful outcome

The executable exits with `Missing explicit fields:` followed by `Success:`. It preserves the supplied fields, infers no success rule, emits no recommendation, and adds no repair mode.

## Actual outcome

Run 87 mentally simulates `python decision_brief.py SCENARIOS/086-missing-fields-first.md`. Unsupported-label detection returns none. `Success` alone has no value, so the existing missing-field path exits with `Missing explicit fields:` followed by `Success:`. No complete-contract output, inferred rule, or recommendation appears.

## Whether the system helped

yes

## What broke

The prior line `contract incomplete; add the missing explicit fields without rewriting the notes:` was accurate but generic. The list of absent schema labels already states both the defect and the repair.

## What would make the result more useful

Pressure the unsupported-field error for the same directness without weakening its schema-preservation guidance.