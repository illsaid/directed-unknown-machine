# 096 — Reject a line break before an allowed-label colon

## Type

hostile-regression

## User

An operator whose notes contain a structurally broken field label and who needs the tool to request a repair rather than silently accept a multiline label.

## Situation

The input is a concrete rollout decision with all four required meanings, but the `Decision` label is split from its colon by a line break. The test is whether pre-colon tolerance remains limited to horizontal presentation spacing and refuses this structural variation as a missing explicit Decision field.

## Input

Decision
: Decide whether the growth team should roll out the new checkout.
Evidence: Paid conversion is 23 percent and p95 latency is 480 milliseconds.
Constraints: Conversion must be at least 20 percent and latency must be below 500 milliseconds.
Success: Roll out only if every gate is satisfied; otherwise delay.

## Expected useful outcome

The executable exits with `Missing explicit fields:` followed by `Decision:`. It does not emit complete-contract output, infer that the detached colon belongs to Decision, absorb the Decision text into another field, or broaden the four-field grammar to multiline labels.

## Actual outcome

Run 97 limits allowed-label pre-colon and post-colon padding to spaces and tabs. `Decision\n:` no longer matches `labeled_value()`, so the executable requests the missing explicit `Decision:` field while the remaining canonical fields stay structurally intact.

## Whether the system helped

yes

## What broke

Before Run 97, `labeled_value()` used `\s*` around the colon. Because `\s` includes newlines, `Decision\n:` was accepted as if it were harmless same-line spacing, weakening the explicit-field boundary established by the four-field contract.

## What would make the result more useful

Test whether a tab before the colon remains accepted as horizontal presentation variation without permitting any other multiline label structure.