# 064 — Source record and evidence transformation remain distinct audit questions

## Type

structural-regression

## User

A product lead reviewing a delegated checkout rollout decision before it leaves the team.

## Situation

The current executable has one audit group for recording what each source actually reports and another for validating exclusions or adjustments that change how a reported value applies. The groups should remain separate only if their labels make the difference immediately inspectable.

## Input

Decision: Roll out the checkout change to US web users on Monday or delay it.
Evidence: Production report A records paid conversion at 23% and p95 latency at 540 milliseconds. Mobile canary B records p95 latency at 560 milliseconds and states that 82% of its traffic came from native-app sessions outside the US web rollout population. A browser-segment table for report A supplies segment latencies, the target production browser mix, and arithmetic yielding an adjusted p95 estimate of 480 milliseconds.
Constraints: Paid conversion must be at least 20%. P95 latency must be below 500 milliseconds. Preserve every original source value. Exclude canary B only because the supplied traffic mismatch is explicitly relevant to the target population. Use the 480 millisecond adjustment only because the method, target mix, and arithmetic are supplied.
Success: Recommend rollout only if every gate is satisfied; otherwise recommend delay. First record which measurements and values each source supplies. Then separately audit whether the exclusion and adjustment have enough supplied support to change how those values apply. Recommend rollout only after the supported transformations leave conversion at 23% and applicable latency at 480 milliseconds.

## Expected useful outcome

Emit separate, plainly named audit groups for Evidence provenance and Evidence transformation. Evidence provenance records report A's conversion and latency values, canary B's latency value, and the browser table's adjustment inputs without spill or double-counting. Evidence transformation then validates the population-based exclusion and auditable adjustment while preserving all originals. Recording a source claim must not itself authorize excluding or changing it, and transformation support must not rewrite the source record.

## Actual outcome

Run 65 keeps the two audit questions separate but renames Applicability and adjustment to Evidence transformation. The executable now distinguishes preserving the source record from auditing a supported operation that changes how evidence applies. No parser or requirement behavior changed.

## Whether the system helped

yes

## What broke

Before Run 65, Applicability and adjustment named two subject areas rather than the audit operation. Beside Evidence provenance, it did not make clear that provenance preserves source claims while the second group governs any exclusion or adjustment applied to them.

## What would make the result more useful

Next, inspect whether the remaining six audit groups can be ordered as a single visible reasoning sequence without merging distinct obligations.