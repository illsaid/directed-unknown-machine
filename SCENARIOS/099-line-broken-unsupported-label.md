# 099 — Refuse a line-broken unsupported label without normalizing it

## Type

hostile-regression

## User

An operator whose otherwise valid decision contract contains an unsupported field name on one line and its colon at the start of the next line.

## Situation

The input is a concrete rollout decision with all four allowed fields plus a visually label-like `Owner\n:` fragment. The test is whether the tool keeps that malformed structure outside the explicit-label grammar while also preventing its ownership meaning from silently contaminating the preceding Success field.

## Input

Decision: Decide whether the growth team should roll out the new checkout.
Evidence: Paid conversion is 23 percent and p95 latency is 480 milliseconds.
Constraints: Conversion must be at least 20 percent and latency must be below 500 milliseconds.
Success: Roll out only if every gate is satisfied; otherwise delay.
Owner
: Growth team owns implementation.

## Expected useful outcome

The executable refuses the malformed label structure before emitting complete-contract output. It does not normalize `Owner\n:` into a valid explicit field, absorb the ownership statement into Success, infer a destination field, or add Owner to the schema.

## Actual outcome

Run 101 adds a narrow preflight check for an unsupported label-only line immediately followed by a colon-start line. The executable now exits with `Malformed explicit fields:`, one `- Owner`, and `Keep each field label and colon on the same line.` It does not treat `Owner\n:` as valid, reach field extraction, or contaminate Success. Allowed labels remain excluded from this check, so the established `Decision\n:` missing-field boundary is unchanged.

## Whether the system helped

yes

## What broke

Before Run 101, the malformed unsupported fragment stayed outside explicit-label detection but was absorbed into Success because field extraction stopped only at another valid allowed label.

## What would make the result more useful

Verify that a line-broken allowed label such as `Decision\n:` still follows the existing missing-field refusal rather than being reclassified as a malformed unsupported field.