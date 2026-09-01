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


def _load_temporary_profile(tmp_path: Path, profile_data: dict):
    profile_path = tmp_path / "profile.yaml"
    _write_yaml(profile_path, profile_data)
    return load_scan_config(_temporary_scan(tmp_path, profile_path))


def test_valid_config_loads() -> None:
    loaded = load_scan_config(SCAN_PATH)

    assert loaded.scan_config.aoi.commune_codes == ("31395",)
    assert loaded.profile.technology == "BESS"
    assert loaded.profile_path == PROFILE_PATH

    shape_screening = loaded.profile.shape_screening
    assert shape_screening.enabled is True
    assert shape_screening.min_width_m == 15
    assert shape_screening.max_length_width_ratio == 10

    calibration = shape_screening.calibration
    assert calibration is not None
    assert calibration.policy_version == "muret_empirical_v1"
    assert calibration.method == "empirical_distribution"
    assert calibration.calibration_scope == "Muret 31395"
    assert calibration.sample_size == 4013
    assert calibration.calibrated_at == "2026-08-11"
    assert calibration.target_retention_pct == 90
    assert calibration.observed_retention_pct == 90.655370


@pytest.mark.parametrize("document", ["scan", "profile"])
def test_trust_bearing_yaml_rejects_duplicate_mapping_keys(
    tmp_path: Path,
    document: str,
) -> None:
    scan_data = _yaml_data(SCAN_PATH)
    scan_data["profile"]["path"] = str(PROFILE_PATH)
    if document == "scan":
        duplicate = yaml.safe_dump(scan_data, sort_keys=False) + yaml.safe_dump(
            {"scan": scan_data["scan"]}, sort_keys=False
        )
        path = tmp_path / "scan.yaml"
        path.write_text(duplicate, encoding="utf-8")
        action = lambda: load_scan_config(path)
    else:
        profile_data = _yaml_data(PROFILE_PATH)
        duplicate = yaml.safe_dump(profile_data, sort_keys=False) + yaml.safe_dump(
            {"parcel": profile_data["parcel"]}, sort_keys=False
        )
        profile_path = tmp_path / "profile.yaml"
        profile_path.write_text(duplicate, encoding="utf-8")
        action = lambda: load_scan_config(_temporary_scan(tmp_path, profile_path))

    with pytest.raises((TypeError, ValueError), match="(?i)duplicate"):
        action()


def test_loaded_scan_and_profile_models_are_immutable() -> None:
    loaded = load_scan_config(SCAN_PATH)

    with pytest.raises(ValidationError, match="frozen"):
        loaded.scan_config.scan.name = "mutated"
    with pytest.raises(ValidationError, match="frozen"):
        loaded.profile.parcel.min_area_m2 = 1.0
    with pytest.raises(AttributeError):
        loaded.scan_config.aoi.commune_codes.append("75056")


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


@pytest.mark.parametrize(
    ("field", "invalid_value"),
    [
        ("min_width_m", -1),
        ("min_width_m", 0),
        ("max_length_width_ratio", 0),
        ("max_length_width_ratio", 0.999),
    ],
)
def test_invalid_shape_threshold_fails(
    tmp_path: Path, field: str, invalid_value: float
) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    profile_data["shape_screening"][field] = invalid_value

    with pytest.raises(ValidationError):
        _load_temporary_profile(tmp_path, profile_data)


@pytest.mark.parametrize(
    ("field", "invalid_value"),
    [
        ("target_retention_pct", -1),
        ("target_retention_pct", 0),
        ("target_retention_pct", 100.001),
        ("observed_retention_pct", -0.001),
        ("observed_retention_pct", 100.001),
    ],
)
def test_invalid_calibration_percentage_fails(
    tmp_path: Path, field: str, invalid_value: float
) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    profile_data["shape_screening"]["calibration"][field] = invalid_value

    with pytest.raises(ValidationError):
        _load_temporary_profile(tmp_path, profile_data)


@pytest.mark.parametrize("invalid_value", [-1, 0])
def test_invalid_calibration_sample_size_fails(
    tmp_path: Path, invalid_value: int
) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    profile_data["shape_screening"]["calibration"]["sample_size"] = invalid_value

    with pytest.raises(ValidationError):
        _load_temporary_profile(tmp_path, profile_data)


@pytest.mark.parametrize(
    "field",
    ["policy_version", "method", "calibration_scope", "calibrated_at"],
)
def test_empty_calibration_metadata_fails(tmp_path: Path, field: str) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    profile_data["shape_screening"]["calibration"][field] = "   "

    with pytest.raises(ValidationError):
        _load_temporary_profile(tmp_path, profile_data)


@pytest.mark.parametrize(
    "field", ["min_width_m", "max_length_width_ratio", "calibration"]
)
def test_enabled_shape_screening_requires_policy_values(
    tmp_path: Path, field: str
) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    del profile_data["shape_screening"][field]

    with pytest.raises(ValidationError, match="enabled shape screening requires"):
        _load_temporary_profile(tmp_path, profile_data)


@pytest.mark.parametrize(
    "field",
    [
        "policy_version",
        "method",
        "calibration_scope",
        "sample_size",
        "calibrated_at",
        "target_retention_pct",
        "observed_retention_pct",
    ],
)
def test_enabled_shape_screening_requires_complete_calibration(
    tmp_path: Path, field: str
) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    del profile_data["shape_screening"]["calibration"][field]

    with pytest.raises(ValidationError):
        _load_temporary_profile(tmp_path, profile_data)


