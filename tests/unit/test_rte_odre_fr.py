import io
import json
from datetime import UTC, datetime, timedelta
from hashlib import sha256
from pathlib import Path
from unittest.mock import patch
from urllib.error import HTTPError

import pytest
import yaml
from pydantic import ValidationError

from landscout.sources import rte_odre_fr
from landscout.sources.rte_odre_fr import (
    RteOdreDownloadError,
    RteOdreExportSummary,
    RteOdreSourceConfig,
    build_rte_odre_export_url,
    build_rte_odre_metadata_url,
    download_rte_odre_dataset,
    fetch_rte_odre_dataset_metadata,
    load_rte_odre_source_config,
)

PROJECT_ROOT = Path(__file__).parents[2]
CONFIG_PATH = PROJECT_ROOT / "configs/sources/rte_odre_fr.yaml"
BASE_URL = "https://odre.opendatasoft.com/api/explore/v2.1"
DATASET_IDS = {
    "sites": "postes-electriques-rte",
    "overhead_lines": "lignes-aeriennes-rte-nv",
    "underground_lines": "lignes-souterraines-rte-nv",
}


def _config_data() -> dict:
    with CONFIG_PATH.open(encoding="utf-8") as stream:
        return yaml.safe_load(stream)


def _metadata_content(dataset_id: str, records_count: int | None = 2) -> bytes:
    payload = {
        "dataset_id": dataset_id,
        "metas": {
            "default": {
                "title": "Official RTE dataset",
                "publisher": "RTE",
                "modified": "2026-06-16T12:00:00+00:00",
                "data_processed": "2026-06-16T12:01:00+00:00",
                "metadata_processed": "2026-06-16T12:01:01+00:00",
                "license": "Licence Ouverte v2.0 (Etalab)",
                "records_count": records_count,
                "description": (
                    "RTE a fait évoluer l'accès aux données GPS pour des raisons "
                    "de sécurité publique."
                ),
            }
        },
    }
    return json.dumps(payload, ensure_ascii=False).encode("utf-8")


def _feature_collection(*, all_null_geometry: bool = False) -> bytes:
    geometry = None if all_null_geometry else {"type": "Point", "coordinates": [1, 2]}
    payload = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {"code": "A"},
                "geometry": geometry,
            },
            {
                "type": "Feature",
                "properties": {"code": "B"},
                "geometry": None,
            },
        ],
    }
    return json.dumps(payload).encode("utf-8")


def _response(content: bytes) -> io.BytesIO:
    return io.BytesIO(content)


def _metadata_path(cache_dir: Path, dataset_id: str) -> Path:
    return cache_dir / f"{dataset_id}.geojson.metadata.json"


def _expire_cache(metadata_path: Path) -> None:
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    metadata["download_timestamp"] = (
        datetime.now(UTC) - timedelta(hours=169)
    ).isoformat()
    metadata_path.write_text(json.dumps(metadata), encoding="utf-8")


@pytest.fixture
def source_config() -> RteOdreSourceConfig:
    return load_rte_odre_source_config(CONFIG_PATH)


def test_valid_source_config_loads(source_config: RteOdreSourceConfig) -> None:
    assert source_config.provider == "RTE"
    assert source_config.portal == "ODRE"
    assert source_config.datasets.sites.dataset_id == "postes-electriques-rte"
    assert source_config.cache.max_age_hours == 168


def test_missing_dataset_id_fails() -> None:
    config_data = _config_data()
    del config_data["datasets"]["sites"]["dataset_id"]

    with pytest.raises(ValidationError):
        RteOdreSourceConfig.model_validate(config_data)


def test_empty_base_url_fails() -> None:
    config_data = _config_data()
    config_data["api"]["base_url"] = ""

    with pytest.raises(ValidationError):
        RteOdreSourceConfig.model_validate(config_data)


def test_negative_cache_age_fails() -> None:
    config_data = _config_data()
    config_data["cache"]["max_age_hours"] = -1

    with pytest.raises(ValidationError):
        RteOdreSourceConfig.model_validate(config_data)


def test_unsupported_export_format_fails() -> None:
    config_data = _config_data()
    config_data["datasets"]["sites"]["preferred_format"] = "csv"

    with pytest.raises(ValidationError):
        RteOdreSourceConfig.model_validate(config_data)


