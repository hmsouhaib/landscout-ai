from __future__ import annotations

from dataclasses import replace
from pathlib import Path

import pandas as pd
import pytest

from landscout import stages
from landscout.common.planning_text import normalize_planning_search_text
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
from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureError,
    _line_records,
    _literal_topic_matches,
    _result_with_hashes,
    _section_content_sha256,
    load_planning_regulation_structure_config,
    structure_planning_regulation,
    validate_planning_regulation_structure,
)


def _index(raw_pages: tuple[str, ...] | None = None) -> PlanningRegulationIndex:
    raw_pages = raw_pages or (
        "Test PLU\n1\nZONE U\nARTICLE U 1 - TOC ENTRY",
        "Test PLU\n2\nARTICLE 1 - GENERAL PROVISIONS\nGeneral energy rule.",
        "Test PLU\n3\nZONE U\nCharacter of U.\nARTICLE U 1 - USES\nFirst page energy text.",
        "Test PLU\n4\nSecond page of the same article.\nARTICLE U 2 - NETWORKS\nNetwork text.",
        "Test PLU\n5\nZONE N\nARTICLE N 1 - RISK\nRisk text.",
        "Test PLU\n6\nZONE Z\nARTICLE Z 1 - FIRST\nText.",
        "Test PLU\n7\nZONE Z\nARTICLE Z 2 - SECOND\nText.",
    )
    rows: list[dict[str, object]] = []
    for number, raw_text in enumerate(raw_pages, start=1):
        row: dict[str, object] = {
            "page_number": number,
            "extraction_status": "TEXT",
            "raw_text": raw_text,
            "normalized_search_text": raw_text.casefold(),
            "character_count": len(raw_text),
            "extraction_error": None,
            "page_content_sha256": "",
        }
        # Use the production normalizer rather than this deliberately simple placeholder.
        row["normalized_search_text"] = _normalize_search_text(raw_text)
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


def _config(index: PlanningRegulationIndex) -> PlanningRegulationStructureConfig:
    return PlanningRegulationStructureConfig.model_validate(
        {
            "schema_version": 1,
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
                "table_of_contents_pages": [1],
                "max_heading_continuation_lines": 2,
                "include_table_of_contents_in_topic_evidence": False,
            },
            "heading_patterns": {
                "zone_chapter": [r"^ZONE\s+(?P<label>[A-Za-z0-9]+)$"],
                "article": [
                    r"^ARTICLE\s+(?P<zone>[A-Za-z0-9]+)\s+(?P<number>\d+)\s*[-–—]\s*(?P<title>.*)$"
                ],
                "general_section": [
                    r"^ARTICLE\s+(?P<number>\d+)\s*[-–—]\s*(?P<title>.*)$"
                ],
                "continuation": [r"^[^a-z]*[A-Z][^a-z]*$"],
            },
            "ignored_patterns": {
                "page_headers": [r"^Test PLU$"],
                "page_footers": [r"^\d+$"],
            },
            "zone_aliases": {"Ua": "U"},
            "topics": {"energy": ["energy"], "risk": ["risk"]},
            "topic_match_policy": {
                "boundary_mode": "token",
                "overlap_resolution": "longest_match",
            },
            "topic_context_characters": 20,
        }
    )


def _zones(index: PlanningRegulationIndex) -> pd.DataFrame:
    labels = ["U", "Ua", "X", "UX", "Z"]
    return pd.DataFrame(
        {
            "planning_zone_id": [f"ZONE-{label}" for label in labels],
            "source_zone_id": [f"SRC-{label}" for label in labels],
            "zone_label_raw": labels,
            "source_document_id": index.document_id,
            "source_archive_sha256": index.archive_sha256,
        }
    )


