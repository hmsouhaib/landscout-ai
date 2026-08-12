"""Resolve factual GPU planning-feature codes against an offline CNIG snapshot."""

from __future__ import annotations

import json
import math
import re
import unicodedata
from collections.abc import Mapping, Sequence
from dataclasses import dataclass, replace
from datetime import date, datetime
from hashlib import sha256
from numbers import Integral, Real
from pathlib import Path
from typing import Literal

import geopandas as gpd  # type: ignore[import-untyped]
import numpy as np
import pandas as pd  # type: ignore[import-untyped]
import yaml  # type: ignore[import-untyped]
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, model_validator
from pyproj import CRS
from shapely import to_wkb  # type: ignore[import-untyped]
from shapely.geometry.base import BaseGeometry  # type: ignore[import-untyped]

from landscout.sources.gpu_fr import GpuPlanningDocument

__all__ = [
    "CnigFeatureCodeProfile",
    "PlanningFeatureCodeError",
    "PlanningFeatureCodeResult",
    "load_cnig_feature_code_profile",
    "resolve_planning_feature_codes",
    "validate_planning_feature_code_result",
]

PROFILE_SCHEMA_VERSION = 2
RESULT_HASH_SCHEMA_VERSION = 2
STANDARD_MODEL = "CNIG PLU v2017"
OFFICIAL_TEXT_NORMALIZATION = "GPU_DISPLAY_TEXT_NFC_WHITESPACE_V1"
PRESCRIPTION_OFFICIAL_SOURCE_URL = (
    "https://www.geoportail-urbanisme.gouv.fr/standard/"
    "cnig_PLU_2017/codes/PrescriptionUrbaType"
)
INFORMATION_OFFICIAL_SOURCE_URL = (
    "https://www.geoportail-urbanisme.gouv.fr/standard/"
    "cnig_PLU_2017/codes/InformationUrbaType"
)

FeatureFamily = Literal["PRESCRIPTION", "INFORMATION"]
OfficialCodeStatus = Literal["RESOLVED_OFFICIAL", "UNKNOWN_CODE_PAIR"]

OFFICIAL_CODE_COLUMNS = (
    "official_code_status",
    "official_code_label",
    "official_legal_reference",
    "official_regulation_reference",
    "official_code_source_url",
    "official_code_profile",
    "official_code_profile_sha256",
)
CODE_DICTIONARY_COLUMNS = (
    "feature_family",
    "type_code",
    "subtype_code",
    "official_label",
    "legal_reference",
    "regulation_or_annex_reference",
    "official_source_url",
    "profile",
    "profile_sha256",
    "standard_model",
)

_FEATURE_REQUIRED_COLUMNS = (
    "planning_feature_id",
    "source_feature_id",
    "source_identity_kind",
    "source_identity_field",
    "logical_layer",
    "feature_family",
    "geometry_kind",
    "type_code_raw",
    "subtype_code_raw",
    "source_document_id",
    "source_archive_sha256",
    "source_layer",
    "source_standard_model",
    "geometry",
)
_RELATION_MATCH_COLUMNS = (
    "source_feature_id",
    "source_identity_kind",
    "source_identity_field",
    "logical_layer",
    "feature_family",
    "geometry_kind",
    "type_code_raw",
    "subtype_code_raw",
    "source_document_id",
    "source_archive_sha256",
    "source_layer",
)
_CODE_PATTERN = re.compile(r"[0-9]{2}")
_SHA_PATTERN = re.compile(r"[0-9a-f]{64}")
_CATALOG_STRING_COLUMNS = (
    "planning_feature_id",
    "source_feature_id",
    "source_identity_kind",
    "source_identity_field",
    "logical_layer",
    "feature_family",
    "geometry_kind",
    "source_layer",
)


@dataclass(frozen=True)
class _CatalogContract:
    geometry_kind: str
    logical_layers: frozenset[str]
    geometry_types: frozenset[str]


