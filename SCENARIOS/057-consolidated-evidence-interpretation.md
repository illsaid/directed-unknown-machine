# 057 — Consolidated evidence handling preserves status and conflict

## Type

structural-regression

## User

A product lead reviewing a delegated checkout diagnosis before choosing a remedy.

## Situation

The Decision group separately requires evidence-status separation and observation-only handling of conflicting interpretations. These may be one invariant if observations, interpretations, assumptions, unresolved conflict, and the distinguishing evidence all remain explicit.

## Input

Decision: Choose whether to rewrite checkout copy, prioritize latency work, or run another diagnostic before changing the checkout.
Evidence: Observed checkout abandonment was 12%. The growth lead interprets the abandonment as evidence that the new copy is confusing. The engineering lead interprets it as evidence that latency is driving exits. The operator assumes returning users will adapt to the copy. No step-level abandonment breakdown or response-time correlation was supplied.
Constraints: Do not describe either interpretation or the adaptation assumption as an observed cause. Do not recommend a causal remedy unless supplied observations distinguish the competing explanations.
Success: Recommend one action. Preserve the 12% observation, both interpretations, the unsupported adaptation assumption, and the unresolved causal gap. Name step-level abandonment and response-time correlation as the evidence needed to distinguish the explanations. If the cause remains unresolved, recommend another diagnostic rather than a copy or latency remedy.

## Expected useful outcome

Emit one concise Decision requirement that preserves the status of every supplied statement, compares competing interpretations only with observations, leaves unsupported causal conflict unresolved, and names the evidence that would distinguish it. The 12% abandonment rate remains an observation; confusing copy and latency remain rival interpretations; user adaptation remains an assumption; the cause remains unresolved; and the supported recommendation is another diagnostic.

## Actual outcome

Run 58 consolidates the two remaining Decision bullets into one inspectable invariant. The output still preserves the 12% observation, both rival interpretations, the unsupported adaptation assumption, and the unresolved causal gap; it requires comparison only against supplied observations and requires the missing distinguishing evidence to be named. Neither causal remedy is supported, so another diagnostic remains the governed recommendation.

## Whether the system helped

yes

## What broke

Before Run 58, statement-status preservation and conflicting-interpretation handling were expressed as separate bullets even though both enforce one boundary: supplied claims may only gain decision weight from supplied observations.

## What would make the result more useful

Next, inspect whether the two Applicability and adjustment requirements are genuinely separate invariants or can be consolidated without allowing source exclusion and value adjustment to blur together.
