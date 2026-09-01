# `pyproject.toml`

## File identity

- Repository path: `pyproject.toml`
- File type: TOML project configuration
- Layer: project metadata
- Domain: project/tool configuration
- Responsibility: Defines project/dependency/tool configuration and excludes `docs/code/files` from Ruff so byte-exact companion source snapshots are not reformatted.
- Source SHA256: `9e07f6e2aa5c86dfab991f374412101243bacbf1203d1a1c120486893a513148`

## 1. STEP 7F.1A.4 contract delta

- Adds the narrow Ruff exclusion for `docs/code/files` so byte-exact embedded source snapshots are preserved and are validated by the documentation auditor instead of reformatted as Markdown code.

## 2. Purpose and authority

Defines project/dependency/tool configuration and excludes `docs/code/files` from Ruff so byte-exact companion source snapshots are not reformatted.

- Project/tool metadata changes documentation formatting scope only and do not change LandScout evidence or business semantics.

## 3. Source-specific structure

The exact project/tool leaves below are parsed from the current TOML; arrays remain values and are not misclassified as source schemas.

| Qualified TOML key | Runtime type | Exact parsed value |
|---|---|---|
| `project.name` | `str` | `'landscout-ai'` |
| `project.version` | `str` | `'0.1.0'` |
| `project.description` | `str` | `'LandScout AI'` |
| `project.readme` | `str` | `'README.md'` |
| `project.requires-python` | `str` | `'>=3.12,<3.13'` |
| `project.dependencies` | `list` | `['geopandas>=1.1.4', 'pandas>=3.0,<4', 'py7zr>=1.1.3', 'pyarrow>=25.0.1', 'pydantic>=2.13.4', 'pydantic-settings>=2.15.0', 'pyogrio>=0.13.0', 'pypdf>=6.15.0', 'pyproj>=3.7.2', 'pyyaml>=6.0.3', 'shapely>=2.1.2']` |
| `build-system.requires` | `list` | `['uv_build>=0.12.3,<0.13']` |
| `build-system.build-backend` | `str` | `'uv_build'` |
| `tool.uv.build-backend.module-name` | `str` | `'landscout'` |
| `tool.pytest.ini_options.pythonpath` | `list` | `['src']` |
| `tool.pytest.ini_options.testpaths` | `list` | `['tests']` |
| `tool.ruff.target-version` | `str` | `'py312'` |
| `tool.ruff.extend-exclude` | `list` | `['docs/code/files']` |
| `tool.mypy.python_version` | `str` | `'3.12'` |
| `tool.mypy.mypy_path` | `str` | `'src'` |
| `dependency-groups.dev` | `list` | `['mypy>=2.3.0', 'pytest>=9.1.1', 'pytest-cov>=7.1.0', 'ruff>=0.16.2']` |

The STEP-specific formatting boundary is `[tool.ruff].extend-exclude = ["docs/code/files"]`: exact companion source snapshots are audited as bytes/Markdown and are not rewritten by Ruff. All other project/dependency/tool declarations retain their exact current values.

## 4. Side effects and change impact

- This declarative/history file performs no runtime network, filesystem, CRS, geometry, policy, or parcel operation by itself.
- Any byte change invalidates the SHA above and requires updating this companion; project-tool changes also require lock/tool validation where applicable.

## 5. Exact complete current file content

The following UTF-8 snapshot is complete and byte-bound, not an excerpt.

```toml
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
extend-exclude = ["docs/code/files"]

[tool.mypy]
python_version = "3.12"
mypy_path = "src"
```
