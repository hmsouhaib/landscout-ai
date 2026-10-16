"""Full physical synthetic IGN/cadastre integration, no private-stage bypass."""

import io
import json
from dataclasses import replace
from pathlib import Path
from unittest.mock import patch

import geopandas as gpd
import pandas as pd
import py7zr
import pyogrio
import pytest
import yaml
from geopandas.testing import assert_geodataframe_equal
from shapely.affinity import translate
from shapely.geometry import LineString, box, shape
from test_cadastre_screening import PROJECT, read_csv, write_project

from landscout.config import load_scan_config
from landscout.sources import cadastre_fr
from landscout.sources import ign_bdtopo_fr as ign
from landscout.sources.cadastre_loader_fr import load_cadastre_parcels
from landscout.stages.enrich_shape import enrich_parcel_shapes
from landscout.stages.filter_parcels import (
    filter_parcels_by_area,
    filter_parcels_by_shape,
)
from landscout.stages.normalize_cadastre import normalize_cadastre_parcels
from landscout.workflows import CadastreScreeningRunError, run_cadastre_screening
from landscout.workflows import cadastre_screening as workflow
from landscout.workflows import grid_screening as grid
from landscout.workflows import ign_screening as ign_workflow


@pytest.fixture(autouse=True)
def forbid_transport(monkeypatch):
    def fail(*args, **kwargs):
        raise AssertionError("Grid run must use verified local caches only")

    monkeypatch.setattr(ign, "open_safe_https", fail)
    monkeypatch.setattr(cadastre_fr, "open_safe_https", fail)


