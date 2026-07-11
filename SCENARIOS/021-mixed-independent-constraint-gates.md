# 021 — Independent constraints split between pass and fail

## Type

boundary-contract

## User

A growth lead preparing a recommendation on whether to roll out a tested annual pricing offer.

## Situation

Paid conversion clears the launch threshold, one independent operational constraint is satisfied, and one independent refund constraint is violated.

## Input

Decision: Launch the annual pricing offer on Monday or delay it.
Evidence: Eighteen of 60 eligible users purchased the annual offer during the seven-day test. Support handled all 18 purchasers without exceeding current staffing capacity. Of the 40 purchasers who reached 30 days after purchase, four requested refunds, for a 10% observed 30-day refund rate.
Constraints: Do not recommend launch if support cannot handle the observed purchaser volume within current staffing capacity. Do not recommend launch if the observed 30-day refund rate exceeds 5%.
Success: Recommend launch on Monday only if paid conversion is at least 20% and both supplied constraints are satisfied; otherwise recommend delay.

## Expected useful outcome

Preserve the met conversion threshold, identify the support-capacity constraint as satisfied from supplied evidence, identify the refund constraint as violated from the supplied 10% rate, and require the analyst to report the two gate judgments separately before recommending delay.

## Actual outcome

Run 22 preserves the complete four-field contract and requires a separate evidence-backed judgment for each constraint, preventing the satisfied support gate from disappearing inside an overall failed result.

## Whether the system helped

yes

## What broke

Before Run 22, the consistency requirement named gate states and supporting evidence but did not explicitly require each independent constraint to receive its own judgment. A downstream analyst could collapse the contract into one overall failure and omit the satisfied support-capacity gate.

## What would make the result more useful

Next, test two constraints that depend on the same evidence but use different thresholds, verifying that separate reporting does not imply false independence.