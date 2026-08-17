# `configs/sources/inpn_protected_areas_fr.yaml`

## File identity

- Repository path: `configs/sources/inpn_protected_areas_fr.yaml`
- File type: YAML configuration
- Primary responsibility: Pins the PatriNat/MNHN/INPN EP 07/2026 archive identity, size, SHA256, URLs, and cache root.
- Layer / domain: `checked-in configuration` / `environment`
- Public or internal role: Repository artifact; not a Python public API.
- Source SHA256: `75e3e45003b66cff10a755dfd64c27d3066ba65e4807af6e17e82bd3eae03397`

## 1. Purpose

Pins the PatriNat/MNHN/INPN EP 07/2026 archive identity, size, SHA256, URLs, and cache root.

## 2. Position in LandScout architecture

This `checked-in configuration` artifact supplies exact checked-in bytes to the current repository. Consumers found by exact path reference are: `src/landscout/sources/inpn_protected_areas_fr.py`, `tests/unit/test_inpn_protected_areas_fr.py`.

## 3. Imports and dependencies

Not a Python module. Its consumers parse or interpret the bytes using the source/configuration functions identified by repository references and pipeline documentation.

## 4. Constants and domains

Every parsed leaf field is listed below; list indices preserve source order.

| Field path | Exact checked-in value | Contract role |
|---|---|---|
| `provider` | `"PatriNat"` (`str`) | Names the configured source provider copied/compared as lineage. Consumers found by exact repository path reference: `src/landscout/sources/inpn_protected_areas_fr.py`, `tests/unit/test_inpn_protected_areas_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `authority` | `"MNHN"` (`str`) | Names the configured publishing/oversight authority retained as source identity. Consumers found by exact repository path reference: `src/landscout/sources/inpn_protected_areas_fr.py`, `tests/unit/test_inpn_protected_areas_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `program` | `"INPN"` (`str`) | Names the official source program retained as identity. Consumers found by exact repository path reference: `src/landscout/sources/inpn_protected_areas_fr.py`, `tests/unit/test_inpn_protected_areas_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `dataset_id` | `"EP"` (`str`) | Selects the exact external dataset identity used in source URL/API/cache validation. Consumers found by exact repository path reference: `src/landscout/sources/inpn_protected_areas_fr.py`, `tests/unit/test_inpn_protected_areas_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `dataset_name` | `"Base de référence des espaces protégés français"` (`str`) | Records the exact human-readable external dataset name. Consumers found by exact repository path reference: `src/landscout/sources/inpn_protected_areas_fr.py`, `tests/unit/test_inpn_protected_areas_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `declared_version` | `"07/2026"` (`str`) | Pins the declared source snapshot version and contributes to cache/source identity. Consumers found by exact repository path reference: `src/landscout/sources/inpn_protected_areas_fr.py`, `tests/unit/test_inpn_protected_areas_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `reference_page_url` | `"https://www.patrinat.fr/fr/page-temporaire-de-telechargement-des-referentiels-de-donnees-lies-linpn-7353"` (`str`) | Records the official reference-page provenance URL; it is not the archive bytes. Consumers found by exact repository path reference: `src/landscout/sources/inpn_protected_areas_fr.py`, `tests/unit/test_inpn_protected_areas_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `archive_url` | `"https://assets.patrinat.fr/files/donnees/ep/EP.zip"` (`str`) | Pins the official HTTPS archive location; transport safety and adapter origin/path checks still apply. Consumers found by exact repository path reference: `src/landscout/sources/inpn_protected_areas_fr.py`, `tests/unit/test_inpn_protected_areas_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `archive_filename` | `"EP.zip"` (`str`) | Pins the portable archive basename used by cache/source validation. Consumers found by exact repository path reference: `src/landscout/sources/inpn_protected_areas_fr.py`, `tests/unit/test_inpn_protected_areas_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `expected_archive_size_bytes` | `99835011` (`int`) | Pins the exact approved archive byte length. Consumers found by exact repository path reference: `src/landscout/sources/inpn_protected_areas_fr.py`, `tests/unit/test_inpn_protected_areas_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `expected_archive_sha256` | `"73688bc37205a5e7f59e2065a0b81fc8cf2a242bdec5d7d2786f083671c4abe5"` (`str`) | Pins the lowercase SHA256 of the approved archive bytes. Consumers found by exact repository path reference: `src/landscout/sources/inpn_protected_areas_fr.py`, `tests/unit/test_inpn_protected_areas_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `cache_root` | `".cache/landscout/inpn/protected_areas"` (`str`) | Selects the repository-relative cache root; containment/link/recovery checks apply at runtime. Consumers found by exact repository path reference: `src/landscout/sources/inpn_protected_areas_fr.py`, `tests/unit/test_inpn_protected_areas_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |

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

This file supports the `environment` domain only through its exact checked-in values and current consumers.

## 15. Explicit non-goals

- Protected-area acquisition does not interpret categories, intersect parcels, exclude land, or calculate an environmental score.

## 16. Tests

Tests that load or mention this path are documented in their companion files. No test is inferred solely from the filename.

## 17. Change impact

Changing these bytes requires reviewing every consuming validator, source/policy/config hash, generated result or artifact lineage, affected tests, and this companion SHA256. Dependency-lock changes also require `uv lock --check` and `uv pip check`.
