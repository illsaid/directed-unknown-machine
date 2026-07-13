# 062 — Boundary application and reconciliation remain distinct audit questions

## Type

structural-regression

## User

A product lead reviewing a delegated checkout rollout decision before it leaves the team.

## Situation

The current executable has one group for applying supplied evidence to a single boundary and another for incompatible boundary statements. The groups should remain separate only if their labels make the distinction immediately inspectable.

## Input

Decision: Roll out the checkout change to US web users on Monday or delay it.
Evidence: Paid conversion was exactly 20%. P95 latency was 480 milliseconds.
Constraints: Paid conversion must be at least 20%. P95 latency must be below 500 milliseconds in the operating note and below 450 milliseconds in the governing success rule; no precedence or reconciliation is supplied.
Success: Recommend rollout only if every gate is satisfied; otherwise recommend delay. Apply the single supplied conversion boundary and mark conversion satisfied. Preserve both incompatible latency boundaries and leave latency unresolved because no governing rule is supplied. Do not treat ordinary boundary application as permission to choose between conflicting boundaries.

## Expected useful outcome

Emit separate, plainly named audit groups for Boundary evaluation and Boundary reconciliation. Conversion is satisfied by applying one inclusive boundary. Latency remains unresolved because two incompatible boundaries require reconciliation support that was not supplied. Because not every gate is satisfied, delay is the governed recommendation.

## Actual outcome

Run 63 keeps the two audit questions separate but renames Threshold conflict to Boundary reconciliation. The executable now distinguishes applying evidence to one supplied boundary from choosing among incompatible supplied boundaries without changing the four-field contract or any established decision rule. Conversion is satisfied, latency remains unresolved, and delay remains the governed recommendation.

## Whether the system helped

yes

## What broke

Before Run 63, the label Threshold conflict described the input condition but not the audit operation. Beside Boundary evaluation, it obscured the precise distinction between applying one boundary and reconciling multiple incompatible boundaries.

## What would make the result more useful

Next, inspect whether Decision and Gate judgments remain distinct audit questions: selecting a governed action versus evaluating the constraints that permit it.
