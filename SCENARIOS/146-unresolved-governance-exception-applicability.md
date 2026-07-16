# 146 — Preserve unresolved governance exception applicability

## Type

hostile real decision handoff

## User

A laboratory operations manager delegating disposition of a temperature-exposed specimen batch.

## Situation

A batch fails its release-temperature gate. Two fallback branches qualify and two policies give opposite precedence. A generally applicable governance rule would select one policy unless the batch is under contamination hold, but the supplied evidence does not establish whether that exception applies.

## Input

Decision: Decide whether to release, local-reprocess, salvage-ship, or hold specimen batch B-266.
Evidence: Freezer F-19 recorded minus 61 degrees Celsius. The release boundary is at or below minus 70 degrees Celsius. The batch remains sealed. Reprocessing suite R-10 is validated, a qualified technician is available, and local-reprocessing authorization is signed. A validated dry-ice overpack is reserved, salvage-shipment authorization is signed, and a courier confirmed collection within four hours. Policy DP-9 gives local reprocessing precedence when both branches qualify. Policy NT-3 gives salvage shipment precedence when both branches qualify. Governance rule QG-4 states that DP-9 controls NT-3 for specimen disposition, except for batches under contamination hold. Monitoring alert MA-27 flagged B-266 for contamination review. Quality review is pending; no contamination-hold order or clearance record has been supplied.
Constraints: Release requires storage at or below minus 70 degrees Celsius and an intact seal. Local reprocessing requires a violated temperature gate, an intact seal, a validated suite, an available qualified technician, and signed authorization. Salvage shipment requires a violated temperature gate, an intact seal, a reserved validated overpack, signed authorization, and confirmed courier collection within four hours. Neither fallback depends on the other. Do not infer that an exception is absent merely because its applicability is unresolved.
Success: Release if both release gates are satisfied. Otherwise use any fully satisfied fallback according to supplied precedence. Apply QG-4 only if supplied evidence establishes that B-266 is outside its contamination-hold exception. If exception applicability remains unresolved, hold the batch, preserve QG-4, DP-9, NT-3, and both satisfied fallback branches, and identify a contamination-hold order or clearance record as the missing evidence.

## Expected useful outcome

The contract must mark the temperature gate violated and the seal gate satisfied. Both fallback branches qualify. MA-27 establishes review, not contamination-hold status or clearance. QG-4 therefore cannot yet govern. The output must preserve QG-4 and its unresolved exception applicability, preserve DP-9 and NT-3 as conflicting, preserve both fallback branches as satisfied candidates, recommend hold, and identify a contamination-hold order or clearance record as missing evidence.

## Actual outcome

Run 148 exposed a remaining authority gap: the recommendation obligation blocks a governance rule when an exception is established, but does not explicitly block it when applicability of the exception is unresolved. Without that distinction, absence of a supplied hold order could be mistaken for evidence that the target is outside the exception.

## Whether the system helped

partial

## What broke

The compiler did not explicitly require unresolved exception applicability to leave governance authority unresolved.

## What would make the result more useful

Require positive evidence that the target is outside every exception before governance can resolve precedence; when exception applicability is unresolved, preserve the uncertainty, withhold branch authority, and name the evidence needed to resolve it.
