# `tests/unit/test_inpn_protected_areas_attributes_fr.py`

## File identity

- Repository path: `tests/unit/test_inpn_protected_areas_attributes_fr.py`
- File type: Python unit/regression tests
- Domain: isolated INPN EP source-bound attribute profile evidence
- Source SHA256: `3c7605e5017eb94536e8a8a6da90fe9000b62495d92434298934c6c18a4bf154`
- Collected cases: `130`

## 1. Isolation and fixture architecture

All source fixtures are synthetic ZIP/GPKG bytes built under Pytest's unique temporary directory. `_spatial_frame` and `_gpkg_bytes` use geometry only to create valid fixture containers; production reads are intercepted as exact pandas DataFrames and are separately guarded against geometry-bearing results. `_source_from_package` replaces `source_module.open_safe_https` with an in-memory `_Response`, so tests perform no live DNS or HTTP. No real EP cache or archive is changed.

## 2. Every import

```python
from __future__ import annotations

import io
import warnings
import zipfile
from collections.abc import Mapping
from contextlib import contextmanager
from dataclasses import FrozenInstanceError, fields, is_dataclass, replace
from datetime import UTC, date, datetime
from hashlib import sha256
from pathlib import Path
from typing import Any, ClassVar

import geopandas as gpd  # type: ignore[import-untyped]
import numpy as np
import pandas as pd  # type: ignore[import-untyped]
import pyogrio  # type: ignore[import-untyped]
import pytest
import yaml
from pandas.testing import assert_frame_equal
from shapely.geometry import Point  # type: ignore[import-untyped]

from landscout import sources
from landscout.sources import inpn_protected_areas_attributes_fr as attributes
from landscout.sources import inpn_protected_areas_catalog_fr as catalog_module
from landscout.sources import inpn_protected_areas_fr as source_module
from landscout.sources.inpn_protected_areas_attributes_fr import (
    ATTRIBUTE_PROFILE_SCHEMA_VERSION,
    InpnProtectedAreasAttributeProfile,
    InpnProtectedAreasAttributeProfileError,
    InpnProtectedAreasDistinctAttributeValue,
    InpnProtectedAreasFieldAttributeProfile,
    InpnProtectedAreasLayerAttributeProfile,
    build_inpn_protected_areas_attribute_profile,
    validate_inpn_protected_areas_attribute_profile,
)
from landscout.sources.inpn_protected_areas_catalog_fr import (
    InpnProtectedAreasCatalog,
    build_inpn_protected_areas_catalog,
)
from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    download_inpn_protected_areas_archive,
    extract_inpn_protected_areas_archive,
)
```

Standard-library imports build deterministic ZIP bytes, inspect immutable dataclasses, hash payloads, and type test doubles. GeoPandas/Shapely create fixture GPKGs; NumPy/Pandas exercise scalar/dtype/FID cases; Pyogrio names forbidden geometry readers; Pytest provides parametrization, temporary paths, warnings, and monkeypatching. Imports from `landscout.sources`, the attribute module, catalog module, and source module exercise both public ownership and private adversarial seams.

## 3. Support classes

- `_Response(io.BytesIO)` is the minimal closable response body consumed by the download adapter.
- `_ArbitraryObject` supplies an unsupported object cell to prove fail-closed scalar handling.
- `_StringSubclass(str)` is comparison-equal to canonical text but proves exact built-in runtime-type enforcement.

`CONFIG_PATH` identifies the checked-in source configuration used for provenance comparison, `EXPECTED_EXPORTS` fixes the exact seven-name public boundary, and `KNOWN_BYTES_GPKG_WARNING` supplies the one precise warning string accepted by the scoped suppression regression. Production warning tests install exact warning expectations; there is no global warning filter.

## 4. Every fixture/helper

| Helper | Exact signature | Role |
|---|---|---|
| `_response` | `def _response(payload: bytes) -> Any` | Wraps ZIP bytes in the minimal HTTP-like response object expected by the source adapter. |
| `_spatial_frame` | `def _spatial_frame( values: tuple[str, ...] = (" alpha ", "béta"), *, field_names: tuple[str, str] = ("text", "number"), ) -> gpd.GeoDataFrame` | Creates a tiny projected GeoDataFrame solely for writing synthetic source fixtures; production profiling never receives it. |
| `_gpkg_bytes` | `def _gpkg_bytes( tmp_path: Path, frame: pd.DataFrame, *, filename: str = "build.gpkg", layer_name: str = "physical_layer", ) -> bytes` | Writes a temporary GPKG fixture with selected layers and returns exact file bytes. |
| `_zip_bytes` | `def _zip_bytes(files: Mapping[str, bytes]) -> bytes` | Creates deterministic in-memory EP ZIP bytes from an ordered member mapping. |
| `_config` | `def _config(tmp_path: Path, archive: bytes) -> InpnProtectedAreasSourceConfig` | Constructs a strict local source config pinned to the synthetic archive size/SHA. |
| `_source_from_package` | `def _source_from_package( tmp_path: Path, monkeypatch: pytest.MonkeyPatch, package: bytes, *, relative_path: str = "EP/one.gpkg", ) -> tuple[ InpnProtectedAreasSourceConfig, InpnProtectedAreasExtraction, InpnProtectedAreasCatalog, ]` | Mocks safe HTTPS once, downloads/extracts the synthetic archive, and builds its physical catalog. |
| `_source` | `def _source( tmp_path: Path, monkeypatch: pytest.MonkeyPatch, *, values: tuple[str, ...] = (" alpha ", "béta"), field_names: tuple[str, str] = ("text", "number"), ) -> tuple[ InpnProtectedAreasSourceConfig, InpnProtectedAreasExtraction, InpnProtectedAreasCatalog, ]` | Convenience builder for a one-package/one-layer verified extraction/config/catalog triple. |
| `_frame_for` | `def _frame_for( catalog: InpnProtectedAreasCatalog, values: list[object], *, fids: list[object] | None = None, ) -> pd.DataFrame` | Creates the exact pandas attribute frame and named FID index expected for a catalog layer. |
| `_build_with_frame` | `def _build_with_frame( monkeypatch: pytest.MonkeyPatch, config: InpnProtectedAreasSourceConfig, extraction: InpnProtectedAreasExtraction, catalog: InpnProtectedAreasCatalog, frame: pd.DataFrame, ) -> InpnProtectedAreasAttributeProfile` | Monkeypatches only `attributes.pyogrio.read_dataframe` and invokes the public profile builder. |
| `_profile_with_hash` | `def _profile_with_hash( profile: InpnProtectedAreasAttributeProfile, ) -> InpnProtectedAreasAttributeProfile` | Recomputes the private canonical complete hash after a deliberate immutable-record replacement for adversarial tests. |
| `_catalog_with_hash` | `def _catalog_with_hash(catalog: InpnProtectedAreasCatalog) -> InpnProtectedAreasCatalog` | Recomputes the canonical catalog hash after a deliberate package-path replacement so cross-layer parity reaches intrinsic grammar validation. |
| `_intrinsic_field` | `def _intrinsic_field( name: str, position: int, *, feature_count: int = 2, source_dtype: str = "object", runtime_dtype: str = "object", ) -> InpnProtectedAreasFieldAttributeProfile` | Constructs one internally coherent non-empty or empty immutable field record for fast intrinsic-only adversarial profiles; empty column hashes use the production canonical helper. |
| `_intrinsic_layer` | `def _intrinsic_layer( *, relative_path: str = "EP/one.gpkg", package_position: int = 0, layer_name: str = "physical_layer", layer_position: int = 0, file_size: int = 100, file_sha256: str = "2" * 64, feature_count: int = 2, fid_min: int | None = 1, fid_max: int | None = 2, fields: tuple[InpnProtectedAreasFieldAttributeProfile, ...] | None = None, ) -> InpnProtectedAreasLayerAttributeProfile` | Constructs coherent package/layer/FID evidence, including production-derived empty FID, row, and column hashes, without physical I/O. |
| `_intrinsic_profile` | `def _intrinsic_profile( *layers: InpnProtectedAreasLayerAttributeProfile, ) -> InpnProtectedAreasAttributeProfile` | Wraps intrinsic layers in a source/catalog envelope, derives every aggregate, and recalculates the complete profile hash so each mutation isolates the intended structural contract. |
| `_first_field` | `def _first_field( profile: InpnProtectedAreasAttributeProfile, ) -> InpnProtectedAreasFieldAttributeProfile` | Selects the first immutable layer/field profile for concise assertions. |

Synthetic GPKGs deliberately cover one and multiple packages/layers, ordered field schemas, empty layers, geometry-like attribute names, catalog dtype/runtime dtype differences, sparse/unsorted FIDs, and content mutation. They are construction inputs only and never weaken production's immutable byte or no-geometry contracts.

## 5. Monkeypatch inventory

- `source_module.open_safe_https` is replaced only by deterministic in-memory archive responses; this isolates DNS/HTTP.
- `attributes.pyogrio.read_dataframe` is replaced by exact DataFrames, recording wrappers, warning emitters, or deliberate TOCTOU mutations. Recording assertions prove bytes identity and the six required reader options.
- `gpd.read_file`, `gpd.read_parquet`, `pyogrio.read_arrow`, `pyogrio.open_arrow`, and `pyogrio.read_bounds` are replaced by fatal sentinels in the no-geometry regression.
- Selected tests make `read_dataframe` fatal to prove malformed extraction/catalog/package evidence is rejected before any attribute read.
- Temporary/persistent package mutation hooks operate only inside per-test temporary extraction roots and prove immutable byte isolation plus final postcondition rejection.

## 6. Every test and parametrization

