# 145 — Honor an explicit governance exception

## Type

hostile real decision handoff

## User

A laboratory operations manager delegating disposition of a temperature-exposed specimen batch.

## Situation

A batch fails its release-temperature gate. Two fallback branches qualify and two policies give opposite precedence. A generally applicable governance rule would select one policy, but the same rule explicitly exempts batches under contamination hold, including the target batch.

## Input

Decision: Decide whether to release, local-reprocess, salvage-ship, or hold specimen batch B-261.
Evidence: Freezer F-18 recorded minus 62 degrees Celsius. The release boundary is at or below minus 70 degrees Celsius. The batch remains sealed. Reprocessing suite R-9 is validated, a qualified technician is available, and local-reprocessing authorization is signed. A validated dry-ice overpack is reserved, salvage-shipment authorization is signed, and a courier confirmed collection within four hours. Policy DP-9 gives local reprocessing precedence when both branches qualify. Policy NT-3 gives salvage shipment precedence when both branches qualify. Governance rule QG-4 states that DP-9 controls NT-3 for specimen disposition, except for batches under contamination hold. Batch B-261 is under contamination hold CH-11.
Constraints: Release requires storage at or below minus 70 degrees Celsius and an intact seal. Local reprocessing requires a violated temperature gate, an intact seal, a validated suite, an available qualified technician, and signed authorization. Salvage shipment requires a violated temperature gate, an intact seal, a reserved validated overpack, signed authorization, and confirmed courier collection within four hours. Neither fallback depends on the other. An explicit exception limits the authority of the rule that contains it.
Success: Release if both release gates are satisfied. Otherwise use any fully satisfied fallback according to supplied precedence. Apply a governance rule only when the target is inside its governing scope and outside every explicit exception. If conflicting precedence remains unresolved, hold the batch, preserve both policies and both satisfied branches, and identify governance authority covering contamination-hold batches as the missing evidence.

## Expected useful outcome

The contract must mark the temperature gate violated and the seal gate satisfied. Both fallback branches qualify. QG-4 generally resolves DP-9 versus NT-3, but its contamination-hold exception explicitly includes B-261, so QG-4 cannot govern this decision. The output must preserve QG-4 and its exception, preserve DP-9 and NT-3 as conflicting, preserve both fallback branches as satisfied candidates, recommend hold, and identify governance authority covering contamination-hold batches as missing.

## Actual outcome

Run 147 confirmed that the prior governance rule did not explicitly state how exceptions constrain otherwise applicable authority. The recommendation obligation was tightened so a governance rule governs only when the target is outside every supplied exception. QG-4 remains visible but non-governing; DP-9 and NT-3 remain conflicting; both fallback branches remain satisfied candidates; and hold is authorized pending governance authority covering contamination-hold batches.

## Whether the system helped

yes

## What broke

The authority trace covered governance scope but did not explicitly require checking exceptions within an otherwise applicable governance rule.

## What would make the result more useful

Test an exception whose applicability to the target is itself unresolved.