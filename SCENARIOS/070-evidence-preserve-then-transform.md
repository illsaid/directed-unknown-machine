# 070 — Preserve the evidence, then transform it

## Type

structural-regression

## User

A product lead delegating a rollout decision whose notes contain both original measurements and a supported adjustment.

## Situation

The executable keeps evidence provenance and evidence transformation separate, but the headings `Evidence provenance` and `Evidence transformation` read like adjacent categories rather than an ordered pair. The source record must be visibly preserved before any exclusion or adjustment is allowed to change how it applies.

## Input

Decision: Roll out the checkout change or delay it.
Evidence: Report A records paid conversion at 23% and p95 latency at 540 milliseconds. A browser-segment table records 60% desktop traffic at 450 milliseconds and 40% mobile-web traffic at 525 milliseconds; the production mix is explicitly the same, yielding an auditable weighted estimate of 480 milliseconds.
Constraints: Paid conversion must be at least 20%. P95 latency must be below 500 milliseconds. Any adjusted value must retain the original value and show the supplied method, target population, and supported assumptions.
Success: First preserve Report A's original 23% and 540 millisecond values and the browser-segment table as separate source records. Then apply only the supplied weighted adjustment to latency, producing 480 milliseconds for the matching production population. Judge both gates satisfied and recommend rollout because every gate clears.

## Expected useful outcome

The executable prints `Evidence: preserve` before `Evidence: transform`. The first stage keeps every source and original value visible without spill or double-counting. The second stage permits the 480 millisecond latency estimate only because the notes supply the segment values, weights, matching target population, arithmetic, and governing assumption support. Boundary and gate stages remain unchanged, and Governed recommendation selects rollout.

## Actual outcome

Run 71 renames only the two evidence audit headings to `Evidence: preserve` and `Evidence: transform`. Their requirements, order, parser behavior, and refusal boundaries remain unchanged. The output now exposes the sequence as two imperative operations: fix the source record, then authorize any supported change in how that record applies.

## Whether the system helped

yes

## What broke

Before Run 71, the noun phrases `Evidence provenance` and `Evidence transformation` preserved the conceptual distinction but did not make the dependency as scannable as the boundary pair. A reader could treat transformation as parallel to provenance rather than as an operation constrained by the preserved record.

## What would make the result more useful

Next, test whether `Gate judgments` and `Governed recommendation` create a comparable sequencing ambiguity. Change them only if one concrete scenario shows that shared operation-first grammar improves the reasoning path without collapsing judgment into action selection.
