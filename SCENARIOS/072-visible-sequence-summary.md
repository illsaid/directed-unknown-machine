# 072 — Show the reasoning sequence before the dense audit requirements

## Type

structural-regression

## User

A nontechnical operator reviewing a delegated rollout brief before handing it to an analyst.

## Situation

The executable contains six correctly ordered audit stages, but a reader must infer the full workflow by scanning six dense headings and requirements. The operator needs to see the complete reasoning path immediately without losing any detailed obligation.

## Input

Decision: Roll out the checkout change or delay it.
Evidence: Paid conversion is 23%. P95 latency is 480 milliseconds.
Constraints: Paid conversion must be at least 20%. P95 latency must be below 500 milliseconds.
Success: Judge both gates from the supplied evidence. Rollout is allowed only if every gate clears; otherwise recommend delay.

## Expected useful outcome

Before printing the six detailed requirement groups, the executable prints one compact sequence line: preserve evidence, transform evidence, reconcile boundaries, apply boundaries, judge gates, recommend. The detailed requirements remain unchanged, and the supplied evidence resolves both gates as satisfied, supporting rollout.

## Actual outcome

Run 73 adds one literal `Reasoning sequence` line before `Brief requirements`. It summarizes the existing six ordered operations without adding a requirement, changing parser behavior, altering fields, or introducing a new abstraction. The detailed groups remain the authoritative audit contract.

## Whether the system helped

yes

## What broke

Before Run 73, the operation order was present only as six separate headings. The sequence was structurally correct but not visible as one workflow, so the output still read like a dense checklist on first scan.

## What would make the result more useful

Keep the sequence line only as a compact orientation aid. Do not duplicate requirement content into another summary layer or add configurable presentation modes.