def _intersections(index: PlanningRegulationIndex) -> pd.DataFrame:
    return pd.DataFrame(
        {
            "parcel_id": ["PARCEL-1", "PARCEL-2"],
            "planning_zone_id": ["ZONE-U", "ZONE-Ua"],
            "source_zone_id": ["SRC-U", "SRC-Ua"],
            "zone_label_raw": ["U", "Ua"],
            "relation_type": ["AREA_OVERLAP", "AREA_OVERLAP"],
            "intersection_area_m2": [100.0, 50.0],
            "source_document_id": index.document_id,
            "source_archive_sha256": index.archive_sha256,
        }
    )


@pytest.fixture
def valid_result():
    index = _index()
    result = structure_planning_regulation(
        index, _zones(index), _intersections(index), _config(index)
    )
    return index, result


def _validate(
    index: PlanningRegulationIndex,
    result,
) -> None:
    validate_planning_regulation_structure(
        index,
        _zones(index),
        _intersections(index),
        _config(index),
        result,
    )


def test_package_exports_clean_high_level_api() -> None:
    assert "structure_planning_regulation" in stages.__all__
    assert "validate_planning_regulation_structure" in stages.__all__
    assert not any(name.startswith("_build_") for name in stages.__all__)


@pytest.mark.parametrize(
    "lock_field",
    [
        "document_id",
        "pdf_sha256",
        "pages_content_sha256",
        "index_content_sha256",
        "normalization_profile",
    ],
)
def test_document_lock_mismatch_is_rejected(lock_field: str) -> None:
    index = _index()
    config = _config(index)
    lock = config.document_lock.model_copy(
        update={lock_field: "f" * 64 if "sha256" in lock_field else "wrong"}
    )
    changed = config.model_copy(update={"document_lock": lock})
    with pytest.raises(PlanningRegulationStructureError, match="document lock"):
        structure_planning_regulation(index, _zones(index), _intersections(index), changed)


def test_invalid_regex_and_unknown_yaml_field_are_controlled(tmp_path: Path) -> None:
    index = _index()
    payload = _config(index).model_dump(mode="json")
    payload["heading_patterns"]["zone_chapter"] = ["["]
    payload["unexpected"] = True
    import yaml

    path = tmp_path / "bad.yaml"
    path.write_text(yaml.safe_dump(payload), encoding="utf-8")
    with pytest.raises(PlanningRegulationStructureError):
        load_planning_regulation_structure_config(path)


def test_duplicate_yaml_alias_and_alias_cycle_are_rejected(tmp_path: Path) -> None:
    index = _index()
    config = _config(index).model_dump(mode="json")
    import yaml

    cycle = tmp_path / "cycle.yaml"
    config["zone_aliases"] = {"A": "B", "B": "A"}
    cycle.write_text(yaml.safe_dump(config), encoding="utf-8")
    with pytest.raises(PlanningRegulationStructureError):
        load_planning_regulation_structure_config(cycle)
    duplicate = tmp_path / "duplicate.yaml"
    text = yaml.safe_dump(_config(index).model_dump(mode="json"))
    text = text.replace("zone_aliases:\n", "zone_aliases:\n  A: U\n  A: N\n")
    duplicate.write_text(text, encoding="utf-8")
    with pytest.raises(PlanningRegulationStructureError, match="Duplicate YAML"):
        load_planning_regulation_structure_config(duplicate)


def test_realistic_structure_is_deterministic_and_toc_heading_is_ignored(
    valid_result,
) -> None:
    index, result = valid_result
    _validate(index, result)
    assert result.sections["section_id"].tolist() == [
        f"SECTION-{number:04d}" for number in range(1, len(result.sections) + 1)
    ]
    chapters = result.sections.loc[result.sections["section_type"].eq("ZONE_CHAPTER")]
    assert chapters["zone_chapter_label"].tolist() == ["U", "N", "Z", "Z"]
    assert len(chapters.loc[chapters["zone_chapter_label"].eq("U")]) == 1
    general = result.sections.loc[result.sections["section_type"].eq("GENERAL")].iloc[0]
    assert general["heading_raw"] == "ARTICLE 1 - GENERAL PROVISIONS"
    assert "General energy rule." in general["raw_text"]


