# 079 — Remove duplicated recommendation wording without weakening branch traceability

## Type

structural-regression

## User

A product lead delegating a rollout decision whose Success field contains ordered fallback branches.

## Situation

The final recommendation invariant repeats concepts already fixed by the four-field contract. The test is whether it can name the schema field directly and remain fully auditable.

## Input

Decision: Choose whether to roll out the new checkout.
Evidence: Paid conversion is 23%. P95 latency is 540 milliseconds. Retention is 70%, but the contract supplies no comparator for the retention threshold.
Constraints: Conversion must be at least 20%. Latency must be below 500 milliseconds. Retention has a threshold of 70%, with no comparator supplied.
Success: If any gate is violated, delay rollout. Otherwise, if any gate is unresolved, run a diagnostic. Roll out only if every gate is satisfied.

## Expected useful outcome

The executable prints a shorter `Decision: recommend` invariant that still requires one authorized action and the governing Success branch. The observable recommendation is delay because latency violates its gate and the violated-gate branch precedes the unresolved-gate branch.

## Actual outcome

Run 80 changes only the `Decision: recommend` requirement to `Recommend one authorized action and name the governing Success branch.` Conversion is satisfied, latency is violated, and retention is unresolved. The only authorized action is delay, governed by the first Success branch. The shorter wording still forbids blending delay with diagnostic work and still identifies where authorization comes from.

## Whether the system helped

yes

## What broke

Before Run 80, `exactly one`, `authorized`, and `supplied success or reversal rule` partly restated guarantees already carried by `one authorized action`, the explicit `Success` field, and the requirement to name its governing branch.

## What would make the result more useful

Next, test whether the literal reasoning-sequence line duplicates the six ordered headings or still improves first-scan comprehension.