# 098 — Detect a tab before an unsupported-label colon

## Type

hostile-regression

## User

An operator whose otherwise valid decision contract contains a tab between an unsupported field label and its colon.

## Situation

The input is a concrete rollout decision with all four allowed fields plus an `Owner` line whose label is separated from its colon by a tab. The test is whether unsupported-field validation applies the same horizontal-spacing boundary as allowed-field parsing instead of letting the extra meaning disappear into the preceding field value.

## Input

Decision: Decide whether the growth team should roll out the new checkout.
Evidence: Paid conversion is 23 percent and p95 latency is 480 milliseconds.
Constraints: Conversion must be at least 20 percent and latency must be below 500 milliseconds.
Success: Roll out only if every gate is satisfied; otherwise delay.
Owner	: Growth team owns implementation.

## Expected useful outcome

The executable exits with `Unsupported explicit fields:` followed by one `- Owner`, then `Allowed: Decision, Evidence, Constraints, Success.` and `Remap each extra meaning to one of those fields.` It does not absorb the ownership statement into Success, emit complete-contract output, infer a destination field, or add Owner to the schema.

## Actual outcome

Run 99 aligns unsupported-label detection with the existing horizontal-spacing grammar. `Owner\t:` is detected as one unsupported explicit field, its first supplied spelling is retained after trimming, and complete-contract processing stops before the extra meaning can be absorbed into Success.

## Whether the system helped

yes

## What broke

Before Run 99, unsupported-label detection allowed ordinary spaces inside a label but not tabs before the colon. `Owner\t:` therefore escaped the unsupported-field refusal even though allowed labels intentionally accept the same horizontal presentation variation.

## What would make the result more useful

Test whether a line break before an unsupported-label colon remains outside the explicit-field grammar rather than being normalized as horizontal spacing.
