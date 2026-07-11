# 018 — Supplied evidence satisfies the success gate

## Type

transfer-contract

## User

A growth lead preparing a recommendation on whether to roll out a tested annual pricing offer.

## Situation

The success rule points toward launch, while a constraint requires refund evidence before launch. Unlike the prior scenario, the required evidence is supplied and satisfies the constraint.

## Input

Decision: Launch the annual pricing offer on Monday or delay it.
Evidence: Eighteen of 60 eligible users purchased the annual offer during the seven-day test. Of the 40 test users who reached 30 days after purchase, one requested a refund, for a 2.5% observed 30-day refund rate.
Constraints: Do not expose more users before the decision; do not infer refund behavior beyond the observed 30-day cohort; do not recommend launch if the observed 30-day refund rate exceeds 5%.
Success: Recommend launch on Monday if paid conversion is at least 20% and the supplied refund evidence satisfies the constraint; otherwise recommend delay.

## Expected useful outcome

Preserve the conversion and refund evidence, recognize that the supplied 2.5% refund rate satisfies the 5% constraint, and require the analyst to distinguish a satisfied gate from a genuine Constraints/Success conflict.

## Actual outcome

Run 19 preserves the complete four-field contract and changes the consistency requirement so the analyst must distinguish satisfied constraints from genuine conflicts before stating whether a recommendation is supported.

## Whether the system helped

yes

## What broke

Before Run 19, the assignment said to identify apparent conflicts between Constraints and Success. In a gated decision where supplied evidence already satisfies the constraint, that wording could encourage the analyst to frame ordinary consistency checking as a conflict.

## What would make the result more useful

Next, test a scenario where supplied evidence is incomplete rather than clearly satisfying or violating the constraint, and verify that the assignment leaves the gate unresolved without inventing a blocker or a pass.
