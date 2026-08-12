from __future__ import annotations

import importlib
from dataclasses import replace
from hashlib import sha256
from pathlib import Path

import geopandas as gpd  # type: ignore[import-untyped]
import pandas as pd
import pytest
from geopandas.testing import assert_geodataframe_equal
from shapely.geometry import Polygon

interpret_module = importlib.import_module(
    "landscout.stages.interpret_bess_zoning"
)

from landscout import stages
from landscout.stages.index_planning_regulation import (
    INDEX_HASH_SCHEMA_VERSION,
    PAGE_HASH_SCHEMA_VERSION,
    SEARCH_NORMALIZATION_PROFILE,
    PlanningRegulationIndex,
    _index_content_sha256,
    _normalize_search_text,
    _page_content_sha256,
    _pages_content_sha256,
)
from landscout.stages.interpret_bess_zoning import (
    CHAPTER_POLICY_COLUMNS,
    EVIDENCE_CATALOG_COLUMNS,
    PARCEL_ZONE_POLICY_COLUMNS,
    SOURCE_ZONE_POLICY_COLUMNS,
    BessZoningPolicyConfig,
    BessZoningPrecheckError,
    _result_with_hashes,
    interpret_bess_zoning,
    load_bess_zoning_policy_config,
    validate_bess_zoning_precheck,
)
from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    planning_regulation_section_page_fragments,
    structure_planning_regulation,
)
from landscout.stages.structure_planning_regulation import (
    _result_with_hashes as _structure_with_hashes,
)


def _index() -> PlanningRegulationIndex:
    raw_pages = (
        "ARTICLE 1 - GENERAL\nGeneral factual text.",
        (
            "ZONE U\nARTICLE U 1 - USES\nTechnical equipment is permitted.\n"
            "Formal review is required.\nTechnical equipment is permitted."
        ),
        (
            "ZONE N\nARTICLE N 1 - USES\nBattery facilities are restricted.\n"
            "Technical equipment is permitted."
        ),
    )
    rows: list[dict[str, object]] = []
    for number, raw_text in enumerate(raw_pages, start=1):
        row: dict[str, object] = {
            "page_number": number,
            "extraction_status": "TEXT",
            "raw_text": raw_text,
            "normalized_search_text": _normalize_search_text(raw_text),
            "character_count": len(raw_text),
            "extraction_error": None,
            "page_content_sha256": "",
        }
        row["page_content_sha256"] = _page_content_sha256(row)
        rows.append(row)
    pages = pd.DataFrame(rows)
    index = PlanningRegulationIndex(
        document_id="doc-1",
        archive_sha256="a" * 64,
        regulation_filename="commune_reglement.pdf",
        source_selection_method="ZONING_NOMFIC",
        source_selection_sha256="b" * 64,
        pdf_relative_path="package/commune_reglement.pdf",
        pdf_size_bytes=100,
        pdf_sha256="c" * 64,
        extraction_library="pypdf",
        extraction_library_version="test-version",
        search_normalization_profile=SEARCH_NORMALIZATION_PROFILE,
        page_hash_schema_version=PAGE_HASH_SCHEMA_VERSION,
        index_hash_schema_version=INDEX_HASH_SCHEMA_VERSION,
        total_page_count=len(pages),
        pages_content_sha256=_pages_content_sha256(pages),
        index_content_sha256="d" * 64,
        pages=pages,
    )
    return replace(index, index_content_sha256=_index_content_sha256(index))


def _zones(index: PlanningRegulationIndex) -> pd.DataFrame:
    return pd.DataFrame(
        {
            "planning_zone_id": ["ZONE-U", "ZONE-UA", "ZONE-N"],
            "source_zone_id": ["SRC-U", "SRC-UA", "SRC-N"],
            "zone_label_raw": ["U", "Ua", "N"],
            "source_document_id": index.document_id,
            "source_archive_sha256": index.archive_sha256,
            "source_layer": "ZONE",
        }
    )


def _relations(index: PlanningRegulationIndex) -> pd.DataFrame:
    rows = (
        ("P-1", "ZONE-U", "SRC-U", "U", "AREA_OVERLAP", 100.0, 100.0),
        ("P-2", "ZONE-U", "SRC-U", "U", "AREA_OVERLAP", 60.0, 60.0),
        ("P-2", "ZONE-UA", "SRC-UA", "Ua", "AREA_OVERLAP", 40.0, 40.0),
        ("P-3", "ZONE-U", "SRC-U", "U", "AREA_OVERLAP", 60.0, 60.0),
        ("P-3", "ZONE-N", "SRC-N", "N", "AREA_OVERLAP", 40.0, 40.0),
        ("P-4", "ZONE-N", "SRC-N", "N", "TOUCH_ONLY", 0.0, 0.0),
    )
    return pd.DataFrame(
        [
            {
                "parcel_id": parcel_id,
                "planning_zone_id": planning_zone_id,
                "source_zone_id": source_zone_id,
                "zone_label_raw": label,
                "relation_type": relation_type,
                "intersection_area_m2": area,
                "parcel_share_pct": share,
                "zone_share_pct": area / 10.0,
                "source_document_id": index.document_id,
                "source_archive_sha256": index.archive_sha256,
                "source_layer": "ZONE",
                "parcel_metric_area_m2": 100.0,
                "zone_area_m2": 1000.0,
            }
            for (
                parcel_id,
                planning_zone_id,
                source_zone_id,
                label,
                relation_type,
                area,
                share,
            ) in rows
        ]
    )


