# 147 — Resolve conflicting exception evidence with supplied applicability authority

## Type

hostile real decision handoff

## User

A laboratory operations manager delegating disposition of a temperature-exposed specimen batch.

## Situation

A batch fails its release-temperature gate. Two fallback branches qualify and two policies give opposite precedence. A governance rule would select one policy unless the batch is under contamination hold. The supplied hold-status records conflict, but a separate applicability rule identifies which record governs.

## Input

Decision: Decide whether to release, local-reprocess, salvage-ship, or hold specimen batch B-271.
Evidence: Freezer F-20 recorded minus 60 degrees Celsius. The release boundary is at or below minus 70 degrees Celsius. The batch remains sealed. Reprocessing suite R-11 is validated, a qualified technician is available, and local-reprocessing authorization is signed. A validated dry-ice overpack is reserved, salvage-shipment authorization is signed, and a courier confirmed collection within four hours. Policy DP-9 gives local reprocessing precedence when both branches qualify. Policy NT-3 gives salvage shipment precedence when both branches qualify. Governance rule QG-4 states that DP-9 controls NT-3 for specimen disposition, except for batches under contamination hold. Hold order CH-14 lists B-271 under contamination hold. Quality release record CR-8 states that B-271 is cleared from contamination hold and is signed by the QA director. Applicability rule AR-6 states that, when hold-status records conflict, the QA-director-signed quality release record governs current contamination-hold status.
Constraints: Release requires storage at or below minus 70 degrees Celsius and an intact seal. Local reprocessing requires a violated temperature gate, an intact seal, a validated suite, an available qualified technician, and signed authorization. Salvage shipment requires a violated temperature gate, an intact seal, a reserved validated overpack, signed authorization, and confirmed courier collection within four hours. Neither fallback depends on the other. Preserve conflicting exception-status records even when supplied applicability authority identifies one as governing.
Success: Release if both release gates are satisfied. Otherwise use any fully satisfied fallback according to supplied precedence. Apply QG-4 only if supplied evidence establishes that B-271 is outside its contamination-hold exception. Use AR-6 to resolve the conflicting hold-status records, preserve the displaced record as conflicting but non-governing, apply QG-4 and DP-9 if CR-8 governs, and local-reprocess the batch.

## Expected useful outcome

The contract must mark the temperature gate violated and the seal gate satisfied. Both fallback branches qualify. CH-14 and CR-8 conflict about exception applicability. AR-6 makes CR-8 governing because it is a QA-director-signed quality release record. The output must preserve CH-14 as conflicting but non-governing, establish that B-271 is outside QG-4's exception, preserve NT-3 and salvage shipment as non-governing, and recommend local reprocessing under the authority chain AR-6 to CR-8 to QG-4 to DP-9.

## Actual outcome

Run 149 found that no new executable rule was needed. The existing evidence-preservation obligation already allows supplied applicability evidence to resolve conflicting records while preserving displaced sources, and the governance obligation already requires positive evidence that the target is outside every exception. Applied together, AR-6 makes CR-8 governing, CH-14 remains conflicting but non-governing, QG-4 governs, DP-9 selects local reprocessing, and NT-3 plus salvage shipment remain satisfied but non-governing.

## Whether the system helped

yes

## What broke

Nothing. The existing general applicability and governance obligations compose correctly for conflicting exception-status evidence.

## What would make the result more useful

Test conflicting applicability authorities that select opposite exception-status records.