# 013 — Repaired observation evidence

## Type

contract-repair

## User

A product lead preparing a recommendation on whether to keep a new onboarding flow.

## Situation

The operator repaired an unsupported Observation field by moving the observed behavior under Evidence without changing its wording.

## Input

Decision: Keep the new onboarding flow for the next release or restore the prior flow.
Evidence: Twelve of 40 test users abandoned the new flow at the permissions screen; seven of those users completed the prior flow in an earlier test.
Constraints: Do not infer why users abandoned; do not treat the earlier test as a controlled comparison; separate observed behavior from causal claims.
Success: Recommend keep or restore, and name the additional observation that would reverse the recommendation.

## Expected useful outcome

Accept the repaired four-field contract, preserve both observations as supplied evidence, and avoid turning the abandonment rate or prior-flow completions into performance requirements.

## Actual outcome

Run 14 accepts all four explicit fields, labels the observations as supplied evidence, and keeps the fixed deliverable focused on one recommendation governed by the stated success or reversal rule.

## Whether the system helped

yes

## What broke

Before Run 14, the output label `Evidence:` was semantically neutral but did not make clear that the parsed text was supplied observational input rather than a target the recommendation had to satisfy.

## What would make the result more useful

Test whether evidence containing an operator interpretation can still be separated from observed facts without adding another field or an inference engine.
