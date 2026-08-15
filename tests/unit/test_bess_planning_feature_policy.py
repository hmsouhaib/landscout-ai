from __future__ import annotations

import importlib
import json
import tomllib
from dataclasses import fields, replace
from hashlib import sha256
from io import BytesIO
from pathlib import Path

import pandas as pd
import pytest
from pandas.testing import assert_frame_equal
from pydantic import ValidationError
from test_resolve_planning_feature_codes import _integration_inputs

from landscout import stages
from landscout.common.artifact_paths import validate_portable_parquet_filename
from landscout.common.frame_integrity import deterministic_frame_schema_signature
from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyError,
    BessPlanningFeaturePolicyResult,
    compile_bess_planning_feature_policy,
    load_bess_planning_feature_policy_config,
    validate_bess_planning_feature_policy_result,
)
from landscout.stages.resolve_planning_feature_codes import (
    load_cnig_feature_code_profile,
    resolve_planning_feature_codes,
)

POLICY_PATH = Path("configs/planning/muret_bess_cnig_feature_policy.yaml")
POLICY_SCOPE = "OFFICIAL_CNIG_CODE_MEANING_ONLY"
STATUS_PRIORITIES = {
    "LIKELY_MATERIAL_CONSTRAINT": 50,
    "UNKNOWN": 40,
    "MATERIAL_REVIEW_REQUIRED": 30,
    "DESIGN_REVIEW_REQUIRED": 20,
    "CONTEXT_REVIEW_REQUIRED": 10,
}
EXPECTED_MURET_DECISIONS = {
    ("INFORMATION", "02", "00"): ("CONTEXT_REVIEW_REQUIRED", "HIGH"),
    ("INFORMATION", "14", "00"): ("CONTEXT_REVIEW_REQUIRED", "HIGH"),
    ("INFORMATION", "27", "00"): ("CONTEXT_REVIEW_REQUIRED", "HIGH"),
    ("INFORMATION", "99", "00"): ("UNKNOWN", "LOW"),
    ("PRESCRIPTION", "01", "00"): ("LIKELY_MATERIAL_CONSTRAINT", "HIGH"),
    ("PRESCRIPTION", "05", "00"): ("MATERIAL_REVIEW_REQUIRED", "HIGH"),
    ("PRESCRIPTION", "07", "00"): ("LIKELY_MATERIAL_CONSTRAINT", "MEDIUM"),
    ("PRESCRIPTION", "07", "04"): ("LIKELY_MATERIAL_CONSTRAINT", "HIGH"),
    ("PRESCRIPTION", "15", "00"): ("DESIGN_REVIEW_REQUIRED", "MEDIUM"),
    ("PRESCRIPTION", "15", "01"): ("DESIGN_REVIEW_REQUIRED", "HIGH"),
    ("PRESCRIPTION", "17", "00"): ("MATERIAL_REVIEW_REQUIRED", "MEDIUM"),
    ("PRESCRIPTION", "18", "00"): ("MATERIAL_REVIEW_REQUIRED", "HIGH"),
}
EXPECTED_POLICY_ENTRIES_SHA256 = (
    "1d3e63f1123000402065b74402cb1e2295db2ac5655209ce410aaf36bfc2be91"
)
EXPECTED_POLICY_SHA256 = (
    "1cfca0eb3d777e9b6604748e8a81609abe7b728de8d0695711cd569180df6489"
)
EXPECTED_POLICY_TABLE_SHA256 = (
    "225105fe488e21f8aa080751812dde1671340c26620cae1d8372c2e59488ed41"
)
EXPECTED_COMPLETE_RESULT_SHA256 = (
    "84a59b418f5a53bc61df73296964b2847cc5d3529c10d0c6912c96222edba09c"
)
EXPECTED_SOURCE_LOCK = {
    "document_id": "33edb4c9f6943c88d8d92518bff20bec",
    "archive_sha256": (
        "9d6677cd6634b56b712311042f0cc714d5ca42a38f82a417b27dd473255d7d93"
    ),
    "cnig_profile": "cnig_plu_2017_muret_observed_pairs_v2",
    "cnig_profile_schema_version": 2,
    "cnig_profile_sha256": (
        "5611b814eb4bc057578b908c6505094f9df5d2c2bf4ca126629b1362983c47ee"
    ),
    "cnig_result_hash_schema_version": 5,
    "cnig_complete_result_content_sha256": (
        "b56b195b32914583e6599fe96b3d29977c52450c9755228d89ce7e192903ab3e"
    ),
}
ARTIFACT_KIND = "BESS_CNIG_FEATURE_POLICY_RESULT"


