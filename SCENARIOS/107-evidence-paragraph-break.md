# 107 — Preserve an Evidence paragraph break

## Type

transfer

## User

An operator handing an analyst a bounded rollout decision whose Evidence contains two deliberately separated paragraphs.

## Situation

A complete four-field contract contains a blank line inside Evidence. The test is whether the handoff preserves that paragraph boundary without treating the second paragraph as a new field or ending Evidence early.

## Input

Decision: Decide whether the growth team should roll out the new checkout.
Evidence: Paid conversion is 23 percent across 4,200 sessions.

Interview notes say accountability remains unclear after launch.
Constraints: Conversion must be at least 20 percent and latency must be below 500 milliseconds.
Success: Roll out only if every gate is satisfied; otherwise delay.

## Expected useful outcome

The executable reaches `Contract: complete` and prints the Evidence value with the blank line intact between the measurement and interview-note paragraphs. It does not trigger structural repair, infer a field boundary, or flatten the paragraphs.

## Actual outcome

Run 109 confirms the existing extraction preserves the blank-line paragraph break exactly because the field terminates only at the next explicit allowed label.

## Whether the system helped

yes

## What broke

Nothing. The Run 108 change from internal whitespace normalization to surrounding-whitespace stripping already preserves paragraph separation.

## What would make the result more useful

Stop expanding whitespace permutations. Test a real handoff risk in which a continuation line begins with an allowed-label word but is ordinary prose rather than a field.