def _structure_config(index: PlanningRegulationIndex) -> PlanningRegulationStructureConfig:
    return PlanningRegulationStructureConfig.model_validate(
        {
            "schema_version": 2,
            "structure_profile": "synthetic_v1",
            "document_lock": {
                "document_id": index.document_id,
                "pdf_sha256": index.pdf_sha256,
                "pages_content_sha256": index.pages_content_sha256,
                "index_content_sha256": index.index_content_sha256,
                "normalization_profile": index.search_normalization_profile,
            },
            "document_layout": {
                "body_start_page": 1,
                "table_of_contents_pages": [],
                "max_heading_continuation_lines": 0,
                "include_table_of_contents_in_topic_evidence": False,
            },
            "heading_patterns": {
                "zone_chapter": [r"^ZONE\s+(?P<label>[A-Za-z0-9]+)$"],
                "article": [
                    r"^ARTICLE\s+(?P<zone>[A-Za-z0-9]+)\s+(?P<number>\d+)\s*-\s*(?P<title>.*)$"
                ],
                "general_section": [
                    r"^ARTICLE\s+(?P<number>\d+)\s*-\s*(?P<title>.*)$"
                ],
                "continuation": [],
            },
            "ignored_patterns": {"page_headers": [], "page_footers": []},
            "zone_aliases": {"Ua": "U"},
            "topics": {"technical": ["technical equipment"]},
            "topic_match_policy": {
                "boundary_mode": "token",
                "overlap_resolution": "longest_match",
            },
            "topic_context_characters": 20,
        }
    )


def _parcels(index: PlanningRegulationIndex) -> gpd.GeoDataFrame:
    frame = gpd.GeoDataFrame(
        {
            "parcel_id": ["P-1", "P-2", "P-3", "P-4"],
            "dominant_planning_zone_id": ["ZONE-U", "ZONE-U", "ZONE-U", None],
            "planning_surface_relation_count": [0, 1, 2, 0],
            "prescription_surface_relation_count": [0, 1, 1, 0],
            "information_surface_relation_count": [0, 0, 1, 0],
            "planning_line_relation_count": [0, 0, 0, 0],
            "planning_point_relation_count": [0, 0, 0, 0],
            "planning_document_id": index.document_id,
            "planning_archive_sha256": index.archive_sha256,
            "planning_feature_document_id": index.document_id,
            "planning_feature_archive_sha256": index.archive_sha256,
            "prior_fact": ["one", "two", "three", "four"],
        },
        geometry=[
            Polygon([(x, 0), (x + 10, 0), (x + 10, 10), (x, 10), (x, 0)])
            for x in (0, 20, 40, 60)
        ],
        crs="EPSG:2154",
        index=pd.Index([10, 20, 30, 40], name="source_row"),
    )
    return frame


def _policy(index, structure, config, zones, relations) -> BessZoningPolicyConfig:
    sections = structure.sections
    u_article = sections.loc[
        sections["section_type"].eq("ARTICLE")
        & sections["zone_chapter_label"].eq("U")
    ].iloc[0]
    n_article = sections.loc[
        sections["section_type"].eq("ARTICLE")
        & sections["zone_chapter_label"].eq("N")
    ].iloc[0]
    fragments = planning_regulation_section_page_fragments(
        index, zones, relations, config, structure
    ).set_index(["section_id", "page_number"])
    u_positive = "Technical equipment is permitted."
    u_condition = "Formal review is required."
    n_excerpt = "Battery facilities are restricted."

    def evidence(
        evidence_id: str,
        section_id: str,
        page_number: int,
        kind: str,
        direction: str,
        excerpt: str,
        note: str,
    ) -> dict[str, object]:
        fragment = fragments.loc[(section_id, page_number)]
        raw = fragment["raw_text"]
        start = raw.index(excerpt)
        return {
            "evidence_id": evidence_id,
            "section_id": section_id,
            "page_number": page_number,
            "evidence_kind": kind,
            "evidence_direction": direction,
            "exact_raw_excerpt": excerpt,
            "excerpt_sha256": sha256(excerpt.encode()).hexdigest(),
            "section_page_fragment_sha256": fragment[
                "section_page_fragment_sha256"
            ],
            "excerpt_start": start,
            "excerpt_end": start + len(excerpt),
            "interpretation_note": note,
        }

    return BessZoningPolicyConfig.model_validate(
        {
            "schema_version": 2,
            "policy_profile": "synthetic_policy_v1",
            "planning_precheck_scope": "WRITTEN_ZONING_REGULATION_ONLY",
            "source_lock": {
                "document_id": index.document_id,
                "archive_sha256": index.archive_sha256,
                "pdf_sha256": index.pdf_sha256,
                "index_content_sha256": index.index_content_sha256,
                "structure_result_content_sha256": (
                    structure.structure_result_content_sha256
                ),
                "structure_profile": structure.structure_profile,
            },
            "required_zone_article_numbers": ["1", "2"],
            "chapters": [
                {
                    "resolved_zone_chapter_label": "U",
                    "review_completeness": "COMPLETE_FOR_WRITTEN_ZONING_PRECHECK",
                    "reviewed_section_ids": [u_article["section_id"]],
                    "review_note": "The required use-control article was reviewed.",
                    "zoning_precheck_status": "CONDITIONAL_REVIEW",
                    "zoning_precheck_confidence": "MEDIUM",
                    "rationale": "The source states a review condition.",
                    "missing_information": "Formal classification and review.",
                    "evidence": [
                        evidence(
                            "E-U-POSITIVE",
                            u_article["section_id"],
                            2,
                            "USE_PERMISSION",
                            "SUPPORTS_POTENTIAL_COMPATIBILITY",
                            u_positive,
                            "This is positive route evidence only.",
                        ),
                        evidence(
                            "E-U-CONDITION",
                            u_article["section_id"],
                            2,
                            "TECHNICAL_EQUIPMENT_RULE",
                            "CONDITION",
                            u_condition,
                            "This is a condition only.",
                        ),
                    ],
                },
                {
                    "resolved_zone_chapter_label": "N",
                    "review_completeness": "COMPLETE_FOR_WRITTEN_ZONING_PRECHECK",
                    "reviewed_section_ids": [n_article["section_id"]],
                    "review_note": "The required use-control article was reviewed.",
                    "zoning_precheck_status": "LIKELY_DIFFICULT",
                    "zoning_precheck_confidence": "HIGH",
                    "rationale": "The source states a relevant restriction.",
                    "missing_information": "Formal classification and review.",
                    "evidence": [
                        evidence(
                            "E-N-1",
                            n_article["section_id"],
                            3,
                            "USE_RESTRICTION",
                            "SUPPORTS_DIFFICULTY",
                            n_excerpt,
                            "This is difficulty evidence only.",
                        )
                    ],
                },
            ],
        }
    )


