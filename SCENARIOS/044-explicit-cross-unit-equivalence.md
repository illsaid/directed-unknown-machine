# 044 — Explicit cross-unit threshold equivalence

## Type

boundary-contract

## User

A product lead preparing a recommendation on whether to roll out a checkout change.

## Situation

The notes state the same latency threshold in milliseconds and seconds and explicitly declare the two representations equivalent.

## Input

Decision: Roll out the checkout change to US web users on Monday or delay it.
Evidence: The supported p95 latency range is 460 to 490 milliseconds. Paid conversion is 23%. For this decision, 500 milliseconds and 0.5 seconds are explicitly equivalent representations of the same latency threshold.
Constraints: Do not recommend rollout unless paid conversion is at least 20% and p95 response time for the Monday US web rollout population is at or below 500 milliseconds.
Success: Recommend rollout on Monday only if paid conversion is at least 20% and p95 response time is at or below 0.5 seconds; otherwise recommend delay.

## Expected useful outcome

Preserve both supplied latency representations and the explicit equivalence statement. Reconcile 500 milliseconds with 0.5 seconds using only that supplied equivalence, judge the supported 460–490 millisecond range as satisfying the inclusive latency gate, judge paid conversion as satisfied, and recommend rollout. Do not add or invoke an automatic unit converter.

## Actual outcome

Run 45 requires cross-unit thresholds to remain unresolved when equivalence is absent, but permits reconciliation when the contract explicitly supplies the equivalence. Both gates are satisfied and rollout follows from the supplied success rule.

## Whether the system helped

yes

## What broke

Before Run 45, the requirement stated the negative boundary but did not explicitly say that a supplied equivalence statement is sufficient to reconcile the representations without an automatic conversion engine.

## What would make the result more useful

Next, test whether an explicit precedence rule can reconcile genuinely different numeric thresholds without silently replacing either supplied value.