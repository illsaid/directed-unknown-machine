# 032 — Transparent adjustment with an unsupported target-mix assumption

## Type

boundary-contract

## User

A product lead preparing a recommendation on whether to roll out a checkout change.

## Situation

The notes supply segment measurements and reproducible arithmetic for an adjusted latency estimate, but the target-population weight used in that calculation is an unsupported operator assumption rather than an observed or evidenced input.

## Input

Decision: Roll out the checkout change to US web users on Monday or delay it.
Evidence: A 10,000-request production-shadow test measured p95 response time at 430 milliseconds for the current US web traffic mix. A separate 2,000-request canary test measured an unadjusted p95 response time of 560 milliseconds. The canary's supplied browser-segment measurements were Safari p95 820 milliseconds and non-Safari p95 390 milliseconds. The launch owner assumes Monday's rollout population will be 24% Safari but supplies no traffic forecast, historical Monday mix, or other observation supporting that weight. Using the assumed 24% Safari weight, the supplied calculation is (0.24 × 820) + (0.76 × 390) = 493.2 milliseconds. Paid conversion was 23%.
Constraints: Do not recommend rollout unless p95 response time for the Monday US web rollout population is confirmed below 500 milliseconds.
Success: Recommend rollout on Monday only if paid conversion is at least 20% and the supplied performance constraint is satisfied; otherwise recommend delay.

## Expected useful outcome

Preserve the raw 560-millisecond canary result, the segment measurements, the explicit calculation, and the 493.2-millisecond conditional estimate. Do not treat reproducible arithmetic as confirmation of the gate because the 24% target-population weight is unsupported. Name the missing evidence needed to establish that weight and recommend delay while the performance gate remains unresolved.

## Actual outcome

Run 33 requires an adjusted estimate to identify any supplied assumption used by its method and prevents a reproducible calculation from resolving a gate when a governing assumption lacks supplied evidence. The 493.2-millisecond result remains visible as a conditional estimate, while the unsupported 24% Safari weight leaves the performance gate unresolved and delay remains the supported recommendation.

## Whether the system helped

yes

## What broke

Before Run 33, the assignment rejected opaque adjustments but could still allow transparent arithmetic to make an unsupported target-population assumption look like observed evidence.

## What would make the result more useful

Next, test a supplied assumption with an explicit sensitivity range that crosses the decision threshold, verifying that the brief reports the decision boundary rather than selecting a convenient point estimate.