def write_grid_project(root: Path, variant="normal", *, road_frame=None):
    scan, _, cache = write_project(root)
    raw_path = root / "fixture/grid.gpkg"
    raw_path.parent.mkdir()
    line_geometry = [
        LineString([(600070, 6199900), (600070, 6200200)]),
        LineString([(599990, 6199900), (599990, 6200200)]),
        LineString([(606020, 6199900), (606020, 6200200)]),
        LineString([(606050, 6199900), (606050, 6200200)]),
    ]
    voltage = ["63 kV", "132,5 kV", "<45 kV", "Inconnu"]
    if variant == "no_exact":
        voltage = ["Inconnu", "<45 kV", "<45 kV", "Inconnu"]
    lines = gpd.GeoDataFrame(
        {
            "cleabs": ["A", "B", "C_BELOW", "D_UNKNOWN"],
            "voltage": voltage,
            "gestionnaire": ["Manager"] * 4,
            "siren_gestionnaire": ["123456789"] * 4,
            "etat_de_l_objet": ["En service"] * 4,
            "sources": ["synthetic"] * 4,
            "identifiants_sources": ["fixture"] * 4,
            "date_creation": ["2026-01-01"] * 4,
            "date_modification": ["2026-01-02"] * 4,
            "date_de_confirmation": ["2026-01-03"] * 4,
            "methode_d_acquisition_planimetrique": ["synthetic"] * 4,
            "precision_planimetrique": [1.0] * 4,
        },
        geometry=[None] * 4 if variant == "no_lines" else line_geometry,
        crs=2154,
    )
    pyogrio.write_dataframe(
        lines,
        raw_path,
        layer="LIGNE_ELECTRIQUE",
        driver="GPKG",
        geometry_type="LineString",
    )
    posts = gpd.GeoDataFrame(
        {
            "cleabs": ["P1", "P2"],
            "toponyme": ["Inside", "East"],
            "statut_du_toponyme": ["Validé"] * 2,
            "importance": ["1", "2"],
            "etat_de_l_objet": ["En service"] * 2,
            "sources": ["synthetic"] * 2,
            "identifiants_sources": ["fixture"] * 2,
            "date_creation": ["2026-01-01"] * 2,
            "date_modification": ["2026-01-02"] * 2,
            "date_de_confirmation": ["2026-01-03"] * 2,
            "methode_d_acquisition_planimetrique": ["synthetic"] * 2,
            "precision_planimetrique": [1.0] * 2,
        },
        geometry=[None, None]
        if variant == "no_posts"
        else [
            box(600010, 6200010, 600020, 6200020),
            box(606110, 6200010, 606120, 6200020),
        ],
        crs=2154,
    )
    pyogrio.write_dataframe(
        posts,
        raw_path,
        layer="POSTE_DE_TRANSFORMATION",
        driver="GPKG",
        append=True,
        geometry_type="Polygon",
    )
    roads = (
        road_frame
        if road_frame is not None
        else gpd.GeoDataFrame(
            {"cleabs": ["R1"], "nature": ["Route à 1 chaussée"]},
            geometry=[LineString([(599000, 6199000), (607000, 6201000)])],
            crs=2154,
        )
    )
    pyogrio.write_dataframe(
        roads, raw_path, layer="TRONCON_DE_ROUTE", driver="GPKG", append=True
    )
    coverage = box(599000, 6199000, 607000, 6201000)
    if variant in ("near", "equal", "crossing", "touch", "outside"):
        source = load_cadastre_parcels(
            cadastre_fr.download_cadastre_parcelles(
                "31395", cache, allow_download=False
            )
        )
        bounds = (
            source.parcels.loc[source.parcels.id == "31395000AA0001"]
            .to_crs(2154)
            .total_bounds
        )
        if variant == "near":
            coverage = box(599000, 6199000, bounds[2] + 5, 6201000)
        elif variant == "equal":
            coverage = box(599000, 6199000, 600070, 6201000)
        elif variant == "crossing":
            coverage = box(600030, 6199000, 607000, 6201000)
        elif variant == "touch":
            coverage = box(bounds[0], 6199000, 607000, 6201000)
        else:
            coverage = box(bounds[2] + 100, 6199000, 607000, 6201000)
    departments = gpd.GeoDataFrame(
        {"code_insee": ["31"], "nom_officiel": ["Synthetic department"]},
        geometry=[coverage],
        crs=2154,
    )
    pyogrio.write_dataframe(
        departments, raw_path, layer="DEPARTEMENT", driver="GPKG", append=True
    )
    archive_path = root / "fixture/grid.7z"
    with py7zr.SevenZipFile(archive_path, "w") as archive:
        archive.write(raw_path, arcname="BDTOPO/grid.gpkg")
    raw = archive_path.read_bytes()
    payload = yaml.safe_load(
        (PROJECT / "configs/sources/ign_bdtopo_fr.yaml").read_bytes()
    )
    from hashlib import sha256

    payload.update(
        source_url="https://example.test/GRID_TEST.7z",
        checksum_url=None,
        official_checksum_algorithm="sha256",
        official_checksum=sha256(raw).hexdigest(),
        expected_archive_size_bytes=len(raw),
    )
    config_path = root / "configs/sources/ign_bdtopo_fr.yaml"
    config_path.parent.mkdir()
    config_path.write_text(
        yaml.safe_dump(payload, allow_unicode=True), encoding="utf-8"
    )
    config = ign.load_ign_bdtopo_source_config(config_path)
    with patch.object(ign, "open_safe_https", return_value=io.BytesIO(raw)):
        download = ign.download_ign_bdtopo_archive(
            config, root / ign.DEFAULT_CACHE_DIR, allow_download=True
        )
    extraction = ign.extract_ign_bdtopo_archive(download, config, allow_extract=True)
    return scan, config_path, download, extraction


def _retained(scan):
    loaded = load_scan_config(scan)
    source = load_cadastre_parcels(
        cadastre_fr.download_cadastre_parcelles(
            "31395", scan.parents[2] / "data/cache/cadastre", allow_download=False
        )
    )
    normalized = normalize_cadastre_parcels(source)
    candidates, _ = filter_parcels_by_area(normalized, loaded.profile.parcel)
    retained, _ = filter_parcels_by_shape(
        enrich_parcel_shapes(candidates), loaded.profile.shape_screening
    )
    return retained


def _grid_run(root):
    scan, config_path, _, _ = write_grid_project(root)
    retained = _retained(scan)
    retained.index = pd.Index([19, 45], name="cadastre_row")
    options = grid._prepare_grid(
        root,
        "31395",
        root / "data/cache/cadastre",
        root / "outputs/check",
        (scan, root / "configs/profiles/bess_default_fr.yaml"),
        config_path,
        None,
        None,
    )
    return retained, grid._run_grid(retained, options)


