# 063 — Governed recommendation and gate judgments remain distinct audit questions

## Type

structural-regression

## User

A product lead reviewing a delegated checkout rollout decision before it leaves the team.

## Situation

The current executable has one audit group for selecting the action governed by the success rule and another for judging each constraint against supplied evidence. The groups should remain separate only if their labels make the difference immediately inspectable.

## Input

Decision: Roll out the checkout change to US web users on Monday or delay it.
Evidence: Paid conversion was 23%. P95 latency was 540 milliseconds.
Constraints: Paid conversion must be at least 20%. P95 latency must be below 500 milliseconds.
Success: Recommend rollout only if every gate is satisfied; otherwise recommend delay. Judge conversion satisfied and latency violated from the supplied evidence, then select delay because the supplied governance rule makes any failed gate blocking.

## Expected useful outcome

Emit separate, plainly named audit groups for Governed recommendation and Gate judgments. Gate judgments evaluates conversion and latency independently from supplied evidence. Governed recommendation then selects delay from the supplied fallback rule because latency is violated. The action must not be presented as another gate judgment, and the gate results must not be collapsed into the action.

## Actual outcome

Run 64 keeps the two audit questions separate but renames Decision to Governed recommendation. The executable now distinguishes evaluating the constraints that permit an action from selecting the action required by the supplied success or reversal rule. Conversion is satisfied, latency is violated, and delay is the governed recommendation.

## Whether the system helped

yes

## What broke

Before Run 64, the label Decision duplicated the name of an input field and did not identify the audit operation. Beside Gate judgments, it obscured that this group governs action selection after the constraints have been evaluated.

## What would make the result more useful

Next, inspect whether Evidence provenance and Applicability and adjustment remain distinct audit questions: recording what each source says versus determining whether a supported transformation may change how that evidence applies.