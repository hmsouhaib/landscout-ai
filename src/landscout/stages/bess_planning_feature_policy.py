"""Compile a source-locked BESS policy for official CNIG feature-code meanings."""

from __future__ import annotations

import json
import math
import re
from collections.abc import Mapping
from dataclasses import dataclass, replace
from datetime import date, datetime
from hashlib import sha256
from io import BytesIO
from numbers import Integral, Real
from pathlib import Path
from typing import Literal

import geopandas as gpd  # type: ignore[import-untyped]
import numpy as np
import pandas as pd  # type: ignore[import-untyped]
from pydantic import (
    BaseModel,
    ConfigDict,
    StrictBool,
    StrictInt,
    StrictStr,
    field_serializer,
    model_validator,
)

from landscout.common.artifact_paths import validate_portable_parquet_filename
from landscout.common.frame_integrity import deterministic_frame_schema_signature
from landscout.common.immutable_mapping import freeze_mapping
from landscout.common.strict_json import loads_strict_json_object
from landscout.common.strict_yaml import StrictYamlError, loads_strict_yaml
from landscout.sources.gpu_fr import GpuPlanningDocument
from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeResult,
    validate_planning_feature_code_result,
)

__all__ = [
    "BessPlanningFeaturePolicyArtifactManifest",
    "BessPlanningFeaturePolicyConfig",
    "BessPlanningFeaturePolicyError",
    "BessPlanningFeaturePolicyResult",
    "compile_bess_planning_feature_policy",
    "load_bess_planning_feature_policy_artifacts",
    "load_bess_planning_feature_policy_config",
    "validate_bess_planning_feature_policy_result",
    "validate_bess_planning_feature_policy_result_envelope",
]

POLICY_SCHEMA_VERSION = 1
RESULT_HASH_SCHEMA_VERSION = 1
ARTIFACT_MANIFEST_SCHEMA_VERSION = 2
POLICY_SCOPE = "OFFICIAL_CNIG_CODE_MEANING_ONLY"
ARTIFACT_KIND = "BESS_CNIG_FEATURE_POLICY_RESULT"

FeatureFamily = Literal["PRESCRIPTION", "INFORMATION"]
PrecheckStatus = Literal[
    "LIKELY_MATERIAL_CONSTRAINT",
    "MATERIAL_REVIEW_REQUIRED",
    "DESIGN_REVIEW_REQUIRED",
    "CONTEXT_REVIEW_REQUIRED",
    "UNKNOWN",
]
Confidence = Literal["HIGH", "MEDIUM", "LOW"]

ALLOWED_STATUSES = frozenset(
    {
        "LIKELY_MATERIAL_CONSTRAINT",
        "MATERIAL_REVIEW_REQUIRED",
        "DESIGN_REVIEW_REQUIRED",
        "CONTEXT_REVIEW_REQUIRED",
        "UNKNOWN",
    }
)
ALLOWED_CONFIDENCES = frozenset({"HIGH", "MEDIUM", "LOW"})
CODE_PATTERN = re.compile(r"[0-9]{2}")
SHA_PATTERN = re.compile(r"[0-9a-f]{64}")

POLICY_TABLE_COLUMNS = (
    "feature_family",
    "type_code",
    "subtype_code",
    "official_label",
    "official_legal_reference",
    "official_regulation_reference",
    "precheck_status",
    "confidence",
    "status_priority",
    "rationale",
    "required_human_action",
    "limitations",
    "policy_scope",
    "local_feature_text_interpreted",
    "local_regulation_content_interpreted",
    "legal_conclusion_produced",
    "policy_profile",
    "policy_sha256",
    "cnig_profile",
    "cnig_profile_sha256",
    "cnig_complete_result_content_sha256",
)
POLICY_TABLE_DTYPES = tuple(
    "int64"
    if column == "status_priority"
    else "bool"
    if column
    in {
        "local_feature_text_interpreted",
        "local_regulation_content_interpreted",
        "legal_conclusion_produced",
    }
    else "str"
    for column in POLICY_TABLE_COLUMNS
)
POLICY_TABLE_SCHEMA_SIGNATURE: dict[str, object] = {
    "columns": list(POLICY_TABLE_COLUMNS),
    "dtypes": list(POLICY_TABLE_DTYPES),
    "index_class": "pandas.Index",
    "index_names": [None],
    "index_level_dtypes": ["int64"],
}
NULL_REFERENCE_LITERALS = frozenset({"None", "nan", "<NA>"})
POLICY_RESULT_SCALAR_FIELDS = (
    "policy_schema_version",
    "result_hash_schema_version",
    "policy_profile",
    "policy_scope",
    "policy_sha256",
    "source_document_id",
    "source_archive_sha256",
    "cnig_profile",
    "cnig_profile_schema_version",
    "cnig_profile_sha256",
    "cnig_result_hash_schema_version",
    "cnig_complete_result_content_sha256",
    "policy_table_content_sha256",
    "complete_result_content_sha256",
)


