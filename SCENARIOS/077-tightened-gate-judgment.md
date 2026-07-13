# 077 — Tighten gate judgment without erasing independent results

## Type

structural-regression

## User

A product lead delegating a rollout decision with one satisfied gate, one violated gate, and one unresolved gate.

## Situation

The `Decision: judge gates` requirement must stay compact without allowing an overall delay verdict to hide which gate passed, which failed, which remains unresolved, what evidence supports each status, or how each affects the recommendation.

## Input

Decision: Choose whether to roll out the new checkout.
Evidence: Paid conversion is 23%. P95 latency is 540 milliseconds. The retention report states 70%, but the contract supplies no strict or inclusive comparator for the 70% threshold.
Constraints: Conversion must be at least 20%. Latency must be below 500 milliseconds. Retention has a threshold of 70%, with no comparator supplied.
Success: Roll out only if every gate is supported as satisfied. Otherwise delay and identify every blocking gate.

## Expected useful outcome

The executable prints a shorter `Decision: judge gates` invariant that still requires an independent status, supplied evidence, and recommendation effect for every gate, while forbidding an overall verdict from erasing violated or unresolved blockers.

## Actual outcome

Run 78 shortens only the `Decision: judge gates` requirement. Conversion is satisfied by the supplied 23% result. Latency is violated by the supplied 540 millisecond result. Retention remains unresolved because equality at 70% has no supplied comparator. The overall recommendation is delay, but all three gate-level results remain visible and the latency and retention gates retain their blocking effects.

## Whether the system helped

yes

## What broke

Before Run 78, the gate-judgment invariant repeated preservation and blocking language across one long sentence. The behavior was correct, but the core rule was less visible: judge every gate independently, cite its evidence, and carry its effect into the recommendation.

## What would make the result more useful

Next, test whether `Decision: recommend` can be tightened while still requiring one action and explicit traceability to the supplied success or reversal rule.
