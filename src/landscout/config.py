from math import isfinite
from numbers import Real
from pathlib import Path
from typing import Annotated, Any

from pydantic import (
    BaseModel,
    BeforeValidator,
    ConfigDict,
    Field,
    StrictBool,
    StringConstraints,
    model_validator,
)
from pydantic_core import PydanticCustomError
from pyproj import CRS

from landscout.common.strict_yaml import loads_strict_yaml

NonEmptyString = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
CommuneCode = Annotated[
    str,
    StringConstraints(strict=True, pattern=r"^(?:\d{5}|2[AB]\d{3})$"),
]


def _strict_finite_number(value: object) -> object:
    if isinstance(value, bool) or not isinstance(value, Real):
        raise PydanticCustomError(
            "strict_number",
            "value must be a strict YAML number",
        )
    if not isfinite(float(value)):
        raise ValueError("value must be finite")
    return value


StrictFiniteFloat = Annotated[float, BeforeValidator(_strict_finite_number)]
StrictPositiveFloat = Annotated[
    float,
    BeforeValidator(_strict_finite_number),
    Field(gt=0, allow_inf_nan=False),
]
StrictPositiveInt = Annotated[int, Field(strict=True, gt=0)]


class _ConfigModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class ParcelConfig(_ConfigModel):
    min_area_m2: StrictPositiveFloat
    max_area_m2: StrictPositiveFloat

    @model_validator(mode="after")
    def validate_area_range(self) -> "ParcelConfig":
        if self.max_area_m2 <= self.min_area_m2:
            raise ValueError("max_area_m2 must be greater than min_area_m2")
        return self


class ShapeCalibrationConfig(_ConfigModel):
    policy_version: NonEmptyString
    method: NonEmptyString
    calibration_scope: NonEmptyString
    sample_size: StrictPositiveInt
    calibrated_at: NonEmptyString
    target_retention_pct: Annotated[
        StrictFiniteFloat, Field(gt=0, le=100, allow_inf_nan=False)
    ]
    observed_retention_pct: Annotated[
        StrictFiniteFloat, Field(ge=0, le=100, allow_inf_nan=False)
    ]


class ShapeScreeningConfig(_ConfigModel):
    enabled: StrictBool
    min_width_m: StrictPositiveFloat | None = None
    max_length_width_ratio: StrictFiniteFloat | None = Field(
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


class CrsConfig(_ConfigModel):
    storage: NonEmptyString
    calculation: NonEmptyString

    @model_validator(mode="after")
    def validate_crs_contract(self) -> "CrsConfig":
        for field, value, expected in (
            ("storage", self.storage, 4326),
            ("calculation", self.calculation, 2154),
        ):
            try:
                observed = CRS.from_user_input(value)
            except Exception as error:
                raise ValueError(f"{field} CRS is unreadable") from error
            if not observed.equals(CRS.from_epsg(expected)):
                raise ValueError(f"{field} CRS must be EPSG:{expected}")
        return self


class BessProfile(_ConfigModel):
    country: NonEmptyString
    technology: NonEmptyString
    parcel: ParcelConfig
    shape_screening: ShapeScreeningConfig
    crs: CrsConfig


class ScanMetadata(_ConfigModel):
    name: NonEmptyString
    country: NonEmptyString
    technology: NonEmptyString


class AoiConfig(_ConfigModel):
    commune_codes: tuple[CommuneCode, ...] = Field(min_length=1)

    @model_validator(mode="after")
    def validate_unique_communes(self) -> "AoiConfig":
        if len(set(self.commune_codes)) != len(self.commune_codes):
            raise ValueError("commune_codes must not contain duplicates")
        return self


class ProfileReference(_ConfigModel):
    path: Path


class OutputConfig(_ConfigModel):
    directory: Path


class ScanConfig(_ConfigModel):
    scan: ScanMetadata
    aoi: AoiConfig
    profile: ProfileReference
    output: OutputConfig


class LoadedScanConfig(_ConfigModel):
    scan_config: ScanConfig
    profile: BessProfile
    profile_path: Path

    @model_validator(mode="after")
    def validate_scan_profile_identity(self) -> "LoadedScanConfig":
        if self.scan_config.scan.country != self.profile.country:
            raise ValueError("scan country must equal profile country")
        if self.scan_config.scan.technology != self.profile.technology:
            raise ValueError("scan technology must equal profile technology")
        return self


def _load_yaml(path: Path) -> dict[str, Any]:
    content = loads_strict_yaml(path.read_bytes())
    if type(content) is not dict:
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