def _canonical_sha256(value: object) -> str:
    return sha256(
        json.dumps(
            value,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    ).hexdigest()


def _policy_entry(row: object, position: int) -> dict[str, object]:
    statuses = tuple(STATUS_PRIORITIES)
    status = statuses[position % len(statuses)]
    legal_reference = row.legal_reference
    regulation_reference = row.regulation_or_annex_reference
    return {
        "feature_family": row.feature_family,
        "type_code": row.type_code,
        "subtype_code": row.subtype_code,
        "expected_official_label": row.official_label,
        "expected_legal_reference": (
            None if pd.isna(legal_reference) else legal_reference
        ),
        "expected_regulation_reference": (
            None if pd.isna(regulation_reference) else regulation_reference
        ),
        "precheck_status": status,
        "confidence": ("HIGH", "MEDIUM", "LOW")[position % 3],
        "rationale": f"Official pair {row.feature_family} {row.type_code}/{row.subtype_code} requires conservative review.",
        "required_human_action": "Review the official code meaning and the separate local planning material.",
        "limitations": "This entry does not interpret local text or establish authorization or prohibition.",
    }


def _compiled_fixture() -> tuple[
    tuple[object, ...],
    object,
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyResult,
]:
    inputs = _integration_inputs()
    coded = resolve_planning_feature_codes(*inputs)
    config = BessPlanningFeaturePolicyConfig.model_validate(
        _policy_payload(inputs, coded)
    )
    result = compile_bess_planning_feature_policy(*inputs, coded, config)
    return inputs, coded, config, result


def _policy_payload(inputs: tuple[object, ...], coded: object) -> dict[str, object]:
    entries = [
        _policy_entry(row, position)
        for position, row in enumerate(
            coded.code_dictionary.itertuples(index=False),
        )
    ]
    return {
        "schema_version": 1,
        "profile": "synthetic_bess_cnig_feature_policy_v1",
        "policy_scope": POLICY_SCOPE,
        "local_feature_text_interpreted": False,
        "local_regulation_content_interpreted": False,
        "legal_conclusion_produced": False,
        "source_lock": {
            "document_id": coded.source_document_id,
            "archive_sha256": coded.source_archive_sha256,
            "cnig_profile": coded.profile,
            "cnig_profile_schema_version": coded.profile_schema_version,
            "cnig_profile_sha256": coded.profile_sha256,
            "cnig_result_hash_schema_version": coded.result_hash_schema_version,
            "cnig_complete_result_content_sha256": (
                coded.complete_result_content_sha256
            ),
        },
        "status_priority": dict(STATUS_PRIORITIES),
        "canonical_policy_entries_sha256": _canonical_sha256(entries),
        "entries": entries,
    }


def _validated_config(payload: dict[str, object]) -> BessPlanningFeaturePolicyConfig:
    entries = payload["entries"]
    assert isinstance(entries, list)
    payload["canonical_policy_entries_sha256"] = _canonical_sha256(entries)
    return BessPlanningFeaturePolicyConfig.model_validate(payload)


def _artifact_manifest(
    result: BessPlanningFeaturePolicyResult,
    parquet: Path,
) -> dict[str, object]:
    scalar_names = tuple(
        field.name
        for field in fields(BessPlanningFeaturePolicyResult)
        if field.name != "policy_table"
    )
    return {
        "schema_version": 2,
        "artifact_kind": ARTIFACT_KIND,
        **{name: getattr(result, name) for name in scalar_names},
        "parquet_filename": parquet.name,
        "parquet_row_count": len(result.policy_table),
        "parquet_size_bytes": parquet.stat().st_size,
        "parquet_sha256": sha256(parquet.read_bytes()).hexdigest(),
        "policy_table_schema_signature": deterministic_frame_schema_signature(
            result.policy_table
        ),
    }


def _write_artifacts(
    tmp_path: Path,
    result: BessPlanningFeaturePolicyResult,
) -> tuple[Path, Path, dict[str, object]]:
    parquet = tmp_path / "policy.parquet"
    manifest_path = tmp_path / "policy.json"
    result.policy_table.to_parquet(parquet, index=True)
    manifest = _artifact_manifest(result, parquet)
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    return parquet, manifest_path, manifest


def _checked_in_policy_result() -> BessPlanningFeaturePolicyResult:
    inputs = _integration_inputs()
    coded = resolve_planning_feature_codes(*inputs)
    config = load_bess_planning_feature_policy_config(POLICY_PATH)
    cnig_profile = load_cnig_feature_code_profile(
        Path("configs/planning/cnig_plu_2017_feature_codes.yaml")
    )
    cnig_module = importlib.import_module(
        "landscout.stages.resolve_planning_feature_codes"
    )
    policy_module = importlib.import_module(
        "landscout.stages.bess_planning_feature_policy"
    )
    locked_coded = replace(
        coded,
        profile=config.source_lock.cnig_profile,
        profile_schema_version=config.source_lock.cnig_profile_schema_version,
        profile_sha256=config.source_lock.cnig_profile_sha256,
        source_document_id=config.source_lock.document_id,
        source_archive_sha256=config.source_lock.archive_sha256,
        result_hash_schema_version=(config.source_lock.cnig_result_hash_schema_version),
        complete_result_content_sha256=(
            config.source_lock.cnig_complete_result_content_sha256
        ),
        code_dictionary=cnig_module._dictionary(
            cnig_profile, config.source_lock.cnig_profile_sha256
        ),
    )
    return policy_module._build_result(config, locked_coded)


def test_valid_exact_policy_compiles_without_applying_feature_or_parcel_status() -> (
    None
):
    inputs, coded, config, result = _compiled_fixture()
    validate_bess_planning_feature_policy_result(*inputs, coded, config, result)
    assert result.policy_schema_version == 1
    assert result.result_hash_schema_version == 1
    assert result.policy_scope == POLICY_SCOPE
    assert len(result.policy_table) == len(coded.code_dictionary)
    assert not any(
        column in result.policy_table.columns
        for column in ("parcel_id", "planning_feature_id", "relation_type")
    )
    assert result.policy_table["local_feature_text_interpreted"].eq(False).all()
    assert result.policy_table["local_regulation_content_interpreted"].eq(False).all()
    assert result.policy_table["legal_conclusion_produced"].eq(False).all()


def test_checked_in_policy_pins_all_twelve_exact_muret_decisions() -> None:
    config = load_bess_planning_feature_policy_config(POLICY_PATH)
    actual = {
        (entry.feature_family, entry.type_code, entry.subtype_code): (
            entry.precheck_status,
            entry.confidence,
        )
        for entry in config.entries
    }
    assert actual == EXPECTED_MURET_DECISIONS
    assert config.status_priority == STATUS_PRIORITIES
    assert config.policy_scope == POLICY_SCOPE
    assert config.local_feature_text_interpreted is False
    assert config.local_regulation_content_interpreted is False
    assert config.legal_conclusion_produced is False
    assert len(config.entries) == 12
    assert ("PRESCRIPTION", "15", "00") in actual
    assert ("PRESCRIPTION", "15", "01") in actual
    assert all(len(key[1]) == len(key[2]) == 2 for key in actual)


def test_checked_in_policy_complete_snapshot_is_immutable() -> None:
    config = load_bess_planning_feature_policy_config(POLICY_PATH)
    assert config.schema_version == 1
    assert config.profile == "muret_bess_cnig_feature_policy_v1"
    assert config.policy_scope == POLICY_SCOPE
    assert config.local_feature_text_interpreted is False
    assert config.local_regulation_content_interpreted is False
    assert config.legal_conclusion_produced is False
    assert config.source_lock.model_dump(mode="json") == EXPECTED_SOURCE_LOCK
    assert config.status_priority == STATUS_PRIORITIES
    assert config.canonical_policy_entries_sha256 == EXPECTED_POLICY_ENTRIES_SHA256
    assert (
        _canonical_sha256([entry.model_dump(mode="json") for entry in config.entries])
        == EXPECTED_POLICY_ENTRIES_SHA256
    )
    assert _canonical_sha256(config.model_dump(mode="json")) == EXPECTED_POLICY_SHA256


def test_checked_in_compiled_policy_result_hashes_are_pinned() -> None:
    result = _checked_in_policy_result()
    assert result.policy_table_content_sha256 == EXPECTED_POLICY_TABLE_SHA256
    assert result.complete_result_content_sha256 == EXPECTED_COMPLETE_RESULT_SHA256


@pytest.mark.parametrize(
    "field",
    ["rationale", "required_human_action", "limitations"],
)
def test_profile_v1_snapshot_detects_policy_text_drift(field: str) -> None:
    config = load_bess_planning_feature_policy_config(POLICY_PATH)
    payload = config.model_dump(mode="json")
    entries = payload["entries"]
    assert isinstance(entries, list)
    entries[0][field] = f"{entries[0][field]} Changed."
    payload["canonical_policy_entries_sha256"] = _canonical_sha256(entries)
    changed = BessPlanningFeaturePolicyConfig.model_validate(payload)
    assert changed.profile == "muret_bess_cnig_feature_policy_v1"
    assert _canonical_sha256(changed.model_dump(mode="json")) != EXPECTED_POLICY_SHA256


def test_profile_v1_snapshot_detects_source_lock_drift() -> None:
    config = load_bess_planning_feature_policy_config(POLICY_PATH)
    payload = config.model_dump(mode="json")
    source_lock = payload["source_lock"]
    assert isinstance(source_lock, dict)
    source_lock["document_id"] = "another-document"
    changed = BessPlanningFeaturePolicyConfig.model_validate(payload)
    assert changed.profile == "muret_bess_cnig_feature_policy_v1"
    assert _canonical_sha256(changed.model_dump(mode="json")) != EXPECTED_POLICY_SHA256


def test_pandas_is_a_direct_bounded_runtime_dependency() -> None:
    project = tomllib.loads(Path("pyproject.toml").read_text(encoding="utf-8"))[
        "project"
    ]
    assert "pandas>=3.0,<4" in project["dependencies"]


def test_information_9900_official_references_remain_missing() -> None:
    _, _, _, result = _compiled_fixture()
    row = result.policy_table.loc[
        (result.policy_table["feature_family"] == "INFORMATION")
        & (result.policy_table["type_code"] == "99")
        & (result.policy_table["subtype_code"] == "00")
    ].iloc[0]
    assert pd.isna(row["official_legal_reference"])
    assert pd.isna(row["official_regulation_reference"])


@pytest.mark.parametrize(
    ("column", "literal"),
    [
        (column, literal)
        for column in (
            "official_legal_reference",
            "official_regulation_reference",
        )
        for literal in ("None", "nan", "<NA>")
    ],
)
def test_null_reference_literal_is_rejected_by_local_envelope(
    column: str,
    literal: str,
) -> None:
    _, _, _, result = _compiled_fixture()
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    table = result.policy_table.copy(deep=True)
    row = table.index[
        (table["feature_family"] == "INFORMATION")
        & (table["type_code"] == "99")
        & (table["subtype_code"] == "00")
    ][0]
    table.loc[row, column] = literal
    coordinated = module._result_with_hashes(replace(result, policy_table=table))
    with pytest.raises(BessPlanningFeaturePolicyError, match="reference|null|missing"):
        module._validate_result_envelope(coordinated)


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("document_id", "another-document"),
        ("archive_sha256", "f" * 64),
        ("cnig_profile", "another-profile"),
        ("cnig_profile_schema_version", 1),
        ("cnig_profile_sha256", "f" * 64),
        ("cnig_result_hash_schema_version", 4),
        ("cnig_complete_result_content_sha256", "f" * 64),
    ],
)
def test_source_lock_mismatch_is_rejected(field: str, value: object) -> None:
    inputs, coded, config, _ = _compiled_fixture()
    changed_lock = config.source_lock.model_copy(update={field: value})
    changed = config.model_copy(update={"source_lock": changed_lock})
    with pytest.raises(BessPlanningFeaturePolicyError, match="lock|source|CNIG"):
        compile_bess_planning_feature_policy(*inputs, coded, changed)


