# 046 — Grouped requirements preserve threshold precedence

## Type

structural-regression

## User

A product lead reviewing the generated assignment before delegating a rollout recommendation.

## Situation

The executable contains the correct threshold-precedence boundary, but its gate requirements are printed as one dense paragraph that is difficult to audit.

## Input

Decision: Roll out the checkout change to US web users on Monday or delay it.
Evidence: Paid conversion is 21%. The supported p95 latency range is 460 to 490 milliseconds. For this rollout decision, the Success threshold governs if it conflicts with the Constraints threshold; the Constraints threshold remains contextual and must still be reported.
Constraints: Do not recommend rollout unless paid conversion is at least 20% and p95 response time is at or below 500 milliseconds.
Success: Recommend rollout on Monday only if paid conversion is at least 22% and p95 response time is at or below 500 milliseconds; otherwise recommend delay.

## Expected useful outcome

Emit the unchanged four-field contract and requirements grouped under inspectable labels. The threshold-conflict group must still require the governing 22% threshold, preserve the displaced 20% threshold, and report the result under each. The output remains a delay recommendation: conversion violates the governing threshold while latency is satisfied.

## Actual outcome

Run 47 prints the existing requirements in named groups. The threshold-conflict group preserves explicit precedence and every displaced threshold; no established decision boundary was removed or weakened.

## Whether the system helped

yes

## What broke

Before Run 47, the executable placed nearly all gate obligations in one long bullet, making a correct assignment unnecessarily difficult to inspect.

## What would make the result more useful

Next, test whether one grouped obligation can replace duplicated equality clauses without losing strict and inclusive threshold behavior.
