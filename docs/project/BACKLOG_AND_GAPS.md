# Backlog and evidence gaps

This is a classified queue, not permission to implement proposals. Evidence comes from the [bootstrap ticket](tickets/DOCS.CONTINUITY.1.txt), Git, [step ledger](STEP_LEDGER.json) and [audit findings](../code/audit/DOCUMENTATION_AUDIT.md).

## Authorized but unfinished

- `W-001` — DOCS.CONTINUITY.1: complete the file/symbol content audit, checker/tests, portable source bindings, durable history/state and final validation. Status **IN_PROGRESS**, no partial completion publication.

## Independent reviews pending

- `R-001` — Full independent semantic review of STEP 7F.1C.1 at `aa4ebc7063f2abdfcbae95154ba89b5b1a0dba02`: all 64 entries, 42 documents and full reference equivalence were not reviewed by the supplied bootstrap verdict. Its 64 inventory entries are not 64 executable meanings; zero meanings are confirmed for the snapshot.
- `R-002` — Independent review of DOCS.CONTINUITY.1 once actually published, tied to that Git-resolved commit and precise scope. Codex cannot close it.
- `R-003` — Cold-start comprehension acceptance: an [interim fresh-context exercise](COLD_START_EXERCISE.md) was executed on 2026-09-17 and separately verified within a bounded scope. Final acceptance remains pending while the audit is partial; this does not constitute ChatGPT's independent approval.

## Proposed future work, not authorized

- `P-001` — Any executable EP semantic mapping needs independent review of the draft and an explicit new ticket with proven producer/field/value/snapshot correspondence.
- `P-002` — Future environmental geometry selection/normalization and parcel analysis require separate contracts and authorization.
- `P-003` — Global scoring, owner/contact discovery, production export/human delivery and orchestration remain product outcomes, not approved tasks here.

## Deferred by user decision

- `D-001` — CI, PR workflow and pipeline automation. A read-only local documentation checker does not reopen this decision. No date or rejected implementation alternative is invented.

## Source and semantic questions

- `S-001` — Exact EP producer export edition/dictionary and field/value correspondence remain unresolved; the unversioned CNIG conformity announcement is insufficient.
- `S-002` — All 11,381 `statut` NULLs; `Nature` versus `nature`; compound-label syntax; CEN “ou assimilé”; Apia history; local, seasonal, perimeter/buffer and maritime wording require the dossier's explicit qualifications.
- `S-003` — CNIG project chronology conflicts with its own draft/consultation status; historical COVADIS adoption is not proof of the later export contract.
- `S-004` — `EP/sig_tadl.gpkg`: EPSG:32753 versus its geographic-looking coordinates remains an observation, not proof of an alternative CRS. Matching bounds do not resolve real georeferencing.
- `S-005` — PDF visual inspection and some official-source access remain limited. Do not claim a newer audit closed them without an actual successful execution.

## Historical material unavailable in the versioned record

- `H-001` — Appendix A is a selected user-supplied summary, not a full chat export. Unavailable conversation text cannot be reconstructed verbatim.
- `H-002` — Full original independent-review receipts for earlier steps, including the approved 7F.1B.4 boundary, are not retained here. Use `APPROVED_RECORDED_IN_CONVERSATION` only for the precise supplied scope; older intermediate commits are not implicitly approved.
- `H-003` — Earlier exact ticket prompts are not supplied by Git/DEV_LOG. A purpose/summary reconstructed from commits is not an original prompt. Per-step availability and ambiguous mappings belong in STEP_LEDGER.
- `H-004` — Historical test and real-source runs are reported evidence unless rerun in this audit. Existing source snapshots are not being redownloaded/reprofiled merely for documentation.
- `H-005` — Any remaining ambiguous step/commit association or decision rationale must stay explicitly unresolved rather than being filled from a plausible commit title.

## Application findings

No claim of a defect-free codebase is made. These findings require separate corrective tickets; documentation changes do not redefine the intended contracts to excuse observed behavior.

- `A-001` — **OPEN, contract-integrity gap**: `landscout.common.cadastre_contract.validate_normalized_cadastre_parcels` checks Z but not M. A valid XYM polygon (`has_z=False`, `has_m=True`, coordinate dimension 3), with a coherent EPSG:2154 area, passes the intrinsic canonical boundary unchanged. The approved exactly-2D parcel contract remains intended. Reproduction is in-memory, not a demonstrated official acquisition path or claim of changed real parcels. The exact fixture/command and observed result are retained in [foundations review](../code/audit/reviews/foundations.json).
- `A-002` — **OPEN, controlled-error gap**: `landscout.sources.rte_odre_fr._validate_geojson_geometry` receives `{"type": [], "coordinates": [1, 43]}` or the corresponding dict-valued `type`; unhashable membership leaks `TypeError` instead of `RteOdreDownloadError`. This is a pure-helper malformed-input reproduction, not an end-to-end request/cache run and not evidence of unsafe outbound access. Exact commands/results are in the same review fragment. Preserve recovery/network behavior in any separately authorized correction.
- `A-003` — **OPEN, MEDIUM, producer/validator contract mismatch**: `landscout.stages.enrich_planning_features.intersect_parcels_with_gpu_planning_features` preserves physical optional `LIBELLE = " Label "` in both the feature catalog and relation, but `validate_normalized_planning_feature_inputs` rejects it with `PlanningFeaturesError: Feature catalog label raw must be a non-empty exact string`. A fresh offline synthetic GeoPackage reproduction succeeded on 2026-09-17; [command, fixture, output and limits](../code/audit/RECOVERY_STATUS_2026-09-17.md#application-findings). This is not an official GPU acquisition or evidence that exact raw-text preservation is wrong. Resolve the public contract in a separately authorized ticket; no production or existing test was changed.
- `A-004` — **OPEN, model/result reference-contract mismatch**: in `src/landscout/stages/resolve_planning_feature_codes.py`, `CnigFeatureCodeRecord._validate_record` / `_validate_optional_official_text` accept canonical literal `"None"` as a non-null legal reference, while `_validate_nullable_official_value` rejects it in the result dictionary. R4 reproduced only this record-model/helper difference in memory, derived from a copy of the checked-in INFORMATION 99/00 row; no full profile forgery or source-complete resolver execution. The same guard names `"nan"` and `"<NA>"` (source-read, not separately executed). Current YAML uses true null and is unchanged. [Exact scope and reproduction](../code/audit/R4_CNIG_CONFIGURATION.md#r4-application-finding); requires separate corrective authority, not a documentation fix or claim of affected official rows.