@pytest.fixture
def inputs():
    index = _index()
    zones = _zones(index)
    relations = _relations(index)
    config = _structure_config(index)
    structure = structure_planning_regulation(index, zones, relations, config)
    parcels = _parcels(index)
    policy = _policy(index, structure, config, zones, relations)
    return index, structure, config, zones, relations, parcels, policy


@pytest.fixture
def valid_result(inputs):
    return interpret_bess_zoning(*inputs)


def _payload(policy: BessZoningPolicyConfig) -> dict[str, object]:
    return policy.model_dump(mode="python")


def _validate(inputs, result) -> None:
    validate_bess_zoning_precheck(*inputs, result)


def test_package_exports_precheck_api() -> None:
    for name in (
        "BessZoningPolicyConfig",
        "BessZoningPrecheckError",
        "BessZoningPrecheckResult",
        "interpret_bess_zoning",
        "load_bess_zoning_policy_config",
        "planning_regulation_section_page_fragments",
        "validate_bess_zoning_precheck",
    ):
        assert name in stages.__all__


def test_valid_locked_policy_builds_complete_outputs(inputs, valid_result) -> None:
    index, structure, _, zones, relations, parcels, policy = inputs
    result = valid_result
    _validate(inputs, result)
    assert tuple(result.chapter_policy.columns) == CHAPTER_POLICY_COLUMNS
    assert tuple(result.source_zone_policy.columns) == SOURCE_ZONE_POLICY_COLUMNS
    assert tuple(result.parcel_zone_interpretations.columns) == PARCEL_ZONE_POLICY_COLUMNS
    assert len(result.chapter_policy) == 2
    assert len(result.source_zone_policy) == 3
    assert len(result.parcel_zone_interpretations) == 5
    assert len(result.parcels) == len(parcels)
    assert result.policy_schema_version == 2
    assert result.result_hash_schema_version == 2
    assert tuple(result.evidence_catalog.columns) == EVIDENCE_CATALOG_COLUMNS
    assert result.planning_precheck_scope == "WRITTEN_ZONING_REGULATION_ONLY"
    assert result.touch_only_relation_count == 1
    assert result.document_id == index.document_id
    assert result.structure_result_content_sha256 == structure.structure_result_content_sha256
    assert result.zoning_relation_hash_columns == tuple(relations.columns)
    assert set(result.source_zone_policy["source_zone_label_raw"]) == set(
        zones["zone_label_raw"]
    )
    assert result.policy_profile == policy.policy_profile


@pytest.mark.parametrize(
    "field",
    [
        "document_id",
        "archive_sha256",
        "pdf_sha256",
        "index_content_sha256",
        "structure_result_content_sha256",
        "structure_profile",
    ],
)
def test_source_lock_mismatch_is_rejected(inputs, field: str) -> None:
    *sources, policy = inputs
    payload = _payload(policy)
    payload["source_lock"][field] = "f" * 64 if "sha256" in field else "wrong"
    bad = BessZoningPolicyConfig.model_validate(payload)
    with pytest.raises(BessZoningPrecheckError, match="differs from factual source"):
        interpret_bess_zoning(*sources, bad)


def test_missing_and_extra_chapter_are_rejected(inputs) -> None:
    *sources, policy = inputs
    missing_payload = _payload(policy)
    missing_payload["chapters"] = missing_payload["chapters"][:-1]
    with pytest.raises(BessZoningPrecheckError, match="completeness differs"):
        interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(missing_payload))
    extra_payload = _payload(policy)
    extra = dict(extra_payload["chapters"][0])
    extra["resolved_zone_chapter_label"] = "EXTRA"
    extra["evidence"] = []
    extra["zoning_precheck_status"] = "UNKNOWN"
    extra_payload["chapters"] = (*extra_payload["chapters"], extra)
    with pytest.raises(BessZoningPrecheckError, match="extra=.*EXTRA"):
        interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(extra_payload))


def test_duplicate_chapter_and_evidence_id_are_rejected(inputs) -> None:
    policy = inputs[-1]
    chapter_payload = _payload(policy)
    chapter_payload["chapters"] = (
        *chapter_payload["chapters"],
        chapter_payload["chapters"][0],
    )
    with pytest.raises(ValueError, match="chapter policy labels must be unique"):
        BessZoningPolicyConfig.model_validate(chapter_payload)
    evidence_payload = _payload(policy)
    evidence_payload["chapters"][1]["evidence"][0]["evidence_id"] = "E-U-POSITIVE"
    with pytest.raises(ValueError, match="evidence IDs must be globally unique"):
        BessZoningPolicyConfig.model_validate(evidence_payload)


