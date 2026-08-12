from __future__ import annotations

from copy import deepcopy
from dataclasses import FrozenInstanceError, replace
from hashlib import sha256
from importlib import import_module
from pathlib import Path

import geopandas as gpd  # type: ignore[import-untyped]
import pytest
from geopandas.testing import assert_geodataframe_equal
from pandas.testing import assert_frame_equal
from shapely.geometry import Polygon

from landscout import stages
from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSpatialLayerReference,
)
from landscout.stages.index_planning_regulation import (
    MURET_REGULATION_PDF_BASENAME,
    PlanningRegulationIndexError,
    _validate_index,
    index_planning_regulation,
    search_planning_regulation,
)

regulation_module = import_module("landscout.stages.index_planning_regulation")

DOCUMENT_ID = "doc-1"
ARCHIVE_SHA = "a" * 64
PDF_BYTES = b"synthetic-pdf-bytes"


class _FakePage:
    def __init__(self, result: object) -> None:
        self.result = result

    def extract_text(self) -> object:
        if isinstance(self.result, Exception):
            raise self.result
        return self.result


class _FakeReader:
    def __init__(self, pages: list[object], *, encrypted: bool = False) -> None:
        self.pages = [_FakePage(page) for page in pages]
        self.is_encrypted = encrypted


def _patch_reader(
    monkeypatch: pytest.MonkeyPatch,
    pages: list[object],
    *,
    encrypted: bool = False,
) -> None:
    monkeypatch.setattr(
        regulation_module,
        "PdfReader",
        lambda *args, **kwargs: _FakeReader(pages, encrypted=encrypted),
    )


def _zone_layer() -> GpuInspectedLayer:
    frame = gpd.GeoDataFrame(
        {"zone": ["Z"]},
        geometry=[Polygon([(0, 0), (0, 1), (1, 1), (1, 0), (0, 0)])],
        crs="EPSG:2154",
    )
    summary = GpuLayerSummary(
        source_document_id=DOCUMENT_ID,
        source_archive_sha256=ARCHIVE_SHA,
        source_layer="ZONE",
        crs="EPSG:2154",
        feature_count=1,
        columns=("zone", "geometry"),
        dtypes=(("zone", "object"), ("geometry", "geometry")),
        null_counts=(("zone", 0), ("geometry", 0)),
        geometry_types=(("Polygon", 1),),
        null_geometry_count=0,
        empty_geometry_count=0,
        invalid_geometry_count=0,
    )
    reference = GpuSpatialLayerReference(Path("zone.gpkg"), "ZONE", "GPKG")
    return GpuInspectedLayer("zoning", reference, frame, summary)


def _document(
    root: Path,
    inventory: tuple[GpuExtractedFile, ...],
    *,
    archive_sha: str = ARCHIVE_SHA,
    status: str = "document.production",
) -> GpuPlanningDocument:
    metadata = GpuDocumentMetadata(
        provider="Géoportail de l'Urbanisme",
        portal="GPU",
        commune_code="31395",
        partition="DU_31395",
        document_id=DOCUMENT_ID,
        document_family="DU",
        document_type="PLU",
        document_title="Muret PLU",
        status=status,
        legal_status="APPROVED",
        effective_status="EN_VIGUEUR",
        version="10",
        archive_name="31395_PLU_20240215",
        publication_timestamp=None,
        update_timestamp=None,
        revision_date=None,
        producer=None,
        standard_model="CNIG PLU v2017",
        projection="EPSG:2154",
        metadata_identifier=None,
        source_url="https://www.geoportail-urbanisme.gouv.fr/api/document/download-by-partition/DU_31395",
        written_files=(),
    )
    archive = GpuArchiveDownload(
        document=metadata,
        download_timestamp="2026-08-12T12:00:00+00:00",
        filename="31395_PLU_20240215.zip",
        archive_format="zip",
        file_size=100,
        sha256=archive_sha,
        path=root.parent / "source.zip",
        cache_hit=True,
    )
    extraction = GpuExtraction(
        archive=archive,
        extraction_root=root,
        files=inventory,
        standard_models=("CNIG PLU v2017",),
        cache_hit=True,
    )
    zoning = _zone_layer()
    if archive_sha != ARCHIVE_SHA:
        zoning = replace(
            zoning,
            summary=replace(zoning.summary, source_archive_sha256=archive_sha),
        )
    return GpuPlanningDocument(
        extraction=extraction,
        all_spatial_layers=(zoning.reference,),
        zoning=zoning,
        related_layers=(),
    )


