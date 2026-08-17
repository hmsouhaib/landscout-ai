# `configs/sources/rte_odre_fr.yaml`

## File identity

- Repository path: `configs/sources/rte_odre_fr.yaml`
- File type: YAML configuration
- Primary responsibility: Pins the official ODRÉ API/cache identity and exact RTE dataset IDs/formats.
- Layer / domain: `checked-in configuration` / `grid`
- Public or internal role: Repository artifact; not a Python public API.
- Source SHA256: `f2b5ffb43b1e8a73e1396eda3d91b42fe9074bc348a94a61ea84c1c29e1a8649`

## 1. Purpose

Pins the official ODRÉ API/cache identity and exact RTE dataset IDs/formats.

## 2. Position in LandScout architecture

This `checked-in configuration` artifact supplies exact checked-in bytes to the current repository. Consumers found by exact path reference are: `docs/DEV_LOG.md`, `src/landscout/sources/rte_odre_fr.py`, `tests/unit/test_rte_odre_fr.py`.

## 3. Imports and dependencies

Not a Python module. Its consumers parse or interpret the bytes using the source/configuration functions identified by repository references and pipeline documentation.

## 4. Constants and domains

Every parsed leaf field is listed below; list indices preserve source order.

| Field path | Exact checked-in value | Contract role |
|---|---|---|
| `provider` | `"RTE"` (`str`) | Names the configured source provider copied/compared as lineage. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/rte_odre_fr.py`, `tests/unit/test_rte_odre_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `portal` | `"ODRE"` (`str`) | Configures `portal` under the exact parent path `<root>`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/rte_odre_fr.py`, `tests/unit/test_rte_odre_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `api.base_url` | `"https://odre.opendatasoft.com/api/explore/v2.1"` (`str`) | Pins the exact official HTTPS API origin/path used to build requests. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/rte_odre_fr.py`, `tests/unit/test_rte_odre_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `datasets.sites.dataset_id` | `"postes-electriques-rte"` (`str`) | Selects the exact external dataset identity used in source URL/API/cache validation. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/rte_odre_fr.py`, `tests/unit/test_rte_odre_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `datasets.sites.preferred_format` | `"geojson"` (`str`) | Configures `preferred format` under the exact parent path `datasets.sites`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/rte_odre_fr.py`, `tests/unit/test_rte_odre_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `datasets.overhead_lines.dataset_id` | `"lignes-aeriennes-rte-nv"` (`str`) | Selects the exact external dataset identity used in source URL/API/cache validation. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/rte_odre_fr.py`, `tests/unit/test_rte_odre_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `datasets.overhead_lines.preferred_format` | `"geojson"` (`str`) | Configures `preferred format` under the exact parent path `datasets.overhead_lines`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/rte_odre_fr.py`, `tests/unit/test_rte_odre_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `datasets.underground_lines.dataset_id` | `"lignes-souterraines-rte-nv"` (`str`) | Selects the exact external dataset identity used in source URL/API/cache validation. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/rte_odre_fr.py`, `tests/unit/test_rte_odre_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `datasets.underground_lines.preferred_format` | `"geojson"` (`str`) | Configures `preferred format` under the exact parent path `datasets.underground_lines`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/rte_odre_fr.py`, `tests/unit/test_rte_odre_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `cache.max_age_hours` | `168` (`int`) | Configures `max age hours` under the exact parent path `cache`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/rte_odre_fr.py`, `tests/unit/test_rte_odre_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |

## 5. Classes / models / dataclasses

Not applicable; this file declares no Python class.

## 6. Functions and methods

Not applicable; this file declares no Python function or method.

## 7. Data contracts

The exact byte-bound values or text lines above are the data contract for this file. Structured validators in consuming Python modules remain authoritative for types, nullability, allowed values, units, source provenance, calculations, and downstream semantics.

## 8. Interfaces

Direct literal-path consumers are listed above. Git, uv, Python, configuration loaders, documentation readers, or generated-data directory conventions consume project metadata according to the file type.

## 9. Error handling

This passive file raises no exception. Its consumers reject missing, malformed, unsupported, duplicate, semantically invalid, or stale content with their documented controlled errors.

## 10. Side effects

The file itself has no runtime side effect. A consumer may read it, resolve dependencies, configure tools, or use it as source/policy evidence; those effects belong to the consuming function.

## 11. Security / trust boundaries

The SHA256 binds this documentation to exact bytes. Checked-in configuration identity is necessary but does not replace physical source/hash verification performed by source-complete adapters.

## 12. GIS / CRS rules

Only structured CRS fields listed above impose a GIS rule, and their consuming validators define it. Otherwise not applicable.

## 13. Provenance rules

Checked-in source locks, URLs, hashes, versions, profile IDs, and evidence references are textual provenance inputs. Their consuming code determines whether and how physical bytes are revalidated.

## 14. Business meaning

This file supports the `grid` domain only through its exact checked-in values and current consumers.

## 15. Explicit non-goals

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

## 16. Tests

Tests that load or mention this path are documented in their companion files. No test is inferred solely from the filename.

## 17. Change impact

Changing these bytes requires reviewing every consuming validator, source/policy/config hash, generated result or artifact lineage, affected tests, and this companion SHA256. Dependency-lock changes also require `uv lock --check` and `uv pip check`.
