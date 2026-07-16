# 144 — Refuse out-of-scope governance precedence

## Type

hostile real decision handoff

## User

A laboratory operations manager delegating disposition of a temperature-exposed specimen batch.

## Situation

A batch fails its release-temperature gate. Two fallback branches qualify and two policies give opposite precedence. A supplied governance rule resolves that conflict only for off-site disposition, while the target batch is being dispositioned on site.

## Input

Decision: Decide whether to release, local-reprocess, salvage-ship, or hold specimen batch B-257.
Evidence: Freezer F-16 recorded minus 63 degrees Celsius. The release boundary is at or below minus 70 degrees Celsius. The batch remains sealed. Reprocessing suite R-8 is validated, a qualified technician is available, and local-reprocessing authorization is signed. A validated dry-ice overpack is reserved, salvage-shipment authorization is signed, and a courier confirmed collection within four hours. Policy DP-9 gives local reprocessing precedence when both branches qualify. Policy NT-3 gives salvage shipment precedence when both branches qualify. Governance rule QG-2 states that DP-9 controls NT-3 for off-site specimen disposition. Batch B-257 is being dispositioned on site.
Constraints: Release requires storage at or below minus 70 degrees Celsius and an intact seal. Local reprocessing requires a violated temperature gate, an intact seal, a validated suite, an available qualified technician, and signed authorization. Salvage shipment requires a violated temperature gate, an intact seal, a reserved validated overpack, signed authorization, and confirmed courier collection within four hours. Neither fallback depends on the other. A governance rule may resolve conflicting precedence only within its explicit disposition scope.
Success: Release if both release gates are satisfied. Otherwise use any fully satisfied fallback according to supplied precedence. Apply a governance rule only when its explicit scope covers the target disposition. If conflicting precedence remains unresolved, hold the batch, preserve both policies and both satisfied branches, and identify governance authority covering on-site disposition as the missing evidence.

## Expected useful outcome

The contract must mark the temperature gate violated and the seal gate satisfied. Both fallback branches qualify. QG-2 applies only to off-site disposition and therefore cannot establish that DP-9 governs this on-site decision. The output must preserve DP-9 and NT-3 as conflicting, preserve both fallback branches as satisfied candidates, recommend hold, and identify governance authority covering on-site disposition as missing.

## Actual outcome

Run 146 exposed a scope-specific authority gap. The compiler required governance evidence to resolve conflicting precedence, but did not explicitly state that governance authority is usable only within its supplied scope.

## Whether the system helped

partial

## What broke

A downstream analyst could borrow QG-2 from off-site disposition to resolve an on-site policy conflict merely because the same policy names appear.

## What would make the result more useful

Require governance evidence to resolve conflicting precedence only when its explicit scope covers the target decision; otherwise preserve the conflict and name governance authority for the uncovered scope as missing.