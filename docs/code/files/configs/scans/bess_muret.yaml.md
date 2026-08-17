# `configs/scans/bess_muret.yaml`

## File identity

- Repository path: `configs/scans/bess_muret.yaml`
- File type: YAML configuration
- Primary responsibility: Defines the Muret scan identity, AOI, profile reference, and output root.
- Layer / domain: `checked-in configuration` / `project`
- Public or internal role: Repository artifact; not a Python public API.
- Source SHA256: `6da68dfa5442b7b856687d5c9d5b0db10a2a2f799a2d7b8b35342573d54c65ba`

## 1. Purpose

Defines the Muret scan identity, AOI, profile reference, and output root.

## 2. Position in LandScout architecture

This `checked-in configuration` artifact supplies exact checked-in bytes to the current repository. Consumers found by exact path reference are: `docs/DEV_LOG.md`, `tests/unit/test_config.py`.

## 3. Imports and dependencies

Not a Python module. Its consumers parse or interpret the bytes using the source/configuration functions identified by repository references and pipeline documentation.

## 4. Constants and domains

Every parsed leaf field is listed below; list indices preserve source order.

| Field path | Exact checked-in value | Contract role |
|---|---|---|
| `scan.name` | `"bess_muret"` (`str`) | Configures `name` under the exact parent path `scan`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `tests/unit/test_config.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `scan.country` | `"FR"` (`str`) | Configures `country` under the exact parent path `scan`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `tests/unit/test_config.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `scan.technology` | `"BESS"` (`str`) | Configures `technology` under the exact parent path `scan`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `tests/unit/test_config.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `aoi.commune_codes[0]` | `"31395"` (`str`) | Ordered configured member of `aoi.commune_codes`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `tests/unit/test_config.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `profile.path` | `"configs/profiles/bess_default_fr.yaml"` (`str`) | Configures `path` under the exact parent path `profile`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `tests/unit/test_config.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `output.directory` | `"outputs"` (`str`) | Configures `directory` under the exact parent path `output`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `tests/unit/test_config.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |

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
