# 097 — Accept a tab before an allowed-label colon

## Type

hostile-regression

## User

An operator whose otherwise valid decision contract contains a tab between one allowed field label and its colon.

## Situation

The input is a concrete rollout decision with all four required meanings, but the `Decision` label is written with a tab before the colon. The test is whether horizontal presentation tolerance accepts the tab while the multiline refusal boundary from Run 97 remains intact.

## Input

Decision	: Decide whether the growth team should roll out the new checkout.
Evidence: Paid conversion is 23 percent and p95 latency is 480 milliseconds.
Constraints: Conversion must be at least 20 percent and latency must be below 500 milliseconds.
Success: Roll out only if every gate is satisfied; otherwise delay.

## Expected useful outcome

The executable emits `Contract: complete — 4/4 fields explicit; nothing inferred.`, preserves the full Decision value, prints all four fields and the six audit operations, and does not report `Decision` as missing or unsupported. The accepted tab must not imply acceptance of a line break before the colon.

## Actual outcome

Run 98 verifies that the existing `[ \t]*` allowed-label grammar accepts `Decision\t:` as horizontal presentation variation. All four values remain explicit and complete-contract output is reached. The Run 97 boundary is unchanged because newline characters are still excluded.

## Whether the system helped

yes

## What broke

Nothing in the executable. The Run 97 restriction was correctly narrow: it removed structural newline tolerance without accidentally rejecting tabs that belong to the intended horizontal-spacing allowance.

## What would make the result more useful

Test whether an unsupported label with a tab before its colon is still detected and repaired rather than escaping unsupported-field validation.
