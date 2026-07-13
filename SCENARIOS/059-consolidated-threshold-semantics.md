# 059 — Consolidated threshold semantics preserve the no-comparator boundary

## Type

structural-regression

## User

A product lead reviewing a delegated checkout rollout decision before it leaves the team.

## Situation

The Threshold semantics group separately governs equality under explicit strict or inclusive wording and equality when the contract supplies a number but no comparator. These may be one invariant only if the absence of comparison wording still leaves equality unresolved rather than inheriting a convention.

## Input

Decision: Roll out the checkout change to US web users on Monday or delay it.
Evidence: Paid conversion was exactly 20%. P95 latency was exactly 500 milliseconds. Seven-day retention was exactly 70%.
Constraints: Paid conversion must be at least 20%. P95 latency must be below 500 milliseconds. The seven-day retention threshold is 70%, with no supplied statement saying whether equality passes or fails.
Success: Recommend rollout only if every gate is satisfied; otherwise recommend delay. Treat equality as satisfying the explicitly inclusive conversion gate, violating the explicitly strict latency gate, and unresolved for retention because its threshold has no comparator. Do not infer strict or inclusive semantics for retention.

## Expected useful outcome

Emit one concise Threshold semantics requirement that resolves equality only from supplied comparison wording. Conversion is satisfied, latency is violated, and retention remains unresolved. Because not every gate is satisfied, delay is the governed recommendation.

## Actual outcome

Run 60 consolidates the two Threshold semantics bullets into one inspectable invariant. Equality follows supplied inclusive or strict wording when present and remains unresolved when comparison wording is absent. Conversion is satisfied, latency is violated, retention is unresolved, and delay remains the governed recommendation.

## Whether the system helped

yes

## What broke

Before Run 60, explicit equality semantics and missing-comparator handling were separate bullets even though both are governed by the same boundary: equality may be resolved only from comparison wording actually supplied by the contract.

## What would make the result more useful

Next, inspect whether the three Threshold conflict requirements can be reduced without allowing precedence, reconciliation, and cross-unit equivalence to substitute for one another.