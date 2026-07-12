# 056 — Consolidated recommendation preserves fallback governance

## Type

structural-regression

## User

A product lead reviewing a delegated rollout decision before it leaves the team.

## Situation

The Decision group separately requires one recommendation and an explanation of how the supplied success or reversal rule governs it. These may be one invariant if the output still names one action and applies the operator's fallback exactly.

## Input

Decision: Roll out the checkout change to US web users on Monday or delay it.
Evidence: Paid conversion was 23%. P95 latency was 540 milliseconds.
Constraints: Paid conversion must be at least 20%, and p95 latency must be below 500 milliseconds.
Success: Recommend rollout only if every constraint is satisfied from supplied evidence; otherwise recommend delay.

## Expected useful outcome

Emit one concise Decision requirement that both recommends one action and states how the supplied success or reversal rule governs it. Conversion is satisfied, latency is violated, and the operator-supplied fallback therefore requires delay. The consolidation must not permit a recommendation without showing why the fallback applies.

## Actual outcome

Run 57 consolidates the two Decision governance bullets into one inspectable invariant. The output still requires exactly one action and requires that action to be governed by the supplied success or reversal rule. For this scenario, the violated latency gate triggers the supplied fallback, so delay remains the supported recommendation.

## Whether the system helped

yes

## What broke

Before Run 57, recommending one action and applying the supplied success or reversal rule were expressed as separate bullets even though a bounded recommendation is incomplete without its governing fallback.

## What would make the result more useful

Next, inspect whether the two remaining Decision requirements can be consolidated without weakening the distinction between evidence status and conflicting interpretations.