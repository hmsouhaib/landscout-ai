from pathlib import Path

import pytest
import yaml
from pydantic import ValidationError

from landscout.config import load_scan_config

PROJECT_ROOT = Path(__file__).parents[2]
SCAN_PATH = PROJECT_ROOT / "configs/scans/bess_muret.yaml"
PROFILE_PATH = PROJECT_ROOT / "configs/profiles/bess_default_fr.yaml"


def _yaml_data(path: Path) -> dict:
    with path.open(encoding="utf-8") as stream:
        return yaml.safe_load(stream)


def _write_yaml(path: Path, data: dict) -> None:
    path.write_text(yaml.safe_dump(data), encoding="utf-8")


def _temporary_scan(tmp_path: Path, profile_path: Path) -> Path:
    scan_data = _yaml_data(SCAN_PATH)
    scan_data["profile"]["path"] = str(profile_path)
    scan_path = tmp_path / "scan.yaml"
    _write_yaml(scan_path, scan_data)
    return scan_path


def test_valid_config_loads() -> None:
    loaded = load_scan_config(SCAN_PATH)

    assert loaded.scan_config.aoi.commune_codes == ["31395"]
    assert loaded.profile.technology == "BESS"
    assert loaded.profile_path == PROFILE_PATH


def test_invalid_commune_code_fails(tmp_path: Path) -> None:
    scan_data = _yaml_data(SCAN_PATH)
    scan_data["aoi"]["commune_codes"] = ["3139"]
    scan_path = tmp_path / "scan.yaml"
    _write_yaml(scan_path, scan_data)

    with pytest.raises(ValidationError):
        load_scan_config(scan_path)


def test_negative_minimum_area_fails(tmp_path: Path) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    profile_data["parcel"]["min_area_m2"] = -1
    profile_path = tmp_path / "profile.yaml"
    _write_yaml(profile_path, profile_data)

    with pytest.raises(ValidationError):
        load_scan_config(_temporary_scan(tmp_path, profile_path))


def test_maximum_area_smaller_than_minimum_fails(tmp_path: Path) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    profile_data["parcel"]["max_area_m2"] = 1000
    profile_path = tmp_path / "profile.yaml"
    _write_yaml(profile_path, profile_data)

    with pytest.raises(ValidationError):
        load_scan_config(_temporary_scan(tmp_path, profile_path))


def test_missing_profile_fails(tmp_path: Path) -> None:
    missing_profile = tmp_path / "missing.yaml"

    with pytest.raises(FileNotFoundError):
        load_scan_config(_temporary_scan(tmp_path, missing_profile))
