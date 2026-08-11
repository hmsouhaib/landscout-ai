from pathlib import Path
from typing import Annotated, Any

import yaml  # type: ignore[import-untyped]
from pydantic import BaseModel, ConfigDict, Field, StringConstraints, model_validator

NonEmptyString = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
CommuneCode = Annotated[str, StringConstraints(pattern=r"^\d{5}$")]


class ParcelConfig(BaseModel):
    min_area_m2: float = Field(gt=0)
    max_area_m2: float

    @model_validator(mode="after")
    def validate_area_range(self) -> "ParcelConfig":
        if self.max_area_m2 <= self.min_area_m2:
            raise ValueError("max_area_m2 must be greater than min_area_m2")
        return self


class ShapeCalibrationConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    policy_version: NonEmptyString
    method: NonEmptyString
    calibration_scope: NonEmptyString
    sample_size: int = Field(gt=0)
    calibrated_at: NonEmptyString
    target_retention_pct: float = Field(gt=0, le=100, allow_inf_nan=False)
    observed_retention_pct: float = Field(ge=0, le=100, allow_inf_nan=False)


class ShapeScreeningConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    enabled: bool
    min_width_m: float | None = Field(default=None, gt=0, allow_inf_nan=False)
    max_length_width_ratio: float | None = Field(
        default=None, ge=1, allow_inf_nan=False
    )
    calibration: ShapeCalibrationConfig | None = None

    @model_validator(mode="after")
    def validate_enabled_policy(self) -> "ShapeScreeningConfig":
        if not self.enabled:
            return self

        required_values = {
            "min_width_m": self.min_width_m,
            "max_length_width_ratio": self.max_length_width_ratio,
            "calibration": self.calibration,
        }
        missing = [name for name, value in required_values.items() if value is None]
        if missing:
            formatted = ", ".join(missing)
            raise ValueError(f"enabled shape screening requires: {formatted}")
        return self


class CrsConfig(BaseModel):
    storage: NonEmptyString
    calculation: NonEmptyString


class BessProfile(BaseModel):
    country: NonEmptyString
    technology: NonEmptyString
    parcel: ParcelConfig
    shape_screening: ShapeScreeningConfig
    crs: CrsConfig


class ScanMetadata(BaseModel):
    name: NonEmptyString
    country: NonEmptyString
    technology: NonEmptyString


class AoiConfig(BaseModel):
    commune_codes: list[CommuneCode]


class ProfileReference(BaseModel):
    path: Path


class OutputConfig(BaseModel):
    directory: Path


class ScanConfig(BaseModel):
    scan: ScanMetadata
    aoi: AoiConfig
    profile: ProfileReference
    output: OutputConfig


class LoadedScanConfig(BaseModel):
    scan_config: ScanConfig
    profile: BessProfile
    profile_path: Path


def _load_yaml(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as stream:
        content = yaml.safe_load(stream)
    if not isinstance(content, dict):
        raise TypeError(f"Expected a YAML mapping in {path}")
    return content


def _resolve_profile_path(scan_path: Path, profile_path: Path) -> Path:
    if profile_path.is_absolute():
        return profile_path

    resolved_scan_path = scan_path.resolve()
    project_root = resolved_scan_path.parents[2]
    return project_root / profile_path


def load_scan_config(path: Path) -> LoadedScanConfig:
    scan_path = path.resolve()
    scan_config = ScanConfig.model_validate(_load_yaml(scan_path))
    profile_path = _resolve_profile_path(scan_path, scan_config.profile.path)
    if not profile_path.is_file():
        raise FileNotFoundError(f"Profile file does not exist: {profile_path}")

    profile = BessProfile.model_validate(_load_yaml(profile_path))
    return LoadedScanConfig(
        scan_config=scan_config,
        profile=profile,
        profile_path=profile_path,
    )