def _inventory_item(relative_path: str, data: bytes = PDF_BYTES) -> GpuExtractedFile:
    return GpuExtractedFile(
        relative_path=relative_path,
        file_type="pdf",
        size_bytes=len(data),
        sha256=sha256(data).hexdigest(),
        category="WRITTEN_REGULATION",
    )


def _fixture_document(
    tmp_path: Path,
    *,
    relative_path: str = f"written/{MURET_REGULATION_PDF_BASENAME}",
    data: bytes = PDF_BYTES,
) -> GpuPlanningDocument:
    root = tmp_path / "extraction"
    path = root.joinpath(*relative_path.split("/"))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return _document(root, (_inventory_item(relative_path, data),))


def test_only_clean_high_level_api_is_exported() -> None:
    assert stages.index_planning_regulation is index_planning_regulation
    assert stages.search_planning_regulation is search_planning_regulation
    assert "index_planning_regulation" in stages.__all__
    assert "search_planning_regulation" in stages.__all__
    assert stages.PlanningRegulationIndex is regulation_module.PlanningRegulationIndex
    assert (
        stages.PlanningRegulationIndexError
        is regulation_module.PlanningRegulationIndexError
    )
    assert "PlanningRegulationIndex" in stages.__all__
    assert "PlanningRegulationIndexError" in stages.__all__


