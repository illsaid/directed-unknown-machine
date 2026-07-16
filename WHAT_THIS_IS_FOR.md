# What This Is For

_Last rewritten: 2026-07-16 after Run 146_

## 1. What is this now?

A small authority-preservation compiler for bounded decision handoffs.

It accepts exactly four labeled fields — `Decision`, `Evidence`, `Constraints`, and `Success` — and emits a fixed audit contract that tells a downstream analyst or agent what must remain visible, what may be transformed, which gates govern which branches, and when no supplied authority permits a recommendation.

## 2. Who should use it?

An operator delegating a consequential but bounded decision from messy notes to an analyst, contractor, or agent. The operator already knows the decision to be made and can label the relevant material. The risk is that the recipient produces a plausible answer by changing scope, collapsing conflicts, borrowing authority, treating missing evidence as failure, or choosing an attractive branch that the supplied rule never authorized.

## 3. What narrow task does it solve well?

It converts a complete labeled handoff into six inspectable reasoning obligations. Those obligations preserve source-specific evidence, restrict transformations to explicitly supported operations, apply boundaries literally, judge each gate independently, map gates to supplied branches, and keep the final action inside the authority provided by `Success`.

When the handoff is structurally invalid, it refuses with a repairable explanation rather than inventing missing fields.

## 4. What has repeated testing revealed?

The useful core is not summarization or recommendation generation. It is preventing authority leakage.

Across measurement conflicts, threshold rules, fallback branches, duration scopes, overlapping populations, competing precedence policies, and governance rules, the same principle has held: a fact, rule, or authority may govern only the operation and scope it explicitly supports. Run 146 confirmed that even a valid governance rule cannot be borrowed from off-site disposition to settle an on-site policy conflict.

## 5. Why is this better than a checklist?

The rules are executable, ordered, and pressure-tested against concrete hostile scenarios. A checklist can remind an analyst to “check applicability.” This compiler states the consequence: preserve the out-of-scope authority, do not apply it, leave the affected branch unresolved, and name the exact authority still missing.

## 6. What is the current best use case?

Preparing an auditable decision-analysis handoff where multiple supplied rules, fallback actions, or precedence authorities could produce a confident but unauthorized answer.

Current demonstration:

```bash
python decision_brief.py SCENARIOS/144-out-of-scope-governance-precedence.md
```

The historical harness remains runnable:

```bash
python machine.py run SCENARIOS/001-friendly.md
```

## 7. What should not be built?

Do not add semantic classification, automatic policy interpretation, domain modes, dashboards, evidence graphs, date engines, configurable schemas, or workflow orchestration. The present threat is not missing flexibility; it is accumulating near-duplicate rules after the authority model has already generalized. Add executable behavior only when a concrete scenario exposes a distinct way the current contract can authorize the wrong action, suppress an authorized action, or lose supplied meaning.
