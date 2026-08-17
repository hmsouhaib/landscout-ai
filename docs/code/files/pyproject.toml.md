# `pyproject.toml`

## File identity

- Repository path: `pyproject.toml`
- File type: TOML project metadata
- Responsibility: Defines the Python project, runtime and development dependencies, and Ruff/mypy/pytest configuration.
- Source SHA256: `5ff62947716aca6156a4b736e29a5e69b6becc71f97c3ced8e97edb073b82d20`

## 1. Purpose

Defines the Python project, runtime and development dependencies, and Ruff/mypy/pytest configuration.

## 2. Position in LandScout architecture

This is TOML project/tool configuration, consumed by Python packaging/build backend, uv, pytest, Ruff, and mypy.

## 3. Imports and dependencies

Not applicable: this is not Python source.

## 4. Contract taxonomy

Its exact content is reproduced below. No Python alias, frame column, model field, or runtime business semantic is inferred from passive text.

### Structured TOML field inventory

| Exact path | Exact value | Runtime type | Actual consumer/role |
|---|---|---|---|
| `project.name` | `"landscout-ai"` | `str` | Python package/dependency metadata consumed by packaging and uv. |
| `project.version` | `"0.1.0"` | `str` | Python package/dependency metadata consumed by packaging and uv. |
| `project.description` | `"LandScout AI"` | `str` | Python package/dependency metadata consumed by packaging and uv. |
| `project.readme` | `"README.md"` | `str` | Python package/dependency metadata consumed by packaging and uv. |
| `project.requires-python` | `">=3.12,<3.13"` | `str` | Python package/dependency metadata consumed by packaging and uv. |
| `project.dependencies[0]` | `"geopandas>=1.1.4"` | `str` | Python package/dependency metadata consumed by packaging and uv. |
| `project.dependencies[1]` | `"pandas>=3.0,<4"` | `str` | Python package/dependency metadata consumed by packaging and uv. |
| `project.dependencies[2]` | `"py7zr>=1.1.3"` | `str` | Python package/dependency metadata consumed by packaging and uv. |
| `project.dependencies[3]` | `"pyarrow>=25.0.1"` | `str` | Python package/dependency metadata consumed by packaging and uv. |
| `project.dependencies[4]` | `"pydantic>=2.13.4"` | `str` | Python package/dependency metadata consumed by packaging and uv. |
| `project.dependencies[5]` | `"pydantic-settings>=2.15.0"` | `str` | Python package/dependency metadata consumed by packaging and uv. |
| `project.dependencies[6]` | `"pyogrio>=0.13.0"` | `str` | Python package/dependency metadata consumed by packaging and uv. |
| `project.dependencies[7]` | `"pypdf>=6.15.0"` | `str` | Python package/dependency metadata consumed by packaging and uv. |
| `project.dependencies[8]` | `"pyproj>=3.7.2"` | `str` | Python package/dependency metadata consumed by packaging and uv. |
| `project.dependencies[9]` | `"pyyaml>=6.0.3"` | `str` | Python package/dependency metadata consumed by packaging and uv. |
| `project.dependencies[10]` | `"shapely>=2.1.2"` | `str` | Python package/dependency metadata consumed by packaging and uv. |
| `build-system.requires[0]` | `"uv_build>=0.12.3,<0.13"` | `str` | Python build-backend configuration. |
| `build-system.build-backend` | `"uv_build"` | `str` | Python build-backend configuration. |
| `tool.uv.build-backend.module-name` | `"landscout"` | `str` | Python package/dependency metadata consumed by packaging and uv. |
| `tool.pytest.ini_options.pythonpath[0]` | `"src"` | `str` | pytest configuration. |
| `tool.pytest.ini_options.testpaths[0]` | `"tests"` | `str` | pytest configuration. |
| `tool.ruff.target-version` | `"py312"` | `str` | Ruff lint configuration. |
| `tool.mypy.python_version` | `"3.12"` | `str` | mypy static-type configuration. |
| `tool.mypy.mypy_path` | `"src"` | `str` | mypy static-type configuration. |
| `dependency-groups.dev[0]` | `"mypy>=2.3.0"` | `str` | Python package/dependency metadata consumed by packaging and uv. |
| `dependency-groups.dev[1]` | `"pytest>=9.1.1"` | `str` | Python package/dependency metadata consumed by packaging and uv. |
| `dependency-groups.dev[2]` | `"pytest-cov>=7.1.0"` | `str` | Python package/dependency metadata consumed by packaging and uv. |
| `dependency-groups.dev[3]` | `"ruff>=0.16.2"` | `str` | Python package/dependency metadata consumed by packaging and uv. |

````text
[project]
name = "landscout-ai"
version = "0.1.0"
description = "LandScout AI"
readme = "README.md"
requires-python = ">=3.12,<3.13"
dependencies = [
    "geopandas>=1.1.4",
    "pandas>=3.0,<4",
    "py7zr>=1.1.3",
    "pyarrow>=25.0.1",
    "pydantic>=2.13.4",
    "pydantic-settings>=2.15.0",
    "pyogrio>=0.13.0",
    "pypdf>=6.15.0",
    "pyproj>=3.7.2",
    "pyyaml>=6.0.3",
    "shapely>=2.1.2",
]

[build-system]
requires = ["uv_build>=0.12.3,<0.13"]
build-backend = "uv_build"

[tool.uv.build-backend]
module-name = "landscout"

[dependency-groups]
dev = [
    "mypy>=2.3.0",
    "pytest>=9.1.1",
    "pytest-cov>=7.1.0",
    "ruff>=0.16.2",
]

[tool.pytest.ini_options]
pythonpath = ["src"]
testpaths = ["tests"]

[tool.ruff]
target-version = "py312"

[tool.mypy]
python_version = "3.12"
mypy_path = "src"
````

## 5. Classes / models / dataclasses

Not applicable.

## 6. Functions and methods

Not applicable.

## 7. Data contracts

Interpreted only as TOML project/tool configuration by Python packaging/build backend, uv, pytest, Ruff, and mypy; not a Pandas/GeoPandas schema.

## 8. Interfaces

Consumer: Python packaging/build backend, uv, pytest, Ruff, and mypy.

## 9. Error handling

Not applicable to the passive file itself; its consumer reports malformed or unsupported content.

## 10. Side effects

The passive file performs no operation. Reads/resolution belong to its named consumer.

## 11. Security / trust boundaries

The companion SHA binds exact bytes. No source authority is inferred unless a runtime adapter validates it.

## 12. GIS / CRS rules

Not applicable unless an exact configuration field in the reproduced content is consumed by a GIS validator.

## 13. Provenance rules

The path and SHA identify this repository snapshot; passive prose/history is not implementation proof.

## 14. Business meaning

No business decision is executed by this passive file.

## 15. Explicit non-goals

- Does not independently run a source adapter, GIS calculation, policy, score, ranking, or legal decision.

## 16. Tests

Not applicable directly; repository/tool configuration may be exercised by the mandated validation commands.

## 17. Change impact

Review Python packaging/build backend, uv, pytest, Ruff, and mypy, repository workflows, and this companion SHA after any byte change.
