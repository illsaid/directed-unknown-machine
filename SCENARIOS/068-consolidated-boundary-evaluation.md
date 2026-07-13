# 068 — Boundary evaluation is one application invariant

## Type

structural-regression

## User

A product lead delegating a rollout decision with both uncertain ranges and exact boundary values.

## Situation

Boundary evaluation currently uses one requirement for full-range sensitivity handling and another for equality semantics. They should become one invariant only if the combined wording still resolves same-side ranges, preserves threshold-crossing conditionality, honors explicit strict and inclusive comparators, and refuses to invent semantics for a bare threshold.

## Input

Decision: Roll out the checkout change or delay it.
Evidence: Paid conversion is exactly 20%. P95 latency is estimated at 480–520 milliseconds. Thirty-day retention is exactly 70%.
Constraints: Paid conversion must be at least 20%. P95 latency must be below 500 milliseconds. The retention threshold is 70%, with no strict or inclusive comparator supplied. Evaluate the complete latency range rather than selecting one point.
Success: Recommend rollout only if every gate is satisfied. Treat conversion equality as satisfying the inclusive minimum, preserve latency as conditional because its range crosses the strict maximum, leave retention unresolved because its comparator is missing, and therefore recommend delay.

## Expected useful outcome

Boundary evaluation appears as one invariant. It evaluates the complete 480–520 millisecond range, states that values below 500 satisfy latency while values at or above 500 violate it, treats conversion at 20% as satisfying “at least 20%,” and leaves retention at 70% unresolved because the contract supplies no equality semantics. Gate judgments keep the three outcomes separate, and the governed recommendation is delay.

## Actual outcome

Run 69 consolidates full-range handling and supplied equality semantics into one Boundary evaluation requirement. The combined invariant still prohibits point-selection from a range, resolves same-side ranges from the whole range, applies explicit inclusive and strict wording at equality, and preserves the no-comparator refusal boundary.

## Whether the system helped

yes

## What broke

Before Run 69, applying evidence to one boundary was expressed as two adjacent requirements even though range position and equality are both cases of the same operation: evaluate all supplied evidence against the boundary exactly as written.

## What would make the result more useful

Next, inspect whether Boundary reconciliation and Boundary evaluation can share a shorter common vocabulary without merging the distinct operations.