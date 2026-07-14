# 093 — Collapse case-variant unsupported labels

## Type

hostile-regression

## User

An operator who supplied two distinct ownership notes under case variants of the same unsupported label and needs one concise schema repair without losing either source meaning.

## Situation

The input is a concrete rollout decision with all four allowed fields plus `Owner` and `owner` lines containing distinct meanings. The test is whether repair treats label case as insignificant, reports the schema defect once using the first supplied spelling, and leaves both meanings untouched for manual remapping.

## Input

Decision: Decide whether the growth team should roll out the new checkout.
Evidence: Paid conversion is 23 percent and p95 latency is 480 milliseconds.
Constraints: Conversion must be at least 20 percent and latency must be below 500 milliseconds.
Success: Roll out only if every gate is satisfied; otherwise delay.
Owner: Growth team owns implementation.
owner: Finance owns final approval.

## Expected useful outcome

The executable exits with `Unsupported explicit fields:` followed by one `- Owner`, then `Allowed: Decision, Evidence, Constraints, Success.` and `Remap each extra meaning to one of those fields.` It does not emit a second `- owner`, alter or discard either ownership note, infer where either meaning belongs, emit complete-contract output, or add an ownership field to the schema.

## Actual outcome

Run 94 mentally simulates `python decision_brief.py SCENARIOS/093-case-variant-unsupported-label.md`. `unsupported_labels` lowers both labels to the same deduplication key, retains the first supplied spelling `Owner`, and exits through `unsupported_template` with one repair item. Both source lines remain untouched for operator-directed remapping; missing-field checks, complete-contract output, audit requirements, and recommendation are not reached.

## Whether the system helped

yes

## What broke

Nothing in this boundary. The Run 93 case-insensitive deduplication correctly treats `Owner` and `owner` as one unsupported field type while preserving the first spelling for the repair output.

## What would make the result more useful

Test whether harmless spacing before the colon, such as `Owner :`, should normalize to the same unsupported label without producing a duplicate repair item.
