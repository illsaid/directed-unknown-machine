# 075 — Tighten boundary reconciliation without cross-authorizing support

## Type

structural-regression

## User

A product lead delegating a rollout decision with both same-metric rule conflicts and cross-unit boundary statements.

## Situation

The `Boundary: reconcile` requirement protects two different operations: selecting among conflicting same-metric rules by supplied precedence, and reconciling cross-unit statements by supplied conversion or equivalence. The operator needs a shorter invariant that does not let evidence for either operation authorize the other.

## Input

Decision: Choose whether to roll out the new checkout.
Evidence: Paid conversion is 21%. P95 latency is 480 milliseconds. Retention is 71%. The experiment charter explicitly states that the revised conversion rule of at least 22% supersedes the earlier rule of at least 20%. A separate infrastructure note defines 1 second as 1000 milliseconds, but supplies no statement connecting the latency rules below. No source states which retention rule governs.
Constraints: Preserve both conversion rules and report the result under each before applying the supplied charter precedence. Conversion must be at least 20% under the original plan and at least 22% under the revised plan. Latency must be below 500 milliseconds and below 0.5 seconds; do not use conversion precedence as unit-equivalence support. Retention must be at least 70% under one note and at least 72% under another; do not use the infrastructure equivalence as precedence support.
Success: Roll out only if every governing gate is supported as satisfied. Otherwise delay and identify each unresolved or violated gate.

## Expected useful outcome

The executable prints a shorter `Boundary: reconcile` invariant that still requires exact operation-specific support, preserves displaced same-metric rules and their results, requires supplied conversion or equivalence for cross-unit reconciliation, leaves unsupported conflicts unresolved, and prevents precedence and equivalence evidence from authorizing each other.

## Actual outcome

Run 76 shortens only the `Boundary: reconcile` requirement. The charter validly selects the revised 22% conversion rule while preserving the original 20% result, so conversion violates the governing rule. The latency statements remain unresolved because no supplied source connects 500 milliseconds and 0.5 seconds for this contract, and conversion precedence cannot fill that gap. The retention conflict also remains unresolved because unit-equivalence evidence cannot choose between the 70% and 72% rules. The governed recommendation is delay.

## Whether the system helped

yes

## What broke

Before Run 76, the reconciliation invariant repeated the shared exact-support rule inside separate clauses. The refusal boundaries were correct, but the wording obscured that precedence and equivalence are distinct authorization operations.

## What would make the result more useful

Next, test whether `Boundary: apply` can be shortened without weakening full-range handling or supplied equality semantics.