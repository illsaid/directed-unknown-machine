# 020 — Supplied evidence directly violates the success gate

## Type

boundary-contract

## User

A growth lead preparing a recommendation on whether to roll out a tested annual pricing offer.

## Situation

Paid conversion clears the launch threshold, but the mature refund cohort directly exceeds the maximum refund rate allowed by the constraint.

## Input

Decision: Launch the annual pricing offer on Monday or delay it.
Evidence: Eighteen of 60 eligible users purchased the annual offer during the seven-day test. Of the 40 purchasers who reached 30 days after purchase, four requested refunds, for a 10% observed 30-day refund rate.
Constraints: Do not expose more users before the decision; do not infer refund behavior beyond the observed 30-day cohort; do not recommend launch if the observed 30-day refund rate exceeds 5%.
Success: Recommend launch on Monday if paid conversion is at least 20% and the supplied refund evidence satisfies the constraint; otherwise recommend delay.

## Expected useful outcome

Preserve the met conversion threshold and the directly failed refund gate, and require the analyst to identify the supplied 10% refund evidence as violating the 5% constraint rather than calling the gate unresolved or internally conflicting.

## Actual outcome

Run 21 preserves the complete four-field contract and requires every gate judgment to name the supplied evidence supporting it, so the 10% observed refund rate is explicitly tied to the violated 5% maximum.

## Whether the system helped

yes

## What broke

Before Run 21, the consistency requirement named violated constraints but did not require the analyst to identify which supplied evidence established the violation. A downstream analyst could label the gate failed without leaving an auditable evidence trail.

## What would make the result more useful

Next, test a decision with two independent constraints where one is satisfied and one is violated, verifying that the assignment reports each gate separately rather than collapsing the contract into one overall pass or fail.