def test_zone_article_parent_and_multi_page_text_are_preserved(valid_result) -> None:
    _, result = valid_result
    article = result.sections.loc[
        result.sections["heading_raw"].str.startswith("ARTICLE U 1")
    ].iloc[0]
    parent = result.sections.set_index("section_id").loc[article["parent_section_id"]]
    assert parent["section_type"] == "ZONE_CHAPTER"
    assert tuple(article["page_numbers"]) == (3, 4)
    assert "First page energy text." in article["raw_text"]
    assert "Second page of the same article." in article["raw_text"]


def test_exact_alias_unmapped_ambiguous_and_no_fuzzy_mapping(valid_result) -> None:
    _, result = valid_result
    mappings = result.zone_mapping.set_index("source_zone_label_raw")
    assert mappings.at["U", "mapping_status"] == "EXACT"
    assert mappings.at["Ua", "mapping_status"] == "CONFIG_ALIAS"
    assert mappings.at["X", "mapping_status"] == "UNMAPPED"
    assert mappings.at["UX", "mapping_status"] == "UNMAPPED"
    assert mappings.at["Z", "mapping_status"] == "AMBIGUOUS"
    assert mappings.at["X", "dominant_candidate_count"] == 0


def test_topic_evidence_distinguishes_general_and_zone_specific(valid_result) -> None:
    _, result = valid_result
    energy = result.topic_evidence.loc[result.topic_evidence["topic"].eq("energy")]
    assert set(energy["evidence_scope"]) == {"GENERAL_RULE", "ZONE_SPECIFIC_RULE"}
    assert set(energy["occurrence_count"]) == {1}
    assert all(context for context in energy["raw_context"])


def test_inputs_are_not_mutated() -> None:
    index = _index()
    zones = _zones(index)
    intersections = _intersections(index)
    pages_before = index.pages.copy(deep=True)
    zones_before = zones.copy(deep=True)
    intersections_before = intersections.copy(deep=True)
    structure_planning_regulation(index, zones, intersections, _config(index))
    pd.testing.assert_frame_equal(index.pages, pages_before)
    pd.testing.assert_frame_equal(zones, zones_before)
    pd.testing.assert_frame_equal(intersections, intersections_before)


@pytest.mark.parametrize(
    "frame_name,hash_name,column",
    [
        ("sections", "sections_content_sha256", "raw_text"),
        ("zone_mapping", "zone_map_content_sha256", "candidate_parcel_count"),
        ("topic_evidence", "topic_evidence_content_sha256", "raw_context"),
    ],
)
def test_coordinated_frame_mutation_is_rejected(
    valid_result,
    frame_name: str,
    hash_name: str,
    column: str,
) -> None:
    index, result = valid_result
    frame = getattr(result, frame_name).copy(deep=True)
    if column == "candidate_parcel_count":
        frame.loc[0, column] = int(frame.loc[0, column]) + 1
    else:
        frame.loc[0, column] = f"{frame.loc[0, column]} changed"
    changed = replace(result, **{frame_name: frame})
    with pytest.raises(PlanningRegulationStructureError):
        _validate(index, changed)
    # Updating only the exposed envelope hash cannot legitimize inner-row corruption.
    changed = replace(changed, **{hash_name: "f" * 64})
    with pytest.raises(PlanningRegulationStructureError):
        _validate(index, changed)


def test_unknown_topic_page_reference_is_rejected(valid_result) -> None:
    index, result = valid_result
    evidence = result.topic_evidence.copy(deep=True)
    evidence.loc[0, "page_number"] = 999
    with pytest.raises(PlanningRegulationStructureError, match="unknown page"):
        _validate(index, replace(result, topic_evidence=evidence))


def test_coordinated_section_row_mutation_is_caught_by_outer_envelope(
    valid_result,
) -> None:
    index, result = valid_result
    sections = result.sections.copy(deep=True)
    sections.loc[0, "raw_text"] = f"{sections.loc[0, 'raw_text']} changed"
    sections.loc[0, "normalized_text"] = _normalize_search_text(
        sections.loc[0, "raw_text"]
    )
    sections.loc[0, "character_count"] = len(sections.loc[0, "raw_text"])
    row = sections.loc[0].to_dict()
    sections.loc[0, "section_content_sha256"] = _section_content_sha256(row)
    with pytest.raises(PlanningRegulationStructureError):
        _validate(index, replace(result, sections=sections))


