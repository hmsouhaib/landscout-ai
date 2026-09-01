from __future__ import annotations

from dataclasses import dataclass, replace
from hashlib import sha256
from pathlib import Path
from urllib.parse import quote
from zipfile import ZIP_DEFLATED, ZipFile

import geopandas as gpd  # type: ignore[import-untyped]
import pytest
from pypdf import PdfWriter
from pypdf.generic import (
    DecodedStreamObject,
    DictionaryObject,
    NameObject,
)
from shapely.geometry import Polygon

from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuWrittenFile,
    build_gpu_partition,
    build_gpu_partition_download_url,
    extract_gpu_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
)
from landscout.stages.enrich_planning_zoning import (
    ParcelZoningResult,
    intersect_parcels_with_gpu_zoning,
)
from landscout.stages.index_planning_regulation import (
    PlanningRegulationIndex,
    index_planning_regulation,
)
from landscout.stages.interpret_bess_zoning import (
    BessZoningPolicyConfig,
    BessZoningPrecheckError,
    BessZoningPrecheckResult,
    interpret_bess_zoning,
    validate_bess_zoning_precheck,
)
from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureResult,
    structure_planning_regulation,
)

_ARCHIVE_NAME = "synthetic_gpu_document"
_DOCUMENT_ID = "synthetic-document"
_REGULATION_FILENAME = "reglement.pdf"


@dataclass(frozen=True)
class _PhysicalPlanningChain:
    planning_document: GpuPlanningDocument
    zoning: ParcelZoningResult
    index: PlanningRegulationIndex
    structure_config: PlanningRegulationStructureConfig
    structure: PlanningRegulationStructureResult
    parcels: gpd.GeoDataFrame
    policy: BessZoningPolicyConfig


def _sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def _write_text_pdf(path: Path, *, include_article_two: bool) -> None:
    lines = [
        "ZONE U",
        "ARTICLE U 1 - USES",
        "First factual source sentence.",
    ]
    if include_article_two:
        lines.extend(
            (
                "ARTICLE U 2 - OTHER",
                "Second factual source sentence.",
            )
        )
    writer = PdfWriter()
    page = writer.add_blank_page(width=612, height=792)
    font = DictionaryObject(
        {
            NameObject("/Type"): NameObject("/Font"),
            NameObject("/Subtype"): NameObject("/Type1"),
            NameObject("/BaseFont"): NameObject("/Helvetica"),
        }
    )
    page[NameObject("/Resources")] = DictionaryObject(
        {
            NameObject("/Font"): DictionaryObject(
                {NameObject("/F1"): writer._add_object(font)}
            )
        }
    )
    operations = [b"BT", b"/F1 12 Tf", b"72 720 Td"]
    for position, line in enumerate(lines):
        if position:
            operations.append(b"0 -18 Td")
        operations.append(f"({line}) Tj".encode("ascii"))
    operations.append(b"ET")
    stream = DecodedStreamObject()
    stream.set_data(b"\n".join(operations))
    page[NameObject("/Contents")] = writer._add_object(stream)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("wb") as output:
        writer.write(output)


def _write_gpu_archive(
    tmp_path: Path,
    *,
    include_article_two: bool,
) -> Path:
    package = tmp_path / "package-source"
    package.mkdir()
    zoning_path = package / "planning.gpkg"
    zones = gpd.GeoDataFrame(
        {
            "LIB_IDZONE": ["ZONE-U"],
            "LIBELLE": ["U"],
            "LIBELONG": ["Zone U"],
            "TYPEZONE": ["U"],
            "NOMFIC": [_REGULATION_FILENAME],
            "URLFIC": ["https://example.invalid/reglement.pdf"],
            "IDURBA": [_ARCHIVE_NAME],
            "DATVALID": ["2026-01-01"],
        },
        geometry=[Polygon([(0, 0), (100, 0), (100, 100), (0, 100), (0, 0)])],
        crs="EPSG:2154",
    )
    zones.to_file(
        zoning_path,
        layer="zone_urba",
        driver="GPKG",
        engine="pyogrio",
    )
    pdf_path = package / _REGULATION_FILENAME
    _write_text_pdf(pdf_path, include_article_two=include_article_two)
    archive_path = tmp_path / f"{_ARCHIVE_NAME}.zip"
    with ZipFile(archive_path, "w", compression=ZIP_DEFLATED) as archive:
        archive.write(zoning_path, "package/planning.gpkg")
        archive.write(pdf_path, f"package/{_REGULATION_FILENAME}")
    return archive_path