def test_exact_pdf_discovery_and_page_states(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    document = _fixture_document(tmp_path)
    _patch_reader(
        monkeypatch,
        ["ÉNERGIE\n Batterie  ", "  \n", RuntimeError("page failed")],
    )
    result = index_planning_regulation(document)
    assert result.document_id == DOCUMENT_ID
    assert result.archive_sha256 == ARCHIVE_SHA
    assert result.pdf_relative_path == f"written/{MURET_REGULATION_PDF_BASENAME}"
    assert result.pdf_size_bytes == len(PDF_BYTES)
    assert result.pdf_sha256 == sha256(PDF_BYTES).hexdigest()
    assert result.extraction_library == "pypdf"
    assert result.extraction_library_version
    assert result.total_page_count == 3
    assert result.pages["page_number"].tolist() == [1, 2, 3]
    assert result.pages["extraction_status"].tolist() == ["TEXT", "EMPTY", "ERROR"]
    assert result.pages.loc[0, "raw_text"] == "ÉNERGIE\n Batterie  "
    assert result.pages.loc[0, "normalized_search_text"] == "energie batterie"
    assert result.pages.loc[1, "raw_text"] == "  \n"
    assert result.pages.loc[1, "character_count"] == 3
    assert result.pages.loc[2, "raw_text"] == ""
    assert result.pages.loc[2, "extraction_error"] == "RuntimeError: page failed"
    with pytest.raises(FrozenInstanceError):
        result.total_page_count = 9  # type: ignore[misc]


def test_none_text_is_an_empty_page(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    document = _fixture_document(tmp_path)
    _patch_reader(monkeypatch, [None])
    row = index_planning_regulation(document).pages.iloc[0]
    assert row["extraction_status"] == "EMPTY"
    assert row["raw_text"] == ""
    assert row["character_count"] == 0


def test_missing_pdf_is_rejected(tmp_path: Path) -> None:
    root = tmp_path / "extraction"
    root.mkdir()
    document = _document(root, ())
    with pytest.raises(PlanningRegulationIndexError, match="missing"):
        index_planning_regulation(document)


def test_public_index_api_has_no_alternate_pdf_override() -> None:
    with pytest.raises(TypeError):
        index_planning_regulation(  # type: ignore[call-arg]
            object(),  # type: ignore[arg-type]
            "another.pdf",
        )


def test_ambiguous_pdf_is_rejected(tmp_path: Path) -> None:
    root = tmp_path / "extraction"
    inventory: list[GpuExtractedFile] = []
    for directory in ("a", "b"):
        relative = f"{directory}/{MURET_REGULATION_PDF_BASENAME}"
        path = root.joinpath(*relative.split("/"))
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(PDF_BYTES)
        inventory.append(_inventory_item(relative))
    with pytest.raises(PlanningRegulationIndexError, match="ambiguous"):
        index_planning_regulation(_document(root, tuple(inventory)))


def test_inventory_path_outside_root_is_rejected(tmp_path: Path) -> None:
    root = tmp_path / "extraction"
    root.mkdir()
    outside = tmp_path / MURET_REGULATION_PDF_BASENAME
    outside.write_bytes(PDF_BYTES)
    item = _inventory_item(f"../{MURET_REGULATION_PDF_BASENAME}")
    with pytest.raises(PlanningRegulationIndexError, match="unsafe"):
        index_planning_regulation(_document(root, (item,)))


def test_pdf_size_mismatch_is_rejected(tmp_path: Path) -> None:
    document = _fixture_document(tmp_path)
    item = replace(document.extraction.files[0], size_bytes=len(PDF_BYTES) + 1)
    corrupted = replace(
        document,
        extraction=replace(document.extraction, files=(item,)),
    )
    with pytest.raises(PlanningRegulationIndexError, match="size differs"):
        index_planning_regulation(corrupted)


def test_pdf_hash_mismatch_is_rejected(tmp_path: Path) -> None:
    document = _fixture_document(tmp_path)
    item = replace(document.extraction.files[0], sha256="b" * 64)
    corrupted = replace(
        document,
        extraction=replace(document.extraction, files=(item,)),
    )
    with pytest.raises(PlanningRegulationIndexError, match="SHA256 differs"):
        index_planning_regulation(corrupted)


def test_pdf_link_or_junction_is_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    document = _fixture_document(tmp_path)
    target_name = MURET_REGULATION_PDF_BASENAME
    original = regulation_module._is_link_or_junction

    def fake_link(path: Path) -> bool:
        return path.name == target_name or original(path)

    monkeypatch.setattr(regulation_module, "_is_link_or_junction", fake_link)
    with pytest.raises(PlanningRegulationIndexError, match="symbolic link or junction"):
        index_planning_regulation(document)


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("status", "draft"),
        ("legal_status", "CANCELLED"),
        ("effective_status", "NOT_EFFECTIVE"),
        ("document_family", "SUP"),
    ],
)
def test_non_current_document_lineage_is_rejected(
    tmp_path: Path,
    field: str,
    value: str,
) -> None:
    document = _fixture_document(tmp_path)
    metadata = replace(document.extraction.archive.document, **{field: value})
    archive = replace(document.extraction.archive, document=metadata)
    corrupted = replace(
        document,
        extraction=replace(document.extraction, archive=archive),
    )
    with pytest.raises(PlanningRegulationIndexError, match="current effective DU"):
        index_planning_regulation(corrupted)


def test_zero_page_pdf_is_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    document = _fixture_document(tmp_path)
    _patch_reader(monkeypatch, [])
    with pytest.raises(PlanningRegulationIndexError, match="at least one page"):
        index_planning_regulation(document)


