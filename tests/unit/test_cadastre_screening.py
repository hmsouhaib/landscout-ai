"""Physical synthetic gzip integration; no normalization/revalidation stub."""

import csv
import gzip
import io
import json
import subprocess
from datetime import UTC, datetime
from hashlib import sha256
from pathlib import Path

import geopandas as gpd
import pytest
import yaml
from shapely.geometry import MultiPolygon, Polygon, box, mapping, shape

from landscout.config import load_scan_config
from landscout.sources import cadastre_fr
from landscout.sources.cadastre_fr import (
    build_cadastre_parcelles_url,
    download_cadastre_parcelles,
)
from landscout.sources.cadastre_loader_fr import load_cadastre_parcels
from landscout.stages.enrich_shape import enrich_parcel_shapes
from landscout.stages.filter_parcels import (
    filter_parcels_by_area,
    filter_parcels_by_shape,
)
from landscout.stages.normalize_cadastre import normalize_cadastre_parcels
from landscout.workflows import CadastreScreeningRunError, run_cadastre_screening
from landscout.workflows import cadastre_screening as workflow

PROJECT = Path(__file__).resolve().parents[2]


def write_project(root: Path, *, empty_source: bool = False) -> tuple[Path, Path, Path]:
    scan = root / "configs/scans/bess_muret.yaml"
    profile = root / "configs/profiles/bess_default_fr.yaml"
    scan.parent.mkdir(parents=True)
    profile.parent.mkdir(parents=True)
    scan.write_bytes((PROJECT / "configs/scans/bess_muret.yaml").read_bytes())
    profile.write_bytes(
        (PROJECT / "configs/profiles/bess_default_fr.yaml").read_bytes()
    )
    xy = gpd.GeoSeries(
        [
            box(600000, 6200000, 600060, 6200060),
            box(601000, 6200000, 601020, 6200020),
            box(602000, 6200000, 602200, 6200200),
            box(603000, 6200000, 603300, 6200010),
            box(604000, 6200000, 604300, 6200020),
            None,
            Polygon(
                [
                    (605000, 6200000),
                    (605060, 6200060),
                    (605060, 6200000),
                    (605000, 6200060),
                ]
            ),
            MultiPolygon(
                [
                    box(606000, 6200000, 606040, 6200040),
                    box(606060, 6200000, 606100, 6200040),
                ]
            ),
        ],
        crs=2154,
    ).to_crs(4326)
    features = [
        {
            "type": "Feature",
            "properties": {
                "id": f"31395000AA{i:04d}",
                "commune": "31395",
                "prefixe": "000",
                "section": "AA",
                "numero": str(i),
                "private_source_attribute": "not exported",
            },
            "geometry": mapping(geometry) if geometry is not None else None,
        }
        for i, geometry in enumerate(xy, 1)
    ]
    raw = gzip.compress(
        json.dumps(
            {
                "type": "FeatureCollection",
                "features": [] if empty_source else list(reversed(features)),
            },
            allow_nan=False,
        ).encode(),
        mtime=0,
    )
    cache = root / "data/cache/cadastre"
    cache.mkdir(parents=True)
    archive = cache / "cadastre-31395-parcelles.json.gz"
    archive.write_bytes(raw)
    metadata = {
        "schema_version": 1,
        "commune_code": "31395",
        "source_url": build_cadastre_parcelles_url("31395"),
        "download_timestamp": datetime.now(UTC).isoformat(),
        "filename": archive.name,
        "file_size": len(raw),
        "sha256": sha256(raw).hexdigest(),
    }
    (cache / f"{archive.name}.metadata.json").write_text(
        json.dumps(metadata), encoding="utf-8"
    )
    return scan, profile, cache


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


@pytest.fixture(autouse=True)
def no_transport(monkeypatch: pytest.MonkeyPatch) -> None:
    def fail(*args, **kwargs):
        raise AssertionError("Synthetic integration must never use the network")

    monkeypatch.setattr(cadastre_fr, "open_safe_https", fail)


