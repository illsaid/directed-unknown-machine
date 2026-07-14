# 083 — Refuse an incomplete contract before declaring completeness

## Type

hostile-regression

## User

A product lead delegating a rollout decision who needs the tool to expose a missing success rule rather than infer one from the decision or constraints.

## Situation

The input supplies Decision, Evidence, and Constraints but omits Success. The test is whether the executable refuses before printing a complete-contract line, identifies the exact missing field, and preserves the supplied notes without inventing a fallback rule.

## Input

Decision: Choose whether to roll out the new checkout.
Evidence: Paid conversion is 23%. P95 latency is 480 milliseconds.
Constraints: Conversion must be at least 20%. Latency must be below 500 milliseconds.

## Expected useful outcome

The executable exits before printing any complete-contract output and returns a repair instruction containing only `Success:`. It does not infer rollout, delay, or any other success rule from the supplied decision, evidence, or constraints.

## Actual outcome

Run 84 mentally simulates `python decision_brief.py SCENARIOS/083-incomplete-contract-check.md`. The parser finds three populated labels and one missing label, exits through `repair_template`, and prints `cannot preserve the decision contract from unlabeled prose; add these explicit fields without rewriting the notes:` followed by `Success:`. The compact complete-state line is never reached, so no completeness claim or inferred recommendation appears.

## Whether the system helped

yes

## What broke

The previous complete-state wording was longer than necessary. The hostile case showed that the actual missing-field refusal boundary lives in the pre-output validation and repair instruction, while the first line for valid contracts only needs to state the verified postcondition: all four fields are explicit and nothing was inferred.

## What would make the result more useful

Next, test whether the repair message's phrase `from unlabeled prose` is accurate when the input is partially labeled rather than wholly unlabeled.