def test_one_excerpt_cannot_be_reused_with_contradictory_directions(inputs) -> None:
    payload = _payload(inputs[-1])
    first = dict(payload["chapters"][0]["evidence"][1])
    second = dict(first)
    first["evidence_direction"] = "SUPPORTS_POTENTIAL_COMPATIBILITY"
    second["evidence_id"] = "E-U-2"
    second["evidence_direction"] = "SUPPORTS_DIFFICULTY"
    payload["chapters"][0]["evidence"] = (first, second)
    with pytest.raises(ValueError, match="contradictory directions"):
        BessZoningPolicyConfig.model_validate(payload)


@pytest.mark.parametrize("status", ["ALLOWED", "FORBIDDEN", "PROHIBITED"])
def test_forbidden_or_invalid_final_status_is_rejected(inputs, status: str) -> None:
    payload = _payload(inputs[-1])
    payload["chapters"][0]["zoning_precheck_status"] = status
    with pytest.raises(ValueError):
        BessZoningPolicyConfig.model_validate(payload)


def test_invalid_confidence_and_unknown_field_are_rejected(inputs) -> None:
    payload = _payload(inputs[-1])
    payload["chapters"][0]["zoning_precheck_confidence"] = "CERTAIN"
    with pytest.raises(ValueError):
        BessZoningPolicyConfig.model_validate(payload)
    payload = _payload(inputs[-1])
    payload["automatic_classifier"] = True
    with pytest.raises(ValueError):
        BessZoningPolicyConfig.model_validate(payload)


def test_duplicate_yaml_key_is_rejected(tmp_path: Path) -> None:
    path = tmp_path / "duplicate.yaml"
    path.write_text(
        "schema_version: 2\nschema_version: 2\n",
        encoding="utf-8",
    )
    with pytest.raises(BessZoningPrecheckError, match="Duplicate YAML policy key"):
        load_bess_zoning_policy_config(path)


def test_policy_schema_version_one_is_rejected(inputs) -> None:
    payload = _payload(inputs[-1])
    payload["schema_version"] = 1
    with pytest.raises(ValueError, match="unsupported BESS zoning policy schema"):
        BessZoningPolicyConfig.model_validate(payload)


@pytest.mark.parametrize(
    ("kind", "direction"),
    [
        ("USE_RESTRICTION", "SUPPORTS_POTENTIAL_COMPATIBILITY"),
        ("USE_PERMISSION", "SUPPORTS_DIFFICULTY"),
        ("ACCESS_OR_NETWORK_CONDITION", "SUPPORTS_POTENTIAL_COMPATIBILITY"),
    ],
)
def test_evidence_kind_direction_contract_is_strict(
    inputs, kind: str, direction: str
) -> None:
    payload = _payload(inputs[-1])
    evidence = payload["chapters"][0]["evidence"][0]
    evidence["evidence_kind"] = kind
    evidence["evidence_direction"] = direction
    with pytest.raises(ValueError, match="kind and direction are incompatible"):
        BessZoningPolicyConfig.model_validate(payload)


def test_valid_exact_evidence_is_preserved(inputs, valid_result) -> None:
    policy = inputs[-1]
    excerpt = policy.chapters[0].evidence[0].exact_raw_excerpt
    assert excerpt == "Technical equipment is permitted."
    assert policy.chapters[0].evidence[0].excerpt_sha256 == sha256(
        excerpt.encode()
    ).hexdigest()
    assert valid_result.chapter_policy.iloc[0]["evidence_ids"] == (
        "E-U-POSITIVE",
        "E-U-CONDITION",
    )


def test_absent_excerpt_and_section_page_mismatch_are_rejected(inputs) -> None:
    *sources, policy = inputs
    payload = _payload(policy)
    excerpt = "Not present in the indexed source."
    payload["chapters"][0]["evidence"][0]["exact_raw_excerpt"] = excerpt
    payload["chapters"][0]["evidence"][0]["excerpt_sha256"] = sha256(
        excerpt.encode()
    ).hexdigest()
    with pytest.raises(BessZoningPrecheckError, match="offsets"):
        interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(payload))
    payload = _payload(policy)
    payload["chapters"][0]["evidence"][0]["page_number"] = 3
    with pytest.raises(BessZoningPrecheckError, match="section/page fragment"):
        interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(payload))


def test_excerpt_hash_and_length_are_rejected(inputs) -> None:
    payload = _payload(inputs[-1])
    payload["chapters"][0]["evidence"][0]["excerpt_sha256"] = "f" * 64
    with pytest.raises(ValueError, match="excerpt SHA256 differs"):
        BessZoningPolicyConfig.model_validate(payload)
    payload = _payload(inputs[-1])
    excerpt = "x" * 601
    payload["chapters"][0]["evidence"][0]["exact_raw_excerpt"] = excerpt
    payload["chapters"][0]["evidence"][0]["excerpt_sha256"] = sha256(
        excerpt.encode()
    ).hexdigest()
    with pytest.raises(ValueError):
        BessZoningPolicyConfig.model_validate(payload)


@pytest.mark.parametrize(
    ("status", "direction", "message"),
    [
        (
            "POTENTIALLY_COMPATIBLE",
            "CONTEXT_ONLY",
            "requires a positive route",
        ),
        ("LIKELY_DIFFICULT", "CONTEXT_ONLY", "requires difficulty"),
        ("CONDITIONAL_REVIEW", "CONTEXT_ONLY", "requires a positive route"),
    ],
)
def test_status_requires_consistent_evidence(
    inputs, status: str, direction: str, message: str
) -> None:
    payload = _payload(inputs[-1])
    payload["chapters"][0]["zoning_precheck_status"] = status
    for evidence in payload["chapters"][0]["evidence"]:
        evidence["evidence_direction"] = direction
    with pytest.raises(ValueError, match=message):
        BessZoningPolicyConfig.model_validate(payload)


