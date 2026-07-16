# 143 — Govern conflicting fallback precedence

## Type

hostile real decision handoff

## User

A laboratory operations manager delegating disposition of a temperature-exposed specimen batch.

## Situation

A batch fails its release-temperature gate. Two fallback branches qualify and two policies give opposite precedence, but one supplied governance rule establishes which policy controls.

## Input

Decision: Decide whether to release, local-reprocess, salvage-ship, or hold specimen batch B-251.
Evidence: Freezer F-14 recorded minus 62 degrees Celsius. The release boundary is at or below minus 70 degrees Celsius. The batch remains sealed. Reprocessing suite R-6 is validated, a qualified technician is available, and local-reprocessing authorization is signed. A validated dry-ice overpack is reserved, salvage-shipment authorization is signed, and a courier confirmed collection within four hours. Policy DP-9 gives local reprocessing precedence when both branches qualify. Policy NT-3 gives salvage shipment precedence when both branches qualify. Governance rule QG-2 states that DP-9 controls NT-3 for on-site specimen disposition, including batch B-251.
Constraints: Release requires storage at or below minus 70 degrees Celsius and an intact seal. Local reprocessing requires a violated temperature gate, an intact seal, a validated suite, an available qualified technician, and signed authorization. Salvage shipment requires a violated temperature gate, an intact seal, a reserved validated overpack, signed authorization, and confirmed courier collection within four hours. Neither fallback depends on the other.
Success: Release if both release gates are satisfied. Otherwise use any fully satisfied fallback according to supplied precedence. When supplied governance establishes which precedence policy controls, recommend the branch selected by that policy, cite the governance rule and governing policy, and preserve the displaced policy and branch as conflicting but non-governing.

## Expected useful outcome

The contract must mark the temperature gate violated and the seal gate satisfied. Both fallback branches qualify. QG-2 establishes that DP-9 governs, so local reprocessing must be recommended. The output must cite QG-2 and DP-9, preserve NT-3 as conflicting but non-governing, and preserve salvage shipment as satisfied but non-governing.

## Actual outcome

Run 145 exposed a traceability gap. The current rule allows governance evidence to resolve which policy governs, but does not explicitly require the recommendation to cite both the governance rule and selected policy or preserve the displaced policy as conflicting but non-governing.

## Whether the system helped

partial

## What broke

The selected branch could be correct while the authority chain or displaced conflicting policy disappears from the handoff.

## What would make the result more useful

Require a governance-resolved recommendation to cite the governance rule and selected precedence policy, while preserving displaced policies as conflicting but non-governing and displaced branches as satisfied but non-governing.