def test_missing_policy_pair_is_rejected() -> None:
    inputs = _integration_inputs()
    coded = resolve_planning_feature_codes(*inputs)
    payload = _policy_payload(inputs, coded)
    entries = payload["entries"]
    assert isinstance(entries, list)
    entries.pop()
    config = _validated_config(payload)
    with pytest.raises(BessPlanningFeaturePolicyError, match="missing|pair"):
        compile_bess_planning_feature_policy(*inputs, coded, config)


def test_extra_policy_pair_is_rejected_without_type_fallback() -> None:
    inputs = _integration_inputs()
    coded = resolve_planning_feature_codes(*inputs)
    payload = _policy_payload(inputs, coded)
    entries = payload["entries"]
    assert isinstance(entries, list)
    extra = dict(entries[-1])
    extra.update(
        {
            "feature_family": "INFORMATION",
            "type_code": "98",
            "subtype_code": "00",
            "expected_official_label": "Synthetic extra official pair",
            "expected_legal_reference": None,
            "expected_regulation_reference": None,
        }
    )
    entries.append(extra)
    entries.sort(
        key=lambda row: (row["feature_family"], row["type_code"], row["subtype_code"])
    )
    config = _validated_config(payload)
    with pytest.raises(BessPlanningFeaturePolicyError, match="extra|pair"):
        compile_bess_planning_feature_policy(*inputs, coded, config)


