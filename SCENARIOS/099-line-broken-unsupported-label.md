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

Run 100 shows that the current executable keeps `Owner\n:` outside unsupported-label detection, but field extraction then absorbs both lines into the Success value and emits complete-contract output. The horizontal-spacing boundary survives, but the contract-preservation claim does not: malformed label-like content can silently alter a supported field.

## Whether the system helped

partial

## What broke

The explicit-label regex correctly excludes newlines, but there is no separate refusal for a label-only line followed by a colon-start line. Because allowed-field extraction stops only at another valid allowed label, the malformed ownership fragment becomes part of Success.

## What would make the result more useful

Add one narrow malformed-label refusal for a label-only line immediately followed by a colon-start line, without treating that structure as a valid explicit field or broadening normal label parsing.
