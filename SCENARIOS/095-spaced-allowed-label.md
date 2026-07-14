# 095 — Accept spacing before an allowed-label colon

## Type

hostile-regression

## User

An operator whose otherwise valid decision contract contains harmless spacing before one allowed field’s colon.

## Situation

The input is a concrete rollout decision with all four required meanings, but the `Decision` label is written as `Decision :`. The test is whether the parser treats that spacing as presentation variation, preserves the field value, and emits the same complete contract as the canonical spelling.

## Input

Decision : Decide whether the growth team should roll out the new checkout.
Evidence: Paid conversion is 23 percent and p95 latency is 480 milliseconds.
Constraints: Conversion must be at least 20 percent and latency must be below 500 milliseconds.
Success: Roll out only if every gate is satisfied; otherwise delay.

## Expected useful outcome

The executable emits `Contract: complete — 4/4 fields explicit; nothing inferred.`, preserves the full Decision value, prints all four fields and the six audit operations, and does not report `Decision` as missing or unsupported.

## Actual outcome

Run 96 updates `labeled_value()` so allowed labels may contain insignificant whitespace immediately before the colon, including in the next-label boundary. `Decision :` is parsed as the existing Decision field, all four values remain explicit, and complete-contract output is reached without schema expansion or semantic inference.

## Whether the system helped

yes

## What broke

Before Run 96, unsupported-label detection normalized `Decision :` to an allowed label, but `labeled_value()` required `Decision:` exactly. The same line therefore escaped unsupported-field repair and was then falsely reported as a missing Decision field.

## What would make the result more useful

Test whether spacing after a label name but before a colon should remain bounded to horizontal whitespace rather than accepting line breaks or other structural variation.