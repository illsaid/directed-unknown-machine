# 037 — Supported range touches a strict threshold

## Type

boundary-contract

## User

A product lead preparing a recommendation on whether to roll out a checkout change.

## Situation

The notes supply a supported latency range whose upper bound equals an explicitly strict rollout threshold.

## Input

Decision: Roll out the checkout change to US web users on Monday or delay it.
Evidence: An auditable target-population adjustment produces a supported p95 latency range of 480 to 500 milliseconds. Paid conversion was 23%.
Constraints: Do not recommend rollout unless p95 response time for the Monday US web rollout population is strictly below 500 milliseconds.
Success: Recommend rollout on Monday only if paid conversion is at least 20% and the supplied performance constraint is satisfied; otherwise recommend delay.

## Expected useful outcome

Preserve the full 480–500 millisecond range and the supplied strict wording. Because the supported range includes 500 milliseconds, the performance gate is violated even though paid conversion is 23%; recommend delay. Do not silently reinterpret “strictly below” as “at or below.”

## Actual outcome

Run 38 requires equality under a strict comparison to count as a violation. The range includes 500 milliseconds, so it does not satisfy a requirement that every supported value be strictly below 500 milliseconds. Delay is supported.

## Whether the system helped

yes

## What broke

Before Run 38, the assignment required the supplied comparison wording to govern equality but did not explicitly state the strict-boundary outcome, leaving room to treat equality as unresolved instead of violated.

## What would make the result more useful

Next, test the mirrored minimum boundary: a supported range whose lower bound equals a threshold stated as “at least,” verifying that equality satisfies an inclusive minimum.