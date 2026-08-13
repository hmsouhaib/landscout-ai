from __future__ import annotations

import importlib
import json
from dataclasses import fields, replace
from hashlib import sha256
from pathlib import Path

import pandas as pd
import pytest
from pandas.testing import assert_frame_equal
from pydantic import ValidationError
from test_resolve_planning_feature_codes import _integration_inputs

from landscout import stages
from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyError,
    BessPlanningFeaturePolicyResult,
    compile_bess_planning_feature_policy,
    load_bess_planning_feature_policy_config,
    validate_bess_planning_feature_policy_result,
)
from landscout.stages.resolve_planning_feature_codes import (
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
    return {
        "feature_family": row.feature_family,
        "type_code": row.type_code,
        "subtype_code": row.subtype_code,
        "expected_official_label": row.official_label,
        "expected_legal_reference": row.legal_reference,
        "expected_regulation_reference": row.regulation_or_annex_reference,
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


def test_valid_exact_policy_compiles_without_applying_feature_or_parcel_status() -> None:
    inputs, coded, config, result = _compiled_fixture()
    validate_bess_planning_feature_policy_result(
        *inputs, coded, config, result
    )
    assert result.policy_schema_version == 1
    assert result.result_hash_schema_version == 1
    assert result.policy_scope == POLICY_SCOPE
    assert len(result.policy_table) == len(coded.code_dictionary)
    assert not any(
        column in result.policy_table.columns
        for column in ("parcel_id", "planning_feature_id", "relation_type")
    )
    assert result.policy_table["local_feature_text_interpreted"].eq(False).all()
    assert result.policy_table["local_regulation_content_interpreted"].eq(
        False
    ).all()
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
    entries.sort(key=lambda row: (row["feature_family"], row["type_code"], row["subtype_code"]))
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
    entries.sort(key=lambda row: (row["feature_family"], row["type_code"], row["subtype_code"]))
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
    corrupted = config.model_copy(
        update={"canonical_policy_entries_sha256": "f" * 64}
    )
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
        result.policy_table[
            ["feature_family", "type_code", "subtype_code"]
        ].itertuples(index=False, name=None)
    )
    assert keys == sorted(keys)
    assert all(len(type_code) == len(subtype_code) == 2 for _, type_code, subtype_code in keys)


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
    module = importlib.import_module(
        "landscout.stages.bess_planning_feature_policy"
    )
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
    parquet = tmp_path / "policy.parquet"
    manifest_path = tmp_path / "policy.json"
    result.policy_table.to_parquet(parquet, index=True)
    scalar_names = tuple(
        field.name
        for field in fields(BessPlanningFeaturePolicyResult)
        if field.name != "policy_table"
    )
    manifest = {name: getattr(result, name) for name in scalar_names}
    manifest["schema_version"] = 1
    manifest["output"] = {
        "filename": parquet.name,
        "row_count": len(result.policy_table),
    }
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    decoded = json.loads(manifest_path.read_text(encoding="utf-8"))
    persisted = BessPlanningFeaturePolicyResult(
        **{name: decoded[name] for name in scalar_names},
        policy_table=pd.read_parquet(parquet),
    )
    assert_frame_equal(result.policy_table, persisted.policy_table, check_dtype=True)
    validate_bess_planning_feature_policy_result(
        *inputs, coded, config, persisted
    )


def test_compiler_and_public_validator_invoke_source_complete_coding_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inputs = _integration_inputs()
    coded = resolve_planning_feature_codes(*inputs)
    config = BessPlanningFeaturePolicyConfig.model_validate(
        _policy_payload(inputs, coded)
    )
    module = importlib.import_module(
        "landscout.stages.bess_planning_feature_policy"
    )
    actual = module.validate_planning_feature_code_result
    calls = 0

    def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1
        actual(*args, **kwargs)

    monkeypatch.setattr(module, "validate_planning_feature_code_result", counted)
    result = module.compile_bess_planning_feature_policy(*inputs, coded, config)
    assert calls == 1
    module.validate_bess_planning_feature_policy_result(
        *inputs, coded, config, result
    )
    assert calls == 2


def test_public_policy_api_exports_only_stable_symbols() -> None:
    required = {
        "BessPlanningFeaturePolicyConfig",
        "BessPlanningFeaturePolicyError",
        "BessPlanningFeaturePolicyResult",
        "load_bess_planning_feature_policy_config",
        "compile_bess_planning_feature_policy",
        "validate_bess_planning_feature_policy_result",
    }
    module = importlib.import_module(
        "landscout.stages.bess_planning_feature_policy"
    )
    assert set(module.__all__) == required
    assert required.issubset(set(stages.__all__))
    assert all(getattr(stages, name) is getattr(module, name) for name in required)
    assert not any(name in module.__all__ for name in ("_canonical_sha256", "_lookup"))