def test_physical_end_to_end_partition_metrics_geometry_and_digests(
    tmp_path: Path,
) -> None:
    scan, profile_path, cache = write_project(tmp_path)
    inputs = {p: p.read_bytes() for p in (scan, profile_path, *cache.iterdir())}
    result = run_cadastre_screening(
        scan, cache_dir=Path("data/cache/cadastre"), output_dir=Path("outputs/run-one")
    )
    assert result.output_dir == tmp_path / "outputs/run-one"
    assert (
        result.normalized_count,
        result.area_rejected_count,
        result.shape_rejected_count,
        result.retained_count,
    ) == (8, 4, 2, 2)
    assert {p.name for p in result.output_dir.iterdir()} == {
        "candidates.csv",
        "rejections.csv",
        "candidates.geojson",
        "run.json",
    }
    kept, rejected = read_csv(result.candidates_csv), read_csv(result.rejections_csv)
    assert tuple(kept[0]) == workflow.EXPORT_COLUMNS
    assert [x["parcel_id"] for x in kept] == ["31395000AA0001", "31395000AA0008"]
    assert [x["parcel_id"] for x in rejected] == sorted(
        x["parcel_id"] for x in rejected
    )
    expected_reasons = {
        "0002": ("AREA", "AREA_BELOW_MIN"),
        "0003": ("AREA", "AREA_ABOVE_MAX"),
        "0004": ("SHAPE", "WIDTH_BELOW_MIN"),
        "0005": ("SHAPE", "RATIO_ABOVE_MAX"),
        "0006": ("AREA", "INVALID_GEOMETRY"),
        "0007": ("AREA", "INVALID_GEOMETRY"),
    }
    for row in rejected:
        assert (row["screening_stage"], row["rejection_reason"]) == expected_reasons[
            row["parcel_id"][-4:]
        ]
        if row["screening_stage"] == "AREA":
            assert all(
                row[key] == "" for key in ("shape_status", *workflow.METRIC_COLUMNS[1:])
            )
    assert float(kept[0]["area_m2"]) == pytest.approx(3600, abs=1e-4)
    assert float(kept[0]["width_m"]) == pytest.approx(60, abs=1e-4)
    assert all(x["screening_status"] == "RETAINED_BY_EXECUTED_FILTERS" for x in kept)

    loaded = load_scan_config(scan)
    source = load_cadastre_parcels(
        download_cadastre_parcelles("31395", cache, allow_download=False)
    )
    normalized = normalize_cadastre_parcels(source)
    area, area_no = filter_parcels_by_area(normalized, loaded.profile.parcel)
    enriched = enrich_parcel_shapes(area)
    retained, shape_no = filter_parcels_by_shape(
        enriched, loaded.profile.shape_screening
    )
    for row in kept:
        actual = retained.set_index("parcel_id").loc[row["parcel_id"]]
        for metric in workflow.METRIC_COLUMNS:
            assert float(row[metric]) == float(actual[metric])
    features = json.loads(result.candidates_geojson.read_bytes())["features"]
    assert [x["properties"]["parcel_id"] for x in features] == [
        x["parcel_id"] for x in kept
    ]
    for feature in features:
        actual = retained.set_index("parcel_id").geometry.loc[feature["id"]]
        assert shape(feature["geometry"]).wkb == actual.wkb
        assert "private_source_attribute" not in feature["properties"]
    assert len(normalized) == len(area_no) + len(shape_no) + len(retained)
    manifest = json.loads(
        result.manifest_path.read_text(encoding="utf-8"),
        parse_constant=lambda x: pytest.fail(f"nonfinite JSON: {x}"),
    )
    assert (
        manifest["status"] == "COMPLETE"
        and manifest["scope"] == "CADASTRE_AREA_SHAPE_ONLY"
    )
    assert manifest["schema_version"] == 1 and manifest["commune_code"] == "31395"
    assert manifest["source"]["cache_hit"] is True
    assert manifest["filters"]["shape"] == loaded.profile.shape_screening.model_dump(
        mode="json"
    )
    assert manifest["filters"]["area"] == loaded.profile.parcel.model_dump(mode="json")
    assert all(value == "NOT_RUN" for value in manifest["not_run"].values())
    assert manifest["counts"]["rejection_reasons"] == {
        "AREA": {"AREA_ABOVE_MAX": 1, "AREA_BELOW_MIN": 1, "INVALID_GEOMETRY": 2},
        "SHAPE": {"RATIO_ABOVE_MAX": 1, "WIDTH_BELOW_MIN": 1},
    }
    for binding in manifest["data_files"]:
        content = (result.output_dir / binding["path"]).read_bytes()
        assert (
            len(content) == binding["size_bytes"]
            and sha256(content).hexdigest() == binding["sha256"]
        )
    for binding in manifest["configuration"].values():
        assert (
            sha256(Path(binding["path"]).read_bytes()).hexdigest() == binding["sha256"]
        )
    for stamp in ("started_at_utc", "completed_at_utc"):
        assert datetime.fromisoformat(manifest[stamp]).utcoffset().total_seconds() == 0
    assert all(path.read_bytes() == content for path, content in inputs.items())
    repeat = run_cadastre_screening(scan, output_dir=Path("outputs/run-two"))
    assert all(
        (repeat.output_dir / name).read_bytes()
        == (result.output_dir / name).read_bytes()
        for name in ("candidates.csv", "rejections.csv", "candidates.geojson")
    )


