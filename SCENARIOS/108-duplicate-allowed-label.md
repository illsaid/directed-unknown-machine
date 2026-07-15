# 108 — Refuse a duplicate allowed label

## Type

hostile

## User

An operator handing an analyst a bounded rollout decision whose Evidence contains interview prose formatted like an allowed field.

## Situation

A line inside the intended Evidence says `Success: depends on support coverage after launch.` The contract later supplies the real Success rule. Because both lines are structurally explicit `Success` fields, silently choosing the first would replace the authorized outcome and silently choosing the last would discard supplied prose.

## Input

Decision: Decide whether the growth team should roll out the new checkout.
Evidence: Paid conversion is 23 percent across 4,200 sessions.
Success: depends on support coverage after launch.
Constraints: Conversion must be at least 20 percent and latency must be below 500 milliseconds.
Success: Roll out only if every gate is satisfied; otherwise delay.

## Expected useful outcome

The executable refuses before extraction and reports `Success` as duplicated with both Input-relative line numbers. It does not guess which occurrence is prose, choose either value, merge them, or emit complete-contract output.

## Actual outcome

Run 110 adds a duplicate allowed-label preflight. The scenario exits with `Duplicate explicit fields:` and reports `Success (input lines 3 and 5)` before any field value is extracted.

## Whether the system helped

yes

## What broke

Before Run 110, `labeled_value()` selected the first structurally explicit `Success` occurrence. The interview sentence became the authorized Success rule, while the actual rollout rule was silently ignored.

## What would make the result more useful

Verify that ordinary continuation prose beginning with an allowed-label word but without a colon remains inside Evidence and does not trigger duplicate-field refusal.