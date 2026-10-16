"""Physical gzip/7z/GPKG integration through the complete public road chain."""

import json
from dataclasses import replace
from hashlib import sha256
from pathlib import Path

import geopandas as gpd
import numpy as np
import pandas as pd
import pytest
import yaml
from shapely.affinity import translate
from shapely.geometry import LineString
from test_cadastre_screening import PROJECT, read_csv, write_project
from test_grid_screening import _retained, write_grid_project

from landscout.sources import cadastre_fr
from landscout.sources import ign_bdtopo_fr as source_ign
from landscout.workflows import CadastreScreeningRunError, run_cadastre_screening
from landscout.workflows import cadastre_screening as workflow
from landscout.workflows import grid_screening as grid
from landscout.workflows import ign_screening as ign
from landscout.workflows import road_screening as road


@pytest.fixture(autouse=True)
def no_transport(monkeypatch):
    def deny(*args, **kwargs):
        raise AssertionError("Road workflow must stay offline")

    monkeypatch.setattr(cadastre_fr, "open_safe_https", deny)
    monkeypatch.setattr(source_ign, "open_safe_https", deny)


def road_frame(variant="normal"):
    # Actual factual dtypes: fictif bool; prive/width float64; source TEXT str.
    count = 7
    text = {
        "cleabs": [
            "B",
            "A",
            "LIMITED",
            "RESTRICTED",
            "NON_GENERAL",
            "FICTITIOUS",
            "UNKNOWN",
        ],
        "nature": ["Route à 1 chaussée"] * 2
        + [
            "Chemin",
            "Route à 1 chaussée",
            "Sentier",
            "Route à 1 chaussée",
            "Route à 1 chaussée",
        ],
        "importance": ["2"] * count,
        "etat_de_l_objet": ["En service"] * count,
        "sens_de_circulation": ["Double sens"] * count,
        "acces_vehicule_leger": [
            "A péage",
            "A péage",
            "Libre",
            "Restreint aux ayants droit",
            "Libre",
            "Libre",
            "Libre",
        ],
        # A real TEXT value avoids the reader's all-null -> float64 inference.
        # These facts belong to the fictitious, distance-ineligible road only.
        "periode_de_fermeture": [None] * 5 + ["Hiver", None],
        "nature_de_la_restriction": [None] * 5 + ["Passage barré", None],
        "cpx_classement_administratif": ["Départementale"] * count,
        "cpx_gestionnaire": ["Source manager"] * count,
        "sources": ["  raw source ; preserved  "] * count,
        "identifiants_sources": ["fixture"] * count,
        "date_creation": ["2026-01-01"] * count,
        "date_modification": ["2026-01-02"] * count,
        "date_de_confirmation": ["2026-01-03"] * count,
        "methode_d_acquisition_planimetrique": ["synthetic"] * count,
    }
    values = {key: pd.Series(items, dtype="str") for key, items in text.items()}
    values.update(
        fictif=pd.Series([False] * 5 + [True, False], dtype="bool"),
        prive=pd.Series([0, 0, 0, 1, 0, 0, None], dtype="float64"),
        largeur_de_chaussee=pd.Series([4.0] * count, dtype="float64"),
        position_par_rapport_au_sol=[0] * count,
        nombre_de_voies=[2] * count,
        urbain=[False] * count,
        vitesse_moyenne_vl=[50.0] * count,
        matieres_dangereuses_interdites=[False] * count,
        precision_planimetrique=[1.0] * count,
    )
    for name in ("hauteur", "poids_total", "poids_par_essieu", "largeur", "longueur"):
        values["restriction_de_" + name] = [np.nan] * count
    geometries = [
        LineString([(x, 6199900), (x, 6200200)])
        for x in (600070, 600070, 606020, 600080, 600090, 600100, 600110)
    ]
    frame = gpd.GeoDataFrame(values, geometry=geometries, crs=2154)
    if variant == "empty_classes":
        frame = frame.iloc[:2].copy()
    elif variant == "all_not_distance":
        frame["fictif"] = True
    elif variant == "private_bool":
        frame["prive"] = pd.Series([False, False, False, True, False, False, False])
        frame.loc[6, "nature"] = "Unknown nature"
    elif variant == "private_text":
        frame["prive"] = "  unresolved private TEXT  "
    return frame


def write_road_project(root, variant="normal", coverage="normal"):
    scan, config, download, extraction = write_grid_project(
        root, coverage, road_frame=road_frame(variant)
    )
    policy = root / "configs/access/ign_bdtopo_vehicle_proxy_policy.yaml"
    policy.parent.mkdir()
    policy.write_bytes(
        (PROJECT / "configs/access/ign_bdtopo_vehicle_proxy_policy.yaml").read_bytes()
    )
    return scan, config, download, extraction, policy