def test_zero_candidates_is_success_with_stable_empty_exports(tmp_path: Path) -> None:
    scan, profile, _ = write_project(tmp_path)
    payload = yaml.safe_load(profile.read_bytes())
    payload["parcel"] = {"min_area_m2": 80000, "max_area_m2": 90000}
    profile.write_text(yaml.safe_dump(payload), encoding="utf-8")
    result = run_cadastre_screening(scan)
    assert result.retained_count == 0 and result.area_rejected_count == 8
    assert result.candidates_csv.read_text(encoding="utf-8").strip().split(",") == list(
        workflow.EXPORT_COLUMNS
    )
    assert json.loads(result.candidates_geojson.read_bytes()) == {
        "type": "FeatureCollection",
        "features": [],
    }
    assert len(read_csv(result.rejections_csv)) == 8


def test_disabled_shape_uses_existing_no_exclusion_behavior(tmp_path: Path) -> None:
    scan, profile, _ = write_project(tmp_path)
    payload = yaml.safe_load(profile.read_bytes())
    payload["shape_screening"]["enabled"] = False
    profile.write_text(yaml.safe_dump(payload), encoding="utf-8")
    result = run_cadastre_screening(scan)
    assert result.retained_count == 4 and result.shape_rejected_count == 0
    assert {x["screening_stage"] for x in read_csv(result.candidates_csv)} == {"AREA"}
    assert (
        json.loads(result.manifest_path.read_bytes())["filters"]["shape"]["enabled"]
        is False
    )


@pytest.mark.parametrize(
    "change", ["country", "technology", "communes", "invalid_profile"]
)
def test_invalid_or_unsupported_configuration_precedes_acquisition(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    change: str,
) -> None:
    scan, profile, _ = write_project(tmp_path)
    payload = yaml.safe_load(scan.read_bytes())
    profile_data = yaml.safe_load(profile.read_bytes())
    if change in ("country", "technology"):
        value = "BE" if change == "country" else "SOLAR"
        payload["scan"][change] = profile_data[change] = value
    elif change == "communes":
        payload["aoi"]["commune_codes"].append("75056")
    else:
        profile_data["parcel"]["min_area_m2"] = -1
    scan.write_text(yaml.safe_dump(payload), encoding="utf-8")
    profile.write_text(yaml.safe_dump(profile_data), encoding="utf-8")

    def fail(*args, **kwargs):
        raise AssertionError("acquisition was too early")

    monkeypatch.setattr(workflow, "download_cadastre_parcelles", fail)
    with pytest.raises(CadastreScreeningRunError):
        run_cadastre_screening(scan, output_dir=Path("outputs/fail"))
    assert not (tmp_path / "outputs").exists()


def test_empty_physical_source_is_a_read_error(tmp_path: Path) -> None:
    scan, _, _ = write_project(tmp_path, empty_source=True)
    with pytest.raises(CadastreScreeningRunError, match="empty"):
        run_cadastre_screening(scan, output_dir=Path("outputs/fail"))
    assert not (tmp_path / "outputs").exists()


@pytest.mark.parametrize("change", ["profile", "scan", "source"])
def test_persistent_mutation_during_export_prevents_completion(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    change: str,
) -> None:
    scan, profile, cache = write_project(tmp_path)
    original = workflow._write_geojson
    target = {
        "profile": profile,
        "scan": scan,
        "source": cache / "cadastre-31395-parcelles.json.gz",
    }[change]

    def mutate(*args, **kwargs):
        original(*args, **kwargs)
        target.write_bytes(target.read_bytes() + b"\n#persistent mutation")

    monkeypatch.setattr(workflow, "_write_geojson", mutate)
    output = tmp_path / "outputs/fail"
    with pytest.raises(CadastreScreeningRunError, match="changed|differs") as error:
        run_cadastre_screening(scan, output_dir=output)
    assert str(output) in str(error.value) and "incomplete" in str(error.value)
    assert not (output / "run.json").exists()
    assert (output / "candidates.csv").exists()


