# 027 — Unsupported comparability claim cannot exclude evidence

## Type

boundary-contract

## User

A product lead preparing a recommendation on whether to roll out a checkout change.

## Situation

Two sources report incompatible values for the same rollout measurement, and the notes assert that the unfavorable source is probably non-comparable without supplying observations that establish the mismatch.

## Input

Decision: Roll out the checkout change to US web users on Monday or delay it.
Evidence: A 10,000-request production-shadow test measured p95 response time at 430 milliseconds. A separate 2,000-request canary test measured p95 response time at 560 milliseconds. The product lead says the canary is probably not comparable because it may have included unusual mobile traffic, but no traffic-mix breakdown or other source-scope evidence was supplied. Paid conversion was 23%.
Constraints: Do not recommend rollout unless p95 response time for the Monday US web rollout population is confirmed below 500 milliseconds.
Success: Recommend rollout on Monday only if paid conversion is at least 20% and the supplied performance constraint is satisfied; otherwise recommend delay.

## Expected useful outcome

Preserve both reported p95 values, distinguish the product lead's unsupported comparability claim from supplied evidence, refuse to exclude the canary on that claim alone, and leave the performance gate unresolved.

## Actual outcome

Run 28 preserves both measurements and requires a source exclusion to name supplied observations that establish the comparability reason. Because the notes provide no traffic-mix evidence, the canary cannot be excluded and the performance gate remains unresolved.

## Whether the system helped

yes

## What broke

Before Run 28, the assignment required a supplied comparability reason and excluded value but did not distinguish an evidence-backed reason from an unsupported assertion written inside Evidence.

## What would make the result more useful

Next, test a comparability reason supported only by a downstream interpretation rather than a direct supplied observation, checking whether the same boundary remains clear without sentence-level classification.