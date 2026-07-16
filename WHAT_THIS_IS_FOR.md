# What This Is For

_Last rewritten: 2026-07-15 after Run 135_

## 1. What problem is this system currently the best solution to?

Compiling a small, explicitly labeled decision handoff into an auditable analysis contract that prevents an analyst or agent from silently changing evidence, applicability, thresholds, gate logic, or authorized outcomes.

## 2. Who has this problem?

A nontechnical operator delegating one bounded decision whose source notes already state the decision, evidence, constraints, and success rule. The dangerous failure is not weak ideation; it is a plausible-looking recommendation that borrows authority from the wrong source, hides an unresolved gate, extrapolates beyond evidence scope, or invents a branch.

## 3. What is the narrowest version it already solves well?

Given exactly `Decision`, `Evidence`, `Constraints`, and `Success`, the tool either returns a repairable structural refusal or emits six ordered audit obligations. Those obligations preserve source-specific facts and conflicts, restrict transformations to supplied support, apply boundaries literally, judge every gate independently, and keep the recommendation inside a fully authorized Success branch.

## 4. What has the repeated testing revealed it is unusually good at?

It is becoming a compact authority-preservation compiler for messy but labeled decision notes. Its strongest behavior is maintaining the chain from supplied evidence to scope, from scope to gate judgment, and from gate judgment to the one action the supplied rule actually authorizes. Recent shipment scenarios show that it can distinguish unresolved evidence from an authorized fallback, require every fallback-specific gate, and compose complementary evidence without bridging gaps or reusing support by implication.

## 5. Why use it instead of a prompt or checklist?

The accumulated refusal boundaries are executable and scenario-tested. A checklist can say “consider evidence quality”; this compiler states what must remain visible, what cannot be inferred, when evidence may compose, which gates remain unresolved, and why a recommendation lacks authority. The result is inspectable before downstream analysis begins.

## 6. What is the biggest threat to usefulness?

Continuing to enumerate near-duplicate scope permutations after the authority model is already stable. A new rule is justified only when a concrete handoff exposes a distinct way the current obligations could authorize the wrong action, suppress an authorized action, or lose supplied meaning.

## 7. What should be removed or avoided?

Keep `machine.py` only because the historical demo command is mandatory. Do not add semantic classification, domain modes, calculations, configurable schemas, dashboards, evidence graphs, date engines, or generic workflow machinery. Prefer proving that an existing obligation survives a hostile scenario over adding redundant prose.