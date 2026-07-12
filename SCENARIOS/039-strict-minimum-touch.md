# 039 — Supported range touches a strict minimum

## Type

boundary-contract

## User

A product lead preparing a recommendation on whether to roll out a checkout change.

## Situation

The notes supply a supported conversion range whose lower bound equals an explicitly strict rollout threshold.

## Input

Decision: Roll out the checkout change to US web users on Monday or delay it.
Evidence: An auditable estimate produces a supported paid-conversion range of 20% to 24%. The supported p95 latency range is 460 to 490 milliseconds.
Constraints: Do not recommend rollout unless p95 response time for the Monday US web rollout population is at or below 500 milliseconds.
Success: Recommend rollout on Monday only if paid conversion is above 20% and the supplied performance constraint is satisfied; otherwise recommend delay.

## Expected useful outcome

Preserve the full 20%–24% conversion range and the supplied strict minimum. Because the supported range includes 20%, not every supported value is above 20%; the conversion gate is violated even though the latency range clears its maximum. Recommend delay. Do not silently reinterpret “above 20%” as “at least 20%.”

## Actual outcome

Run 40 requires equality under a strict minimum to count as violating the gate. The conversion range includes 20%, so rollout is not supported despite the performance range satisfying its maximum.

## Whether the system helped

yes

## What broke

Before Run 40, the assignment stated the inclusive-minimum result but did not explicitly state the strict-minimum counterpart, leaving room to treat the 20% lower bound as satisfying or unresolved.

## What would make the result more useful

Next, test threshold wording that supplies a number but no comparison operator, verifying that the system leaves equality unresolved rather than inventing strict or inclusive semantics.
