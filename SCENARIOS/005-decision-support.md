# 005 — Decision support: preserve the actual decision and constraints

## Type

decision-support

## User

A biotech newsletter operator deciding whether to publish a probability-of-approval score for an upcoming FDA decision.

## Situation

The operator has a messy note set mixing regulatory facts, sponsor history, model assumptions, and editorial concerns. They need one bounded analysis task, not a generic dashboard or an invented menu of three options.

## Input

Decision: Should the next issue publish a numeric probability-of-approval score for Asset X, publish only a qualitative risk band, or omit the forecast?
Evidence: pivotal trial result and endpoint hierarchy; FDA review designation; known CMC or inspection issues; advisory committee history; sponsor disclosure and prior CRL history; comparable approvals and CRLs.
Constraints: do not treat Priority Review as causal evidence of approval; separate verified facts from inference; do not invent missing FDA correspondence; preserve the newsletter's existing reader-facing POA convention unless evidence shows it is misleading.
Success: the editor can choose one publishing treatment and explain the choice in two sentences, with the largest unresolved uncertainty named explicitly.

## Expected useful outcome

The system should preserve the named publishing decision, evidence categories, anti-causal constraint, non-invention rule, and observable editorial success condition. It should output one bounded brief task rather than replacing the problem with a generic three-option template.

## Actual outcome

Run 5 added `decision_brief.py`. On this scenario it extracts the four labeled parts of the messy input and emits a bounded one-page brief task that keeps the actual decision, required evidence, constraints, and success condition intact.

## Whether the system helped

yes

## What broke

The previous `machine.py` vague-input path would have replaced these domain constraints with a fixed instruction to produce three evidence-backed options. That would preserve superficial structure while discarding the most important rules of the decision.

## What would make the result more useful

Test a second decision-support scenario without explicit labels. If the system cannot preserve the decision and constraints without labels, keep the labeled-note-set requirement as part of the narrow use case rather than adding a generic extractor.