| Test function | Parametrization/decorators | Protected regression |
|---|---|---|
| `test_valid_source_complete_attribute_profile_and_validation` | none | Builds and independently validates a complete two-field profile and asserts source lineage, aggregates, exact domain/frequency evidence, and hashes. |
| `test_wrong_public_input_types_are_controlled` | `pytest.mark.parametrize(<br>    ("argument", "value"),<br>    [("extraction", object()), ("config", object()), ("catalog", object())],<br>)` | Parametrically substitutes wrong extraction, config, and catalog objects and requires the controlled application error. |
| `test_catalog_from_another_source_or_config_is_rejected` | none | Proves a catalog bound to other verified bytes/config cannot authorize profiling. |
| `test_schema_one_catalog_is_rejected_before_attribute_read` | none | Downgrades catalog schema and proves rejection occurs before Pyogrio can materialize attributes. |
| `test_coordinated_catalog_and_hash_mutation_is_rejected_before_attribute_read` | none | Rehashes a forged catalog and proves independent physical catalog reconstruction defeats coordinated metadata/hash tampering before the attribute call. |
| `test_modified_package_is_rejected_before_attribute_read` | none | Mutates extracted package bytes and proves archive/package identity fails before feature attributes are read. |
| `test_reader_receives_exact_bytes_layer_fields_and_options` | none | Captures the production reader call and asserts the identical built-in bytes snapshot, layer, ordered columns, read_geometry=False, fid_as_index=True, use_arrow=False, and datetime_as_string=True. |
| `test_every_package_and_layer_uses_one_verified_byte_snapshot` | none | Uses multiple packages/layers and identity-sensitive wrappers to prove each layer read uses its package's one immutable verified snapshot. |
| `test_no_geometry_reader_or_geodataframe_is_used` | none | Makes GeoPandas and Pyogrio geometry/Arrow/bounds APIs fatal and proves the approved DataFrame-only path succeeds. |
| `test_geometry_like_attribute_names_are_preserved` | none | Proves attribute columns whose names resemble geometry are retained when their values and dtype are non-geometric. |
| `test_known_warning_is_narrowly_suppressed_for_attribute_read` | none | Emits the exact bytes-backed GPKG extension warning and proves only that known warning is locally suppressed. |
| `test_unrelated_runtime_warning_remains_observable` | none | Emits a different RuntimeWarning and proves it remains visible. |
| `test_geometry_bearing_reader_results_are_rejected` | `pytest.mark.parametrize("kind", ["geodataframe", "geometry-dtype", "shapely-cell"])` | Parametrically returns a GeoDataFrame, GeometryDtype frame, or Shapely cell and requires fail-closed rejection. |
| `test_attribute_columns_must_equal_catalog_order` | `pytest.mark.parametrize("mutation", ["missing", "extra", "reordered", "duplicate"])` | Parametrically supplies missing, extra, reordered, or duplicate columns and proves exact catalog order is mandatory. |
| `test_row_count_must_equal_catalog_feature_count` | none | Makes the returned frame length disagree with physical metadata and requires rejection. |
| `test_invalid_fids_are_rejected` | `pytest.mark.parametrize(<br>    ("fids", "message"),<br>    [<br>        ([1, 1], "duplicate"),<br>        ([1, None], "non-integral&#124;null"),<br>        ([1, True], "Boolean"),<br>        ([1, 2.5], "non-integral"),<br>    ],<br>)` | Parametrically covers Boolean, float, null, duplicate, and otherwise non-integral FID index values. |
| `test_multiindex_is_rejected` | none | Proves a multi-level index cannot masquerade as the required physical FID sequence. |
| `test_noncontiguous_unsorted_fids_are_canonicalized_without_renumbering` | none | Proves valid sparse/unsorted identifiers are sorted for hashing but retain their exact numeric identities. |
| `test_empty_layer_has_empty_deterministic_fid_evidence` | none | Proves an empty physical layer yields null extrema and stable empty FID/row hashes. |
| `test_supported_values_have_exact_canonical_domains` | `pytest.mark.parametrize(<br>    ("values", "kind", "canonical"),<br>    [<br>        (["  text  ", ""], "TEXT", ["", "  text  "]),<br>        (["école", "ÉCOLE"], "TEXT", ["ÉCOLE", "école"]),<br>        ([True, np.bool_(False)], "BOOLEAN", ["false", "true"]),<br>        ([1, np.int64(-2)], "INTEGER", ["-2", "1"]),<br>        ([1.5, np.float64(-0.0)], "FLOAT_HEX", ["-0x0.0p+0", "0x1.8000000000000p+0"]),<br>        ([b"\x00\xff", b""], "BINARY_BASE64", ["", "AP8="]),<br>    ],<br>)` | Parametrically proves canonical TEXT, BOOLEAN, INTEGER, FLOAT_HEX, and BINARY_BASE64 values and exact frequencies. |
| `test_numpy_string_scalar_is_normalized_to_exact_text` | none | Proves NumPy string scalars normalize to portable built-in TEXT without retaining the NumPy object. |
| `test_source_and_runtime_dtypes_are_recorded_separately` | none | Proves physical catalog dtype and actual DataFrame dtype are retained as distinct factual fields. |
| `test_null_scalars_are_counted_separately` | `pytest.mark.parametrize("null_value", [None, float("nan"), pd.NA, pd.NaT])` | Parametrically covers None, NaN, pd.NA, and pd.NaT and proves nulls never enter distinct non-null domains. |
| `test_nonfinite_nonnull_numbers_are_rejected` | `pytest.mark.parametrize("value", [float("inf"), float("-inf")])` | Parametrically rejects positive and negative infinity instead of emitting noncanonical JSON. |
| `test_unsupported_or_mutable_values_are_rejected` | `pytest.mark.parametrize(<br>    "value",<br>    [bytearray(b"x"), [1], (1,), {"x": 1}, {1}, frozenset({1}), _ArbitraryObject()],<br>)` | Parametrically rejects bytearray, list, tuple, dictionary, set, frozenset, and arbitrary-object cells. |
| `test_temporal_objects_are_rejected_because_reader_requires_text` | `pytest.mark.parametrize(<br>    "value",<br>    [<br>        datetime(2026, 7, 1, tzinfo=UTC),<br>        date(2026, 7, 1),<br>        pd.Timestamp("2026-07-01"),<br>    ],<br>)` | Parametrically rejects datetime/date/Timestamp scalars because datetime_as_string requires temporal source values to arrive as text. |
| `test_all_distinct_values_and_exact_frequencies_are_retained_and_sorted` | none | Proves domains are complete, frequency exact, and ordered by value-kind then canonical text rather than encounter order. |
| `test_reader_frame_is_not_mutated` | none | Deep-compares the fake reader frame before and after profiling. |
| `test_repeated_build_and_portable_cache_roots_are_deterministic` | none | Proves identical bytes under different absolute cache roots produce equal portable evidence and hashes. |
| `test_cache_hit_state_does_not_affect_profile_hash` | none | Proves cache-hit flags are operational metadata excluded from portable profile identity. |
| `test_content_mutations_change_component_and_profile_hashes` | `pytest.mark.parametrize("mutation", ["text", "fid", "frequency", "null"])` | Parametrically changes text, FID, frequency, or null content and proves the relevant component plus complete hashes change. |
| `test_field_order_change_changes_profile_hash` | none | Proves ordered schema position is hash-significant. |
| `test_coordinated_profile_and_hash_mutation_fails_independent_rebuild` | none | Recalculates a forged complete profile hash and proves public validation rejects it after physical rebuild. |
| `test_intrinsic_validator_rejects_malformed_profile` | `pytest.mark.parametrize(<br>    "mutation", ["aggregate", "nested-list", "bad-kind", "bad-hash"]<br>)` | Covers exactly aggregate-count mismatch, a mutable nested list, an unsupported value kind, and a malformed complete-profile hash. Package/layer lineage and ordering are covered by the dedicated regressions below. |
| `test_intrinsic_validator_rejects_comparison_equal_string_subclass` | none | Proves a comparison-equal str subclass cannot cross exact canonical runtime-type validation. |
| `test_intrinsic_rejects_noncanonical_package_paths` | seven paths: leading whitespace, trailing whitespace, POSIX absolute, Windows drive, traversal, backslash alias, and wrong suffix | Recalculates each complete hash and rejects every noncanonical package path intrinsically. |
| `test_intrinsic_attribute_package_path_uses_authoritative_grammar` | the 11-case shared path corpus | Proves profile intrinsic validation uses the extraction grammar, accepts valid nested `.gpkg`/`.GPKG` paths unchanged, and chains controlled source/path causes for every rejection. |
| `test_package_path_decisions_match_extraction_catalog_and_attribute_layers` | the 11-case shared path corpus | Runs every row through extraction, catalog, and profile validators and requires the three decisions to equal the single expected result. |
| `test_intrinsic_rejects_one_package_path_under_two_positions` | none | Rejects a non-bijective exact package path reused under two positions. |
| `test_intrinsic_rejects_exact_duplicate_package_paths` | none | Permanently and explicitly locks rejection of an exact duplicate package path. |
| `test_intrinsic_rejects_package_identity_collisions` | exact casefold-equivalent pair and Unicode-NFKC-equivalent pair | Rejects package identities that collide after casefold or NFKC normalization. |
| `test_intrinsic_rejects_nonlexical_package_order` | none | Rejects contiguous positions whose exact package paths are not lexically ordered. |
| `test_intrinsic_rejects_inconsistent_repeated_package_metadata` | `file_size`, `file_sha256` | Rejects contradictory size or SHA evidence repeated by two layers of one package. |
| `test_intrinsic_rejects_noncanonical_layer_positions` | duplicate `(0, 0)`, gap `(0, 2)`, and out-of-order `(1, 0)` | Requires exact contiguous zero-based layer positions in flattened package order. |
| `test_intrinsic_rejects_noncontiguous_package_groups` | none | Rejects a package whose layers resume after a different package group begins. |
| `test_intrinsic_rejects_layer_identity_collisions` | exact duplicate, casefold-equivalent, and Unicode-NFKC-equivalent names | Rejects all three layer-identity collision forms within one package. |
| `test_intrinsic_rejects_layer_name_edge_whitespace` | none | Rejects noncanonical layer identity text with edge whitespace. |
| `test_intrinsic_rejects_field_identity_collisions` | exact duplicate, casefold-equivalent, and Unicode-NFKC-equivalent names | Rejects all three ordered field-identity collision forms within one layer. |
| `test_intrinsic_rejects_field_name_edge_whitespace` | none | Rejects noncanonical field identity text with edge whitespace. |
| `test_intrinsic_rejects_dtype_edge_whitespace` | `source`, `runtime` | Rejects edge whitespace independently in source and runtime dtype metadata. |
| `test_intrinsic_rejects_single_row_fid_extrema_mismatch` | none | Requires one FID to have equal minimum and maximum evidence. |
| `test_intrinsic_rejects_impossible_multirow_fid_ranges` | equal extrema and reversed extrema | Requires multiple FIDs to have a strict increasing range with adequate integer capacity. |
| `test_intrinsic_accepts_sparse_fid_range` | none | Preserves valid sparse FID support; two FIDs spanning 1 through 10 remain intrinsic-valid. |
| `test_intrinsic_rejects_fid_count_exceeding_range_capacity` | none | Directly rejects `fid_count=3`, `fid_min=1`, `fid_max=2` as impossible inclusive capacity. |
| `test_intrinsic_accepts_sparse_fid_range_with_capacity` | none | Directly accepts sparse `fid_count=3`, `fid_min=1`, `fid_max=4`. |
| `test_intrinsic_rejects_different_paths_for_one_package_position` | none | Rejects two different exact package paths claiming one package position. |
| `test_intrinsic_rejects_malformed_empty_component_hashes` | `fid`, `row`, `column` | Independently recalculates the complete hash and rejects each wrong deterministically recomputable empty component hash. |
| `test_public_validator_rejects_catalog_mismatch_before_attribute_read` | top-level source, source-catalog SHA, package evidence, layer identity, and field source dtype | Builds a valid physical source/profile, coherently forges one cheap catalog-bound fact, makes `read_dataframe` fatal, and proves all five mismatches fail with zero attribute calls. |
| `test_public_validator_valid_profile_reaches_attribute_rebuild` | none | Wraps the real attribute reader and proves a valid profile reaches and passes the independent one-read-per-layer rebuild. |
| `test_public_validator_rejects_wrong_profile_type_before_physical_rebuild` | none | Proves exact profile type is checked before physical work. |
| `test_temporary_package_path_swap_cannot_inject_other_attributes` | none | Swaps live package path content during inspection and proves immutable already-verified bytes prevent attribute injection. |
| `test_persistent_package_mutation_fails_final_source_revalidation` | none | Mutates package storage after the read and proves the final extraction postcondition rejects the result. |
| `test_profile_contains_no_frame_or_geometry_object` | none | Recursively audits returned evidence and proves it retains no DataFrame, GeoDataFrame, GeometryDtype, or geometry instance. |
| `test_public_api_exports_only_profile_boundary` | none | Asserts the package and module expose only the approved records, controlled error, builder, and validator rather than internal byte/frame helpers. |
| `test_profile_models_are_frozen_factual_records` | none | Proves all four public profile records are frozen dataclasses and reject field reassignment. |

