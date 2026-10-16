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
        "PYTHONPATH": os.pathsep.join((str(root), str(PROJECT / "src"))),
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


def _forbid_child_network(root: Path) -> None:
    # Subprocess isolation: fail before even DNS, and leave observable evidence.
    (root / "sitecustomize.py").write_text(
        "import socket\nfrom pathlib import Path\n"
        f"_attempt = Path({str(root / 'network-attempt.txt')!r})\n"
        "def deny(*args, **kwargs):\n"
        "    _attempt.write_text('unexpected network boundary', encoding='utf-8')\n"
        "    raise AssertionError('network forbidden in synthetic CLI')\n"
        "socket.getaddrinfo = deny\nsocket.create_connection = deny\n"
        "socket.socket.connect = deny\nsocket.socket.connect_ex = deny\n",
        encoding="utf-8",
    )


def test_grid_cli_subprocess_uses_only_verified_synthetic_local_sources(tmp_path):
    from test_grid_screening import write_grid_project

    scan, _, _, _ = write_grid_project(tmp_path)
    _forbid_child_network(tmp_path)
    result = _cli(
        tmp_path,
        "scan",
        "--scan",
        str(scan),
        "--with-grid",
        "--offline",
        "--output",
        "outputs/cli-grid",
    )
    assert result.returncode == 0, result.stderr
    manifest = json.loads((tmp_path / "outputs/cli-grid/run.json").read_bytes())
    assert manifest["schema_version"] == 2 and manifest["grid"]["status"] == "COMPLETE"
    assert manifest["counts"]["retained"] == 2
    assert not (tmp_path / "network-attempt.txt").exists()


@pytest.mark.parametrize("failure", ["archive", "extraction", "department"])
def test_grid_cli_source_failures_are_controlled_and_offline(tmp_path, failure):
    import yaml
    from test_grid_screening import write_grid_project

    scan, config, _, _ = write_grid_project(tmp_path)
    extra = []
    if failure == "archive":
        extra = ["--ign-cache-dir", "missing-cache"]
    elif failure == "extraction":
        extra = ["--ign-extraction-dir", "missing-extraction"]
    else:
        values = yaml.safe_load(config.read_bytes())
        values["department_code"] = "32"
        config.write_text(yaml.safe_dump(values), encoding="utf-8")
    _forbid_child_network(tmp_path)
    result = _cli(
        tmp_path,
        "scan",
        "--scan",
        str(scan),
        "--with-grid",
        "--output",
        "outputs/failed-grid",
        *extra,
    )
    assert result.returncode == 1 and "Cadastre screening failed:" in result.stderr
    assert not (tmp_path / "outputs/failed-grid/run.json").exists()
    assert not (tmp_path / "network-attempt.txt").exists()
    assert not (tmp_path / "missing-cache").exists()
    assert not (tmp_path / "missing-extraction").exists()


@pytest.mark.parametrize(
    "flag", ["--ign-config", "--ign-cache-dir", "--ign-extraction-dir"]
)
def test_ign_cli_options_require_grid_usage_flag(tmp_path, flag):
    result = _cli(tmp_path, "scan", "--scan", "unused", flag, "unused")
    assert result.returncode == 2 and "require --with-grid" in result.stderr
    assert not list(tmp_path.iterdir())


@pytest.mark.parametrize("with_grid", [False, True])
@pytest.mark.parametrize("permission", ["--offline", "--allow-download"])
def test_road_cli_subprocess_complete_from_verified_local_sources(
    tmp_path, with_grid, permission
):
    from test_road_screening import write_road_project

    scan, _, _, _, policy = write_road_project(tmp_path)
    _forbid_child_network(tmp_path)
    result = _cli(
        tmp_path,
        "scan",
        "--scan",
        str(scan),
        "--with-roads",
        permission,
        "--road-policy",
        str(policy),
        "--output",
        "outputs/roads",
        *(["--with-grid"] if with_grid else []),
    )
    assert result.returncode == 0, result.stderr
    manifest = json.loads((tmp_path / "outputs/roads/run.json").read_bytes())
    assert manifest["schema_version"] == 3 and manifest["roads"]["status"] == "COMPLETE"
    assert manifest["counts"]["retained"] == 2
    assert manifest["roads"]["policy"]["heavy_vehicle_access"] == "NOT_PROVEN"
    assert not (tmp_path / "network-attempt.txt").exists()


@pytest.mark.parametrize("failure", ["archive", "extraction", "policy", "department"])
@pytest.mark.parametrize("with_grid", [False, True])
def test_road_cli_source_failures_are_controlled_before_network(
    tmp_path, failure, with_grid
):
    import yaml
    from test_road_screening import write_road_project

    scan, config, _, _, _ = write_road_project(tmp_path)
    extra = []
    if failure == "archive":
        extra = ["--ign-cache-dir", "missing-cache"]
    elif failure == "extraction":
        extra = ["--ign-extraction-dir", "missing-extraction"]
    elif failure == "policy":
        extra = ["--road-policy", "missing-policy"]
    else:
        values = yaml.safe_load(config.read_bytes())
        values["department_code"] = "32"
        config.write_text(yaml.safe_dump(values), encoding="utf-8")
    _forbid_child_network(tmp_path)
    result = _cli(
        tmp_path,
        "scan",
        "--scan",
        str(scan),
        "--with-roads",
        "--output",
        "outputs/fail",
        *(["--with-grid"] if with_grid else []),
        *extra,
    )
    assert result.returncode == 1 and "Cadastre screening failed:" in result.stderr
    assert not (tmp_path / "outputs/fail/run.json").exists()
    assert not (tmp_path / "network-attempt.txt").exists()
    assert (
        not (tmp_path / "missing-cache").exists()
        and not (tmp_path / "missing-extraction").exists()
    )


@pytest.mark.parametrize("grid_flag", [[], ["--with-grid"]])
def test_cli_road_policy_requires_road_flag_before_run(tmp_path, grid_flag):
    _forbid_child_network(tmp_path)
    before = set(tmp_path.iterdir())
    result = _cli(
        tmp_path, "scan", "--scan", "unused", "--road-policy", "unused", *grid_flag
    )
    assert result.returncode == 2 and "requires --with-roads" in result.stderr
    assert set(tmp_path.iterdir()) == before
