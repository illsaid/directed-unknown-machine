# 026 — Supplied comparability reason permits explicit exclusion

## Type

boundary-contract

## User

A product lead preparing a recommendation on whether to roll out a checkout change.

## Situation

Two sources report incompatible values for the same rollout measurement, but the supplied notes explain that one source used a traffic mix outside the decision's stated scope.

## Input

Decision: Roll out the checkout change to US web users on Monday or delay it.
Evidence: A 10,000-request production-shadow test using the current US web traffic mix measured p95 response time at 430 milliseconds. A separate 2,000-request canary test measured p95 response time at 560 milliseconds, but 78% of its requests came from an internal mobile-client build that is not included in Monday's US web rollout. Paid conversion in the matched US web cohort was 23%.
Constraints: Do not recommend rollout unless p95 response time for the Monday US web rollout population is confirmed below 500 milliseconds.
Success: Recommend rollout on Monday only if paid conversion is at least 20% and the supplied performance constraint is satisfied; otherwise recommend delay.

## Expected useful outcome

Preserve both reported p95 values, state the supplied traffic-mix reason the canary result is not comparable to the Monday US web rollout population, and permit the production-shadow measurement to govern only because the notes establish that scope difference explicitly.

## Actual outcome

Run 27 preserves both measurements and requires any source exclusion to name the supplied comparability reason and the excluded value, distinguishing justified exclusion from silent source preference.

## Whether the system helped

yes

## What broke

Before Run 27, the assignment allowed a disagreement to be resolved when supplied evidence established which source applied, but it did not require the analyst to expose the exclusion rationale and excluded value.

## What would make the result more useful

Next, test an asserted comparability reason that is not supported by supplied evidence, verifying that an unsupported rationale cannot justify source exclusion.
