from __future__ import annotations

import json
from copy import deepcopy
from dataclasses import FrozenInstanceError, replace
from hashlib import sha256
from importlib import import_module
from pathlib import Path
from re import fullmatch
from urllib.parse import quote

import geopandas as gpd  # type: ignore[import-untyped]
import pandas as pd
import pytest
from geopandas.testing import assert_geodataframe_equal
from pandas.testing import assert_frame_equal
from shapely.geometry import Polygon

from landscout import stages
from landscout.common.planning_text import (
    normalize_planning_search_text as _normalize_search_text,
)
from landscout.sources import gpu_fr as gpu_source_module
from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialLayerReference,
    GpuWrittenFile,
    load_gpu_source_config,
)
from landscout.stages.index_planning_regulation import (
    PAGE_COLUMNS,
    SEARCH_HIT_COLUMNS,
    SEARCH_NORMALIZATION_PROFILE,
    PlanningRegulationIndexError,
    index_planning_regulation,
    search_planning_regulation,
    validate_planning_regulation_index,
    validate_planning_regulation_search_result,
)

regulation_module = import_module("landscout.stages.index_planning_regulation")

DOCUMENT_ID = "doc-1"
ARCHIVE_SHA = "a" * 64
DEFAULT_PDF = "31395_reglement_20240215.pdf"
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


def _summary(
    frame: gpd.GeoDataFrame,
    *,
    source_layer: str = "ZONE",
) -> GpuLayerSummary:
    geometry = frame.geometry
    non_null = geometry.notna()
    non_empty = non_null & ~geometry.is_empty
    return GpuLayerSummary(
        source_document_id=DOCUMENT_ID,
        source_archive_sha256=ARCHIVE_SHA,
        source_layer=source_layer,
        crs="EPSG:2154",
        feature_count=len(frame),
        columns=tuple(str(column) for column in frame.columns),
        dtypes=tuple(
            (str(column), str(dtype)) for column, dtype in frame.dtypes.items()
        ),
        null_counts=tuple(
            (str(column), int(frame[column].isna().sum())) for column in frame.columns
        ),
        geometry_types=tuple(
            (str(key), int(value))
            for key, value in geometry.geom_type.value_counts().sort_index().items()
        ),
        null_geometry_count=int((~non_null).sum()),
        empty_geometry_count=int((non_null & geometry.is_empty).sum()),
        invalid_geometry_count=int((non_empty & ~geometry.is_valid).sum()),
    )


def _zone_frame(
    nomfic: list[object] | None = None,
    *,
    include_nomfic: bool = True,
) -> gpd.GeoDataFrame:
    filenames = [DEFAULT_PDF] if nomfic is None else nomfic
    count = len(filenames)
    attributes: dict[str, list[object]] = {
        "LIB_IDZONE": [f"ZONE-{index + 1}" for index in range(count)]
    }
    if include_nomfic:
        attributes["NOMFIC"] = filenames
    return gpd.GeoDataFrame(
        attributes,
        geometry=[
            Polygon(
                [
                    (index, 0),
                    (index, 1),
                    (index + 1, 1),
                    (index + 1, 0),
                    (index, 0),
                ]
            )
            for index in range(count)
        ],
        crs="EPSG:2154",
    )


def _inventory_item(relative_path: str, data: bytes = PDF_BYTES) -> GpuExtractedFile:
    return GpuExtractedFile(
        relative_path=relative_path,
        file_type="pdf",
        size_bytes=len(data),
        sha256=sha256(data).hexdigest(),
        category="WRITTEN_REGULATION",
    )


def _spatial_inventory_item(root: Path, path: Path) -> GpuExtractedFile:
    data = path.read_bytes()
    return GpuExtractedFile(
        relative_path=path.relative_to(root).as_posix(),
        file_type=path.suffix.lower().lstrip(".") or "binary",
        size_bytes=len(data),
        sha256=sha256(data).hexdigest(),
        category="SPATIAL_DATA",
    )