def test_duplicate_policy_pair_is_rejected() -> None:
    inputs = _integration_inputs()
    coded = resolve_planning_feature_codes(*inputs)
    payload = _policy_payload(inputs, coded)
    entries = payload["entries"]
    assert isinstance(entries, list)
    entries.append(dict(entries[0]))
    payload["canonical_policy_entries_sha256"] = _canonical_sha256(entries)
    with pytest.raises(ValidationError, match="duplicate|pair"):
        BessPlanningFeaturePolicyConfig.model_validate(payload)


def test_prescription_information_code_spaces_remain_separate() -> None:
    inputs = _integration_inputs()
    coded = resolve_planning_feature_codes(*inputs)
    payload = _policy_payload(inputs, coded)
    entries = payload["entries"]
    assert isinstance(entries, list)
    entries[0]["feature_family"] = "PRESCRIPTION"
    entries.sort(
        key=lambda row: (row["feature_family"], row["type_code"], row["subtype_code"])
    )
    config = _validated_config(payload)
    with pytest.raises(BessPlanningFeaturePolicyError, match="missing|extra|pair"):
        compile_bess_planning_feature_policy(*inputs, coded, config)


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("expected_official_label", "Wrong official label", "label"),
        ("expected_legal_reference", "Wrong legal reference", "legal"),
        ("expected_regulation_reference", "Wrong regulation reference", "regulation"),
    ],
)
def test_official_meaning_mismatch_is_rejected(
    field: str,
    value: object,
    message: str,
) -> None:
    inputs = _integration_inputs()
    coded = resolve_planning_feature_codes(*inputs)
    payload = _policy_payload(inputs, coded)
    entries = payload["entries"]
    assert isinstance(entries, list)
    entries[0][field] = value
    config = _validated_config(payload)
    with pytest.raises(BessPlanningFeaturePolicyError, match=message):
        compile_bess_planning_feature_policy(*inputs, coded, config)


@pytest.mark.parametrize("status", ["ALLOWED", "FORBIDDEN", "PROHIBITED"])
def test_invalid_or_legal_conclusion_status_is_rejected(status: str) -> None:
    inputs = _integration_inputs()
    coded = resolve_planning_feature_codes(*inputs)
    payload = _policy_payload(inputs, coded)
    entries = payload["entries"]
    assert isinstance(entries, list)
    entries[0]["precheck_status"] = status
    payload["canonical_policy_entries_sha256"] = _canonical_sha256(entries)
    with pytest.raises(ValidationError):
        BessPlanningFeaturePolicyConfig.model_validate(payload)


def test_invalid_confidence_is_rejected() -> None:
    inputs = _integration_inputs()
    coded = resolve_planning_feature_codes(*inputs)
    payload = _policy_payload(inputs, coded)
    entries = payload["entries"]
    assert isinstance(entries, list)
    entries[0]["confidence"] = "CERTAIN"
    payload["canonical_policy_entries_sha256"] = _canonical_sha256(entries)
    with pytest.raises(ValidationError):
        BessPlanningFeaturePolicyConfig.model_validate(payload)


@pytest.mark.parametrize("mutation", ["duplicate", "missing", "zero", "bool", "string"])
def test_status_priority_contract_is_strict(mutation: str) -> None:
    inputs = _integration_inputs()
    coded = resolve_planning_feature_codes(*inputs)
    payload = _policy_payload(inputs, coded)
    priorities = payload["status_priority"]
    assert isinstance(priorities, dict)
    if mutation == "duplicate":
        priorities["UNKNOWN"] = priorities["LIKELY_MATERIAL_CONSTRAINT"]
    elif mutation == "missing":
        priorities.pop("UNKNOWN")
    elif mutation == "zero":
        priorities["UNKNOWN"] = 0
    elif mutation == "bool":
        priorities["UNKNOWN"] = True
    else:
        priorities["UNKNOWN"] = "40"
    with pytest.raises(ValidationError, match="priority|integer"):
        BessPlanningFeaturePolicyConfig.model_validate(payload)


def test_duplicate_yaml_key_is_rejected(tmp_path: Path) -> None:
    path = tmp_path / "duplicate.yaml"
    path.write_text("schema_version: 1\nschema_version: 1\n", encoding="utf-8")
    with pytest.raises(BessPlanningFeaturePolicyError, match="Duplicate YAML"):
        load_bess_planning_feature_policy_config(path)


def test_unknown_yaml_field_is_rejected() -> None:
    inputs = _integration_inputs()
    coded = resolve_planning_feature_codes(*inputs)
    payload = _policy_payload(inputs, coded)
    payload["unknown_field"] = "not allowed"
    with pytest.raises(ValidationError):
        BessPlanningFeaturePolicyConfig.model_validate(payload)


def test_noncanonical_whitespace_is_rejected() -> None:
    inputs = _integration_inputs()
    coded = resolve_planning_feature_codes(*inputs)
    payload = _policy_payload(inputs, coded)
    entries = payload["entries"]
    assert isinstance(entries, list)
    entries[0]["rationale"] = " leading whitespace"
    payload["canonical_policy_entries_sha256"] = _canonical_sha256(entries)
    with pytest.raises(ValidationError, match="whitespace|exact"):
        BessPlanningFeaturePolicyConfig.model_validate(payload)