@pytest.mark.parametrize(
    ("logical_name", "dataset_id"),
    list(DATASET_IDS.items()),
)
def test_build_export_url(
    source_config: RteOdreSourceConfig, logical_name: str, dataset_id: str
) -> None:
    url = build_rte_odre_export_url(source_config, logical_name)  # type: ignore[arg-type]

    assert url == f"{BASE_URL}/catalog/datasets/{dataset_id}/exports/geojson"


def test_build_metadata_url(source_config: RteOdreSourceConfig) -> None:
    assert build_rte_odre_metadata_url(source_config, "sites") == (
        f"{BASE_URL}/catalog/datasets/postes-electriques-rte"
    )


def test_export_url_uses_configured_dataset_id() -> None:
    config_data = _config_data()
    config_data["datasets"]["sites"]["dataset_id"] = "configured-sites"
    config = RteOdreSourceConfig.model_validate(config_data)

    assert build_rte_odre_export_url(config, "sites").endswith(
        "/catalog/datasets/configured-sites/exports/geojson"
    )


def test_metadata_is_captured_without_fabrication(
    source_config: RteOdreSourceConfig,
) -> None:
    content = _metadata_content(DATASET_IDS["sites"])
    with patch(
        "landscout.sources.rte_odre_fr.urlopen", return_value=_response(content)
    ):
        metadata = fetch_rte_odre_dataset_metadata(source_config, "sites")

    assert metadata.title == "Official RTE dataset"
    assert metadata.publisher == "RTE"
    assert metadata.modified == "2026-06-16T12:00:00+00:00"
    assert metadata.data_processed == "2026-06-16T12:01:00+00:00"
    assert metadata.metadata_processed == "2026-06-16T12:01:01+00:00"
    assert metadata.license == "Licence Ouverte v2.0 (Etalab)"
    assert metadata.records_count == 2
    assert metadata.geometry_precision_status == "GENERALIZED_OR_RESTRICTED"