def test_dominant_unmapped_zone_stops_processing() -> None:
    index = _index()
    relations = _intersections(index).copy(deep=True)
    relations.loc[0, ["planning_zone_id", "source_zone_id", "zone_label_raw"]] = [
        "ZONE-X",
        "SRC-X",
        "X",
    ]
    with pytest.raises(PlanningRegulationStructureError, match="Dominant candidate"):
        structure_planning_regulation(index, _zones(index), relations, _config(index))


def test_positional_header_footer_filter_preserves_matching_body_lines() -> None:
    index = _index(
        (
            (
                "\nTest PLU\n\nARTICLE 1 - GENERAL PROVISIONS\n"
                "Test PLU\n100\nBody text\n\n42\n"
            ),
        )
    )
    config = _config(index)
    records = _line_records(index, config)
    retained = [record.raw for record in records]
    assert "Test PLU" in retained
    assert "100" in retained
    assert "42" not in retained
    assert retained[0] == "ARTICLE 1 - GENERAL PROVISIONS"
    assert records[0].page_line_number == 4


def test_page_without_configured_header_or_footer_is_unchanged() -> None:
    index = _index(("ARTICLE 1 - GENERAL\n100\nBody",))
    config = _config(index)
    config = config.model_copy(
        update={
            "ignored_patterns": config.ignored_patterns.model_copy(
                update={"page_headers": (), "page_footers": ()}
            )
        }
    )
    assert [record.raw for record in _line_records(index, config)] == [
        "ARTICLE 1 - GENERAL",
        "100",
        "Body",
    ]


@pytest.mark.parametrize(
    ("group", "pattern"),
    [
        ("zone_chapter", r"^ZONE\s+[A-Z]+$"),
        ("article", r"^ARTICLE\s+(?P<zone>[A-Z]+)\s+\d+\s+-\s+.*$"),
        ("general_section", r"^ARTICLE\s+(?P<number>\d+)\s+-\s+.*$"),
    ],
)
def test_heading_patterns_require_mandatory_named_captures(
    group: str,
    pattern: str,
) -> None:
    index = _index()
    config = _config(index)
    patterns = config.heading_patterns.model_copy(update={group: (pattern,)})
    with pytest.raises(ValueError, match="named captures"):
        PlanningRegulationStructureConfig.model_validate(
            config.model_dump(mode="python")
            | {"heading_patterns": patterns.model_dump(mode="python")}
        )


def test_optional_pattern_lists_may_be_empty() -> None:
    index = _index()
    config = _config(index)
    payload = config.model_dump(mode="python")
    payload["heading_patterns"]["continuation"] = ()
    payload["ignored_patterns"] = {"page_headers": (), "page_footers": ()}
    validated = PlanningRegulationStructureConfig.model_validate(payload)
    assert validated.heading_patterns.continuation == ()
    assert validated.ignored_patterns.page_headers == ()


@pytest.mark.parametrize(
    ("mutation", "value"),
    [
        ("section_id", "SECTION-9999"),
        ("start_record_id", "RECORD-999999"),
        ("source_record_count", 999),
        ("source_records_sha256", "f" * 64),
    ],
)
def test_lossless_partition_mutation_is_rejected(
    valid_result,
    mutation: str,
    value: object,
) -> None:
    index, result = valid_result
    sections = result.sections.copy(deep=True)
    sections.loc[0, mutation] = value
    with pytest.raises(PlanningRegulationStructureError):
        _validate(index, replace(result, sections=sections))


def test_duplicate_or_reordered_record_partition_is_rejected(valid_result) -> None:
    index, result = valid_result
    sections = result.sections.copy(deep=True)
    sections.loc[1, "start_record_id"] = sections.loc[0, "start_record_id"]
    with pytest.raises(PlanningRegulationStructureError, match="partition"):
        _validate(index, replace(result, sections=sections))