def test_physical_grid_exports_preserve_selection_distances_ties_and_provenance(
    tmp_path, monkeypatch
):
    scan, _, download, extraction = write_grid_project(tmp_path)
    before = {p: p.read_bytes() for p in tmp_path.rglob("*") if p.is_file()}
    assess_calls = []
    public_results = []
    original = grid.assess_grid_coverage

    def record(*args):
        assess_calls.append(args)
        result = original(*args)
        public_results.append(result)
        return result

    monkeypatch.setattr(grid, "assess_grid_coverage", record)
    result = run_cadastre_screening(
        scan, with_grid=True, output_dir=Path("outputs/grid")
    )
    assert len(assess_calls) == 1
    assert (
        result.normalized_count,
        result.area_rejected_count,
        result.shape_rejected_count,
        result.retained_count,
    ) == (8, 4, 2, 2)
    assert (
        result.grid_status == "COMPLETE"
        and result.voltage_proximity_csv.name == "voltage_proximity.csv"
    )
    rows = read_csv(result.candidates_csv)
    assert tuple(rows[0]) == (*workflow.EXPORT_COLUMNS, *grid.GRID_COLUMNS)
    first, second = rows
    assert float(first["nearest_line_proxy_distance_m"]) == pytest.approx(10, abs=1e-6)
    assert float(first["nearest_exact_line_proxy_distance_m"]) == pytest.approx(
        10, abs=1e-6
    )
    assert (
        first["nearest_line_tie_count"] == first["nearest_exact_line_tie_count"] == "2"
    )
    assert first["nearest_line_source_feature_id"] == "A"
    assert float(first["nearest_post_proxy_distance_m"]) == 0
    assert first["nearest_line_coverage_status"] == "NOT_BOUNDARY_LIMITED"
    assert (
        second["nearest_line_voltage_status"] == "BELOW"
        and second["nearest_line_voltage_kv"] == ""
    )
    assert float(second["nearest_line_voltage_upper_bound_kv"]) == 45
    assert float(second["nearest_line_proxy_distance_m"]) == 0
    assert second["nearest_exact_line_coverage_status"] == "BOUNDARY_LIMITED"
    voltage = read_csv(result.voltage_proximity_csv)
    assert tuple(voltage[0]) == grid.VOLTAGE_EXPORT_COLUMNS
    assert [(r["parcel_id"], float(r["voltage_kv"])) for r in voltage] == [
        (r["parcel_id"], v) for r in rows for v in (63, 132.5)
    ]
    assert len(voltage) == 4
    public_table = public_results[0].voltage_level_proximity.set_index(
        ["parcel_id", "voltage_kv"]
    )
    for row in voltage:
        actual = public_table.loc[(row["parcel_id"], float(row["voltage_kv"]))]
        assert (
            float(row["nearest_line_proxy_distance_m"])
            == actual["nearest_line_proxy_distance_m"]
        )
        assert int(row["tie_count"]) == actual["tie_count"]
        for column in set(grid.VOLTAGE_EXPORT_COLUMNS) - {
            "parcel_id",
            "voltage_kv",
            "nearest_line_proxy_distance_m",
            "tie_count",
            "source_boundary_distance_m",
        }:
            assert row[column] == (
                "" if pd.isna(actual[column]) else str(actual[column])
            )
        assert (
            float(row["source_boundary_distance_m"])
            == actual["source_boundary_distance_m"]
        )
    geo = json.loads(result.candidates_geojson.read_bytes())
    retained = _retained(scan).set_index("parcel_id")
    for feature, row in zip(geo["features"], rows, strict=True):
        assert feature["id"] == row["parcel_id"]
        props = feature["properties"]
        assert type(props["nearest_line_tie_count"]) is int
        assert type(props["nearest_line_proxy_distance_m"]) is float
        assert props["nearest_line_voltage_upper_bound_kv"] is None or row[
            "parcel_id"
        ].endswith("0008")
        assert (
            shape(feature["geometry"]).wkb == retained.geometry.loc[feature["id"]].wkb
        )
        assert set(props) == set(row)
    manifest = json.loads(
        result.manifest_path.read_bytes(),
        parse_constant=lambda value: pytest.fail(value),
    )
    assert (
        manifest["schema_version"] == 2
        and manifest["scope"] == "CADASTRE_AREA_SHAPE_WITH_GRID_PROXIES"
    )
    assert (
        manifest["grid"]["status"] == "COMPLETE" and "grid" not in manifest["not_run"]
    )
    assert set(manifest["not_run"].values()) == {"NOT_RUN"}
    assert manifest["grid"]["archive"]["sha256"] == download.sha256
    assert manifest["grid"]["archive"]["cache_hit"] is True
    assert manifest["grid"]["geopackage"]["sha256"] == extraction.geopackage_sha256
    assert manifest["grid"]["extraction"]["cache_hit"] is True
    assert [r["voltage_kv"] for r in manifest["grid"]["voltage_level_coverage"]] == [
        63,
        132.5,
    ]
    from hashlib import sha256

    for entry in manifest["data_files"]:
        content = (result.output_dir / entry["path"]).read_bytes()
        assert (
            len(content) == entry["size_bytes"]
            and sha256(content).hexdigest() == entry["sha256"]
        )
    assert len(manifest["data_files"]) == 4
    assert (
        sha256(Path(manifest["configuration"]["ign"]["path"]).read_bytes()).hexdigest()
        == manifest["configuration"]["ign"]["sha256"]
    )
    assert all(path.read_bytes() == content for path, content in before.items())
    old = run_cadastre_screening(scan, output_dir=Path("outputs/old"))
    assert old.voltage_proximity_csv is None and old.grid_status is None
    assert json.loads(old.manifest_path.read_bytes())["schema_version"] == 1
    assert len(list(old.output_dir.iterdir())) == 4
    assert old.rejections_csv.read_bytes() == result.rejections_csv.read_bytes()
    assert [{k: row[k] for k in workflow.EXPORT_COLUMNS} for row in rows] == read_csv(
        old.candidates_csv
    )


