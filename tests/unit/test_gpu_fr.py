from __future__ import annotations

import io
import json
import warnings
import zipfile
from dataclasses import replace
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Self
from urllib.error import URLError

import geopandas as gpd  # type: ignore[import-untyped]
import pytest
from pydantic import HttpUrl, ValidationError
from shapely.geometry import Polygon

import landscout.sources.gpu_fr as gpu
from landscout.sources.gpu_fr import (
    GpuArchiveDownload,
    GpuArchiveError,
    GpuDiscoveryError,
    GpuDownloadError,
    GpuExtraction,
    GpuSourceConfig,
    GpuSpatialInspectionError,
    build_gpu_document_list_url,
    build_gpu_partition,
    build_gpu_partition_download_url,
    discover_current_gpu_document,
    discover_gpu_spatial_layers,
    download_gpu_document,
    extract_gpu_document,
    inspect_gpu_planning_document,
    load_gpu_source_config,
    validate_gpu_archive,
)

_UNSAFE_ARCHIVE_NAMES = (
    "../escape",
    r"..\escape",
    "/absolute",
    r"C:\absolute",
    ".",
    "..",
    " leading",
    "trailing ",
    "nul\x00name",
    "CON",
    "nul.txt",
    "bad:name",
    "bad?.zip",
    "trailing.",
    "archive.zip.zip",
    "a" * 252,
)


class _Response(io.BytesIO):
    def __enter__(self) -> Self:
        return self

    def __exit__(self, *args: object) -> None:
        self.close()


def _config() -> GpuSourceConfig:
    return load_gpu_source_config(Path("configs/sources/gpu_fr.yaml"))


def _listing_item(**overrides: object) -> dict[str, object]:
    result: dict[str, object] = {
        "id": "doc-1",
        "status": "document.production",
        "legalStatus": "APPROVED",
        "effectiveStatus": "EN_VIGUEUR",
        "originalName": "31395_PLU_20240215",
        "type": "PLU",
        "name": "DU_31395",
        "grid": {"name": "31395", "title": "MURET"},
    }
    result.update(overrides)
    return result


def _details(**overrides: object) -> dict[str, object]:
    result = _listing_item(
        title="Plan Local d'Urbanisme de Muret",
        producer="Mairie de Muret",
        projectionCode="EPSG:2154",
        publicationDate="26/03/2024 08:52:34",
        updateDate="26/03/2024 08:52:34",
        metadata="fr-000031395-plu20240215",
        archiveUrl="https://www.geoportail-urbanisme.gouv.fr/api/document/doc-1/download/31395_PLU_20240215.zip",
        writingMaterials={
            "reglement.pdf": "https://www.geoportail-urbanisme.gouv.fr/api/document/doc-1/files/reglement.pdf"
        },
    )
    result.update(overrides)
    return result


def _files() -> list[dict[str, object]]:
    return [{"name": "reglement.pdf", "title": "Règlement écrit", "path": "Règlements"}]


def _patch_json_responses(monkeypatch: pytest.MonkeyPatch, values: list[object]) -> None:
    responses = iter(values)

    def opener(*args: object, **kwargs: object) -> _Response:
        return _Response(json.dumps(next(responses)).encode())

    monkeypatch.setattr(gpu, "open_safe_https", opener)


def _document(monkeypatch: pytest.MonkeyPatch):
    _patch_json_responses(monkeypatch, [[_listing_item()], _details(), _files()])
    return discover_current_gpu_document(_config())


def _zip_bytes(files: dict[str, bytes] | None = None) -> bytes:
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name, content in (files or {"document/readme.txt": b"GPU"}).items():
            archive.writestr(name, content)
    return stream.getvalue()