def _road_run(root, variant="normal"):
    scan, config, _, _, policy = write_road_project(root, variant)
    retained = _retained(scan)
    retained.index = pd.Index([19, 45], name="cadastre_row")
    options = grid._prepare_grid(
        root,
        "31395",
        root / "data/cache/cadastre",
        root / "outputs/run",
        (scan, policy),
        config,
        None,
        None,
    )
    context = ign._acquire_ign(
        options.config, options.cache_dir, options.extraction_dir
    )
    return retained, road._run_roads(
        retained, options, road._prepare_roads(root, policy), context
    )


def test_all_four_modes_keep_selection_and_share_one_physical_context(
    tmp_path, monkeypatch
):
    scan, _, _, extraction, policy = write_road_project(tmp_path)
    before = {p: p.read_bytes() for p in tmp_path.rglob("*") if p.is_file()}
    observed = []
    assessments = []
    original_download, original_extract = (
        ign.download_ign_bdtopo_archive,
        ign.extract_ign_bdtopo_archive,
    )
    original_grid, original_road = (
        grid.assess_grid_coverage,
        road.assess_road_proximity_coverage,
    )

    def download(*args, **kwargs):
        observed.append(("download", kwargs["allow_download"]))
        return original_download(*args, **kwargs)

    def extract(*args, **kwargs):
        observed.append(("extract", kwargs["allow_extract"]))
        return original_extract(*args, **kwargs)

    def grid_assessment(*args):
        assessments.append(("grid", args))
        return original_grid(*args)

    def road_assessment(*args):
        assessments.append(("road", args))
        return original_road(*args)

    monkeypatch.setattr(ign, "download_ign_bdtopo_archive", download)
    monkeypatch.setattr(ign, "extract_ign_bdtopo_archive", extract)
    monkeypatch.setattr(grid, "assess_grid_coverage", grid_assessment)
    monkeypatch.setattr(road, "assess_road_proximity_coverage", road_assessment)
    results = {}
    for with_grid, with_roads in (
        (False, False),
        (True, False),
        (False, True),
        (True, True),
    ):
        observed.clear()
        assessments.clear()
        result = run_cadastre_screening(
            scan,
            with_grid=with_grid,
            with_roads=with_roads,
            allow_download=True,
            output_dir=Path(f"outputs/{with_grid}-{with_roads}"),
        )
        results[with_grid, with_roads] = result
        assert observed == (
            [("download", False), ("extract", False)] if with_grid or with_roads else []
        )
        assert [kind for kind, _ in assessments] == (["grid"] if with_grid else []) + (
            ["road"] if with_roads else []
        )
        if with_grid and with_roads:
            assert assessments[0][1][0] is assessments[1][1][0]
            assert assessments[0][1][1].extraction is assessments[1][1][1].extraction
            assert assessments[1][1][3] == policy.resolve()
        manifest = json.loads(result.manifest_path.read_bytes())
        assert manifest["schema_version"] == (
            3 if with_roads else 2 if with_grid else 1
        )
        assert len(manifest["data_files"]) == 3 + int(with_grid) + int(with_roads)
        assert len(list(result.output_dir.iterdir())) == 4 + int(with_grid) + int(
            with_roads
        )
        assert (
            result.normalized_count,
            result.area_rejected_count,
            result.shape_rejected_count,
            result.retained_count,
        ) == (8, 4, 2, 2)
        for item in manifest["data_files"]:
            raw = (result.output_dir / item["path"]).read_bytes()
            assert (
                len(raw) == item["size_bytes"]
                and sha256(raw).hexdigest() == item["sha256"]
            )
        if with_roads:
            assert (
                manifest["roads"]["geopackage"]["sha256"]
                == extraction.geopackage_sha256
            )
            assert (
                manifest["roads"]["policy"]["binding"]
                == manifest["configuration"]["road_policy"]
            )
            assert (
                manifest["roads"]["policy"]["config_sha256"]
                == sha256(policy.read_bytes()).hexdigest()
            )
            assert manifest["roads"]["policy"]["heavy_vehicle_access"] == "NOT_PROVEN"
            assert "roads" not in manifest["not_run"]
        if with_grid and with_roads:
            assert manifest["grid"]["extraction"] == manifest["roads"]["extraction"]
            assert (
                manifest["grid"]["source_coverage"]
                == manifest["roads"]["source_coverage"]
            )
    plain = results[False, False]
    for result in results.values():
        assert result.rejections_csv.read_bytes() == plain.rejections_csv.read_bytes()
        assert [
            {k: r[k] for k in workflow.EXPORT_COLUMNS}
            for r in read_csv(result.candidates_csv)
        ] == read_csv(plain.candidates_csv)
        assert [
            f["geometry"]
            for f in json.loads(result.candidates_geojson.read_bytes())["features"]
        ] == [
            f["geometry"]
            for f in json.loads(plain.candidates_geojson.read_bytes())["features"]
        ]
    assert (
        results[True, False].candidates_csv.read_bytes()
        == results[True, True].candidates_csv.read_bytes()
    )
    assert (
        results[True, False].voltage_proximity_csv.read_bytes()
        == results[True, True].voltage_proximity_csv.read_bytes()
    )
    assert (
        results[False, True].road_proximity_csv.read_bytes()
        == results[True, True].road_proximity_csv.read_bytes()
    )
    assert all(path.read_bytes() == raw for path, raw in before.items())