class BessPlanningFeaturePolicyError(ValueError):
    """Raised when the official-code BESS policy cannot be proven exact."""


class _StrictPolicyModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class PolicyTableSchemaSignature(_StrictPolicyModel):
    """Immutable persisted schema identity for the normalized policy table."""

    columns: tuple[StrictStr, ...]
    dtypes: tuple[StrictStr, ...]
    index_class: StrictStr
    index_names: tuple[StrictStr | None, ...]
    index_level_dtypes: tuple[StrictStr, ...]


def _exact_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise ValueError(
            f"{label} must be an exact non-empty string without edge whitespace"
        )
    return value


def _optional_exact_string(value: object, label: str) -> str | None:
    if value is None:
        return None
    return _exact_string(value, label)


def _sha256_string(value: object, label: str) -> str:
    text = _exact_string(value, label)
    if SHA_PATTERN.fullmatch(text) is None:
        raise ValueError(f"{label} must be a lowercase SHA256")
    return text


class PolicySourceLock(_StrictPolicyModel):
    document_id: StrictStr
    archive_sha256: StrictStr
    cnig_profile: StrictStr
    cnig_profile_schema_version: StrictInt
    cnig_profile_sha256: StrictStr
    cnig_result_hash_schema_version: StrictInt
    cnig_complete_result_content_sha256: StrictStr

    @model_validator(mode="after")
    def _validate_lock(self) -> PolicySourceLock:
        _exact_string(self.document_id, "document_id")
        _sha256_string(self.archive_sha256, "archive_sha256")
        _exact_string(self.cnig_profile, "cnig_profile")
        _sha256_string(self.cnig_profile_sha256, "cnig_profile_sha256")
        _sha256_string(
            self.cnig_complete_result_content_sha256,
            "cnig_complete_result_content_sha256",
        )
        for value, label in (
            (self.cnig_profile_schema_version, "cnig_profile_schema_version"),
            (self.cnig_result_hash_schema_version, "cnig_result_hash_schema_version"),
        ):
            if type(value) is not int or value < 1:
                raise ValueError(f"{label} must be a strict positive integer")
        return self


class PolicyEntry(_StrictPolicyModel):
    feature_family: FeatureFamily
    type_code: StrictStr
    subtype_code: StrictStr
    expected_official_label: StrictStr
    expected_legal_reference: StrictStr | None
    expected_regulation_reference: StrictStr | None
    precheck_status: PrecheckStatus
    confidence: Confidence
    rationale: StrictStr
    required_human_action: StrictStr
    limitations: StrictStr

    @model_validator(mode="after")
    def _validate_entry(self) -> PolicyEntry:
        if CODE_PATTERN.fullmatch(self.type_code) is None:
            raise ValueError("type_code must be an exact two-character digit string")
        if CODE_PATTERN.fullmatch(self.subtype_code) is None:
            raise ValueError("subtype_code must be an exact two-character digit string")
        _exact_string(self.expected_official_label, "expected_official_label")
        _optional_exact_string(
            self.expected_legal_reference, "expected_legal_reference"
        )
        _optional_exact_string(
            self.expected_regulation_reference,
            "expected_regulation_reference",
        )
        _exact_string(self.rationale, "rationale")
        _exact_string(self.required_human_action, "required_human_action")
        _exact_string(self.limitations, "limitations")
        return self


