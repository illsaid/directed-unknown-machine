# 038 — Supported range touches an inclusive minimum

## Type

boundary-contract

## User

A product lead preparing a recommendation on whether to roll out a checkout change.

## Situation

The notes supply a supported conversion range whose lower bound equals an explicitly inclusive rollout threshold.

## Input

Decision: Roll out the checkout change to US web users on Monday or delay it.
Evidence: An auditable estimate produces a supported paid-conversion range of 20% to 24%. The supported p95 latency range is 460 to 490 milliseconds.
Constraints: Do not recommend rollout unless p95 response time for the Monday US web rollout population is at or below 500 milliseconds.
Success: Recommend rollout on Monday only if paid conversion is at least 20% and the supplied performance constraint is satisfied; otherwise recommend delay.

## Expected useful outcome

Preserve the full 20%–24% conversion range and the supplied inclusive minimum. Because every supported conversion value is at least 20%, including the lower bound exactly at 20%, the conversion gate is satisfied. The latency range is also wholly at or below 500 milliseconds, so recommend rollout. Do not silently reinterpret “at least 20%” as “above 20%.”

## Actual outcome

Run 39 requires equality under an inclusive minimum to count as satisfying the gate. The full conversion range is at least 20%, and the performance range satisfies its maximum, so rollout is supported.

## Whether the system helped

yes

## What broke

Before Run 39, the assignment explicitly resolved strict maximum equality but did not state the mirrored inclusive-minimum outcome, leaving room to treat the 20% lower bound as unresolved or failing.

## What would make the result more useful

Next, test the strict minimum counterpart: a supported range whose lower bound equals a threshold stated as “above,” verifying that equality violates a strict minimum.