@pytest.mark.parametrize(
    "variant",
    ["normal", "empty_classes", "all_not_distance", "private_bool", "private_text"],
)
def test_physical_road_chain_classes_types_ties_nulls_and_every_csv_cell(
    tmp_path, variant
):
    retained, run = _road_run(tmp_path, variant)
    if variant == "normal":
        raw = run.source.road_segments
        assert str(raw.fictif.dtype) == "bool"
        assert str(raw.prive.dtype) == str(raw.largeur_de_chaussee.dtype) == "float64"
        assert all(
            str(raw[name].dtype) == "str"
            for name in (
                "nature",
                "importance",
                "etat_de_l_objet",
                "acces_vehicule_leger",
                "periode_de_fermeture",
                "nature_de_la_restriction",
            )
        )
    table = run.assessment.class_proximity
    before = table.copy(deep=True)
    grid._compare_frame(retained, run.assessment.parcels)
    assert retained.index.tolist() == [19, 45] and retained.index.name == "cadastre_row"
    assert table.index.equals(pd.RangeIndex(10))
    coverage = run.assessment.class_coverage
    assert len(coverage) == 6 and sum(c.feature_count for c in coverage) == len(
        road_frame(variant)
    )
    assert [c.feature_count for c in coverage] == (
        {
            "normal": [2, 1, 1, 1, 1, 1],
            "empty_classes": [2, 0, 0, 0, 0, 0],
            "all_not_distance": [0, 0, 0, 0, 7, 0],
            "private_bool": [2, 1, 1, 1, 1, 1],
            "private_text": [0, 1, 1, 1, 1, 3],
        }[variant]
    )
    assert not table.road_proxy_class.eq("NOT_DISTANCE_PROXY").any()
    records = road._road_records(run)
    path = tmp_path / "roads.csv"
    road._write_road_csv(path, records)
    rows = read_csv(path)
    assert tuple(rows[0]) == road.ROAD_EXPORT_COLUMNS
    expected_order = [
        (p, c.road_proxy_class)
        for p in sorted(retained.parcel_id)
        for c in coverage
        if c.distance_eligible
    ]
    assert [(r["parcel_id"], r["road_proxy_class"]) for r in rows] == expected_order
    lookup = table.set_index(["parcel_id", "road_proxy_class"])
    for row in rows:
        actual = lookup.loc[(row["parcel_id"], row["road_proxy_class"])]
        for column in road.ROAD_EXPORT_COLUMNS:
            value = (
                row[column]
                if column in ("parcel_id", "road_proxy_class")
                else actual[column]
            )
            # Independent encoding expectation, including nullable extension bools.
            encoded = (
                ""
                if pd.isna(value)
                else ("true" if value else "false")
                if isinstance(value, (bool, np.bool_))
                else str(value)
            )
            assert row[column] == encoded
    pd.testing.assert_frame_equal(table, before, check_exact=True)
    if variant in ("normal", "private_bool"):
        first = next(
            r for r in rows if r["road_proxy_class"] == "GENERAL_VEHICLE_PROXY"
        )
        assert (
            first["nearest_source_feature_id"] == "A"
            and first["nearest_road_tie_count"] == "2"
        )
        assert float(first["nearest_road_proxy_distance_m"]) == pytest.approx(
            10, abs=1e-6
        )
        assert first["nearest_road_toll_evidence"] == "true"
        restricted = next(
            r for r in rows if r["road_proxy_class"] == "RESTRICTED_REVIEW"
        )
        assert restricted["nearest_road_primary_rule"] == "RIGHTS_RESTRICTED"
        assert json.loads(restricted["nearest_road_rule_trace_json"])[:2] == [
            "RIGHTS_RESTRICTED",
            "PRIVATE_ROAD",
        ]
        unknown = next(r for r in rows if r["road_proxy_class"] == "UNKNOWN_REVIEW")
        assert unknown["nearest_road_unknown_fields_json"] == (
            '["private_raw"]' if variant == "normal" else '["nature_raw"]'
        )
        second_limited = next(
            r
            for r in rows
            if r["parcel_id"].endswith("0008")
            and r["road_proxy_class"] == "LIMITED_VEHICLE_PROXY"
        )
        assert float(second_limited["nearest_road_proxy_distance_m"]) == 0
        assert second_limited["nearest_road_toll_evidence"] == "false"
        assert type(
            road._scalar(
                lookup.loc[
                    (restricted["parcel_id"], "RESTRICTED_REVIEW"),
                    "nearest_private_raw",
                ],
                "nearest_private_raw",
            )
        ) is (float if variant == "normal" else bool)
    if variant in ("empty_classes", "all_not_distance"):
        empty = [
            r
            for r in rows
            if variant == "all_not_distance"
            or r["road_proxy_class"] != "GENERAL_VEHICLE_PROXY"
        ]
        assert all(
            r["road_proximity_coverage_status"] == "NO_MATCH"
            and r["nearest_road_proxy_distance_m"]
            == r["nearest_road_tie_count"]
            == r["nearest_road_toll_evidence"]
            == ""
            for r in empty
        )
    if variant == "private_text":
        assert all(
            r["nearest_private_raw"] == "  unresolved private TEXT  "
            for r in rows
            if r["nearest_road_feature_id"]
        )
    road._final_road_check(run)