The decorators above are the exact source declarations, including every parameter value and generated case. The file collects 130 cases; no existing INPN test is replaced.

## 7. Boundary and change impact

The suite proves a factual attribute profiler, not environmental policy. It asserts no EP category meaning, legal effect, Natura 2000/ZNIEFF mapping, geometry load, parcel relation, exclusion, score, or rank. Any source change requires this 130-case suite plus the existing 269 INPN source/catalog cases, independent real-cache verification, full repository tests, quality gates, and companion SHA synchronization.

## 8. Exact complete current file content

```python
from __future__ import annotations

import io
import warnings
import zipfile
from collections.abc import Mapping
from contextlib import contextmanager
from dataclasses import FrozenInstanceError, fields, is_dataclass, replace
from datetime import UTC, date, datetime
from hashlib import sha256
from pathlib import Path
from typing import Any, ClassVar

import geopandas as gpd  # type: ignore[import-untyped]
import numpy as np
import pandas as pd  # type: ignore[import-untyped]
import pyogrio  # type: ignore[import-untyped]
import pytest
import yaml
from pandas.testing import assert_frame_equal
from shapely.geometry import Point  # type: ignore[import-untyped]

from landscout import sources
from landscout.sources import inpn_protected_areas_attributes_fr as attributes
from landscout.sources import inpn_protected_areas_catalog_fr as catalog_module
from landscout.sources import inpn_protected_areas_fr as source_module
from landscout.sources.inpn_protected_areas_attributes_fr import (
    ATTRIBUTE_PROFILE_SCHEMA_VERSION,
    InpnProtectedAreasAttributeProfile,
    InpnProtectedAreasAttributeProfileError,
    InpnProtectedAreasDistinctAttributeValue,
    InpnProtectedAreasFieldAttributeProfile,
    InpnProtectedAreasLayerAttributeProfile,
    build_inpn_protected_areas_attribute_profile,
    validate_inpn_protected_areas_attribute_profile,
)
from landscout.sources.inpn_protected_areas_catalog_fr import (
    InpnProtectedAreasCatalog,
    build_inpn_protected_areas_catalog,
)
from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    download_inpn_protected_areas_archive,
    extract_inpn_protected_areas_archive,
)

CONFIG_PATH = Path("configs/sources/inpn_protected_areas_fr.yaml")
EXPECTED_EXPORTS = {
    "InpnProtectedAreasAttributeProfile",
    "InpnProtectedAreasAttributeProfileError",
    "InpnProtectedAreasDistinctAttributeValue",
    "InpnProtectedAreasFieldAttributeProfile",
    "InpnProtectedAreasLayerAttributeProfile",
    "build_inpn_protected_areas_attribute_profile",
    "validate_inpn_protected_areas_attribute_profile",
}
KNOWN_BYTES_GPKG_WARNING = (
    "File /vsimem/pyogrio_deadbeef has GPKG application_id, "
    "but non conformant file extension"
)
PACKAGE_PATH_GRAMMAR_CASES = (
    ("EP/CON.gpkg", False),
    ("EP/NUL.gpkg", False),
    ("EP/a:b.gpkg", False),
    ("EP/dir /one.gpkg", False),
    ("EP/ dir/one.gpkg", False),
    ("EP/dir./one.gpkg", False),
    ("EP/control\x01.gpkg", False),
    ("EP/ＮＵＬ.gpkg", False),
    ("EP/dir／one.gpkg", False),
    ("EP/subdir/one.gpkg", True),
    ("EP/subdir/one.GPKG", True),
)


class _Response(io.BytesIO):
    headers: ClassVar[dict[str, str]] = {"Content-Type": "application/zip"}


class _ArbitraryObject:
    pass


class _StringSubclass(str):
    pass


@contextmanager
def _response(payload: bytes) -> Any:
    response = _Response(payload)
    try:
        yield response
    finally:
        response.close()


def _spatial_frame(
    values: tuple[str, ...] = (" alpha ", "béta"),
    *,
    field_names: tuple[str, str] = ("text", "number"),
) -> gpd.GeoDataFrame:
    size = len(values)
    return gpd.GeoDataFrame(
        {
            field_names[0]: pd.Series(values, dtype="object"),
            field_names[1]: pd.Series(range(size), dtype="int64"),
        },
        geometry=gpd.GeoSeries(
            [Point(1000.0 + index, 2000.0 + index) for index in range(size)],
            crs="EPSG:2154",
        ),
        crs="EPSG:2154",
    )


def _gpkg_bytes(
    tmp_path: Path,
    frame: pd.DataFrame,
    *,
    filename: str = "build.gpkg",
    layer_name: str = "physical_layer",
) -> bytes:
    path = tmp_path / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    pyogrio.write_dataframe(frame, path, layer=layer_name, driver="GPKG")
    return path.read_bytes()


def _zip_bytes(files: Mapping[str, bytes]) -> bytes:
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w", compression=zipfile.ZIP_STORED) as archive:
        for name, payload in files.items():
            info = zipfile.ZipInfo(name, date_time=(2026, 7, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_STORED
            archive.writestr(info, payload)
    return stream.getvalue()


def _config(tmp_path: Path, archive: bytes) -> InpnProtectedAreasSourceConfig:
    payload = yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))
    assert isinstance(payload, dict)
    payload["cache_root"] = str(tmp_path / "cache")
    payload["expected_archive_size_bytes"] = len(archive)
    payload["expected_archive_sha256"] = sha256(archive).hexdigest()
    return InpnProtectedAreasSourceConfig.model_validate(payload)


def _source_from_package(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    package: bytes,
    *,
    relative_path: str = "EP/one.gpkg",
) -> tuple[
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasCatalog,
]:
    archive = _zip_bytes({relative_path: package})
    config = _config(tmp_path, archive)

    def fake_open(*args: object, **kwargs: object) -> Any:
        return _response(archive)

    monkeypatch.setattr(source_module, "open_safe_https", fake_open)
    download = download_inpn_protected_areas_archive(config)
    extraction = extract_inpn_protected_areas_archive(download, config)
    catalog = build_inpn_protected_areas_catalog(extraction, config)
    return config, extraction, catalog


def _source(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    *,
    values: tuple[str, ...] = (" alpha ", "béta"),
    field_names: tuple[str, str] = ("text", "number"),
) -> tuple[
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasCatalog,
]:
    package = _gpkg_bytes(
        tmp_path,
        _spatial_frame(values, field_names=field_names),
    )
    return _source_from_package(tmp_path, monkeypatch, package)


def _frame_for(
    catalog: InpnProtectedAreasCatalog,
    values: list[object],
    *,
    fids: list[object] | None = None,
) -> pd.DataFrame:
    names = [field.name for field in catalog.packages[0].layers[0].fields]
    frame = pd.DataFrame(
        {
            names[0]: pd.Series(values, dtype="object"),
            names[1]: pd.Series(range(len(values)), dtype="int64"),
        }
    )
    if fids is not None:
        frame.index = pd.Index(fids, dtype="object")
    else:
        frame.index = pd.Index(range(1, len(values) + 1), dtype="int64")
    return frame


def _build_with_frame(
    monkeypatch: pytest.MonkeyPatch,
    config: InpnProtectedAreasSourceConfig,
    extraction: InpnProtectedAreasExtraction,
    catalog: InpnProtectedAreasCatalog,
    frame: pd.DataFrame,
) -> InpnProtectedAreasAttributeProfile:
    monkeypatch.setattr(attributes.pyogrio, "read_dataframe", lambda *a, **k: frame)
    return build_inpn_protected_areas_attribute_profile(extraction, config, catalog)


def _profile_with_hash(
    profile: InpnProtectedAreasAttributeProfile,
) -> InpnProtectedAreasAttributeProfile:
    blank = replace(profile, complete_attribute_profile_content_sha256="")
    return replace(
        blank,
        complete_attribute_profile_content_sha256=attributes._profile_content_sha256(
            blank
        ),
    )


def _catalog_with_hash(catalog: InpnProtectedAreasCatalog) -> InpnProtectedAreasCatalog:
    blank = replace(catalog, complete_catalog_content_sha256="")
    return replace(
        blank,
        complete_catalog_content_sha256=catalog_module._catalog_content_sha256(blank),
    )


def _intrinsic_field(
    name: str,
    position: int,
    *,
    feature_count: int = 2,
    source_dtype: str = "object",
    runtime_dtype: str = "object",
) -> InpnProtectedAreasFieldAttributeProfile:
    distinct_values = (
        (InpnProtectedAreasDistinctAttributeValue("TEXT", "x", feature_count),)
        if feature_count
        else ()
    )
    column_hash = (
        attributes._canonical_json_sha256([], "empty test column")
        if feature_count == 0
        else "1" * 64
    )
    return InpnProtectedAreasFieldAttributeProfile(
        name=name,
        position=position,
        source_dtype=source_dtype,
        runtime_dtype=runtime_dtype,
        null_count=0,
        non_null_count=feature_count,
        distinct_non_null_count=len(distinct_values),
        distinct_values=distinct_values,
        column_content_sha256=column_hash,
    )


def _intrinsic_layer(
    *,
    relative_path: str = "EP/one.gpkg",
    package_position: int = 0,
    layer_name: str = "physical_layer",
    layer_position: int = 0,
    file_size: int = 100,
    file_sha256: str = "2" * 64,
    feature_count: int = 2,
    fid_min: int | None = 1,
    fid_max: int | None = 2,
    fields: tuple[InpnProtectedAreasFieldAttributeProfile, ...] | None = None,
) -> InpnProtectedAreasLayerAttributeProfile:
    selected_fields = fields or (
        _intrinsic_field("text", 0, feature_count=feature_count),
        _intrinsic_field("number", 1, feature_count=feature_count),
    )
    if feature_count == 0:
        fid_min = None
        fid_max = None
    return InpnProtectedAreasLayerAttributeProfile(
        relative_path=relative_path,
        file_size=file_size,
        file_sha256=file_sha256,
        package_position=package_position,
        driver_name="GPKG",
        layer_name=layer_name,
        layer_position=layer_position,
        feature_count=feature_count,
        fid_count=feature_count,
        fid_min=fid_min,
        fid_max=fid_max,
        fid_sequence_sha256=(
            attributes._canonical_json_sha256([], "empty test FIDs")
            if feature_count == 0
            else "3" * 64
        ),
        row_content_sha256=(
            attributes._canonical_json_sha256(
                {
                    "fields": [field.name for field in selected_fields],
                    "rows": [],
                },
                "empty test rows",
            )
            if feature_count == 0
            else "4" * 64
        ),
        fields=selected_fields,
    )


def _intrinsic_profile(
    *layers: InpnProtectedAreasLayerAttributeProfile,
) -> InpnProtectedAreasAttributeProfile:
    selected_layers = layers or (_intrinsic_layer(),)
    profile = InpnProtectedAreasAttributeProfile(
        attribute_profile_schema_version=ATTRIBUTE_PROFILE_SCHEMA_VERSION,
        provider="PatriNat",
        authority="MNHN",
        program="INPN",
        dataset_id="EP",
        dataset_name="Protected areas",
        declared_version="07/2026",
        reference_page_url="https://example.com/reference",
        archive_url="https://example.com/EP.zip",
        archive_filename="EP.zip",
        archive_size=1_000,
        archive_sha256="5" * 64,
        source_catalog_schema_version=catalog_module.CATALOG_HASH_SCHEMA_VERSION,
        source_catalog_content_sha256="6" * 64,
        layers=selected_layers,
        package_count=len({layer.package_position for layer in selected_layers}),
        layer_count=len(selected_layers),
        field_definition_count=sum(len(layer.fields) for layer in selected_layers),
        total_row_count=sum(layer.feature_count for layer in selected_layers),
        total_null_count=sum(
            field.null_count for layer in selected_layers for field in layer.fields
        ),
        total_distinct_non_null_value_count=sum(
            field.distinct_non_null_count
            for layer in selected_layers
            for field in layer.fields
        ),
        complete_attribute_profile_content_sha256="",
    )
    return _profile_with_hash(profile)


def _first_field(
    profile: InpnProtectedAreasAttributeProfile,
) -> InpnProtectedAreasFieldAttributeProfile:
    return profile.layers[0].fields[0]


def test_valid_source_complete_attribute_profile_and_validation(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, extraction, catalog = _source(tmp_path, monkeypatch)

    result = build_inpn_protected_areas_attribute_profile(
        extraction,
        config,
        catalog,
    )
    validate_inpn_protected_areas_attribute_profile(
        extraction,
        config,
        catalog,
        result,
    )

    assert type(result) is InpnProtectedAreasAttributeProfile
    assert (
        result.attribute_profile_schema_version == ATTRIBUTE_PROFILE_SCHEMA_VERSION == 1
    )
    assert result.package_count == result.layer_count == 1
    assert result.field_definition_count == 2
    assert result.total_row_count == 2
    assert result.source_catalog_schema_version == 2
    assert (
        result.source_catalog_content_sha256 == catalog.complete_catalog_content_sha256
    )
    assert len(result.complete_attribute_profile_content_sha256) == 64


@pytest.mark.parametrize(
    ("argument", "value"),
    [("extraction", object()), ("config", object()), ("catalog", object())],
)
def test_wrong_public_input_types_are_controlled(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    argument: str,
    value: object,
) -> None:
    config, extraction, catalog = _source(tmp_path, monkeypatch)
    inputs: dict[str, object] = {
        "extraction": extraction,
        "config": config,
        "catalog": catalog,
    }
    inputs[argument] = value

    with pytest.raises(InpnProtectedAreasAttributeProfileError, match=argument):
        build_inpn_protected_areas_attribute_profile(
            inputs["extraction"],  # type: ignore[arg-type]
            inputs["config"],  # type: ignore[arg-type]
            inputs["catalog"],  # type: ignore[arg-type]
        )


def test_catalog_from_another_source_or_config_is_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config_a, extraction_a, _ = _source(tmp_path / "a", monkeypatch)
    config_b, _, catalog_b = _source(
        tmp_path / "b",
        monkeypatch,
        values=("other-a", "other-b"),
    )

    with pytest.raises(InpnProtectedAreasAttributeProfileError, match="catalog|source"):
        build_inpn_protected_areas_attribute_profile(
            extraction_a,
            config_a,
            catalog_b,
        )
    with pytest.raises(InpnProtectedAreasAttributeProfileError, match="source|config"):
        build_inpn_protected_areas_attribute_profile(
            extraction_a,
            config_b,
            catalog_b,
        )


def test_schema_one_catalog_is_rejected_before_attribute_read(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, extraction, catalog = _source(tmp_path, monkeypatch)
    schema_one = replace(catalog, catalog_schema_version=1)
    schema_one = replace(
        schema_one,
        complete_catalog_content_sha256=catalog_module._catalog_content_sha256(
            schema_one
        ),
    )
    calls = 0

    def forbidden(*args: object, **kwargs: object) -> pd.DataFrame:
        nonlocal calls
        calls += 1
        raise AssertionError("attribute reader called")

    monkeypatch.setattr(attributes.pyogrio, "read_dataframe", forbidden)

    with pytest.raises(InpnProtectedAreasAttributeProfileError, match="catalog"):
        build_inpn_protected_areas_attribute_profile(
            extraction,
            config,
            schema_one,
        )

    assert calls == 0


def test_coordinated_catalog_and_hash_mutation_is_rejected_before_attribute_read(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, extraction, catalog = _source(tmp_path, monkeypatch)
    layer = catalog.packages[0].layers[0]
    forged_field = replace(layer.fields[0], name="forged")
    forged_layer = replace(layer, fields=(forged_field, *layer.fields[1:]))
    forged_package = replace(catalog.packages[0], layers=(forged_layer,))
    forged = replace(catalog, packages=(forged_package,))
    forged = replace(
        forged,
        complete_catalog_content_sha256=catalog_module._catalog_content_sha256(forged),
    )
    calls = 0

    def forbidden(*args: object, **kwargs: object) -> pd.DataFrame:
        nonlocal calls
        calls += 1
        raise AssertionError("attribute reader called")

    monkeypatch.setattr(attributes.pyogrio, "read_dataframe", forbidden)

    with pytest.raises(InpnProtectedAreasAttributeProfileError, match="catalog"):
        build_inpn_protected_areas_attribute_profile(extraction, config, forged)

    assert calls == 0


def test_modified_package_is_rejected_before_attribute_read(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, extraction, catalog = _source(tmp_path, monkeypatch)
    package_path = extraction.extraction_path / "EP" / "one.gpkg"
    payload = package_path.read_bytes()
    package_path.write_bytes(payload[:-1] + bytes([payload[-1] ^ 1]))
    calls = 0

    def forbidden(*args: object, **kwargs: object) -> pd.DataFrame:
        nonlocal calls
        calls += 1
        raise AssertionError("attribute reader called")

    monkeypatch.setattr(attributes.pyogrio, "read_dataframe", forbidden)

    with pytest.raises(InpnProtectedAreasAttributeProfileError, match="source|catalog"):
        build_inpn_protected_areas_attribute_profile(extraction, config, catalog)

    assert calls == 0


def test_reader_receives_exact_bytes_layer_fields_and_options(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, extraction, catalog = _source(tmp_path, monkeypatch)
    expected_bytes = (extraction.extraction_path / "EP" / "one.gpkg").read_bytes()
    original = attributes.pyogrio.read_dataframe
    calls: list[tuple[object, dict[str, object]]] = []

    def inspected(source: object, **kwargs: object) -> object:
        calls.append((source, dict(kwargs)))
        return original(source, **kwargs)

    monkeypatch.setattr(attributes.pyogrio, "read_dataframe", inspected)

    result = build_inpn_protected_areas_attribute_profile(extraction, config, catalog)

    assert result.total_row_count == 2
    assert len(calls) == 1
    package_input, options = calls[0]
    assert type(package_input) is bytes
    assert package_input == expected_bytes
    assert options == {
        "layer": "physical_layer",
        "columns": ["text", "number"],
        "read_geometry": False,
        "fid_as_index": True,
        "use_arrow": False,
        "datetime_as_string": True,
    }


def test_every_package_and_layer_uses_one_verified_byte_snapshot(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    first_path = tmp_path / "first.gpkg"
    pyogrio.write_dataframe(
        _spatial_frame(("one-a", "one-b")),
        first_path,
        layer="first",
        driver="GPKG",
    )
    pyogrio.write_dataframe(
        _spatial_frame(("two-a", "two-b")),
        first_path,
        layer="second",
        driver="GPKG",
        append=True,
    )
    second = _gpkg_bytes(
        tmp_path,
        _spatial_frame(("three-a", "three-b")),
        filename="second.gpkg",
        layer_name="third",
    )
    archive = _zip_bytes({"EP/a.gpkg": first_path.read_bytes(), "EP/z.gpkg": second})
    config = _config(tmp_path / "source", archive)

    def fake_open(*args: object, **kwargs: object) -> Any:
        return _response(archive)

    monkeypatch.setattr(source_module, "open_safe_https", fake_open)
    download = download_inpn_protected_areas_archive(config)
    extraction = extract_inpn_protected_areas_archive(download, config)
    catalog = build_inpn_protected_areas_catalog(extraction, config)
    original = attributes.pyogrio.read_dataframe
    inputs: list[bytes] = []

    def recorded(source: object, **kwargs: object) -> object:
        assert type(source) is bytes
        inputs.append(source)
        return original(source, **kwargs)

    monkeypatch.setattr(attributes.pyogrio, "read_dataframe", recorded)

    result = build_inpn_protected_areas_attribute_profile(extraction, config, catalog)

    assert result.package_count == 2
    assert result.layer_count == 3
    assert [layer.layer_name for layer in result.layers] == ["first", "second", "third"]
    assert len(inputs) == 3
    assert inputs[0] is inputs[1]
    assert inputs[2] is not inputs[0]


def test_no_geometry_reader_or_geodataframe_is_used(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, extraction, catalog = _source(tmp_path, monkeypatch)

    def forbidden(*args: object, **kwargs: object) -> Any:
        raise AssertionError("geometry reader called")

    monkeypatch.setattr(gpd, "read_file", forbidden)
    monkeypatch.setattr(gpd, "read_parquet", forbidden)
    monkeypatch.setattr(pyogrio, "read_arrow", forbidden)
    monkeypatch.setattr(pyogrio, "open_arrow", forbidden)
    monkeypatch.setattr(pyogrio, "read_bounds", forbidden)

    result = build_inpn_protected_areas_attribute_profile(extraction, config, catalog)

    assert result.total_row_count == 2


def test_geometry_like_attribute_names_are_preserved(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, extraction, catalog = _source(
        tmp_path,
        monkeypatch,
        field_names=("geometry_label", "shape_code"),
    )

    result = build_inpn_protected_areas_attribute_profile(extraction, config, catalog)

    assert tuple(field.name for field in result.layers[0].fields) == (
        "geometry_label",
        "shape_code",
    )


def test_known_warning_is_narrowly_suppressed_for_attribute_read(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, extraction, catalog = _source(tmp_path, monkeypatch)
    original = attributes.pyogrio.read_dataframe

    def warned(*args: object, **kwargs: object) -> object:
        warnings.warn(KNOWN_BYTES_GPKG_WARNING, RuntimeWarning, stacklevel=1)
        return original(*args, **kwargs)

    monkeypatch.setattr(attributes.pyogrio, "read_dataframe", warned)
    with warnings.catch_warnings(record=True) as captured:
        warnings.simplefilter("always")
        build_inpn_protected_areas_attribute_profile(extraction, config, catalog)

    assert not [warning for warning in captured if warning.category is RuntimeWarning]


def test_unrelated_runtime_warning_remains_observable(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, extraction, catalog = _source(tmp_path, monkeypatch)
    original = attributes.pyogrio.read_dataframe

    def warned(*args: object, **kwargs: object) -> object:
        warnings.warn("unrelated attribute warning", RuntimeWarning, stacklevel=1)
        return original(*args, **kwargs)

    monkeypatch.setattr(attributes.pyogrio, "read_dataframe", warned)
    with pytest.warns(RuntimeWarning, match="unrelated attribute warning") as captured:
        build_inpn_protected_areas_attribute_profile(extraction, config, catalog)

    assert len(captured) == 1


@pytest.mark.parametrize("kind", ["geodataframe", "geometry-dtype", "shapely-cell"])
def test_geometry_bearing_reader_results_are_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    kind: str,
) -> None:
    config, extraction, catalog = _source(tmp_path, monkeypatch)
    names = [field.name for field in catalog.packages[0].layers[0].fields]
    if kind == "geodataframe":
        frame: object = _spatial_frame()
    elif kind == "geometry-dtype":
        frame = pd.DataFrame(
            {
                names[0]: gpd.GeoSeries([Point(0, 0), Point(1, 1)]),
                names[1]: [0, 1],
            },
            index=[1, 2],
        )
    else:
        frame = _frame_for(catalog, [Point(0, 0), Point(1, 1)])
    monkeypatch.setattr(attributes.pyogrio, "read_dataframe", lambda *a, **k: frame)

    with pytest.raises(
        InpnProtectedAreasAttributeProfileError,
        match="DataFrame|geometry",
    ):
        build_inpn_protected_areas_attribute_profile(extraction, config, catalog)


@pytest.mark.parametrize("mutation", ["missing", "extra", "reordered", "duplicate"])
def test_attribute_columns_must_equal_catalog_order(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    mutation: str,
) -> None:
    config, extraction, catalog = _source(tmp_path, monkeypatch)
    frame = _frame_for(catalog, ["a", "b"])
    if mutation == "missing":
        frame = frame.iloc[:, :1]
    elif mutation == "extra":
        frame["extra"] = [1, 2]
    elif mutation == "reordered":
        frame = frame.iloc[:, ::-1]
    else:
        frame.columns = [frame.columns[0], frame.columns[0]]

    with pytest.raises(InpnProtectedAreasAttributeProfileError, match="column"):
        _build_with_frame(monkeypatch, config, extraction, catalog, frame)


def test_row_count_must_equal_catalog_feature_count(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, extraction, catalog = _source(tmp_path, monkeypatch)
    frame = _frame_for(catalog, ["only-one"])

    with pytest.raises(InpnProtectedAreasAttributeProfileError, match="row count"):
        _build_with_frame(monkeypatch, config, extraction, catalog, frame)


@pytest.mark.parametrize(
    ("fids", "message"),
    [
        ([1, 1], "duplicate"),
        ([1, None], "non-integral|null"),
        ([1, True], "Boolean"),
        ([1, 2.5], "non-integral"),
    ],
)
def test_invalid_fids_are_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    fids: list[object],
    message: str,
) -> None:
    config, extraction, catalog = _source(tmp_path, monkeypatch)
    frame = _frame_for(catalog, ["a", "b"], fids=fids)

    with pytest.raises(InpnProtectedAreasAttributeProfileError, match=message):
        _build_with_frame(monkeypatch, config, extraction, catalog, frame)


def test_multiindex_is_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, extraction, catalog = _source(tmp_path, monkeypatch)
    frame = _frame_for(catalog, ["a", "b"])
    frame.index = pd.MultiIndex.from_tuples([(1, 1), (2, 1)])

    with pytest.raises(InpnProtectedAreasAttributeProfileError, match="MultiIndex"):
        _build_with_frame(monkeypatch, config, extraction, catalog, frame)


def test_noncontiguous_unsorted_fids_are_canonicalized_without_renumbering(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, extraction, catalog = _source(tmp_path, monkeypatch)
    unsorted = _frame_for(catalog, ["b", "a"], fids=[7, 2])
    first = _build_with_frame(monkeypatch, config, extraction, catalog, unsorted)
    sorted_frame = _frame_for(catalog, ["a", "b"], fids=[2, 7])
    sorted_frame.iloc[:, 1] = [1, 0]
    second = _build_with_frame(monkeypatch, config, extraction, catalog, sorted_frame)

    assert first == second
    assert first.layers[0].fid_min == 2
    assert first.layers[0].fid_max == 7
    assert first.layers[0].fid_count == 2


def test_empty_layer_has_empty_deterministic_fid_evidence(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    package = _gpkg_bytes(tmp_path, _spatial_frame(()), filename="empty.gpkg")
    config, extraction, catalog = _source_from_package(
        tmp_path,
        monkeypatch,
        package,
    )

    result = build_inpn_protected_areas_attribute_profile(extraction, config, catalog)
    layer = result.layers[0]

    assert layer.feature_count == layer.fid_count == 0
    assert layer.fid_min is layer.fid_max is None
    assert layer.fid_sequence_sha256 == attributes._canonical_json_sha256([], "test")
    assert all(field.null_count == field.non_null_count == 0 for field in layer.fields)


@pytest.mark.parametrize(
    ("values", "kind", "canonical"),
    [
        (["  text  ", ""], "TEXT", ["", "  text  "]),
        (["école", "ÉCOLE"], "TEXT", ["ÉCOLE", "école"]),
        ([True, np.bool_(False)], "BOOLEAN", ["false", "true"]),
        ([1, np.int64(-2)], "INTEGER", ["-2", "1"]),
        ([1.5, np.float64(-0.0)], "FLOAT_HEX", ["-0x0.0p+0", "0x1.8000000000000p+0"]),
        ([b"\x00\xff", b""], "BINARY_BASE64", ["", "AP8="]),
    ],
)
def test_supported_values_have_exact_canonical_domains(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    values: list[object],
    kind: str,
    canonical: list[str],
) -> None:
    config, extraction, catalog = _source(tmp_path, monkeypatch)
    frame = _frame_for(catalog, values)

    result = _build_with_frame(monkeypatch, config, extraction, catalog, frame)
    field = _first_field(result)

    assert field.null_count == 0
    assert field.non_null_count == 2
    assert field.distinct_non_null_count == 2
    assert [value.value_kind for value in field.distinct_values] == [kind, kind]
    assert [value.canonical_value for value in field.distinct_values] == canonical
    assert [value.count for value in field.distinct_values] == [1, 1]


def test_numpy_string_scalar_is_normalized_to_exact_text(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, extraction, catalog = _source(tmp_path, monkeypatch)
    frame = _frame_for(catalog, [np.str_("numpy"), "python"])

    field = _first_field(
        _build_with_frame(monkeypatch, config, extraction, catalog, frame)
    )

    assert field.distinct_values == (
        InpnProtectedAreasDistinctAttributeValue("TEXT", "numpy", 1),
        InpnProtectedAreasDistinctAttributeValue("TEXT", "python", 1),
    )


def test_source_and_runtime_dtypes_are_recorded_separately(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, extraction, catalog = _source(tmp_path, monkeypatch)

    result = build_inpn_protected_areas_attribute_profile(extraction, config, catalog)

    assert tuple(field.source_dtype for field in result.layers[0].fields) == tuple(
        field.source_dtype for field in catalog.packages[0].layers[0].fields
    )
    assert tuple(field.runtime_dtype for field in result.layers[0].fields) == (
        "str",
        "int64",
    )


@pytest.mark.parametrize("null_value", [None, float("nan"), pd.NA, pd.NaT])
def test_null_scalars_are_counted_separately(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    null_value: object,
) -> None:
    config, extraction, catalog = _source(tmp_path, monkeypatch)
    frame = _frame_for(catalog, [null_value, "known"])

    field = _first_field(
        _build_with_frame(monkeypatch, config, extraction, catalog, frame)
    )

    assert field.null_count == 1
    assert field.non_null_count == 1
    assert field.distinct_values == (
        InpnProtectedAreasDistinctAttributeValue("TEXT", "known", 1),
    )


@pytest.mark.parametrize("value", [float("inf"), float("-inf")])
def test_nonfinite_nonnull_numbers_are_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    value: float,
) -> None:
    config, extraction, catalog = _source(tmp_path, monkeypatch)

    with pytest.raises(InpnProtectedAreasAttributeProfileError, match="non-finite"):
        _build_with_frame(
            monkeypatch,
            config,
            extraction,
            catalog,
            _frame_for(catalog, [value, 1.0]),
        )


@pytest.mark.parametrize(
    "value",
    [bytearray(b"x"), [1], (1,), {"x": 1}, {1}, frozenset({1}), _ArbitraryObject()],
)
def test_unsupported_or_mutable_values_are_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    value: object,
) -> None:
    config, extraction, catalog = _source(tmp_path, monkeypatch)

    with pytest.raises(
        InpnProtectedAreasAttributeProfileError, match="forbidden|unsupported"
    ):
        _build_with_frame(
            monkeypatch,
            config,
            extraction,
            catalog,
            _frame_for(catalog, [value, "known"]),
        )


@pytest.mark.parametrize(
    "value",
    [
        datetime(2026, 7, 1, tzinfo=UTC),
        date(2026, 7, 1),
        pd.Timestamp("2026-07-01"),
    ],
)
def test_temporal_objects_are_rejected_because_reader_requires_text(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    value: object,
) -> None:
    config, extraction, catalog = _source(tmp_path, monkeypatch)

    with pytest.raises(InpnProtectedAreasAttributeProfileError, match="temporal|text"):
        _build_with_frame(
            monkeypatch,
            config,
            extraction,
            catalog,
            _frame_for(catalog, [value, "known"]),
        )


def test_all_distinct_values_and_exact_frequencies_are_retained_and_sorted(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    values = ("z", "a", "z", "b", "a")
    config, extraction, catalog = _source(tmp_path, monkeypatch, values=values)

    result = build_inpn_protected_areas_attribute_profile(extraction, config, catalog)
    field = _first_field(result)

    assert field.distinct_non_null_count == 3
    assert field.distinct_values == (
        InpnProtectedAreasDistinctAttributeValue("TEXT", "a", 2),
        InpnProtectedAreasDistinctAttributeValue("TEXT", "b", 1),
        InpnProtectedAreasDistinctAttributeValue("TEXT", "z", 2),
    )
    assert sum(value.count for value in field.distinct_values) == field.non_null_count


def test_reader_frame_is_not_mutated(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, extraction, catalog = _source(tmp_path, monkeypatch)
    frame = _frame_for(catalog, ["b", "a"], fids=[7, 2])
    before = frame.copy(deep=True)

    _build_with_frame(monkeypatch, config, extraction, catalog, frame)

    assert_frame_equal(frame, before)


def test_repeated_build_and_portable_cache_roots_are_deterministic(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    package = _gpkg_bytes(tmp_path, _spatial_frame(), filename="portable.gpkg")
    source_a = _source_from_package(tmp_path / "a", monkeypatch, package)
    source_b = _source_from_package(tmp_path / "b", monkeypatch, package)

    config_a, extraction_a, catalog_a = source_a
    config_b, extraction_b, catalog_b = source_b
    first = build_inpn_protected_areas_attribute_profile(
        extraction_a, config_a, catalog_a
    )
    repeat = build_inpn_protected_areas_attribute_profile(
        extraction_a, config_a, catalog_a
    )
    other_root = build_inpn_protected_areas_attribute_profile(
        extraction_b,
        config_b,
        catalog_b,
    )

    assert first == repeat == other_root
    assert first.complete_attribute_profile_content_sha256 == (
        other_root.complete_attribute_profile_content_sha256
    )


def test_cache_hit_state_does_not_affect_profile_hash(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, extraction, catalog = _source(tmp_path, monkeypatch)
    first = build_inpn_protected_areas_attribute_profile(extraction, config, catalog)
    changed = replace(
        extraction,
        download=replace(
            extraction.download,
            cache_hit=not extraction.download.cache_hit,
        ),
        cache_hit=not extraction.cache_hit,
    )

    second = build_inpn_protected_areas_attribute_profile(changed, config, catalog)

    assert first == second


@pytest.mark.parametrize("mutation", ["text", "fid", "frequency", "null"])
def test_content_mutations_change_component_and_profile_hashes(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    mutation: str,
) -> None:
    config, extraction, catalog = _source(tmp_path, monkeypatch)
    original = _build_with_frame(
        monkeypatch,
        config,
        extraction,
        catalog,
        _frame_for(catalog, ["a", "b"], fids=[2, 7]),
    )
    if mutation == "text":
        changed_frame = _frame_for(catalog, ["a", "c"], fids=[2, 7])
    elif mutation == "fid":
        changed_frame = _frame_for(catalog, ["a", "b"], fids=[2, 8])
    elif mutation == "frequency":
        changed_frame = _frame_for(catalog, ["a", "a"], fids=[2, 7])
    else:
        changed_frame = _frame_for(catalog, ["a", None], fids=[2, 7])
    changed = _build_with_frame(
        monkeypatch,
        config,
        extraction,
        catalog,
        changed_frame,
    )

    assert original.layers[0].row_content_sha256 != changed.layers[0].row_content_sha256
    assert original.complete_attribute_profile_content_sha256 != (
        changed.complete_attribute_profile_content_sha256
    )
    if mutation == "fid":
        assert original.layers[0].fid_sequence_sha256 != (
            changed.layers[0].fid_sequence_sha256
        )
    else:
        assert _first_field(original).column_content_sha256 != (
            _first_field(changed).column_content_sha256
        )


def test_field_order_change_changes_profile_hash(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config_a, extraction_a, catalog_a = _source(tmp_path / "a", monkeypatch)
    config_b, extraction_b, catalog_b = _source(
        tmp_path / "b",
        monkeypatch,
        field_names=("number", "text"),
    )

    profile_a = build_inpn_protected_areas_attribute_profile(
        extraction_a,
        config_a,
        catalog_a,
    )
    profile_b = build_inpn_protected_areas_attribute_profile(
        extraction_b,
        config_b,
        catalog_b,
    )

    assert tuple(field.name for field in profile_a.layers[0].fields) != tuple(
        field.name for field in profile_b.layers[0].fields
    )
    assert profile_a.complete_attribute_profile_content_sha256 != (
        profile_b.complete_attribute_profile_content_sha256
    )


def test_coordinated_profile_and_hash_mutation_fails_independent_rebuild(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, extraction, catalog = _source(tmp_path, monkeypatch)
    profile = build_inpn_protected_areas_attribute_profile(extraction, config, catalog)
    field = _first_field(profile)
    first_value = replace(field.distinct_values[0], canonical_value=" alpha forged")
    forged_field = replace(
        field,
        distinct_values=(first_value, *field.distinct_values[1:]),
    )
    forged_layer = replace(
        profile.layers[0],
        fields=(forged_field, *profile.layers[0].fields[1:]),
    )
    forged = _profile_with_hash(replace(profile, layers=(forged_layer,)))

    with pytest.raises(InpnProtectedAreasAttributeProfileError, match="rebuilt"):
        validate_inpn_protected_areas_attribute_profile(
            extraction,
            config,
            catalog,
            forged,
        )


@pytest.mark.parametrize(
    "mutation", ["aggregate", "nested-list", "bad-kind", "bad-hash"]
)
def test_intrinsic_validator_rejects_malformed_profile(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    mutation: str,
) -> None:
    config, extraction, catalog = _source(tmp_path, monkeypatch)
    profile = build_inpn_protected_areas_attribute_profile(extraction, config, catalog)
    if mutation == "aggregate":
        forged = _profile_with_hash(replace(profile, total_null_count=1))
    elif mutation == "nested-list":
        field = replace(
            _first_field(profile),
            distinct_values=list(_first_field(profile).distinct_values),  # type: ignore[arg-type]
        )
        layer = replace(
            profile.layers[0],
            fields=(field, *profile.layers[0].fields[1:]),
        )
        forged = _profile_with_hash(replace(profile, layers=(layer,)))
    elif mutation == "bad-kind":
        field = _first_field(profile)
        value = replace(field.distinct_values[0], value_kind="UNKNOWN")
        changed = replace(field, distinct_values=(value, *field.distinct_values[1:]))
        layer = replace(
            profile.layers[0],
            fields=(changed, *profile.layers[0].fields[1:]),
        )
        forged = _profile_with_hash(replace(profile, layers=(layer,)))
    else:
        forged = replace(profile, complete_attribute_profile_content_sha256="0" * 64)

    with pytest.raises(InpnProtectedAreasAttributeProfileError):
        attributes._validate_profile_intrinsic(forged)


def test_intrinsic_validator_rejects_comparison_equal_string_subclass(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, extraction, catalog = _source(tmp_path, monkeypatch)
    profile = build_inpn_protected_areas_attribute_profile(extraction, config, catalog)
    forged = _profile_with_hash(
        replace(profile, provider=_StringSubclass(profile.provider))
    )

    with pytest.raises(
        InpnProtectedAreasAttributeProfileError, match="built-in string"
    ):
        attributes._validate_profile_intrinsic(forged)


@pytest.mark.parametrize(
    "relative_path",
    [
        " EP/one.gpkg",
        "EP/one.gpkg ",
        "/EP/one.gpkg",
        "C:/EP/one.gpkg",
        "../EP/one.gpkg",
        "EP\\one.gpkg",
        "EP/one.txt",
    ],
)
def test_intrinsic_rejects_noncanonical_package_paths(relative_path: str) -> None:
    profile = _intrinsic_profile(_intrinsic_layer(relative_path=relative_path))

    with pytest.raises(InpnProtectedAreasAttributeProfileError):
        attributes._validate_profile_intrinsic(profile)


@pytest.mark.parametrize(("relative_path", "accepted"), PACKAGE_PATH_GRAMMAR_CASES)
def test_intrinsic_attribute_package_path_uses_authoritative_grammar(
    relative_path: str,
    accepted: bool,
) -> None:
    profile = _intrinsic_profile(_intrinsic_layer(relative_path=relative_path))

    if accepted:
        assert attributes._validate_profile_intrinsic(profile) is profile
    else:
        with pytest.raises(InpnProtectedAreasAttributeProfileError) as error:
            attributes._validate_profile_intrinsic(profile)
        assert isinstance(
            error.value.__cause__,
            (source_module.InpnProtectedAreasSourceError, ValueError, OSError),
        )


def test_package_path_decisions_match_extraction_catalog_and_attribute_layers(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, extraction, catalog = _source(tmp_path, monkeypatch)
    profile = build_inpn_protected_areas_attribute_profile(extraction, config, catalog)

    for relative_path, expected in PACKAGE_PATH_GRAMMAR_CASES:
        forged_package = replace(catalog.packages[0], relative_path=relative_path)
        forged_catalog = _catalog_with_hash(
            replace(catalog, packages=(forged_package,))
        )
        forged_layer = replace(profile.layers[0], relative_path=relative_path)
        forged_profile = _profile_with_hash(replace(profile, layers=(forged_layer,)))

        decisions: list[bool] = []
        for operation in (
            lambda value=relative_path: source_module._validate_inventory_relative_path(
                value
            ),
            lambda value=forged_catalog: catalog_module._validate_catalog_intrinsic(
                value
            ),
            lambda value=forged_profile: attributes._validate_profile_intrinsic(value),
        ):
            try:
                operation()
            except (
                source_module.InpnProtectedAreasSourceError,
                InpnProtectedAreasAttributeProfileError,
                catalog_module.InpnProtectedAreasCatalogError,
                OSError,
                TypeError,
                ValueError,
            ):
                decisions.append(False)
            else:
                decisions.append(True)

        assert decisions == [expected, expected, expected], relative_path


def test_intrinsic_rejects_one_package_path_under_two_positions() -> None:
    profile = _intrinsic_profile(
        _intrinsic_layer(),
        _intrinsic_layer(
            package_position=1,
            layer_name="other_layer",
            relative_path="EP/one.gpkg",
        ),
    )

    with pytest.raises(InpnProtectedAreasAttributeProfileError):
        attributes._validate_profile_intrinsic(profile)


def test_intrinsic_rejects_exact_duplicate_package_paths() -> None:
    profile = _intrinsic_profile(
        _intrinsic_layer(relative_path="EP/duplicate.gpkg"),
        _intrinsic_layer(
            relative_path="EP/duplicate.gpkg",
            package_position=1,
            layer_name="other_layer",
        ),
    )

    with pytest.raises(InpnProtectedAreasAttributeProfileError):
        attributes._validate_profile_intrinsic(profile)


@pytest.mark.parametrize(
    ("first_path", "second_path"),
    [
        ("EP/ONE.gpkg", "ep/one.gpkg"),
        ("EP/K.gpkg", "EP/\u212a.gpkg"),
    ],
)
def test_intrinsic_rejects_package_identity_collisions(
    first_path: str,
    second_path: str,
) -> None:
    profile = _intrinsic_profile(
        _intrinsic_layer(relative_path=first_path),
        _intrinsic_layer(
            relative_path=second_path,
            package_position=1,
            layer_name="other_layer",
        ),
    )

    with pytest.raises(InpnProtectedAreasAttributeProfileError):
        attributes._validate_profile_intrinsic(profile)


def test_intrinsic_rejects_nonlexical_package_order() -> None:
    profile = _intrinsic_profile(
        _intrinsic_layer(relative_path="EP/z.gpkg"),
        _intrinsic_layer(
            relative_path="EP/a.gpkg",
            package_position=1,
            layer_name="other_layer",
        ),
    )

    with pytest.raises(InpnProtectedAreasAttributeProfileError):
        attributes._validate_profile_intrinsic(profile)


@pytest.mark.parametrize("metadata", ["file_size", "file_sha256"])
def test_intrinsic_rejects_inconsistent_repeated_package_metadata(
    metadata: str,
) -> None:
    second = _intrinsic_layer(layer_name="other_layer", layer_position=1)
    if metadata == "file_size":
        second = replace(second, file_size=second.file_size + 1)
    else:
        second = replace(second, file_sha256="7" * 64)
    profile = _intrinsic_profile(_intrinsic_layer(), second)

    with pytest.raises(InpnProtectedAreasAttributeProfileError):
        attributes._validate_profile_intrinsic(profile)


@pytest.mark.parametrize("positions", [(0, 0), (0, 2), (1, 0)])
def test_intrinsic_rejects_noncanonical_layer_positions(
    positions: tuple[int, int],
) -> None:
    profile = _intrinsic_profile(
        _intrinsic_layer(layer_position=positions[0]),
        _intrinsic_layer(layer_name="other_layer", layer_position=positions[1]),
    )

    with pytest.raises(InpnProtectedAreasAttributeProfileError):
        attributes._validate_profile_intrinsic(profile)


def test_intrinsic_rejects_noncontiguous_package_groups() -> None:
    profile = _intrinsic_profile(
        _intrinsic_layer(),
        _intrinsic_layer(
            relative_path="EP/two.gpkg",
            package_position=1,
            layer_name="second_package_layer",
        ),
        _intrinsic_layer(layer_name="late_first_package_layer", layer_position=1),
    )

    with pytest.raises(InpnProtectedAreasAttributeProfileError):
        attributes._validate_profile_intrinsic(profile)


@pytest.mark.parametrize(
    ("first_name", "second_name"),
    [
        ("same", "same"),
        ("Layer", "layer"),
        ("K", "\u212a"),
    ],
)
def test_intrinsic_rejects_layer_identity_collisions(
    first_name: str,
    second_name: str,
) -> None:
    profile = _intrinsic_profile(
        _intrinsic_layer(layer_name=first_name),
        _intrinsic_layer(layer_name=second_name, layer_position=1),
    )

    with pytest.raises(InpnProtectedAreasAttributeProfileError):
        attributes._validate_profile_intrinsic(profile)


def test_intrinsic_rejects_layer_name_edge_whitespace() -> None:
    profile = _intrinsic_profile(_intrinsic_layer(layer_name=" layer"))

    with pytest.raises(InpnProtectedAreasAttributeProfileError):
        attributes._validate_profile_intrinsic(profile)


@pytest.mark.parametrize(
    ("first_name", "second_name"),
    [
        ("same", "same"),
        ("Field", "field"),
        ("K", "\u212a"),
    ],
)
def test_intrinsic_rejects_field_identity_collisions(
    first_name: str,
    second_name: str,
) -> None:
    fields = (
        _intrinsic_field(first_name, 0),
        _intrinsic_field(second_name, 1),
    )
    profile = _intrinsic_profile(_intrinsic_layer(fields=fields))

    with pytest.raises(InpnProtectedAreasAttributeProfileError):
        attributes._validate_profile_intrinsic(profile)


def test_intrinsic_rejects_field_name_edge_whitespace() -> None:
    fields = (
        _intrinsic_field(" field", 0),
        _intrinsic_field("number", 1),
    )
    profile = _intrinsic_profile(_intrinsic_layer(fields=fields))

    with pytest.raises(InpnProtectedAreasAttributeProfileError):
        attributes._validate_profile_intrinsic(profile)


@pytest.mark.parametrize("dtype", ["source", "runtime"])
def test_intrinsic_rejects_dtype_edge_whitespace(dtype: str) -> None:
    kwargs = {f"{dtype}_dtype": " object"}
    fields = (
        _intrinsic_field("text", 0, **kwargs),
        _intrinsic_field("number", 1),
    )
    profile = _intrinsic_profile(_intrinsic_layer(fields=fields))

    with pytest.raises(InpnProtectedAreasAttributeProfileError):
        attributes._validate_profile_intrinsic(profile)


def test_intrinsic_rejects_single_row_fid_extrema_mismatch() -> None:
    profile = _intrinsic_profile(
        _intrinsic_layer(feature_count=1, fid_min=1, fid_max=2)
    )

    with pytest.raises(InpnProtectedAreasAttributeProfileError):
        attributes._validate_profile_intrinsic(profile)


@pytest.mark.parametrize(("fid_min", "fid_max"), [(2, 2), (2, 1)])
def test_intrinsic_rejects_impossible_multirow_fid_ranges(
    fid_min: int,
    fid_max: int,
) -> None:
    profile = _intrinsic_profile(
        _intrinsic_layer(feature_count=2, fid_min=fid_min, fid_max=fid_max)
    )

    with pytest.raises(InpnProtectedAreasAttributeProfileError):
        attributes._validate_profile_intrinsic(profile)


def test_intrinsic_accepts_sparse_fid_range() -> None:
    profile = _intrinsic_profile(
        _intrinsic_layer(feature_count=2, fid_min=1, fid_max=10)
    )

    assert attributes._validate_profile_intrinsic(profile) is profile


def test_intrinsic_rejects_fid_count_exceeding_range_capacity() -> None:
    profile = _intrinsic_profile(
        _intrinsic_layer(feature_count=3, fid_min=1, fid_max=2)
    )

    with pytest.raises(
        InpnProtectedAreasAttributeProfileError,
        match="FID range is impossible",
    ):
        attributes._validate_profile_intrinsic(profile)


def test_intrinsic_accepts_sparse_fid_range_with_capacity() -> None:
    profile = _intrinsic_profile(
        _intrinsic_layer(feature_count=3, fid_min=1, fid_max=4)
    )

    assert attributes._validate_profile_intrinsic(profile) is profile


def test_intrinsic_rejects_different_paths_for_one_package_position() -> None:
    profile = _intrinsic_profile(
        _intrinsic_layer(),
        _intrinsic_layer(
            relative_path="EP/other.gpkg",
            layer_name="other_layer",
            layer_position=1,
        ),
    )

    with pytest.raises(
        InpnProtectedAreasAttributeProfileError,
        match="repeated package metadata",
    ):
        attributes._validate_profile_intrinsic(profile)


@pytest.mark.parametrize("component", ["fid", "row", "column"])
def test_intrinsic_rejects_malformed_empty_component_hashes(component: str) -> None:
    layer = _intrinsic_layer(feature_count=0)
    if component == "fid":
        layer = replace(layer, fid_sequence_sha256="8" * 64)
    elif component == "row":
        layer = replace(layer, row_content_sha256="8" * 64)
    else:
        first = replace(layer.fields[0], column_content_sha256="8" * 64)
        layer = replace(layer, fields=(first, *layer.fields[1:]))
    profile = _intrinsic_profile(layer)

    with pytest.raises(InpnProtectedAreasAttributeProfileError):
        attributes._validate_profile_intrinsic(profile)


@pytest.mark.parametrize(
    "mutation",
    ["source", "catalog", "package", "layer", "field"],
)
def test_public_validator_rejects_catalog_mismatch_before_attribute_read(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    mutation: str,
) -> None:
    config, extraction, catalog = _source(tmp_path, monkeypatch)
    profile = build_inpn_protected_areas_attribute_profile(extraction, config, catalog)
    if mutation == "source":
        forged = replace(profile, provider="forged provider")
    elif mutation == "catalog":
        forged = replace(profile, source_catalog_content_sha256="9" * 64)
    elif mutation == "package":
        layer = replace(profile.layers[0], file_size=profile.layers[0].file_size + 1)
        forged = replace(profile, layers=(layer,))
    elif mutation == "layer":
        layer = replace(profile.layers[0], layer_name="other_layer")
        forged = replace(profile, layers=(layer,))
    else:
        field = replace(profile.layers[0].fields[0], source_dtype="forged")
        layer = replace(
            profile.layers[0], fields=(field, *profile.layers[0].fields[1:])
        )
        forged = replace(profile, layers=(layer,))
    forged = _profile_with_hash(forged)
    read_calls = 0

    def forbidden_read(*args: object, **kwargs: object) -> object:
        nonlocal read_calls
        read_calls += 1
        raise AssertionError("attribute read reached before cheap catalog comparison")

    monkeypatch.setattr(attributes.pyogrio, "read_dataframe", forbidden_read)

    with pytest.raises(InpnProtectedAreasAttributeProfileError):
        validate_inpn_protected_areas_attribute_profile(
            extraction,
            config,
            catalog,
            forged,
        )
    assert read_calls == 0


def test_public_validator_valid_profile_reaches_attribute_rebuild(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, extraction, catalog = _source(tmp_path, monkeypatch)
    profile = build_inpn_protected_areas_attribute_profile(extraction, config, catalog)
    original = attributes.pyogrio.read_dataframe
    read_calls = 0

    def recording_read(*args: object, **kwargs: object) -> object:
        nonlocal read_calls
        read_calls += 1
        return original(*args, **kwargs)

    monkeypatch.setattr(attributes.pyogrio, "read_dataframe", recording_read)

    validate_inpn_protected_areas_attribute_profile(
        extraction,
        config,
        catalog,
        profile,
    )

    assert read_calls == catalog.layer_count


def test_public_validator_rejects_wrong_profile_type_before_physical_rebuild(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, extraction, catalog = _source(tmp_path, monkeypatch)

    with pytest.raises(InpnProtectedAreasAttributeProfileError, match="profile"):
        validate_inpn_protected_areas_attribute_profile(
            extraction,
            config,
            catalog,
            object(),  # type: ignore[arg-type]
        )


def test_temporary_package_path_swap_cannot_inject_other_attributes(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    package_a = _gpkg_bytes(
        tmp_path,
        _spatial_frame(("from-a-1", "from-a-2")),
        filename="a.gpkg",
    )
    package_b = _gpkg_bytes(
        tmp_path,
        _spatial_frame(("from-b-1", "from-b-2")),
        filename="b.gpkg",
    )
    config, extraction, catalog = _source_from_package(
        tmp_path / "source",
        monkeypatch,
        package_a,
    )
    package_path = extraction.extraction_path / "EP" / "one.gpkg"
    original = attributes.pyogrio.read_dataframe
    swap_observed = False

    def swapped(source: object, **kwargs: object) -> object:
        nonlocal swap_observed
        assert type(source) is bytes and source == package_a
        package_path.write_bytes(package_b)
        swap_observed = True
        try:
            return original(source, **kwargs)
        finally:
            package_path.write_bytes(package_a)

    monkeypatch.setattr(attributes.pyogrio, "read_dataframe", swapped)

    profile = build_inpn_protected_areas_attribute_profile(extraction, config, catalog)

    assert swap_observed
    assert {
        value.canonical_value for value in _first_field(profile).distinct_values
    } == {
        "from-a-1",
        "from-a-2",
    }


def test_persistent_package_mutation_fails_final_source_revalidation(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    package_a = _gpkg_bytes(tmp_path, _spatial_frame(), filename="a.gpkg")
    package_b = _gpkg_bytes(
        tmp_path,
        _spatial_frame(("other-1", "other-2")),
        filename="b.gpkg",
    )
    config, extraction, catalog = _source_from_package(
        tmp_path / "source",
        monkeypatch,
        package_a,
    )
    package_path = extraction.extraction_path / "EP" / "one.gpkg"
    original = attributes.pyogrio.read_dataframe

    def mutate(source: object, **kwargs: object) -> object:
        frame = original(source, **kwargs)
        package_path.write_bytes(package_b)
        return frame

    monkeypatch.setattr(attributes.pyogrio, "read_dataframe", mutate)

    with pytest.raises(InpnProtectedAreasAttributeProfileError, match="changed"):
        build_inpn_protected_areas_attribute_profile(extraction, config, catalog)


def test_profile_contains_no_frame_or_geometry_object(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config, extraction, catalog = _source(tmp_path, monkeypatch)
    profile = build_inpn_protected_areas_attribute_profile(extraction, config, catalog)

    def walk(value: object) -> None:
        assert not isinstance(value, (pd.DataFrame, gpd.GeoDataFrame, BaseException))
        assert not hasattr(value, "geom_type")
        if is_dataclass(value) and not isinstance(value, type):
            for field in fields(value):
                walk(getattr(value, field.name))
        elif isinstance(value, tuple):
            for member in value:
                walk(member)

    walk(profile)


def test_public_api_exports_only_profile_boundary() -> None:
    assert set(attributes.__all__) == EXPECTED_EXPORTS
    assert EXPECTED_EXPORTS <= set(sources.__all__)
    assert all(
        getattr(sources, name) is getattr(attributes, name) for name in EXPECTED_EXPORTS
    )
    assert not hasattr(sources, "_canonical_cell")
    assert not hasattr(sources, "_read_verified_package_bytes")
    assert not hasattr(sources, "read_dataframe")


def test_profile_models_are_frozen_factual_records() -> None:
    value = InpnProtectedAreasDistinctAttributeValue("TEXT", "x", 1)

    with pytest.raises(FrozenInstanceError):
        value.count = 2  # type: ignore[misc]

    names = {
        field.name
        for model in (
            InpnProtectedAreasDistinctAttributeValue,
            InpnProtectedAreasFieldAttributeProfile,
            InpnProtectedAreasLayerAttributeProfile,
            InpnProtectedAreasAttributeProfile,
        )
        for field in fields(model)
    }
    assert not names.intersection(
        {"category", "legal_regime", "natura_2000", "znieff", "parcel", "score"}
    )
```