def _canonical_json_sha256(value: object) -> str:
    try:
        encoded = json.dumps(
            value,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    except (TypeError, ValueError) as error:
        raise BessPlanningFeaturePolicyError(
            "Policy integrity payload is not canonical JSON"
        ) from error
    return sha256(encoded).hexdigest()


def _policy_entries_sha256(entries: tuple[PolicyEntry, ...]) -> str:
    return _canonical_json_sha256([entry.model_dump(mode="json") for entry in entries])


class BessPlanningFeaturePolicyConfig(_StrictPolicyModel):
    schema_version: StrictInt
    profile: StrictStr
    policy_scope: Literal["OFFICIAL_CNIG_CODE_MEANING_ONLY"]
    local_feature_text_interpreted: StrictBool
    local_regulation_content_interpreted: StrictBool
    legal_conclusion_produced: StrictBool
    source_lock: PolicySourceLock
    status_priority: Mapping[PrecheckStatus, StrictInt]
    canonical_policy_entries_sha256: StrictStr
    entries: tuple[PolicyEntry, ...]

    @field_serializer("status_priority")
    def _serialize_status_priority(
        self, value: Mapping[PrecheckStatus, int]
    ) -> dict[PrecheckStatus, int]:
        return dict(value)

    @model_validator(mode="after")
    def _validate_policy(self) -> BessPlanningFeaturePolicyConfig:
        if (
            type(self.schema_version) is not int
            or self.schema_version != POLICY_SCHEMA_VERSION
        ):
            raise ValueError(
                f"policy schema version must equal {POLICY_SCHEMA_VERSION}"
            )
        _exact_string(self.profile, "profile")
        if self.policy_scope != POLICY_SCOPE:
            raise ValueError("policy_scope is unsupported")
        if (
            self.local_feature_text_interpreted is not False
            or self.local_regulation_content_interpreted is not False
            or self.legal_conclusion_produced is not False
        ):
            raise ValueError(
                "policy interpretation and legal-conclusion flags must be false"
            )
        if set(self.status_priority) != ALLOWED_STATUSES:
            raise ValueError(
                "status priority must contain every allowed status exactly once"
            )
        priorities = list(self.status_priority.values())
        if any(type(value) is not int or value <= 0 for value in priorities):
            raise ValueError("status priority values must be strict positive integers")
        if len(set(priorities)) != len(priorities):
            raise ValueError("status priority values must be unique")
        keys = [
            (entry.feature_family, entry.type_code, entry.subtype_code)
            for entry in self.entries
        ]
        if len(keys) != len(set(keys)):
            raise ValueError(
                "policy entries contain a duplicate family/type/subtype pair"
            )
        if keys != sorted(keys):
            raise ValueError(
                "policy entries must use deterministic family/type/subtype order"
            )
        _sha256_string(
            self.canonical_policy_entries_sha256,
            "canonical_policy_entries_sha256",
        )
        if _policy_entries_sha256(self.entries) != self.canonical_policy_entries_sha256:
            raise ValueError(
                "canonical policy-entry SHA256 differs from policy entries"
            )
        object.__setattr__(
            self, "status_priority", freeze_mapping(self.status_priority)
        )
        return self


def load_bess_planning_feature_policy_config(
    path: str | Path,
) -> BessPlanningFeaturePolicyConfig:
    """Load a strict offline BESS policy for official CNIG feature-code pairs."""

    try:
        payload = loads_strict_yaml(Path(path).read_bytes())
        if not isinstance(payload, Mapping):
            raise BessPlanningFeaturePolicyError("BESS CNIG policy must be a mapping")
        return BessPlanningFeaturePolicyConfig.model_validate(payload)
    except BessPlanningFeaturePolicyError:
        raise
    except StrictYamlError as error:
        raise BessPlanningFeaturePolicyError(str(error)) from error
    except Exception as error:
        raise BessPlanningFeaturePolicyError(
            "BESS CNIG feature policy is invalid"
        ) from error


def _resolved_policy_config(
    config: BessPlanningFeaturePolicyConfig | str | Path,
) -> BessPlanningFeaturePolicyConfig:
    if not isinstance(config, BessPlanningFeaturePolicyConfig):
        return load_bess_planning_feature_policy_config(config)
    try:
        payload = config.model_dump(mode="python", warnings="error")
        return BessPlanningFeaturePolicyConfig.model_validate(payload)
    except Exception as error:
        raise BessPlanningFeaturePolicyError(
            "in-memory BESS planning-feature policy config is invalid"
        ) from error


def _policy_sha256(config: BessPlanningFeaturePolicyConfig) -> str:
    return _canonical_json_sha256(config.model_dump(mode="json"))


@dataclass(frozen=True)
class BessPlanningFeaturePolicyResult:
    """Immutable normalized policy table and its source-complete hash envelope."""

    policy_schema_version: int
    result_hash_schema_version: int
    policy_profile: str
    policy_scope: str
    policy_sha256: str
    source_document_id: str
    source_archive_sha256: str
    cnig_profile: str
    cnig_profile_schema_version: int
    cnig_profile_sha256: str
    cnig_result_hash_schema_version: int
    cnig_complete_result_content_sha256: str
    policy_table_content_sha256: str
    complete_result_content_sha256: str
    policy_table: pd.DataFrame


class BessPlanningFeaturePolicyArtifactManifest(_StrictPolicyModel):
    """Strict physical binding between one policy table and its hash envelope."""

    schema_version: StrictInt
    artifact_kind: Literal["BESS_CNIG_FEATURE_POLICY_RESULT"]
    policy_schema_version: StrictInt
    result_hash_schema_version: StrictInt
    policy_profile: StrictStr
    policy_scope: Literal["OFFICIAL_CNIG_CODE_MEANING_ONLY"]
    policy_sha256: StrictStr
    source_document_id: StrictStr
    source_archive_sha256: StrictStr
    cnig_profile: StrictStr
    cnig_profile_schema_version: StrictInt
    cnig_profile_sha256: StrictStr
    cnig_result_hash_schema_version: StrictInt
    cnig_complete_result_content_sha256: StrictStr
    policy_table_content_sha256: StrictStr
    complete_result_content_sha256: StrictStr
    parquet_filename: StrictStr
    parquet_row_count: StrictInt
    parquet_size_bytes: StrictInt
    parquet_sha256: StrictStr
    policy_table_schema_signature: PolicyTableSchemaSignature

    @model_validator(mode="after")
    def _validate_manifest(self) -> BessPlanningFeaturePolicyArtifactManifest:
        if (
            type(self.schema_version) is not int
            or self.schema_version != ARTIFACT_MANIFEST_SCHEMA_VERSION
        ):
            raise ValueError(
                "artifact manifest schema version must equal "
                f"{ARTIFACT_MANIFEST_SCHEMA_VERSION}"
            )
        if (
            type(self.policy_schema_version) is not int
            or self.policy_schema_version != POLICY_SCHEMA_VERSION
        ):
            raise ValueError("artifact policy schema version is unsupported")
        if (
            type(self.result_hash_schema_version) is not int
            or self.result_hash_schema_version != RESULT_HASH_SCHEMA_VERSION
        ):
            raise ValueError("artifact result hash schema version is unsupported")
        if (
            type(self.cnig_profile_schema_version) is not int
            or self.cnig_profile_schema_version != 2
        ):
            raise ValueError("artifact CNIG profile schema version is unsupported")
        if (
            type(self.cnig_result_hash_schema_version) is not int
            or self.cnig_result_hash_schema_version != 5
        ):
            raise ValueError("artifact CNIG result hash schema version is unsupported")
        for exact_value, label in (
            (self.policy_profile, "policy_profile"),
            (self.source_document_id, "source_document_id"),
            (self.cnig_profile, "cnig_profile"),
        ):
            _exact_string(exact_value, label)
        for hash_value, label in (
            (self.policy_sha256, "policy_sha256"),
            (self.source_archive_sha256, "source_archive_sha256"),
            (self.cnig_profile_sha256, "cnig_profile_sha256"),
            (
                self.cnig_complete_result_content_sha256,
                "cnig_complete_result_content_sha256",
            ),
            (self.policy_table_content_sha256, "policy_table_content_sha256"),
            (self.complete_result_content_sha256, "complete_result_content_sha256"),
            (self.parquet_sha256, "parquet_sha256"),
        ):
            _sha256_string(hash_value, label)
        for integer_value, label, allow_zero in (
            (self.parquet_row_count, "parquet_row_count", True),
            (self.parquet_size_bytes, "parquet_size_bytes", False),
        ):
            minimum = 0 if allow_zero else 1
            if type(integer_value) is not int or integer_value < minimum:
                raise ValueError(f"{label} is invalid")
        validate_portable_parquet_filename(self.parquet_filename, "parquet_filename")
        return self


def _null_value(value: object) -> object:
    if value is None or value is pd.NA:
        return None
    try:
        missing = pd.isna(value)
    except (TypeError, ValueError):
        missing = False
    if isinstance(missing, (bool, np.bool_)) and bool(missing):
        return None
    return value


def _null_safe_equal(left: object, right: object) -> bool:
    normalized_left = _null_value(left)
    normalized_right = _null_value(right)
    if normalized_left is None or normalized_right is None:
        return normalized_left is None and normalized_right is None
    try:
        return bool(normalized_left == normalized_right)
    except (TypeError, ValueError):
        return False


def _canonical_value(value: object) -> object:
    value = _null_value(value)
    if value is None:
        return None
    if isinstance(value, (datetime, date, pd.Timestamp)):
        return value.isoformat()
    if isinstance(value, np.generic):
        return _canonical_value(value.item())
    if isinstance(value, bool):
        return value
    if isinstance(value, Integral):
        return int(value)
    if isinstance(value, Real):
        number = float(value)
        if not math.isfinite(number):
            raise BessPlanningFeaturePolicyError(
                "Policy integrity payload contains non-finite data"
            )
        return number
    if isinstance(value, str):
        return value
    raise BessPlanningFeaturePolicyError(
        f"Policy integrity payload contains unsupported {type(value).__name__}"
    )


def _frame_payload(frame: pd.DataFrame) -> dict[str, object]:
    return {
        "schema": deterministic_frame_schema_signature(frame),
        "index": [_canonical_value(value) for value in frame.index.tolist()],
        "rows": [
            [_canonical_value(value) for value in row]
            for row in frame.itertuples(index=False, name=None)
        ],
    }


def _validate_source_lock(
    config: BessPlanningFeaturePolicyConfig,
    coded_result: PlanningFeatureCodeResult,
) -> None:
    lock = config.source_lock
    comparisons = (
        (lock.document_id, coded_result.source_document_id, "document ID"),
        (lock.archive_sha256, coded_result.source_archive_sha256, "archive SHA256"),
        (lock.cnig_profile, coded_result.profile, "CNIG profile"),
        (
            lock.cnig_profile_schema_version,
            coded_result.profile_schema_version,
            "CNIG profile schema version",
        ),
        (lock.cnig_profile_sha256, coded_result.profile_sha256, "CNIG profile SHA256"),
        (
            lock.cnig_result_hash_schema_version,
            coded_result.result_hash_schema_version,
            "CNIG result hash schema version",
        ),
        (
            lock.cnig_complete_result_content_sha256,
            coded_result.complete_result_content_sha256,
            "CNIG complete result SHA256",
        ),
    )
    for configured, actual, label in comparisons:
        if configured != actual:
            raise BessPlanningFeaturePolicyError(
                f"Policy source lock differs from validated {label}"
            )


def _dictionary_by_pair(
    coded_result: PlanningFeatureCodeResult,
) -> dict[tuple[str, str, str], dict[str, object]]:
    rows = coded_result.code_dictionary.to_dict("records")
    indexed: dict[tuple[str, str, str], dict[str, object]] = {}
    for row in rows:
        key = (
            str(row["feature_family"]),
            str(row["type_code"]),
            str(row["subtype_code"]),
        )
        if key in indexed:
            raise BessPlanningFeaturePolicyError(
                "Validated CNIG code dictionary contains a duplicate pair"
            )
        indexed[key] = row
    return indexed


def _validate_policy_completeness(
    config: BessPlanningFeaturePolicyConfig,
    coded_result: PlanningFeatureCodeResult,
) -> dict[tuple[str, str, str], dict[str, object]]:
    dictionary = _dictionary_by_pair(coded_result)
    entries: dict[tuple[str, str, str], PolicyEntry] = {
        (entry.feature_family, entry.type_code, entry.subtype_code): entry
        for entry in config.entries
    }
    missing = sorted(set(dictionary) - set(entries))
    extra = sorted(set(entries) - set(dictionary))
    if missing:
        raise BessPlanningFeaturePolicyError(
            f"Policy is missing validated CNIG pair(s): {missing}"
        )
    if extra:
        raise BessPlanningFeaturePolicyError(
            f"Policy contains extra CNIG pair(s): {extra}"
        )
    for key, row in dictionary.items():
        entry = entries[key]
        if entry.expected_official_label != row["official_label"]:
            raise BessPlanningFeaturePolicyError(
                f"Policy official label mismatch for pair {key}"
            )
        if not _null_safe_equal(entry.expected_legal_reference, row["legal_reference"]):
            raise BessPlanningFeaturePolicyError(
                f"Policy legal reference mismatch for pair {key}"
            )
        if not _null_safe_equal(
            entry.expected_regulation_reference,
            row["regulation_or_annex_reference"],
        ):
            raise BessPlanningFeaturePolicyError(
                f"Policy regulation reference mismatch for pair {key}"
            )
    return dictionary


def _policy_table(
    config: BessPlanningFeaturePolicyConfig,
    coded_result: PlanningFeatureCodeResult,
    dictionary: dict[tuple[str, str, str], dict[str, object]],
    policy_hash: str,
) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for entry in config.entries:
        key = (entry.feature_family, entry.type_code, entry.subtype_code)
        official = dictionary[key]
        rows.append(
            {
                "feature_family": entry.feature_family,
                "type_code": entry.type_code,
                "subtype_code": entry.subtype_code,
                "official_label": official["official_label"],
                "official_legal_reference": official["legal_reference"],
                "official_regulation_reference": (
                    official["regulation_or_annex_reference"]
                ),
                "precheck_status": entry.precheck_status,
                "confidence": entry.confidence,
                "status_priority": config.status_priority[entry.precheck_status],
                "rationale": entry.rationale,
                "required_human_action": entry.required_human_action,
                "limitations": entry.limitations,
                "policy_scope": config.policy_scope,
                "local_feature_text_interpreted": (
                    config.local_feature_text_interpreted
                ),
                "local_regulation_content_interpreted": (
                    config.local_regulation_content_interpreted
                ),
                "legal_conclusion_produced": config.legal_conclusion_produced,
                "policy_profile": config.profile,
                "policy_sha256": policy_hash,
                "cnig_profile": coded_result.profile,
                "cnig_profile_sha256": coded_result.profile_sha256,
                "cnig_complete_result_content_sha256": (
                    coded_result.complete_result_content_sha256
                ),
            }
        )
    output = pd.DataFrame(rows, columns=POLICY_TABLE_COLUMNS)
    string_columns = tuple(
        column
        for column in POLICY_TABLE_COLUMNS
        if column
        not in {
            "status_priority",
            "local_feature_text_interpreted",
            "local_regulation_content_interpreted",
            "legal_conclusion_produced",
        }
    )
    for column in string_columns:
        output[column] = pd.array(output[column].tolist(), dtype="str")
    output["status_priority"] = output["status_priority"].astype("int64")
    for column in (
        "local_feature_text_interpreted",
        "local_regulation_content_interpreted",
        "legal_conclusion_produced",
    ):
        output[column] = output[column].astype("bool")
    output.index = pd.Index(output.index.to_numpy(copy=True), name=output.index.name)
    return output


def _component_metadata(result: BessPlanningFeaturePolicyResult) -> dict[str, object]:
    return {
        "policy_schema_version": result.policy_schema_version,
        "result_hash_schema_version": result.result_hash_schema_version,
        "policy_profile": result.policy_profile,
        "policy_scope": result.policy_scope,
        "policy_sha256": result.policy_sha256,
        "source_document_id": result.source_document_id,
        "source_archive_sha256": result.source_archive_sha256,
        "cnig_profile": result.cnig_profile,
        "cnig_profile_schema_version": result.cnig_profile_schema_version,
        "cnig_profile_sha256": result.cnig_profile_sha256,
        "cnig_result_hash_schema_version": result.cnig_result_hash_schema_version,
        "cnig_complete_result_content_sha256": (
            result.cnig_complete_result_content_sha256
        ),
    }


def _policy_table_sha256(result: BessPlanningFeaturePolicyResult) -> str:
    return _canonical_json_sha256(
        {
            "domain": "landscout.bess_cnig_feature_policy.table",
            **_component_metadata(result),
            "frame": _frame_payload(result.policy_table),
        }
    )


def _complete_result_sha256(result: BessPlanningFeaturePolicyResult) -> str:
    return _canonical_json_sha256(
        {
            "domain": "landscout.bess_cnig_feature_policy.result",
            **_component_metadata(result),
            "policy_table_content_sha256": result.policy_table_content_sha256,
        }
    )


def _result_with_hashes(
    result: BessPlanningFeaturePolicyResult,
) -> BessPlanningFeaturePolicyResult:
    component = replace(
        result, policy_table_content_sha256=_policy_table_sha256(result)
    )
    return replace(
        component,
        complete_result_content_sha256=_complete_result_sha256(component),
    )


def _validate_policy_table_rows(result: BessPlanningFeaturePolicyResult) -> None:
    records: dict[tuple[str, str, str], dict[str, object]] = {}
    ordered_keys: list[tuple[str, str, str]] = []
    priority_to_status: dict[int, str] = {}
    status_to_priority: dict[str, int] = {}
    for position, row in enumerate(result.policy_table.to_dict("records")):
        family = row["feature_family"]
        type_code = row["type_code"]
        subtype_code = row["subtype_code"]
        if family not in {"PRESCRIPTION", "INFORMATION"}:
            raise BessPlanningFeaturePolicyError(
                f"policy table row {position} feature family is invalid"
            )
        for value, label in (
            (type_code, "type code"),
            (subtype_code, "subtype code"),
        ):
            if not isinstance(value, str) or CODE_PATTERN.fullmatch(value) is None:
                raise BessPlanningFeaturePolicyError(
                    f"policy table row {position} {label} is invalid"
                )
        key = (family, type_code, subtype_code)
        if key in records:
            raise BessPlanningFeaturePolicyError(
                "policy table contains a duplicate code pair"
            )
        for field, label in (
            ("official_label", "official label"),
            ("rationale", "rationale"),
            ("required_human_action", "required human action"),
            ("limitations", "limitations"),
        ):
            try:
                _exact_string(row[field], f"policy row {position} {label}")
            except ValueError as error:
                raise BessPlanningFeaturePolicyError(str(error)) from error
        for field in (
            "official_legal_reference",
            "official_regulation_reference",
        ):
            value = row[field]
            if _null_value(value) is None:
                continue
            if isinstance(value, str) and value in NULL_REFERENCE_LITERALS:
                raise BessPlanningFeaturePolicyError(
                    f"{field} contains a literal null replacement"
                )
            try:
                _exact_string(value, f"policy row {position} {field}")
            except ValueError as error:
                raise BessPlanningFeaturePolicyError(str(error)) from error
        status = row["precheck_status"]
        confidence = row["confidence"]
        priority = row["status_priority"]
        if status not in ALLOWED_STATUSES:
            raise BessPlanningFeaturePolicyError(
                f"policy table row {position} status is invalid"
            )
        if confidence not in ALLOWED_CONFIDENCES:
            raise BessPlanningFeaturePolicyError(
                f"policy table row {position} confidence is invalid"
            )
        if type(priority) is not int or priority <= 0:
            raise BessPlanningFeaturePolicyError(
                f"policy table row {position} priority is invalid"
            )
        previous_status = priority_to_status.setdefault(priority, status)
        previous_priority = status_to_priority.setdefault(status, priority)
        if previous_status != status or previous_priority != priority:
            raise BessPlanningFeaturePolicyError(
                "policy table status and priority mapping is not one-to-one"
            )
        if row["policy_scope"] != result.policy_scope:
            raise BessPlanningFeaturePolicyError(
                f"policy table row {position} scope differs from result"
            )
        for field in (
            "local_feature_text_interpreted",
            "local_regulation_content_interpreted",
            "legal_conclusion_produced",
        ):
            if row[field] is not False:
                raise BessPlanningFeaturePolicyError(
                    f"policy table row {position} {field} must be false"
                )
        if (
            row["policy_profile"] != result.policy_profile
            or row["policy_sha256"] != result.policy_sha256
            or row["cnig_profile"] != result.cnig_profile
            or row["cnig_profile_sha256"] != result.cnig_profile_sha256
            or row["cnig_complete_result_content_sha256"]
            != result.cnig_complete_result_content_sha256
        ):
            raise BessPlanningFeaturePolicyError(
                f"policy table row {position} result lineage differs"
            )
        records[key] = row
        ordered_keys.append(key)
    if ordered_keys != sorted(ordered_keys):
        raise BessPlanningFeaturePolicyError("policy table pair order is not canonical")


def _build_result(
    config: BessPlanningFeaturePolicyConfig,
    coded_result: PlanningFeatureCodeResult,
) -> BessPlanningFeaturePolicyResult:
    dictionary = _validate_policy_completeness(config, coded_result)
    policy_hash = _policy_sha256(config)
    result = BessPlanningFeaturePolicyResult(
        policy_schema_version=config.schema_version,
        result_hash_schema_version=RESULT_HASH_SCHEMA_VERSION,
        policy_profile=config.profile,
        policy_scope=config.policy_scope,
        policy_sha256=policy_hash,
        source_document_id=coded_result.source_document_id,
        source_archive_sha256=coded_result.source_archive_sha256,
        cnig_profile=coded_result.profile,
        cnig_profile_schema_version=coded_result.profile_schema_version,
        cnig_profile_sha256=coded_result.profile_sha256,
        cnig_result_hash_schema_version=coded_result.result_hash_schema_version,
        cnig_complete_result_content_sha256=(
            coded_result.complete_result_content_sha256
        ),
        policy_table_content_sha256="",
        complete_result_content_sha256="",
        policy_table=_policy_table(config, coded_result, dictionary, policy_hash),
    )
    return _result_with_hashes(result)


def _validate_result_envelope(result: BessPlanningFeaturePolicyResult) -> None:
    if type(result) is not BessPlanningFeaturePolicyResult:
        raise BessPlanningFeaturePolicyError(
            "result must be a BessPlanningFeaturePolicyResult"
        )
    for version, expected, label in (
        (result.policy_schema_version, POLICY_SCHEMA_VERSION, "policy schema"),
        (
            result.result_hash_schema_version,
            RESULT_HASH_SCHEMA_VERSION,
            "result hash schema",
        ),
        (result.cnig_profile_schema_version, 2, "CNIG profile schema"),
        (result.cnig_result_hash_schema_version, 5, "CNIG result hash schema"),
    ):
        if type(version) is not int or version != expected:
            raise BessPlanningFeaturePolicyError(f"unsupported {label} version")
    if result.policy_scope != POLICY_SCOPE:
        raise BessPlanningFeaturePolicyError("result policy scope is invalid")
    for value, label in (
        (result.policy_profile, "policy profile"),
        (result.source_document_id, "source document ID"),
        (result.cnig_profile, "CNIG profile"),
    ):
        try:
            _exact_string(value, label)
        except ValueError as error:
            raise BessPlanningFeaturePolicyError(str(error)) from error
    if not isinstance(result.policy_table, pd.DataFrame) or isinstance(
        result.policy_table, gpd.GeoDataFrame
    ):
        raise BessPlanningFeaturePolicyError("policy table must be a DataFrame")
    if (
        result.policy_table.columns.duplicated().any()
        or tuple(result.policy_table.columns) != POLICY_TABLE_COLUMNS
    ):
        raise BessPlanningFeaturePolicyError("policy table schema is invalid")
    if (
        deterministic_frame_schema_signature(result.policy_table)
        != POLICY_TABLE_SCHEMA_SIGNATURE
    ):
        raise BessPlanningFeaturePolicyError("policy table schema is invalid")
    if result.policy_table.empty:
        raise BessPlanningFeaturePolicyError(
            "policy table must contain at least one policy entry"
        )
    for field in POLICY_RESULT_SCALAR_FIELDS:
        if not field.endswith("_sha256"):
            continue
        try:
            _sha256_string(getattr(result, field), field)
        except ValueError as error:
            raise BessPlanningFeaturePolicyError(str(error)) from error
    _validate_policy_table_rows(result)
    rebuilt = _result_with_hashes(result)
    if result.policy_table_content_sha256 != rebuilt.policy_table_content_sha256:
        raise BessPlanningFeaturePolicyError("policy table hash is invalid")
    if result.complete_result_content_sha256 != rebuilt.complete_result_content_sha256:
        raise BessPlanningFeaturePolicyError("complete result hash is invalid")


def validate_bess_planning_feature_policy_result_envelope(
    result: BessPlanningFeaturePolicyResult,
) -> None:
    """Validate one compiled-policy envelope without rebuilding CNIG sources."""

    try:
        _validate_result_envelope(result)
    except BessPlanningFeaturePolicyError:
        raise
    except Exception as error:
        raise BessPlanningFeaturePolicyError(
            "BESS planning-feature policy result envelope is invalid"
        ) from error


def load_bess_planning_feature_policy_artifacts(
    parquet_path: str | Path,
    manifest_path: str | Path,
) -> BessPlanningFeaturePolicyResult:
    """Load and locally validate one physically sealed compiled-policy artifact."""

    try:
        parquet = Path(parquet_path)
        manifest_file = Path(manifest_path)
        payload = loads_strict_json_object(manifest_file.read_bytes())
        manifest = BessPlanningFeaturePolicyArtifactManifest.model_validate(payload)
        if manifest.parquet_filename != parquet.name:
            raise BessPlanningFeaturePolicyError(
                "Artifact manifest Parquet filename differs from the supplied file"
            )
        parquet_payload = parquet.read_bytes()
        if len(parquet_payload) != manifest.parquet_size_bytes:
            raise BessPlanningFeaturePolicyError(
                "Artifact manifest Parquet size differs from the supplied file"
            )
        if sha256(parquet_payload).hexdigest() != manifest.parquet_sha256:
            raise BessPlanningFeaturePolicyError(
                "Artifact manifest Parquet SHA256 differs from the supplied file"
            )
        table = pd.read_parquet(BytesIO(parquet_payload))
        if len(table) != manifest.parquet_row_count:
            raise BessPlanningFeaturePolicyError(
                "Artifact manifest Parquet row count differs from the supplied file"
            )
        actual_schema = deterministic_frame_schema_signature(table)
        declared_schema = manifest.policy_table_schema_signature.model_dump(mode="json")
        if actual_schema != declared_schema:
            raise BessPlanningFeaturePolicyError(
                "Artifact manifest policy-table schema differs from the supplied file"
            )
        result = BessPlanningFeaturePolicyResult(
            **{name: getattr(manifest, name) for name in POLICY_RESULT_SCALAR_FIELDS},
            policy_table=table,
        )
        _validate_result_envelope(result)
        return result
    except BessPlanningFeaturePolicyError:
        raise
    except Exception as error:
        raise BessPlanningFeaturePolicyError(
            f"BESS CNIG feature policy artifacts are invalid: {error}"
        ) from error


def _validate_coded_source(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
    coded_result: PlanningFeatureCodeResult,
) -> None:
    try:
        validate_planning_feature_code_result(
            planning_document,
            parcels,
            surface_features,
            line_features,
            point_features,
            relations,
            code_profile,
            coded_result,
        )
    except Exception as error:
        raise BessPlanningFeaturePolicyError(
            "Source-complete CNIG result validation failed"
        ) from error


def compile_bess_planning_feature_policy(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
    coded_result: PlanningFeatureCodeResult,
    policy_config: BessPlanningFeaturePolicyConfig | str | Path,
) -> BessPlanningFeaturePolicyResult:
    """Compile the exact source-locked policy without applying it to features."""

    try:
        config = _resolved_policy_config(policy_config)
        _validate_source_lock(config, coded_result)
        _validate_coded_source(
            planning_document,
            parcels,
            surface_features,
            line_features,
            point_features,
            relations,
            code_profile,
            coded_result,
        )
        result = _build_result(config, coded_result)
        _validate_result_envelope(result)
        return result
    except BessPlanningFeaturePolicyError:
        raise
    except Exception as error:
        raise BessPlanningFeaturePolicyError(
            "BESS CNIG feature policy compilation failed safely"
        ) from error


def validate_bess_planning_feature_policy_result(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
    coded_result: PlanningFeatureCodeResult,
    policy_config: BessPlanningFeaturePolicyConfig | str | Path,
    result: BessPlanningFeaturePolicyResult,
) -> None:
    """Rebuild and validate a normalized policy from every factual source input."""

    try:
        _validate_result_envelope(result)
        config = _resolved_policy_config(policy_config)
        _validate_source_lock(config, coded_result)
        _validate_coded_source(
            planning_document,
            parcels,
            surface_features,
            line_features,
            point_features,
            relations,
            code_profile,
            coded_result,
        )
        expected = _build_result(config, coded_result)
        for field in POLICY_RESULT_SCALAR_FIELDS:
            if getattr(result, field) != getattr(expected, field):
                raise BessPlanningFeaturePolicyError(
                    f"result {field} differs from rebuilt policy"
                )
        if _frame_payload(result.policy_table) != _frame_payload(expected.policy_table):
            raise BessPlanningFeaturePolicyError(
                "policy table differs from rebuilt policy"
            )
    except BessPlanningFeaturePolicyError:
        raise
    except Exception as error:
        raise BessPlanningFeaturePolicyError(
            "BESS CNIG feature policy result validation failed safely"
        ) from error
