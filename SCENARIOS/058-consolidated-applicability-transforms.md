# 058 — Consolidated applicability rule preserves exclusion and adjustment

## Type

structural-regression

## User

A product lead reviewing a delegated checkout rollout decision before it leaves the team.

## Situation

The Applicability and adjustment group separately governs excluding a non-comparable source and adjusting a source to the target population. These may be one invariant only if evidence sufficient for exclusion cannot silently substitute for the method and assumptions required for adjustment, or vice versa.

## Input

Decision: Roll out the checkout change to US web users on Monday or delay it.
Evidence: Paid conversion was 23%. Mobile Canary A reported p95 latency of 560 milliseconds; its traffic was 95% native-app sessions, and the contract states native-app telemetry is outside the US web rollout population. Web Canary B reported an unadjusted p95 latency of 540 milliseconds from a 70% Safari and 30% Chrome sample. Canary B measured Safari at 600 milliseconds and Chrome at 400 milliseconds. Current production analytics report the target US web population as 40% Safari and 60% Chrome, yielding a supplied reweighted estimate of 480 milliseconds: (0.40 × 600) + (0.60 × 400).
Constraints: Paid conversion must be at least 20%, and p95 latency must be below 500 milliseconds for the target US web population. Preserve every original source value. Excluding a source must be justified by a supplied observed mismatch and its supplied relevance to the target population. Adjusting a value must preserve the original and include the supplied method, target population, and supported assumptions.
Success: Recommend rollout only if every gate is satisfied from applicable supplied evidence; otherwise recommend delay. Keep Canary A's 560-millisecond value visible while excluding it for the supplied native-app mismatch. Keep Canary B's 540-millisecond original value visible while using the auditable 480-millisecond target-population estimate. Do not treat the exclusion rationale as an adjustment method or the reweighting calculation as a reason to erase a source.

## Expected useful outcome

Emit one concise Applicability and adjustment requirement with distinct branches for source exclusion and value adjustment under one preservation-and-support invariant. Canary A remains visible but is excluded because both the observed mismatch and its relevance are supplied. Canary B remains visible and is adjusted because the segment values, target mix, arithmetic, and target population are supplied. Conversion and target-population latency are satisfied, so rollout is supported.

## Actual outcome

Run 59 consolidates the two Applicability and adjustment bullets into one inspectable invariant. The output still requires every original value to remain visible; source exclusion still requires both an observed mismatch and supplied relevance; value adjustment still requires an auditable method, target population, and supported assumptions; and support for one transformation cannot substitute for the other. Canary A is excluded without deletion, Canary B is adjusted without hiding its original value, and rollout remains the governed recommendation.

## Whether the system helped

yes

## What broke

Before Run 59, source exclusion and value adjustment were separate bullets even though both are applicability transformations governed by the same boundary: preserve the original evidence and require supplied support for the specific transformation being applied.

## What would make the result more useful

Next, inspect whether the two Threshold semantics requirements can be consolidated without letting a threshold with no comparator inherit strict or inclusive meaning.