def _zip_member_bytes(members: list[tuple[str, bytes]]) -> bytes:
    stream = io.BytesIO()
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)
        with zipfile.ZipFile(stream, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            for name, content in members:
                archive.writestr(name, content)
    return stream.getvalue()


def _download(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    archive_bytes: bytes | None = None,
) -> GpuArchiveDownload:
    document = _document(monkeypatch)
    monkeypatch.setattr(gpu, "open_safe_https", lambda *args, **kwargs: _Response(archive_bytes or _zip_bytes()))
    return download_gpu_document(document, _config(), tmp_path)


def _planning_archive(tmp_path: Path) -> Path:
    package = tmp_path / "package"
    package.mkdir()
    gpkg = package / "planning.gpkg"
    valid = Polygon([(0, 0), (10, 0), (10, 10), (0, 10)])
    invalid = Polygon([(0, 0), (10, 10), (10, 0), (0, 10), (0, 0)])
    zoning = gpd.GeoDataFrame(
        {"LIBELLE": ["U", "N", None], "TYPEZONE": ["U", "N", "AU"]},
        geometry=[valid, invalid, None],
        crs="EPSG:2154",
    )
    prescription = gpd.GeoDataFrame(
        {"TYPEPSC": [5]}, geometry=[valid], crs="EPSG:2154"
    )
    zoning.to_file(gpkg, layer="zone_urba", driver="GPKG", engine="pyogrio")
    prescription.to_file(
        gpkg, layer="prescription_surf", driver="GPKG", engine="pyogrio", mode="a"
    )
    (package / "31395_reglement.pdf").write_bytes(b"%PDF synthetic")
    (package / "metadata.xml").write_text(
        "<metadata><standard>CNIG PLU v2017</standard></metadata>", encoding="utf-8"
    )
    archive_path = tmp_path / "planning.zip"
    with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in package.rglob("*"):
            if path.is_file():
                archive.write(path, path.relative_to(package).as_posix())
    return archive_path


def test_valid_config_and_urls() -> None:
    config = _config()
    assert build_gpu_partition(config) == "DU_31395"
    assert "partition=DU_31395" in build_gpu_document_list_url(config)
    assert build_gpu_partition_download_url(config).endswith(
        "/document/download-by-partition/DU_31395"
    )


@pytest.mark.parametrize(
    ("path", "value"),
    [
        (("pilot", "commune_code"), "3139"),
        (("api", "base_url"), "file:///api"),
        (("api", "base_url"), "http://www.geoportail-urbanisme.gouv.fr/api"),
        (("api", "base_url"), "https://example.com/api"),
        (("api", "base_url"), "https://www.geoportail-urbanisme.gouv.fr:8443/api"),
        (("api", "base_url"), "https://www.geoportail-urbanisme.gouv.fr/api?x=1"),
        (("download", "strategy"), "parcel"),
        (("download", "partition_template"), ""),
        (("cache", "max_age_hours"), -1),
    ],
)
def test_invalid_config_values_are_rejected(path: tuple[str, str], value: object) -> None:
    payload = _config().model_dump(mode="json")
    payload[path[0]][path[1]] = value
    with pytest.raises(ValidationError):
        GpuSourceConfig.model_validate(payload)


def test_mutated_loaded_api_origin_is_rejected_before_discovery_network(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config = _config()
    config.api.base_url = HttpUrl("https://unrelated.example/api")
    network_calls = 0

    def fail_network(*args: object, **kwargs: object) -> object:
        nonlocal network_calls
        network_calls += 1
        raise AssertionError("network used after GPU origin mutation")

    monkeypatch.setattr(gpu, "open_safe_https", fail_network)

    with pytest.raises(GpuDiscoveryError, match="config|official|origin"):
        discover_current_gpu_document(config)

    assert network_calls == 0


def test_unknown_config_field_is_rejected() -> None:
    payload = _config().model_dump(mode="json")
    payload["unexpected"] = True
    with pytest.raises(ValidationError):
        GpuSourceConfig.model_validate(payload)


def test_document_discovery_success(monkeypatch: pytest.MonkeyPatch) -> None:
    document = _document(monkeypatch)
    assert document.document_id == "doc-1"
    assert document.document_type == "PLU"
    assert document.effective_status == "EN_VIGUEUR"
    assert document.archive_name == "31395_PLU_20240215"
    assert document.version is None
    assert document.written_files[0].title == "Règlement écrit"
    assert document.written_files[0].source_url == (
        "https://www.geoportail-urbanisme.gouv.fr/api/document/"
        "doc-1/files/reglement.pdf"
    )


@pytest.mark.parametrize(
    "source_url",
    [
        (
            "http://www.geoportail-urbanisme.gouv.fr/api/document/"
            "doc-1/files/reglement.pdf"
        ),
        "https://unrelated.example/api/document/doc-1/files/reglement.pdf",
    ],
    ids=["http", "unrelated-https-origin"],
)
def test_written_material_url_must_be_exact_official_https_api_url(
    monkeypatch: pytest.MonkeyPatch,
    source_url: str,
) -> None:
    _patch_json_responses(
        monkeypatch,
        [
            [_listing_item()],
            _details(writingMaterials={"reglement.pdf": source_url}),
            _files(),
        ],
    )

    with pytest.raises(GpuDiscoveryError, match="written material URL"):
        discover_current_gpu_document(_config())


@pytest.mark.parametrize(
    "archive_url",
    [
        (
            "http://www.geoportail-urbanisme.gouv.fr/api/document/"
            "doc-1/download/31395_PLU_20240215.zip"
        ),
        (
            "https://unrelated.example/api/document/doc-1/download/"
            "31395_PLU_20240215.zip"
        ),
    ],
    ids=["http", "unrelated-https-origin"],
)
def test_written_material_fallback_rejects_unsafe_archive_url_provenance(
    monkeypatch: pytest.MonkeyPatch,
    archive_url: str,
) -> None:
    _patch_json_responses(
        monkeypatch,
        [
            [_listing_item()],
            _details(archiveUrl=archive_url, writingMaterials={}),
            _files(),
        ],
    )

    with pytest.raises(GpuDiscoveryError, match="archive URL"):
        discover_current_gpu_document(_config())


def test_no_current_document_is_rejected(monkeypatch: pytest.MonkeyPatch) -> None:
    _patch_json_responses(monkeypatch, [[_listing_item(status="document.deleted")]])
    with pytest.raises(GpuDiscoveryError, match="No current"):
        discover_current_gpu_document(_config())


def test_ambiguous_current_documents_are_rejected(monkeypatch: pytest.MonkeyPatch) -> None:
    _patch_json_responses(monkeypatch, [[_listing_item(), _listing_item(id="doc-2")]])
    with pytest.raises(GpuDiscoveryError, match="Ambiguous"):
        discover_current_gpu_document(_config())


@pytest.mark.parametrize("field", ["id", "originalName", "type"])
def test_missing_document_identity_is_rejected(
    monkeypatch: pytest.MonkeyPatch, field: str
) -> None:
    item = _listing_item()
    item.pop(field)
    _patch_json_responses(monkeypatch, [[item]])
    with pytest.raises(GpuDiscoveryError, match="missing"):
        discover_current_gpu_document(_config())


@pytest.mark.parametrize(
    ("field", "different_value"),
    [
        ("id", "doc-2"),
        ("originalName", "31395_PLU_OTHER"),
        ("name", "DU_99999"),
        ("type", "CC"),
        ("status", "document.deleted"),
        ("legalStatus", "CANCELLED"),
        ("effectiveStatus", "ANNULE"),
    ],
)
def test_document_details_must_match_selected_listing(
    monkeypatch: pytest.MonkeyPatch,
    field: str,
    different_value: str,
) -> None:
    _patch_json_responses(
        monkeypatch,
        [[_listing_item()], _details(**{field: different_value}), _files()],
    )

    with pytest.raises(GpuDiscoveryError, match="match|changed|current"):
        discover_current_gpu_document(_config())


def test_document_details_commune_must_match_selected_listing(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _patch_json_responses(
        monkeypatch,
        [
            [_listing_item()],
            _details(grid={"name": "99999", "title": "OTHER"}),
            _files(),
        ],
    )

    with pytest.raises(GpuDiscoveryError, match="match"):
        discover_current_gpu_document(_config())


@pytest.mark.parametrize(
    "archive_name",
    _UNSAFE_ARCHIVE_NAMES,
)
def test_discovery_rejects_unsafe_archive_name(
    monkeypatch: pytest.MonkeyPatch,
    archive_name: str,
) -> None:
    _patch_json_responses(
        monkeypatch,
        [
            [_listing_item(originalName=archive_name)],
            _details(originalName=archive_name),
            _files(),
        ],
    )

    with pytest.raises(GpuDiscoveryError, match="archive name|safe"):
        discover_current_gpu_document(_config())


def test_successful_download_persists_sha_and_sidecar(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    result = _download(tmp_path, monkeypatch)
    sidecar = json.loads((tmp_path / f"{result.filename}.metadata.json").read_text())
    assert result.path.is_file()
    assert result.file_size > 0
    assert len(result.sha256) == 64
    assert sidecar["sha256"] == result.sha256
    assert sidecar["document"]["document_id"] == "doc-1"
    assert not list(tmp_path.glob("*.part"))


@pytest.mark.parametrize(
    ("field", "different_value"),
    [
        ("provider", "OTHER PROVIDER"),
        ("portal", "OTHER PORTAL"),
        ("commune_code", "99999"),
        ("partition", "DU_99999"),
        ("status", "document.deleted"),
        ("legal_status", "CANCELLED"),
        ("effective_status", "ANNULE"),
        ("source_url", "https://example.test/not-the-gpu.zip"),
        (
            "source_url",
            (
                "https://www.geoportail-urbanisme.gouv.fr/api/document/"
                "download-by-partition/DU_99999"
            ),
        ),
    ],
)
def test_download_rejects_document_inconsistent_with_config(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    field: str,
    different_value: str,
) -> None:
    document = replace(_document(monkeypatch), **{field: different_value})
    monkeypatch.setattr(
        gpu,
        "open_safe_https",
        lambda *args, **kwargs: pytest.fail("invalid document reached network"),
    )

    with pytest.raises(GpuDownloadError, match="document|identity|config"):
        download_gpu_document(document, _config(), tmp_path)

    assert not any(tmp_path.iterdir())


@pytest.mark.parametrize("mutation", ["forged-source-url", "wrong-item-type"])
def test_download_rejects_forged_written_file_provenance_before_network(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    mutation: str,
) -> None:
    original = _document(monkeypatch)
    if mutation == "forged-source-url":
        written_files = (
            replace(
                original.written_files[0],
                source_url="http://unrelated.example/reglement.pdf",
            ),
        )
    else:
        written_files = (object(),)
    document = replace(original, written_files=written_files)  # type: ignore[arg-type]
    network_calls = 0

    def fail_network(*args: object, **kwargs: object) -> object:
        nonlocal network_calls
        network_calls += 1
        raise AssertionError("forged written-file provenance reached network")

    monkeypatch.setattr(gpu, "open_safe_https", fail_network)

    with pytest.raises(GpuDownloadError, match="written|document|source|URL"):
        download_gpu_document(document, _config(), tmp_path)

    assert network_calls == 0


@pytest.mark.parametrize(
    "archive_name",
    _UNSAFE_ARCHIVE_NAMES,
)
def test_download_rejects_forged_unsafe_archive_name_before_io(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    archive_name: str,
) -> None:
    document = replace(_document(monkeypatch), archive_name=archive_name)
    monkeypatch.setattr(
        gpu,
        "open_safe_https",
        lambda *args, **kwargs: pytest.fail("unsafe archive name reached network"),
    )

    with pytest.raises(GpuDownloadError, match="archive name|archive filename|safe"):
        download_gpu_document(document, _config(), tmp_path / "cache")

    assert not (tmp_path / "escape.zip").exists()


def test_archive_name_with_one_zip_suffix_is_not_duplicated(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    document = replace(_document(monkeypatch), archive_name="safe-name.zip")
    monkeypatch.setattr(
        gpu,
        "open_safe_https",
        lambda *args, **kwargs: _Response(_zip_bytes()),
    )

    result = download_gpu_document(document, _config(), tmp_path)

    assert result.filename == "safe-name.zip"
    assert result.path == tmp_path / "safe-name.zip"


def test_fresh_cache_is_reused(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    first = _download(tmp_path, monkeypatch)
    monkeypatch.setattr(gpu, "open_safe_https", lambda *args, **kwargs: pytest.fail("network used"))
    second = download_gpu_document(first.document, _config(), tmp_path)
    assert second.cache_hit
    assert second.sha256 == first.sha256


def test_stale_recovery_backup_rejects_cache_before_network(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    first = _download(tmp_path, monkeypatch)
    recovery_path = first.path.with_suffix(f"{first.path.suffix}.bak")
    recovery_bytes = b"manual GPU recovery material"
    recovery_path.write_bytes(recovery_bytes)

    def fail_network(*args: object, **kwargs: object) -> _Response:
        pytest.fail("stale recovery must fail before network")

    monkeypatch.setattr(gpu, "open_safe_https", fail_network)
    with pytest.raises(GpuDownloadError, match="backup|recovery|manual"):
        download_gpu_document(first.document, _config(), tmp_path)

    assert recovery_path.read_bytes() == recovery_bytes


def test_expired_cache_is_refreshed(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    first = _download(tmp_path, monkeypatch)
    sidecar_path = tmp_path / f"{first.filename}.metadata.json"
    sidecar = json.loads(sidecar_path.read_text())
    sidecar["download_timestamp"] = (datetime.now(UTC) - timedelta(days=8)).isoformat()
    sidecar_path.write_text(json.dumps(sidecar), encoding="utf-8")
    fresh_bytes = _zip_bytes({"fresh.txt": b"fresh"})
    monkeypatch.setattr(gpu, "open_safe_https", lambda *args, **kwargs: _Response(fresh_bytes))
    refreshed = download_gpu_document(first.document, _config(), tmp_path)
    assert not refreshed.cache_hit
    assert refreshed.sha256 != first.sha256


def test_failed_refresh_preserves_previous_cache(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    first = _download(tmp_path, monkeypatch)
    sidecar_path = tmp_path / f"{first.filename}.metadata.json"
    sidecar = json.loads(sidecar_path.read_text())
    sidecar["download_timestamp"] = (datetime.now(UTC) - timedelta(days=8)).isoformat()
    sidecar_path.write_text(json.dumps(sidecar), encoding="utf-8")
    old_archive = first.path.read_bytes()
    old_sidecar = sidecar_path.read_bytes()

    def fail(*args: object, **kwargs: object) -> _Response:
        raise URLError("offline")

    monkeypatch.setattr(gpu, "open_safe_https", fail)
    with pytest.raises(GpuDownloadError):
        download_gpu_document(first.document, _config(), tmp_path)
    assert first.path.read_bytes() == old_archive
    assert sidecar_path.read_bytes() == old_sidecar
    assert not list(tmp_path.glob("*.part"))


def test_metadata_publication_failure_rolls_back_both_cache_files(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    first = _download(tmp_path, monkeypatch)
    sidecar_path = tmp_path / f"{first.filename}.metadata.json"
    sidecar = json.loads(sidecar_path.read_text())
    sidecar["download_timestamp"] = (datetime.now(UTC) - timedelta(days=8)).isoformat()
    sidecar_path.write_text(json.dumps(sidecar), encoding="utf-8")
    old_archive = first.path.read_bytes()
    old_sidecar = sidecar_path.read_bytes()
    monkeypatch.setattr(
        gpu, "open_safe_https", lambda *args, **kwargs: _Response(_zip_bytes({"fresh": b"x"}))
    )
    original_replace = gpu._replace_file
    failed = False

    def fail_new_metadata_once(source: Path, target: Path) -> None:
        nonlocal failed
        if source.suffix == ".part" and target == sidecar_path and not failed:
            failed = True
            raise OSError("simulated metadata lock")
        original_replace(source, target)

    monkeypatch.setattr(gpu, "_replace_file", fail_new_metadata_once)
    with pytest.raises(GpuDownloadError):
        download_gpu_document(first.document, _config(), tmp_path)
    assert first.path.read_bytes() == old_archive
    assert sidecar_path.read_bytes() == old_sidecar
    assert not list(tmp_path.glob("*.part"))
    assert not list(tmp_path.glob("*.bak"))


def test_publication_and_rollback_failure_preserves_exact_recovery_backups(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    archive_path = tmp_path / "cached.zip"
    metadata_path = tmp_path / "cached.zip.metadata.json"
    temporary_archive = tmp_path / "cached.zip.part"
    temporary_metadata = tmp_path / "cached.zip.metadata.json.part"
    old_archive = b"exact old archive"
    old_metadata = b"exact old metadata"
    archive_path.write_bytes(old_archive)
    metadata_path.write_bytes(old_metadata)
    temporary_archive.write_bytes(b"replacement archive")
    temporary_metadata.write_bytes(b"replacement metadata")
    archive_backup = archive_path.with_suffix(f"{archive_path.suffix}.bak")
    metadata_backup = metadata_path.with_suffix(f"{metadata_path.suffix}.bak")
    original_replace = gpu._replace_file

    def fail_publication_and_rollback(source: Path, target: Path) -> None:
        if source == temporary_metadata and target == metadata_path:
            raise OSError("simulated metadata publication failure")
        if source == archive_backup and target == archive_path:
            raise OSError("simulated archive rollback failure")
        original_replace(source, target)

    monkeypatch.setattr(
        gpu,
        "_replace_file",
        fail_publication_and_rollback,
    )
    with pytest.raises(GpuDownloadError, match="rollback"):
        gpu._publish_cache_pair(
            temporary_archive,
            temporary_metadata,
            archive_path,
            metadata_path,
        )

    assert archive_backup.read_bytes() == old_archive
    assert metadata_backup.read_bytes() == old_metadata


def test_cleanup_failure_does_not_mask_double_failure_recovery_error(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    first = _download(tmp_path, monkeypatch)
    metadata_path = tmp_path / f"{first.filename}.metadata.json"
    metadata = json.loads(metadata_path.read_text())
    metadata["download_timestamp"] = (
        datetime.now(UTC) - timedelta(days=8)
    ).isoformat()
    metadata_path.write_text(json.dumps(metadata), encoding="utf-8")
    old_archive = first.path.read_bytes()
    old_metadata = metadata_path.read_bytes()
    temporary_metadata = metadata_path.with_suffix(f"{metadata_path.suffix}.part")
    archive_backup = first.path.with_suffix(f"{first.path.suffix}.bak")
    metadata_backup = metadata_path.with_suffix(f"{metadata_path.suffix}.bak")
    original_replace = gpu._replace_file
    original_unlink = Path.unlink
    rollback_failed = False

    def fail_publication_and_rollback(source: Path, target: Path) -> None:
        nonlocal rollback_failed
        if source == temporary_metadata and target == metadata_path:
            raise OSError("simulated metadata publication failure")
        if source == archive_backup and target == first.path:
            rollback_failed = True
            raise OSError("simulated archive rollback failure")
        original_replace(source, target)

    def fail_temporary_cleanup(path: Path, *, missing_ok: bool = False) -> None:
        if rollback_failed and path == temporary_metadata:
            raise PermissionError("simulated temporary cleanup failure")
        original_unlink(path, missing_ok=missing_ok)

    monkeypatch.setattr(
        gpu,
        "open_safe_https",
        lambda *args, **kwargs: _Response(_zip_bytes({"fresh": b"x"})),
    )
    monkeypatch.setattr(gpu, "_replace_file", fail_publication_and_rollback)
    monkeypatch.setattr(Path, "unlink", fail_temporary_cleanup)
    with pytest.raises(GpuDownloadError, match="rollback"):
        download_gpu_document(first.document, _config(), tmp_path)

    assert archive_backup.read_bytes() == old_archive
    assert metadata_backup.read_bytes() == old_metadata


def test_stale_cache_recovery_backup_fails_closed_without_destroying_it(
    tmp_path: Path,
) -> None:
    archive_path = tmp_path / "cached.zip"
    metadata_path = tmp_path / "cached.zip.metadata.json"
    temporary_archive = tmp_path / "cached.zip.part"
    temporary_metadata = tmp_path / "cached.zip.metadata.json.part"
    archive_backup = tmp_path / "cached.zip.bak"
    archive_path.write_bytes(b"old archive")
    metadata_path.write_bytes(b"old metadata")
    temporary_archive.write_bytes(b"new archive")
    temporary_metadata.write_bytes(b"new metadata")
    archive_backup.write_bytes(b"manual recovery archive")

    with pytest.raises(GpuDownloadError, match="backup|recovery|manual"):
        gpu._publish_cache_pair(
            temporary_archive,
            temporary_metadata,
            archive_path,
            metadata_path,
        )

    assert archive_path.read_bytes() == b"old archive"
    assert metadata_path.read_bytes() == b"old metadata"
    assert archive_backup.read_bytes() == b"manual recovery archive"


def test_preexisting_temporary_archive_symlink_cannot_modify_target(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    document = _document(monkeypatch)
    filename = gpu._safe_gpu_archive_filename(document.archive_name)
    temporary_archive = tmp_path / f"{filename}.part"
    sentinel = tmp_path / "do-not-overwrite.txt"
    sentinel_bytes = b"irreplaceable sentinel bytes"
    sentinel.write_bytes(sentinel_bytes)
    original_is_symlink = Path.is_symlink
    original_open = Path.open

    def simulated_is_symlink(path: Path) -> bool:
        return path == temporary_archive or original_is_symlink(path)

    def simulated_symlink_open(
        path: Path, *args: object, **kwargs: object
    ) -> object:
        if path == temporary_archive:
            return original_open(sentinel, *args, **kwargs)
        return original_open(path, *args, **kwargs)

    opener_calls = 0

    def record_network(*args: object, **kwargs: object) -> _Response:
        nonlocal opener_calls
        opener_calls += 1
        return _Response(_zip_bytes())

    monkeypatch.setattr(Path, "is_symlink", simulated_is_symlink)
    monkeypatch.setattr(Path, "open", simulated_symlink_open)
    monkeypatch.setattr(gpu, "open_safe_https", record_network)

    with pytest.raises(GpuDownloadError):
        download_gpu_document(document, _config(), tmp_path)

    assert opener_calls == 0
    assert sentinel.read_bytes() == sentinel_bytes


def test_corrupt_download_is_rejected(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    document = _document(monkeypatch)
    monkeypatch.setattr(gpu, "open_safe_https", lambda *args, **kwargs: _Response(b"not zip"))
    with pytest.raises(GpuDownloadError):
        download_gpu_document(document, _config(), tmp_path)
    assert not list(tmp_path.glob("*.part"))


def test_tampered_sidecar_invalidates_cache(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    first = _download(tmp_path, monkeypatch)
    sidecar_path = tmp_path / f"{first.filename}.metadata.json"
    sidecar = json.loads(sidecar_path.read_text())
    sidecar["sha256"] = "0" * 64
    sidecar_path.write_text(json.dumps(sidecar), encoding="utf-8")
    monkeypatch.setattr(gpu, "open_safe_https", lambda *args, **kwargs: _Response(_zip_bytes()))
    assert not download_gpu_document(first.document, _config(), tmp_path).cache_hit


def test_archive_path_traversal_is_rejected(tmp_path: Path) -> None:
    path = tmp_path / "unsafe.zip"
    path.write_bytes(_zip_bytes({"../escape.txt": b"bad"}))
    with pytest.raises(GpuArchiveError, match="Unsafe"):
        validate_gpu_archive(path)


def test_archive_symlink_is_rejected(tmp_path: Path) -> None:
    path = tmp_path / "unsafe.zip"
    with zipfile.ZipFile(path, "w") as archive:
        entry = zipfile.ZipInfo("link")
        entry.create_system = 3
        entry.external_attr = (0o120777 << 16) | 0xA000
        archive.writestr(entry, "target")
    with pytest.raises(GpuArchiveError, match="Symbolic"):
        validate_gpu_archive(path)


@pytest.mark.parametrize(
    "members",
    [
        [("duplicate.txt", b"first"), ("duplicate.txt", b"second")],
        [("folder/file.txt", b"first"), (r"folder\file.txt", b"second")],
        [("folder/file.txt", b"first"), ("folder/./file.txt", b"second")],
        [("Folder/File.txt", b"first"), ("folder/file.txt", b"second")],
    ],
)
def test_duplicate_zip_extraction_targets_are_rejected(
    tmp_path: Path,
    members: list[tuple[str, bytes]],
) -> None:
    path = tmp_path / "collision.zip"
    path.write_bytes(_zip_member_bytes(members))

    with pytest.raises(GpuArchiveError, match="(?i)duplicate|collid"):
        validate_gpu_archive(path)


def test_zip_file_directory_target_collision_is_rejected(tmp_path: Path) -> None:
    path = tmp_path / "collision.zip"
    path.write_bytes(
        _zip_member_bytes(
            [("blocked", b"file"), ("blocked/child.txt", b"child")]
        )
    )

    with pytest.raises(GpuArchiveError, match="collision|target"):
        validate_gpu_archive(path)


def test_zip_cannot_claim_extraction_manifest_path(tmp_path: Path) -> None:
    path = tmp_path / "collision.zip"
    path.write_bytes(
        _zip_bytes({f"{gpu.EXTRACTION_MANIFEST_NAME}/child": b"forbidden"})
    )

    with pytest.raises(GpuArchiveError, match="manifest"):
        validate_gpu_archive(path)


def test_extraction_inventory_and_cache(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    first = _download(
        tmp_path / "cache",
        monkeypatch,
        _zip_bytes({"data/a.txt": b"x", "docs/reglement.pdf": b"pdf"}),
    )
    extracted = extract_gpu_document(first, tmp_path / "cache")
    assert [item.relative_path for item in extracted.files] == [
        "data/a.txt",
        "docs/reglement.pdf",
    ]
    assert {item.category for item in extracted.files} == {
        "METADATA",
        "WRITTEN_REGULATION",
    }
    assert extract_gpu_document(first, tmp_path / "cache").cache_hit
    manifest = json.loads(
        (
            extracted.extraction_root / gpu.EXTRACTION_MANIFEST_NAME
        ).read_text(encoding="utf-8")
    )
    assert manifest["schema_version"] == 2
    assert manifest["archive_sha256"] == first.sha256
    assert manifest["files"] == [
        {
            "relative_path": item.relative_path,
            "size_bytes": item.size_bytes,
            "sha256": item.sha256,
        }
        for item in extracted.files
    ]
    assert not list((tmp_path / "cache" / "x").glob("*.part"))


def test_stale_download_object_rejects_replaced_valid_archive(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    download = _download(
        tmp_path / "cache",
        monkeypatch,
        _zip_bytes({"data/value.txt": b"A"}),
    )
    replacement = _zip_bytes({"data/value.txt": b"B"})
    assert len(replacement) == download.file_size
    download.path.write_bytes(replacement)

    with pytest.raises(GpuArchiveError, match="checksum|SHA|stale|metadata"):
        extract_gpu_document(download, tmp_path / "cache")

    assert not (tmp_path / "cache" / "x" / download.sha256[:16]).exists()


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("sha256", "0" * 64),
        ("file_size", 1),
        ("filename", "other.zip"),
        ("archive_format", "7z"),
    ],
)
def test_extraction_rejects_archive_object_inconsistent_with_path(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    field: str,
    value: object,
) -> None:
    download = _download(tmp_path / "cache", monkeypatch)
    stale = replace(download, **{field: value})

    with pytest.raises(GpuArchiveError, match="archive|metadata|checksum|size"):
        extract_gpu_document(stale, tmp_path / "cache")


@pytest.mark.parametrize("mutation", ["content", "deleted", "added", "path"])
def test_tampered_extraction_is_rebuilt_from_verified_archive(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    mutation: str,
) -> None:
    download = _download(
        tmp_path / "cache",
        monkeypatch,
        _zip_bytes(
            {
                "data/value.txt": b"source",
                "docs/reglement.pdf": b"pdf",
            }
        ),
    )
    first = extract_gpu_document(download, tmp_path / "cache")
    original = first.extraction_root / "data" / "value.txt"
    if mutation == "content":
        original.write_bytes(b"forged")
    elif mutation == "deleted":
        original.unlink()
    elif mutation == "added":
        (first.extraction_root / "unexpected.txt").write_bytes(b"unexpected")
    else:
        original.rename(original.with_name("renamed.txt"))

    refreshed = extract_gpu_document(download, tmp_path / "cache")

    assert not refreshed.cache_hit
    assert (refreshed.extraction_root / "data" / "value.txt").read_bytes() == b"source"
    assert not (refreshed.extraction_root / "data" / "renamed.txt").exists()
    assert not (refreshed.extraction_root / "unexpected.txt").exists()


def _extraction_from_archive(path: Path, tmp_path: Path) -> GpuExtraction:
    document = gpu.GpuDocumentMetadata(
        provider="GPU",
        portal="GPU",
        commune_code="31395",
        partition="DU_31395",
        document_id="doc-1",
        document_family="DU",
        document_type="PLU",
        document_title=None,
        status="document.production",
        legal_status="APPROVED",
        effective_status="EN_VIGUEUR",
        version=None,
        archive_name=path.stem,
        publication_timestamp=None,
        update_timestamp=None,
        revision_date=None,
        producer=None,
        standard_model=None,
        projection="EPSG:2154",
        metadata_identifier=None,
        source_url="https://example.test/archive.zip",
        written_files=(),
    )
    download = GpuArchiveDownload(
        document=document,
        download_timestamp=datetime.now(UTC).isoformat(),
        filename=path.name,
        archive_format="zip",
        file_size=path.stat().st_size,
        sha256=gpu._sha256(path),
        path=path,
        cache_hit=False,
    )
    return extract_gpu_document(download, tmp_path / "cache")


def test_spatial_inventory_and_inspection_preserve_source_quality(tmp_path: Path) -> None:
    extraction = _extraction_from_archive(_planning_archive(tmp_path), tmp_path)
    references = discover_gpu_spatial_layers(extraction)
    assert [item.source_layer for item in references] == [
        "prescription_surf",
        "zone_urba",
    ]
    result = inspect_gpu_planning_document(extraction, _config())
    assert result.zoning.reference.source_layer == "zone_urba"
    assert result.zoning.summary.crs == "EPSG:2154"
    assert result.zoning.summary.feature_count == 3
    assert result.zoning.summary.null_geometry_count == 1
    assert result.zoning.summary.invalid_geometry_count == 1
    assert not result.zoning.data.geometry.iloc[1].is_valid
    assert result.related_layers[0].logical_name == "prescription_surface"
    assert extraction.standard_models == ("CNIG PLU v2017",)
    assert [item.relative_path for item in extraction.files] == sorted(
        item.relative_path for item in extraction.files
    )


def test_missing_zoning_layer_fails_clearly(tmp_path: Path) -> None:
    source = _planning_archive(tmp_path)
    extraction = _extraction_from_archive(source, tmp_path)
    payload = _config().model_dump(mode="json")
    payload["spatial_layers"]["zoning"]["match_tokens"] = ["missing"]
    with pytest.raises(GpuSpatialInspectionError, match="zoning"):
        inspect_gpu_planning_document(
            extraction, GpuSourceConfig.model_validate(payload)
        )


def test_ambiguous_zoning_layer_fails_clearly(tmp_path: Path) -> None:
    extraction = _extraction_from_archive(_planning_archive(tmp_path), tmp_path)
    payload = _config().model_dump(mode="json")
    payload["spatial_layers"]["zoning"]["match_tokens"] = [
        "zone_urba",
        "prescription_surf",
    ]
    with pytest.raises(GpuSpatialInspectionError, match="found 2"):
        inspect_gpu_planning_document(
            extraction, GpuSourceConfig.model_validate(payload)
        )


def test_cached_document_lineage_change_forces_refresh(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    first = _download(tmp_path, monkeypatch)
    changed = replace(
        first.document,
        document_id="doc-2",
        written_files=tuple(
            replace(
                item,
                source_url=(
                    item.source_url.replace("/doc-1/", "/doc-2/")
                    if item.source_url is not None
                    else None
                ),
            )
            for item in first.document.written_files
        ),
    )
    monkeypatch.setattr(gpu, "open_safe_https", lambda *args, **kwargs: _Response(_zip_bytes()))
    assert not download_gpu_document(changed, _config(), tmp_path).cache_hit
