from pathlib import Path
from tomllib import loads

import landscout


def test_package_import_and_version() -> None:
    project = loads(Path("pyproject.toml").read_text(encoding="utf-8"))["project"]
    assert landscout.__version__ == project["version"]
