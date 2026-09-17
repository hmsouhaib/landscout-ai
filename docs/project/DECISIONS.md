# Durable decisions

These are evidenced decisions, not newly granted permissions. Sources are the exact [bootstrap ticket](tickets/DOCS.CONTINUITY.1.txt), named commits and current source/test companions. Appendix A is a supplied summary; unrecorded dates, rationale and rejected alternatives remain unavailable. `ACTIVE` means the decision governs its stated scope, not that every related implementation is independently approved or defect-free.

## DEC-001 — Evidence before decisions (ACTIVE)

User direction, Appendix A2: prefer official/open evidence; unknown stays unknown. Keep acquisition, normalization, physical/spatial facts, proxies, preliminary policy/precheck, diagnostics and eventual human decisions separate. Consequence: proximity cannot establish legal road access, heavy-truck access, grid capacity, connection feasibility or BESS authorization; no fabricated owners/contacts. Alternatives genuinely considered: unavailable; do not invent a prior score-first design. Affects all [pipelines](../code/DATA_FLOW.md) and [trust boundaries](../code/SOURCE_TRUST_MODEL.md).

## DEC-002 — Muret is a pilot, not permanent geography (ACTIVE)

User direction, Appendix A1; [README](../../README.md) and [scan configuration](../code/files/configs/scans/bess_muret.yaml.md). Product purpose is BESS-first land origination and preliminary analysis; commune 31395 is the proving ground. `SCAN -> FILTER -> ANALYZE -> SCORE -> IDENTIFY -> EXPORT -> HUMAN` describes the intended product, not existing autonomous orchestration. An overnight scan was an example, not a scheduling requirement. No date or discarded alternative is retained.

## DEC-003 — EP, Natura 2000 and ZNIEFF are separate sources (ACTIVE)

User direction, Appendix A2/A3. Current acquisition is the pinned EP archive; its evidence components do not implement the other archives or their semantic policies. Consequence: no category name in EP silently authorizes another source adapter or parcel rule. See [INPN source config](../code/files/configs/sources/inpn_protected_areas_fr.yaml.md) and [environment pipeline](../code/ENVIRONMENT_PIPELINE.md).

## DEC-004 — EP geometry rows use immutable SQLite bytes (ACTIVE)

Implementation commit `57edf93611d028092450a58de1b6df73bc6a1ee2`, STEP 7F.1B.3; rationale explicitly retained in Appendix A3 and DEV_LOG: locked Pyogrio 0.13.0 loses M during geometry-row conversion. Chosen route: verified GPKG bytes -> `sqlite3.deserialize` -> query-only FID/BLOB projection -> Standard GeoPackageBinary -> embedded ISO WKB -> Shapely. Metadata and attribute-only Pyogrio remain separate supported readers. Alternative actually addressed: Pyogrio geometry-row materialization. Consequences: preserve supported XY/XYZ/XYM/XYZM and EMPTY evidence; no repair, dimension dropping or reprojection. See [geometry module](../code/files/src/landscout/sources/inpn_protected_areas_geometry_fr.py.md) and [tests](../code/files/tests/unit/test_inpn_protected_areas_geometry_fr.py.md).

## DEC-005 — GEOMETRYCOLLECTION subtype correction (ACTIVE; supersedes earlier restrictive instruction)

