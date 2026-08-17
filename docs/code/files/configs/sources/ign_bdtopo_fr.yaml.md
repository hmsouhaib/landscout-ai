# `configs/sources/ign_bdtopo_fr.yaml`

## File identity

- Repository path: `configs/sources/ign_bdtopo_fr.yaml`
- File type: YAML configuration
- Primary responsibility: Pins the IGN BD TOPO D031 archive identity, checksum/size, cache, logical layers, access, and coverage selection.
- Layer / domain: `checked-in configuration` / `grid`
- Public or internal role: Repository artifact; not a Python public API.
- Source SHA256: `fa3cc4e82f7c5a2a917a60508fdba6de37f0bde07d7da6b27f2cd00124e44a86`

## 1. Purpose

Pins the IGN BD TOPO D031 archive identity, checksum/size, cache, logical layers, access, and coverage selection.

## 2. Position in LandScout architecture

This `checked-in configuration` artifact supplies exact checked-in bytes to the current repository. Consumers found by exact path reference are: `docs/DEV_LOG.md`, `src/landscout/sources/ign_bdtopo_fr.py`, `tests/unit/test_ign_bdtopo_fr.py`.

## 3. Imports and dependencies

Not a Python module. Its consumers parse or interpret the bytes using the source/configuration functions identified by repository references and pipeline documentation.

## 4. Constants and domains

Every parsed leaf field is listed below; list indices preserve source order.

| Field path | Exact checked-in value | Contract role |
|---|---|---|
| `provider` | `"Institut national de l'information géographique et forestière (IGN)"` (`str`) | Names the configured source provider copied/compared as lineage. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/ign_bdtopo_fr.py`, `tests/unit/test_ign_bdtopo_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `product` | `"BD TOPO"` (`str`) | Configures `product` under the exact parent path `<root>`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/ign_bdtopo_fr.py`, `tests/unit/test_ign_bdtopo_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `department_code` | `"31"` (`str`) | Configures `department code` under the exact parent path `<root>`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/ign_bdtopo_fr.py`, `tests/unit/test_ign_bdtopo_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `edition` | `"2026-06-15"` (`str`) | Configures `edition` under the exact parent path `<root>`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/ign_bdtopo_fr.py`, `tests/unit/test_ign_bdtopo_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `product_version` | `"3.5"` (`str`) | Configures `product version` under the exact parent path `<root>`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/ign_bdtopo_fr.py`, `tests/unit/test_ign_bdtopo_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `projection` | `"EPSG:2154"` (`str`) | Configures `projection` under the exact parent path `<root>`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/ign_bdtopo_fr.py`, `tests/unit/test_ign_bdtopo_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `format` | `"GPKG"` (`str`) | Configures `format` under the exact parent path `<root>`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/ign_bdtopo_fr.py`, `tests/unit/test_ign_bdtopo_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `archive_format` | `"7z"` (`str`) | Configures `archive format` under the exact parent path `<root>`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/ign_bdtopo_fr.py`, `tests/unit/test_ign_bdtopo_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `source_url` | `"https://data.geopf.fr/telechargement/download/BDTOPO/BDTOPO_3-5_TOUSTHEMES_GPKG_LAMB93_D031_2026-06-15/BDTOPO_3-5_TOUSTHEMES_GPKG_LAMB93_D031_2026-06-15.7z"` (`str`) | Configures the exact source url; HTTPS/origin/path validation is defined by the consuming model. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/ign_bdtopo_fr.py`, `tests/unit/test_ign_bdtopo_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `checksum_url` | `null` (`NoneType`) | Configures the exact checksum url; HTTPS/origin/path validation is defined by the consuming model. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/ign_bdtopo_fr.py`, `tests/unit/test_ign_bdtopo_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `official_checksum_algorithm` | `"md5"` (`str`) | Configures `official checksum algorithm` under the exact parent path `<root>`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/ign_bdtopo_fr.py`, `tests/unit/test_ign_bdtopo_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `official_checksum` | `"24d4a50b7eae3c0d55bb55ffd5b525a6"` (`str`) | Configures `official checksum` under the exact parent path `<root>`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/ign_bdtopo_fr.py`, `tests/unit/test_ign_bdtopo_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `expected_archive_size_bytes` | `494818677` (`int`) | Pins the exact approved archive byte length. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/ign_bdtopo_fr.py`, `tests/unit/test_ign_bdtopo_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `cache_max_age_hours` | `168` (`int`) | Configures `cache max age hours` under the exact parent path `<root>`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/ign_bdtopo_fr.py`, `tests/unit/test_ign_bdtopo_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `logical_layers.electric_lines.class_label` | `"Ligne électrique"` (`str`) | Configures `class label` under the exact parent path `logical_layers.electric_lines`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/ign_bdtopo_fr.py`, `tests/unit/test_ign_bdtopo_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `logical_layers.electric_lines.match_tokens[0]` | `"ligne"` (`str`) | Ordered configured member of `logical_layers.electric_lines.match_tokens`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/ign_bdtopo_fr.py`, `tests/unit/test_ign_bdtopo_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `logical_layers.electric_lines.match_tokens[1]` | `"électrique"` (`str`) | Ordered configured member of `logical_layers.electric_lines.match_tokens`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/ign_bdtopo_fr.py`, `tests/unit/test_ign_bdtopo_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `logical_layers.transformation_posts.class_label` | `"Poste de transformation"` (`str`) | Configures `class label` under the exact parent path `logical_layers.transformation_posts`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/ign_bdtopo_fr.py`, `tests/unit/test_ign_bdtopo_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `logical_layers.transformation_posts.match_tokens[0]` | `"poste"` (`str`) | Ordered configured member of `logical_layers.transformation_posts.match_tokens`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/ign_bdtopo_fr.py`, `tests/unit/test_ign_bdtopo_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `logical_layers.transformation_posts.match_tokens[1]` | `"transformation"` (`str`) | Ordered configured member of `logical_layers.transformation_posts.match_tokens`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/ign_bdtopo_fr.py`, `tests/unit/test_ign_bdtopo_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `access.road_segments.class_label` | `"Tronçon de route"` (`str`) | Configures `class label` under the exact parent path `access.road_segments`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/ign_bdtopo_fr.py`, `tests/unit/test_ign_bdtopo_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `access.road_segments.match_tokens[0]` | `"tronçon"` (`str`) | Ordered configured member of `access.road_segments.match_tokens`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/ign_bdtopo_fr.py`, `tests/unit/test_ign_bdtopo_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `access.road_segments.match_tokens[1]` | `"route"` (`str`) | Ordered configured member of `access.road_segments.match_tokens`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/ign_bdtopo_fr.py`, `tests/unit/test_ign_bdtopo_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `coverage.department_layer.class_label` | `"Département"` (`str`) | Configures `class label` under the exact parent path `coverage.department_layer`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/ign_bdtopo_fr.py`, `tests/unit/test_ign_bdtopo_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `coverage.department_layer.match_tokens[0]` | `"departement"` (`str`) | Ordered configured member of `coverage.department_layer.match_tokens`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/ign_bdtopo_fr.py`, `tests/unit/test_ign_bdtopo_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `coverage.department_layer.department_code_field` | `"code_insee"` (`str`) | Configures `department code field` under the exact parent path `coverage.department_layer`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/ign_bdtopo_fr.py`, `tests/unit/test_ign_bdtopo_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |

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
