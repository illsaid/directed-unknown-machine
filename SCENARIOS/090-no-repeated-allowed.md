# 090 — Remove repeated allowed wording

## Type

hostile-regression

## User

An operator who supplied a complete four-field decision contract plus one unsupported ownership field and needs a concise repair that preserves the schema boundary without repeating itself.

## Situation

The input is a concrete rollout decision with all four allowed fields and an extra `Owner` field. The test is whether the remapping instruction can omit the second use of `allowed` while still directing the operator to preserve the extra meaning inside the fixed schema.

## Input

Decision: Decide whether the growth team should roll out the new checkout.
Evidence: Paid conversion is 23 percent and p95 latency is 480 milliseconds.
Constraints: Conversion must be at least 20 percent and latency must be below 500 milliseconds.
Success: Roll out only if every gate is satisfied; otherwise delay.
Owner: Growth team.

## Expected useful outcome

The executable exits with `Unsupported explicit fields:` followed by `- Owner`, then `Allowed: Decision, Evidence, Constraints, Success.` and `Place each extra meaning under its matching field.` It emits no complete-contract output or recommendation, does not drop the ownership meaning, does not assign it automatically, and does not add `Owner` to the schema.

## Actual outcome

Run 91 mentally simulates `python decision_brief.py SCENARIOS/090-no-repeated-allowed.md`. Unsupported-label detection finds `Owner`; the executable exits through `unsupported_template` with the unsupported label first, the unchanged allowed-field list, and the shorter remapping instruction. Missing-field checks, complete-contract output, audit requirements, and recommendation are not reached.

## Whether the system helped

yes

## What broke

The prior instruction, `Place each extra meaning under its matching allowed field.`, preserved the boundary but repeated `allowed` immediately after the schema line had already established which fields are allowed.

## What would make the result more useful

Test whether `matching field` remains unambiguous when more than one unsupported field is supplied.