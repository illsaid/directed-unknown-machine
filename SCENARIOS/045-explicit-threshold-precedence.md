# 045 — Explicit precedence between numeric thresholds

## Type

boundary-contract

## User

A product lead preparing a recommendation on whether to roll out a checkout change.

## Situation

The notes contain two genuinely different conversion thresholds, but explicitly state which threshold governs the rollout decision.

## Input

Decision: Roll out the checkout change to US web users on Monday or delay it.
Evidence: Paid conversion is 21%. The supported p95 latency range is 460 to 490 milliseconds. For this rollout decision, the Success threshold governs if it conflicts with the Constraints threshold; the Constraints threshold remains contextual and must still be reported.
Constraints: Do not recommend rollout unless paid conversion is at least 20% and p95 response time is at or below 500 milliseconds.
Success: Recommend rollout on Monday only if paid conversion is at least 22% and p95 response time is at or below 500 milliseconds; otherwise recommend delay.

## Expected useful outcome

Preserve both conversion thresholds and the explicit precedence rule. State that 21% satisfies the contextual 20% threshold but violates the governing 22% Success threshold. Judge latency satisfied and recommend delay under the supplied fallback. Do not silently delete or rewrite the non-governing threshold.

## Actual outcome

Run 46 requires an explicit precedence rule to identify the governing threshold while preserving the displaced threshold and its result. Conversion violates the governing 22% threshold, latency is satisfied, and delay follows from the supplied Success rule.

## Whether the system helped

yes

## What broke

Before Run 46, the brief allowed reconciliation when precedence was supplied but did not explicitly require the non-governing threshold and its separate judgment to remain visible.

## What would make the result more useful

Next, simplify the accumulated gate requirements into a smaller inspectable structure without weakening the preservation rules.