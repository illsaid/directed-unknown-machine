# 061 — Consolidated boundary evaluation preserves range and equality semantics

## Type

structural-regression

## User

A product lead reviewing a delegated checkout rollout decision before it leaves the team.

## Situation

The Sensitivity and Threshold semantics groups both govern how supplied evidence relates to a decision boundary. They may be one audit group only if full-range treatment, explicit equality wording, and the no-comparator refusal boundary remain distinct.

## Input

Decision: Roll out the checkout change to US web users on Monday or delay it.
Evidence: Paid conversion was exactly 20%. P95 latency has a supported sensitivity range of 480 to 520 milliseconds. Seven-day retention was exactly 70%.
Constraints: Paid conversion must be at least 20%. P95 latency must be below 500 milliseconds. The seven-day retention threshold is 70%, with no supplied statement saying whether equality passes or fails.
Success: Recommend rollout only if every gate is satisfied; otherwise recommend delay. Treat conversion equality as satisfying the inclusive minimum. Preserve the full latency range and leave the latency gate conditional because the range crosses the strict maximum. Leave retention unresolved because its threshold has no comparator. Do not select a representative latency value or infer comparison semantics for retention.

## Expected useful outcome

Emit one concise Boundary evaluation group that governs both ranges and equality from the supplied boundary wording. Conversion is satisfied, latency is conditional because its full range crosses the threshold, and retention is unresolved because equality semantics were not supplied. Because not every gate is satisfied, delay is the governed recommendation.

## Actual outcome

Run 62 merges the adjacent Sensitivity and Threshold semantics groups into one Boundary evaluation group while retaining two inspectable requirements: one for full-range treatment and one for equality semantics. Conversion remains satisfied, latency remains conditional from the complete 480–520 millisecond range, retention remains unresolved, and delay remains the governed recommendation.

## Whether the system helped

yes

## What broke

Before Run 62, range evaluation and equality evaluation appeared as separate top-level audit groups even though both ask how supplied evidence relates to a stated boundary. This made the seven-group structure more fragmented than the underlying decision contract required.

## What would make the result more useful

Next, inspect whether Boundary evaluation and Threshold conflict remain distinct audit questions: ordinary boundary application versus choosing among incompatible boundary statements.