@pytest.mark.parametrize(
    ("variant", "status"),
    [
        ("near", "BOUNDARY_LIMITED"),
        ("touch", "OUTSIDE_OR_CROSSING_COVERAGE"),
        ("outside", "OUTSIDE_OR_CROSSING_COVERAGE"),
    ],
)
def test_real_coverage_stages_preserve_boundary_statuses(tmp_path, variant, status):
    scan, _, _, _ = write_grid_project(tmp_path, variant)
    result = run_cadastre_screening(scan, with_grid=True)
    row = read_csv(result.candidates_csv)[0]
    assert row["nearest_line_coverage_status"] == status
    if variant != "near":
        assert float(row["grid_source_boundary_distance_m"]) == 0


def test_no_exact_voltage_is_valid_distinct_from_unusable_source(tmp_path):
    scan, _, _, _ = write_grid_project(tmp_path, "no_exact")
    result = run_cadastre_screening(scan, with_grid=True)
    rows = read_csv(result.candidates_csv)
    assert rows[0]["nearest_line_voltage_status"] == "UNKNOWN"
    assert rows[0]["nearest_line_voltage_kv"] == ""
    assert all(
        r["nearest_exact_line_proxy_distance_m"] == ""
        and r["nearest_exact_line_coverage_status"] == "NO_MATCH"
        for r in rows
    )
    assert read_csv(result.voltage_proximity_csv) == []
    assert result.voltage_proximity_csv.read_text(encoding="utf-8").strip().split(
        ","
    ) == list(grid.VOLTAGE_EXPORT_COLUMNS)
    manifest = json.loads(result.manifest_path.read_bytes())
    assert (
        manifest["grid"]["status"] == "COMPLETE"
        and manifest["grid"]["voltage_level_coverage"] == []
    )


@pytest.mark.parametrize("variant", ["no_lines", "no_posts"])
def test_unusable_electric_geometry_fails_instead_of_no_match(tmp_path, variant):
    scan, _, _, _ = write_grid_project(tmp_path, variant)
    with pytest.raises(CadastreScreeningRunError, match="proximity"):
        run_cadastre_screening(scan, with_grid=True, output_dir=Path("outputs/fail"))
    assert not (tmp_path / "outputs/fail/run.json").exists()