def test_config_mutation_around_load_is_rejected_before_acquisition(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    scan, profile, _ = write_project(tmp_path)
    original = workflow.load_scan_config

    def mutate(path):
        value = original(path)
        profile.write_bytes(profile.read_bytes() + b"\n#changed during load")
        return value

    monkeypatch.setattr(workflow, "load_scan_config", mutate)
    with pytest.raises(CadastreScreeningRunError, match="Configuration changed"):
        run_cadastre_screening(scan)
    assert not (tmp_path / "outputs").exists()


@pytest.mark.parametrize(
    "failed_file",
    ["candidates.csv", "rejections.csv", "candidates.geojson", "run.json.part"],
)
def test_write_failure_preserves_only_incomplete_new_output(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    failed_file: str,
) -> None:
    scan, _, _ = write_project(tmp_path)
    original = Path.open

    def fail(path, *args, **kwargs):
        if path.name == failed_file and args and "x" in args[0]:
            raise OSError("injected write failure")
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", fail)
    output = tmp_path / "outputs/fail"
    with pytest.raises(CadastreScreeningRunError, match="incomplete output"):
        run_cadastre_screening(scan, output_dir=output)
    assert output.is_dir() and not (output / "run.json").exists()


@pytest.mark.parametrize(
    "kind",
    ["existing", "symlink", "junction", "within_cache", "contains_cache", "tracked"],
)
def test_output_collision_is_rejected_before_source_access(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    kind: str,
) -> None:
    scan, _, cache = write_project(tmp_path)
    output = tmp_path / "outputs/run"
    if kind == "existing":
        output.mkdir(parents=True)
        (output / "sentinel").write_bytes(b"old output")
    elif kind in ("symlink", "junction"):
        method = "is_symlink" if kind == "symlink" else "is_junction"
        original = getattr(Path, method)
        monkeypatch.setattr(Path, method, lambda path: path == output or original(path))
    elif kind == "within_cache":
        output = cache / "run"
    elif kind == "contains_cache":
        output = tmp_path / "data"
    else:
        (tmp_path / ".git").mkdir()
        monkeypatch.setattr(
            workflow.subprocess,
            "run",
            lambda *a, **k: subprocess.CompletedProcess(
                a, 0, b"outputs/run/missing-tracked-file\0", b""
            ),
        )

    def fail(*args, **kwargs):
        raise AssertionError("Source access must follow output preflight")

    monkeypatch.setattr(workflow, "download_cadastre_parcelles", fail)
    with pytest.raises(CadastreScreeningRunError):
        run_cadastre_screening(scan, output_dir=output)
    if kind == "existing":
        assert (output / "sentinel").read_bytes() == b"old output"
    else:
        assert not (output / "run.json").exists()


def test_explicit_allow_download_uses_only_adapter_mock_transport(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    scan, _, cache = write_project(tmp_path)
    raw = (cache / "cadastre-31395-parcelles.json.gz").read_bytes()
    # A separate empty cache exercises the adapter's real download/publication path.
    urls = []

    def transport(url, **kwargs):
        urls.append(url)
        return io.BytesIO(raw)

    monkeypatch.setattr(cadastre_fr, "open_safe_https", transport)
    result = run_cadastre_screening(
        scan, cache_dir=Path("fresh-cache"), allow_download=True
    )
    assert urls == [build_cadastre_parcelles_url("31395")]
    assert json.loads(result.manifest_path.read_bytes())["source"]["cache_hit"] is False


def test_partition_guard_rejects_missing_parcel(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    scan, _, _ = write_project(tmp_path)
    original = workflow.filter_parcels_by_shape

    def lose_row(*args, **kwargs):
        kept, rejected = original(*args, **kwargs)
        return kept.iloc[1:], rejected

    monkeypatch.setattr(workflow, "filter_parcels_by_shape", lose_row)
    with pytest.raises(CadastreScreeningRunError, match="partition"):
        run_cadastre_screening(scan)
    assert not (tmp_path / "outputs").exists()
