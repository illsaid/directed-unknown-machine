# 025 — Conflicting source measurements remain explicit

## Type

boundary-contract

## User

A product lead preparing a recommendation on whether to roll out a checkout change.

## Situation

Two evidence sources report incompatible values for the same performance measurement needed for a rollout gate.

## Input

Decision: Roll out the checkout change to all users on Monday or delay it.
Evidence: A 10,000-request production-shadow test measured p95 response time at 430 milliseconds. A separate 2,000-request canary test measured p95 response time at 560 milliseconds. Paid conversion in the matched cohort was 23%.
Constraints: Do not recommend rollout unless p95 response time is confirmed below 500 milliseconds.
Success: Recommend rollout on Monday only if paid conversion is at least 20% and the supplied performance constraint is satisfied; otherwise recommend delay.

## Expected useful outcome

Preserve the disagreement between the 430-millisecond and 560-millisecond p95 measurements, do not average them or silently select one source, and leave the performance gate unresolved unless the supplied evidence establishes why one measurement should govern.

## Actual outcome

Run 26 preserves the complete four-field contract and requires conflicting measurements for the same gate to remain explicit rather than being averaged, silently resolved, or presented as consensus.

## Whether the system helped

yes

## What broke

Before Run 26, the assignment handled shared and overlapping evidence but did not explicitly prevent incompatible measurements from being averaged or silently resolved.

## What would make the result more useful

Next, test two conflicting measurements where the supplied notes include a concrete reason one source is not comparable, verifying that justified exclusion is distinguished from silent source preference.
