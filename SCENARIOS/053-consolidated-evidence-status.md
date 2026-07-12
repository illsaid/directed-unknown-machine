# 053 — Consolidated evidence-status rule preserves the no-promotion boundary

## Type

structural-regression

## User

A product lead reviewing a delegated checkout diagnosis before it leaves the team.

## Situation

The Decision requirements separately ask the analyst to distinguish facts, assumptions, and gaps, forbid promoting interpretations to facts, and preserve unresolved conflict. These may be one evidence-status invariant plus one conflict-handling rule.

## Input

Decision: Ship a copy-only checkout fix on Monday or delay and investigate latency first.
Evidence: Production logs directly show 12% checkout abandonment. The support lead interprets the abandonment as confusion caused by the payment copy. The product manager interprets the same abandonment as a latency problem. The launch owner assumes returning users will adapt to the current copy, but supplies no cohort evidence. No step-level abandonment, response-time, or user-research evidence distinguishes the two interpretations.
Constraints: Recommend an action using only supplied observations. Keep interpretations and assumptions visible but do not restate them as measured causes.
Success: Recommend the copy-only fix only if supplied observations support copy confusion as the cause; recommend latency investigation only if supplied observations support latency as the cause; otherwise state that the causal conflict is unresolved and name the smallest evidence needed to distinguish it.

## Expected useful outcome

Emit one concise evidence-status rule that keeps the 12% abandonment observation, both causal interpretations, the returning-user assumption, and the missing evidence distinct without promoting any of them. Emit one conflict rule requiring both interpretations to be tested only against supplied observations, leaving the cause unresolved and naming step-level abandonment plus response-time evidence as the distinguishing test. Do not recommend either causal remedy as supported.

## Actual outcome

Run 54 consolidates the three overlapping Decision requirements into two inspectable rules. The output still preserves the measured abandonment separately from both interpretations and the unsupported returning-user assumption, leaves the causal conflict unresolved, and requires the missing distinguishing evidence to be named.

## Whether the system helped

yes

## What broke

Before Run 54, one evidence-status boundary was spread across three bullets whose wording partially repeated the same prohibition against silently upgrading interpretation into fact.

## What would make the result more useful

Next, inspect the Gate judgments requirements for duplicated wording around separate gate status, evidence binding, and recommendation blocking.
