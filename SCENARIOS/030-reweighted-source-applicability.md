# 030 — Reweighting establishes source applicability

## Type

boundary-contract

## User

A product lead preparing a recommendation on whether to roll out a checkout change.

## Situation

Two sources report incompatible p95 latency values. The notes supply both an observed traffic-mix difference and segment-level measurements showing how to adjust the canary result to the target rollout population.

## Input

Decision: Roll out the checkout change to US web users on Monday or delay it.
Evidence: A 10,000-request production-shadow test measured p95 response time at 430 milliseconds for the current US web traffic mix. A separate 2,000-request canary test measured an unadjusted p95 response time of 560 milliseconds and contained 38% Safari traffic versus 24% in the current US web mix. The canary's supplied browser-segment measurements were Safari p95 820 milliseconds and non-Safari p95 390 milliseconds. The supplied reweighting calculation using Monday's 24% Safari target mix produced an adjusted canary estimate of 493 milliseconds. Paid conversion was 23%.
Constraints: Do not recommend rollout unless p95 response time for the Monday US web rollout population is confirmed below 500 milliseconds.
Success: Recommend rollout on Monday only if paid conversion is at least 20% and the supplied performance constraint is satisfied; otherwise recommend delay.

## Expected useful outcome

Allow the target-population estimate to resolve the performance gate because the notes supply the observed mix difference, segment measurements, target mix, and adjustment result. Preserve the original 560-millisecond canary value, name the adjusted 493-millisecond estimate, and expose the supplied reweighting method rather than silently replacing the unfavorable result.

## Actual outcome

Run 31 preserves the original canary measurement while requiring any adjusted or reweighted value used for source applicability to name the adjusted result, supplied method, and target population. The 493-millisecond target-population estimate and 430-millisecond production-shadow result both satisfy the performance constraint, so rollout is supported without erasing the original 560-millisecond canary result.

## Whether the system helped

yes

## What broke

Before Run 31, the assignment required relevance evidence for excluding a source but did not explicitly prevent a supplied adjusted estimate from silently replacing the original measurement or hiding how the target-population estimate was produced.

## What would make the result more useful

Next, test an adjusted estimate whose supplied method is incomplete, verifying that a numeric adjustment without an auditable method cannot resolve the gate.