def test_reader_failure_is_controlled_and_chained(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    document = _fixture_document(tmp_path)

    def fail_reader(*args: object, **kwargs: object) -> object:
        raise RuntimeError("broken xref")

    monkeypatch.setattr(regulation_module, "PdfReader", fail_reader)
    with pytest.raises(PlanningRegulationIndexError, match="opened or parsed") as caught:
        index_planning_regulation(document)
    assert isinstance(caught.value.__cause__, RuntimeError)


def test_search_is_accent_case_and_whitespace_insensitive(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    document = _fixture_document(tmp_path)
    _patch_reader(
        monkeypatch,
        [
            "Énergie BATTERIE batterie et poste\n électrique.",
            "Aucun résultat.",
        ],
    )
    result = index_planning_regulation(document)
    snapshot = result.pages.copy(deep=True)
    hits = search_planning_regulation(
        result, ["energie", "Batterie", "poste électrique"], context_characters=20
    )
    assert hits[["search_term", "page_number", "occurrence_count"]].to_dict(
        "records"
    ) == [
        {"search_term": "energie", "page_number": 1, "occurrence_count": 1},
        {"search_term": "Batterie", "page_number": 1, "occurrence_count": 2},
        {
            "search_term": "poste électrique",
            "page_number": 1,
            "occurrence_count": 1,
        },
    ]
    assert all(isinstance(value, str) and value for value in hits["context"])
    assert_frame_equal(result.pages, snapshot)


def test_index_and_search_are_deterministic(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    document = _fixture_document(tmp_path)
    _patch_reader(monkeypatch, ["Risque risque", "Nuisance"])
    first = index_planning_regulation(document)
    second = index_planning_regulation(document)
    assert first.document_id == second.document_id
    assert first.archive_sha256 == second.archive_sha256
    assert first.pdf_relative_path == second.pdf_relative_path
    assert first.pdf_size_bytes == second.pdf_size_bytes
    assert first.pdf_sha256 == second.pdf_sha256
    assert first.extraction_library == second.extraction_library
    assert first.extraction_library_version == second.extraction_library_version
    assert first.total_page_count == second.total_page_count
    assert_frame_equal(first.pages, second.pages)
    assert_frame_equal(
        search_planning_regulation(first, ["risque", "nuisance"]),
        search_planning_regulation(second, ["risque", "nuisance"]),
    )


def test_indexing_does_not_mutate_planning_document(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    document = _fixture_document(tmp_path)
    extraction_before = deepcopy(document.extraction)
    zoning_before = document.zoning.data.copy(deep=True)
    _patch_reader(monkeypatch, ["Texte"])
    index_planning_regulation(document)
    assert document.extraction == extraction_before
    assert_geodataframe_equal(document.zoning.data, zoning_before)


@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("page_number", 2),
        ("extraction_status", "BAD"),
        ("normalized_search_text", "wrong"),
        ("character_count", 999),
        ("extraction_error", "unexpected"),
    ],
)
def test_search_rejects_mutated_index(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    column: str,
    value: object,
) -> None:
    document = _fixture_document(tmp_path)
    _patch_reader(monkeypatch, ["Énergie"])
    index = index_planning_regulation(document)
    pages = index.pages.copy(deep=True)
    pages.loc[0, column] = value
    with pytest.raises(PlanningRegulationIndexError):
        search_planning_regulation(replace(index, pages=pages), ["energie"])


@pytest.mark.parametrize("term", ["", "   ", " term", "term ", 7])
def test_invalid_search_term_is_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    term: object,
) -> None:
    document = _fixture_document(tmp_path)
    _patch_reader(monkeypatch, ["Text"])
    index = index_planning_regulation(document)
    with pytest.raises(PlanningRegulationIndexError, match="search term"):
        search_planning_regulation(index, [term])  # type: ignore[list-item]


def test_duplicate_normalized_search_terms_are_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    document = _fixture_document(tmp_path)
    _patch_reader(monkeypatch, ["Énergie"])
    index = index_planning_regulation(document)
    with pytest.raises(PlanningRegulationIndexError, match="unique"):
        search_planning_regulation(index, ["énergie", "ENERGIE"])


def test_validate_index_rejects_total_page_mismatch(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    document = _fixture_document(tmp_path)
    _patch_reader(monkeypatch, ["Text"])
    index = index_planning_regulation(document)
    with pytest.raises(PlanningRegulationIndexError, match="page count"):
        _validate_index(replace(index, total_page_count=2))