def test_zero_retained_does_not_access_ign_but_keeps_extended_empty_schema(
    tmp_path, monkeypatch
):
    scan, _, _, _ = write_grid_project(tmp_path)
    profile = tmp_path / "configs/profiles/bess_default_fr.yaml"
    values = yaml.safe_load(profile.read_bytes())
    values["parcel"] = {"min_area_m2": 80000, "max_area_m2": 90000}
    profile.write_text(yaml.safe_dump(values), encoding="utf-8")

    def fail(*args, **kwargs):
        raise AssertionError("No grid source access for zero retained parcels")

    for name in (
        "download_ign_bdtopo_archive",
        "extract_ign_bdtopo_archive",
    ):
        monkeypatch.setattr(ign_workflow, name, fail)
    for name in ("load_ign_bdtopo_electricity", "assess_grid_coverage"):
        monkeypatch.setattr(grid, name, fail)
    result = run_cadastre_screening(scan, with_grid=True)
    assert result.retained_count == 0 and result.grid_status == "NOT_RUN"
    assert result.candidates_csv.read_text(encoding="utf-8").strip().split(",") == [
        *workflow.EXPORT_COLUMNS,
        *grid.GRID_COLUMNS,
    ]
    assert read_csv(result.voltage_proximity_csv) == []
    manifest = json.loads(result.manifest_path.read_bytes())
    assert manifest["grid"] == {"status": "NOT_RUN", "reason": "NO_RETAINED_PARCELS"}
    assert manifest["not_run"]["grid"] == "NOT_RUN" and manifest["schema_version"] == 2


def test_named_sparse_index_is_restored_only_on_a_copy(tmp_path):
    retained, run = _grid_run(tmp_path)
    stage_before = run.assessment.parcels.copy(deep=True)
    retained_before = retained.copy(deep=True)
    restored = grid._restore_parcel_index(retained, run.assessment.parcels)
    assert type(restored.index) is type(retained.index) and restored.index.equals(
        retained.index
    )
    assert restored.index.name == "cadastre_row" and restored.index.tolist() == [19, 45]
    assert_geodataframe_equal(retained, retained_before)
    assert_geodataframe_equal(run.assessment.parcels, stage_before)
    grid._compare_frame(restored.loc[:, retained.columns], retained)
    assert run.assessment.voltage_level_proximity.index.equals(pd.RangeIndex(4))


@pytest.mark.parametrize(
    "mutation",
    ["permutation", "missing", "duplicate", "value", "dtype", "geometry", "column"],
)
def test_index_restoration_never_hides_prefix_or_id_damage(tmp_path, mutation):
    retained, run = _grid_run(tmp_path)
    changed = run.assessment.parcels.copy(deep=True)
    if mutation == "permutation":
        changed = changed.iloc[::-1]
    elif mutation == "missing":
        changed = changed.iloc[1:]
    elif mutation == "duplicate":
        changed.loc[1, "parcel_id"] = changed.loc[0, "parcel_id"]
    elif mutation == "value":
        changed.loc[0, "area_m2"] += 1
    elif mutation == "dtype":
        changed["area_m2"] = changed.area_m2.astype(object)
    elif mutation == "geometry":
        changed.loc[0, "geometry"] = translate(changed.geometry.iloc[0], xoff=0.001)
    else:
        changed = changed.drop(columns="compactness")
    with pytest.raises(grid.GridScreeningError):
        grid._restore_parcel_index(retained, changed)