@pytest.mark.parametrize(
    "coverage,status",
    [
        ("normal", "NOT_BOUNDARY_LIMITED"),
        ("near", "BOUNDARY_LIMITED"),
        ("equal", "BOUNDARY_LIMITED"),
        ("crossing", "OUTSIDE_OR_CROSSING_COVERAGE"),
        ("touch", "OUTSIDE_OR_CROSSING_COVERAGE"),
        ("outside", "OUTSIDE_OR_CROSSING_COVERAGE"),
    ],
)
def test_roads_only_uses_real_boundary_not_electric_assessment(
    tmp_path, monkeypatch, coverage, status
):
    scan, _, _, _, _ = write_road_project(tmp_path, coverage=coverage)

    def deny(*args, **kwargs):
        raise AssertionError("Road-only mode must not load/analyze electricity")

    monkeypatch.setattr(grid, "load_ign_bdtopo_electricity", deny)
    monkeypatch.setattr(grid, "assess_grid_coverage", deny)
    result = run_cadastre_screening(scan, with_roads=True)
    row = read_csv(result.road_proximity_csv)[0]
    assert row["road_proximity_coverage_status"] == status
    if coverage in ("touch", "outside"):
        assert float(row["road_source_boundary_distance_m"]) == 0
    if coverage == "equal":
        assert float(row["road_source_boundary_distance_m"]) == float(
            row["nearest_road_proxy_distance_m"]
        )


@pytest.mark.parametrize("with_grid", [False, True])
def test_zero_retained_validates_policy_without_any_ign_acquisition(
    tmp_path, monkeypatch, with_grid
):
    scan, _, _, _, _ = write_road_project(tmp_path)
    profile = tmp_path / "configs/profiles/bess_default_fr.yaml"
    payload = yaml.safe_load(profile.read_bytes())
    payload["parcel"] = {"min_area_m2": 80000, "max_area_m2": 90000}
    profile.write_text(yaml.safe_dump(payload), encoding="utf-8")

    def deny(*args, **kwargs):
        raise AssertionError("Zero retained means no IGN physical access")

    monkeypatch.setattr(ign, "_acquire_ign", deny)
    monkeypatch.setattr(road, "load_ign_bdtopo_roads", deny)
    monkeypatch.setattr(road, "assess_road_proximity_coverage", deny)
    result = run_cadastre_screening(scan, with_roads=True, with_grid=with_grid)
    assert result.retained_count == 0 and result.roads_status == "NOT_RUN"
    assert read_csv(result.road_proximity_csv) == []
    assert result.road_proximity_csv.read_text().strip().split(",") == list(
        road.ROAD_EXPORT_COLUMNS
    )
    manifest = json.loads(result.manifest_path.read_bytes())
    assert manifest["schema_version"] == 3 and manifest["not_run"]["roads"] == "NOT_RUN"
    assert set(manifest["roads"]) == {"status", "reason", "policy"}
    assert manifest["roads"]["reason"] == "NO_RETAINED_PARCELS"