def test_unsorted_section_pages_are_rejected(valid_result) -> None:
    index, result = valid_result
    sections = result.sections.copy(deep=True)
    row_index = sections.index[sections["page_numbers"].map(len).gt(1)][0]
    sections.at[row_index, "page_numbers"] = tuple(
        reversed(sections.at[row_index, "page_numbers"])
    )
    with pytest.raises(PlanningRegulationStructureError, match="page references"):
        _validate(index, replace(result, sections=sections))


@pytest.mark.parametrize("mutation", ["missing_parent", "parent_after", "zone_mismatch"])
def test_article_parent_semantics_are_enforced(valid_result, mutation: str) -> None:
    index, result = valid_result
    sections = result.sections.copy(deep=True)
    article_index = sections.index[sections["section_type"].eq("ARTICLE")][0]
    if mutation == "missing_parent":
        sections.loc[article_index, "parent_section_id"] = None
    elif mutation == "parent_after":
        sections.loc[article_index, "parent_section_id"] = sections.iloc[-1]["section_id"]
    else:
        sections.loc[article_index, "zone_chapter_label"] = "N"
    with pytest.raises(PlanningRegulationStructureError):
        _validate(index, replace(result, sections=sections))


def test_wrong_intersection_source_zone_id_is_rejected(valid_result) -> None:
    index, result = valid_result
    intersections = _intersections(index)
    intersections.loc[0, "source_zone_id"] = "WRONG"
    with pytest.raises(PlanningRegulationStructureError, match="source-zone"):
        validate_planning_regulation_structure(
            index, _zones(index), intersections, _config(index), result
        )


@pytest.mark.parametrize("upper_column", ["parcel_metric_area_m2", "zone_area_m2"])
def test_intersection_area_cannot_exceed_available_geometry_area(
    upper_column: str,
) -> None:
    index = _index()
    intersections = _intersections(index)
    intersections[upper_column] = [99.0, 50.0]
    with pytest.raises(PlanningRegulationStructureError, match="exceeds"):
        structure_planning_regulation(
            index, _zones(index), intersections, _config(index)
        )


@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("mapping_method", "NONE"),
        ("matched_section_id", "SECTION-0002"),
        ("resolved_zone_chapter_label", "N"),
        ("zone_polygon_count", 99),
        ("candidate_intersection_count", 0),
        ("dominant_candidate_count", 99),
    ],
)
def test_zone_mapping_contract_mutations_are_rejected(
    valid_result,
    column: str,
    value: object,
) -> None:
    index, result = valid_result
    mapping = result.zone_mapping.copy(deep=True)
    row_index = mapping.index[mapping["source_zone_label_raw"].eq("U")][0]
    mapping.loc[row_index, column] = value
    with pytest.raises(PlanningRegulationStructureError):
        _validate(index, replace(result, zone_mapping=mapping))


def test_alias_chain_resolves_to_final_configured_target() -> None:
    index = _index()
    config = _config(index).model_copy(update={"zone_aliases": {"Ua": "Urban", "Urban": "U"}})
    result = structure_planning_regulation(
        index, _zones(index), _intersections(index), config
    )
    mapping = result.zone_mapping.set_index("source_zone_label_raw")
    assert mapping.at["Ua", "resolved_zone_chapter_label"] == "U"
    assert mapping.at["Ua", "mapping_status"] == "CONFIG_ALIAS"
    assert mapping.at["X", "mapping_status"] == "UNMAPPED"