_CATALOG_CONTRACTS = {
    "surface": _CatalogContract(
        geometry_kind="SURFACE",
        logical_layers=frozenset({"prescription_surface", "information_surface"}),
        geometry_types=frozenset({"Polygon", "MultiPolygon"}),
    ),
    "line": _CatalogContract(
        geometry_kind="LINE",
        logical_layers=frozenset({"prescription_line", "information_line"}),
        geometry_types=frozenset({"LineString", "MultiLineString"}),
    ),
    "point": _CatalogContract(
        geometry_kind="POINT",
        logical_layers=frozenset({"prescription_point", "information_point"}),
        geometry_types=frozenset({"Point", "MultiPoint"}),
    ),
}
_RELATION_TYPES_BY_GEOMETRY_KIND = {
    "SURFACE": frozenset({"AREA_OVERLAP", "TOUCH_ONLY"}),
    "LINE": frozenset({"LENGTH_OVERLAP", "TOUCH_ONLY"}),
    "POINT": frozenset({"INSIDE", "BOUNDARY_TOUCH"}),
}


class PlanningFeatureCodeError(ValueError):
    """Raised when official code resolution integrity cannot be proven."""


class _StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


def _exact_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise ValueError(f"{label} must be a non-empty exact string")
    return value


def _canonical_official_text(value: str) -> str:
    return " ".join(unicodedata.normalize("NFC", value).split())


def _validate_official_text(value: object, label: str) -> str:
    text = _exact_string(value, label)
    if text != _canonical_official_text(text):
        raise ValueError(
            f"{label} must already use canonical {OFFICIAL_TEXT_NORMALIZATION} text"
        )
    return text


def _validate_optional_official_text(value: object, label: str) -> str | None:
    if value is None:
        return None
    return _validate_official_text(value, label)


class OfficialSourceUrls(_StrictModel):
    prescription: StrictStr
    information: StrictStr

    @model_validator(mode="after")
    def _validate_urls(self) -> OfficialSourceUrls:
        if self.prescription != PRESCRIPTION_OFFICIAL_SOURCE_URL:
            raise ValueError(
                "prescription source URL is not the exact official GPU host endpoint"
            )
        if self.information != INFORMATION_OFFICIAL_SOURCE_URL:
            raise ValueError(
                "information source URL is not the exact official GPU host endpoint"
            )
        return self


class CnigFeatureCodeRecord(_StrictModel):
    feature_family: FeatureFamily
    type_code: StrictStr
    subtype_code: StrictStr
    official_label: StrictStr
    legal_reference: StrictStr | None
    regulation_or_annex_reference: StrictStr | None
    official_source_url: StrictStr

    @model_validator(mode="after")
    def _validate_record(self) -> CnigFeatureCodeRecord:
        for code, label in (
            (self.type_code, "type code"),
            (self.subtype_code, "subtype code"),
        ):
            if _CODE_PATTERN.fullmatch(code) is None:
                raise ValueError(f"{label} must contain exactly two digits")
        _validate_official_text(self.official_label, "official label")
        _validate_optional_official_text(self.legal_reference, "legal reference")
        _validate_optional_official_text(
            self.regulation_or_annex_reference,
            "regulation or annex reference",
        )
        expected_url = (
            PRESCRIPTION_OFFICIAL_SOURCE_URL
            if self.feature_family == "PRESCRIPTION"
            else INFORMATION_OFFICIAL_SOURCE_URL
        )
        if self.official_source_url != expected_url:
            raise ValueError("record source URL is not the exact family endpoint")
        return self


def _record_payload(record: CnigFeatureCodeRecord) -> dict[str, object]:
    return {
        "feature_family": record.feature_family,
        "type_code": record.type_code,
        "subtype_code": record.subtype_code,
        "official_label": record.official_label,
        "legal_reference": record.legal_reference,
        "regulation_or_annex_reference": record.regulation_or_annex_reference,
        "official_source_url": record.official_source_url,
    }