def test_successful_download(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
    dataset_id = DATASET_IDS["sites"]
    export_content = _feature_collection()
    with patch(
        "landscout.sources.rte_odre_fr.urlopen",
        side_effect=[
            _response(_metadata_content(dataset_id)),
            _response(export_content),
        ],
    ):
        result = download_rte_odre_dataset("sites", source_config, tmp_path)

    assert result.logical_name == "sites"
    assert result.dataset_id == dataset_id
    assert result.provider == "RTE"
    assert result.portal == "ODRE"
    assert result.export_format == "geojson"
    assert result.path.read_bytes() == export_content
    assert result.file_size == len(export_content)
    assert result.sha256 == sha256(export_content).hexdigest()
    assert result.cache_hit is False
    assert result.dataset_metadata.title == "Official RTE dataset"
    assert result.dataset_metadata.records_count == result.export_summary.feature_count
    assert result.export_summary == RteOdreExportSummary(
        feature_count=2,
        null_geometry_count=1,
        non_null_geometry_count=1,
        geometry_types=("Point",),
    )


@pytest.mark.parametrize("records_count", [1, 3])
def test_metadata_export_record_count_mismatch_is_rejected(
    tmp_path: Path,
    source_config: RteOdreSourceConfig,
    records_count: int,
) -> None:
    dataset_id = DATASET_IDS["sites"]
    with (
        patch(
            "landscout.sources.rte_odre_fr.urlopen",
            side_effect=[
                _response(_metadata_content(dataset_id, records_count)),
                _response(_feature_collection()),
            ],
        ),
        pytest.raises(RteOdreDownloadError, match="records_count"),
    ):
        download_rte_odre_dataset("sites", source_config, tmp_path)

    assert not list(tmp_path.glob("*.geojson"))
    assert not list(tmp_path.glob("*.part"))
    assert not list(tmp_path.glob("*.bak"))


def test_unavailable_metadata_record_count_is_accepted(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
    dataset_id = DATASET_IDS["sites"]
    with patch(
        "landscout.sources.rte_odre_fr.urlopen",
        side_effect=[
            _response(_metadata_content(dataset_id, records_count=None)),
            _response(_feature_collection()),
        ],
    ):
        result = download_rte_odre_dataset("sites", source_config, tmp_path)

    assert result.dataset_metadata.records_count is None
    assert result.export_summary.feature_count == 2


def test_negative_source_record_count_is_rejected(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
    dataset_id = DATASET_IDS["sites"]
    with (
        patch(
            "landscout.sources.rte_odre_fr.urlopen",
            return_value=_response(_metadata_content(dataset_id, records_count=-1)),
        ),
        pytest.raises(RteOdreDownloadError, match="must not be negative"),
    ):
        download_rte_odre_dataset("sites", source_config, tmp_path)

    assert not list(tmp_path.glob("*.part"))
    assert not list(tmp_path.glob("*.bak"))


@pytest.mark.parametrize(
    ("feature_count", "null_geometry_count", "non_null_geometry_count"),
    [
        (-1, 0, 0),
        (1, -1, 2),
        (1, 0, -1),
        (2, 0, 1),
    ],
)
def test_export_summary_rejects_invalid_geometry_counts(
    feature_count: int,
    null_geometry_count: int,
    non_null_geometry_count: int,
) -> None:
    with pytest.raises(ValueError):
        RteOdreExportSummary(
            feature_count=feature_count,
            null_geometry_count=null_geometry_count,
            non_null_geometry_count=non_null_geometry_count,
            geometry_types=(),
        )


def test_fresh_cache_is_reused(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
    dataset_id = DATASET_IDS["sites"]
    with patch(
        "landscout.sources.rte_odre_fr.urlopen",
        side_effect=[
            _response(_metadata_content(dataset_id)),
            _response(_feature_collection()),
        ],
    ) as opener:
        first = download_rte_odre_dataset("sites", source_config, tmp_path)
        second = download_rte_odre_dataset("sites", source_config, tmp_path)

    assert opener.call_count == 2
    assert first.cache_hit is False
    assert second.cache_hit is True
    assert second.download_timestamp == first.download_timestamp
    assert second.sha256 == first.sha256


def test_expired_cache_is_refreshed(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
    dataset_id = DATASET_IDS["sites"]
    initial_content = _feature_collection()
    refreshed_payload = json.loads(initial_content)
    refreshed_payload["features"].append(
        {"type": "Feature", "properties": {"code": "C"}, "geometry": None}
    )
    refreshed_content = json.dumps(refreshed_payload).encode("utf-8")
    with patch(
        "landscout.sources.rte_odre_fr.urlopen",
        side_effect=[
            _response(_metadata_content(dataset_id)),
            _response(initial_content),
        ],
    ):
        first = download_rte_odre_dataset("sites", source_config, tmp_path)
    _expire_cache(_metadata_path(tmp_path, dataset_id))

    with patch(
        "landscout.sources.rte_odre_fr.urlopen",
        side_effect=[
            _response(_metadata_content(dataset_id, records_count=3)),
            _response(refreshed_content),
        ],
    ) as opener:
        refreshed = download_rte_odre_dataset("sites", source_config, tmp_path)

    assert opener.call_count == 2
    assert refreshed.cache_hit is False
    assert refreshed.path.read_bytes() == refreshed_content
    assert refreshed.sha256 != first.sha256
    assert refreshed.export_summary.feature_count == 3
    assert not list(tmp_path.glob("*.bak"))
    assert not list(tmp_path.glob("*.part"))


def test_http_failure_raises_and_cleans_temporary_files(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
    dataset_id = DATASET_IDS["sites"]
    source_url = build_rte_odre_export_url(source_config, "sites")
    error = HTTPError(source_url, 503, "Unavailable", hdrs=None, fp=None)
    with (
        patch(
            "landscout.sources.rte_odre_fr.urlopen",
            side_effect=[_response(_metadata_content(dataset_id)), error],
        ),
        pytest.raises(RteOdreDownloadError),
    ):
        download_rte_odre_dataset("sites", source_config, tmp_path)

    assert not list(tmp_path.glob("*.part"))
    assert not list(tmp_path.glob("*.geojson"))


def test_failed_refresh_preserves_previous_valid_cache(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
    dataset_id = DATASET_IDS["sites"]
    with patch(
        "landscout.sources.rte_odre_fr.urlopen",
        side_effect=[
            _response(_metadata_content(dataset_id)),
            _response(_feature_collection()),
        ],
    ):
        first = download_rte_odre_dataset("sites", source_config, tmp_path)
    original_archive = first.path.read_bytes()
    metadata_path = _metadata_path(tmp_path, dataset_id)
    original_metadata = metadata_path.read_bytes()
    _expire_cache(metadata_path)
    expired_metadata = metadata_path.read_bytes()
    metadata_url = build_rte_odre_metadata_url(source_config, "sites")
    error = HTTPError(metadata_url, 503, "Unavailable", hdrs=None, fp=None)

    with (
        patch("landscout.sources.rte_odre_fr.urlopen", side_effect=error),
        pytest.raises(RteOdreDownloadError),
    ):
        download_rte_odre_dataset("sites", source_config, tmp_path)

    assert first.path.read_bytes() == original_archive
    assert metadata_path.read_bytes() == expired_metadata
    assert metadata_path.read_bytes() != original_metadata
    assert not list(tmp_path.glob("*.part"))


def test_corrupted_refresh_preserves_previous_valid_cache(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
    dataset_id = DATASET_IDS["sites"]
    with patch(
        "landscout.sources.rte_odre_fr.urlopen",
        side_effect=[
            _response(_metadata_content(dataset_id)),
            _response(_feature_collection()),
        ],
    ):
        first = download_rte_odre_dataset("sites", source_config, tmp_path)
    original_archive = first.path.read_bytes()
    metadata_path = _metadata_path(tmp_path, dataset_id)
    _expire_cache(metadata_path)
    expired_metadata = metadata_path.read_bytes()

    with (
        patch(
            "landscout.sources.rte_odre_fr.urlopen",
            side_effect=[
                _response(_metadata_content(dataset_id)),
                _response(b"{corrupted"),
            ],
        ),
        pytest.raises(RteOdreDownloadError),
    ):
        download_rte_odre_dataset("sites", source_config, tmp_path)

    assert first.path.read_bytes() == original_archive
    assert metadata_path.read_bytes() == expired_metadata
    assert not list(tmp_path.glob("*.part"))


def test_metadata_publication_failure_restores_previous_pair(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
    dataset_id = DATASET_IDS["sites"]
    with patch(
        "landscout.sources.rte_odre_fr.urlopen",
        side_effect=[
            _response(_metadata_content(dataset_id)),
            _response(_feature_collection()),
        ],
    ):
        first = download_rte_odre_dataset("sites", source_config, tmp_path)
    metadata_path = _metadata_path(tmp_path, dataset_id)
    _expire_cache(metadata_path)
    old_archive = first.path.read_bytes()
    old_metadata = metadata_path.read_bytes()
    temporary_metadata = metadata_path.with_suffix(f"{metadata_path.suffix}.part")
    original_replace = rte_odre_fr._replace_file
    failure_injected = False

    def fail_metadata_publication(source: Path, target: Path) -> None:
        nonlocal failure_injected
        if source == temporary_metadata and target == metadata_path:
            failure_injected = True
            raise PermissionError("simulated persistent metadata file lock")
        original_replace(source, target)

    with (
        patch(
            "landscout.sources.rte_odre_fr.urlopen",
            side_effect=[
                _response(_metadata_content(dataset_id)),
                _response(_feature_collection(all_null_geometry=True)),
            ],
        ),
        patch.object(
            rte_odre_fr,
            "_replace_file",
            side_effect=fail_metadata_publication,
        ),
        pytest.raises(RteOdreDownloadError),
    ):
        download_rte_odre_dataset("sites", source_config, tmp_path)

    assert failure_injected
    assert first.path.read_bytes() == old_archive
    assert metadata_path.read_bytes() == old_metadata
    assert not list(tmp_path.glob("*.part"))
    assert not list(tmp_path.glob("*.bak"))


@pytest.mark.parametrize(
    "invalid_content",
    [
        b"{not-json",
        json.dumps({"type": "Point", "coordinates": [1, 2]}).encode(),
        json.dumps({"type": "FeatureCollection"}).encode(),
    ],
)
def test_invalid_geojson_download_is_rejected(
    tmp_path: Path,
    source_config: RteOdreSourceConfig,
    invalid_content: bytes,
) -> None:
    dataset_id = DATASET_IDS["sites"]
    with (
        patch(
            "landscout.sources.rte_odre_fr.urlopen",
            side_effect=[
                _response(_metadata_content(dataset_id)),
                _response(invalid_content),
            ],
        ),
        pytest.raises(RteOdreDownloadError),
    ):
        download_rte_odre_dataset("sites", source_config, tmp_path)

    assert not list(tmp_path.glob("*.part"))
    assert not list(tmp_path.glob("*.geojson"))


@pytest.mark.parametrize(
    "feature",
    [
        123,
        "feature",
        {"geometry": None},
        {"type": "NotFeature", "geometry": None},
        {"type": "Feature", "geometry": {}},
        {"type": "Feature", "geometry": {"type": ""}},
        {"type": "Feature", "geometry": {"type": "SOMETHING_RANDOM"}},
        {"type": "Feature", "geometry": {"type": "Point"}},
        {"type": "Feature", "geometry": {"type": "GeometryCollection"}},
        {"type": "Feature", "geometry": 123},
    ],
)
def test_malformed_geojson_feature_or_geometry_is_rejected(
    tmp_path: Path,
    feature: object,
) -> None:
    path = tmp_path / "malformed.geojson"
    path.write_text(
        json.dumps({"type": "FeatureCollection", "features": [feature]}),
        encoding="utf-8",
    )

    with pytest.raises(RteOdreDownloadError):
        rte_odre_fr._validate_geojson(path)


def test_standard_geojson_geometry_types_are_summarized(tmp_path: Path) -> None:
    coordinate_types = {
        "Point": [1, 2],
        "MultiPoint": [[1, 2]],
        "LineString": [[1, 2], [2, 3]],
        "MultiLineString": [[[1, 2], [2, 3]]],
        "Polygon": [[[1, 2], [2, 3], [1, 2]]],
        "MultiPolygon": [[[[1, 2], [2, 3], [1, 2]]]],
    }
    features = [
        {
            "type": "Feature",
            "geometry": {"type": geometry_type, "coordinates": coordinates},
        }
        for geometry_type, coordinates in coordinate_types.items()
    ]
    features.extend(
        [
            {
                "type": "Feature",
                "geometry": {"type": "GeometryCollection", "geometries": []},
            },
            {"type": "Feature", "geometry": None},
        ]
    )
    path = tmp_path / "valid.geojson"
    path.write_text(
        json.dumps({"type": "FeatureCollection", "features": features}),
        encoding="utf-8",
    )

    summary = rte_odre_fr._validate_geojson(path)

    assert summary.feature_count == 8
    assert summary.null_geometry_count == 1
    assert summary.non_null_geometry_count == 7
    assert summary.geometry_types == tuple(sorted((*coordinate_types, "GeometryCollection")))


def test_null_feature_geometries_are_accepted(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
    dataset_id = DATASET_IDS["sites"]
    export_content = _feature_collection(all_null_geometry=True)
    with patch(
        "landscout.sources.rte_odre_fr.urlopen",
        side_effect=[
            _response(_metadata_content(dataset_id)),
            _response(export_content),
        ],
    ):
        result = download_rte_odre_dataset("sites", source_config, tmp_path)

    assert result.path.is_file()
    assert result.dataset_metadata.geometry_precision_status == "MISSING"
    assert result.export_summary == RteOdreExportSummary(
        feature_count=2,
        null_geometry_count=2,
        non_null_geometry_count=0,
        geometry_types=(),
    )


def test_lineage_sidecar_records_integrity(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
    dataset_id = DATASET_IDS["sites"]
    export_content = _feature_collection()
    with patch(
        "landscout.sources.rte_odre_fr.urlopen",
        side_effect=[
            _response(_metadata_content(dataset_id)),
            _response(export_content),
        ],
    ):
        result = download_rte_odre_dataset("sites", source_config, tmp_path)

    metadata_path = _metadata_path(tmp_path, dataset_id)
    lineage = json.loads(metadata_path.read_text(encoding="utf-8"))
    assert lineage["source_url"] == result.source_url
    assert lineage["file_size"] == len(export_content)
    assert lineage["sha256"] == sha256(export_content).hexdigest()
    assert lineage["dataset_metadata"]["publisher"] == "RTE"
    assert lineage["export_summary"] == {
        "feature_count": 2,
        "geometry_types": ["Point"],
        "non_null_geometry_count": 1,
        "null_geometry_count": 1,
    }
    assert (
        lineage["export_summary"]["null_geometry_count"]
        + lineage["export_summary"]["non_null_geometry_count"]
        == lineage["export_summary"]["feature_count"]
    )
    assert "path" not in lineage
    assert "cache_hit" not in lineage


@pytest.mark.parametrize("cached_records_count", [-1, 1])
def test_invalid_cached_record_count_invalidates_cache(
    tmp_path: Path,
    source_config: RteOdreSourceConfig,
    cached_records_count: int,
) -> None:
    dataset_id = DATASET_IDS["sites"]
    valid_content = _feature_collection()
    with patch(
        "landscout.sources.rte_odre_fr.urlopen",
        side_effect=[
            _response(_metadata_content(dataset_id)),
            _response(valid_content),
        ],
    ):
        first = download_rte_odre_dataset("sites", source_config, tmp_path)
    metadata_path = _metadata_path(tmp_path, dataset_id)
    lineage = json.loads(metadata_path.read_text(encoding="utf-8"))
    lineage["dataset_metadata"]["records_count"] = cached_records_count
    metadata_path.write_text(json.dumps(lineage), encoding="utf-8")

    with patch(
        "landscout.sources.rte_odre_fr.urlopen",
        side_effect=[
            _response(_metadata_content(dataset_id)),
            _response(valid_content),
        ],
    ) as opener:
        refreshed = download_rte_odre_dataset("sites", source_config, tmp_path)

    assert opener.call_count == 2
    assert refreshed.cache_hit is False
    assert refreshed.path.read_bytes() == first.path.read_bytes()
    assert refreshed.dataset_metadata.records_count == 2


def test_cached_export_summary_mismatch_invalidates_cache(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
    dataset_id = DATASET_IDS["sites"]
    valid_content = _feature_collection()
    with patch(
        "landscout.sources.rte_odre_fr.urlopen",
        side_effect=[
            _response(_metadata_content(dataset_id)),
            _response(valid_content),
        ],
    ):
        download_rte_odre_dataset("sites", source_config, tmp_path)
    metadata_path = _metadata_path(tmp_path, dataset_id)
    lineage = json.loads(metadata_path.read_text(encoding="utf-8"))
    lineage["export_summary"]["null_geometry_count"] = 2
    lineage["export_summary"]["non_null_geometry_count"] = 0
    lineage["export_summary"]["geometry_types"] = []
    metadata_path.write_text(json.dumps(lineage), encoding="utf-8")

    with patch(
        "landscout.sources.rte_odre_fr.urlopen",
        side_effect=[
            _response(_metadata_content(dataset_id)),
            _response(valid_content),
        ],
    ) as opener:
        refreshed = download_rte_odre_dataset("sites", source_config, tmp_path)

    assert opener.call_count == 2
    assert refreshed.cache_hit is False
    assert refreshed.export_summary.geometry_types == ("Point",)


def test_corrupted_cached_export_triggers_refresh(
    tmp_path: Path, source_config: RteOdreSourceConfig
) -> None:
    dataset_id = DATASET_IDS["sites"]
    valid_content = _feature_collection()
    with patch(
        "landscout.sources.rte_odre_fr.urlopen",
        side_effect=[
            _response(_metadata_content(dataset_id)),
            _response(valid_content),
        ],
    ):
        first = download_rte_odre_dataset("sites", source_config, tmp_path)
    first.path.write_bytes(b"corrupted")

    with patch(
        "landscout.sources.rte_odre_fr.urlopen",
        side_effect=[
            _response(_metadata_content(dataset_id)),
            _response(valid_content),
        ],
    ) as opener:
        refreshed = download_rte_odre_dataset("sites", source_config, tmp_path)

    assert opener.call_count == 2
    assert refreshed.cache_hit is False
    assert refreshed.path.read_bytes() == valid_content
