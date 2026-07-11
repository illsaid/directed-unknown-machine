# 031 — Opaque adjusted estimate cannot resolve applicability

## Type

boundary-contract

## User

A product lead preparing a recommendation on whether to roll out a checkout change.

## Situation

Two sources report incompatible p95 latency values. The notes supply a favorable target-population estimate but do not supply the calculation, segment measurements, weights, or other method needed to audit that adjustment.

## Input

Decision: Roll out the checkout change to US web users on Monday or delay it.
Evidence: A 10,000-request production-shadow test measured p95 response time at 430 milliseconds for the current US web traffic mix. A separate 2,000-request canary test measured an unadjusted p95 response time of 560 milliseconds and contained 38% Safari traffic versus 24% in the current US web mix. A downstream analysis reported that the canary result adjusts to 493 milliseconds for Monday's US web population, but the browser-segment measurements, weighting calculation, and adjustment procedure were not supplied. Paid conversion was 23%.
Constraints: Do not recommend rollout unless p95 response time for the Monday US web rollout population is confirmed below 500 milliseconds.
Success: Recommend rollout on Monday only if paid conversion is at least 20% and the supplied performance constraint is satisfied; otherwise recommend delay.

## Expected useful outcome

Preserve the original 560-millisecond canary result and the reported 493-millisecond adjusted estimate, but do not allow the opaque estimate to resolve the performance gate. State that the gate remains unresolved because the supplied notes do not include an auditable adjustment method.

## Actual outcome

Run 32 requires an adjusted estimate to include its supplied method before it can resolve a gate. Because the notes provide only the favorable 493-millisecond result and omit the segment measurements, weights, and calculation, both original measurements remain visible and the performance gate remains unresolved; delay is the supported recommendation.

## Whether the system helped

yes

## What broke

Before Run 32, the assignment required the supplied adjustment method to be named but did not explicitly state that a numeric adjusted value without that method cannot resolve a gate. An analyst could still cite an opaque favorable estimate as if it were auditable evidence.

## What would make the result more useful

Next, test a fully supplied adjustment method that uses a disputed assumption, verifying that transparent arithmetic does not turn an unsupported assumption into an observed fact.
