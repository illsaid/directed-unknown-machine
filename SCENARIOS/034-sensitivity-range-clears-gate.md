# 034 — Sensitivity range clears the decision gate

## Type

boundary-contract

## User

A product lead preparing a recommendation on whether to roll out a checkout change.

## Situation

The notes supply an auditable latency adjustment and a supported range for the uncertain target-population weight. Every value in the resulting latency range remains below the rollout threshold.

## Input

Decision: Roll out the checkout change to US web users on Monday or delay it.
Evidence: A 10,000-request production-shadow test measured p95 response time at 430 milliseconds for the current US web traffic mix. A separate 2,000-request canary test measured an unadjusted p95 response time of 560 milliseconds. The canary's supplied browser-segment measurements were Safari p95 820 milliseconds and non-Safari p95 390 milliseconds. Historical Monday traffic observations support a Safari share between 15% and 22%. Applying the supplied formula (Safari share × 820) + (remaining share × 390) gives a sensitivity range of 454.5 milliseconds at 15% Safari to 484.6 milliseconds at 22% Safari. Paid conversion was 23%.
Constraints: Do not recommend rollout unless p95 response time for the Monday US web rollout population is confirmed below 500 milliseconds.
Success: Recommend rollout on Monday only if paid conversion is at least 20% and the supplied performance constraint is satisfied; otherwise recommend delay.

## Expected useful outcome

Preserve the full 454.5–484.6 millisecond sensitivity range and state that every supported value remains below the 500-millisecond limit. Do not mark the performance gate unresolved merely because the result is a range. Because paid conversion is 23% and the entire supported latency range clears the gate, recommend rollout.

## Actual outcome

Run 35 requires a supported sensitivity range entirely on one side of a gate to be judged from the whole range rather than treated as unresolved by default. The 454.5–484.6 millisecond range remains below the 500-millisecond limit, so the performance gate is satisfied and rollout is the supported recommendation.

## Whether the system helped

yes

## What broke

Before Run 35, the assignment specified what to do when a sensitivity range crossed a threshold but did not explicitly state that a fully threshold-clearing range can satisfy a gate.

## What would make the result more useful

Next, test a sensitivity range entirely above the threshold, verifying that a bounded range can also establish a violated gate without selecting one representative value.