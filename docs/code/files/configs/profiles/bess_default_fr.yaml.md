# `configs/profiles/bess_default_fr.yaml`

## File identity

- Repository path: `configs/profiles/bess_default_fr.yaml`
- File type: YAML configuration
- Primary responsibility: Defines the default French BESS parcel-area and shape-screening profile consumed by scan configuration.
- Layer / domain: `checked-in configuration` / `project`
- Public or internal role: Repository artifact; not a Python public API.
- Source SHA256: `5126d21c94cc399f9318f988b6ba9b7a07d24006e542861e167c08c9ace39684`

## 1. Purpose

Defines the default French BESS parcel-area and shape-screening profile consumed by scan configuration.

## 2. Position in LandScout architecture

This `checked-in configuration` artifact supplies exact checked-in bytes to the current repository. Consumers found by exact path reference are: `configs/scans/bess_muret.yaml`, `docs/DEV_LOG.md`, `tests/unit/test_config.py`.

## 3. Imports and dependencies

Not a Python module. Its consumers parse or interpret the bytes using the source/configuration functions identified by repository references and pipeline documentation.

## 4. Constants and domains

Every parsed leaf field is listed below; list indices preserve source order.

| Field path | Exact checked-in value | Contract role |
|---|---|---|
| `country` | `"FR"` (`str`) | Configures `country` under the exact parent path `<root>`. Consumers found by exact repository path reference: `configs/scans/bess_muret.yaml`, `docs/DEV_LOG.md`, `tests/unit/test_config.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `technology` | `"BESS"` (`str`) | Configures `technology` under the exact parent path `<root>`. Consumers found by exact repository path reference: `configs/scans/bess_muret.yaml`, `docs/DEV_LOG.md`, `tests/unit/test_config.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `parcel.min_area_m2` | `2000` (`int`) | Configures min area m2 in square metres. Consumers found by exact repository path reference: `configs/scans/bess_muret.yaml`, `docs/DEV_LOG.md`, `tests/unit/test_config.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `parcel.max_area_m2` | `15000` (`int`) | Configures max area m2 in square metres. Consumers found by exact repository path reference: `configs/scans/bess_muret.yaml`, `docs/DEV_LOG.md`, `tests/unit/test_config.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `shape_screening.enabled` | `true` (`bool`) | Enables/disables the exact enabled behavior; Boolean coercion rules belong to the consuming model. Consumers found by exact repository path reference: `configs/scans/bess_muret.yaml`, `docs/DEV_LOG.md`, `tests/unit/test_config.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `shape_screening.min_width_m` | `15` (`int`) | Configures min width m in metres. Consumers found by exact repository path reference: `configs/scans/bess_muret.yaml`, `docs/DEV_LOG.md`, `tests/unit/test_config.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `shape_screening.max_length_width_ratio` | `10` (`int`) | Configures `max length width ratio` under the exact parent path `shape_screening`. Consumers found by exact repository path reference: `configs/scans/bess_muret.yaml`, `docs/DEV_LOG.md`, `tests/unit/test_config.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `shape_screening.calibration.policy_version` | `"muret_empirical_v1"` (`str`) | Configures `policy version` under the exact parent path `shape_screening.calibration`. Consumers found by exact repository path reference: `configs/scans/bess_muret.yaml`, `docs/DEV_LOG.md`, `tests/unit/test_config.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `shape_screening.calibration.method` | `"empirical_distribution"` (`str`) | Configures `method` under the exact parent path `shape_screening.calibration`. Consumers found by exact repository path reference: `configs/scans/bess_muret.yaml`, `docs/DEV_LOG.md`, `tests/unit/test_config.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `shape_screening.calibration.calibration_scope` | `"Muret 31395"` (`str`) | Configures `calibration scope` under the exact parent path `shape_screening.calibration`. Consumers found by exact repository path reference: `configs/scans/bess_muret.yaml`, `docs/DEV_LOG.md`, `tests/unit/test_config.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `shape_screening.calibration.sample_size` | `4013` (`int`) | Configures `sample size` under the exact parent path `shape_screening.calibration`. Consumers found by exact repository path reference: `configs/scans/bess_muret.yaml`, `docs/DEV_LOG.md`, `tests/unit/test_config.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `shape_screening.calibration.calibrated_at` | `"2026-08-11"` (`str`) | Configures `calibrated at` under the exact parent path `shape_screening.calibration`. Consumers found by exact repository path reference: `configs/scans/bess_muret.yaml`, `docs/DEV_LOG.md`, `tests/unit/test_config.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `shape_screening.calibration.target_retention_pct` | `90` (`int`) | Configures target retention pct as a percentage. Consumers found by exact repository path reference: `configs/scans/bess_muret.yaml`, `docs/DEV_LOG.md`, `tests/unit/test_config.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `shape_screening.calibration.observed_retention_pct` | `90.65537` (`float`) | Configures observed retention pct as a percentage. Consumers found by exact repository path reference: `configs/scans/bess_muret.yaml`, `docs/DEV_LOG.md`, `tests/unit/test_config.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `crs.storage` | `"EPSG:4326"` (`str`) | Configures `storage` under the exact parent path `crs`. Consumers found by exact repository path reference: `configs/scans/bess_muret.yaml`, `docs/DEV_LOG.md`, `tests/unit/test_config.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `crs.calculation` | `"EPSG:2154"` (`str`) | Configures `calculation` under the exact parent path `crs`. Consumers found by exact repository path reference: `configs/scans/bess_muret.yaml`, `docs/DEV_LOG.md`, `tests/unit/test_config.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |

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

This file supports the `project` domain only through its exact checked-in values and current consumers.

## 15. Explicit non-goals

- This project file does not implement a business algorithm.

## 16. Tests

Tests that load or mention this path are documented in their companion files. No test is inferred solely from the filename.

## 17. Change impact

Changing these bytes requires reviewing every consuming validator, source/policy/config hash, generated result or artifact lineage, affected tests, and this companion SHA256. Dependency-lock changes also require `uv lock --check` and `uv pip check`.
