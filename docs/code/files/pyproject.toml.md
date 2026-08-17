# `pyproject.toml`

## File identity

- Repository path: `pyproject.toml`
- File type: TOML project metadata
- Primary responsibility: Defines the Python project, runtime and development dependencies, and Ruff/mypy/pytest configuration.
- Layer / domain: `project metadata` / `project`
- Public or internal role: Repository artifact; not a Python public API.
- Source SHA256: `5ff62947716aca6156a4b736e29a5e69b6becc71f97c3ced8e97edb073b82d20`

## 1. Purpose

Defines the Python project, runtime and development dependencies, and Ruff/mypy/pytest configuration.

## 2. Position in LandScout architecture

This `project metadata` artifact supplies exact checked-in bytes to the current repository. Consumers found by exact path reference are: `docs/DEV_LOG.md`, `tests/unit/test_bess_planning_feature_policy.py`.

## 3. Imports and dependencies

Not a Python module. Its consumers parse or interpret the bytes using the source/configuration functions identified by repository references and pipeline documentation.

## 4. Constants and domains

Every parsed leaf field is listed below; list indices preserve source order.

| Field path | Exact checked-in value | Contract role |
|---|---|---|
| `project.name` | `"landscout-ai"` (`str`) | Configures `name` under the exact parent path `project`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `tests/unit/test_bess_planning_feature_policy.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `project.version` | `"0.1.0"` (`str`) | Configures `version` under the exact parent path `project`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `tests/unit/test_bess_planning_feature_policy.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `project.description` | `"LandScout AI"` (`str`) | Configures `description` under the exact parent path `project`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `tests/unit/test_bess_planning_feature_policy.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `project.readme` | `"README.md"` (`str`) | Configures `readme` under the exact parent path `project`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `tests/unit/test_bess_planning_feature_policy.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `project.requires-python` | `">=3.12,<3.13"` (`str`) | Configures `requires-python` under the exact parent path `project`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `tests/unit/test_bess_planning_feature_policy.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `project.dependencies[0]` | `"geopandas>=1.1.4"` (`str`) | Ordered configured member of `project.dependencies`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `tests/unit/test_bess_planning_feature_policy.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `project.dependencies[1]` | `"pandas>=3.0,<4"` (`str`) | Ordered configured member of `project.dependencies`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `tests/unit/test_bess_planning_feature_policy.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `project.dependencies[2]` | `"py7zr>=1.1.3"` (`str`) | Ordered configured member of `project.dependencies`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `tests/unit/test_bess_planning_feature_policy.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `project.dependencies[3]` | `"pyarrow>=25.0.1"` (`str`) | Ordered configured member of `project.dependencies`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `tests/unit/test_bess_planning_feature_policy.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `project.dependencies[4]` | `"pydantic>=2.13.4"` (`str`) | Ordered configured member of `project.dependencies`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `tests/unit/test_bess_planning_feature_policy.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `project.dependencies[5]` | `"pydantic-settings>=2.15.0"` (`str`) | Ordered configured member of `project.dependencies`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `tests/unit/test_bess_planning_feature_policy.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `project.dependencies[6]` | `"pyogrio>=0.13.0"` (`str`) | Ordered configured member of `project.dependencies`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `tests/unit/test_bess_planning_feature_policy.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `project.dependencies[7]` | `"pypdf>=6.15.0"` (`str`) | Ordered configured member of `project.dependencies`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `tests/unit/test_bess_planning_feature_policy.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `project.dependencies[8]` | `"pyproj>=3.7.2"` (`str`) | Ordered configured member of `project.dependencies`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `tests/unit/test_bess_planning_feature_policy.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `project.dependencies[9]` | `"pyyaml>=6.0.3"` (`str`) | Ordered configured member of `project.dependencies`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `tests/unit/test_bess_planning_feature_policy.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `project.dependencies[10]` | `"shapely>=2.1.2"` (`str`) | Ordered configured member of `project.dependencies`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `tests/unit/test_bess_planning_feature_policy.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `build-system.requires[0]` | `"uv_build>=0.12.3,<0.13"` (`str`) | Ordered configured member of `build-system.requires`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `tests/unit/test_bess_planning_feature_policy.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `build-system.build-backend` | `"uv_build"` (`str`) | Configures `build-backend` under the exact parent path `build-system`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `tests/unit/test_bess_planning_feature_policy.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `tool.uv.build-backend.module-name` | `"landscout"` (`str`) | Configures `module-name` under the exact parent path `tool.uv.build-backend`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `tests/unit/test_bess_planning_feature_policy.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `tool.pytest.ini_options.pythonpath[0]` | `"src"` (`str`) | Ordered configured member of `tool.pytest.ini_options.pythonpath`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `tests/unit/test_bess_planning_feature_policy.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `tool.pytest.ini_options.testpaths[0]` | `"tests"` (`str`) | Ordered configured member of `tool.pytest.ini_options.testpaths`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `tests/unit/test_bess_planning_feature_policy.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `tool.ruff.target-version` | `"py312"` (`str`) | Configures `target-version` under the exact parent path `tool.ruff`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `tests/unit/test_bess_planning_feature_policy.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `tool.mypy.python_version` | `"3.12"` (`str`) | Configures `python version` under the exact parent path `tool.mypy`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `tests/unit/test_bess_planning_feature_policy.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `tool.mypy.mypy_path` | `"src"` (`str`) | Configures `mypy path` under the exact parent path `tool.mypy`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `tests/unit/test_bess_planning_feature_policy.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `dependency-groups.dev[0]` | `"mypy>=2.3.0"` (`str`) | Ordered configured member of `dependency-groups.dev`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `tests/unit/test_bess_planning_feature_policy.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `dependency-groups.dev[1]` | `"pytest>=9.1.1"` (`str`) | Ordered configured member of `dependency-groups.dev`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `tests/unit/test_bess_planning_feature_policy.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `dependency-groups.dev[2]` | `"pytest-cov>=7.1.0"` (`str`) | Ordered configured member of `dependency-groups.dev`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `tests/unit/test_bess_planning_feature_policy.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `dependency-groups.dev[3]` | `"ruff>=0.16.2"` (`str`) | Ordered configured member of `dependency-groups.dev`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`, `tests/unit/test_bess_planning_feature_policy.py`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |

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