def _write_zoning_source(
    root: Path,
    frame: gpd.GeoDataFrame,
    *,
    source_format: str,
) -> tuple[GpuInspectedLayer, tuple[GpuExtractedFile, ...]]:
    spatial_root = root / "spatial"
    spatial_root.mkdir(parents=True, exist_ok=True)
    if source_format == "GPKG":
        path = spatial_root / "zone.gpkg"
        source_layer = "ZONE"
        frame.to_file(path, layer=source_layer, driver="GPKG", engine="pyogrio")
        source_paths = (path,)
        loaded = gpd.read_file(path, layer=source_layer, engine="pyogrio")
        driver = "GPKG"
    elif source_format == "ESRI Shapefile":
        path = spatial_root / "ZONE.shp"
        source_layer = path.stem
        frame.to_file(path, driver="ESRI Shapefile", engine="pyogrio")
        source_paths = tuple(
            candidate
            for candidate in sorted(path.parent.glob(f"{path.stem}.*"))
            if candidate.is_file()
        )
        loaded = gpd.read_file(path, engine="pyogrio")
        driver = "ESRI Shapefile"
    else:  # pragma: no cover - fixture misuse
        raise AssertionError(f"Unsupported test source format: {source_format}")
    reference = GpuSpatialLayerReference(path, source_layer, driver)
    layer = GpuInspectedLayer(
        "zoning",
        reference,
        loaded,
        _summary(loaded, source_layer=source_layer),
    )
    inventory = tuple(_spatial_inventory_item(root, item) for item in source_paths)
    return layer, inventory


def _document(
    root: Path,
    inventory: tuple[GpuExtractedFile, ...],
    zoning: GpuInspectedLayer,
    *,
    zoning_filenames: list[object] | None = None,
    written_filenames: tuple[str, ...] = (DEFAULT_PDF,),
) -> GpuPlanningDocument:
    inventory = tuple(sorted(inventory, key=lambda item: item.relative_path))
    base_config = load_gpu_source_config(Path("configs/sources/gpu_fr.yaml"))
    written = tuple(
        GpuWrittenFile(
            filename=value,
            title=None,
            document_path=None,
            source_url=(
                f"{str(base_config.api.base_url).rstrip('/')}/document/"
                f"{quote(DOCUMENT_ID, safe='')}/files/{quote(value, safe='')}"
            ),
        )
        for value in written_filenames
    )
    metadata = GpuDocumentMetadata(
        provider="Géoportail de l'Urbanisme",
        portal="G\u00e9oportail de l'Urbanisme",
        commune_code="31395",
        partition="DU_31395",
        document_id=DOCUMENT_ID,
        document_family="DU",
        document_type="PLU",
        document_title="Planning document",
        status="document.production",
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
        written_files=written,
    )
    archive = GpuArchiveDownload(
        document=metadata,
        download_timestamp="2026-08-12T12:00:00+00:00",
        filename="31395_PLU_20240215.zip",
        archive_format="zip",
        file_size=100,
        sha256=ARCHIVE_SHA,
        path=root.parent / "source.zip",
        cache_hit=True,
    )
    marker = root / ".landscout-gpu-extraction.json"
    marker.write_text(
        json.dumps(
            {
                "schema_version": 2,
                "archive_sha256": archive.sha256,
                "files": [
                    {
                        "relative_path": item.relative_path,
                        "size_bytes": item.size_bytes,
                        "sha256": item.sha256,
                    }
                    for item in inventory
                ],
            },
            sort_keys=True,
        ),
        encoding="utf-8",
    )
    extraction = GpuExtraction(
        archive=archive,
        extraction_root=root,
        files=inventory,
        standard_models=("CNIG PLU v2017",),
        cache_hit=True,
    )
    config_payload = base_config.model_dump(mode="python")
    config_payload["spatial_layers"]["zoning"]["match_tokens"] = ["ZONE"]
    source_config = GpuSourceConfig.model_validate(config_payload)
    return GpuPlanningDocument(
        source_config=source_config,
        source_config_sha256=gpu_source_module._source_config_sha256(source_config),
        extraction=extraction,
        all_spatial_layers=(zoning.reference,),
        zoning=zoning,
        related_layers=(),
    )


