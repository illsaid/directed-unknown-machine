# 101 — Locate a malformed unsupported label inside a valid contract

## Type

hostile-regression

## User

An operator whose otherwise valid decision contract contains a malformed unsupported field between two required fields and who needs to find the exact repair point without inspecting the whole handoff.

## Situation

The input is a concrete rollout decision with `Owner` on one line and its colon at the start of the next line between Evidence and Constraints. The test is whether the tool refuses before field extraction, preserves both neighboring allowed fields, and identifies where the malformed fragment occurs.

## Input

Decision: Decide whether the growth team should roll out the new checkout.
Evidence: Paid conversion is 23 percent and p95 latency is 480 milliseconds.
Owner
: Growth team owns implementation.
Constraints: Conversion must be at least 20 percent and latency must be below 500 milliseconds.
Success: Roll out only if every gate is satisfied; otherwise delay.

## Expected useful outcome

The executable exits with `Malformed explicit fields:` followed by `- Owner (line 3)` and the existing same-line repair instruction. It does not absorb ownership into Evidence, Constraints, or Success; normalize `Owner\n:`; infer a destination field; or emit complete-contract output.

## Actual outcome

Run 103 changes the malformed-label preflight to retain the input line number while preserving its narrow grammar and case-insensitive deduplication. The executable now exits with `Malformed explicit fields:`, `- Owner (line 3)`, and `Keep each field label and colon on the same line.` Because the refusal still runs before field extraction, neither neighboring allowed field is contaminated.

## Whether the system helped

yes

## What broke

The Run 101 refusal prevented contamination but reported only the label name. Once the malformed fragment appears inside a complete contract, the repair requires searching the handoff to find the detached colon.

## What would make the result more useful

Verify that repeated malformed occurrences of the same unsupported label still collapse to one repair item while preserving the first occurrence line number.
