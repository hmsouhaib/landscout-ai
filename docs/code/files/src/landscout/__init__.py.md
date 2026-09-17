# `src/landscout/__init__.py`

## File identity

- Repository path: `src/landscout/__init__.py`
- Responsibility: Package version.
- Source SHA256: `91447944015cec709e8aa7655f7e9d64e1e4508e7023a57fe3746911c0fc6fed`
- Source SHA256 basis: `git-content`

The package initializer assigns only `__version__ = "0.1.0"`. It imports no module and defines no model, function, export list or pipeline entry point. The variable is ordinary module metadata, not a deeply immutable trust object or an approval status.

`tests/unit/test_package.py::test_package_import_and_version` imports `landscout`, reads the repository-root `pyproject.toml` as UTF-8 with `tomllib.loads`, and compares this value with `project.version`. Updating either version requires reviewing both values and that single assertion. No source/network/GIS behavior is exercised by this initializer.

## Exact complete current file content

The fenced UTF-8 content below equals the Git-stored file bytes.

````python
__version__ = "0.1.0"
````
