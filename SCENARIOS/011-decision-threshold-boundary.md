# 011 — Decision threshold boundary

## Type

contract-boundary

## User

A growth lead preparing a recommendation on whether to continue a paid acquisition test.

## Situation

The team must decide whether to continue the campaign, but the operator has supplied the stopping rule as its own explicit field.

## Input

Decision: Continue the paid acquisition test for another week or stop it now.
Evidence: The test spent $1,800, acquired 41 trial users, and converted 6 to paid accounts.
Threshold: Continue only if paid conversion reaches at least 18% by the end of the next seven days.
Constraints: Do not project lifetime value; do not assume conversion will improve; separate observed results from expectations.
Success: Recommend continue or stop and make the reversal condition explicit.

## Expected useful outcome

Reject the unsupported Threshold field without telling the operator to move it under Constraints. The repair instruction should preserve its role as a success or decision rule and avoid inventing a fifth field.

## Actual outcome

Run 12 rejects Threshold and tells the operator to place its meaning under the supported field that preserves its role, naming Decision, Evidence, Constraints, and Success rather than forcing it into Constraints.

## Whether the system helped

yes

## What broke

Before Run 12, every unsupported field was told to move under Constraints. That advice would misclassify this stopping rule and weaken the decision contract.

## What would make the result more useful

Test whether operators can repair two differently named boundary fields without losing meaning; do not add aliases unless repeated scenarios prove one is necessary.