@pytest.mark.parametrize("layer", ["electric_lines", "transformation_posts"])
@pytest.mark.parametrize(
    "mutation",
    ["value", "dtype", "geometry", "summary", "summary_type", "index", "attrs"],
)
def test_final_public_reread_compares_both_complete_bundles(
    tmp_path, monkeypatch, layer, mutation
):
    _, run = _grid_run(tmp_path)
    public_load = grid.load_ign_bdtopo_electricity

    def altered(*args):
        fresh = public_load(*args)
        if mutation in ("summary", "summary_type"):
            name = layer + "_summary"
            summary = getattr(fresh, name)
            return replace(
                fresh,
                **{
                    name: replace(summary, feature_count=summary.feature_count + 1)
                    if mutation == "summary"
                    else object()
                },
            )
        frame = getattr(fresh, layer).copy(deep=True)
        if mutation == "value":
            frame.loc[0, "etat_de_l_objet"] = "Changed"
        elif mutation == "dtype":
            frame["precision_planimetrique"] = frame.precision_planimetrique.astype(
                object
            )
        elif mutation == "geometry":
            frame.loc[0, "geometry"] = translate(frame.geometry.iloc[0], xoff=1)
        elif mutation == "index":
            frame.index = pd.Index(list(frame.index), name="changed")
        else:
            frame.attrs["changed"] = True
        return replace(fresh, **{layer: frame})

    monkeypatch.setattr(grid, "load_ign_bdtopo_electricity", altered)
    with pytest.raises(grid.GridScreeningError):
        grid._final_grid_check(run)


@pytest.mark.parametrize("mutation", ["yaml", "archive", "gpkg", "marker"])
def test_persistent_physical_mutation_after_export_prevents_complete(
    tmp_path, monkeypatch, mutation
):
    scan, config, download, extraction = write_grid_project(tmp_path)
    path = {
        "yaml": config,
        "archive": download.path,
        "gpkg": extraction.geopackage_path,
        "marker": extraction.extraction_path / ".landscout-extraction.json",
    }[mutation]
    original = workflow._write_geojson

    def alter(*args):
        original(*args)
        path.write_bytes(
            path.read_bytes() + (b"\n " if mutation == "marker" else b"\n#changed")
        )

    monkeypatch.setattr(workflow, "_write_geojson", alter)
    output = tmp_path / "outputs/fail"
    with pytest.raises(CadastreScreeningRunError, match="incomplete output") as error:
        run_cadastre_screening(scan, with_grid=True, output_dir=output)
    assert error.value.__cause__ is not None and not (output / "run.json").exists()


@pytest.mark.parametrize(
    "filename",
    [
        "candidates.csv",
        "rejections.csv",
        "candidates.geojson",
        "voltage_proximity.csv",
        "run.json.part",
    ],
)
def test_grid_write_failure_never_publishes_complete(tmp_path, monkeypatch, filename):
    scan, _, _, _ = write_grid_project(tmp_path)
    original = Path.open

    def fail(path, *args, **kwargs):
        if path.name == filename and args and "x" in args[0]:
            raise OSError("injected grid output failure")
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", fail)
    output = tmp_path / "outputs/fail"
    with pytest.raises(CadastreScreeningRunError, match="incomplete output"):
        run_cadastre_screening(scan, with_grid=True, output_dir=output)
    assert output.exists() and not (output / "run.json").exists()


@pytest.mark.parametrize("flag", [None, 0, 1, "true"])
def test_grid_flag_is_exact_bool_before_acquisition(tmp_path, flag):
    scan, _, _ = write_project(tmp_path)
    with pytest.raises(CadastreScreeningRunError, match="exact bool"):
        run_cadastre_screening(scan, with_grid=flag)


@pytest.mark.parametrize(
    "key", ["ign_config_path", "ign_cache_dir", "ign_extraction_dir"]
)
def test_ign_paths_are_not_silently_ignored_without_grid(tmp_path, key):
    scan, _, _ = write_project(tmp_path)
    with pytest.raises(CadastreScreeningRunError, match="require with_grid"):
        run_cadastre_screening(scan, **{key: Path("unused")})