def test_condition_alone_cannot_create_conditional_review(inputs) -> None:
    payload = _payload(inputs[-1])
    payload["chapters"][0]["zoning_precheck_status"] = "CONDITIONAL_REVIEW"
    payload["chapters"][0]["evidence"] = [
        payload["chapters"][0]["evidence"][1]
    ]
    payload["chapters"][0]["evidence"][0]["evidence_direction"] = "CONDITION"
    with pytest.raises(ValueError, match="positive route"):
        BessZoningPolicyConfig.model_validate(payload)


def test_condition_only_unknown_succeeds(inputs) -> None:
    payload = _payload(inputs[-1])
    chapter = payload["chapters"][0]
    chapter["zoning_precheck_status"] = "UNKNOWN"
    chapter["zoning_precheck_confidence"] = "LOW"
    chapter["evidence"] = [chapter["evidence"][1]]
    policy = BessZoningPolicyConfig.model_validate(payload)
    assert policy.chapters[0].zoning_precheck_status == "UNKNOWN"


def test_positive_condition_and_conflict_status_routes(inputs) -> None:
    payload = _payload(inputs[-1])
    assert BessZoningPolicyConfig.model_validate(payload).chapters[
        0
    ].zoning_precheck_status == "CONDITIONAL_REVIEW"
    conflict = _payload(inputs[-1])
    conflict["chapters"][0]["evidence"][1][
        "evidence_direction"
    ] = "SUPPORTS_DIFFICULTY"
    policy = BessZoningPolicyConfig.model_validate(conflict)
    assert policy.chapters[0].zoning_precheck_status == "CONDITIONAL_REVIEW"


def test_difficulty_and_positive_only_status_routes(inputs) -> None:
    difficult = _payload(inputs[-1])
    chapter = difficult["chapters"][0]
    chapter["zoning_precheck_status"] = "LIKELY_DIFFICULT"
    chapter["evidence"] = [chapter["evidence"][1]]
    chapter["evidence"][0]["evidence_direction"] = "SUPPORTS_DIFFICULTY"
    assert BessZoningPolicyConfig.model_validate(difficult).chapters[
        0
    ].zoning_precheck_status == "LIKELY_DIFFICULT"
    potential = _payload(inputs[-1])
    chapter = potential["chapters"][0]
    chapter["zoning_precheck_status"] = "POTENTIALLY_COMPATIBLE"
    chapter["evidence"] = [chapter["evidence"][0]]
    assert BessZoningPolicyConfig.model_validate(potential).chapters[
        0
    ].zoning_precheck_status == "POTENTIALLY_COMPATIBLE"


def test_incomplete_review_requires_unknown_low(inputs) -> None:
    payload = _payload(inputs[-1])
    chapter = payload["chapters"][0]
    chapter["review_completeness"] = "INCOMPLETE"
    chapter["zoning_precheck_status"] = "UNKNOWN"
    chapter["zoning_precheck_confidence"] = "LOW"
    chapter["evidence"] = []
    assert BessZoningPolicyConfig.model_validate(payload).chapters[
        0
    ].review_completeness == "INCOMPLETE"
    for field, value in (
        ("zoning_precheck_status", "CONDITIONAL_REVIEW"),
        ("zoning_precheck_confidence", "MEDIUM"),
    ):
        invalid = _payload(inputs[-1])
        candidate = invalid["chapters"][0]
        candidate["review_completeness"] = "INCOMPLETE"
        candidate["zoning_precheck_status"] = "UNKNOWN"
        candidate["zoning_precheck_confidence"] = "LOW"
        candidate["evidence"] = []
        candidate[field] = value
        with pytest.raises(ValueError, match="incomplete review"):
            BessZoningPolicyConfig.model_validate(invalid)


def test_unknown_is_accepted_when_evidence_is_insufficient(inputs) -> None:
    *sources, policy = inputs
    payload = _payload(policy)
    payload["chapters"][0]["zoning_precheck_status"] = "UNKNOWN"
    payload["chapters"][0]["evidence"] = []
    result = interpret_bess_zoning(
        *sources, BessZoningPolicyConfig.model_validate(payload)
    )
    assert result.chapter_policy.iloc[0]["zoning_precheck_status"] == "UNKNOWN"


def test_reviewed_sections_cover_required_articles(inputs) -> None:
    *sources, policy = inputs
    index, structure = inputs[:2]
    payload = _payload(policy)
    chapter_id = structure.sections.loc[
        structure.sections["section_type"].eq("ZONE_CHAPTER")
        & structure.sections["zone_chapter_label"].eq("U"),
        "section_id",
    ].iloc[0]
    payload["chapters"][0]["reviewed_section_ids"] = [chapter_id]
    with pytest.raises(BessZoningPrecheckError, match="omits required reviewed"):
        interpret_bess_zoning(
            *sources, BessZoningPolicyConfig.model_validate(payload)
        )
    assert index.document_id == "doc-1"


def test_evidence_must_be_inside_reviewed_sections(inputs) -> None:
    *sources, policy = inputs
    structure = inputs[1]
    payload = _payload(policy)
    payload["required_zone_article_numbers"] = ["2"]
    chapter_id = structure.sections.loc[
        structure.sections["section_type"].eq("ZONE_CHAPTER")
        & structure.sections["zone_chapter_label"].eq("U"),
        "section_id",
    ].iloc[0]
    payload["chapters"][0]["reviewed_section_ids"] = [chapter_id]
    with pytest.raises(BessZoningPrecheckError, match="outside reviewed sections"):
        interpret_bess_zoning(
            *sources, BessZoningPolicyConfig.model_validate(payload)
        )