def _gpu_document(config: GpuSourceConfig) -> GpuDocumentMetadata:
    written_url = (
        f"{str(config.api.base_url).rstrip('/')}/document/"
        f"{quote(_DOCUMENT_ID, safe='')}/files/"
        f"{quote(_REGULATION_FILENAME, safe='')}"
    )
    return GpuDocumentMetadata(
        provider=config.provider,
        portal=config.portal,
        commune_code=config.pilot.commune_code,
        partition=build_gpu_partition(config),
        document_id=_DOCUMENT_ID,
        document_family="DU",
        document_type="PLU",
        document_title="Synthetic planning document",
        status="document.production",
        legal_status="APPROVED",
        effective_status="EN_VIGUEUR",
        version="1",
        archive_name=_ARCHIVE_NAME,
        publication_timestamp=None,
        update_timestamp=None,
        revision_date=None,
        producer=None,
        standard_model=None,
        projection="EPSG:2154",
        metadata_identifier=None,
        source_url=build_gpu_partition_download_url(config),
        written_files=(
            GpuWrittenFile(
                filename=_REGULATION_FILENAME,
                title="Synthetic regulation",
                document_path=None,
                source_url=written_url,
            ),
        ),
    )


def _structure_config(
    index: PlanningRegulationIndex,
) -> PlanningRegulationStructureConfig:
    return PlanningRegulationStructureConfig.model_validate(
        {
            "schema_version": 2,
            "structure_profile": "synthetic_physical_v1",
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
                "general_section": [r"^ARTICLE\s+(?P<number>\d+)\s*-\s*(?P<title>.*)$"],
                "continuation": [],
            },
            "ignored_patterns": {"page_headers": [], "page_footers": []},
            "zone_aliases": {},
            "topics": {"factual": ["factual"]},
            "topic_match_policy": {
                "boundary_mode": "token",
                "overlap_resolution": "longest_match",
            },
            "topic_context_characters": 10,
        }
    )


def _policy(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
) -> BessZoningPolicyConfig:
    reviewed = tuple(
        structure.sections.loc[
            structure.sections["section_type"].eq("ARTICLE"), "section_id"
        ].tolist()
    )
    return BessZoningPolicyConfig.model_validate(
        {
            "schema_version": 5,
            "policy_profile": "synthetic_physical_policy_v5",
            "planning_precheck_scope": "WRITTEN_ZONING_REGULATION_ONLY",
            "review_scope": "CONFIGURED_USE_CONTROL_ARTICLES_ONLY",
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
                    "review_completeness": (
                        "COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES"
                    ),
                    "reviewed_section_ids": reviewed,
                    "review_note": "The configured source articles were reviewed.",
                    "zoning_precheck_status": "UNKNOWN",
                    "zoning_precheck_confidence": "LOW",
                    "rationale": "No decision evidence is configured in this fixture.",
                    "missing_information": "Formal planning review remains required.",
                    "evidence": [],
                    "route_assessments": [],
                }
            ],
        }
    )


