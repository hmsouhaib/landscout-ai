import json
import os
import subprocess
import sys
from pathlib import Path

import pytest
from test_cadastre_screening import write_project

PROJECT = Path(__file__).resolve().parents[2]


def _cli(root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    environment = {
        **os.environ,
        "PYTHONPATH": str(PROJECT / "src"),
        "PYTHONDONTWRITEBYTECODE": "1",
    }
    return subprocess.run(
        [sys.executable, "-B", "-X", "utf8", "-m", "landscout", *args],
        cwd=root,
        env=environment,
        capture_output=True,
        text=True,
        encoding="utf-8",
        timeout=60,
        check=False,
    )


@pytest.mark.parametrize("args", [("--help",), ("scan", "--help")])
def test_help_has_no_run_or_file_write(tmp_path: Path, args: tuple[str, ...]) -> None:
    result = _cli(tmp_path, *args)
    assert result.returncode == 0 and "usage:" in result.stdout
    assert not list(tmp_path.iterdir())


@pytest.mark.parametrize("mode", [[], ["--offline"]])
def test_cli_subprocess_runs_physical_synthetic_offline_cache(
    tmp_path: Path, mode: list[str]
) -> None:
    scan, _, _ = write_project(tmp_path)
    result = _cli(
        tmp_path, "scan", "--scan", str(scan), "--output", "outputs/cli", *mode
    )
    assert result.returncode == 0, result.stderr
    assert "RETAINED_BY_EXECUTED_FILTERS: 2/8" in result.stdout
    manifest = json.loads((tmp_path / "outputs/cli/run.json").read_bytes())
    assert (
        manifest["allow_download"] is False and manifest["source"]["cache_hit"] is True
    )
    again = _cli(
        tmp_path, "scan", "--scan", str(scan), "--output", "outputs/cli", *mode
    )
    assert again.returncode == 1 and "already exists" in again.stderr


def test_cli_offline_miss_is_controlled_without_creating_cache_or_output(
    tmp_path: Path,
) -> None:
    scan, _, _ = write_project(tmp_path)
    result = _cli(
        tmp_path,
        "scan",
        "--scan",
        str(scan),
        "--cache-dir",
        "absent-cache",
        "--output",
        "outputs/fail",
    )
    assert result.returncode == 1 and "Offline cadastre cache" in result.stderr
    assert (
        not (tmp_path / "absent-cache").exists() and not (tmp_path / "outputs").exists()
    )


@pytest.mark.parametrize(
    "args",
    [
        [],
        ["scan"],
        ["bogus"],
        ["scan", "--scan", "x", "--offline", "--allow-download"],
        ["scan", "--scan", "x", "--max-cache-age-hours", "text"],
    ],
)
def test_cli_usage_errors_return_two(tmp_path: Path, args: list[str]) -> None:
    result = _cli(tmp_path, *args)
    assert result.returncode == 2 and "usage:" in result.stderr
    assert not list(tmp_path.iterdir())
