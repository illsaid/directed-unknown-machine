# 148 — Preserve conflicting applicability authorities

## Type

hostile real decision handoff

## User

A laboratory operations manager delegating disposition of a temperature-exposed specimen batch.

## Situation

A batch fails its release-temperature gate. Two fallback branches qualify and two policies give opposite precedence. A governance rule would select one policy unless the batch is under contamination hold. The hold-status records conflict, and two applicability authorities select opposite records with no supplied rule establishing which applicability authority controls.

## Input

Decision: Decide whether to release, local-reprocess, salvage-ship, or hold specimen batch B-276.
Evidence: Freezer F-21 recorded minus 59 degrees Celsius. The release boundary is at or below minus 70 degrees Celsius. The batch remains sealed. Reprocessing suite R-12 is validated, a qualified technician is available, and local-reprocessing authorization is signed. A validated dry-ice overpack is reserved, salvage-shipment authorization is signed, and a courier confirmed collection within four hours. Policy DP-9 gives local reprocessing precedence when both branches qualify. Policy NT-3 gives salvage shipment precedence when both branches qualify. Governance rule QG-4 states that DP-9 controls NT-3 for specimen disposition, except for batches under contamination hold. Hold order CH-19 lists B-276 under contamination hold. Quality release record CR-11 states that B-276 is cleared from contamination hold and is signed by the QA director. Applicability rule AR-6 states that, when hold-status records conflict, the QA-director-signed quality release record governs current contamination-hold status. Applicability rule AR-9 states that, when hold-status records conflict, the most recent active hold order governs current contamination-hold status. CH-19 is the most recent active hold order. No supplied governance rule establishes whether AR-6 or AR-9 controls.
Constraints: Release requires storage at or below minus 70 degrees Celsius and an intact seal. Local reprocessing requires a violated temperature gate, an intact seal, a validated suite, an available qualified technician, and signed authorization. Salvage shipment requires a violated temperature gate, an intact seal, a reserved validated overpack, signed authorization, and confirmed courier collection within four hours. Neither fallback depends on the other. Preserve both applicability authorities and both hold-status records.
Success: Release if both release gates are satisfied. Otherwise use any fully satisfied fallback according to supplied precedence. Apply QG-4 only if supplied evidence establishes that B-276 is outside its contamination-hold exception. Because AR-6 and AR-9 select opposite hold-status records and no supplied authority resolves their conflict, leave exception applicability, governance, precedence, and branch authority unresolved; hold the batch pending authority that establishes which applicability rule controls.

## Expected useful outcome

The contract must mark the temperature gate violated and the seal gate satisfied. Both fallback branches qualify. CH-19 and CR-11 conflict about exception applicability. AR-6 selects CR-11 while AR-9 selects CH-19. The output must preserve both applicability authorities and both records, refuse to choose either authority by recency, specificity, source rank, or convenience, leave QG-4 and branch authority unresolved, and recommend holding B-276 pending supplied governance evidence that establishes whether AR-6 or AR-9 controls.

## Actual outcome

Run 150 tightened the recommendation obligation so conflicting applicability authorities cannot silently resolve one another. AR-6, AR-9, CH-19, and CR-11 remain visible; exception applicability is unresolved; QG-4 cannot govern; DP-9 and NT-3 remain conflicting; both fallback branches remain satisfied candidates; and hold is authorized pending authority that selects the governing applicability rule.

## Whether the system helped

yes

## What broke

The contract preserved conflicting evidence and conflicting precedence authorities, but did not explicitly state that conflicting applicability authorities themselves leave downstream authority unresolved.

## What would make the result more useful

Test a supplied governance rule that explicitly selects one of the conflicting applicability authorities.