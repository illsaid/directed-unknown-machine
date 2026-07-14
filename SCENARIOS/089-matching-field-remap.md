# 089 — Shorten unsupported-field remapping guidance

## Type

hostile-regression

## User

An operator who supplied a complete four-field decision contract plus one unsupported ownership field and needs the repair to preserve that ownership meaning without expanding the schema or pretending to classify it automatically.

## Situation

The input is a concrete rollout decision with all four allowed fields and an extra `Owner` field. The test is whether the remapping instruction can become shorter and more direct while still requiring the operator to place the extra meaning under the matching allowed field.

## Input

Decision: Decide whether the growth team should roll out the new checkout.
Evidence: Paid conversion is 23 percent and p95 latency is 480 milliseconds.
Constraints: Conversion must be at least 20 percent and latency must be below 500 milliseconds.
Success: Roll out only if every gate is satisfied; otherwise delay.
Owner: Growth team.

## Expected useful outcome

The executable exits with `Unsupported explicit fields:` followed by `- Owner`, then `Allowed: Decision, Evidence, Constraints, Success.` and `Place each extra meaning under its matching allowed field.` It emits no complete-contract output or recommendation, does not drop the ownership meaning, does not assign it automatically, and does not add `Owner` to the schema.

## Actual outcome

Run 90 mentally simulates `python decision_brief.py SCENARIOS/089-matching-field-remap.md`. Unsupported-label detection finds `Owner`; the executable exits through `unsupported_template` with the unsupported label first, the unchanged allowed-field list, and the shorter remapping instruction. Missing-field checks, complete-contract output, audit requirements, and recommendation are not reached.

## Whether the system helped

yes

## What broke

The prior instruction, `Move each extra meaning under the allowed field matching its role.`, preserved the boundary but used a longer verb phrase and repeated the matching relationship indirectly.

## What would make the result more useful

Test whether `Allowed:` and `matching allowed field` can avoid repeating `allowed` without weakening the fixed-schema boundary.
