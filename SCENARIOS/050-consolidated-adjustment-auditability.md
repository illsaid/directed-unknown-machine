# 050 — Consolidated adjustment auditability preserves unsupported-assumption boundary

## Type

structural-regression

## User

A product lead reviewing a delegated rollout assignment before it leaves the team.

## Situation

The executable separately requires preserving adjusted values, rejecting adjustments without an auditable method, and keeping transparent adjustments conditional when a governing assumption lacks support. These obligations may be one adjustment-auditability rule.

## Input

Decision: Roll out the checkout change to US web users on Monday or delay it.
Evidence: A 2,000-request canary measured unadjusted p95 latency at 560 milliseconds. Safari p95 was 820 milliseconds and non-Safari p95 was 390 milliseconds. The launch owner assumes Monday traffic will be 24% Safari but supplies no forecast, historical Monday mix, or other evidence supporting that weight. The supplied calculation is (0.24 × 820) + (0.76 × 390) = 493.2 milliseconds. Paid conversion was 23%.
Constraints: Paid conversion must be at least 20%, and Monday-rollout p95 latency must be below 500 milliseconds.
Success: Recommend rollout only if both gates are satisfied from supplied evidence; otherwise recommend delay.

## Expected useful outcome

Emit one inspectable adjustment-auditability rule that preserves the original 560-millisecond value, names the 493.2-millisecond adjusted value, supplied method, target population, and unsupported 24% Safari assumption, and leaves the latency gate unresolved because the assumption lacks supplied support. Conversion is satisfied, rollout is unsupported, and delay is recommended.

## Actual outcome

Run 51 consolidates three adjustment clauses into one rule. The output still preserves the original and adjusted values, method, target population, and governing assumption; because the 24% Safari weight lacks supplied support, the adjusted estimate remains conditional and cannot resolve the latency gate.

## Whether the system helped

yes

## What broke

Before Run 51, one auditability invariant was split across three bullets: preserve the adjustment context, reject opaque methods, and condition transparent methods on supported assumptions.

## What would make the result more useful

Next, inspect the source-exclusion requirement for duplicated wording that can be shortened without weakening the direct-observation and relevance boundaries.