@pytest.mark.parametrize(
    "mutation",
    [
        "permutation",
        "missing",
        "duplicate",
        "value",
        "dtype",
        "geometry",
        "index",
        "attrs",
    ],
)
def test_road_parcels_have_no_index_restoration_exception(
    tmp_path, monkeypatch, mutation
):
    scan, _, _, _, _ = write_road_project(tmp_path)
    original = road.assess_road_proximity_coverage

    def altered(*args):
        result = original(*args)
        frame = result.parcels.copy(deep=True)
        if mutation == "permutation":
            frame = frame.iloc[::-1]
        elif mutation == "missing":
            frame = frame.iloc[1:]
        elif mutation == "duplicate":
            frame.iloc[1, frame.columns.get_loc("parcel_id")] = frame.parcel_id.iloc[0]
        elif mutation == "value":
            frame["area_m2"] += 1
        elif mutation == "dtype":
            frame["area_m2"] = frame.area_m2.astype(object)
        elif mutation == "geometry":
            frame.iloc[0, frame.columns.get_loc("geometry")] = translate(
                frame.geometry.iloc[0], xoff=0.001
            )
        elif mutation == "index":
            frame.index = pd.RangeIndex(len(frame))
        else:
            frame.attrs["changed"] = True
        return replace(result, parcels=frame)

    monkeypatch.setattr(road, "assess_road_proximity_coverage", altered)
    with pytest.raises(CadastreScreeningRunError) as error:
        run_cadastre_screening(scan, with_roads=True)
    assert error.value.__cause__ is not None and not (tmp_path / "outputs").exists()


@pytest.mark.parametrize(
    "mutation",
    [
        "value",
        "dtype",
        "geometry",
        "index",
        "attrs",
        "summary",
        "summary_type",
        "extraction",
        "role",
    ],
)
def test_final_road_public_reread_refuses_complete_on_full_bundle_difference(
    tmp_path, monkeypatch, mutation
):
    scan, _, _, _, _ = write_road_project(tmp_path)
    original = road.load_ign_bdtopo_roads
    calls = []

    def altered(*args):
        fresh = original(*args)
        calls.append(fresh)
        if len(calls) == 1:
            return fresh
        if mutation == "summary":
            return replace(
                fresh,
                road_segments_summary=replace(
                    fresh.road_segments_summary, feature_count=99
                ),
            )
        if mutation == "summary_type":
            return replace(fresh, road_segments_summary=object())
        if mutation == "extraction":
            return replace(fresh, extraction=replace(fresh.extraction))
        if mutation == "role":
            return replace(
                fresh,
                road_segments_summary=replace(
                    fresh.road_segments_summary, spatial_role="wrong"
                ),
            )
        frame = fresh.road_segments.copy(deep=True)
        if mutation == "value":
            frame.loc[0, "nature"] = "Changed"
        elif mutation == "dtype":
            frame["largeur_de_chaussee"] = frame.largeur_de_chaussee.astype(object)
        elif mutation == "geometry":
            frame.loc[0, "geometry"] = translate(frame.geometry.iloc[0], xoff=1)
        elif mutation == "index":
            frame.index = pd.Index(frame.index.tolist(), name="changed")
        else:
            frame.attrs["changed"] = True
        return replace(fresh, road_segments=frame)

    monkeypatch.setattr(road, "load_ign_bdtopo_roads", altered)
    output = tmp_path / "outputs/fail"
    with pytest.raises(CadastreScreeningRunError, match="incomplete output") as error:
        run_cadastre_screening(scan, with_roads=True, output_dir=output)
    assert error.value.__cause__ is not None and not (output / "run.json").exists()


@pytest.mark.parametrize("with_grid", [False, True])
@pytest.mark.parametrize("mutation", ["yaml", "policy", "archive", "gpkg", "marker"])
def test_persistent_physical_or_policy_mutation_after_export_blocks_complete(
    tmp_path, monkeypatch, with_grid, mutation
):
    scan, config, download, extraction, policy = write_road_project(tmp_path)
    target = {
        "yaml": config,
        "policy": policy,
        "archive": download.path,
        "gpkg": extraction.geopackage_path,
        "marker": extraction.extraction_path / ".landscout-extraction.json",
    }[mutation]
    original = road._write_road_csv

    def alter(*args):
        original(*args)
        target.write_bytes(target.read_bytes() + b"\n ")

    monkeypatch.setattr(road, "_write_road_csv", alter)
    output = tmp_path / "outputs/fail"
    with pytest.raises(CadastreScreeningRunError, match="incomplete output") as error:
        run_cadastre_screening(
            scan, with_roads=True, with_grid=with_grid, output_dir=output
        )
    assert error.value.__cause__ is not None and not (output / "run.json").exists()


