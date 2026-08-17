# LandScout technical code reference

## How an AI agent should use this documentation

1. Read [ARCHITECTURE.md](ARCHITECTURE.md) first.
2. Read [DATA_FLOW.md](DATA_FLOW.md).
3. Read the relevant pipeline document for Cadastre, grid, road, planning, or environment.
4. Open the companion document under `files/` for every file that may be modified.
5. Compare the source file's exact byte SHA256 with the companion's `Source SHA256`.
6. If the SHA differs, treat the companion as potentially stale.
7. Source code always wins over this documentation and over `docs/DEV_LOG.md`.
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

The implementation hierarchy is source code, checked-in configuration, tests, physical/source contracts, and only then historical development evidence. A companion SHA is standard SHA256 of exact file bytes, not a Git blob ID. The reference intentionally exposes private functions and test helpers because future changes to those helpers can alter a public trust boundary even when the helper is not exported.

This tree documents the repository at the commit named in the surrounding Git history. It does not turn current proxy evidence into legal, engineering, capacity, ownership, environmental, ranking, or authorization conclusions.