def _canonical_json_sha256(value: object) -> str:
    try:
        encoded = json.dumps(
            value,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    except Exception as error:
        raise PlanningFeatureCodeError(
            "Canonical integrity payload cannot be serialized"
        ) from error
    return sha256(encoded).hexdigest()


def _records_sha256(records: Sequence[CnigFeatureCodeRecord]) -> str:
    return _canonical_json_sha256([_record_payload(record) for record in records])


class CnigFeatureCodeProfile(_StrictModel):
    """Strict offline snapshot of official CNIG feature code records."""

    schema_version: StrictInt
    profile: StrictStr = Field(min_length=1)
    standard_model: Literal["CNIG PLU v2017"]
    official_text_normalization: Literal["GPU_DISPLAY_TEXT_NFC_WHITESPACE_V1"]
    official_sources: OfficialSourceUrls
    retrieval_date: date
    canonical_records_sha256: StrictStr
    records: tuple[CnigFeatureCodeRecord, ...] = Field(min_length=1)

    @model_validator(mode="after")
    def _validate_profile(self) -> CnigFeatureCodeProfile:
        if self.schema_version != PROFILE_SCHEMA_VERSION:
            raise ValueError(
                f"unsupported CNIG feature-code profile schema: {self.schema_version}"
            )
        _exact_string(self.profile, "code profile")
        if _SHA_PATTERN.fullmatch(self.canonical_records_sha256) is None:
            raise ValueError("canonical records SHA256 is invalid")
        keys = [
            (record.feature_family, record.type_code, record.subtype_code)
            for record in self.records
        ]
        if len(set(keys)) != len(keys):
            raise ValueError("configured CNIG code pairs contain a duplicate")
        if keys != sorted(keys):
            raise ValueError("configured CNIG records must use deterministic order")
        if _records_sha256(self.records) != self.canonical_records_sha256:
            raise ValueError("canonical records SHA256 differs from configured records")
        return self


class _UniqueKeyLoader(yaml.SafeLoader):
    pass


def _construct_unique_mapping(
    loader: yaml.SafeLoader,
    node: yaml.MappingNode,
    deep: bool = False,
) -> dict[object, object]:
    result: dict[object, object] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise PlanningFeatureCodeError(f"Duplicate YAML code-profile key: {key!r}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


_UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    _construct_unique_mapping,
)


def load_cnig_feature_code_profile(path: str | Path) -> CnigFeatureCodeProfile:
    """Load a strict offline CNIG feature-code profile."""

    try:
        payload = yaml.load(
            Path(path).read_text(encoding="utf-8"), Loader=_UniqueKeyLoader
        )
        if not isinstance(payload, Mapping):
            raise PlanningFeatureCodeError(
                "CNIG feature-code profile must be a mapping"
            )
        return CnigFeatureCodeProfile.model_validate(payload)
    except PlanningFeatureCodeError:
        raise
    except Exception as error:
        raise PlanningFeatureCodeError(
            "CNIG feature-code profile is invalid"
        ) from error


@dataclass(frozen=True)
class PlanningFeatureCodeResult:
    """Immutable envelope around exact official code resolution outputs."""

    result_hash_schema_version: int
    profile_schema_version: int
    profile: str
    standard_model: str
    profile_sha256: str
    source_document_id: str
    source_archive_sha256: str
    code_dictionary_content_sha256: str
    surface_features_content_sha256: str
    line_features_content_sha256: str
    point_features_content_sha256: str
    relations_content_sha256: str
    complete_result_content_sha256: str
    code_dictionary: pd.DataFrame
    surface_features: gpd.GeoDataFrame
    line_features: gpd.GeoDataFrame
    point_features: gpd.GeoDataFrame
    relations: pd.DataFrame


def _resolved_profile(
    profile: CnigFeatureCodeProfile | str | Path,
) -> CnigFeatureCodeProfile:
    if not isinstance(profile, CnigFeatureCodeProfile):
        return load_cnig_feature_code_profile(profile)
    try:
        payload = profile.model_dump(mode="python", warnings="error")
        return CnigFeatureCodeProfile.model_validate(payload)
    except Exception as error:
        raise PlanningFeatureCodeError(
            "In-memory CNIG feature-code profile is invalid"
        ) from error


def _profile_sha256(profile: CnigFeatureCodeProfile) -> str:
    return _canonical_json_sha256(profile.model_dump(mode="json"))


def _strict_string(value: object, label: str) -> str:
    try:
        return _exact_string(value, label)
    except ValueError as error:
        raise PlanningFeatureCodeError(str(error)) from error


def _planning_standard(document: GpuPlanningDocument) -> str:
    if not isinstance(document, GpuPlanningDocument):
        raise PlanningFeatureCodeError(
            "planning_document must be a GpuPlanningDocument"
        )
    metadata = document.extraction.archive.document
    models = list(document.extraction.standard_models)
    if metadata.standard_model is not None:
        models.append(metadata.standard_model)
    distinct = tuple(dict.fromkeys(models))
    if len(distinct) != 1:
        raise PlanningFeatureCodeError(
            "Planning document standard lineage is ambiguous"
        )
    return _strict_string(distinct[0], "planning document standard")


def _validated_code_series(series: pd.Series, label: str) -> None:
    for value in series.tolist():
        if not isinstance(value, str) or _CODE_PATTERN.fullmatch(value) is None:
            raise PlanningFeatureCodeError(
                f"{label} must contain exact two-character digit strings"
            )


def _validate_exact_string_column(
    frame: pd.DataFrame,
    column: str,
    label: str,
) -> None:
    for value in frame[column].tolist():
        _strict_string(value, f"{label} {column}")


def _validate_feature_catalog(
    frame: object,
    catalog_kind: str,
    label: str,
    document: GpuPlanningDocument,
    standard_model: str,
) -> gpd.GeoDataFrame:
    if not isinstance(frame, gpd.GeoDataFrame):
        raise PlanningFeatureCodeError(f"{label} must be a GeoDataFrame")
    if frame.columns.duplicated().any():
        raise PlanningFeatureCodeError(f"{label} contains duplicate columns")
    missing = set(_FEATURE_REQUIRED_COLUMNS).difference(frame.columns)
    if missing:
        raise PlanningFeatureCodeError(f"{label} lacks columns: {sorted(missing)}")
    collisions = set(OFFICIAL_CODE_COLUMNS).intersection(frame.columns)
    if collisions:
        raise PlanningFeatureCodeError(
            f"{label} already contains official-code columns: {sorted(collisions)}"
        )
    try:
        active_geometry = frame.active_geometry_name
    except Exception as error:
        raise PlanningFeatureCodeError(
            f"{label} active geometry is unavailable"
        ) from error
    if active_geometry != "geometry":
        raise PlanningFeatureCodeError(
            f"{label} must use geometry as its active geometry column"
        )
    if frame.crs is None:
        raise PlanningFeatureCodeError(f"{label} CRS is missing")
    try:
        CRS.from_user_input(frame.crs)
    except Exception as error:
        raise PlanningFeatureCodeError(f"{label} CRS is invalid") from error
    contract = _CATALOG_CONTRACTS[catalog_kind]
    for column in _CATALOG_STRING_COLUMNS:
        _validate_exact_string_column(frame, column, label)
    identifiers = frame["planning_feature_id"]
    if identifiers.duplicated().any():
        raise PlanningFeatureCodeError(f"{label} planning feature IDs must be unique")
    _validated_code_series(frame["type_code_raw"], f"{label} type code")
    _validated_code_series(frame["subtype_code_raw"], f"{label} subtype code")
    geometry = frame.geometry
    if geometry.isna().any():
        raise PlanningFeatureCodeError(f"{label} geometry must be non-null")
    if geometry.is_empty.any():
        raise PlanningFeatureCodeError(f"{label} geometry must be non-empty")
    if (~geometry.is_valid).any():
        raise PlanningFeatureCodeError(f"{label} geometry must be valid")
    geometry_types = set(geometry.geom_type.tolist())
    if not geometry_types.issubset(contract.geometry_types):
        raise PlanningFeatureCodeError(
            f"{label} geometry type differs from its {catalog_kind} contract"
        )
    for row in frame[["logical_layer", "feature_family", "geometry_kind"]].itertuples(
        index=False,
        name=None,
    ):
        logical_layer, family, geometry_kind = row
        if logical_layer not in contract.logical_layers:
            raise PlanningFeatureCodeError(
                f"{label} logical layer differs from its {catalog_kind} contract"
            )
        if geometry_kind != contract.geometry_kind:
            raise PlanningFeatureCodeError(
                f"{label} geometry kind differs from its {catalog_kind} contract"
            )
        expected_family = (
            "PRESCRIPTION"
            if str(logical_layer).startswith("prescription_")
            else "INFORMATION"
        )
        if family != expected_family:
            raise PlanningFeatureCodeError(
                f"{label} logical layer and feature family disagree"
            )
    metadata = document.extraction.archive.document
    if not frame["source_document_id"].eq(metadata.document_id).all():
        raise PlanningFeatureCodeError(f"{label} document lineage differs")
    if not frame["source_archive_sha256"].eq(document.extraction.archive.sha256).all():
        raise PlanningFeatureCodeError(f"{label} archive lineage differs")
    if not frame["source_standard_model"].eq(standard_model).all():
        raise PlanningFeatureCodeError(f"{label} source standard lineage differs")
    return frame.copy(deep=True)


def _dictionary(
    profile: CnigFeatureCodeProfile,
    profile_hash: str,
) -> pd.DataFrame:
    rows = [
        {
            **_record_payload(record),
            "profile": profile.profile,
            "profile_sha256": profile_hash,
            "standard_model": profile.standard_model,
        }
        for record in profile.records
    ]
    return pd.DataFrame(rows, columns=CODE_DICTIONARY_COLUMNS)


def _lookup(
    profile: CnigFeatureCodeProfile,
) -> dict[tuple[str, str, str], CnigFeatureCodeRecord]:
    return {
        (record.feature_family, record.type_code, record.subtype_code): record
        for record in profile.records
    }


def _coded_catalog(
    frame: gpd.GeoDataFrame,
    profile: CnigFeatureCodeProfile,
    profile_hash: str,
) -> gpd.GeoDataFrame:
    output = frame.copy(deep=True)
    mapping = _lookup(profile)
    columns: dict[str, list[object]] = {column: [] for column in OFFICIAL_CODE_COLUMNS}
    for row in frame.to_dict("records"):
        key = (row["feature_family"], row["type_code_raw"], row["subtype_code_raw"])
        record = mapping.get(key)
        columns["official_code_status"].append(
            "RESOLVED_OFFICIAL" if record is not None else "UNKNOWN_CODE_PAIR"
        )
        columns["official_code_label"].append(
            record.official_label if record is not None else None
        )
        columns["official_legal_reference"].append(
            record.legal_reference if record is not None else None
        )
        columns["official_regulation_reference"].append(
            record.regulation_or_annex_reference if record is not None else None
        )
        columns["official_code_source_url"].append(
            record.official_source_url if record is not None else None
        )
        columns["official_code_profile"].append(profile.profile)
        columns["official_code_profile_sha256"].append(profile_hash)
    for column in OFFICIAL_CODE_COLUMNS:
        values = np.empty(len(output), dtype=object)
        values[:] = columns[column]
        output[column] = values
    return output


def _catalog_by_id(
    catalogs: Sequence[gpd.GeoDataFrame],
) -> dict[str, dict[str, object]]:
    records: dict[str, dict[str, object]] = {}
    for catalog in catalogs:
        for row in catalog.to_dict("records"):
            identifier = str(row["planning_feature_id"])
            if identifier in records:
                raise PlanningFeatureCodeError(
                    "Planning feature IDs must be unique across feature catalogs"
                )
            records[identifier] = row
    return records


def _coded_relations(
    relations: object,
    originals: Sequence[gpd.GeoDataFrame],
    coded: Sequence[gpd.GeoDataFrame],
) -> pd.DataFrame:
    if not isinstance(relations, pd.DataFrame) or isinstance(
        relations, gpd.GeoDataFrame
    ):
        raise PlanningFeatureCodeError("Planning-feature relations must be a DataFrame")
    if relations.columns.duplicated().any():
        raise PlanningFeatureCodeError(
            "Planning-feature relations contain duplicate columns"
        )
    missing = {
        "parcel_id",
        "planning_feature_id",
        "relation_type",
        *_RELATION_MATCH_COLUMNS,
    }.difference(relations.columns)
    if missing:
        raise PlanningFeatureCodeError(
            f"Planning-feature relations lack: {sorted(missing)}"
        )
    collisions = set(OFFICIAL_CODE_COLUMNS).intersection(relations.columns)
    if collisions:
        raise PlanningFeatureCodeError(
            f"Relations already contain official-code columns: {sorted(collisions)}"
        )
    source = _catalog_by_id(originals)
    meanings = _catalog_by_id(coded)
    _validate_exact_string_column(relations, "parcel_id", "planning-feature relations")
    _validate_exact_string_column(
        relations,
        "planning_feature_id",
        "planning-feature relations",
    )
    if relations.duplicated(["parcel_id", "planning_feature_id"]).any():
        raise PlanningFeatureCodeError(
            "Planning-feature relations contain a duplicate parcel/feature pair"
        )
    output = relations.copy(deep=True)
    appended: dict[str, list[object]] = {column: [] for column in OFFICIAL_CODE_COLUMNS}
    for row in relations.to_dict("records"):
        identifier = _strict_string(row["planning_feature_id"], "relation feature ID")
        catalog = source.get(identifier)
        meaning = meanings.get(identifier)
        if catalog is None or meaning is None:
            raise PlanningFeatureCodeError(
                "Relation references an unknown feature catalog ID"
            )
        for column in _RELATION_MATCH_COLUMNS:
            left = row[column]
            right = catalog[column]
            try:
                left_missing = pd.isna(left)
                right_missing = pd.isna(right)
            except (TypeError, ValueError):
                left_missing = right_missing = False
            if (
                isinstance(left_missing, (bool, np.bool_))
                and isinstance(right_missing, (bool, np.bool_))
                and bool(left_missing)
                and bool(right_missing)
            ):
                continue
            comparison = left == right
            if not isinstance(comparison, (bool, np.bool_)) or not bool(comparison):
                raise PlanningFeatureCodeError(
                    f"Relation/catalog {column} differs for {identifier}"
                )
        relation_type = _strict_string(row["relation_type"], "relation type")
        allowed_relation_types = _RELATION_TYPES_BY_GEOMETRY_KIND[
            str(catalog["geometry_kind"])
        ]
        if relation_type not in allowed_relation_types:
            raise PlanningFeatureCodeError(
                f"relation type {relation_type!r} is incompatible with "
                f"{catalog['geometry_kind']} feature {identifier}"
            )
        for column in OFFICIAL_CODE_COLUMNS:
            appended[column].append(meaning[column])
    for column in OFFICIAL_CODE_COLUMNS:
        values = np.empty(len(output), dtype=object)
        values[:] = appended[column]
        output[column] = values
    return output


def _canonical_value(value: object) -> object:
    if isinstance(value, BaseGeometry):
        return to_wkb(value, hex=True, include_srid=False)
    if isinstance(value, (datetime, date, pd.Timestamp)):
        return value.isoformat()
    if isinstance(value, np.generic):
        return _canonical_value(value.item())
    if isinstance(value, Mapping):
        return {str(key): _canonical_value(item) for key, item in value.items()}
    if isinstance(value, (tuple, list, np.ndarray)):
        return [_canonical_value(item) for item in value]
    if value is None or value is pd.NA:
        return None
    try:
        missing = pd.isna(value)
    except (TypeError, ValueError):
        missing = False
    if isinstance(missing, (bool, np.bool_)) and bool(missing):
        return None
    if isinstance(value, bool):
        return value
    if isinstance(value, Integral):
        return int(value)
    if isinstance(value, Real):
        number = float(value)
        if not math.isfinite(number):
            raise PlanningFeatureCodeError(
                "Integrity payload contains non-finite numeric data"
            )
        return number
    if isinstance(value, str):
        return value
    raise PlanningFeatureCodeError(
        f"Integrity payload contains unsupported value {type(value).__name__}"
    )


def _frame_payload(frame: pd.DataFrame) -> dict[str, object]:
    payload: dict[str, object] = {
        "columns": [str(column) for column in frame.columns],
        "dtypes": [str(dtype) for dtype in frame.dtypes],
        "index_names": [
            None if name is None else str(name) for name in frame.index.names
        ],
        "index": [_canonical_value(value) for value in frame.index.tolist()],
        "rows": [
            [_canonical_value(value) for value in row]
            for row in frame.itertuples(index=False, name=None)
        ],
    }
    if isinstance(frame, gpd.GeoDataFrame):
        payload["geometry_column"] = frame.geometry.name
        try:
            payload["crs"] = CRS.from_user_input(frame.crs).to_json_dict()
        except Exception as error:
            raise PlanningFeatureCodeError("Cannot serialize feature CRS") from error
    return payload


def _component_metadata(result: PlanningFeatureCodeResult) -> dict[str, object]:
    return {
        "result_hash_schema_version": result.result_hash_schema_version,
        "profile_schema_version": result.profile_schema_version,
        "profile": result.profile,
        "standard_model": result.standard_model,
        "profile_sha256": result.profile_sha256,
        "source_document_id": result.source_document_id,
        "source_archive_sha256": result.source_archive_sha256,
    }


def _frame_sha256(
    domain: str,
    result: PlanningFeatureCodeResult,
    frame: pd.DataFrame,
) -> str:
    return _canonical_json_sha256(
        {
            "domain": domain,
            **_component_metadata(result),
            "frame": _frame_payload(frame),
        }
    )


def _complete_sha256(result: PlanningFeatureCodeResult) -> str:
    return _canonical_json_sha256(
        {
            "domain": "landscout.cnig_feature_codes.result",
            **_component_metadata(result),
            "code_dictionary_content_sha256": result.code_dictionary_content_sha256,
            "surface_features_content_sha256": result.surface_features_content_sha256,
            "line_features_content_sha256": result.line_features_content_sha256,
            "point_features_content_sha256": result.point_features_content_sha256,
            "relations_content_sha256": result.relations_content_sha256,
        }
    )


def _result_with_hashes(result: PlanningFeatureCodeResult) -> PlanningFeatureCodeResult:
    component = replace(
        result,
        code_dictionary_content_sha256=_frame_sha256(
            "landscout.cnig_feature_codes.dictionary", result, result.code_dictionary
        ),
        surface_features_content_sha256=_frame_sha256(
            "landscout.cnig_feature_codes.surface", result, result.surface_features
        ),
        line_features_content_sha256=_frame_sha256(
            "landscout.cnig_feature_codes.line", result, result.line_features
        ),
        point_features_content_sha256=_frame_sha256(
            "landscout.cnig_feature_codes.point", result, result.point_features
        ),
        relations_content_sha256=_frame_sha256(
            "landscout.cnig_feature_codes.relations", result, result.relations
        ),
    )
    return replace(
        component, complete_result_content_sha256=_complete_sha256(component)
    )


def _build_result(
    planning_document: GpuPlanningDocument,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile,
) -> PlanningFeatureCodeResult:
    standard = _planning_standard(planning_document)
    if standard != code_profile.standard_model:
        raise PlanningFeatureCodeError(
            f"Planning document standard {standard!r} differs from code-profile standard"
        )
    surface = _validate_feature_catalog(
        surface_features,
        "surface",
        "surface feature catalog",
        planning_document,
        standard,
    )
    line = _validate_feature_catalog(
        line_features,
        "line",
        "line feature catalog",
        planning_document,
        standard,
    )
    point = _validate_feature_catalog(
        point_features,
        "point",
        "point feature catalog",
        planning_document,
        standard,
    )
    profile_hash = _profile_sha256(code_profile)
    coded_surface = _coded_catalog(surface, code_profile, profile_hash)
    coded_line = _coded_catalog(line, code_profile, profile_hash)
    coded_point = _coded_catalog(point, code_profile, profile_hash)
    coded_relations = _coded_relations(
        relations,
        (surface, line, point),
        (coded_surface, coded_line, coded_point),
    )
    archive = planning_document.extraction.archive
    result = PlanningFeatureCodeResult(
        result_hash_schema_version=RESULT_HASH_SCHEMA_VERSION,
        profile_schema_version=code_profile.schema_version,
        profile=code_profile.profile,
        standard_model=standard,
        profile_sha256=profile_hash,
        source_document_id=archive.document.document_id,
        source_archive_sha256=archive.sha256,
        code_dictionary_content_sha256="",
        surface_features_content_sha256="",
        line_features_content_sha256="",
        point_features_content_sha256="",
        relations_content_sha256="",
        complete_result_content_sha256="",
        code_dictionary=_dictionary(code_profile, profile_hash),
        surface_features=coded_surface,
        line_features=coded_line,
        point_features=coded_point,
        relations=coded_relations,
    )
    return _result_with_hashes(result)


def _compare_frame(actual: pd.DataFrame, expected: pd.DataFrame, label: str) -> None:
    if _canonical_value(_frame_payload(actual)) != _canonical_value(
        _frame_payload(expected)
    ):
        raise PlanningFeatureCodeError(f"{label} differs from rebuilt source result")


def validate_planning_feature_code_result(
    planning_document: GpuPlanningDocument,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
    result: PlanningFeatureCodeResult,
) -> None:
    """Rebuild and validate a coded result from every factual source input."""

    try:
        if not isinstance(result, PlanningFeatureCodeResult):
            raise PlanningFeatureCodeError("result must be a PlanningFeatureCodeResult")
        for value, expected_version, label in (
            (
                result.result_hash_schema_version,
                RESULT_HASH_SCHEMA_VERSION,
                "result hash schema version",
            ),
            (
                result.profile_schema_version,
                PROFILE_SCHEMA_VERSION,
                "profile schema version",
            ),
        ):
            if type(value) is not int or value != expected_version:
                raise PlanningFeatureCodeError(f"unsupported {label}: {value!r}")
        expected = _build_result(
            planning_document,
            surface_features,
            line_features,
            point_features,
            relations,
            _resolved_profile(code_profile),
        )
        scalar_fields = (
            "result_hash_schema_version",
            "profile_schema_version",
            "profile",
            "standard_model",
            "profile_sha256",
            "source_document_id",
            "source_archive_sha256",
            "code_dictionary_content_sha256",
            "surface_features_content_sha256",
            "line_features_content_sha256",
            "point_features_content_sha256",
            "relations_content_sha256",
            "complete_result_content_sha256",
        )
        for field in scalar_fields:
            if getattr(result, field) != getattr(expected, field):
                raise PlanningFeatureCodeError(
                    f"result {field} differs from rebuilt source result"
                )
        for actual, rebuilt, label in (
            (result.code_dictionary, expected.code_dictionary, "code dictionary"),
            (result.surface_features, expected.surface_features, "surface features"),
            (result.line_features, expected.line_features, "line features"),
            (result.point_features, expected.point_features, "point features"),
            (result.relations, expected.relations, "coded relations"),
        ):
            _compare_frame(actual, rebuilt, label)
    except PlanningFeatureCodeError:
        raise
    except Exception as error:
        raise PlanningFeatureCodeError(
            "Planning-feature code result validation failed safely"
        ) from error


def resolve_planning_feature_codes(
    planning_document: GpuPlanningDocument,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
) -> PlanningFeatureCodeResult:
    """Attach exact official CNIG meanings without interpreting their impact."""

    try:
        profile = _resolved_profile(code_profile)
        result = _build_result(
            planning_document,
            surface_features,
            line_features,
            point_features,
            relations,
            profile,
        )
        validate_planning_feature_code_result(
            planning_document,
            surface_features,
            line_features,
            point_features,
            relations,
            profile,
            result,
        )
        return result
    except PlanningFeatureCodeError:
        raise
    except Exception as error:
        raise PlanningFeatureCodeError(
            "Planning-feature code resolution failed safely"
        ) from error