@pytest.mark.parametrize(
    "failure", ["invalid", "missing", "during_load", "hash", "after_ign_load"]
)
def test_policy_gate_precedes_cadastre_acquisition_even_zero_retained(
    tmp_path, monkeypatch, failure
):
    scan, _, _, _, policy = write_road_project(tmp_path)
    profile = tmp_path / "configs/profiles/bess_default_fr.yaml"
    payload = yaml.safe_load(profile.read_bytes())
    payload["parcel"] = {"min_area_m2": 80000, "max_area_m2": 90000}
    profile.write_text(yaml.safe_dump(payload), encoding="utf-8")
    if failure == "invalid":
        policy.write_text("invalid: true", encoding="utf-8")
    elif failure == "missing":
        policy.unlink()
    elif failure == "after_ign_load":
        load = grid.load_ign_bdtopo_source_config

        def alter_config(path):
            result = load(path)
            policy.write_bytes(policy.read_bytes() + b"\n")
            return result

        monkeypatch.setattr(grid, "load_ign_bdtopo_source_config", alter_config)
    else:
        original = road.load_ign_road_vehicle_proxy_policy

        def alter(path):
            result = original(path)
            if failure == "during_load":
                path.write_bytes(path.read_bytes() + b"\n")
            else:
                result = replace(result, config_sha256="0" * 64)
            return result

        monkeypatch.setattr(road, "load_ign_road_vehicle_proxy_policy", alter)

    def deny(*args, **kwargs):
        raise AssertionError("Policy validation must be first")

    monkeypatch.setattr(workflow, "download_cadastre_parcelles", deny)
    with pytest.raises(CadastreScreeningRunError):
        run_cadastre_screening(scan, with_roads=True)
    assert not (tmp_path / "outputs").exists()


@pytest.mark.parametrize("filename", ["road_proximity.csv", "run.json.part"])
def test_road_output_failures_preserve_incomplete_directory(
    tmp_path, monkeypatch, filename
):
    scan, _, _, _, _ = write_road_project(tmp_path)
    original = Path.open

    def fail(path, *args, **kwargs):
        if path.name == filename and args and "x" in args[0]:
            raise OSError("injected road write failure")
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", fail)
    output = tmp_path / "outputs/fail"
    with pytest.raises(CadastreScreeningRunError, match="incomplete output"):
        run_cadastre_screening(scan, with_roads=True, output_dir=output)
    assert output.is_dir() and not (output / "run.json").exists()


@pytest.mark.parametrize("flag", [None, 0, 1, "true"])
def test_road_flag_requires_exact_bool(tmp_path, flag):
    scan, _, _ = write_project(tmp_path)
    with pytest.raises(CadastreScreeningRunError, match="exact bool"):
        run_cadastre_screening(scan, with_roads=flag)


def test_policy_option_is_never_silently_ignored(tmp_path):
    scan, _, _ = write_project(tmp_path)
    with pytest.raises(CadastreScreeningRunError, match="requires with_roads"):
        run_cadastre_screening(scan, road_policy_path=Path("unused"))


@pytest.mark.parametrize(
    "column",
    [
        "nearest_road_proxy_distance_m",
        "nearest_carriageway_width_raw",
        "road_source_boundary_distance_m",
        "nearest_road_tie_count",
        "road_proxy_policy_schema_version",
    ],
)
@pytest.mark.parametrize(
    "value", [True, np.bool_(False), float("inf"), float("-inf"), "1"]
)
def test_road_numerics_do_not_coerce_bad_values(column, value):
    with pytest.raises(road.RoadScreeningError):
        road._scalar(value, column)


@pytest.mark.parametrize("value", [None, pd.NA, float("nan")])
def test_road_true_nulls_are_empty_not_zero(value):
    for column in road.ROAD_EXPORT_COLUMNS:
        assert road._scalar(value, column) is None


@pytest.mark.parametrize("value", [0, 1, "true", "False"])
def test_toll_evidence_never_coerces_non_bool(value):
    with pytest.raises(road.RoadScreeningError):
        road._scalar(value, "nearest_road_toll_evidence")