def _build_physical_chain(
    tmp_path: Path,
    *,
    include_article_two: bool = True,
) -> _PhysicalPlanningChain:
    config = load_gpu_source_config(Path("configs/sources/gpu_fr.yaml"))
    archive_path = _write_gpu_archive(
        tmp_path,
        include_article_two=include_article_two,
    )
    document = _gpu_document(config)
    download = GpuArchiveDownload(
        document=document,
        download_timestamp="2026-09-01T00:00:00+00:00",
        filename=archive_path.name,
        archive_format="zip",
        file_size=archive_path.stat().st_size,
        sha256=_sha256(archive_path),
        path=archive_path,
        cache_hit=False,
    )
    extraction = extract_gpu_document(download, tmp_path / "cache")
    planning_document = inspect_gpu_planning_document(extraction, config)
    source_parcels = gpd.GeoDataFrame(
        {"parcel_id": ["PARCEL-1"], "prior_fact": ["unchanged"]},
        geometry=[Polygon([(10, 10), (60, 10), (60, 60), (10, 60), (10, 10)])],
        crs="EPSG:2154",
    )
    zoning = intersect_parcels_with_gpu_zoning(source_parcels, planning_document)
    index = index_planning_regulation(planning_document)
    structure_config = _structure_config(index)
    structure = structure_planning_regulation(
        index,
        zoning.zones,
        zoning.intersections,
        structure_config,
    )
    parcels = zoning.parcels.copy(deep=True)
    for column in (
        "planning_surface_relation_count",
        "prescription_surface_relation_count",
        "information_surface_relation_count",
        "planning_line_relation_count",
        "planning_point_relation_count",
    ):
        parcels[column] = 0
    parcels["planning_feature_document_id"] = index.document_id
    parcels["planning_feature_archive_sha256"] = index.archive_sha256
    return _PhysicalPlanningChain(
        planning_document=planning_document,
        zoning=zoning,
        index=index,
        structure_config=structure_config,
        structure=structure,
        parcels=parcels,
        policy=_policy(index, structure),
    )


def _interpret(chain: _PhysicalPlanningChain) -> BessZoningPrecheckResult:
    return interpret_bess_zoning(
        chain.index,
        chain.structure,
        chain.structure_config,
        chain.zoning.zones,
        chain.zoning.intersections,
        chain.parcels,
        chain.planning_document,
        chain.policy,
    )


def _validate(
    chain: _PhysicalPlanningChain,
    result: BessZoningPrecheckResult,
) -> None:
    validate_bess_zoning_precheck(
        chain.index,
        chain.structure,
        chain.structure_config,
        chain.zoning.zones,
        chain.zoning.intersections,
        chain.parcels,
        chain.planning_document,
        chain.policy,
        result,
    )


def test_physical_gpu_planning_chain_builds_and_revalidates(tmp_path: Path) -> None:
    chain = _build_physical_chain(tmp_path)
    result = _interpret(chain)

    _validate(chain, result)

    assert len(chain.zoning.zones) == 1
    assert len(chain.zoning.intersections) == 1
    assert len(result.parcels) == 1
    assert result.parcels["prior_fact"].tolist() == ["unchanged"]


def test_physical_gpu_source_byte_mutation_is_rejected(tmp_path: Path) -> None:
    chain = _build_physical_chain(tmp_path)
    result = _interpret(chain)
    dataset = chain.planning_document.zoning.reference.dataset_path
    with dataset.open("ab") as output:
        output.write(b"mutated-after-interpretation")

    with pytest.raises(BessZoningPrecheckError, match="source|GPU|zoning"):
        _validate(chain, result)


def test_physical_gpu_config_hash_mutation_is_rejected(tmp_path: Path) -> None:
    chain = _build_physical_chain(tmp_path)
    result = _interpret(chain)
    forged_document = replace(
        chain.planning_document,
        source_config_sha256="0" * 64,
    )
    forged_chain = replace(chain, planning_document=forged_document)

    with pytest.raises(BessZoningPrecheckError, match="source|GPU|zoning"):
        _validate(forged_chain, result)


def test_physical_gpu_missing_required_article_is_rejected(tmp_path: Path) -> None:
    chain = _build_physical_chain(tmp_path, include_article_two=False)

    with pytest.raises(
        BessZoningPrecheckError,
        match="exactly one configured article '2'",
    ):
        _interpret(chain)
