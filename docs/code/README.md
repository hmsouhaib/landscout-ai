# LandScout technical code reference

## How an AI agent should use this documentation

For cross-chat entry, first read [AGENTS.md](../../AGENTS.md), [working rules](../project/WORKING_RULES.md), [current state](../project/CURRENT_STATE.md) and the [resume route](../project/RESUME.md). This technical index does not supersede the active ticket, review gate or interruption ledger.

1. Read [ARCHITECTURE.md](ARCHITECTURE.md) first.
2. Read [DATA_FLOW.md](DATA_FLOW.md).
3. Read the relevant pipeline document for Cadastre, grid, road, planning, or environment.
4. Open the companion document under `files/` for every file that may be modified.
5. Compare exact Git-content bytes with the companion's `Source SHA256` under its explicit binding basis; distinguish checkout EOL bytes from Git content and Git blob IDs.
6. If the SHA differs, treat the companion as potentially stale.
7. Source/tests establish observed behavior. If it contradicts user-approved intent or the source contract, record an application finding; do not rewrite the intended contract to legitimize a defect. DEV_LOG reports are historical evidence, not current behavior or independent approval.
8. Inspect every named test and its source before changing an implementation.
9. Never invent evidence to replace an `UNKNOWN`, null, missing source value, or unresolved applicability.
10. Preserve source-complete trust boundaries and the distinction between factual data, proxy evidence, policy interpretation, diagnostics, and parcel prechecks.
11. Update the relevant companion and cross-cutting documents whenever a documented source file changes.

## What this documentation contains

- [ARCHITECTURE.md](ARCHITECTURE.md): product scope, code layers, dependency direction, public boundaries, and implemented/unimplemented phases.
- [DATA_FLOW.md](DATA_FLOW.md): exact high-level object flow for Cadastre, grid, road, planning, and environment.
- [SOURCE_TRUST_MODEL.md](SOURCE_TRUST_MODEL.md): HTTPS, DNS/socket binding, configuration identity, byte verification, extraction, lineage, and source-complete revalidation.
- [GIS_AND_CRS.md](GIS_AND_CRS.md): storage/calculation CRSs, geometry preservation, metric calculations, overlays, nearest-distance logic, and coverage boundaries.
- [CACHE_AND_RECOVERY.md](CACHE_AND_RECOVERY.md): adapter-specific cache, `.part`, `.bak`, publication, rollback, cleanup, and manual-recovery behavior.
- Pipeline documents: [CADASTRE_PIPELINE.md](CADASTRE_PIPELINE.md), [GRID_PIPELINE.md](GRID_PIPELINE.md), [ROAD_PIPELINE.md](ROAD_PIPELINE.md), [PLANNING_PIPELINE.md](PLANNING_PIPELINE.md), and [ENVIRONMENT_PIPELINE.md](ENVIRONMENT_PIPELINE.md).
- [TESTING_STRATEGY.md](TESTING_STRATEGY.md): test organization, fixture boundaries, failure injection, and the limits of synthetic evidence.
- [GLOSSARY.md](GLOSSARY.md): exact project terminology.
- [CHANGE_IMPACT_GUIDE.md](CHANGE_IMPACT_GUIDE.md): downstream review checklist by change type.
- [FILE_INDEX.md](FILE_INDEX.md): one-sentence navigation entry and companion link for every tracked project file.
- `files/<original path>.md`: byte-bound, source-derived reference for each tracked file outside `docs/code/**`.

## Authority and staleness

Observed implementation, user-approved intent/source contracts, actual test execution and independent review are distinct kinds of authority. A companion SHA proves byte identity, not explanatory fidelity, comprehensive coverage or approval. The portable binding basis is SHA256 of exact Git-stored content, not Git's blob object ID or an implicitly normalized checkout. DOCS.CONTINUITY.1 tracks its migration and any EOL-only exception in the [audit ledger](audit/DOCUMENTATION_AUDIT.md); while that ledger remains partial, do not claim every header has been migrated.

The reference intentionally exposes private functions and test helpers because their changes can affect a public trust boundary even when they are not exported. The [local checker](../../tools/audit_documentation.py) checks recorded mechanics offline; its passing status never grants independent semantic approval. [Project provenance](../project/CONTEXT_PROVENANCE.md) separates publication, historical reports, current executions and actual review scope.

This tree documents the repository at the commit named in the surrounding Git history. It does not turn current proxy evidence into legal, engineering, capacity, ownership, environmental, ranking, or authorization conclusions.
