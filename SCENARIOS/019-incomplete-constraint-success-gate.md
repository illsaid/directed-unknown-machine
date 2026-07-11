# 019 — Supplied evidence is insufficient to resolve the success gate

## Type

boundary-contract

## User

A growth lead preparing a recommendation on whether to roll out a tested annual pricing offer.

## Situation

Paid conversion clears the launch threshold, but only a small fraction of purchasers have reached the required 30-day refund observation window.

## Input

Decision: Launch the annual pricing offer on Monday or delay it.
Evidence: Eighteen of 60 eligible users purchased the annual offer during the seven-day test. Eight purchasers have reached 30 days after purchase and none requested a refund; the other ten purchasers have not yet reached 30 days.
Constraints: Do not expose more users before the decision; do not infer refund behavior for purchasers who have not reached 30 days; do not recommend launch until 30-day refund outcomes are available for at least 15 purchasers and the observed refund rate does not exceed 5%.
Success: Recommend launch on Monday if paid conversion is at least 20% and the supplied refund evidence satisfies the constraint; otherwise recommend delay.

## Expected useful outcome

Preserve the met conversion threshold and incomplete refund cohort, and require the analyst to identify the refund gate as unresolved because evidence is insufficient rather than calling it satisfied, violated, or internally conflicting.

## Actual outcome

Run 20 preserves the complete four-field contract and requires the analyst to distinguish an unresolved gate caused by insufficient evidence from a satisfied or violated constraint before recommending an action.

## Whether the system helped

yes

## What broke

Before Run 20, the consistency requirement distinguished satisfied constraints from genuine conflicts, but did not explicitly name insufficient evidence as a separate state. An analyst could misdescribe the immature refund cohort as a conflict or treat zero observed refunds as a pass.

## What would make the result more useful

Next, test a decision where the supplied evidence directly violates a constraint, verifying that the same requirement identifies a failed gate without calling it missing evidence or an internal conflict.