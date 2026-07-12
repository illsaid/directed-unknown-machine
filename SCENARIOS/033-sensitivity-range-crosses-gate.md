# 033 — Sensitivity range crosses the decision gate

## Type

boundary-contract

## User

A product lead preparing a recommendation on whether to roll out a checkout change.

## Situation

The notes supply an auditable latency adjustment and a supported range for the uncertain target-population weight. The resulting latency range crosses the rollout threshold, so no single point estimate resolves the gate.

## Input

Decision: Roll out the checkout change to US web users on Monday or delay it.
Evidence: A 10,000-request production-shadow test measured p95 response time at 430 milliseconds for the current US web traffic mix. A separate 2,000-request canary test measured an unadjusted p95 response time of 560 milliseconds. The canary's supplied browser-segment measurements were Safari p95 820 milliseconds and non-Safari p95 390 milliseconds. Historical Monday traffic observations support a Safari share between 20% and 30%. Applying the supplied formula (Safari share × 820) + (remaining share × 390) gives a sensitivity range of 476 milliseconds at 20% Safari to 519 milliseconds at 30% Safari. The supplied threshold calculation shows that the adjusted estimate reaches 500 milliseconds at approximately 25.6% Safari. Paid conversion was 23%.
Constraints: Do not recommend rollout unless p95 response time for the Monday US web rollout population is confirmed below 500 milliseconds.
Success: Recommend rollout on Monday only if paid conversion is at least 20% and the supplied performance constraint is satisfied; otherwise recommend delay.

## Expected useful outcome

Preserve the full 476–519 millisecond sensitivity range and the supplied 25.6% Safari decision boundary. State that rollout is supported only below that boundary and not supported at or above it. Do not select the midpoint, best case, or most convenient point estimate. Because the supported target-mix range crosses the threshold and Monday's actual mix is not narrowed further, leave the performance gate unresolved and recommend delay.

## Actual outcome

Run 34 requires a sensitivity analysis that crosses a gate to report the supplied range and decision boundary, preserve the conditional outcome on each side, and avoid selecting a convenient point estimate. The 476–519 millisecond range crosses the 500-millisecond limit at approximately 25.6% Safari, so the performance gate remains unresolved and delay is the supported recommendation.

## Whether the system helped

yes

## What broke

Before Run 34, the assignment kept unsupported assumptions conditional but did not explicitly prevent an analyst from resolving a threshold-crossing sensitivity analysis by choosing its midpoint, best case, or another favorable point estimate.

## What would make the result more useful

Next, test a sensitivity range that stays entirely on one side of the threshold, verifying that uncertainty does not automatically make a resolvable gate unresolved.