def test_shape_screening_can_be_disabled_without_policy_values(
    tmp_path: Path,
) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    profile_data["shape_screening"] = {"enabled": False}

    loaded = _load_temporary_profile(tmp_path, profile_data)

    shape_screening = loaded.profile.shape_screening
    assert shape_screening.enabled is False
    assert shape_screening.min_width_m is None
    assert shape_screening.max_length_width_ratio is None
    assert shape_screening.calibration is None


@pytest.mark.parametrize(
    ("section", "field"),
    [(None, "unknown"), ("aoi", "unexpected"), ("profile", "unexpected")],
)
def test_unknown_scan_fields_are_rejected(
    tmp_path: Path,
    section: str | None,
    field: str,
) -> None:
    scan_data = _yaml_data(SCAN_PATH)
    scan_data["profile"]["path"] = str(PROFILE_PATH)
    target = scan_data if section is None else scan_data[section]
    target[field] = "value"
    scan_path = tmp_path / "scan.yaml"
    _write_yaml(scan_path, scan_data)

    with pytest.raises(ValidationError, match=field):
        load_scan_config(scan_path)


@pytest.mark.parametrize("section", ["parcel", "crs", "shape_screening"])
def test_unknown_profile_fields_are_rejected(
    tmp_path: Path,
    section: str,
) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    profile_data[section]["unexpected"] = "value"

    with pytest.raises(ValidationError, match="unexpected"):
        _load_temporary_profile(tmp_path, profile_data)


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("min_area_m2", 0),
        ("max_area_m2", -1),
        ("max_area_m2", float("nan")),
        ("max_area_m2", float("inf")),
        ("max_area_m2", "15000"),
        ("min_area_m2", True),
    ],
)
def test_parcel_numeric_contract_is_strict_and_finite(
    tmp_path: Path,
    field: str,
    value: object,
) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    profile_data["parcel"][field] = value

    with pytest.raises(ValidationError):
        _load_temporary_profile(tmp_path, profile_data)


@pytest.mark.parametrize("value", [True, "4013", 0, -1])
def test_calibration_sample_size_is_strict_positive_integer(
    tmp_path: Path,
    value: object,
) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    profile_data["shape_screening"]["calibration"]["sample_size"] = value

    with pytest.raises(ValidationError):
        _load_temporary_profile(tmp_path, profile_data)


@pytest.mark.parametrize("value", ["true", 1, 0])
def test_shape_enabled_is_strict_boolean(tmp_path: Path, value: object) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    profile_data["shape_screening"]["enabled"] = value

    with pytest.raises(ValidationError):
        _load_temporary_profile(tmp_path, profile_data)


@pytest.mark.parametrize("code", ["31395", "75056", "2A004", "2B033"])
def test_canonical_france_commune_codes_are_accepted(
    tmp_path: Path,
    code: str,
) -> None:
    scan_data = _yaml_data(SCAN_PATH)
    scan_data["profile"]["path"] = str(PROFILE_PATH)
    scan_data["aoi"]["commune_codes"] = [code]
    scan_path = tmp_path / "scan.yaml"
    _write_yaml(scan_path, scan_data)

    assert load_scan_config(scan_path).scan_config.aoi.commune_codes == (code,)


@pytest.mark.parametrize(
    "code",
    ["", "3139", "313950", "ABCDE", "2C004", "2a004", " 31395 ", 31395],
)
def test_noncanonical_france_commune_codes_are_rejected(
    tmp_path: Path,
    code: object,
) -> None:
    scan_data = _yaml_data(SCAN_PATH)
    scan_data["profile"]["path"] = str(PROFILE_PATH)
    scan_data["aoi"]["commune_codes"] = [code]
    scan_path = tmp_path / "scan.yaml"
    _write_yaml(scan_path, scan_data)

    with pytest.raises(ValidationError):
        load_scan_config(scan_path)


@pytest.mark.parametrize("codes", [[], ["31395", "31395"]])
def test_aoi_requires_nonempty_unique_commune_codes(
    tmp_path: Path,
    codes: list[str],
) -> None:
    scan_data = _yaml_data(SCAN_PATH)
    scan_data["profile"]["path"] = str(PROFILE_PATH)
    scan_data["aoi"]["commune_codes"] = codes
    scan_path = tmp_path / "scan.yaml"
    _write_yaml(scan_path, scan_data)

    with pytest.raises(ValidationError):
        load_scan_config(scan_path)


@pytest.mark.parametrize(
    ("field", "value"),
    [("country", "BE"), ("technology", "SOLAR")],
)
def test_scan_and_profile_identity_must_match(
    tmp_path: Path,
    field: str,
    value: str,
) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    profile_data[field] = value

    with pytest.raises(ValidationError, match=field):
        _load_temporary_profile(tmp_path, profile_data)


@pytest.mark.parametrize(
    ("field", "value"),
    [("storage", "EPSG:3857"), ("calculation", "EPSG:4326"), ("storage", "bad")],
)
def test_profile_crs_contract_is_exact(
    tmp_path: Path,
    field: str,
    value: str,
) -> None:
    profile_data = _yaml_data(PROFILE_PATH)
    profile_data["crs"][field] = value

    with pytest.raises(ValidationError, match="CRS|crs|storage|calculation"):
        _load_temporary_profile(tmp_path, profile_data)