def test_review_cannot_claim_another_chapter_section(inputs) -> None:
    *sources, policy = inputs
    structure = inputs[1]
    payload = _payload(policy)
    n_article = structure.sections.loc[
        structure.sections["section_type"].eq("ARTICLE")
        & structure.sections["zone_chapter_label"].eq("N"),
        "section_id",
    ].iloc[0]
    payload["chapters"][0]["reviewed_section_ids"] += (n_article,)
    with pytest.raises(BessZoningPrecheckError, match="another chapter"):
        interpret_bess_zoning(
            *sources, BessZoningPolicyConfig.model_validate(payload)
        )


def test_general_section_review_is_explicit_and_valid(inputs) -> None:
    *sources, policy = inputs
    structure = inputs[1]
    payload = _payload(policy)
    general_id = structure.sections.loc[
        structure.sections["section_type"].eq("GENERAL"), "section_id"
    ].iloc[0]
    payload["chapters"][0]["reviewed_section_ids"] += (general_id,)
    result = interpret_bess_zoning(
        *sources, BessZoningPolicyConfig.model_validate(payload)
    )
    reviewed = result.chapter_policy.set_index("resolved_zone_chapter_label").loc[
        "U", "reviewed_section_ids"
    ]
    assert general_id in reviewed


def test_exact_section_page_occurrence_is_auditable(inputs, valid_result) -> None:
    index, structure, config, zones, relations, *_ = inputs
    fragments = planning_regulation_section_page_fragments(
        index, zones, relations, config, structure
    ).set_index(["section_id", "page_number"])
    for row in valid_result.evidence_catalog.to_dict("records"):
        fragment = fragments.loc[(row["section_id"], row["page_number"])]
        assert row["section_page_fragment_sha256"] == fragment[
            "section_page_fragment_sha256"
        ]
        assert fragment["raw_text"][row["excerpt_start"] : row["excerpt_end"]] == row[
            "exact_raw_excerpt"
        ]


def test_repeated_excerpt_occurrence_is_bound_to_policy(inputs, valid_result) -> None:
    index, structure, config, zones, relations, *_ = inputs
    row_index = valid_result.evidence_catalog.index[
        valid_result.evidence_catalog["evidence_id"].eq("E-U-POSITIVE")
    ][0]
    row = valid_result.evidence_catalog.loc[row_index]
    fragments = planning_regulation_section_page_fragments(
        index, zones, relations, config, structure
    ).set_index(["section_id", "page_number"])
    raw = fragments.loc[(row["section_id"], row["page_number"]), "raw_text"]
    first = raw.index(row["exact_raw_excerpt"])
    second = raw.index(row["exact_raw_excerpt"], first + 1)
    assert second > first

    catalog = valid_result.evidence_catalog.copy(deep=True)
    catalog.loc[row_index, "excerpt_start"] = second
    catalog.loc[row_index, "excerpt_end"] = second + len(row["exact_raw_excerpt"])
    coordinated = _result_with_hashes(
        replace(valid_result, evidence_catalog=catalog)
    )
    with pytest.raises(BessZoningPrecheckError, match="differs from rebuilt"):
        _validate(inputs, coordinated)


@pytest.mark.parametrize("mutation", ["page", "fragment_hash", "start", "end"])
def test_wrong_occurrence_identity_is_rejected(inputs, mutation: str) -> None:
    *sources, policy = inputs
    payload = _payload(policy)
    evidence = payload["chapters"][0]["evidence"][0]
    if mutation == "page":
        evidence["page_number"] = 1
    elif mutation == "fragment_hash":
        evidence["section_page_fragment_sha256"] = "f" * 64
    elif mutation == "start":
        evidence["excerpt_start"] += 1
    else:
        evidence["excerpt_end"] -= 1
    with pytest.raises(BessZoningPrecheckError, match="fragment|offset"):
        interpret_bess_zoning(
            *sources, BessZoningPolicyConfig.model_validate(payload)
        )


def test_exact_and_alias_mappings_are_inherited_without_prefix_logic(valid_result) -> None:
    policies = valid_result.source_zone_policy.set_index("source_zone_label_raw")
    assert policies.loc["U", "mapping_status"] == "EXACT"
    assert policies.loc["Ua", "mapping_status"] == "CONFIG_ALIAS"
    assert policies.loc["Ua", "resolved_zone_chapter_label"] == "U"
    assert policies.loc["Ua", "zoning_precheck_status"] == policies.loc[
        "U", "zoning_precheck_status"
    ]


def test_unmapped_dominant_zone_is_rejected(inputs) -> None:
    index, structure, config, zones, relations, parcels, policy = inputs
    mapping = structure.zone_mapping.copy()
    mapping.loc[mapping["source_zone_label_raw"].eq("U"), [
        "resolved_zone_chapter_label",
        "matched_section_id",
    ]] = None
    mapping.loc[mapping["source_zone_label_raw"].eq("U"), "mapping_status"] = "UNMAPPED"
    mapping.loc[mapping["source_zone_label_raw"].eq("U"), "mapping_method"] = "NONE"
    mutated = _structure_with_hashes(replace(structure, zone_mapping=mapping))
    changed_policy = policy.model_copy(
        update={
            "source_lock": policy.source_lock.model_copy(
                update={
                    "structure_result_content_sha256": (
                        mutated.structure_result_content_sha256
                    )
                }
            )
        },
    )
    with pytest.raises(BessZoningPrecheckError, match="Factual regulation structure"):
        interpret_bess_zoning(
            index, mutated, config, zones, relations, parcels, changed_policy
        )


