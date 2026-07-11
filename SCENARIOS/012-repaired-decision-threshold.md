# 012 — Repaired decision threshold

## Type

contract-repair

## User

A growth lead preparing a recommendation on whether to continue a paid acquisition test.

## Situation

The operator repaired Scenario 011 by moving the stopping rule under Success without changing its wording.

## Input

Decision: Continue the paid acquisition test for another week or stop it now.
Evidence: The test spent $1,800, acquired 41 trial users, and converted 6 to paid accounts.
Constraints: Do not project lifetime value; do not assume conversion will improve; separate observed results from expectations.
Success: Continue only if paid conversion reaches at least 18% by the end of the next seven days. Recommend continue or stop and make the reversal condition explicit.

## Expected useful outcome

Accept the repaired four-field contract, preserve the 18% stopping rule exactly, and make the recommendation answerable against that rule without adding a Threshold field.

## Actual outcome

Run 13 accepts all four explicit fields, preserves the 18% stopping rule under Success, and requires the final recommendation to state how the supplied success or reversal rule governs the action.

## Whether the system helped

yes

## What broke

Before Run 13, the repaired threshold text survived parsing, but the fixed deliverable only said to test the recommendation against the success condition; it did not require the brief to state how that rule governs continuation or reversal.

## What would make the result more useful

Test a repaired unsupported field whose meaning belongs under Evidence rather than Success; keep the schema fixed unless that repair loses meaning.