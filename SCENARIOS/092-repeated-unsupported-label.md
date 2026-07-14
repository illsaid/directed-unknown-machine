# 092 — Collapse repeated unsupported labels

## Type

hostile-regression

## User

An operator who supplied a complete four-field decision contract plus two separate ownership notes under the same unsupported label and needs a concise repair that preserves both source meanings without repeating the same schema defect.

## Situation

The input is a concrete rollout decision with all four allowed fields plus two `Owner` lines containing distinct meanings. The test is whether the repair reports the unsupported label once while leaving both ownership notes intact for manual remapping.

## Input

Decision: Decide whether the growth team should roll out the new checkout.
Evidence: Paid conversion is 23 percent and p95 latency is 480 milliseconds.
Constraints: Conversion must be at least 20 percent and latency must be below 500 milliseconds.
Success: Roll out only if every gate is satisfied; otherwise delay.
Owner: Growth team owns implementation.
Owner: Finance owns final approval.

## Expected useful outcome

The executable exits with `Unsupported explicit fields:` followed by one `- Owner`, then `Allowed: Decision, Evidence, Constraints, Success.` and `Remap each extra meaning to one of those fields.` It does not repeat the same unsupported label, alter or discard either ownership note, infer where either meaning belongs, emit complete-contract output, or add `Owner` to the schema.

## Actual outcome

Run 93 mentally simulates `python decision_brief.py SCENARIOS/092-repeated-unsupported-label.md`. Unsupported-label detection sees both `Owner` lines, preserves the first label spelling, collapses the repeated case-insensitive label, and exits through `unsupported_template` with one `- Owner`. Both source lines remain untouched in the scenario for operator-directed remapping; missing-field checks, complete-contract output, audit requirements, and recommendation are not reached.

## Whether the system helped

yes

## What broke

The prior implementation listed every unsupported-label occurrence. Repeating `- Owner` described the same schema violation twice without exposing or protecting the distinct meanings any better; those meanings already remain in the untouched source notes.

## What would make the result more useful

Test whether unsupported labels that differ only by case should preserve the first spelling while still collapsing to one repair item.