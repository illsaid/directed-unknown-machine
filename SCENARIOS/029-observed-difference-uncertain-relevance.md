# 029 — Observed difference does not establish relevance

## Type

boundary-contract

## User

A product lead preparing a recommendation on whether to roll out a checkout change.

## Situation

Two sources report incompatible values for the same rollout measurement. The notes directly observe a traffic-mix difference, but do not establish whether that difference explains why one source is less applicable to the planned rollout population.

## Input

Decision: Roll out the checkout change to US web users on Monday or delay it.
Evidence: A 10,000-request production-shadow test measured p95 response time at 430 milliseconds. A separate 2,000-request canary test measured p95 response time at 560 milliseconds. The canary traffic log directly shows that 38% of requests used Safari, compared with 24% in the current US web traffic mix. No browser-segment latency results, weighting analysis, or other evidence establishes that this difference caused the higher p95 result or makes the canary inapplicable to Monday's rollout population. Paid conversion was 23%.
Constraints: Do not recommend rollout unless p95 response time for the Monday US web rollout population is confirmed below 500 milliseconds.
Success: Recommend rollout on Monday only if paid conversion is at least 20% and the supplied performance constraint is satisfied; otherwise recommend delay.

## Expected useful outcome

Preserve both p95 values and the directly observed Safari-mix difference, but do not treat the observation alone as proof that the canary is non-comparable. Require supplied evidence connecting the observed difference to source applicability; otherwise leave the performance gate unresolved.

## Actual outcome

Run 30 preserves both measurements and the observed browser-mix difference, while requiring any source exclusion to name supplied evidence establishing why that observation changes applicability to the target population. Because no such relevance evidence is supplied, the canary cannot be excluded and the performance gate remains unresolved.

## Whether the system helped

yes

## What broke

Before Run 30, the assignment required a direct supplied observation establishing a comparability reason, but could still allow any observed scope difference to be treated as sufficient without showing why it matters to the target decision population.

## What would make the result more useful

Next, test a direct observed difference with supplied segment-level evidence that establishes its relevance, verifying that justified exclusion remains possible.