def test_parcel_aggregation_preserves_conflicts_and_touch_only(valid_result) -> None:
    parcels = valid_result.parcels.set_index("parcel_id")
    assert parcels.loc["P-1", "zoning_precheck_status"] == "CONDITIONAL_REVIEW"
    assert parcels.loc["P-1", "positive_area_zone_count"] == 1
    assert parcels.loc["P-2", "zoning_precheck_status"] == "CONDITIONAL_REVIEW"
    assert parcels.loc["P-2", "positive_area_zone_count"] == 2
    assert parcels.loc["P-2", "distinct_zone_status_count"] == 1
    assert parcels.loc["P-3", "zoning_precheck_status"] == "MIXED_REVIEW_REQUIRED"
    assert parcels.loc["P-3", "dominant_zone_precheck_status"] == "CONDITIONAL_REVIEW"
    assert parcels.loc["P-3", "non_dominant_different_status_count"] == 1
    assert parcels.loc["P-4", "zoning_precheck_status"] == "UNKNOWN"
    assert parcels.loc["P-4", "positive_area_zone_count"] == 0
    assert parcels.loc["P-4", "touch_only_zone_count"] == 1
    assert pd.isna(parcels.loc["P-4", "dominant_zone_precheck_status"])
    assert valid_result.touch_only_relation_count == 1
    assert "P-4" not in set(valid_result.parcel_zone_interpretations["parcel_id"])


def test_prior_parcel_fields_geometry_order_index_and_crs_are_preserved(
    inputs, valid_result
) -> None:
    original = inputs[5]
    prior = valid_result.parcels.loc[:, original.columns]
    assert_geodataframe_equal(prior, original)
    assert valid_result.parcels.index.equals(original.index)
    assert valid_result.parcels.crs == original.crs
    assert valid_result.parcels["planning_surface_relation_count"].equals(
        original["planning_surface_relation_count"]
    )
    assert valid_result.parcels["non_zoning_planning_features_interpreted"].eq(
        False
    ).all()
    assert valid_result.parcels["zoning_precheck_requires_formal_review"].eq(
        True
    ).all()


def test_inputs_are_not_mutated(inputs) -> None:
    _, structure, _, zones, relations, parcels, _ = inputs
    zone_snapshot = zones.copy(deep=True)
    relation_snapshot = relations.copy(deep=True)
    parcel_snapshot = parcels.copy(deep=True)
    section_snapshot = structure.sections.copy(deep=True)
    interpret_bess_zoning(*inputs)
    pd.testing.assert_frame_equal(zones, zone_snapshot)
    pd.testing.assert_frame_equal(relations, relation_snapshot)
    assert_geodataframe_equal(parcels, parcel_snapshot)
    pd.testing.assert_frame_equal(structure.sections, section_snapshot)


def test_policy_change_after_result_creation_is_rejected(inputs, valid_result) -> None:
    payload = _payload(inputs[-1])
    payload["chapters"][0]["rationale"] = "Changed checked-in rationale."
    changed = BessZoningPolicyConfig.model_validate(payload)
    with pytest.raises(BessZoningPrecheckError, match="policy_config_sha256"):
        validate_bess_zoning_precheck(*inputs[:-1], changed, valid_result)


def test_evidence_change_after_result_creation_is_rejected(inputs, valid_result) -> None:
    payload = _payload(inputs[-1])
    excerpt = "Technical equipment is permitted"
    evidence = payload["chapters"][0]["evidence"][0]
    evidence["exact_raw_excerpt"] = excerpt
    evidence["excerpt_sha256"] = sha256(excerpt.encode()).hexdigest()
    changed = BessZoningPolicyConfig.model_validate(payload)
    with pytest.raises(BessZoningPrecheckError):
        validate_bess_zoning_precheck(*inputs[:-1], changed, valid_result)


def test_zoning_relation_and_zone_mapping_changes_are_rejected(inputs, valid_result) -> None:
    index, structure, config, zones, relations, parcels, policy = inputs
    changed_relations = relations.copy()
    changed_relations.loc[0, "intersection_area_m2"] = 99.0
    changed_relations.loc[0, "parcel_share_pct"] = 99.0
    changed_relations.loc[0, "zone_share_pct"] = 9.9
    with pytest.raises(BessZoningPrecheckError, match="Factual regulation structure"):
        validate_bess_zoning_precheck(
            index,
            structure,
            config,
            zones,
            changed_relations,
            parcels,
            policy,
            valid_result,
        )


def test_structure_config_and_hierarchy_changes_are_rejected(inputs) -> None:
    index, structure, config, zones, relations, parcels, policy = inputs
    changed_config = config.model_copy(update={"structure_profile": "changed"})
    with pytest.raises(BessZoningPrecheckError, match="Factual regulation structure"):
        interpret_bess_zoning(
            index,
            structure,
            changed_config,
            zones,
            relations,
            parcels,
            policy,
        )
    changed_sections = structure.sections.copy(deep=True)
    article = changed_sections["section_type"].eq("ARTICLE")
    changed_sections.loc[article.idxmax(), "parent_section_id"] = "SECTION-UNKNOWN"
    changed_structure = _structure_with_hashes(
        replace(structure, sections=changed_sections)
    )
    changed_policy = policy.model_copy(
        update={
            "source_lock": policy.source_lock.model_copy(
                update={
                    "structure_result_content_sha256": (
                        changed_structure.structure_result_content_sha256
                    )
                }
            )
        }
    )
    with pytest.raises(BessZoningPrecheckError, match="Factual regulation structure"):
        interpret_bess_zoning(
            index,
            changed_structure,
            config,
            zones,
            relations,
            parcels,
            changed_policy,
        )


def test_public_source_complete_validator_is_invoked(inputs, monkeypatch) -> None:
    calls = 0
    original = interpret_module.validate_planning_regulation_structure

    def counted(*args, **kwargs):
        nonlocal calls
        calls += 1
        return original(*args, **kwargs)

    monkeypatch.setattr(
        interpret_module, "validate_planning_regulation_structure", counted
    )
    interpret_bess_zoning(*inputs)
    assert calls >= 1


