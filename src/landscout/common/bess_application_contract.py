"""Internal intrinsic contracts for BESS CNIG application rows."""

from __future__ import annotations

import math
import re
from numbers import Integral
from pathlib import PurePosixPath, PureWindowsPath
from typing import Literal

import pandas as pd  # type: ignore[import-untyped]

APPLICATION_SCOPE = "FEATURE_AND_RELATION_POLICY_PROPAGATION_ONLY"
POLICY_SCOPE = "OFFICIAL_CNIG_CODE_MEANING_ONLY"

ApplicationStatus = Literal["APPLIED_EXACT_POLICY", "UNRESOLVED_CODE_PAIR"]

POLICY_COLUMNS = (
    "bess_cnig_policy_application_status",
    "bess_cnig_precheck_status",
    "bess_cnig_precheck_confidence",
    "bess_cnig_status_priority",
    "bess_cnig_rationale",
    "bess_cnig_required_human_action",
    "bess_cnig_limitations",
    "bess_cnig_application_scope",
    "bess_cnig_policy_scope",
    "bess_cnig_local_feature_text_interpreted",
    "bess_cnig_local_regulation_content_interpreted",
    "bess_cnig_legal_conclusion_produced",
    "bess_cnig_parcel_status_aggregated",
    "bess_cnig_parcel_rejection_performed",
    "bess_cnig_score_calculated",
    "bess_cnig_policy_profile",
    "bess_cnig_policy_sha256",
    "bess_cnig_policy_result_sha256",
)
DECISION_COLUMNS = (
    "bess_cnig_precheck_status",
    "bess_cnig_precheck_confidence",
    "bess_cnig_status_priority",
    "bess_cnig_rationale",
    "bess_cnig_required_human_action",
    "bess_cnig_limitations",
)
FLAG_COLUMNS = (
    "bess_cnig_local_feature_text_interpreted",
    "bess_cnig_local_regulation_content_interpreted",
    "bess_cnig_legal_conclusion_produced",
    "bess_cnig_parcel_status_aggregated",
    "bess_cnig_parcel_rejection_performed",
    "bess_cnig_score_calculated",
)
STRING_POLICY_COLUMNS = tuple(
    column
    for column in POLICY_COLUMNS
    if column not in {"bess_cnig_status_priority", *FLAG_COLUMNS}
)
POLICY_SUFFIX_DTYPES = {
    **{column: "str" for column in STRING_POLICY_COLUMNS},
    "bess_cnig_status_priority": "Int64",
    **{column: "bool" for column in FLAG_COLUMNS},
}
ALLOWED_PRECHECK_STATUSES = frozenset(
    {
        "LIKELY_MATERIAL_CONSTRAINT",
        "MATERIAL_REVIEW_REQUIRED",
        "DESIGN_REVIEW_REQUIRED",
        "CONTEXT_REVIEW_REQUIRED",
        "UNKNOWN",
    }
)
ALLOWED_CONFIDENCES = frozenset({"HIGH", "MEDIUM", "LOW"})
ALLOWED_FEATURE_FAMILIES = frozenset({"PRESCRIPTION", "INFORMATION"})
ALLOWED_RELATION_TYPES = frozenset(
    {
        "AREA_OVERLAP",
        "LENGTH_OVERLAP",
        "INSIDE",
        "TOUCH_ONLY",
        "BOUNDARY_TOUCH",
    }
)
NULL_LITERALS = frozenset({"None", "nan", "<NA>"})
CODE_PATTERN = re.compile(r"[0-9]{2}")


def _null_value(value: object) -> object:
    if value is None or value is pd.NA:
        return None
    if isinstance(value, float) and math.isnan(value):
        return None
    return value


def _exact_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise ValueError(f"{label} must be an exact non-empty string")
    return value