Correction commit `9f696c2d687edddff4dc453e195034a7d9b41fac`, STEP 7F.1B.3.2. Appendix A3 explicitly says this corrected an earlier reviewer-written ticket. `GEOMETRYCOLLECTION` accepts GeometryCollection and MultiPoint/MultiLineString/MultiPolygon, not bare Point/LineString/Polygon. Keep exact metadata/SQL declaration equality and preserve actual root names/dimensions. The earlier restrictive instruction is **SUPERSEDED**, not erased or retrospectively approved. Its full original receipt is unavailable in the versioned record. Evidence: [geometry contract/tests](../code/TESTING_STRATEGY.md#inpn-geometry-byte-snapshot-and-measured-dimension-evidence).

## DEC-006 — Full physical FID alignment (ACTIVE)

STEP 7F.1B.4, `ca0ec73de37137b5515c1dfea14e2ea8a2a1ba3d`; Appendix A3/A4. Alignment compares the complete canonical physical FID sequence hash under the full package/layer identity, not merely counts and extrema. `[1,2,4]` and `[1,3,4]` are not equivalent; `id_mnhn` is not a substitute. Consequence: the immutable bundle binds independently validated profiles but creates no joined per-feature attribute/geometry table, semantic meaning or correct-georeferencing guarantee. [Bundle implementation](../code/files/src/landscout/sources/inpn_protected_areas_evidence_fr.py.md), [regressions](../code/files/tests/unit/test_inpn_protected_areas_evidence_fr.py.md).

## DEC-007 — Research draft is not runtime policy (ACTIVE)

STEP 7F.1C.1 publication `aa4ebc7063f2abdfcbae95154ba89b5b1a0dba02`; current user direction and Appendix A4/A5. Preserve `RESEARCH_DRAFT_NOT_RUNTIME_POLICY` and pending full semantic review. Inventory coverage (64 exact non-null keys) is not proof of snapshot applicability (zero confirmed meanings); marginal fields cannot prove co-occurrence, delimiter grammar or automatic `Nature`/`nature` equivalence. No executable mapping is authorized. Consequence: DOCS.CONTINUITY.1 is prioritized before further functional development. [Research pair](../reference/inpn_ep_2026_07_semantic_reference.md), [review scope](CONTEXT_PROVENANCE.md#known-review-boundary).

## DEC-008 — Separate product, reviewer and implementer roles (ACTIVE)

User direction, Appendix A1 and sections 0/5/10: Souhaib decides product direction; ChatGPT reviews/architects/authors tickets read-only; Codex implements, validates and publishes scoped work. Independent review precedes the next functional increment. One explicit Codex ticket at a time; corrective consolidation can be justified. Codex completion is not self-approval. Consequence: archive exact available review receipts during a later authorized Codex update; do not require the reviewer to write secretly to Git. [Working rules](WORKING_RULES.md).

## DEC-009 — CI/PR workflow deferred (DEFERRED)

Explicit user decision, Appendix A1 and section 8. Do not introduce CI, GitHub Actions, PR automation, branch policies or repository-setting changes in this ticket. A narrow offline local documentation checker does not reopen the decision. Rationale beyond prioritization, date and rejected automation alternatives are unavailable. [Backlog D-001](BACKLOG_AND_GAPS.md#deferred-by-user-decision).

## DEC-010 — Integrity evidence must resist aliases and in-place mutation (ACTIVE)

Implementation history STEP 7F.1A.4.1 and 7F.1A.4.2, documented in DEV_LOG and [immutable mapping](../code/files/src/landscout/common/immutable_mapping.py.md)/[regression suite](../code/files/tests/unit/test_deep_immutability.py.md). Frozen fields alone were insufficient: loaded trust configurations use immutable nested representations and copy incoming mutable collections; integrity JSON additionally rejects non-canonical/mutable leaves. Canonical serialization and public reconstruction remain separate requirements. This is not a claim that every returned GeoDataFrame or module-level `__all__` is deeply immutable. Exact model boundaries belong in the relevant companions; any discovered gap remains an application finding rather than a rewritten rule.

## DEC-011 — Physical authority and recovery material are preserved (ACTIVE)

Appendix A2/A3 and recovery history. Public source-complete APIs reconstruct trusted physical evidence; private intrinsic helpers are not equivalent trust roots. A true byte snapshot differs from hashing a path before and after reopening it. Verified local cache reuse stays offline; preserve useful backups and interrupted work. Consequence: no reset/restore/stash/clean/rebase/amend/merge/force-push merely to make a readiness check pass, and no dataset redownload solely for docs. [Cache/recovery](../code/CACHE_AND_RECOVERY.md), [trust model](../code/SOURCE_TRUST_MODEL.md).

## DEC-012 — Short isolated Windows pytest bases (ACTIVE operational rule)

User-approved workaround recorded in Appendix A7: each invocation uses a fresh SHORT unique base under `%LOCALAPPDATA%\LandScout\pytest-runs`. Earlier cleanup failed after successful test bodies; the final process exit code including cleanup is required. Do not reuse the default `pytest-current`, delete broad temp trees, reinstall dependencies or modify security settings. Native failures are observations to verify now, not perpetual assumptions. [Validation strategy](../code/TESTING_STRATEGY.md).

## DEC-013 — Written-planning evidence stays preliminary and route-scoped (ACTIVE)

Appendix A2: BESS ICPE applicability is not assumed; ICPE-only evidence must not be attached as an unconditional UP/AUp general prerequisite. Source excerpts/offsets, complete required articles and coherent evidence routes remain distinct proof obligations. No permit or legal prohibition follows from a precheck alone. [Written-zoning interpretation](../code/files/src/landscout/stages/interpret_bess_zoning.py.md), [planning pipeline](../code/PLANNING_PIPELINE.md). The original decision conversation and every discarded wording are unavailable; the supplied boundary is not expanded.

## Reversals and unresolved decisions

DEC-005 explicitly preserves its superseded predecessor. Other missing conversation-only reversals are HISTORY_GAP, not reconstructed. The exact EP export dictionary, all-null `statut`, documentary chronology and `sig_tadl` georeferencing remain [open questions](BACKLOG_AND_GAPS.md#source-and-semantic-questions), not decisions silently made by this audit.
