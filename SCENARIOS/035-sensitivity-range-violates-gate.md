# 035 — Sensitivity range violates the decision gate

## Type

boundary-contract

## User

A product lead preparing a recommendation on whether to roll out a checkout change.

## Situation

The notes supply an auditable latency adjustment and a supported range for the uncertain target-population weight. Every value in the resulting latency range remains above the rollout threshold.

## Input

Decision: Roll out the checkout change to US web users on Monday or delay it.
Evidence: A 10,000-request production-shadow test measured p95 response time at 430 milliseconds for the current US web traffic mix. A separate 2,000-request canary test measured an unadjusted p95 response time of 560 milliseconds. The canary's supplied browser-segment measurements were Safari p95 820 milliseconds and non-Safari p95 390 milliseconds. Historical Monday traffic observations support a Safari share between 30% and 35%. Applying the supplied formula (Safari share × 820) + (remaining share × 390) gives a sensitivity range of 519 milliseconds at 30% Safari to 540.5 milliseconds at 35% Safari. Paid conversion was 23%.
Constraints: Do not recommend rollout unless p95 response time for the Monday US web rollout population is confirmed below 500 milliseconds.
Success: Recommend rollout on Monday only if paid conversion is at least 20% and the supplied performance constraint is satisfied; otherwise recommend delay.

## Expected useful outcome

Preserve the full 519–540.5 millisecond sensitivity range and state that every supported value exceeds the 500-millisecond limit. Do not mark the performance gate unresolved merely because the result is a range. Because paid conversion is 23% but the entire supported latency range violates the gate, recommend delay.

## Actual outcome

Run 36 requires a supported sensitivity range entirely above a maximum threshold to be judged as a violated gate from the whole range. The 519–540.5 millisecond range remains above the 500-millisecond limit, so delay is the supported recommendation.

## Whether the system helped

yes

## What broke

Before Run 36, the assignment said a range wholly on one side of a threshold could resolve a gate, but did not explicitly map a range wholly above a maximum to a violated judgment.

## What would make the result more useful

Next, test an inclusive threshold where the supported range touches the boundary exactly, verifying that equality is judged from the supplied comparison rule rather than assumed.