def validate_bess_application_policy_frame(
    frame: pd.DataFrame,
    *,
    label: str,
    policy_profile: str,
    policy_sha256: str,
    policy_result_sha256: str,
) -> None:
    """Validate the complete canonical application suffix and every row."""

    if not isinstance(frame, pd.DataFrame):
        raise TypeError(f"{label} must be a DataFrame")
    if frame.columns.duplicated().any():
        raise ValueError(f"{label} contains duplicate columns")
    if tuple(frame.columns[-len(POLICY_COLUMNS) :]) != POLICY_COLUMNS:
        raise ValueError(f"{label} policy schema is invalid")
    for column, expected_dtype in POLICY_SUFFIX_DTYPES.items():
        if str(frame[column].dtype) != expected_dtype:
            raise ValueError(f"{label} policy dtype is invalid for {column}")
    required = {
        "feature_family",
        "type_code_raw",
        "subtype_code_raw",
        "official_code_status",
        *POLICY_COLUMNS,
    }
    if not required.issubset(frame.columns):
        raise ValueError(f"{label} application identity schema is incomplete")
    for row in frame.to_dict("records"):
        if row["feature_family"] not in ALLOWED_FEATURE_FAMILIES:
            raise ValueError(f"{label} feature family is invalid")
        for column in ("type_code_raw", "subtype_code_raw"):
            value = row[column]
            if not isinstance(value, str) or CODE_PATTERN.fullmatch(value) is None:
                raise ValueError(f"{label} {column} is not an exact two-digit code")
        application_status = row["bess_cnig_policy_application_status"]
        official_status = row["official_code_status"]
        if application_status == "APPLIED_EXACT_POLICY":
            if official_status != "RESOLVED_OFFICIAL":
                raise ValueError(
                    f"{label} official status contradicts its application status"
                )
            if any(_null_value(row[column]) is None for column in DECISION_COLUMNS):
                raise ValueError(f"{label} applied policy row has a missing decision")
            if row["bess_cnig_precheck_status"] not in ALLOWED_PRECHECK_STATUSES:
                raise ValueError(f"{label} precheck status is outside the domain")
            if row["bess_cnig_precheck_confidence"] not in ALLOWED_CONFIDENCES:
                raise ValueError(f"{label} confidence is outside the domain")
            priority = row["bess_cnig_status_priority"]
            if (
                isinstance(priority, bool)
                or not isinstance(priority, Integral)
                or int(priority) <= 0
            ):
                raise ValueError(f"{label} priority must be a positive integer")
            for column in (
                "bess_cnig_rationale",
                "bess_cnig_required_human_action",
                "bess_cnig_limitations",
            ):
                _exact_string(row[column], f"{label} {column}")
        elif application_status == "UNRESOLVED_CODE_PAIR":
            if official_status != "UNKNOWN_CODE_PAIR":
                raise ValueError(
                    f"{label} official status contradicts its application status"
                )
            if any(_null_value(row[column]) is not None for column in DECISION_COLUMNS):
                raise ValueError(f"{label} unresolved row has an invented decision")
        else:
            raise ValueError(f"{label} application status is invalid")
        for column in STRING_POLICY_COLUMNS:
            value = row[column]
            if isinstance(value, str) and value in NULL_LITERALS:
                raise ValueError(
                    f"{label} contains a literal missing-value replacement"
                )
        if row["bess_cnig_application_scope"] != APPLICATION_SCOPE:
            raise ValueError(f"{label} application scope is invalid")
        if row["bess_cnig_policy_scope"] != POLICY_SCOPE:
            raise ValueError(f"{label} policy scope is invalid")
        if any(row[column] is not False for column in FLAG_COLUMNS):
            raise ValueError(f"{label} boundary flags must be false")
        for actual, expected, lineage_label in (
            (row["bess_cnig_policy_profile"], policy_profile, "policy profile"),
            (row["bess_cnig_policy_sha256"], policy_sha256, "policy SHA256"),
            (
                row["bess_cnig_policy_result_sha256"],
                policy_result_sha256,
                "policy result SHA256",
            ),
        ):
            if actual != expected:
                raise ValueError(f"{label} {lineage_label} lineage is invalid")


def _relation_identity_string(value: object, label: str) -> str:
    exact = _exact_string(value, label)
    if exact in NULL_LITERALS:
        raise ValueError(f"{label} must not be a textual null sentinel")
    return exact


def validate_bess_application_relation_frame(
    frame: pd.DataFrame,
    *,
    label: str,
    policy_profile: str,
    policy_sha256: str,
    policy_result_sha256: str,
) -> None:
    """Validate canonical application rows and the complete relation identity."""

    validate_bess_application_policy_frame(
        frame,
        label=label,
        policy_profile=policy_profile,
        policy_sha256=policy_sha256,
        policy_result_sha256=policy_result_sha256,
    )
    required = {"parcel_id", "planning_feature_id", "relation_type"}
    if not required.issubset(frame.columns):
        raise ValueError(f"{label} relation identity schema is incomplete")
    for row in frame.to_dict("records"):
        _relation_identity_string(row["parcel_id"], f"{label} parcel identity")
        feature_id = _relation_identity_string(
            row["planning_feature_id"], f"{label} Feature ID identity"
        )
        if (
            PurePosixPath(feature_id).is_absolute()
            or PureWindowsPath(feature_id).is_absolute()
        ):
            raise ValueError(
                f"{label} Feature ID identity must not be an absolute path"
            )
        relation_type = row["relation_type"]
        if (
            not isinstance(relation_type, str)
            or relation_type not in ALLOWED_RELATION_TYPES
        ):
            raise ValueError(f"{label} relation type is invalid")
    if frame.duplicated(["parcel_id", "planning_feature_id"]).any():
        raise ValueError(f"{label} contains a duplicate parcel/feature relation pair")

    priority_to_status: dict[int, set[str]] = {}
    status_to_priority: dict[str, set[int]] = {}
    applied = frame[
        frame["bess_cnig_policy_application_status"] == "APPLIED_EXACT_POLICY"
    ]
    for row in applied.to_dict("records"):
        priority = int(row["bess_cnig_status_priority"])
        status = str(row["bess_cnig_precheck_status"])
        priority_to_status.setdefault(priority, set()).add(status)
        status_to_priority.setdefault(status, set()).add(priority)
    if any(len(statuses) != 1 for statuses in priority_to_status.values()) or any(
        len(priorities) != 1 for priorities in status_to_priority.values()
    ):
        raise ValueError(
            f"{label} document-wide status/priority mapping is not one-to-one"
        )