def _fixture_document(
    tmp_path: Path,
    *,
    filename: str = DEFAULT_PDF,
    zoning_filenames: list[object] | None = None,
    written_filenames: tuple[str, ...] | None = None,
    inventory_filenames: tuple[str, ...] | None = None,
    source_format: str = "GPKG",
    include_nomfic: bool = True,
) -> GpuPlanningDocument:
    root = tmp_path / "extraction"
    inventory_names = (
        (filename,) if inventory_filenames is None else inventory_filenames
    )
    inventory: list[GpuExtractedFile] = []
    for index, name in enumerate(inventory_names):
        relative = f"written-{index}/{name}"
        path = root.joinpath(*relative.split("/"))
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(PDF_BYTES)
        inventory.append(_inventory_item(relative))
    zoning, spatial_inventory = _write_zoning_source(
        root,
        _zone_frame(
            [filename] if zoning_filenames is None else zoning_filenames,
            include_nomfic=include_nomfic,
        ),
        source_format=source_format,
    )
    inventory.extend(spatial_inventory)
    return _document(
        root,
        tuple(inventory),
        zoning,
        zoning_filenames=zoning_filenames or [filename],
        written_filenames=(filename,)
        if written_filenames is None
        else written_filenames,
    )


def _one_page_index(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    text: str = "Énergie",
):
    document = _fixture_document(tmp_path)
    _patch_reader(monkeypatch, [text])
    return index_planning_regulation(document)


def test_public_api_exports_immutable_models_and_validators() -> None:
    for name in (
        "PlanningRegulationIndex",
        "PlanningRegulationIndexError",
        "PlanningRegulationSearchResult",
        "index_planning_regulation",
        "search_planning_regulation",
        "validate_planning_regulation_index",
        "validate_planning_regulation_search_result",
    ):
        assert name in stages.__all__
        assert hasattr(stages, name)


@pytest.mark.parametrize(
    "filename",
    [DEFAULT_PDF, "98765_reglement_20300102.pdf"],
)
def test_source_nomfic_resolves_generic_filename(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    filename: str,
) -> None:
    document = _fixture_document(tmp_path, filename=filename)
    _patch_reader(monkeypatch, ["Texte"])
    result = index_planning_regulation(document)
    assert Path(result.pdf_relative_path).name == filename