def test_malformed_sha256_is_rejected() -> None:
    inputs = _integration_inputs()
    coded = resolve_planning_feature_codes(*inputs)
    payload = _policy_payload(inputs, coded)
    payload["canonical_policy_entries_sha256"] = "NOT-A-SHA"
    with pytest.raises(ValidationError, match="SHA256"):
        BessPlanningFeaturePolicyConfig.model_validate(payload)


def test_in_memory_config_is_revalidated_before_compilation() -> None:
    inputs, coded, config, _ = _compiled_fixture()
    corrupted = config.model_copy(update={"canonical_policy_entries_sha256": "f" * 64})
    with pytest.raises(BessPlanningFeaturePolicyError, match="in-memory|canonical"):
        compile_bess_planning_feature_policy(*inputs, coded, corrupted)


def test_policy_entries_require_deterministic_order() -> None:
    inputs = _integration_inputs()
    coded = resolve_planning_feature_codes(*inputs)
    payload = _policy_payload(inputs, coded)
    entries = payload["entries"]
    assert isinstance(entries, list)
    entries.reverse()
    payload["canonical_policy_entries_sha256"] = _canonical_sha256(entries)
    with pytest.raises(ValidationError, match="order"):
        BessPlanningFeaturePolicyConfig.model_validate(payload)


def test_policy_table_is_sorted_and_preserves_leading_zero_codes() -> None:
    _, _, _, result = _compiled_fixture()
    keys = list(
        result.policy_table[["feature_family", "type_code", "subtype_code"]].itertuples(
            index=False, name=None
        )
    )
    assert keys == sorted(keys)
    assert all(
        len(type_code) == len(subtype_code) == 2 for _, type_code, subtype_code in keys
    )


def test_policy_table_mutation_is_rejected() -> None:
    inputs, coded, config, result = _compiled_fixture()
    table = result.policy_table.copy(deep=True)
    table.loc[table.index[0], "precheck_status"] = "UNKNOWN"
    with pytest.raises(BessPlanningFeaturePolicyError, match="hash|table|rebuilt"):
        validate_bess_planning_feature_policy_result(
            *inputs, coded, config, replace(result, policy_table=table)
        )


def test_coordinated_policy_table_and_hash_mutation_is_rejected() -> None:
    inputs, coded, config, result = _compiled_fixture()
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    table = result.policy_table.copy(deep=True)
    table.loc[table.index[0], "rationale"] = "Coordinated but false rationale."
    coordinated = module._result_with_hashes(replace(result, policy_table=table))
    with pytest.raises(BessPlanningFeaturePolicyError, match="table|rebuilt"):
        validate_bess_planning_feature_policy_result(
            *inputs, coded, config, coordinated
        )


def test_persisted_parquet_and_json_readback_is_source_complete(
    tmp_path: Path,
) -> None:
    inputs, coded, config, result = _compiled_fixture()
    parquet, manifest_path, _ = _write_artifacts(tmp_path, result)
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    persisted = module.load_bess_planning_feature_policy_artifacts(
        parquet, manifest_path
    )
    assert_frame_equal(result.policy_table, persisted.policy_table, check_dtype=True)
    row = persisted.policy_table.loc[
        (persisted.policy_table["feature_family"] == "INFORMATION")
        & (persisted.policy_table["type_code"] == "99")
        & (persisted.policy_table["subtype_code"] == "00")
    ].iloc[0]
    assert pd.isna(row["official_legal_reference"])
    assert pd.isna(row["official_regulation_reference"])
    validate_bess_planning_feature_policy_result(*inputs, coded, config, persisted)


def test_artifact_manifest_model_is_strict_and_frozen(tmp_path: Path) -> None:
    _, _, _, result = _compiled_fixture()
    parquet, _, manifest = _write_artifacts(tmp_path, result)
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    validated = module.BessPlanningFeaturePolicyArtifactManifest.model_validate(
        manifest
    )
    assert validated.schema_version == 2
    assert validated.artifact_kind == ARTIFACT_KIND
    assert validated.cnig_profile_schema_version == 2
    assert validated.cnig_result_hash_schema_version == 5
    assert validated.parquet_filename == parquet.name
    with pytest.raises(ValidationError):
        validated.parquet_row_count = 0


@pytest.mark.parametrize(
    ("mutation", "message"),
    [
        (lambda value: value.update(schema_version=1), "schema"),
        (lambda value: value.update(unknown_field=True), "manifest|artifact"),
        (lambda value: value.update(parquet_filename="other.parquet"), "filename"),
        (lambda value: value.update(parquet_row_count=999), "row"),
        (lambda value: value.update(parquet_size_bytes=999), "size"),
        (lambda value: value.update(parquet_sha256="f" * 64), "SHA|hash"),
        (
            lambda value: value["policy_table_schema_signature"].update(
                index_names=["changed"]
            ),
            "schema",
        ),
        (lambda value: value.update(policy_table_content_sha256="f" * 64), "hash"),
        (lambda value: value.update(complete_result_content_sha256="f" * 64), "hash"),
        (lambda value: value.pop("policy_profile"), "manifest|artifact"),
    ],
)
def test_artifact_loader_rejects_manifest_mismatch(
    tmp_path: Path,
    mutation: object,
    message: str,
) -> None:
    _, _, _, result = _compiled_fixture()
    parquet, manifest_path, manifest = _write_artifacts(tmp_path, result)
    assert callable(mutation)
    mutation(manifest)
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    with pytest.raises(BessPlanningFeaturePolicyError, match=message):
        module.load_bess_planning_feature_policy_artifacts(parquet, manifest_path)


def test_artifact_loader_rejects_duplicate_json_key(tmp_path: Path) -> None:
    _, _, _, result = _compiled_fixture()
    parquet, manifest_path, _ = _write_artifacts(tmp_path, result)
    manifest_path.write_text(
        '{"schema_version": 2, "schema_version": 2}\n', encoding="utf-8"
    )
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    with pytest.raises(BessPlanningFeaturePolicyError, match="Duplicate JSON"):
        module.load_bess_planning_feature_policy_artifacts(parquet, manifest_path)