@pytest.mark.parametrize(
    "conflict",
    [
        "caches",
        "extraction_cadastre",
        "extraction_parent",
        "cache_link",
        "extraction_link",
        "config_link",
        "output_ign",
    ],
)
def test_ign_path_preflight_protects_existing_inputs_before_cadastre_acquisition(
    tmp_path, monkeypatch, conflict
):
    scan, config, _, extraction = write_grid_project(tmp_path)
    cache = tmp_path / "data/cache/ign_bdtopo"
    kwargs = {"with_grid": True, "output_dir": tmp_path / "outputs/fail"}
    if conflict == "caches":
        kwargs["ign_cache_dir"] = tmp_path / "data/cache/cadastre"
    elif conflict == "extraction_cadastre":
        kwargs["ign_extraction_dir"] = tmp_path / "data/cache/cadastre"
    elif conflict == "extraction_parent":
        kwargs["ign_extraction_dir"] = cache.parent
    elif conflict == "output_ign":
        kwargs["output_dir"] = cache / "new-output"
    else:
        unsafe = {
            "cache_link": cache,
            "extraction_link": extraction.extraction_path,
            "config_link": config,
        }[conflict]
        if conflict == "extraction_link":
            kwargs["ign_extraction_dir"] = unsafe
        original = Path.is_symlink
        monkeypatch.setattr(
            Path, "is_symlink", lambda path: path == unsafe or original(path)
        )
    before = {p: p.read_bytes() for p in tmp_path.rglob("*") if p.is_file()}

    def fail(*args, **kwargs):
        raise AssertionError("Cadastre acquisition must follow IGN preflight")

    monkeypatch.setattr(workflow, "download_cadastre_parcelles", fail)
    with pytest.raises(CadastreScreeningRunError):
        run_cadastre_screening(scan, **kwargs)
    assert all(path.read_bytes() == raw for path, raw in before.items())


@pytest.mark.parametrize(
    "column", ["nearest_line_proxy_distance_m", "nearest_line_tie_count", "voltage_kv"]
)
def test_grid_numeric_serialization_never_coerces_bool(column):
    with pytest.raises(grid.GridScreeningError):
        grid._scalar(True, column)


@pytest.mark.parametrize(
    ("commune", "department"),
    [
        ("31395", "31"),
        ("2A004", "2A"),
        ("2B033", "2B"),
        ("97105", "971"),
        ("97601", "976"),
    ],
)
def test_grid_department_mapping_reuses_canonical_commune_contract(
    tmp_path, commune, department
):
    scan, _, _ = write_project(tmp_path)
    path = tmp_path / "ign.yaml"
    values = yaml.safe_load(
        (PROJECT / "configs/sources/ign_bdtopo_fr.yaml").read_bytes()
    )
    values["department_code"] = department
    path.write_text(yaml.safe_dump(values), encoding="utf-8")
    options = grid._prepare_grid(
        tmp_path,
        commune,
        tmp_path / "data/cache/cadastre",
        tmp_path / "outputs/run",
        (scan,),
        path,
        None,
        None,
    )
    assert options.config.department_code == department


def test_ign_configuration_binding_is_checked_around_public_load(tmp_path, monkeypatch):
    scan, _, _, _ = write_grid_project(tmp_path)
    original = grid.load_ign_bdtopo_source_config

    def alter(path):
        loaded = original(path)
        path.write_bytes(path.read_bytes() + b"\n#changed during load")
        return loaded

    monkeypatch.setattr(grid, "load_ign_bdtopo_source_config", alter)
    with pytest.raises(CadastreScreeningRunError, match="configuration changed"):
        run_cadastre_screening(scan, with_grid=True)
    assert not (tmp_path / "outputs").exists()


def test_cadastre_download_permission_never_authorizes_ign_download_or_extract(
    tmp_path, monkeypatch
):
    scan, _, _, _ = write_grid_project(tmp_path)
    observed = []
    download = ign_workflow.download_ign_bdtopo_archive
    extract = ign_workflow.extract_ign_bdtopo_archive

    def record_download(*args, **kwargs):
        observed.append(("download", kwargs["allow_download"]))
        return download(*args, **kwargs)

    def record_extract(*args, **kwargs):
        observed.append(("extract", kwargs["allow_extract"]))
        return extract(*args, **kwargs)

    monkeypatch.setattr(ign_workflow, "download_ign_bdtopo_archive", record_download)
    monkeypatch.setattr(ign_workflow, "extract_ign_bdtopo_archive", record_extract)
    result = run_cadastre_screening(scan, with_grid=True, allow_download=True)
    assert result.grid_status == "COMPLETE"
    assert observed == [("download", False), ("extract", False)]
