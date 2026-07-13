# 065 — Audit groups follow the delegated reasoning sequence

## Type

structural-regression

## User

A product lead reviewing a delegated checkout rollout decision before it leaves the team.

## Situation

The executable preserves six distinct audit operations, but currently prints the final governed recommendation before the source record, transformations, boundary handling, and gate judgments that support it. The same obligations should be easier to audit when presented in dependency order.

## Input

Decision: Roll out the checkout change to US web users on Monday or delay it.
Evidence: Production report A records paid conversion at 23% and p95 latency at 540 milliseconds. A browser-segment table preserves the original latency and supplies the target browser mix plus arithmetic yielding an adjusted p95 estimate of 480 milliseconds.
Constraints: Paid conversion must be at least 20%. P95 latency must be below 500 milliseconds. Preserve every original value. Use the adjusted latency only if the supplied method and target population support it.
Success: First preserve the source record. Then audit the adjustment. Then reconcile any competing boundaries, evaluate the applicable evidence against the governing boundaries, judge each gate, and finally recommend rollout only if every gate is satisfied; otherwise recommend delay.

## Expected useful outcome

Print the six existing audit groups in this visible reasoning sequence: Evidence provenance, Evidence transformation, Boundary reconciliation, Boundary evaluation, Gate judgments, Governed recommendation. Do not merge groups, add requirements, or imply that a later operation may rewrite an earlier source record. With the supported 480 millisecond adjustment, conversion and latency satisfy their gates and the governed recommendation is rollout.

## Actual outcome

Run 66 reorders the unchanged six audit groups into dependency order: source record, supported transformation, boundary reconciliation, boundary evaluation, gate judgments, then governed recommendation. The four-field contract and every requirement remain unchanged.

## Whether the system helped

yes

## What broke

Before Run 66, the executable began with Governed recommendation. That exposed the conclusion before the audit trail needed to support it and made the output read like an unordered checklist rather than a delegated reasoning sequence.

## What would make the result more useful

Next, inspect whether the observation, interpretation, assumption, and gap-status obligation belongs in the source-record stage rather than inside Governed recommendation.
