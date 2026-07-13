# 069 — Reconcile the boundary, then apply the evidence

## Type

structural-regression

## User

A product lead delegating a rollout decision whose notes contain both conflicting thresholds and ordinary evidence application.

## Situation

The executable preserves two distinct boundary stages, but the headings `Boundary reconciliation` and `Boundary evaluation` read like neighboring abstractions rather than an ordered pair of operations. The labels should become shorter and visibly sequential without merging the refusal boundaries.

## Input

Decision: Roll out the checkout change or delay it.
Evidence: Paid conversion is 21%. P95 latency is 480 milliseconds.
Constraints: One note says paid conversion must be at least 20%; the experiment charter says paid conversion must be at least 22% and explicitly governs if thresholds conflict. P95 latency must be below 500 milliseconds.
Success: First preserve both conversion thresholds and use the supplied precedence to reconcile the governing conversion boundary to at least 22%. Then apply the evidence: conversion violates 22%, latency satisfies below 500 milliseconds, and the recommendation is delay because every gate must clear.

## Expected useful outcome

The executable prints `Boundary: reconcile` before `Boundary: apply`. The first stage preserves both conversion rules, uses only the supplied charter precedence, and keeps the displaced 20% result visible. The second stage applies 21% to the governing 22% minimum and 480 milliseconds to the strict 500 millisecond maximum. Gate judgments remain separate, and Governed recommendation selects delay.

## Actual outcome

Run 70 renames only the two boundary audit headings to `Boundary: reconcile` and `Boundary: apply`. Their requirements, order, parser behavior, and refusal boundaries remain unchanged. The output now exposes the sequence as two imperative operations: establish the governing boundary, then apply the evidence to it.

## Whether the system helped

yes

## What broke

Before Run 70, the noun phrases `Boundary reconciliation` and `Boundary evaluation` preserved the conceptual distinction but did not make the dependency as scannable as the other ordered audit stages. A reader could still mistake them for parallel categories rather than reconcile-then-apply operations.

## What would make the result more useful

Next, test whether the remaining four audit headings should stay as nouns or adopt the same operation-first grammar; change them only if one concrete scenario shows a sequencing ambiguity.