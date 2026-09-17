# `tests/unit/test_package.py`

## File identity

- Repository path: `tests/unit/test_package.py`
- Responsibility: Package version regression.
- Source SHA256: `217cdd39bf3105ba5d546c822ba2a3d8a13344abf91812f408cec981eb6d8057`
- Source SHA256 basis: `git-content`

## test_package_import_and_version

Signature: `def test_package_import_and_version() -> None:`. Pytest discovers one unparametrized test; there are no fixtures, helper classes, mocks or expected-exception contexts in this file.

The test first reads `pyproject.toml` relative to the process working directory as UTF-8, parses TOML through `tomllib.loads`, selects `[project]`, then asserts `landscout.__version__ == project["version"]`. Successful completion returns `None`. Missing/unreadable files, malformed TOML, a missing `project`/`version` key or failed equality propagate their normal Python/parser/assertion errors; no adapter error translation is involved.

It proves package import and matching version metadata, **not package exports**. Export contracts are tested in their respective source/stage suites. It reads a real local TOML file and imports only the minimal root package; there is no network, geometry, artifact publication or hash assertion.

## Exact complete current file content

The fenced UTF-8 content below equals the Git-stored file bytes.

````python
from pathlib import Path
from tomllib import loads

import landscout


def test_package_import_and_version() -> None:
    project = loads(Path("pyproject.toml").read_text(encoding="utf-8"))["project"]
    assert landscout.__version__ == project["version"]
````