def test_artifact_loader_rejects_parquet_replacement(tmp_path: Path) -> None:
    _, _, _, result = _compiled_fixture()
    parquet, manifest_path, _ = _write_artifacts(tmp_path, result)
    parquet.write_bytes(parquet.read_bytes() + b"changed-after-manifest")
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    with pytest.raises(BessPlanningFeaturePolicyError, match="size|SHA|hash"):
        module.load_bess_planning_feature_policy_artifacts(parquet, manifest_path)


def test_artifact_loader_parses_the_exact_verified_parquet_bytes(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _, _, _, result = _compiled_fixture()
    parquet, manifest_path, _ = _write_artifacts(tmp_path, result)
    replacement = tmp_path / "replacement.parquet"
    result.policy_table.to_parquet(replacement, index=True, compression="gzip")
    original_read_bytes = Path.read_bytes
    verified_bytes = original_read_bytes(parquet)
    replacement_bytes = original_read_bytes(replacement)
    assert replacement_bytes != verified_bytes
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    original_read_parquet = module.pd.read_parquet
    replacement_performed = False
    parsed_payloads: list[tuple[str, bytes]] = []

    def replace_after_byte_read(path: Path) -> bytes:
        nonlocal replacement_performed
        payload = original_read_bytes(path)
        if path == parquet and not replacement_performed:
            path.write_bytes(replacement_bytes)
            replacement_performed = True
        return payload

    def old_hash_then_replace(path: Path) -> str:
        nonlocal replacement_performed
        payload = original_read_bytes(path)
        if path == parquet and not replacement_performed:
            path.write_bytes(replacement_bytes)
            replacement_performed = True
        return sha256(payload).hexdigest()

    def observed_read_parquet(
        source: object, *args: object, **kwargs: object
    ) -> object:
        if isinstance(source, BytesIO):
            parsed_payloads.append(("buffer", source.getvalue()))
        else:
            path = Path(source)
            parsed_payloads.append(("path", original_read_bytes(path)))
        return original_read_parquet(source, *args, **kwargs)

    monkeypatch.setattr(Path, "read_bytes", replace_after_byte_read)
    monkeypatch.setattr(module, "_file_sha256", old_hash_then_replace, raising=False)
    monkeypatch.setattr(module.pd, "read_parquet", observed_read_parquet)
    loaded = module.load_bess_planning_feature_policy_artifacts(parquet, manifest_path)
    assert replacement_performed
    assert parsed_payloads == [("buffer", verified_bytes)]
    assert_frame_equal(result.policy_table, loaded.policy_table, check_dtype=True)


def test_locally_invalid_result_fast_fails_before_source_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inputs, coded, config, result = _compiled_fixture()
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    calls = 0

    def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1

    monkeypatch.setattr(module, "validate_planning_feature_code_result", counted)
    wrong_table = result.policy_table.drop(columns="confidence")
    invalid_results = (
        object(),
        replace(result, policy_schema_version=2),
        replace(result, policy_table=wrong_table),
        replace(result, policy_table_content_sha256="f" * 64),
        replace(result, complete_result_content_sha256="f" * 64),
    )
    for invalid in invalid_results:
        with pytest.raises(
            BessPlanningFeaturePolicyError, match="type|schema|hash|result"
        ):
            module.validate_bess_planning_feature_policy_result(
                *inputs, coded, config, invalid
            )
    assert calls == 0


def test_compiler_wrong_source_lock_fast_fails_before_source_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inputs, coded, config, _ = _compiled_fixture()
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    calls = 0

    def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1

    wrong_lock = config.source_lock.model_copy(
        update={"document_id": "another-document"}
    )
    wrong_config = config.model_copy(update={"source_lock": wrong_lock})
    monkeypatch.setattr(module, "validate_planning_feature_code_result", counted)
    with pytest.raises(BessPlanningFeaturePolicyError, match="lock|document"):
        module.compile_bess_planning_feature_policy(*inputs, coded, wrong_config)
    assert calls == 0


def test_forged_matching_lock_still_runs_source_complete_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inputs, coded, config, _ = _compiled_fixture()
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    actual = module.validate_planning_feature_code_result
    calls = 0

    def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1
        actual(*args, **kwargs)

    forged_coded = replace(coded, source_document_id="forged-document")
    forged_lock = config.source_lock.model_copy(
        update={"document_id": "forged-document"}
    )
    forged_config = config.model_copy(update={"source_lock": forged_lock})
    monkeypatch.setattr(module, "validate_planning_feature_code_result", counted)
    with pytest.raises(BessPlanningFeaturePolicyError, match="Source-complete|source"):
        module.compile_bess_planning_feature_policy(
            *inputs, forged_coded, forged_config
        )
    assert calls == 1


def test_compiler_and_public_validator_invoke_source_complete_coding_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inputs = _integration_inputs()
    coded = resolve_planning_feature_codes(*inputs)
    config = BessPlanningFeaturePolicyConfig.model_validate(
        _policy_payload(inputs, coded)
    )
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    actual = module.validate_planning_feature_code_result
    calls = 0

    def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1
        actual(*args, **kwargs)

    monkeypatch.setattr(module, "validate_planning_feature_code_result", counted)
    result = module.compile_bess_planning_feature_policy(*inputs, coded, config)
    assert calls == 1
    module.validate_bess_planning_feature_policy_result(*inputs, coded, config, result)
    assert calls == 2


def test_public_policy_api_exports_only_stable_symbols() -> None:
    required = {
        "BessPlanningFeaturePolicyArtifactManifest",
        "BessPlanningFeaturePolicyConfig",
        "BessPlanningFeaturePolicyError",
        "BessPlanningFeaturePolicyResult",
        "load_bess_planning_feature_policy_artifacts",
        "load_bess_planning_feature_policy_config",
        "compile_bess_planning_feature_policy",
        "validate_bess_planning_feature_policy_result",
        "validate_bess_planning_feature_policy_result_envelope",
    }
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    assert set(module.__all__) == required
    assert required.issubset(set(stages.__all__))
    assert all(getattr(stages, name) is getattr(module, name) for name in required)
    assert not any(name in module.__all__ for name in ("_canonical_sha256", "_lookup"))


def test_step_7d_5b_2b_5_exposes_lightweight_policy_result_validator() -> None:
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    assert hasattr(module, "validate_bess_planning_feature_policy_result_envelope")
    _, _, _, result = _compiled_fixture()
    module.validate_bess_planning_feature_policy_result_envelope(result)
    with pytest.raises(BessPlanningFeaturePolicyError, match="hash"):
        module.validate_bess_planning_feature_policy_result_envelope(
            replace(result, complete_result_content_sha256="0" * 64)
        )


@pytest.mark.parametrize(
    "filename",
    [
        "/tmp/file.parquet",
        "../file.parquet",
        "subdir/file.parquet",
        r"C:\absolute\file.parquet",
        "C:/absolute/file.parquet",
        r"\\server\share\file.parquet",
        r"subdir\file.parquet",
        "CON.parquet",
        "con.PARQUET",
        "NUL.parquet",
        "PRN.parquet",
        "AUX.parquet",
        "CLOCK$.parquet",
        "COM1.parquet",
        "COM9.parquet",
        "LPT1.parquet",
        "LPT9.parquet",
        "COM¹.parquet",
        "COM².parquet",
        "COM³.parquet",
        "LPT¹.parquet",
        "LPT².parquet",
        "LPT³.parquet",
        "file:name.parquet",
        "base.parquet:stream.parquet",
        "file?.parquet",
        "file*.parquet",
        "file<.parquet",
        "file>.parquet",
        "file|.parquet",
        'file".parquet',
        "nul\x00.parquet",
        "line\nbreak.parquet",
        "del\x7f.parquet",
    ],
)
def test_policy_manifest_rejects_nonportable_parquet_filename(
    tmp_path: Path, filename: str
) -> None:
    _, _, _, result = _compiled_fixture()
    _, _, manifest = _write_artifacts(tmp_path, result)
    manifest["parquet_filename"] = filename
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    with pytest.raises(ValueError, match="filename|basename|portable"):
        module.BessPlanningFeaturePolicyArtifactManifest.model_validate(manifest)


@pytest.mark.parametrize(
    "filename",
    [
        "com¹.parquet",
        "CoM².parquet",
        "cOm³.parquet",
        "lpt¹.parquet",
        "LpT².parquet",
        "lPt³.parquet",
    ],
)
def test_shared_filename_contract_rejects_superscript_windows_devices(
    filename: str,
) -> None:
    with pytest.raises(ValueError, match="reserved|basename|portable"):
        validate_portable_parquet_filename(filename, "artifact filename")


@pytest.mark.parametrize(
    ("field", "version"),
    [
        ("cnig_profile_schema_version", 0),
        ("cnig_profile_schema_version", 1),
        ("cnig_profile_schema_version", 3),
        ("cnig_profile_schema_version", 999),
        ("cnig_result_hash_schema_version", 0),
        ("cnig_result_hash_schema_version", 1),
        ("cnig_result_hash_schema_version", 4),
        ("cnig_result_hash_schema_version", 6),
        ("cnig_result_hash_schema_version", 999),
    ],
)
def test_policy_manifest_rejects_unsupported_cnig_source_schema(
    tmp_path: Path,
    field: str,
    version: int,
) -> None:
    _, _, _, result = _compiled_fixture()
    _, _, manifest = _write_artifacts(tmp_path, result)
    manifest[field] = version
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    with pytest.raises(ValidationError, match="CNIG|cnig|schema|version"):
        module.BessPlanningFeaturePolicyArtifactManifest.model_validate(manifest)


@pytest.mark.parametrize(
    ("field", "version"),
    [
        ("cnig_profile_schema_version", 0),
        ("cnig_profile_schema_version", 1),
        ("cnig_profile_schema_version", 3),
        ("cnig_profile_schema_version", 999),
        ("cnig_result_hash_schema_version", 0),
        ("cnig_result_hash_schema_version", 1),
        ("cnig_result_hash_schema_version", 4),
        ("cnig_result_hash_schema_version", 6),
        ("cnig_result_hash_schema_version", 999),
    ],
)
def test_policy_artifact_loader_rejects_source_schema_before_parquet_read(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    field: str,
    version: int,
) -> None:
    _, _, _, result = _compiled_fixture()
    parquet, manifest_path, manifest = _write_artifacts(tmp_path, result)
    manifest[field] = version
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    calls = {"bytes": 0, "parse": 0}

    def byte_read(*args: object, **kwargs: object) -> bytes:
        calls["bytes"] += 1
        raise AssertionError("Parquet bytes must not be read")

    def parse(*args: object, **kwargs: object) -> pd.DataFrame:
        calls["parse"] += 1
        raise AssertionError("Parquet must not be parsed")

    monkeypatch.setattr(Path, "read_bytes", byte_read)
    monkeypatch.setattr(pd, "read_parquet", parse)
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    with pytest.raises(
        BessPlanningFeaturePolicyError, match="CNIG|cnig|schema|version"
    ):
        module.load_bess_planning_feature_policy_artifacts(parquet, manifest_path)
    assert calls == {"bytes": 0, "parse": 0}


def _rehash_policy_table(
    result: BessPlanningFeaturePolicyResult, table: pd.DataFrame
) -> BessPlanningFeaturePolicyResult:
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    return module._result_with_hashes(replace(result, policy_table=table))


def _canonical_empty_policy_result(
    result: BessPlanningFeaturePolicyResult,
) -> BessPlanningFeaturePolicyResult:
    table = result.policy_table.iloc[0:0].copy(deep=True)
    table.index = pd.Index([], dtype="int64")
    return _rehash_policy_table(result, table)


def test_policy_envelope_rejects_canonical_empty_policy_table() -> None:
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    _, _, _, result = _compiled_fixture()
    empty = _canonical_empty_policy_result(result)
    with pytest.raises(
        BessPlanningFeaturePolicyError, match="policy|table|empty|entry"
    ):
        module.validate_bess_planning_feature_policy_result_envelope(empty)


def test_policy_envelope_accepts_one_exact_policy_row() -> None:
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    _, _, _, result = _compiled_fixture()
    table = result.policy_table.iloc[[0]].copy(deep=True)
    table.index = pd.Index([0], dtype="int64")
    one_row = _rehash_policy_table(result, table)
    module.validate_bess_planning_feature_policy_result_envelope(one_row)


def test_policy_envelope_accepts_current_twelve_row_snapshot() -> None:
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    result = _checked_in_policy_result()
    assert len(result.policy_table) == 12
    module.validate_bess_planning_feature_policy_result_envelope(result)


@pytest.mark.parametrize("version", [0, 1, 3, 999])
def test_policy_envelope_requires_cnig_profile_schema_two(version: int) -> None:
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    _, _, _, result = _compiled_fixture()
    changed = module._result_with_hashes(
        replace(result, cnig_profile_schema_version=version)
    )
    with pytest.raises(BessPlanningFeaturePolicyError, match="profile schema|schema"):
        module.validate_bess_planning_feature_policy_result_envelope(changed)


@pytest.mark.parametrize("version", [0, 1, 2, 4, 6, 999])
def test_policy_envelope_requires_cnig_result_schema_five(version: int) -> None:
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    _, _, _, result = _compiled_fixture()
    changed = module._result_with_hashes(
        replace(result, cnig_result_hash_schema_version=version)
    )
    with pytest.raises(BessPlanningFeaturePolicyError, match="CNIG result|schema"):
        module.validate_bess_planning_feature_policy_result_envelope(changed)


@pytest.mark.parametrize(
    "mutation",
    [
        "duplicate-pair",
        "reordered-pairs",
        "malformed-code",
        "invalid-status",
        "invalid-confidence",
        "zero-priority",
        "negative-priority",
        "bool-priority",
        "status-two-priorities",
        "priority-two-statuses",
        "row-scope",
        "row-flag",
        "row-policy-sha",
        "row-cnig-profile",
        "row-cnig-sha",
        "row-cnig-result-sha",
        "literal-null-reference",
    ],
)
def test_policy_envelope_validates_every_intrinsic_row_contract(
    mutation: str,
) -> None:
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    _, _, _, result = _compiled_fixture()
    table = result.policy_table.copy(deep=True)
    first, second = table.index[:2]
    if mutation == "duplicate-pair":
        table.loc[second, ["feature_family", "type_code", "subtype_code"]] = table.loc[
            first, ["feature_family", "type_code", "subtype_code"]
        ].tolist()
    elif mutation == "reordered-pairs":
        table = table.iloc[::-1].copy(deep=True)
    elif mutation == "malformed-code":
        table.loc[first, "type_code"] = "1"
    elif mutation == "invalid-status":
        table.loc[first, "precheck_status"] = "AUTHORIZED"
    elif mutation == "invalid-confidence":
        table.loc[first, "confidence"] = "CERTAIN"
    elif mutation == "zero-priority":
        table.loc[first, "status_priority"] = 0
    elif mutation == "negative-priority":
        table.loc[first, "status_priority"] = -1
    elif mutation == "bool-priority":
        values = table["status_priority"].astype("object")
        values.loc[first] = True
        table["status_priority"] = values
    elif mutation == "status-two-priorities":
        table.loc[second, "precheck_status"] = table.loc[first, "precheck_status"]
        table.loc[second, "status_priority"] = table.loc[first, "status_priority"] + 1
    elif mutation == "priority-two-statuses":
        different = table.index[
            table["precheck_status"] != table.loc[first, "precheck_status"]
        ][0]
        table.loc[different, "status_priority"] = table.loc[first, "status_priority"]
    elif mutation == "row-scope":
        table.loc[first, "policy_scope"] = "OTHER_SCOPE"
    elif mutation == "row-flag":
        table.loc[first, "local_feature_text_interpreted"] = True
    elif mutation == "row-policy-sha":
        table.loc[first, "policy_sha256"] = "a" * 64
    elif mutation == "row-cnig-profile":
        table.loc[first, "cnig_profile"] = "other-cnig-profile"
    elif mutation == "row-cnig-sha":
        table.loc[first, "cnig_profile_sha256"] = "a" * 64
    elif mutation == "row-cnig-result-sha":
        table.loc[first, "cnig_complete_result_content_sha256"] = "a" * 64
    else:
        table.loc[first, "official_legal_reference"] = "None"
    changed = _rehash_policy_table(result, table)
    with pytest.raises(
        BessPlanningFeaturePolicyError,
        match="policy|pair|order|code|status|confidence|priority|scope|flag|CNIG|null|schema",
    ):
        module.validate_bess_planning_feature_policy_result_envelope(changed)


def test_policy_envelope_requires_exact_type_and_accepts_valid_schema_v1() -> None:
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    _, _, _, result = _compiled_fixture()

    class DerivedPolicyResult(BessPlanningFeaturePolicyResult):
        pass

    derived = DerivedPolicyResult(**result.__dict__)
    with pytest.raises(BessPlanningFeaturePolicyError, match="type|result"):
        module.validate_bess_planning_feature_policy_result_envelope(derived)
    module.validate_bess_planning_feature_policy_result_envelope(result)


@pytest.mark.parametrize("malformed", [None, object()])
def test_policy_envelope_controls_malformed_result_type(malformed: object) -> None:
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    with pytest.raises(BessPlanningFeaturePolicyError):
        module.validate_bess_planning_feature_policy_result_envelope(malformed)
