# 109 — Preserve allowed-label words in ordinary prose

## Type

hostile regression

## User

An operator handing an analyst a bounded rollout decision whose Evidence contains ordinary prose beginning with an allowed field name.

## Situation

A continuation sentence begins with `Success` but has no colon and is not a second field. The duplicate-field refusal must remain structural rather than treating any allowed-label word at the start of a line as schema.

## Input

Decision: Decide whether the growth team should roll out the new checkout.
Evidence: Paid conversion is 23 percent across 4,200 sessions.
Success depends on support coverage after launch, which is not yet confirmed.
Constraints: Conversion must be at least 20 percent and latency must be below 500 milliseconds.
Success: Roll out only if every gate is satisfied; otherwise delay.

## Expected useful outcome

The executable reaches complete-contract output, preserves the `Success depends...` sentence inside Evidence, and does not report a duplicate `Success` field.

## Actual outcome

Run 111 verified the current structural grammar already behaves correctly. `duplicate_allowed_labels()` requires a same-line colon, while `labeled_value()` keeps the continuation sentence inside Evidence until the later explicit `Constraints:` label. The contract reaches complete output with exactly one Success field.

## Whether the system helped

yes

## What broke

Nothing. The duplicate-field refusal added in Run 110 is narrow enough not to classify an allowed-label word without a colon as schema.

## What would make the result more useful

Stop extending label-format permutations. Test the compiled contract against a fresh real decision handoff to determine whether the six audit obligations improve downstream execution rather than only parser correctness.