def test_explicit_source_validated_selection_succeeds(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    filenames = ("a.pdf", "b.pdf")
    document = _fixture_document(
        tmp_path,
        filename="a.pdf",
        zoning_filenames=list(filenames),
        written_filenames=filenames,
        inventory_filenames=filenames,
    )
    _patch_reader(monkeypatch, ["Texte"])
    result = index_planning_regulation(document, regulation_filename="b.pdf")
    assert Path(result.pdf_relative_path).name == "b.pdf"


@pytest.mark.parametrize("source_format", ["GPKG", "ESRI Shapefile"])
def test_unchanged_zoning_source_is_revalidated_before_selection(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    source_format: str,
) -> None:
    document = _fixture_document(tmp_path, source_format=source_format)
    _patch_reader(monkeypatch, ["Texte"])
    result = index_planning_regulation(document)
    assert result.regulation_filename == DEFAULT_PDF
    assert result.source_selection_method == "ZONING_NOMFIC"
    assert fullmatch(r"[0-9a-f]{64}", result.source_selection_sha256)


def test_mutated_loaded_nomfic_is_rejected_before_selection(tmp_path: Path) -> None:
    document = _fixture_document(tmp_path)
    mutated = document.zoning.data.copy(deep=True)
    mutated.loc[0, "NOMFIC"] = "other_reglement.pdf"
    corrupted = replace(document, zoning=replace(document.zoning, data=mutated))
    with pytest.raises(PlanningRegulationIndexError, match="zoning|source"):
        index_planning_regulation(corrupted)


@pytest.mark.parametrize("mutation", ["reorder", "geometry"])
def test_mutated_loaded_zoning_geometry_or_order_is_rejected(
    tmp_path: Path,
    mutation: str,
) -> None:
    document = _fixture_document(
        tmp_path,
        zoning_filenames=[DEFAULT_PDF, DEFAULT_PDF],
    )
    mutated = document.zoning.data.copy(deep=True)
    if mutation == "reorder":
        mutated = mutated.iloc[::-1].reset_index(drop=True)
    else:
        geometry = mutated.geometry.copy()
        geometry.iloc[0] = Polygon([(20, 0), (20, 1), (21, 1), (21, 0), (20, 0)])
        mutated = mutated.set_geometry(geometry)
    corrupted = replace(document, zoning=replace(document.zoning, data=mutated))
    with pytest.raises(PlanningRegulationIndexError, match="zoning|source"):
        index_planning_regulation(corrupted)


def test_zoning_source_bytes_changed_after_ingestion_are_rejected(
    tmp_path: Path,
) -> None:
    document = _fixture_document(tmp_path)
    with document.zoning.reference.dataset_path.open("ab") as stream:
        stream.write(b"tamper")
    with pytest.raises(PlanningRegulationIndexError, match="size|SHA256|integrity"):
        index_planning_regulation(document)


@pytest.mark.parametrize("field", ["size_bytes", "sha256"])
def test_zoning_source_inventory_integrity_mismatch_is_rejected(
    tmp_path: Path,
    field: str,
) -> None:
    document = _fixture_document(tmp_path)
    items = list(document.extraction.files)
    position = next(
        index for index, item in enumerate(items) if item.category == "SPATIAL_DATA"
    )
    current = items[position]
    replacement: object = current.size_bytes + 1 if field == "size_bytes" else "b" * 64
    items[position] = replace(current, **{field: replacement})
    corrupted = replace(
        document,
        extraction=replace(document.extraction, files=tuple(items)),
    )
    with pytest.raises(PlanningRegulationIndexError, match="size|SHA256|integrity"):
        index_planning_regulation(corrupted)


def test_missing_nomfic_field_is_rejected(tmp_path: Path) -> None:
    document = _fixture_document(tmp_path, include_nomfic=False)
    with pytest.raises(PlanningRegulationIndexError, match="missing NOMFIC"):
        index_planning_regulation(document)


def test_null_nomfic_is_rejected(tmp_path: Path) -> None:
    document = _fixture_document(tmp_path, zoning_filenames=[None])
    with pytest.raises(PlanningRegulationIndexError, match="no regulation filename"):
        index_planning_regulation(document)


def test_multiple_nomfic_values_are_ambiguous(tmp_path: Path) -> None:
    document = _fixture_document(
        tmp_path,
        filename="a.pdf",
        zoning_filenames=["a.pdf", "b.pdf"],
        written_filenames=("a.pdf", "b.pdf"),
        inventory_filenames=("a.pdf", "b.pdf"),
    )
    with pytest.raises(PlanningRegulationIndexError, match="ambiguous"):
        index_planning_regulation(document)


@pytest.mark.parametrize(
    "filename",
    [
        "",
        " file.pdf",
        "file.pdf ",
        "../file.pdf",
        "a/b.pdf",
        "C:\\a.pdf",
        "bad\x00.pdf",
        "file.txt",
    ],
)
def test_unsafe_explicit_filename_is_rejected(tmp_path: Path, filename: str) -> None:
    document = _fixture_document(tmp_path)
    with pytest.raises(PlanningRegulationIndexError, match="filename"):
        index_planning_regulation(document, regulation_filename=filename)


def test_explicit_filename_not_referenced_by_zoning_fails(tmp_path: Path) -> None:
    document = _fixture_document(tmp_path)
    with pytest.raises(PlanningRegulationIndexError, match="not referenced"):
        index_planning_regulation(document, regulation_filename="other.pdf")


def test_filename_absent_from_written_files_fails(tmp_path: Path) -> None:
    document = _fixture_document(tmp_path, written_filenames=("other.pdf",))
    with pytest.raises(PlanningRegulationIndexError, match="written_files"):
        index_planning_regulation(document)


def test_unrelated_non_pdf_written_file_does_not_block_selection(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    document = _fixture_document(
        tmp_path, written_filenames=(DEFAULT_PDF, "technical-note.txt")
    )
    _patch_reader(monkeypatch, ["Texte"])
    assert index_planning_regulation(document).total_page_count == 1


def test_filename_absent_from_inventory_fails(tmp_path: Path) -> None:
    document = _fixture_document(tmp_path)
    item_position = next(
        index
        for index, item in enumerate(document.extraction.files)
        if item.category == "WRITTEN_REGULATION"
    )
    items = list(document.extraction.files)
    items[item_position] = replace(
        items[item_position], relative_path="written/other.pdf"
    )
    corrupted = replace(
        document,
        extraction=replace(document.extraction, files=tuple(items)),
    )
    with pytest.raises(
        PlanningRegulationIndexError,
        match="missing from GPU inventory|verified manifest",
    ):
        index_planning_regulation(corrupted)


def test_duplicate_inventory_basename_fails(tmp_path: Path) -> None:
    document = _fixture_document(
        tmp_path, inventory_filenames=(DEFAULT_PDF, DEFAULT_PDF)
    )
    with pytest.raises(PlanningRegulationIndexError, match="ambiguous"):
        index_planning_regulation(document)


def test_path_outside_root_is_rejected(tmp_path: Path) -> None:
    document = _fixture_document(tmp_path)
    item = replace(document.extraction.files[0], relative_path=f"../{DEFAULT_PDF}")
    corrupted = replace(
        document,
        extraction=replace(document.extraction, files=(item,)),
    )
    with pytest.raises(
        PlanningRegulationIndexError,
        match="unsafe|verified manifest",
    ):
        index_planning_regulation(corrupted)


@pytest.mark.parametrize("field", ["size_bytes", "sha256"])
def test_pdf_inventory_integrity_mismatch_fails(tmp_path: Path, field: str) -> None:
    document = _fixture_document(tmp_path)
    value: object = len(PDF_BYTES) + 1 if field == "size_bytes" else "b" * 64
    item_position = next(
        index
        for index, item in enumerate(document.extraction.files)
        if item.category == "WRITTEN_REGULATION"
    )
    items = list(document.extraction.files)
    items[item_position] = replace(items[item_position], **{field: value})
    corrupted = replace(
        document,
        extraction=replace(document.extraction, files=tuple(items)),
    )
    with pytest.raises(PlanningRegulationIndexError, match="differs"):
        index_planning_regulation(corrupted)


def test_page_states_numbering_and_hashes(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    document = _fixture_document(tmp_path)
    raw = "ÉNERGIE\n Batterie  "
    _patch_reader(monkeypatch, [raw, " \n", RuntimeError("page failed")])
    result = index_planning_regulation(document)
    assert tuple(result.pages.columns) == PAGE_COLUMNS
    assert result.pages.page_number.tolist() == [1, 2, 3]
    assert result.pages.extraction_status.tolist() == ["TEXT", "EMPTY", "ERROR"]
    assert result.pages.loc[0, "raw_text"] == raw
    assert result.pages.loc[0, "normalized_search_text"] == "energie batterie"
    assert result.pages.page_content_sha256.str.fullmatch(r"[0-9a-f]{64}").all()
    assert fullmatch(r"[0-9a-f]{64}", result.pages_content_sha256)
    validate_planning_regulation_index(result)
    with pytest.raises(FrozenInstanceError):
        result.total_page_count = 9  # type: ignore[misc]


def test_zero_page_pdf_is_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    document = _fixture_document(tmp_path)
    _patch_reader(monkeypatch, [])
    with pytest.raises(PlanningRegulationIndexError, match="at least one page"):
        index_planning_regulation(document)


def test_pdf_reader_failure_is_controlled_and_chained(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    document = _fixture_document(tmp_path)

    def fail_reader(*args: object, **kwargs: object) -> object:
        raise RuntimeError("broken xref")

    monkeypatch.setattr(regulation_module, "PdfReader", fail_reader)
    with pytest.raises(
        PlanningRegulationIndexError, match="opened or parsed"
    ) as caught:
        index_planning_regulation(document)
    assert isinstance(caught.value.__cause__, RuntimeError)


@pytest.mark.parametrize(
    ("source", "term"),
    [
        ("ÉNERGIE", "energie"),
        ("intérêt", "interet"),
        ("d’intérêt", "d'interet"),
        ("œuvre", "oeuvre"),
        ("ÆTHER", "aether"),
        ("poste—source", "poste-source"),
        ("inter\u00adruption", "interruption"),
        ("ligne\n   électrique", "ligne electrique"),
    ],
)
def test_french_literal_normalization(source: str, term: str) -> None:
    assert _normalize_search_text(source) == term


def test_raw_context_preserves_source_typography(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    raw = "Le projet vise un Équipement d’intérêt collectif dans la zone."
    index = _one_page_index(tmp_path, monkeypatch, raw)
    result = search_planning_regulation(
        index, ["equipement d'interet collectif"], context_characters=4
    )
    hit = result.hits.iloc[0]
    assert hit["page_number"] == 1
    assert hit["occurrence_count"] == 1
    assert "Équipement d’intérêt collectif" in hit["raw_context"]
    assert "equipement d'interet collectif" in hit["normalized_context"]
    assert index.pages.iloc[0]["raw_text"] == raw


@pytest.mark.parametrize(
    ("raw", "term", "expected_raw", "expected_normalized"),
    [
        ("café", "cafe", "café", "cafe"),
        ("cafe\u0301", "cafe", "cafe\u0301", "cafe"),
        ("œuvre", "oeuvre", "œuvre", "oeuvre"),
        ("æther", "aether", "æther", "aether"),
        ("d’intérêt", "d'interet", "d’intérêt", "d'interet"),
        ("inter\u00adruption", "interruption", "inter\u00adruption", "interruption"),
        ("\u00adcafe", "cafe", "\u00adcafe", "cafe"),
        ("cafe\u00ad", "cafe", "cafe\u00ad", "cafe"),
    ],
)
def test_zero_context_preserves_complete_raw_unicode_span(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    raw: str,
    term: str,
    expected_raw: str,
    expected_normalized: str,
) -> None:
    index = _one_page_index(tmp_path, monkeypatch, raw)
    result = search_planning_regulation(index, [term], context_characters=0)
    hit = result.hits.iloc[0]
    assert hit["raw_context"] == expected_raw
    assert hit["normalized_context"] == expected_normalized
    assert hit["raw_context"] in raw
    assert index.pages.iloc[0]["raw_text"] == raw


def test_literal_search_does_not_add_semantic_synonyms(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    index = _one_page_index(tmp_path, monkeypatch, "Une batterie est mentionnée.")
    result = search_planning_regulation(index, ["accumulateur"])
    assert result.hits.empty


def test_version_discovery_failure_is_controlled_and_chained(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    document = _fixture_document(tmp_path)
    _patch_reader(monkeypatch, ["Texte"])

    def fail_version(name: str) -> str:
        raise RuntimeError(name)

    monkeypatch.setattr(regulation_module, "version", fail_version)
    with pytest.raises(PlanningRegulationIndexError, match="version") as caught:
        index_planning_regulation(document)
    assert isinstance(caught.value.__cause__, RuntimeError)


def test_coordinated_page_mutation_fails_envelope_hash(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    index = _one_page_index(tmp_path, monkeypatch)
    pages = index.pages.copy(deep=True)
    pages.loc[0, "raw_text"] = "Nouveau"
    pages.loc[0, "normalized_search_text"] = "nouveau"
    pages.loc[0, "character_count"] = 7
    row = pages.iloc[0].to_dict()
    pages.loc[0, "page_content_sha256"] = regulation_module._page_content_sha256(row)
    with pytest.raises(PlanningRegulationIndexError, match="envelope"):
        validate_planning_regulation_index(replace(index, pages=pages))


@pytest.mark.parametrize(
    ("target", "value"),
    [
        ("page_hash", "b" * 64),
        ("envelope_hash", "b" * 64),
        ("profile", "other_v1"),
        ("order", None),
    ],
)
def test_index_integrity_mutations_fail(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    target: str,
    value: object,
) -> None:
    document = _fixture_document(tmp_path)
    _patch_reader(monkeypatch, ["One", "Two"])
    index = index_planning_regulation(document)
    if target == "page_hash":
        pages = index.pages.copy(deep=True)
        pages.loc[0, "page_content_sha256"] = value
        corrupted = replace(index, pages=pages)
    elif target == "envelope_hash":
        corrupted = replace(index, pages_content_sha256=value)
    elif target == "profile":
        corrupted = replace(index, search_normalization_profile=value)
    else:
        corrupted = replace(index, pages=index.pages.iloc[::-1].reset_index(drop=True))
    with pytest.raises(PlanningRegulationIndexError):
        validate_planning_regulation_index(corrupted)


@pytest.mark.parametrize(
    ("field", "replacement"),
    [
        ("document_id", "other-document"),
        ("archive_sha256", "b" * 64),
        ("regulation_filename", "other_reglement.pdf"),
        ("source_selection_method", "EXPLICIT_FILENAME"),
        ("source_selection_sha256", "b" * 64),
        ("pdf_relative_path", "written-0/other_reglement.pdf"),
        ("pdf_size_bytes", len(PDF_BYTES) + 1),
        ("pdf_sha256", "b" * 64),
        ("extraction_library", "other-reader"),
        ("extraction_library_version", "0.0.0"),
        ("search_normalization_profile", "other-profile"),
        ("page_hash_schema_version", 2),
        ("total_page_count", 2),
        ("pages_content_sha256", "b" * 64),
        ("index_content_sha256", "b" * 64),
    ],
)
def test_complete_index_envelope_mutation_is_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    field: str,
    replacement: object,
) -> None:
    index = _one_page_index(tmp_path, monkeypatch)
    with pytest.raises(PlanningRegulationIndexError):
        validate_planning_regulation_index(replace(index, **{field: replacement}))


@pytest.mark.parametrize("replacement", [0, -1, 1.5, "1", 2])
def test_unsupported_or_malformed_index_hash_schema_is_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    replacement: object,
) -> None:
    index = _one_page_index(tmp_path, monkeypatch)
    with pytest.raises(PlanningRegulationIndexError):
        validate_planning_regulation_index(
            replace(index, index_hash_schema_version=replacement)
        )


@pytest.mark.parametrize("replacement", [0, -1, 1.5, "1"])
def test_malformed_page_hash_schema_is_rejected_as_controlled_error(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    replacement: object,
) -> None:
    index = _one_page_index(tmp_path, monkeypatch)
    with pytest.raises(PlanningRegulationIndexError):
        validate_planning_regulation_index(
            replace(index, page_hash_schema_version=replacement)
        )


def _valid_search_result(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
):
    index = _one_page_index(
        tmp_path,
        monkeypatch,
        "Énergie énergie et Équipement d’intérêt collectif",
    )
    result = search_planning_regulation(
        index, ["energie", "equipement d'interet collectif"]
    )
    return index, result


def test_search_result_envelope_is_valid_and_deterministic(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    index, first = _valid_search_result(tmp_path, monkeypatch)
    second = search_planning_regulation(index, first.requested_terms)
    assert tuple(first.hits.columns) == SEARCH_HIT_COLUMNS
    assert first.search_normalization_profile == SEARCH_NORMALIZATION_PROFILE
    assert first.index_content_sha256 == index.index_content_sha256
    assert (
        first.search_hash_schema_version == regulation_module.SEARCH_HASH_SCHEMA_VERSION
    )
    assert first.hit_count == 2
    assert_frame_equal(first.hits, second.hits)
    assert first.hits_content_sha256 == second.hits_content_sha256
    validate_planning_regulation_search_result(index, first)


@pytest.mark.parametrize(
    ("field", "replacement"),
    [
        ("index_content_sha256", "b" * 64),
        ("search_hash_schema_version", 2),
        ("search_hash_schema_version", 0),
        ("search_hash_schema_version", -1),
        ("search_hash_schema_version", 1.5),
        ("search_hash_schema_version", "1"),
        ("requested_terms", ("other-term",)),
    ],
)
def test_search_index_identity_schema_and_terms_are_sealed(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    field: str,
    replacement: object,
) -> None:
    index, result = _valid_search_result(tmp_path, monkeypatch)
    with pytest.raises(PlanningRegulationIndexError):
        validate_planning_regulation_search_result(
            index,
            replace(result, **{field: replacement}),
        )


def test_search_requested_terms_must_be_an_immutable_exact_tuple(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    index, result = _valid_search_result(tmp_path, monkeypatch)
    corrupted = replace(
        result,
        requested_terms=list(result.requested_terms),  # type: ignore[arg-type]
    )
    with pytest.raises(PlanningRegulationIndexError, match="tuple"):
        validate_planning_regulation_search_result(index, corrupted)


@pytest.mark.parametrize(
    ("target", "value"),
    [
        ("document_id", "wrong"),
        ("pdf_sha256", "b" * 64),
        ("page_number", 99),
        ("duplicate", None),
        ("occurrence_count", 0),
        ("occurrence_count", 1.5),
        ("occurrence_count", "1"),
        ("raw_context", "corrupted"),
        ("hits_content_sha256", "b" * 64),
    ],
)
def test_search_result_integrity_mutations_fail(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    target: str,
    value: object,
) -> None:
    index, result = _valid_search_result(tmp_path, monkeypatch)
    if target in {"document_id", "pdf_sha256", "hits_content_sha256"}:
        corrupted = replace(result, **{target: value})
    else:
        hits = result.hits.copy(deep=True)
        if target == "duplicate":
            hits = pd.concat([hits, hits.iloc[[0]]], ignore_index=True)
            corrupted = replace(result, hit_count=len(hits), hits=hits)
        else:
            hits[target] = hits[target].astype(object)
            hits.loc[0, target] = value
            corrupted = replace(result, hits=hits)
    with pytest.raises(PlanningRegulationIndexError):
        validate_planning_regulation_search_result(index, corrupted)


@pytest.mark.parametrize("column", ["document_id", "pdf_sha256"])
def test_search_hit_lineage_mutation_fails(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    column: str,
) -> None:
    index, result = _valid_search_result(tmp_path, monkeypatch)
    hits = result.hits.copy(deep=True)
    hits.loc[0, column] = "b" * 64 if column == "pdf_sha256" else "wrong"
    corrupted = replace(result, hits=hits)
    with pytest.raises(PlanningRegulationIndexError, match="lineage"):
        validate_planning_regulation_search_result(index, corrupted)


@pytest.mark.parametrize("term", ["", "   ", " term", "term ", 7])
def test_invalid_search_term_is_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    term: object,
) -> None:
    index = _one_page_index(tmp_path, monkeypatch)
    with pytest.raises(PlanningRegulationIndexError, match="search term"):
        search_planning_regulation(index, [term])  # type: ignore[list-item]


def test_duplicate_normalized_search_terms_are_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    index = _one_page_index(tmp_path, monkeypatch)
    with pytest.raises(PlanningRegulationIndexError, match="unique"):
        search_planning_regulation(index, ["énergie", "ENERGIE"])


def test_empty_search_result_has_stable_schema_and_lineage(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    index = _one_page_index(tmp_path, monkeypatch, "Aucun terme")
    result = search_planning_regulation(index, ["batterie"])
    assert result.hit_count == 0
    assert result.hits.empty
    assert tuple(result.hits.columns) == SEARCH_HIT_COLUMNS
    assert result.document_id == index.document_id
    assert result.pdf_sha256 == index.pdf_sha256
    validate_planning_regulation_search_result(index, result)


def test_malformed_page_value_raises_controlled_index_error(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    index = _one_page_index(tmp_path, monkeypatch)
    pages = index.pages.copy(deep=True)
    pages.at[0, "extraction_error"] = ["ambiguous", "value"]
    with pytest.raises(PlanningRegulationIndexError):
        validate_planning_regulation_index(replace(index, pages=pages))


def test_malformed_hit_value_raises_controlled_index_error(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    index, result = _valid_search_result(tmp_path, monkeypatch)
    hits = result.hits.copy(deep=True)
    hits["raw_context"] = hits["raw_context"].astype(object)
    hits.at[0, "raw_context"] = ["not", "text"]
    with pytest.raises(PlanningRegulationIndexError):
        validate_planning_regulation_search_result(
            index,
            replace(result, hits=hits),
        )


def test_canonical_hash_serialization_failure_is_controlled_and_chained() -> None:
    invalid_payload = {"not_json": object()}
    with pytest.raises(
        PlanningRegulationIndexError,
        match="serialized",
    ) as caught:
        regulation_module._canonical_sha256(invalid_payload)
    assert isinstance(caught.value.__cause__, TypeError)


def test_malformed_source_metadata_raises_controlled_index_error(
    tmp_path: Path,
) -> None:
    document = _fixture_document(tmp_path)
    metadata = replace(
        document.extraction.archive.document,
        written_files=(object(),),  # type: ignore[arg-type]
    )
    archive = replace(document.extraction.archive, document=metadata)
    corrupted = replace(
        document,
        extraction=replace(document.extraction, archive=archive),
    )
    with pytest.raises(PlanningRegulationIndexError):
        index_planning_regulation(corrupted)


def test_extraction_and_search_do_not_mutate_inputs(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    document = _fixture_document(tmp_path)
    extraction_before = deepcopy(document.extraction)
    zoning_before = document.zoning.data.copy(deep=True)
    _patch_reader(monkeypatch, ["Énergie"])
    index = index_planning_regulation(document)
    pages_before = index.pages.copy(deep=True)
    search_planning_regulation(index, ["energie"])
    assert document.extraction == extraction_before
    assert_geodataframe_equal(document.zoning.data, zoning_before)
    assert_frame_equal(index.pages, pages_before)
