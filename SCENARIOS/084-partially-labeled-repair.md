# 084 — Repair a partially labeled contract accurately

## Type

hostile-regression

## User

A product lead who supplied three valid contract fields and needs the tool to request only the missing field without falsely describing the existing notes as unlabeled.

## Situation

The input supplies Decision, Evidence, and Constraints but omits Success. The validation behavior is already correct; the test is whether the repair language accurately describes a partially labeled contract while preserving the exact missing-field request.

## Input

Decision: Choose whether to roll out the new checkout.
Evidence: Paid conversion is 23%. P95 latency is 480 milliseconds.
Constraints: Conversion must be at least 20%. Latency must be below 500 milliseconds.

## Expected useful outcome

The executable exits with `contract incomplete; add the missing explicit fields without rewriting the notes:` followed only by `Success:`. It does not call the supplied three fields unlabeled, infer a Success rule, or alter the four-field schema.

## Actual outcome

Run 86 mentally simulates `python decision_brief.py SCENARIOS/084-partially-labeled-repair.md`. The parser preserves the three populated labels, identifies only `Success` as missing, and exits with `contract incomplete; add the missing explicit fields without rewriting the notes:` followed by `Success:`. No complete-contract output or inferred recommendation appears.

## Whether the system helped

yes

## What broke

The previous repair phrase `from unlabeled prose` was false for partially labeled inputs. Run 86 retains the neutral behavior while replacing the indirect consequence statement with the directly validated state `contract incomplete`.

## What would make the result more useful

Test whether the repair output can lead directly with the missing labels and remove the remaining generic diagnosis without making the refusal less clear.