@pytest.mark.parametrize("branch", ["grid", "roads"])
@pytest.mark.parametrize(
    "mutation",
    [
        "value",
        "dtype",
        "geometry",
        "index",
        "attrs",
        "summary",
        "summary_type",
        "extraction",
        "lineage",
        "lineage_type",
    ],
)
def test_combined_final_checks_each_actual_coverage_bundle(
    tmp_path, monkeypatch, branch, mutation
):
    scan, _, _, _, _ = write_road_project(tmp_path)
    module = grid if branch == "grid" else road
    original = module.load_ign_bdtopo_department_coverage

    def alter(*args):
        fresh = original(*args)
        if mutation == "summary":
            return replace(
                fresh, summary=replace(fresh.summary, source_feature_count=100)
            )
        if mutation == "summary_type":
            return replace(fresh, summary=object())
        if mutation == "extraction":
            return replace(fresh, extraction=replace(fresh.extraction))
        if mutation == "lineage":
            return replace(fresh, source_archive_sha256="0" * 64)
        if mutation == "lineage_type":
            return replace(fresh, source_department_code=31)
        frame = fresh.coverage.copy(deep=True)
        if mutation == "value":
            frame.loc[0, "nom_officiel"] = "Changed"
        elif mutation == "dtype":
            frame["code_insee"] = frame.code_insee.astype(object)
        elif mutation == "geometry":
            frame.loc[0, "geometry"] = translate(frame.geometry.iloc[0], xoff=1)
        elif mutation == "index":
            frame.index = pd.Index(frame.index.tolist(), name="changed")
        else:
            frame.attrs["changed"] = True
        return replace(fresh, coverage=frame)

    monkeypatch.setattr(module, "load_ign_bdtopo_department_coverage", alter)
    output = tmp_path / "outputs/fail"
    with pytest.raises(CadastreScreeningRunError, match="incomplete output") as error:
        run_cadastre_screening(scan, with_roads=True, with_grid=True, output_dir=output)
    assert error.value.__cause__ is not None and not (output / "run.json").exists()


@pytest.mark.parametrize(
    "mutation",
    [
        "order",
        "missing",
        "duplicate",
        "extra",
        "column",
        "duplicate_column",
        "column_order",
        "index",
        "class_coverage",
        "count",
        "eligibility",
        "policy",
    ],
)
def test_table_domain_and_complete_schema_are_checked_before_export_sort(
    tmp_path, mutation
):
    _, run = _road_run(tmp_path)
    table = run.assessment.class_proximity.copy(deep=True)
    coverage = run.assessment.class_coverage
    if mutation == "order":
        table = table.iloc[::-1].reset_index(drop=True)
    elif mutation == "missing":
        table = table.iloc[1:].reset_index(drop=True)
    elif mutation == "duplicate":
        table.iloc[1] = table.iloc[0]
    elif mutation == "extra":
        table.loc[0, "parcel_id"] = "extra"
    elif mutation == "column":
        table = table.drop(columns="nearest_road_rule_trace_json")
    elif mutation == "duplicate_column":
        table.columns = [*table.columns[:-1], table.columns[0]]
    elif mutation == "column_order":
        table = table.iloc[:, ::-1]
    elif mutation == "index":
        table.index = pd.Index(table.index.tolist(), name="changed")
    elif mutation == "class_coverage":
        coverage = coverage[:-1]
    elif mutation == "count":
        coverage = (replace(coverage[0], feature_count=99), *coverage[1:])
    elif mutation == "eligibility":
        coverage = (replace(coverage[0], distance_eligible=False), *coverage[1:])
    else:
        table["road_proxy_policy_config_sha256"] = "0" * 64
    with pytest.raises(road.RoadScreeningError):
        road._road_records(
            replace(
                run,
                assessment=replace(
                    run.assessment, class_proximity=table, class_coverage=coverage
                ),
            )
        )


@pytest.mark.parametrize(
    "conflict",
    [
        "existing",
        "output_policy",
        "output_ign",
        "cache_policy",
        "extraction_policy",
        "policy_symlink",
        "policy_junction",
        "policy_parent_link",
        "output_junction",
        "cache_link",
        "extraction_junction",
    ],
)
def test_road_preflight_rejects_collisions_links_and_junctions_before_acquisition(
    tmp_path, monkeypatch, conflict
):
    scan, _, _, extraction, policy = write_road_project(tmp_path)
    output = tmp_path / "outputs/fail"
    kwargs = {"with_roads": True, "output_dir": output}
    unsafe = None
    method = "is_symlink"
    if conflict == "existing":
        output.mkdir(parents=True)
        (output / "keep.txt").write_text("preserve me", encoding="utf-8")
    elif conflict == "output_policy":
        kwargs["output_dir"] = policy
    elif conflict == "output_ign":
        kwargs["output_dir"] = tmp_path / "data/cache/ign_bdtopo/new-output"
    elif conflict in ("cache_policy", "extraction_policy"):
        kwargs[
            "ign_cache_dir" if conflict == "cache_policy" else "ign_extraction_dir"
        ] = policy.parent
    elif conflict.startswith("policy_"):
        unsafe = policy.parent if conflict == "policy_parent_link" else policy
        method = "is_junction" if conflict == "policy_junction" else "is_symlink"
    elif conflict == "output_junction":
        unsafe, method = output, "is_junction"
    elif conflict == "cache_link":
        unsafe = tmp_path / "data/cache/ign_bdtopo"
    else:
        unsafe, method = extraction.extraction_path, "is_junction"
        kwargs["ign_extraction_dir"] = unsafe
    before = {p: p.read_bytes() for p in tmp_path.rglob("*") if p.is_file()}
    if unsafe is not None:
        original = getattr(Path, method)
        monkeypatch.setattr(Path, method, lambda path: path == unsafe or original(path))

    def deny(*args, **kwargs):
        raise AssertionError("Preflight must precede acquisition")

    monkeypatch.setattr(workflow, "download_cadastre_parcelles", deny)
    with pytest.raises(CadastreScreeningRunError):
        run_cadastre_screening(scan, **kwargs)
    assert all(p.read_bytes() == raw for p, raw in before.items())