@pytest.mark.parametrize(
    "column",
    ["parcel_metric_area_m2", "zone_area_m2"],
)
def test_relation_area_denominators_are_required(inputs, column: str) -> None:
    index, structure, config, zones, relations, parcels, policy = inputs
    with pytest.raises(BessZoningPrecheckError):
        interpret_bess_zoning(
            index,
            structure,
            config,
            zones,
            relations.drop(columns=column),
            parcels,
            policy,
        )


@pytest.mark.parametrize(
    "column",
    ["parcel_share_pct", "zone_share_pct"],
)
def test_relation_percentages_must_match_denominators(inputs, column: str) -> None:
    index, structure, config, zones, relations, parcels, policy = inputs
    changed = relations.copy(deep=True)
    changed.loc[0, column] += 1.0
    with pytest.raises(BessZoningPrecheckError):
        interpret_bess_zoning(
            index,
            structure,
            config,
            zones,
            changed,
            parcels,
            policy,
        )


def test_factual_zone_mapping_counts_are_recomputed(inputs) -> None:
    index, structure, config, zones, relations, parcels, policy = inputs
    changed_mapping = structure.zone_mapping.copy(deep=True)
    changed_mapping.loc[0, "candidate_intersection_count"] += 1
    changed_structure = _structure_with_hashes(
        replace(structure, zone_mapping=changed_mapping)
    )
    changed_policy = policy.model_copy(
        update={
            "source_lock": policy.source_lock.model_copy(
                update={
                    "structure_result_content_sha256": (
                        changed_structure.structure_result_content_sha256
                    )
                }
            )
        }
    )
    with pytest.raises(BessZoningPrecheckError, match="Factual regulation structure"):
        interpret_bess_zoning(
            index,
            changed_structure,
            config,
            zones,
            relations,
            parcels,
            changed_policy,
        )
    changed_mapping = structure.zone_mapping.copy()
    changed_mapping.loc[0, "source_zone_label_raw"] = "CHANGED"
    changed_structure = _structure_with_hashes(
        replace(structure, zone_mapping=changed_mapping)
    )
    changed_policy = policy.model_copy(
        update={
            "source_lock": policy.source_lock.model_copy(
                update={
                    "structure_result_content_sha256": (
                        changed_structure.structure_result_content_sha256
                    )
                }
            )
        },
    )
    with pytest.raises(BessZoningPrecheckError):
        validate_bess_zoning_precheck(
            index,
            changed_structure,
            config,
            zones,
            relations,
            parcels,
            changed_policy,
            valid_result,
        )


def test_coordinated_result_mutation_is_rejected(inputs, valid_result) -> None:
    chapter = valid_result.chapter_policy.copy(deep=True)
    chapter.loc[0, "zoning_precheck_confidence"] = "HIGH"
    mutated = _result_with_hashes(replace(valid_result, chapter_policy=chapter))
    with pytest.raises(BessZoningPrecheckError, match="differs from rebuilt"):
        _validate(inputs, mutated)


def test_coordinated_evidence_catalog_mutation_is_rejected(inputs, valid_result) -> None:
    catalog = valid_result.evidence_catalog.copy(deep=True)
    catalog.loc[0, "interpretation_note"] = "Coordinated mutation."
    mutated = _result_with_hashes(
        replace(valid_result, evidence_catalog=catalog)
    )
    with pytest.raises(BessZoningPrecheckError, match="differs from rebuilt"):
        _validate(inputs, mutated)


def test_result_hash_schema_mutation_is_rejected(inputs, valid_result) -> None:
    with pytest.raises(BessZoningPrecheckError, match="result_hash_schema_version"):
        _validate(inputs, replace(valid_result, result_hash_schema_version=1))


def test_relation_identity_change_is_rejected(inputs) -> None:
    index, structure, config, zones, relations, parcels, policy = inputs
    changed = relations.copy()
    changed.loc[0, "source_zone_id"] = "SRC-N"
    with pytest.raises(BessZoningPrecheckError, match="Factual regulation structure"):
        interpret_bess_zoning(
            index, structure, config, zones, changed, parcels, policy
        )


def test_readback_result_validates(tmp_path: Path, inputs, valid_result) -> None:
    chapter_path = tmp_path / "chapter.parquet"
    evidence_path = tmp_path / "evidence.parquet"
    source_path = tmp_path / "source.parquet"
    relation_path = tmp_path / "relations.parquet"
    parcel_path = tmp_path / "parcels.parquet"
    valid_result.evidence_catalog.to_parquet(evidence_path, index=False)
    valid_result.chapter_policy.to_parquet(chapter_path, index=False)
    valid_result.source_zone_policy.to_parquet(source_path, index=False)
    valid_result.parcel_zone_interpretations.to_parquet(relation_path, index=False)
    valid_result.parcels.to_parquet(parcel_path)
    persisted = replace(
        valid_result,
        evidence_catalog=pd.read_parquet(evidence_path),
        chapter_policy=pd.read_parquet(chapter_path),
        source_zone_policy=pd.read_parquet(source_path),
        parcel_zone_interpretations=pd.read_parquet(relation_path),
        parcels=gpd.read_parquet(parcel_path),
    )
    _validate(inputs, persisted)


def test_policy_yaml_roundtrip_is_strict(tmp_path: Path, inputs) -> None:
    policy = inputs[-1]
    path = tmp_path / "policy.yaml"
    import yaml  # type: ignore[import-untyped]

    path.write_text(
        yaml.safe_dump(
            policy.model_dump(mode="json"),
            allow_unicode=True,
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    assert load_bess_zoning_policy_config(path) == policy
