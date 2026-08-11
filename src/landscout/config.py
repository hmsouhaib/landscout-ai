from pathlib import Path
from typing import Annotated, Any

import yaml  # type: ignore[import-untyped]
from pydantic import BaseModel, Field, StringConstraints, model_validator

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


class CrsConfig(BaseModel):
    storage: NonEmptyString
    calculation: NonEmptyString


class BessProfile(BaseModel):
    country: NonEmptyString
    technology: NonEmptyString
    parcel: ParcelConfig
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