def test_public_chain_runs_once_with_no_private_normalization_bypass(
    tmp_path, monkeypatch
):
    import landscout.stages.apply_road_vehicle_proxy_policy as application
    import landscout.stages.enrich_road_proximity as proximity

    scan, _, _, _, _ = write_road_project(tmp_path)
    counts = {"apply": 0, "normalize": 0, "assess": 0}
    original_apply = proximity.apply_ign_road_vehicle_proxy_policy
    original_normalize = application.normalize_ign_roads
    original_assess = road.assess_road_proximity_coverage

    def apply(*args):
        counts["apply"] += 1
        return original_apply(*args)

    def normalize(*args):
        counts["normalize"] += 1
        return original_normalize(*args)

    def assess(*args):
        counts["assess"] += 1
        return original_assess(*args)

    monkeypatch.setattr(proximity, "apply_ign_road_vehicle_proxy_policy", apply)
    monkeypatch.setattr(application, "normalize_ign_roads", normalize)
    monkeypatch.setattr(road, "assess_road_proximity_coverage", assess)
    result = run_cadastre_screening(scan, with_roads=True)
    assert result.roads_status == "COMPLETE" and counts == {
        "apply": 1,
        "normalize": 1,
        "assess": 1,
    }


def test_csv_reread_checks_non_id_cells_not_only_identifiers(tmp_path, monkeypatch):
    scan, _, _, _, _ = write_road_project(tmp_path)
    original = road.csv.DictWriter.writerows

    def changed(writer, rows):
        if "nearest_road_toll_evidence" in writer.fieldnames:
            rows = [dict(row) for row in rows]
            rows[0]["nearest_road_toll_evidence"] = "false"
        return original(writer, rows)

    monkeypatch.setattr(road.csv.DictWriter, "writerows", changed)
    output = tmp_path / "outputs/fail"
    with pytest.raises(CadastreScreeningRunError, match="Written road table"):
        run_cadastre_screening(scan, with_roads=True, output_dir=output)
    assert not (output / "run.json").exists()


@pytest.mark.parametrize("electric_variant", ["no_lines", "no_posts"])
def test_roads_can_complete_with_unusable_electric_geometry(tmp_path, electric_variant):
    scan, _, _, _, _ = write_road_project(tmp_path, coverage=electric_variant)
    result = run_cadastre_screening(scan, with_roads=True)
    assert (
        result.roads_status == "COMPLETE"
        and len(read_csv(result.road_proximity_csv)) == 10
    )
    output = tmp_path / "outputs/combined-fail"
    with pytest.raises(CadastreScreeningRunError):
        run_cadastre_screening(scan, with_grid=True, with_roads=True, output_dir=output)
    assert not (output / "run.json").exists()


def test_empty_classes_keep_no_match_distinct_from_outside_position(tmp_path):
    scan, _, _, _, _ = write_road_project(tmp_path, "empty_classes", "touch")
    result = run_cadastre_screening(scan, with_roads=True)
    first = [
        r
        for r in read_csv(result.road_proximity_csv)
        if r["parcel_id"].endswith("0001")
    ]
    assert all(
        r["road_source_coverage_position"] == "OUTSIDE_OR_CROSSING_COVERAGE"
        for r in first
    )
    assert first[0]["road_proximity_coverage_status"] == "OUTSIDE_OR_CROSSING_COVERAGE"
    assert all(r["road_proximity_coverage_status"] == "NO_MATCH" for r in first[1:])


def test_all_not_distance_is_an_executed_workflow_not_not_run(tmp_path):
    scan, _, _, _, _ = write_road_project(tmp_path, "all_not_distance")
    result = run_cadastre_screening(scan, with_roads=True)
    manifest = json.loads(result.manifest_path.read_bytes())
    assert result.roads_status == manifest["roads"]["status"] == "COMPLETE"
    assert len(read_csv(result.road_proximity_csv)) == 10
    assert all(
        row["road_proximity_coverage_status"] == "NO_MATCH"
        for row in read_csv(result.road_proximity_csv)
    )