def test_token_boundary_and_longest_match_policy() -> None:
    raw = (
        "risque risques dérisque nuisance nuisances réseau réseaux "
        "équipement d'intérêt collectif intérêt collectif "
        "incendie défense contre l'incendie"
    )
    normalized = normalize_planning_search_text(raw)
    terms = (
        "risque",
        "risques",
        "nuisance",
        "nuisances",
        "réseau",
        "réseaux",
        "équipement d'intérêt collectif",
        "intérêt collectif",
        "incendie",
        "défense contre l'incendie",
    )
    matches = _literal_topic_matches(normalized, terms)
    retained = [match.search_term for match in matches]
    assert retained.count("risque") == 1
    assert retained.count("risques") == 1
    assert retained.count("nuisance") == 1
    assert retained.count("nuisances") == 1
    assert retained.count("réseau") == 1
    assert retained.count("réseaux") == 1
    assert retained.count("équipement d'intérêt collectif") == 1
    assert retained.count("intérêt collectif") == 1
    assert retained.count("incendie") == 1
    assert retained.count("défense contre l'incendie") == 1
    assert len(matches) == 10


@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("evidence_scope", "GENERAL_RULE"),
        ("zone_chapter_label", "N"),
        ("article_number_raw", "999"),
        ("topic", "unconfigured"),
        ("search_term", "unconfigured"),
        ("occurrence_count", 99),
        ("raw_context", "fabricated"),
        ("first_match_normalized_start", 999),
    ],
)
def test_topic_evidence_semantic_mutations_are_rejected(
    valid_result,
    column: str,
    value: object,
) -> None:
    index, result = valid_result
    evidence = result.topic_evidence.copy(deep=True)
    zone_rows = evidence.index[evidence["evidence_scope"].eq("ZONE_SPECIFIC_RULE")]
    row_index = zone_rows[0] if len(zone_rows) else evidence.index[0]
    evidence.loc[row_index, column] = value
    with pytest.raises(PlanningRegulationStructureError):
        _validate(index, replace(result, topic_evidence=evidence))


def test_coordinated_topic_evidence_and_hash_mutation_is_rebuilt_and_rejected(
    valid_result,
) -> None:
    index, result = valid_result
    evidence = result.topic_evidence.copy(deep=True)
    evidence.loc[0, "raw_context"] = "fabricated"
    changed = _result_with_hashes(
        replace(
            result,
            topic_evidence=evidence,
            sections_content_sha256="",
            zone_map_content_sha256="",
            topic_evidence_content_sha256="",
            structure_result_content_sha256="",
        )
    )
    with pytest.raises(PlanningRegulationStructureError):
        _validate(index, changed)


@pytest.mark.parametrize("source_change", ["alias", "topic", "heading", "zone", "area", "relation"])
def test_source_complete_validator_rejects_post_build_source_change(
    valid_result,
    source_change: str,
) -> None:
    index, result = valid_result
    zones = _zones(index)
    intersections = _intersections(index)
    config = _config(index)
    if source_change == "alias":
        config = config.model_copy(update={"zone_aliases": {"Ua": "N"}})
    elif source_change == "topic":
        config = config.model_copy(update={"topics": {"energy": ("electricity",), "risk": ("risk",)}})
    elif source_change == "heading":
        patterns = config.heading_patterns.model_copy(
            update={"zone_chapter": (r"^ZONE\s+(?P<label>[A-Za-z0-9]+)\s*$",)}
        )
        config = config.model_copy(update={"heading_patterns": patterns})
    elif source_change == "zone":
        zones.loc[0, "source_zone_id"] = "CHANGED"
        intersections.loc[0, "source_zone_id"] = "CHANGED"
    elif source_change == "area":
        intersections.loc[0, "intersection_area_m2"] = 99.0
    else:
        intersections.loc[0, "relation_type"] = "TOUCH_ONLY"
        intersections.loc[0, "intersection_area_m2"] = 0.0
    with pytest.raises(PlanningRegulationStructureError):
        validate_planning_regulation_structure(
            index, zones, intersections, config, result
        )


@pytest.mark.parametrize(
    "hash_field",
    [
        "structure_config_sha256",
        "zones_content_sha256",
        "zoning_intersections_content_sha256",
        "structure_result_content_sha256",
    ],
)
def test_source_and_result_hash_mutation_is_rejected(valid_result, hash_field: str) -> None:
    index, result = valid_result
    with pytest.raises(PlanningRegulationStructureError):
        _validate(index, replace(result, **{hash_field: "f" * 64}))
