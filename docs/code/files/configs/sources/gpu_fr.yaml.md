# `configs/sources/gpu_fr.yaml`

## File identity

- Repository path: `configs/sources/gpu_fr.yaml`
- File type: YAML configuration
- Primary responsibility: Pins the official GPU API/cache/pilot identity and logical spatial-layer discovery rules.
- Layer / domain: `checked-in configuration` / `planning`
- Public or internal role: Repository artifact; not a Python public API.
- Source SHA256: `f069bf398c752380ca58c90504aa34c322376d52422fd237805e67f2f7829066`

## 1. Purpose

Pins the official GPU API/cache/pilot identity and logical spatial-layer discovery rules.

## 2. Position in LandScout architecture

This `checked-in configuration` artifact supplies exact checked-in bytes to the current repository. Consumers found by exact path reference are: `docs/DEV_LOG.md`, `src/landscout/sources/gpu_fr.py`, `tests/unit/test_gpu_fr.py`.

## 3. Imports and dependencies

Not a Python module. Its consumers parse or interpret the bytes using the source/configuration functions identified by repository references and pipeline documentation.

## 4. Constants and domains

Every parsed leaf field is listed below; list indices preserve source order.

| Field path | Exact checked-in value | Contract role |
|---|---|---|
| `provider` | `"Géoportail de l'Urbanisme"` (`str`) | Names the configured source provider copied/compared as lineage. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/gpu_fr.py`, `tests/unit/test_gpu_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `portal` | `"Géoportail de l'Urbanisme"` (`str`) | Configures `portal` under the exact parent path `<root>`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/gpu_fr.py`, `tests/unit/test_gpu_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `country` | `"FR"` (`str`) | Configures `country` under the exact parent path `<root>`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/gpu_fr.py`, `tests/unit/test_gpu_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `api.base_url` | `"https://www.geoportail-urbanisme.gouv.fr/api"` (`str`) | Pins the exact official HTTPS API origin/path used to build requests. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/gpu_fr.py`, `tests/unit/test_gpu_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `download.strategy` | `"partition"` (`str`) | Configures `strategy` under the exact parent path `download`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/gpu_fr.py`, `tests/unit/test_gpu_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `download.partition_template` | `"DU_{code_insee}"` (`str`) | Configures `partition template` under the exact parent path `download`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/gpu_fr.py`, `tests/unit/test_gpu_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `cache.max_age_hours` | `168` (`int`) | Configures `max age hours` under the exact parent path `cache`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/gpu_fr.py`, `tests/unit/test_gpu_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `pilot.commune_code` | `"31395"` (`str`) | Configures `commune code` under the exact parent path `pilot`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/gpu_fr.py`, `tests/unit/test_gpu_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `spatial_layers.zoning.class_label` | `"Zone urba"` (`str`) | Configures `class label` under the exact parent path `spatial_layers.zoning`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/gpu_fr.py`, `tests/unit/test_gpu_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `spatial_layers.zoning.match_tokens[0]` | `"zone_urba"` (`str`) | Ordered configured member of `spatial_layers.zoning.match_tokens`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/gpu_fr.py`, `tests/unit/test_gpu_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `spatial_layers.prescription_surface.class_label` | `"Prescription surfacique"` (`str`) | Configures `class label` under the exact parent path `spatial_layers.prescription_surface`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/gpu_fr.py`, `tests/unit/test_gpu_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `spatial_layers.prescription_surface.match_tokens[0]` | `"prescription_surf"` (`str`) | Ordered configured member of `spatial_layers.prescription_surface.match_tokens`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/gpu_fr.py`, `tests/unit/test_gpu_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `spatial_layers.prescription_line.class_label` | `"Prescription linéaire"` (`str`) | Configures `class label` under the exact parent path `spatial_layers.prescription_line`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/gpu_fr.py`, `tests/unit/test_gpu_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `spatial_layers.prescription_line.match_tokens[0]` | `"prescription_lin"` (`str`) | Ordered configured member of `spatial_layers.prescription_line.match_tokens`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/gpu_fr.py`, `tests/unit/test_gpu_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `spatial_layers.prescription_point.class_label` | `"Prescription ponctuelle"` (`str`) | Configures `class label` under the exact parent path `spatial_layers.prescription_point`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/gpu_fr.py`, `tests/unit/test_gpu_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `spatial_layers.prescription_point.match_tokens[0]` | `"prescription_pct"` (`str`) | Ordered configured member of `spatial_layers.prescription_point.match_tokens`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/gpu_fr.py`, `tests/unit/test_gpu_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `spatial_layers.information_surface.class_label` | `"Information surfacique"` (`str`) | Configures `class label` under the exact parent path `spatial_layers.information_surface`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/gpu_fr.py`, `tests/unit/test_gpu_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `spatial_layers.information_surface.match_tokens[0]` | `"info_surf"` (`str`) | Ordered configured member of `spatial_layers.information_surface.match_tokens`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/gpu_fr.py`, `tests/unit/test_gpu_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `spatial_layers.information_line.class_label` | `"Information linéaire"` (`str`) | Configures `class label` under the exact parent path `spatial_layers.information_line`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/gpu_fr.py`, `tests/unit/test_gpu_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `spatial_layers.information_line.match_tokens[0]` | `"info_lin"` (`str`) | Ordered configured member of `spatial_layers.information_line.match_tokens`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/gpu_fr.py`, `tests/unit/test_gpu_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `spatial_layers.information_point.class_label` | `"Information ponctuelle"` (`str`) | Configures `class label` under the exact parent path `spatial_layers.information_point`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/gpu_fr.py`, `tests/unit/test_gpu_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `spatial_layers.information_point.match_tokens[0]` | `"info_pct"` (`str`) | Ordered configured member of `spatial_layers.information_point.match_tokens`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `src/landscout/sources/gpu_fr.py`, `tests/unit/test_gpu_fr.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |

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

This file supports the `planning` domain only through its exact checked-in values and current consumers.

## 15. Explicit non-goals

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

## 16. Tests

Tests that load or mention this path are documented in their companion files. No test is inferred solely from the filename.

## 17. Change impact

Changing these bytes requires reviewing every consuming validator, source/policy/config hash, generated result or artifact lineage, affected tests, and this companion SHA256. Dependency-lock changes also require `uv lock --check` and `uv pip check`.
