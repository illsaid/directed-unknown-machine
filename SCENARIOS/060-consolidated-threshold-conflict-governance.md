# 060 — Consolidated threshold conflict rule preserves distinct reconciliation paths

## Type

structural-regression

## User

A product lead reviewing a delegated checkout rollout decision before it leaves the team.

## Situation

The Threshold conflict group separately governs unresolved conflicting rules, explicit precedence, and cross-unit equivalence. These may be one invariant only if support for one reconciliation path cannot silently authorize another.

## Input

Decision: Roll out the checkout change to US web users on Monday or delay it.
Evidence: Paid conversion was 21%. P95 latency was 480 milliseconds.
Constraints: Paid conversion must be at least 20% in the context note and at least 22% in the governing success rule; the contract explicitly says the success rule takes precedence while the 20% rule remains visible. P95 latency must be below 500 milliseconds in one note and below 0.5 seconds in another; no conversion or equivalence between those representations is supplied.
Success: Recommend rollout only if every gate is satisfied; otherwise recommend delay. Apply the supplied precedence to paid conversion, report that 21% satisfies the displaced 20% rule but violates the governing 22% rule, and preserve both. Do not use that precedence statement to reconcile the latency thresholds. Leave latency unresolved because no cross-unit equivalence was supplied.

## Expected useful outcome

Emit one concise Threshold conflict requirement with distinct branches under one preservation-and-exact-support invariant. Paid conversion is governed by the supplied 22% precedence rule while both thresholds and both results remain visible. Latency remains unresolved because support for precedence does not supply a millisecond-to-second equivalence. Because conversion is violated and latency unresolved, delay is the governed recommendation.

## Actual outcome

Run 61 consolidates the three Threshold conflict bullets into one inspectable invariant. It still preserves every threshold statement, permits precedence only for the same-metric conflict explicitly governed by it, preserves the displaced conversion rule and its separate result, and refuses to treat that precedence as cross-unit equivalence. Conversion is violated under the governing 22% rule, latency remains unresolved, and delay remains the governed recommendation.

## Whether the system helped

yes

## What broke

Before Run 61, unresolved conflicts, precedence, and cross-unit equivalence were expressed as three bullets even though all enforce one boundary: a conflict may be resolved only by supplied support for the exact reconciliation being used.

## What would make the result more useful

Next, inspect whether the seven requirement-group labels still represent distinct audit questions or whether any adjacent groups can be merged without hiding a decision boundary.
