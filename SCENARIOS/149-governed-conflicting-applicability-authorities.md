# 149 — Govern conflicting applicability authorities

## Type

hostile real decision handoff

## User

A laboratory operations manager delegating disposition of a temperature-exposed specimen batch.

## Situation

A batch fails its release-temperature gate. Two fallback branches qualify, two policies give opposite precedence, and two applicability authorities select opposite contamination-hold records. A supplied governance rule explicitly establishes which applicability authority controls.

## Input

Decision: Decide whether to release, local-reprocess, salvage-ship, or hold specimen batch B-281.
Evidence: Freezer F-24 recorded minus 58 degrees Celsius. The release boundary is at or below minus 70 degrees Celsius. The batch remains sealed. Reprocessing suite R-15 is validated, a qualified technician is available, and local-reprocessing authorization is signed. A validated dry-ice overpack is reserved, salvage-shipment authorization is signed, and a courier confirmed collection within four hours. Policy DP-9 gives local reprocessing precedence when both branches qualify. Policy NT-3 gives salvage shipment precedence when both branches qualify. Governance rule QG-4 states that DP-9 controls NT-3 for specimen disposition, except for batches under contamination hold. Hold order CH-23 lists B-281 under contamination hold. Quality release record CR-15 states that B-281 is cleared from contamination hold and is signed by the QA director. Applicability rule AR-6 states that, when hold-status records conflict, the QA-director-signed quality release record governs current contamination-hold status. Applicability rule AR-9 states that, when hold-status records conflict, the most recent active hold order governs current contamination-hold status. CH-23 is the most recent active hold order. Governance rule AG-2 states that AR-6 controls AR-9 for current specimen contamination-hold status.
Constraints: Release requires storage at or below minus 70 degrees Celsius and an intact seal. Local reprocessing requires a violated temperature gate, an intact seal, a validated suite, an available qualified technician, and signed authorization. Salvage shipment requires a violated temperature gate, an intact seal, a reserved validated overpack, signed authorization, and confirmed courier collection within four hours. Neither fallback depends on the other. Preserve both applicability authorities, both hold-status records, both precedence policies, and both satisfied fallback branches.
Success: Release if both release gates are satisfied. Otherwise use any fully satisfied fallback according to supplied precedence. Apply AG-2 to select AR-6; apply AR-6 to select CR-15 as governing current hold-status evidence; preserve AR-9 and CH-23 as conflicting but non-governing. Because CR-15 establishes that B-281 is outside QG-4's exception, apply QG-4 to select DP-9, then authorize local reprocessing. Preserve NT-3 and salvage shipment as satisfied but non-governing.

## Expected useful outcome

The contract must mark the temperature gate violated and the seal gate satisfied. Both fallback branches qualify. AG-2 must govern the applicability-authority conflict, AR-6 must select CR-15, and CH-23 plus AR-9 must remain visible as conflicting but non-governing. CR-15 establishes that B-281 is outside QG-4's exception; QG-4 therefore selects DP-9; DP-9 authorizes local reprocessing. The output must preserve the complete authority chain AG-2 to AR-6 to CR-15 to QG-4 to DP-9, while preserving NT-3 and salvage shipment as satisfied but non-governing.

## Actual outcome

Run 151 requires governance-resolved applicability authority to retain the complete authority trace. AG-2 selects AR-6; AR-6 selects CR-15; AR-9 and CH-23 remain conflicting but non-governing; CR-15 establishes that the exception does not apply; QG-4 selects DP-9; DP-9 authorizes local reprocessing; and NT-3 plus salvage shipment remain satisfied but non-governing.

## Whether the system helped

yes

## What broke

The contract preserved unresolved conflicts between applicability authorities, but did not explicitly require the complete governance-to-applicability-to-evidence authority chain when supplied governance resolves that conflict.

## What would make the result more useful

Test a governance rule whose scope covers only one of several hold-status dimensions, so resolved contamination status cannot be borrowed to resolve a separate release-status conflict.