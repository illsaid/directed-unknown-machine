# 014 — Mixed evidence interpretation

## Type

hostile-contract

## User

A product lead preparing a recommendation on whether to keep a new onboarding flow.

## Situation

The supplied Evidence field mixes observed behavior with the operator's interpretation of why it happened.

## Input

Decision: Keep the new onboarding flow for the next release or restore the prior flow.
Evidence: Twelve of 40 test users abandoned the new flow at the permissions screen. This proves users do not trust the permissions request. Seven of those users completed the prior flow in an earlier test.
Constraints: Do not infer why users abandoned; do not treat the earlier test as a controlled comparison; separate observed behavior from causal claims.
Success: Recommend keep or restore, identify which supplied statement is interpretation rather than observation, and name the additional observation that would reverse the recommendation.

## Expected useful outcome

Preserve the complete Evidence field, but explicitly require the analyst to treat the trust claim as an operator interpretation rather than an observed fact.

## Actual outcome

Run 15 preserves all supplied wording and adds an explicit instruction not to adopt interpretations embedded in Evidence as facts.

## Whether the system helped

yes

## What broke

Before Run 15, the deliverable required separation of facts and assumptions but did not explicitly say that an interpretation already embedded in the Evidence field must remain an interpretation.

## What would make the result more useful

Test whether the same fixed contract handles conflicting supplied interpretations without turning into an evidence-classification system.