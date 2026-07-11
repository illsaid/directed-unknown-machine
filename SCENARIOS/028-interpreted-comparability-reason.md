# 028 — Interpretation alone cannot establish non-comparability

## Type

boundary-contract

## User

A product lead preparing a recommendation on whether to roll out a checkout change.

## Situation

Two sources report incompatible values for the same rollout measurement. A downstream analyst concluded that the unfavorable source was non-comparable, but the notes do not include the observed traffic difference on which that conclusion was supposedly based.

## Input

Decision: Roll out the checkout change to US web users on Monday or delay it.
Evidence: A 10,000-request production-shadow test measured p95 response time at 430 milliseconds. A separate 2,000-request canary test measured p95 response time at 560 milliseconds. A downstream analyst reviewed the tests and concluded that the canary was not comparable because its traffic mix differed from the planned rollout population. The analyst's conclusion is supplied, but no traffic-mix counts, client breakdown, geography breakdown, or other observed scope difference is included. Paid conversion was 23%.
Constraints: Do not recommend rollout unless p95 response time for the Monday US web rollout population is confirmed below 500 milliseconds.
Success: Recommend rollout on Monday only if paid conversion is at least 20% and the supplied performance constraint is satisfied; otherwise recommend delay.

## Expected useful outcome

Preserve both p95 values, treat the analyst's comparability conclusion as an interpretation rather than the observation needed to establish a scope mismatch, refuse to exclude the canary on that conclusion alone, and leave the performance gate unresolved.

## Actual outcome

Run 29 preserves both measurements and requires any exclusion to name the direct supplied observation establishing the mismatch, not merely a downstream conclusion derived from unavailable observations. Because no observed traffic difference is supplied, the canary cannot be excluded and the performance gate remains unresolved.

## Whether the system helped

yes

## What broke

Before Run 29, the assignment required a supplied observation establishing the comparability reason but did not explicitly prevent a downstream analyst's conclusion from being presented as that observation.

## What would make the result more useful

Next, test a comparability mismatch supported by a direct observation whose relevance to the rollout population is itself uncertain.