# `tests/unit/test_inpn_protected_areas_evidence_fr.py`

## File identity

- Repository path: `tests/unit/test_inpn_protected_areas_evidence_fr.py`
- File type: source-complete unit/regression tests using temporary physical sources
- Source SHA256: `2248c5b5e6cb295086674a29f25d6c801ee7e50f04c7aec9f390336bb527b97b`
- Collection: 25 top-level test functions, expanding to 141 Pytest cases; 12 top-level fixture/support functions and 10 explicitly qualified nested callbacks.
- Production owner: [INPN evidence bundle](../../src/landscout/sources/inpn_protected_areas_evidence_fr.py.md).

## 1. Contract and isolation

This suite proves exact source-bound catalog/attribute/geometry alignment and the new immutable compact bundle, not environmental policy or a materialized attribute/geometry join. Real positive controls construct tiny temporary ZIPs and GeoPackages, pass strict download/extraction/catalog validation, build both upstream profiles, then execute the public bundle builder and independent validator without replacing their physical trust checks. The only acquisition transport is an adapter-local byte-backed fake response. No real EP cache, live download, parcel, category, environmental exclusion, or score is involved.

Pure tests named `test_pure_alignment_*` deliberately combine inconsistent, coherently rehashed profile evidence and call the private structural helper. They are not presented as physically valid end-to-end results. Fault-injection tests are similarly explicit about replacing a boundary to inspect error translation. Other instrumentation delegates to real public validators/readers and asserts hook execution or exact counts so a missing hook cannot create false proof.

Fixture writes may use Pyogrio for an ordinary XY container and SQLite to install exact FIDs/raw BLOBs. Runtime geometry evidence still comes only from the approved geometry-module SQLite/parser path; the attribute-only Pyogrio reader remains necessary and is required to use every existing exact option. Independently constructed M/ZM Point BLOBs preserve true measured ordinates rather than asking the lossy Pyogrio geometry reader to manufacture fixtures. Existing upstream schemas/hashes/contracts remain authoritative.

## 2. Imports and qualified ownership

Standard-library `ast`/`inspect` audit the new production module for forbidden direct readers/imports; `io`, `zipfile`, `sqlite3`, and `struct` construct isolated byte-backed physical fixtures; `Iterator`, `Mapping`, and `contextmanager` describe fake responses; `FrozenInstanceError`, `dataclass`, `fields`, `is_dataclass`, and `replace` exercise immutable records and coherent test forgeries; `json`/`hashlib.sha256` independently specify canonical hashes; `Path`, `Any`, and `ClassVar` support fixtures and exact-type adversaries.

Third-party `geopandas as gpd`, `pyogrio`, and `Point` create only the seed XY container; `shapely` checks genuine parsed measured geometry; `numpy as np` supplies invalid scalar/array controls; `pandas as pd` identifies prohibited retained frames; `yaml` reads the unchanged human-authored source config; `pytest` owns fixture/parameter/error/monkeypatch behavior. Imported production bindings and aliases are exact in the block below. `evidence` owns the new alignment/bundle helpers; `attribute_module`, `catalog_module`, `geometry_module`, and `source_module` retain their distinct upstream validator/hash/reader ownership. A rehash helper is not an alternative source validator.

```python
from __future__ import annotations

import ast

import inspect

import io

import json

import sqlite3

import struct

import zipfile

from collections.abc import Iterator, Mapping

from contextlib import contextmanager

from dataclasses import (
    FrozenInstanceError,
    dataclass,
    fields,
    is_dataclass,
    replace,
)

from hashlib import sha256

from pathlib import Path

from typing import Any, ClassVar

import geopandas as gpd

import numpy as np

import pandas as pd

import pyogrio

import pytest

import shapely

import yaml

from shapely.geometry import Point

from landscout import sources

from landscout.sources import inpn_protected_areas_attributes_fr as attribute_module

from landscout.sources import inpn_protected_areas_catalog_fr as catalog_module

from landscout.sources import inpn_protected_areas_evidence_fr as evidence

from landscout.sources import inpn_protected_areas_fr as source_module

from landscout.sources import inpn_protected_areas_geometry_fr as geometry_module

from landscout.sources.inpn_protected_areas_attributes_fr import (
    InpnProtectedAreasAttributeProfile,
    InpnProtectedAreasAttributeProfileError,
    build_inpn_protected_areas_attribute_profile,
)

from landscout.sources.inpn_protected_areas_catalog_fr import (
    InpnProtectedAreasCatalog,
    InpnProtectedAreasCatalogError,
    build_inpn_protected_areas_catalog,
)

from landscout.sources.inpn_protected_areas_evidence_fr import (
    InpnProtectedAreasEvidenceBundle,
    InpnProtectedAreasEvidenceError,
    InpnProtectedAreasLayerAlignment,
    build_inpn_protected_areas_evidence_bundle,
    validate_inpn_protected_areas_evidence_bundle,
)

from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    download_inpn_protected_areas_archive,
    extract_inpn_protected_areas_archive,
)

from landscout.sources.inpn_protected_areas_geometry_fr import (
    InpnProtectedAreasGeometryProfile,
    InpnProtectedAreasGeometryProfileError,
    build_inpn_protected_areas_geometry_profile,
)
```

## 3. Constants, classes, and fixture fields

`CONFIG_PATH` identifies the unchanged checked-in YAML; `_source` overrides only the isolated fixture cache and actual synthetic archive size/SHA. `EXPECTED_EXPORTS` independently lists the five approved new public names. `ALIGNMENT_FIELDS` fixes the exact ten-field order used by independent expected payloads and dataclass contract assertions. `SOURCE_MUTATIONS` is the exact thirteen-row source/archive/catalog adversarial corpus, each applied separately to both profile owners. These mutable test-only setup collections do not become returned trust data.

```python
CONFIG_PATH = Path("configs/sources/inpn_protected_areas_fr.yaml")

EXPECTED_EXPORTS = {
    "InpnProtectedAreasEvidenceBundle",
    "InpnProtectedAreasEvidenceError",
    "InpnProtectedAreasLayerAlignment",
    "build_inpn_protected_areas_evidence_bundle",
    "validate_inpn_protected_areas_evidence_bundle",
}

ALIGNMENT_FIELDS = (
    "relative_path",
    "package_position",
    "file_sha256",
    "layer_name",
    "layer_position",
    "feature_count",
    "fid_count",
    "fid_min",
    "fid_max",
    "fid_sequence_sha256",
)

SOURCE_MUTATIONS = (
    ("provider", "other provider"),
    ("authority", "other authority"),
    ("program", "other program"),
    ("dataset_id", "other dataset"),
    ("dataset_name", "other name"),
    ("declared_version", "08/2026"),
    ("reference_page_url", "https://example.test/reference"),
    ("archive_url", "https://example.test/EP.zip"),
    ("archive_filename", "other.zip"),
    ("archive_size", 1),
    ("archive_sha256", "0" * 64),
    ("source_catalog_schema_version", 1),
    ("source_catalog_content_sha256", "0" * 64),
)
```

| Class and field | Meaning |
|---|---|
| `_Response(io.BytesIO)` | Context-managed in-memory fake HTTP body, no real network. |
| `_Response.headers: ClassVar[dict[str, str]] = {"Content-Type": "application/zip"}` | Test-only shared response header, not a retained source/config integrity model. |
| `_StringSubclass(str)` | Structurally equal but non-exact string adversary; adds no fields or methods. |
| `_Source` with `@dataclass(frozen=True)` | Test convenience envelope retaining five independently built source-bound inputs. |
| `_Source.extraction: InpnProtectedAreasExtraction` | Actual temporary verified archive/extraction envelope. |
| `_Source.config: InpnProtectedAreasSourceConfig` | Strictly validated source locks adjusted to fixture bytes/cache only. |
| `_Source.catalog: InpnProtectedAreasCatalog` | Actual metadata-only physical catalog. |
| `_Source.attributes: InpnProtectedAreasAttributeProfile` | Actual attribute-only physical profile. |
| `_Source.geometries: InpnProtectedAreasGeometryProfile` | Actual raw-BLOB physical geometry profile. |

## 4. Exact collected-case inventory

Case counts below are products of the exact decorators, not inferred from function names. Every parameter value appears with its owning function in section 5. The 141 new cases are added to the retained four-file 803-case INPN baseline; executed final combined/full results are recorded in `docs/DEV_LOG.md` only after those runs complete.

| Top-level test | Cases |
|---|---:|
| `test_complete_bundle_is_deterministic_and_independently_validated` | 1 |
| `test_builder_requires_exact_public_input_types` | 10 |
| `test_validator_requires_exact_public_input_types` | 6 |
| `test_public_boundaries_reconstruct_same_type_config_before_physical_validation` | 2 |
| `test_pure_alignment_rejects_source_archive_catalog_identity_mismatches` | 26 |
| `test_pure_alignment_rejects_layer_inventory_changes` | 8 |
| `test_pure_alignment_rejects_package_layer_and_fid_contradictions` | 24 |
| `test_pure_alignment_retains_upstream_aggregate_contracts` | 4 |
| `test_pure_alignment_equal_counts_and_extrema_do_not_hide_different_fids` | 1 |
| `test_empty_negative_and_sparse_fids_align_without_renumbering` | 3 |
| `test_full_package_layer_key_handles_identical_names_in_distinct_packages` | 1 |
| `test_same_physical_rows_in_reversed_attribute_read_order_still_align` | 1 |
| `test_measured_profiles_bundle_through_only_approved_readers` | 2 |
| `test_portable_bundle_ignores_cache_roots_and_cache_hit_flags` | 1 |
| `test_coordinated_upstream_and_bundle_rehash_cannot_override_physical_bytes` | 3 |
| `test_coordinated_catalog_profiles_and_bundle_rehash_cannot_override_source` | 1 |
| `test_rehashed_bundle_alignment_inventory_must_be_exact` | 4 |
| `test_forged_alignment_record_with_rehashed_bundle_is_rejected` | 10 |
| `test_bundle_validator_rejects_malformed_nested_runtime_evidence` | 14 |
| `test_alignment_fields_require_exact_builtin_runtime_types` | 10 |
| `test_persistent_source_mutation_after_alignment_fails_final_postcondition` | 2 |
| `test_builder_and_validator_delegate_once_per_complete_profile_not_per_layer` | 1 |
| `test_controlled_lower_boundary_failure_preserves_cause` | 4 |
| `test_results_are_deeply_immutable_portable_profiles_not_joined_rows` | 1 |
| `test_module_exposes_only_trusted_public_boundary_and_has_no_third_reader` | 1 |
| Total | 141 |

## 5. Every fixture, helper, test, and nested callback

The exact signature and all decorators—including complete parameter values—appear for each definition. Assertions, expected exceptions/warnings, monkeypatch expressions, and raises are extracted only from that definition's own lexical body: nested callbacks have their own qualified sections and their assertions are not falsely assigned to the parent. Purpose paragraphs explain fixture setup, delegation, mutation, and the boundary actually exercised. The complete byte-bound source snapshot in section 7 preserves every remaining setup/call statement.

### `_response`


```python
@contextmanager
def _response(payload: bytes) -> Iterator[_Response]:
```

Fixture-only context manager yields a byte-backed fake HTTPS response and guarantees its closure. It is used only by `_source`'s adapter-local fake transport.

This helper/callback does not directly assert an outcome; its constructed or delegated state is checked by the owning tests.

### `_json_hash`


```python
def _json_hash(payload: object) -> str:
```

Independent canonical sorted-key, compact, finite-only UTF-8 JSON SHA256 implementation used for expected commitments and deliberately coherent forgeries; it does not call the production bundle hasher.

This helper/callback does not directly assert an outcome; its constructed or delegated state is checked by the owning tests.

### `_point_blob`


```python
def _point_blob(position: int, layout: str) -> bytes:
```

Constructs a fixture-only Standard GeoPackageBinary header for SRS 2154 and little-endian ISO Point WKB. The layout independently adds Z=3 and/or M=4 ordinates and the corresponding 1000/2000 type offsets; measured geometries never pass through Pyogrio conversion.

This helper/callback does not directly assert an outcome; its constructed or delegated state is checked by the owning tests.

### `_package`


```python
def _package(
    tmp_path: Path,
    layers: tuple[tuple[str, tuple[int, ...]], ...] = (("first", (1, 2, 4)),),
    *,
    layout: str = "XY",
) -> bytes:
```

Builds a tiny XY GeoPackage container with Pyogrio, then deserializes it into fixture SQLite to replace rows with exact specified physical FIDs and independently generated raw BLOBs. Business IDs are deliberately repeated and cannot serve as FIDs. Layer order is supplied, identifiers are quoted, Z/M metadata permits optional ordinates, empty-layer bounds are nulled, and the in-memory connection always closes. These fixture writes are not production reads or real EP mutations.

This helper/callback does not directly assert an outcome; its constructed or delegated state is checked by the owning tests.

### `_source`


```python
def _source(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    *,
    files: Mapping[str, bytes] | None = None,
    layers: tuple[tuple[str, tuple[int, ...]], ...] = (("first", (1, 2, 4)),),
    layout: str = "XY",
) -> _Source:
```

Creates deterministic timestamped ZIP members, clones the checked-in YAML with only temporary cache root and fixture byte size/SHA locks, and validates the exact config. Only adapter-local HTTPS is replaced with `_response`; real download validation, extraction, metadata catalog, attribute profile, and geometry profile builders all execute. The returned `_Source` holds those five source-bound inputs; this is the public physical fixture root, not mocked profile trust.

Monkeypatch expressions:


```python
monkeypatch.setattr(
        source_module, "open_safe_https", lambda *a, **k: _response(archive_bytes)
    )
```

This helper/callback does not directly assert an outcome; its constructed or delegated state is checked by the owning tests.

### `source`


```python
@pytest.fixture
def source(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> _Source:
```

Pytest fixture delegates to `_source` under `tmp_path` and `monkeypatch`, yielding one physical layer with sparse FIDs `(1, 2, 4)`.

This helper/callback does not directly assert an outcome; its constructed or delegated state is checked by the owning tests.

### `_build`


```python
def _build(source: _Source) -> InpnProtectedAreasEvidenceBundle:
```

Forwards all five exact `_Source` inputs to the public bundle builder without mocking either profile validator.

This helper/callback does not directly assert an outcome; its constructed or delegated state is checked by the owning tests.

### `_rehash_profile`


```python
def _rehash_profile(profile: Any, **changes: object) -> Any:
```

Pure adversarial helper replaces selected profile facts and recalculates the complete hash using the qualified owning attribute or geometry helper. Rehashing creates intrinsic test evidence, not physical authority.

This helper/callback does not directly assert an outcome; its constructed or delegated state is checked by the owning tests.

### `_profile_layers`


```python
def _profile_layers(profile: Any, layers: tuple[Any, ...]) -> Any:
```

Pure adversarial helper coherently recomputes aggregate package/layer/row/field/null/domain or geometry-state counts for replacement layers, then delegates to `_rehash_profile`. It supports layer-inventory contradictions without presenting impossible profile combinations as genuine source reads.

This helper/callback does not directly assert an outcome; its constructed or delegated state is checked by the owning tests.

### `_expected_payload`


```python
def _expected_payload(bundle: InpnProtectedAreasEvidenceBundle) -> dict[str, object]:
```

Independently spells out the compact schema/hash-pair/alignment payload with explicit ten-field extraction. It never calls production `_bundle_payload` or expands upstream value/geometry domains.

This helper/callback does not directly assert an outcome; its constructed or delegated state is checked by the owning tests.

### `_rehash_bundle`


```python
def _rehash_bundle(
    bundle: InpnProtectedAreasEvidenceBundle, **changes: object
) -> InpnProtectedAreasEvidenceBundle:
```

Replaces selected bundle facts and recomputes the complete bundle digest using the independent expected payload and independent JSON hasher. Used to ensure rejection is not merely stale-hash detection.

This helper/callback does not directly assert an outcome; its constructed or delegated state is checked by the owning tests.

### `_subclass`


```python
def _subclass(value: Any) -> Any:
```

Constructs a real subclass of the supplied runtime model, reconstructing Pydantic config via validation and dataclasses via their field values. Exact-type boundaries must reject these structurally equivalent subclass instances.

This helper/callback does not directly assert an outcome; its constructed or delegated state is checked by the owning tests.

### `test_complete_bundle_is_deterministic_and_independently_validated`


```python
def test_complete_bundle_is_deterministic_and_independently_validated(
    source: _Source,
) -> None:
```

Real physical positive control: build, repeat, and public independent validation succeed. Checks exact schema/model classes, unchanged retained upstream records, the complete ten-field alignment with physical FIDs `[1, 2, 4]`, and exact independent compact hash payload. The attribute subpayload contains only its schema and complete SHA.

Direct assertions:


```python
assert _build(source) == first

assert type(first) is InpnProtectedAreasEvidenceBundle

assert (
        first.evidence_bundle_schema_version
        == evidence.EVIDENCE_BUNDLE_SCHEMA_VERSION
        == 1
    )

assert (first.catalog, first.attributes, first.geometries) == (
        source.catalog,
        source.attributes,
        source.geometries,
    )

assert len(first.layer_alignments) == 1

assert type(alignment) is InpnProtectedAreasLayerAlignment

assert alignment == InpnProtectedAreasLayerAlignment(
        "EP/one.gpkg",
        0,
        source.catalog.packages[0].file_sha256,
        "first",
        0,
        3,
        3,
        1,
        4,
        _json_hash([1, 2, 4]),
    )

assert evidence._bundle_payload(first) == _expected_payload(first)

assert first.complete_evidence_bundle_content_sha256 == _json_hash(
        _expected_payload(first)
    )

assert set(_expected_payload(first)["attributes"]) == {
        "attribute_profile_schema_version",
        "complete_attribute_profile_content_sha256",
    }
```

### `test_builder_requires_exact_public_input_types`


```python
@pytest.mark.parametrize(
    "argument", ["extraction", "config", "catalog", "attributes", "geometries"]
)
@pytest.mark.parametrize("kind", ["object", "subclass"])
def test_builder_requires_exact_public_input_types(
    source: _Source, argument: str, kind: str
) -> None:
```

The five builder arguments are each replaced by an unrelated object and a real subclass (ten cases). Every call must immediately return a controlled evidence error rather than accept structural duck typing.

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasEvidenceError)
```

### `test_validator_requires_exact_public_input_types`


```python
@pytest.mark.parametrize("argument", ["extraction", "config", "bundle"])
@pytest.mark.parametrize("kind", ["object", "subclass"])
def test_validator_requires_exact_public_input_types(
    source: _Source, argument: str, kind: str
) -> None:
```

The three validator arguments are each replaced by an unrelated object and a real subclass (six cases). A valid physical bundle supplies the other inputs.

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasEvidenceError)
```

### `test_public_boundaries_reconstruct_same_type_config_before_physical_validation`


```python
@pytest.mark.parametrize("boundary", ["builder", "validator"])
def test_public_boundaries_reconstruct_same_type_config_before_physical_validation(
    source: _Source, monkeypatch: pytest.MonkeyPatch, boundary: str
) -> None:
```

For both public builder and validator, an unchecked same-class Pydantic model_copy changes the expected archive size to Boolean. Exact class equality is explicitly proven, then config reconstruction must fail with the precise config-invalid error before the first physical profile validator. This preserves source revalidation despite deep freezing.

Direct assertions:


```python
assert type(forged_config) is InpnProtectedAreasSourceConfig

assert calls == []
```

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasEvidenceError, match="config is invalid")
```

Monkeypatch expressions:


```python
monkeypatch.setattr(
        evidence, "validate_inpn_protected_areas_attribute_profile", observed
    )
```

### `test_public_boundaries_reconstruct_same_type_config_before_physical_validation.observed`


```python
    def observed(*args: object, **kwargs: object) -> None:
```

Nested delegating observer owned by the same-type config-forgery test. It would record and invoke the real attribute validator; the owning test asserts it is never reached after config rejection.

This helper/callback does not directly assert an outcome; its constructed or delegated state is checked by the owning tests.

### `test_pure_alignment_rejects_source_archive_catalog_identity_mismatches`


```python
@pytest.mark.parametrize("owner", ["attributes", "geometries"])
@pytest.mark.parametrize(("field_name", "value"), SOURCE_MUTATIONS)
def test_pure_alignment_rejects_source_archive_catalog_identity_mismatches(
    source: _Source, owner: str, field_name: str, value: object
) -> None:
```

Pure structural-only cross product: each attribute/geometry profile receives each of the thirteen source/archive/catalog mutations with a coherent owning profile hash. `_align_layers` must reject the contradiction. No physical validator is mocked and these impossible profiles are not described as a public physical success.

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasEvidenceError)
```

### `test_pure_alignment_rejects_layer_inventory_changes`


```python
@pytest.mark.parametrize("owner", ["attributes", "geometries"])
@pytest.mark.parametrize("mutation", ["missing", "extra", "duplicate", "reordered"])
def test_pure_alignment_rejects_layer_inventory_changes(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, owner: str, mutation: str
) -> None:
```

Pure inventory tests use a genuine two-layer source but deliberately remove, add, duplicate, or reorder one profile's layers while closing aggregates. Both profile owners are exercised; no sorting repair or inventory omission is permitted.

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasEvidenceError)
```

### `test_pure_alignment_rejects_package_layer_and_fid_contradictions`


```python
@pytest.mark.parametrize("owner", ["attributes", "geometries"])
@pytest.mark.parametrize(
    ("field_name", "value"),
    [
        ("relative_path", "EP/other.gpkg"),
        ("file_size", 1),
        ("file_sha256", "0" * 64),
        ("package_position", 1),
        ("driver_name", "SQLite"),
        ("layer_name", "other"),
        ("layer_position", 1),
        ("feature_count", 4),
        ("fid_count", 4),
        ("fid_min", -1),
        ("fid_max", 5),
        ("fid_sequence_sha256", "0" * 64),
    ],
)
def test_pure_alignment_rejects_package_layer_and_fid_contradictions(
    source: _Source, owner: str, field_name: str, value: object
) -> None:
```

Pure structural-only cross product changes each of twelve package/layer/FID fields in each profile and recomputes its complete hash. Catalog binding and inherited intrinsic constraints must reject wrong path/size/SHA/driver/positions/name/count/extrema/sequence commitment.

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasEvidenceError)
```

### `test_pure_alignment_retains_upstream_aggregate_contracts`


```python
@pytest.mark.parametrize("owner", ["attributes", "geometries"])
@pytest.mark.parametrize("field_name", ["package_count", "layer_count"])
def test_pure_alignment_retains_upstream_aggregate_contracts(
    source: _Source, owner: str, field_name: str
) -> None:
```

Each profile's package or layer count is coherently rehashed after incrementing it. The private alignment helper must preserve the upstream aggregate closure checks rather than relying only on zipped layers.

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasEvidenceError)
```

### `test_pure_alignment_equal_counts_and_extrema_do_not_hide_different_fids`


```python
def test_pure_alignment_equal_counts_and_extrema_do_not_hide_different_fids(
    source: _Source,
) -> None:
```

Critical pure regression: the geometry profile's valid-looking FID commitment is changed from `[1, 2, 4]` to `[1, 3, 4]`, its complete hash is recomputed, and its intrinsic validator still succeeds. Explicit assertions prove both count and extrema remain `(3, 1, 4)`; only complete sequence equality exposes the contradiction.

Direct assertions:


```python
assert geometry_module._validate_profile_intrinsic(changed) is changed

assert (
        (attribute_layer.fid_count, attribute_layer.fid_min, attribute_layer.fid_max)
        == (geometry_layer.fid_count, geometry_layer.fid_min, geometry_layer.fid_max)
        == (3, 1, 4)
    )

assert attribute_layer.fid_sequence_sha256 == _json_hash([1, 2, 4])
```

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasEvidenceError, match="FID|fid")
```

### `test_empty_negative_and_sparse_fids_align_without_renumbering`


```python
@pytest.mark.parametrize("fids", [(), (-7, 4, 99), (23,)])
def test_empty_negative_and_sparse_fids_align_without_renumbering(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, fids: tuple[int, ...]
) -> None:
```

Real physical source cases retain empty, sparse negative-containing, and singleton FID domains through build and public independent validation. Checks count/extrema and both upstream FID hashes against the independent sorted integer-sequence commitment, without renumbering.

Direct assertions:


```python
assert record.fid_count == record.feature_count == len(fids)

assert record.fid_min == (min(fids) if fids else None)

assert record.fid_max == (max(fids) if fids else None)

assert (
        record.fid_sequence_sha256
        == source.attributes.layers[0].fid_sequence_sha256
        == source.geometries.layers[0].fid_sequence_sha256
        == _json_hash(sorted(fids))
    )
```

### `test_full_package_layer_key_handles_identical_names_in_distinct_packages`


```python
def test_full_package_layer_key_handles_identical_names_in_distinct_packages(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

Real multipackage/multilayer source with two different `shared` layers proves the key includes the portable package path. Input member order is deliberately reversed; canonical package order and original within-package layer positions yield three exact alignments, including distinct FID commitments for identically named layers.

Direct assertions:


```python
assert [
        (
            item.relative_path,
            item.layer_name,
            item.package_position,
            item.layer_position,
            item.fid_count,
        )
        for item in bundle.layer_alignments
    ] == [
        ("EP/a.gpkg", "shared", 0, 0, 3),
        ("EP/a.gpkg", "second", 0, 1, 2),
        ("EP/b.gpkg", "shared", 1, 0, 2),
    ]

assert (
        bundle.layer_alignments[0].fid_sequence_sha256
        != bundle.layer_alignments[2].fid_sequence_sha256
    )
```

### `test_same_physical_rows_in_reversed_attribute_read_order_still_align`


```python
def test_same_physical_rows_in_reversed_attribute_read_order_still_align(
    source: _Source, monkeypatch: pytest.MonkeyPatch
) -> None:
```

Wraps the real attribute reader to reverse returned rows without changing cells/FIDs. The attribute profile remains equal, bundle build and public independent validation succeed, and the hook proves reversed physical read order was actually exercised.

Direct assertions:


```python
assert rebuilt == source.attributes

assert seen and all(item == (4, 2, 1) for item in seen)

assert bundle.layer_alignments[0].fid_sequence_sha256 == _json_hash([1, 2, 4])
```

Monkeypatch expressions:


```python
monkeypatch.setattr(pyogrio, "read_dataframe", reversed_rows)
```

### `test_same_physical_rows_in_reversed_attribute_read_order_still_align.reversed_rows`


```python
    def reversed_rows(*args: object, **kwargs: object) -> object:
```

Nested callback owned only by the reversed-attribute-order test. Requires the non-geometry reader flag, delegates to real Pyogrio, reverses the resulting frame, records exact FID order, and returns the altered read order for canonicalization.

Direct assertions:


```python
assert kwargs["read_geometry"] is False
```

### `test_measured_profiles_bundle_through_only_approved_readers`


```python
@pytest.mark.parametrize("layout", ["M", "ZM"])
def test_measured_profiles_bundle_through_only_approved_readers(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, layout: str
) -> None:
```

Real M and ZM source cases use independently constructed raw BLOBs. Instrumented real attribute reads require exact byte input and every approved option; instrumented real geometry parsing checks preserved M/Z flags and every expected ordinate. Build and independent validation each perform one attribute read and one full geometry pass; no geometry is materialized by Pyogrio.

Direct assertions:


```python
assert bundle.geometries == source.geometries

assert bundle.geometries.has_m_geometry_count == 2

assert bundle.geometries.has_z_geometry_count == (2 if layout == "ZM" else 0)

assert len(read_calls) == 2

assert coordinates == expected * 2
```

Monkeypatch expressions:


```python
monkeypatch.setattr(pyogrio, "read_dataframe", attribute_read)

monkeypatch.setattr(geometry_module, "_parse_gpkg_geometry_blob", geometry_parse)
```

### `test_measured_profiles_bundle_through_only_approved_readers.attribute_read`


```python
    def attribute_read(*args: object, **kwargs: object) -> object:
```

Nested callback owned by the measured-reader test. Checks immutable byte input and exact layer/column/read_geometry/FID/Arrow/datetime options, records the call, and delegates to the real attribute-only Pyogrio reader.

Direct assertions:


```python
assert type(args[0]) is bytes

assert kwargs == {
            "layer": "first",
            "columns": ["id_mnhn", "value"],
            "read_geometry": False,
            "fid_as_index": True,
            "use_arrow": False,
            "datetime_as_string": True,
        }
```

### `test_measured_profiles_bundle_through_only_approved_readers.geometry_parse`


```python
    def geometry_parse(*args: object, **kwargs: object) -> Any:
```

Nested callback owned by the measured-reader test. Delegates to the actual geometry-module parser, checks M and layout-dependent Z, and records coordinates including present Z/M; it does not normalize or fabricate geometry.

Direct assertions:


```python
assert bool(shapely.has_m(result.geometry)) is True

assert bool(shapely.has_z(result.geometry)) is (layout == "ZM")
```

### `test_portable_bundle_ignores_cache_roots_and_cache_hit_flags`


```python
def test_portable_bundle_ignores_cache_roots_and_cache_hit_flags(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

Two real temporary sources reuse identical package/ZIP bytes under distinct cache roots. Their bundles remain equal, including after validated extraction/download cache-hit flags change; independent payload JSON excludes the local path, cache state, and timestamps.

Direct assertions:


```python
assert _build(second_source) == first

assert _build(replace(second_source, extraction=cached)) == first

assert str(tmp_path) not in encoded

assert "cache_hit" not in encoded and "timestamp" not in encoded
```

### `test_coordinated_upstream_and_bundle_rehash_cannot_override_physical_bytes`


```python
@pytest.mark.parametrize("owner", ["attributes", "geometries", "both"])
def test_coordinated_upstream_and_bundle_rehash_cannot_override_physical_bytes(
    source: _Source, owner: str
) -> None:
```

Attribute row content, geometry parser content, or both are coherently forged and the bundle hash is recomputed. Cheap alignment explicitly still succeeds because the FIDs agree, but public validation fails with the lower physical attribute/geometry error preserved as cause. This is the decisive structural-versus-physical trust distinction.

Direct assertions:


```python
assert (
        evidence._align_layers(forged.catalog, forged.attributes, forged.geometries)
        == bundle.layer_alignments
    )

assert isinstance(
        captured.value.__cause__,
        (
            InpnProtectedAreasAttributeProfileError,
            InpnProtectedAreasGeometryProfileError,
        ),
    )
```

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasEvidenceError)
```

### `test_coordinated_catalog_profiles_and_bundle_rehash_cannot_override_source`


```python
def test_coordinated_catalog_profiles_and_bundle_rehash_cannot_override_source(
    source: _Source,
) -> None:
```

Coordinately renames a catalog field and its attribute field, updates both profile catalog commitments, recomputes all three upstream complete hashes and the bundle hash, and explicitly proves private alignment still succeeds. Public independent validation fails because fresh physical catalog evidence disagrees; the exception-cause chain must contain the actual catalog error.

Direct assertions:


```python
assert (
        evidence._align_layers(catalog, attributes, geometries)
        == bundle.layer_alignments
    )

assert any(isinstance(item, InpnProtectedAreasCatalogError) for item in causes)
```

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasEvidenceError)
```

### `test_rehashed_bundle_alignment_inventory_must_be_exact`


```python
@pytest.mark.parametrize("mutation", ["missing", "extra", "duplicate", "reordered"])
def test_rehashed_bundle_alignment_inventory_must_be_exact(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, mutation: str
) -> None:
```

Real two-layer baseline followed by coherent missing/extra/duplicate/reordered alignment-tuple forgeries. Independent payload hashing is explicitly closed before public validation rejects each exact inventory/order contradiction with an alignment error.

Direct assertions:


```python
assert forged.complete_evidence_bundle_content_sha256 == _json_hash(
        _expected_payload(forged)
    )
```

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasEvidenceError, match="alignment")
```

### `test_forged_alignment_record_with_rehashed_bundle_is_rejected`


```python
@pytest.mark.parametrize(
    ("field_name", "value"),
    [
        ("relative_path", "EP/other.gpkg"),
        ("package_position", 1),
        ("file_sha256", "0" * 64),
        ("layer_name", "other"),
        ("layer_position", 1),
        ("feature_count", 4),
        ("fid_count", 4),
        ("fid_min", 0),
        ("fid_max", 5),
        ("fid_sequence_sha256", "0" * 64),
    ],
)
def test_forged_alignment_record_with_rehashed_bundle_is_rejected(
    source: _Source, field_name: str, value: object
) -> None:
```

Every one of the ten alignment fields is separately changed and the independent complete bundle digest is updated. Public validation rejects contradictions against the retained upstream profiles despite exact hash closure.

Direct assertions:


```python
assert forged.complete_evidence_bundle_content_sha256 == _json_hash(
        _expected_payload(forged)
    )
```

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasEvidenceError)
```

### `test_bundle_validator_rejects_malformed_nested_runtime_evidence`


```python
@pytest.mark.parametrize(
    "mutation",
    [
        "schema-bool",
        "schema-version",
        "hash-case",
        "hash-subclass",
        "hash-stale",
        "alignments-list",
        "alignment-object",
        "alignment-subclass",
        "catalog-object",
        "attributes-object",
        "geometries-object",
        "catalog-packages-list",
        "attribute-domain-list",
        "geometry-domain-list",
    ],
)
def test_bundle_validator_rejects_malformed_nested_runtime_evidence(
    source: _Source, mutation: str
) -> None:
```

Fourteen nested/schema/hash mutations include Boolean or unsupported schema, noncanonical/stale/subclass digest, list alignments, object/subclass alignment, wrong upstream objects, mutable package tuple replacement, and mutable attribute/geometry domains. Each malformed envelope fails controlled validation.

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasEvidenceError)
```

### `test_alignment_fields_require_exact_builtin_runtime_types`


```python
@pytest.mark.parametrize(
    ("field_name", "value"),
    [
        ("relative_path", _StringSubclass("EP/one.gpkg")),
        ("package_position", False),
        ("file_sha256", _StringSubclass("0" * 64)),
        ("layer_name", _StringSubclass("first")),
        ("layer_position", False),
        ("feature_count", True),
        ("fid_count", np.int64(3)),
        ("fid_min", True),
        ("fid_max", 4.0),
        ("fid_sequence_sha256", _StringSubclass("0" * 64)),
    ],
)
def test_alignment_fields_require_exact_builtin_runtime_types(
    source: _Source, field_name: str, value: object
) -> None:
```

Every alignment field receives a noncanonical scalar representation (string subclass, Boolean, NumPy integer, or float). Immediate exact runtime-type checking rejects values even where Python equality could otherwise hide a coercion. The expected error explicitly matches `noncanonical runtime type`, so an unrelated stale digest cannot mask failure to enforce the scalar-type gate.

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(
        InpnProtectedAreasEvidenceError, match="noncanonical runtime type"
    )
```

### `test_persistent_source_mutation_after_alignment_fails_final_postcondition`


```python
@pytest.mark.parametrize("target", ["archive", "package"])
def test_persistent_source_mutation_after_alignment_fails_final_postcondition(
    source: _Source, monkeypatch: pytest.MonkeyPatch, target: str
) -> None:
```

Wraps real structural alignment, then persistently changes one byte of the archive or extracted package. The hook-executed assertion proves the mutation actually occurred after the two real physical profile validators; final extraction validation must reject it with a chained source error.

Direct assertions:


```python
assert executed

assert isinstance(captured.value.__cause__, InpnProtectedAreasSourceError)
```

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasEvidenceError)
```

Monkeypatch expressions:


```python
monkeypatch.setattr(evidence, "_align_layers", align_then_mutate)
```

### `test_persistent_source_mutation_after_alignment_fails_final_postcondition.align_then_mutate`


```python
    def align_then_mutate(*args: object, **kwargs: object) -> Any:
```

Nested fault-injection callback owned by the persistent-source-mutation test. Delegates to real alignment first, flips the last physical byte, records execution, then returns the otherwise valid alignment so the final source postcondition is decisive.

This helper/callback does not directly assert an outcome; its constructed or delegated state is checked by the owning tests.

### `test_builder_and_validator_delegate_once_per_complete_profile_not_per_layer`


```python
def test_builder_and_validator_delegate_once_per_complete_profile_not_per_layer(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

Real two-layer source and wrappers around all three public boundaries prove exact order and once-per-operation calls: attributes, geometries, final-extraction. Both public build and independent validation repeat this sequence; no per-layer validation loop or mocked trust shortcut is used.

Direct assertions:


```python
assert calls == ["attributes", "geometries", "final-extraction"]

assert calls == ["attributes", "geometries", "final-extraction"]
```

Monkeypatch expressions:


```python
monkeypatch.setattr(
        evidence, "validate_inpn_protected_areas_attribute_profile", attributes
    )

monkeypatch.setattr(
        evidence, "validate_inpn_protected_areas_geometry_profile", geometries
    )

monkeypatch.setattr(
        evidence, "validate_inpn_protected_areas_extraction", extraction
    )
```

### `test_builder_and_validator_delegate_once_per_complete_profile_not_per_layer.attributes`


```python
    def attributes(*args: object, **kwargs: object) -> None:
```

Nested delegating wrapper owned by the call-count test; records the attribute public validator once and invokes its real implementation.

This helper/callback does not directly assert an outcome; its constructed or delegated state is checked by the owning tests.

### `test_builder_and_validator_delegate_once_per_complete_profile_not_per_layer.geometries`


```python
    def geometries(*args: object, **kwargs: object) -> None:
```

Nested delegating wrapper owned by the call-count test; records the geometry public validator once and invokes its real implementation.

This helper/callback does not directly assert an outcome; its constructed or delegated state is checked by the owning tests.

### `test_builder_and_validator_delegate_once_per_complete_profile_not_per_layer.extraction`


```python
    def extraction(*args: object, **kwargs: object) -> Any:
```

Nested delegating wrapper owned by the call-count test; records the final extraction boundary and returns its real independently validated extraction.

This helper/callback does not directly assert an outcome; its constructed or delegated state is checked by the owning tests.

### `test_controlled_lower_boundary_failure_preserves_cause`


```python
@pytest.mark.parametrize(
    ("boundary", "error_type"),
    [
        (
            "validate_inpn_protected_areas_attribute_profile",
            InpnProtectedAreasAttributeProfileError,
        ),
        (
            "validate_inpn_protected_areas_attribute_profile",
            InpnProtectedAreasCatalogError,
        ),
        (
            "validate_inpn_protected_areas_geometry_profile",
            InpnProtectedAreasGeometryProfileError,
        ),
        ("validate_inpn_protected_areas_extraction", InpnProtectedAreasSourceError),
    ],
)
def test_controlled_lower_boundary_failure_preserves_cause(
    source: _Source,
    monkeypatch: pytest.MonkeyPatch,
    boundary: str,
    error_type: type[Exception],
) -> None:
```

Fault-injection test, not physical source proof: each relevant lower public boundary raises a deliberate source/catalog/attribute/geometry error with package/layer context. The public bundle builder must preserve the exact original exception as its chained cause.

Direct assertions:


```python
assert captured.value.__cause__ is error
```

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(InpnProtectedAreasEvidenceError)
```

Monkeypatch expressions:


```python
monkeypatch.setattr(evidence, boundary, fail)
```

### `test_controlled_lower_boundary_failure_preserves_cause.fail`


```python
    def fail(*args: object, **kwargs: object) -> Any:
```

Nested callback owned by the controlled-error test; raises the preconstructed lower-layer exception so cause identity can be asserted.

Direct raise statements:


```python
raise error
```

### `test_results_are_deeply_immutable_portable_profiles_not_joined_rows`


```python
def test_results_are_deeply_immutable_portable_profiles_not_joined_rows(
    source: _Source,
) -> None:
```

Recursively walks the real bundle, then verifies immediate frozen field-assignment failure for bundle and alignment. Exact dataclass field-name tuples prove no raw joined rows, operational handles, or unrequested fields were added.

Direct assertions:


```python
assert (
        tuple(field.name for field in fields(InpnProtectedAreasLayerAlignment))
        == ALIGNMENT_FIELDS
    )

assert tuple(field.name for field in fields(InpnProtectedAreasEvidenceBundle)) == (
        "evidence_bundle_schema_version",
        "catalog",
        "attributes",
        "geometries",
        "layer_alignments",
        "complete_evidence_bundle_content_sha256",
    )
```

Expected exception/warning/fatal-check expressions:


```python
pytest.raises(FrozenInstanceError)

pytest.raises(FrozenInstanceError)
```

### `test_results_are_deeply_immutable_portable_profiles_not_joined_rows.walk`


```python
    def walk(value: object) -> None:
```

Nested recursive checker owned by the immutability test. Rejects dict/list/set, bytes, paths, NumPy arrays, DataFrames, SQLite connections, and geometry-bearing values; descends dataclasses and exact tuples and permits only exact portable scalar leaves.

Direct assertions:


```python
assert not isinstance(
            value,
            (
                dict,
                list,
                set,
                bytes,
                Path,
                np.ndarray,
                pd.DataFrame,
                sqlite3.Connection,
            ),
        )

assert not hasattr(value, "geom_type")

assert type(value) in (str, int, bool, float, type(None))
```

### `test_module_exposes_only_trusted_public_boundary_and_has_no_third_reader`


```python
def test_module_exposes_only_trusted_public_boundary_and_has_no_third_reader() -> None:
```

Checks the exact five public exports and package binding identity, plus absence of private alignment/payload exports. AST inspection forbids direct geospatial/SQL/network imports and third-reader/file/network calls in the new production module; existing physical reads remain owned by the upstream public validators.

Direct assertions:


```python
assert set(evidence.__all__) == EXPECTED_EXPORTS

assert EXPECTED_EXPORTS <= set(sources.__all__)

assert all(
        getattr(sources, name) is getattr(evidence, name) for name in EXPECTED_EXPORTS
    )

assert not hasattr(sources, "_align_layers")

assert not hasattr(sources, "_bundle_payload")

assert not imports.intersection(
        {
            "pyogrio",
            "geopandas",
            "pandas",
            "sqlite3",
            "shapely",
            "requests",
            "socket",
            "urllib",
        }
    )

assert not calls.intersection(forbidden)
```

## 6. Coverage boundaries and change impact

The decisive FID-domain regression proves both profiles still have count/min/max `(3, 1, 4)` and valid intrinsic profile closure before rejecting the different `[1, 2, 4]`/`[1, 3, 4]` sequence commitments. Valid controls include `()`, `(-7, 4, 99)`, `(23,)`, reversed attribute read order, and identical layer names under distinct package paths. No contiguous-FID, positive-FID, or business-ID assumption is added.

Physical forgery tests preserve cheap alignment while changing upstream row/parser evidence or coherently changing catalog fields and every dependent complete hash. Their public failures and chained physical causes demonstrate that bundle hash closure cannot authorize different source bytes. Persistent archive/package changes occur after real profile validation and actual alignment, so final extraction validation—not an early fixture rejection—is decisive. Same-type unchecked config mutation must fail before any physical validator call.

The recursive immutability test rejects reachable list/dict/set, bytes, paths, arrays, frames, SQLite handles, and geometry values, and tests immediate frozen reassignment of bundle and alignment fields. Ten exact-type regressions explicitly require the `noncanonical runtime type` message, preventing later stale-hash errors from hiding a missing scalar check. The suite does not assert physical trust merely because an object is frozen or self-consistently hashed.

All reader/validator instrumentation has explicit ownership. The two-layer public call-count control requires exactly attribute validator -> geometry validator -> final extraction once per build and once per independent validation, not once per layer. The no-third-reader AST audit applies to the new evidence module, not to the existing approved attribute/geometry implementations. No test authorizes metadata/category interpretation, raw joined feature output, geometry transformation, or a new source acquisition.

## 7. Exact complete current file content

```python
from __future__ import annotations

import ast
import inspect
import io
import json
import sqlite3
import struct
import zipfile
from collections.abc import Iterator, Mapping
from contextlib import contextmanager
from dataclasses import (
    FrozenInstanceError,
    dataclass,
    fields,
    is_dataclass,
    replace,
)
from hashlib import sha256
from pathlib import Path
from typing import Any, ClassVar

import geopandas as gpd  # type: ignore[import-untyped]
import numpy as np
import pandas as pd  # type: ignore[import-untyped]
import pyogrio  # type: ignore[import-untyped]
import pytest
import shapely  # type: ignore[import-untyped]
import yaml
from shapely.geometry import Point  # type: ignore[import-untyped]

from landscout import sources
from landscout.sources import inpn_protected_areas_attributes_fr as attribute_module
from landscout.sources import inpn_protected_areas_catalog_fr as catalog_module
from landscout.sources import inpn_protected_areas_evidence_fr as evidence
from landscout.sources import inpn_protected_areas_fr as source_module
from landscout.sources import inpn_protected_areas_geometry_fr as geometry_module
from landscout.sources.inpn_protected_areas_attributes_fr import (
    InpnProtectedAreasAttributeProfile,
    InpnProtectedAreasAttributeProfileError,
    build_inpn_protected_areas_attribute_profile,
)
from landscout.sources.inpn_protected_areas_catalog_fr import (
    InpnProtectedAreasCatalog,
    InpnProtectedAreasCatalogError,
    build_inpn_protected_areas_catalog,
)
from landscout.sources.inpn_protected_areas_evidence_fr import (
    InpnProtectedAreasEvidenceBundle,
    InpnProtectedAreasEvidenceError,
    InpnProtectedAreasLayerAlignment,
    build_inpn_protected_areas_evidence_bundle,
    validate_inpn_protected_areas_evidence_bundle,
)
from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    download_inpn_protected_areas_archive,
    extract_inpn_protected_areas_archive,
)
from landscout.sources.inpn_protected_areas_geometry_fr import (
    InpnProtectedAreasGeometryProfile,
    InpnProtectedAreasGeometryProfileError,
    build_inpn_protected_areas_geometry_profile,
)

CONFIG_PATH = Path("configs/sources/inpn_protected_areas_fr.yaml")
EXPECTED_EXPORTS = {
    "InpnProtectedAreasEvidenceBundle",
    "InpnProtectedAreasEvidenceError",
    "InpnProtectedAreasLayerAlignment",
    "build_inpn_protected_areas_evidence_bundle",
    "validate_inpn_protected_areas_evidence_bundle",
}
ALIGNMENT_FIELDS = (
    "relative_path",
    "package_position",
    "file_sha256",
    "layer_name",
    "layer_position",
    "feature_count",
    "fid_count",
    "fid_min",
    "fid_max",
    "fid_sequence_sha256",
)
SOURCE_MUTATIONS = (
    ("provider", "other provider"),
    ("authority", "other authority"),
    ("program", "other program"),
    ("dataset_id", "other dataset"),
    ("dataset_name", "other name"),
    ("declared_version", "08/2026"),
    ("reference_page_url", "https://example.test/reference"),
    ("archive_url", "https://example.test/EP.zip"),
    ("archive_filename", "other.zip"),
    ("archive_size", 1),
    ("archive_sha256", "0" * 64),
    ("source_catalog_schema_version", 1),
    ("source_catalog_content_sha256", "0" * 64),
)


class _Response(io.BytesIO):
    headers: ClassVar[dict[str, str]] = {"Content-Type": "application/zip"}


class _StringSubclass(str):
    pass


@dataclass(frozen=True)
class _Source:
    extraction: InpnProtectedAreasExtraction
    config: InpnProtectedAreasSourceConfig
    catalog: InpnProtectedAreasCatalog
    attributes: InpnProtectedAreasAttributeProfile
    geometries: InpnProtectedAreasGeometryProfile


@contextmanager
def _response(payload: bytes) -> Iterator[_Response]:
    with _Response(payload) as response:
        yield response


def _json_hash(payload: object) -> str:
    return sha256(
        json.dumps(
            payload,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
            allow_nan=False,
        ).encode("utf-8")
    ).hexdigest()


def _point_blob(position: int, layout: str) -> bytes:
    """Fixture-only independent Standard GPB plus ISO dimensional Point WKB."""
    coordinates = (1000.0 + position, 2000.0 + position)
    if "Z" in layout:
        coordinates += (3.0,)
    if "M" in layout:
        coordinates += (4.0,)
    type_word = 1 + 1000 * int("Z" in layout) + 2000 * int("M" in layout)
    return (
        b"GP\x00\x01"
        + struct.pack("<i", 2154)
        + struct.pack(f"<BI{len(coordinates)}d", 1, type_word, *coordinates)
    )


def _package(
    tmp_path: Path,
    layers: tuple[tuple[str, tuple[int, ...]], ...] = (("first", (1, 2, 4)),),
    *,
    layout: str = "XY",
) -> bytes:
    """Write only an ordinary XY container; SQLite installs exact FIDs/raw BLOBs."""
    tmp_path.mkdir(parents=True, exist_ok=True)
    path = tmp_path / "fixture.gpkg"
    seed = gpd.GeoDataFrame(
        {"id_mnhn": ["not-the-physical-fid"], "value": ["évidence"]},
        geometry=[Point(1000, 2000)],
        crs="EPSG:2154",
    )
    for position, (name, _) in enumerate(layers):
        pyogrio.write_dataframe(
            seed,
            path,
            layer=name,
            driver="GPKG",
            append=position > 0,
            geometry_type="Unknown",
            layer_options={"SPATIAL_INDEX": "NO"},
        )
    connection = sqlite3.connect(":memory:")
    try:
        connection.deserialize(path.read_bytes())
        for name, fids in layers:
            quoted = '"' + name.replace('"', '""') + '"'
            connection.execute(f"DELETE FROM {quoted}")
            connection.executemany(
                f"INSERT INTO {quoted} (fid, geom, id_mnhn, value) VALUES (?, ?, ?, ?)",
                [
                    (
                        fid,
                        _point_blob(position, layout),
                        "same-business-id",
                        f"évidence-{fid}",
                    )
                    for position, fid in enumerate(fids)
                ],
            )
            connection.execute(
                "UPDATE gpkg_geometry_columns SET z=2,m=2 WHERE table_name=?", (name,)
            )
            if not fids:
                connection.execute(
                    "UPDATE gpkg_contents SET min_x=NULL,min_y=NULL,max_x=NULL,max_y=NULL WHERE table_name=?",
                    (name,),
                )
        connection.commit()
        return connection.serialize()
    finally:
        connection.close()


def _source(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    *,
    files: Mapping[str, bytes] | None = None,
    layers: tuple[tuple[str, tuple[int, ...]], ...] = (("first", (1, 2, 4)),),
    layout: str = "XY",
) -> _Source:
    members = (
        files
        if files is not None
        else {"EP/one.gpkg": _package(tmp_path / "p", layers, layout=layout)}
    )
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w", compression=zipfile.ZIP_STORED) as archive:
        for name, value in members.items():
            archive.writestr(zipfile.ZipInfo(name, (2026, 7, 1, 0, 0, 0)), value)
    archive_bytes = stream.getvalue()
    payload = yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))
    payload.update(
        cache_root=str(tmp_path / "c"),
        expected_archive_size_bytes=len(archive_bytes),
        expected_archive_sha256=sha256(archive_bytes).hexdigest(),
    )
    config = InpnProtectedAreasSourceConfig.model_validate(payload)
    monkeypatch.setattr(
        source_module, "open_safe_https", lambda *a, **k: _response(archive_bytes)
    )
    download = download_inpn_protected_areas_archive(config)
    extraction = extract_inpn_protected_areas_archive(download, config)
    catalog = build_inpn_protected_areas_catalog(extraction, config)
    attributes = build_inpn_protected_areas_attribute_profile(
        extraction, config, catalog
    )
    geometries = build_inpn_protected_areas_geometry_profile(
        extraction, config, catalog
    )
    return _Source(extraction, config, catalog, attributes, geometries)


@pytest.fixture
def source(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> _Source:
    return _source(tmp_path, monkeypatch)


def _build(source: _Source) -> InpnProtectedAreasEvidenceBundle:
    return build_inpn_protected_areas_evidence_bundle(
        source.extraction,
        source.config,
        source.catalog,
        source.attributes,
        source.geometries,
    )


def _rehash_profile(profile: Any, **changes: object) -> Any:
    """Pure adversarial mutation: recalculate the owning upstream hash, not trust."""
    value = replace(profile, **changes)
    if type(value) is InpnProtectedAreasAttributeProfile:
        return replace(
            value,
            complete_attribute_profile_content_sha256=attribute_module._profile_content_sha256(
                value
            ),
        )
    return replace(
        value,
        complete_geometry_profile_content_sha256=geometry_module._profile_content_sha256(
            value
        ),
    )


def _profile_layers(profile: Any, layers: tuple[Any, ...]) -> Any:
    """Coherently close aggregate counts for pure layer-inventory contradictions."""
    counts = {
        "package_count": len({item.package_position for item in layers}),
        "layer_count": len(layers),
    }
    if type(profile) is InpnProtectedAreasAttributeProfile:
        counts.update(
            field_definition_count=sum(len(item.fields) for item in layers),
            total_row_count=sum(item.feature_count for item in layers),
            total_null_count=sum(
                field.null_count for item in layers for field in item.fields
            ),
            total_distinct_non_null_value_count=sum(
                field.distinct_non_null_count
                for item in layers
                for field in item.fields
            ),
        )
    else:
        names = (
            "null_geometry_count",
            "empty_geometry_count",
            "non_empty_geometry_count",
            "valid_non_empty_geometry_count",
            "invalid_non_empty_geometry_count",
            "has_z_geometry_count",
            "has_m_geometry_count",
            "total_coordinate_count",
        )
        counts.update(
            {name: sum(getattr(item, name) for item in layers) for name in names}
        )
        counts["geometry_row_count"] = sum(item.feature_count for item in layers)
    return _rehash_profile(profile, layers=layers, **counts)


def _expected_payload(bundle: InpnProtectedAreasEvidenceBundle) -> dict[str, object]:
    """Independent specification of the compact bundle payload, never domains."""
    return {
        "evidence_bundle_schema_version": bundle.evidence_bundle_schema_version,
        "catalog": {
            "catalog_schema_version": bundle.catalog.catalog_schema_version,
            "complete_catalog_content_sha256": bundle.catalog.complete_catalog_content_sha256,
        },
        "attributes": {
            "attribute_profile_schema_version": bundle.attributes.attribute_profile_schema_version,
            "complete_attribute_profile_content_sha256": bundle.attributes.complete_attribute_profile_content_sha256,
        },
        "geometries": {
            "geometry_profile_schema_version": bundle.geometries.geometry_profile_schema_version,
            "complete_geometry_profile_content_sha256": bundle.geometries.complete_geometry_profile_content_sha256,
        },
        "layer_alignments": [
            {name: getattr(item, name) for name in ALIGNMENT_FIELDS}
            for item in bundle.layer_alignments
        ],
    }


def _rehash_bundle(
    bundle: InpnProtectedAreasEvidenceBundle, **changes: object
) -> InpnProtectedAreasEvidenceBundle:
    changed = replace(bundle, **changes)
    return replace(
        changed,
        complete_evidence_bundle_content_sha256=_json_hash(_expected_payload(changed)),
    )


def _subclass(value: Any) -> Any:
    cls = type(f"NonExact{type(value).__name__}", (type(value),), {})
    if isinstance(value, InpnProtectedAreasSourceConfig):
        return cls.model_validate(value.model_dump(mode="python"))
    return cls(**{field.name: getattr(value, field.name) for field in fields(value)})


def test_complete_bundle_is_deterministic_and_independently_validated(
    source: _Source,
) -> None:
    first = _build(source)
    assert _build(source) == first
    validate_inpn_protected_areas_evidence_bundle(
        source.extraction, source.config, first
    )
    assert type(first) is InpnProtectedAreasEvidenceBundle
    assert (
        first.evidence_bundle_schema_version
        == evidence.EVIDENCE_BUNDLE_SCHEMA_VERSION
        == 1
    )
    assert (first.catalog, first.attributes, first.geometries) == (
        source.catalog,
        source.attributes,
        source.geometries,
    )
    assert len(first.layer_alignments) == 1
    alignment = first.layer_alignments[0]
    assert type(alignment) is InpnProtectedAreasLayerAlignment
    assert alignment == InpnProtectedAreasLayerAlignment(
        "EP/one.gpkg",
        0,
        source.catalog.packages[0].file_sha256,
        "first",
        0,
        3,
        3,
        1,
        4,
        _json_hash([1, 2, 4]),
    )
    assert evidence._bundle_payload(first) == _expected_payload(first)
    assert first.complete_evidence_bundle_content_sha256 == _json_hash(
        _expected_payload(first)
    )
    assert set(_expected_payload(first)["attributes"]) == {
        "attribute_profile_schema_version",
        "complete_attribute_profile_content_sha256",
    }


@pytest.mark.parametrize(
    "argument", ["extraction", "config", "catalog", "attributes", "geometries"]
)
@pytest.mark.parametrize("kind", ["object", "subclass"])
def test_builder_requires_exact_public_input_types(
    source: _Source, argument: str, kind: str
) -> None:
    inputs = {field.name: getattr(source, field.name) for field in fields(source)}
    inputs[argument] = object() if kind == "object" else _subclass(inputs[argument])
    with pytest.raises(InpnProtectedAreasEvidenceError):
        build_inpn_protected_areas_evidence_bundle(**inputs)


@pytest.mark.parametrize("argument", ["extraction", "config", "bundle"])
@pytest.mark.parametrize("kind", ["object", "subclass"])
def test_validator_requires_exact_public_input_types(
    source: _Source, argument: str, kind: str
) -> None:
    inputs = {
        "extraction": source.extraction,
        "config": source.config,
        "bundle": _build(source),
    }
    inputs[argument] = object() if kind == "object" else _subclass(inputs[argument])
    with pytest.raises(InpnProtectedAreasEvidenceError):
        validate_inpn_protected_areas_evidence_bundle(**inputs)


@pytest.mark.parametrize("boundary", ["builder", "validator"])
def test_public_boundaries_reconstruct_same_type_config_before_physical_validation(
    source: _Source, monkeypatch: pytest.MonkeyPatch, boundary: str
) -> None:
    bundle = _build(source)
    forged_config = source.config.model_copy(
        update={"expected_archive_size_bytes": True}
    )
    assert type(forged_config) is InpnProtectedAreasSourceConfig
    calls: list[str] = []
    original = evidence.validate_inpn_protected_areas_attribute_profile

    def observed(*args: object, **kwargs: object) -> None:
        calls.append("attributes")
        original(*args, **kwargs)

    monkeypatch.setattr(
        evidence, "validate_inpn_protected_areas_attribute_profile", observed
    )
    with pytest.raises(InpnProtectedAreasEvidenceError, match="config is invalid"):
        if boundary == "builder":
            _build(replace(source, config=forged_config))
        else:
            validate_inpn_protected_areas_evidence_bundle(
                source.extraction, forged_config, bundle
            )
    assert calls == []


@pytest.mark.parametrize("owner", ["attributes", "geometries"])
@pytest.mark.parametrize(("field_name", "value"), SOURCE_MUTATIONS)
def test_pure_alignment_rejects_source_archive_catalog_identity_mismatches(
    source: _Source, owner: str, field_name: str, value: object
) -> None:
    """Structural-only contradictory profiles; this is not physical source proof."""
    changed = replace(
        source,
        **{owner: _rehash_profile(getattr(source, owner), **{field_name: value})},
    )
    with pytest.raises(InpnProtectedAreasEvidenceError):
        evidence._align_layers(changed.catalog, changed.attributes, changed.geometries)


@pytest.mark.parametrize("owner", ["attributes", "geometries"])
@pytest.mark.parametrize("mutation", ["missing", "extra", "duplicate", "reordered"])
def test_pure_alignment_rejects_layer_inventory_changes(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, owner: str, mutation: str
) -> None:
    """Pure inventory combinations are impossible together on one trusted source."""
    source = _source(
        tmp_path, monkeypatch, layers=(("z_first", (1, 2, 4)), ("a_second", (8, 9)))
    )
    profile = getattr(source, owner)
    layers = profile.layers
    if mutation == "missing":
        layers = layers[:1]
    elif mutation == "extra":
        layers += (replace(layers[0], layer_name="extra", layer_position=2),)
    elif mutation == "duplicate":
        layers = (layers[0], replace(layers[0], layer_position=1))
    else:
        layers = tuple(
            replace(layer, layer_position=position)
            for position, layer in enumerate(reversed(layers))
        )
    changed = replace(source, **{owner: _profile_layers(profile, layers)})
    with pytest.raises(InpnProtectedAreasEvidenceError):
        evidence._align_layers(changed.catalog, changed.attributes, changed.geometries)


@pytest.mark.parametrize("owner", ["attributes", "geometries"])
@pytest.mark.parametrize(
    ("field_name", "value"),
    [
        ("relative_path", "EP/other.gpkg"),
        ("file_size", 1),
        ("file_sha256", "0" * 64),
        ("package_position", 1),
        ("driver_name", "SQLite"),
        ("layer_name", "other"),
        ("layer_position", 1),
        ("feature_count", 4),
        ("fid_count", 4),
        ("fid_min", -1),
        ("fid_max", 5),
        ("fid_sequence_sha256", "0" * 64),
    ],
)
def test_pure_alignment_rejects_package_layer_and_fid_contradictions(
    source: _Source, owner: str, field_name: str, value: object
) -> None:
    """Coherently rehashed input contradictions exercise only the cheap helper."""
    profile = getattr(source, owner)
    layer = replace(profile.layers[0], **{field_name: value})
    changed = replace(source, **{owner: _rehash_profile(profile, layers=(layer,))})
    with pytest.raises(InpnProtectedAreasEvidenceError):
        evidence._align_layers(changed.catalog, changed.attributes, changed.geometries)


@pytest.mark.parametrize("owner", ["attributes", "geometries"])
@pytest.mark.parametrize("field_name", ["package_count", "layer_count"])
def test_pure_alignment_retains_upstream_aggregate_contracts(
    source: _Source, owner: str, field_name: str
) -> None:
    changed = replace(
        source, **{owner: _rehash_profile(getattr(source, owner), **{field_name: 2})}
    )
    with pytest.raises(InpnProtectedAreasEvidenceError):
        evidence._align_layers(changed.catalog, changed.attributes, changed.geometries)


def test_pure_alignment_equal_counts_and_extrema_do_not_hide_different_fids(
    source: _Source,
) -> None:
    """[1,2,4] and [1,3,4] cannot be one physical pair despite equal ranges."""
    geometry_layer = replace(
        source.geometries.layers[0], fid_sequence_sha256=_json_hash([1, 3, 4])
    )
    changed = _rehash_profile(source.geometries, layers=(geometry_layer,))
    assert geometry_module._validate_profile_intrinsic(changed) is changed
    attribute_layer = source.attributes.layers[0]
    assert (
        (attribute_layer.fid_count, attribute_layer.fid_min, attribute_layer.fid_max)
        == (geometry_layer.fid_count, geometry_layer.fid_min, geometry_layer.fid_max)
        == (3, 1, 4)
    )
    assert attribute_layer.fid_sequence_sha256 == _json_hash([1, 2, 4])
    with pytest.raises(InpnProtectedAreasEvidenceError, match="FID|fid"):
        evidence._align_layers(source.catalog, source.attributes, changed)


@pytest.mark.parametrize("fids", [(), (-7, 4, 99), (23,)])
def test_empty_negative_and_sparse_fids_align_without_renumbering(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, fids: tuple[int, ...]
) -> None:
    source = _source(tmp_path, monkeypatch, layers=(("first", fids),))
    bundle = _build(source)
    validate_inpn_protected_areas_evidence_bundle(
        source.extraction, source.config, bundle
    )
    record = bundle.layer_alignments[0]
    assert record.fid_count == record.feature_count == len(fids)
    assert record.fid_min == (min(fids) if fids else None)
    assert record.fid_max == (max(fids) if fids else None)
    assert (
        record.fid_sequence_sha256
        == source.attributes.layers[0].fid_sequence_sha256
        == source.geometries.layers[0].fid_sequence_sha256
        == _json_hash(sorted(fids))
    )


def test_full_package_layer_key_handles_identical_names_in_distinct_packages(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    first = _package(tmp_path / "a", (("shared", (1, 2, 4)), ("second", (8, 9))))
    other = _package(tmp_path / "b", (("shared", (17, 41)),))
    source = _source(
        tmp_path / "s", monkeypatch, files={"EP/b.gpkg": other, "EP/a.gpkg": first}
    )
    bundle = _build(source)
    validate_inpn_protected_areas_evidence_bundle(
        source.extraction, source.config, bundle
    )
    assert [
        (
            item.relative_path,
            item.layer_name,
            item.package_position,
            item.layer_position,
            item.fid_count,
        )
        for item in bundle.layer_alignments
    ] == [
        ("EP/a.gpkg", "shared", 0, 0, 3),
        ("EP/a.gpkg", "second", 0, 1, 2),
        ("EP/b.gpkg", "shared", 1, 0, 2),
    ]
    assert (
        bundle.layer_alignments[0].fid_sequence_sha256
        != bundle.layer_alignments[2].fid_sequence_sha256
    )


def test_same_physical_rows_in_reversed_attribute_read_order_still_align(
    source: _Source, monkeypatch: pytest.MonkeyPatch
) -> None:
    original = pyogrio.read_dataframe
    seen: list[tuple[int, ...]] = []

    def reversed_rows(*args: object, **kwargs: object) -> object:
        assert kwargs["read_geometry"] is False
        frame = original(*args, **kwargs)
        reverse = frame.iloc[::-1]
        seen.append(tuple(reverse.index.tolist()))
        return reverse

    monkeypatch.setattr(pyogrio, "read_dataframe", reversed_rows)
    rebuilt = build_inpn_protected_areas_attribute_profile(
        source.extraction, source.config, source.catalog
    )
    assert rebuilt == source.attributes
    bundle = _build(replace(source, attributes=rebuilt))
    validate_inpn_protected_areas_evidence_bundle(
        source.extraction, source.config, bundle
    )
    assert seen and all(item == (4, 2, 1) for item in seen)
    assert bundle.layer_alignments[0].fid_sequence_sha256 == _json_hash([1, 2, 4])


@pytest.mark.parametrize("layout", ["M", "ZM"])
def test_measured_profiles_bundle_through_only_approved_readers(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, layout: str
) -> None:
    source = _source(tmp_path, monkeypatch, layers=(("first", (8, 21)),), layout=layout)
    original_read = pyogrio.read_dataframe
    original_parse = geometry_module._parse_gpkg_geometry_blob
    read_calls: list[dict[str, object]] = []
    coordinates: list[list[list[float]]] = []

    def attribute_read(*args: object, **kwargs: object) -> object:
        assert type(args[0]) is bytes
        assert kwargs == {
            "layer": "first",
            "columns": ["id_mnhn", "value"],
            "read_geometry": False,
            "fid_as_index": True,
            "use_arrow": False,
            "datetime_as_string": True,
        }
        read_calls.append(kwargs)
        return original_read(*args, **kwargs)

    def geometry_parse(*args: object, **kwargs: object) -> Any:
        result = original_parse(*args, **kwargs)
        assert bool(shapely.has_m(result.geometry)) is True
        assert bool(shapely.has_z(result.geometry)) is (layout == "ZM")
        coordinates.append(
            shapely.get_coordinates(
                result.geometry, include_z=layout == "ZM", include_m=True
            ).tolist()
        )
        return result

    monkeypatch.setattr(pyogrio, "read_dataframe", attribute_read)
    monkeypatch.setattr(geometry_module, "_parse_gpkg_geometry_blob", geometry_parse)
    bundle = _build(source)
    validate_inpn_protected_areas_evidence_bundle(
        source.extraction, source.config, bundle
    )
    assert bundle.geometries == source.geometries
    assert bundle.geometries.has_m_geometry_count == 2
    assert bundle.geometries.has_z_geometry_count == (2 if layout == "ZM" else 0)
    assert len(read_calls) == 2
    expected = [
        [[1000.0 + index, 2000.0 + index, *([3.0] if layout == "ZM" else []), 4.0]]
        for index in range(2)
    ]
    assert coordinates == expected * 2


def test_portable_bundle_ignores_cache_roots_and_cache_hit_flags(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    package = _package(tmp_path / "p")
    first_source = _source(tmp_path / "a", monkeypatch, files={"EP/one.gpkg": package})
    second_source = _source(tmp_path / "b", monkeypatch, files={"EP/one.gpkg": package})
    first = _build(first_source)
    assert _build(second_source) == first
    cached = replace(
        second_source.extraction,
        cache_hit=True,
        download=replace(second_source.extraction.download, cache_hit=True),
    )
    assert _build(replace(second_source, extraction=cached)) == first
    encoded = json.dumps(_expected_payload(first), ensure_ascii=False)
    assert str(tmp_path) not in encoded
    assert "cache_hit" not in encoded and "timestamp" not in encoded


@pytest.mark.parametrize("owner", ["attributes", "geometries", "both"])
def test_coordinated_upstream_and_bundle_rehash_cannot_override_physical_bytes(
    source: _Source, owner: str
) -> None:
    bundle = _build(source)
    changes: dict[str, object] = {}
    if owner in ("attributes", "both"):
        layer = replace(bundle.attributes.layers[0], row_content_sha256="0" * 64)
        changes["attributes"] = _rehash_profile(bundle.attributes, layers=(layer,))
    if owner in ("geometries", "both"):
        layer = replace(bundle.geometries.layers[0], geometry_content_sha256="0" * 64)
        changes["geometries"] = _rehash_profile(bundle.geometries, layers=(layer,))
    forged = _rehash_bundle(bundle, **changes)
    assert (
        evidence._align_layers(forged.catalog, forged.attributes, forged.geometries)
        == bundle.layer_alignments
    )
    with pytest.raises(InpnProtectedAreasEvidenceError) as captured:
        validate_inpn_protected_areas_evidence_bundle(
            source.extraction, source.config, forged
        )
    assert isinstance(
        captured.value.__cause__,
        (
            InpnProtectedAreasAttributeProfileError,
            InpnProtectedAreasGeometryProfileError,
        ),
    )


def test_coordinated_catalog_profiles_and_bundle_rehash_cannot_override_source(
    source: _Source,
) -> None:
    bundle = _build(source)
    package = bundle.catalog.packages[0]
    layer = package.layers[0]
    forged_layer = replace(
        layer, fields=(replace(layer.fields[0], name="forged"), *layer.fields[1:])
    )
    catalog = replace(
        bundle.catalog, packages=(replace(package, layers=(forged_layer,)),)
    )
    catalog = replace(
        catalog,
        complete_catalog_content_sha256=catalog_module._catalog_content_sha256(catalog),
    )
    attribute_layer = bundle.attributes.layers[0]
    attributes = _rehash_profile(
        bundle.attributes,
        source_catalog_content_sha256=catalog.complete_catalog_content_sha256,
        layers=(
            replace(
                attribute_layer,
                fields=(
                    replace(attribute_layer.fields[0], name="forged"),
                    *attribute_layer.fields[1:],
                ),
            ),
        ),
    )
    geometries = _rehash_profile(
        bundle.geometries,
        source_catalog_content_sha256=catalog.complete_catalog_content_sha256,
    )
    forged = _rehash_bundle(
        bundle, catalog=catalog, attributes=attributes, geometries=geometries
    )
    assert (
        evidence._align_layers(catalog, attributes, geometries)
        == bundle.layer_alignments
    )
    with pytest.raises(InpnProtectedAreasEvidenceError) as captured:
        validate_inpn_protected_areas_evidence_bundle(
            source.extraction, source.config, forged
        )
    causes: list[BaseException] = []
    cause = captured.value.__cause__
    while cause is not None:
        causes.append(cause)
        cause = cause.__cause__
    assert any(isinstance(item, InpnProtectedAreasCatalogError) for item in causes)


@pytest.mark.parametrize("mutation", ["missing", "extra", "duplicate", "reordered"])
def test_rehashed_bundle_alignment_inventory_must_be_exact(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, mutation: str
) -> None:
    source = _source(
        tmp_path, monkeypatch, layers=(("z_first", (1, 2, 4)), ("a_second", (8, 9)))
    )
    bundle = _build(source)
    first, second = bundle.layer_alignments
    alternatives = {
        "missing": (first,),
        "extra": (first, second, replace(second, layer_name="extra", layer_position=2)),
        "duplicate": (first, first),
        "reordered": (second, first),
    }
    forged = _rehash_bundle(bundle, layer_alignments=alternatives[mutation])
    assert forged.complete_evidence_bundle_content_sha256 == _json_hash(
        _expected_payload(forged)
    )
    with pytest.raises(InpnProtectedAreasEvidenceError, match="alignment"):
        validate_inpn_protected_areas_evidence_bundle(
            source.extraction, source.config, forged
        )


@pytest.mark.parametrize(
    ("field_name", "value"),
    [
        ("relative_path", "EP/other.gpkg"),
        ("package_position", 1),
        ("file_sha256", "0" * 64),
        ("layer_name", "other"),
        ("layer_position", 1),
        ("feature_count", 4),
        ("fid_count", 4),
        ("fid_min", 0),
        ("fid_max", 5),
        ("fid_sequence_sha256", "0" * 64),
    ],
)
def test_forged_alignment_record_with_rehashed_bundle_is_rejected(
    source: _Source, field_name: str, value: object
) -> None:
    bundle = _build(source)
    forged = _rehash_bundle(
        bundle,
        layer_alignments=(replace(bundle.layer_alignments[0], **{field_name: value}),),
    )
    assert forged.complete_evidence_bundle_content_sha256 == _json_hash(
        _expected_payload(forged)
    )
    with pytest.raises(InpnProtectedAreasEvidenceError):
        validate_inpn_protected_areas_evidence_bundle(
            source.extraction, source.config, forged
        )


@pytest.mark.parametrize(
    "mutation",
    [
        "schema-bool",
        "schema-version",
        "hash-case",
        "hash-subclass",
        "hash-stale",
        "alignments-list",
        "alignment-object",
        "alignment-subclass",
        "catalog-object",
        "attributes-object",
        "geometries-object",
        "catalog-packages-list",
        "attribute-domain-list",
        "geometry-domain-list",
    ],
)
def test_bundle_validator_rejects_malformed_nested_runtime_evidence(
    source: _Source, mutation: str
) -> None:
    bundle = _build(source)
    changes: dict[str, object]
    if mutation.startswith("schema"):
        changes = {
            "evidence_bundle_schema_version": True if mutation == "schema-bool" else 2
        }
    elif mutation.startswith("hash"):
        values = {
            "hash-case": "A" * 64,
            "hash-subclass": _StringSubclass(
                bundle.complete_evidence_bundle_content_sha256
            ),
            "hash-stale": "0" * 64,
        }
        changes = {"complete_evidence_bundle_content_sha256": values[mutation]}
    elif mutation == "alignments-list":
        changes = {"layer_alignments": list(bundle.layer_alignments)}
    elif mutation in ("alignment-object", "alignment-subclass"):
        changes = {
            "layer_alignments": (
                object()
                if mutation == "alignment-object"
                else _subclass(bundle.layer_alignments[0]),
            )
        }
    elif mutation.endswith("-object"):
        changes = {mutation.removesuffix("-object"): object()}
    elif mutation == "catalog-packages-list":
        changes = {
            "catalog": replace(bundle.catalog, packages=list(bundle.catalog.packages))
        }
    elif mutation == "attribute-domain-list":
        profile = bundle.attributes
        field = replace(
            profile.layers[0].fields[0],
            distinct_values=list(profile.layers[0].fields[0].distinct_values),
        )
        layer = replace(
            profile.layers[0], fields=(field, *profile.layers[0].fields[1:])
        )
        changes = {"attributes": _rehash_profile(profile, layers=(layer,))}
    else:
        profile = bundle.geometries
        layer = replace(
            profile.layers[0],
            geometry_type_counts=list(profile.layers[0].geometry_type_counts),
        )
        changes = {"geometries": _rehash_profile(profile, layers=(layer,))}
    with pytest.raises(InpnProtectedAreasEvidenceError):
        validate_inpn_protected_areas_evidence_bundle(
            source.extraction, source.config, replace(bundle, **changes)
        )


@pytest.mark.parametrize(
    ("field_name", "value"),
    [
        ("relative_path", _StringSubclass("EP/one.gpkg")),
        ("package_position", False),
        ("file_sha256", _StringSubclass("0" * 64)),
        ("layer_name", _StringSubclass("first")),
        ("layer_position", False),
        ("feature_count", True),
        ("fid_count", np.int64(3)),
        ("fid_min", True),
        ("fid_max", 4.0),
        ("fid_sequence_sha256", _StringSubclass("0" * 64)),
    ],
)
def test_alignment_fields_require_exact_builtin_runtime_types(
    source: _Source, field_name: str, value: object
) -> None:
    bundle = _build(source)
    forged = replace(
        bundle,
        layer_alignments=(replace(bundle.layer_alignments[0], **{field_name: value}),),
    )
    with pytest.raises(
        InpnProtectedAreasEvidenceError, match="noncanonical runtime type"
    ):
        validate_inpn_protected_areas_evidence_bundle(
            source.extraction, source.config, forged
        )


@pytest.mark.parametrize("target", ["archive", "package"])
def test_persistent_source_mutation_after_alignment_fails_final_postcondition(
    source: _Source, monkeypatch: pytest.MonkeyPatch, target: str
) -> None:
    original = evidence._align_layers
    path = (
        source.extraction.download.path
        if target == "archive"
        else source.extraction.extraction_path / "EP" / "one.gpkg"
    )
    executed = False

    def align_then_mutate(*args: object, **kwargs: object) -> Any:
        nonlocal executed
        result = original(*args, **kwargs)
        payload = path.read_bytes()
        path.write_bytes(payload[:-1] + bytes([payload[-1] ^ 1]))
        executed = True
        return result

    monkeypatch.setattr(evidence, "_align_layers", align_then_mutate)
    with pytest.raises(InpnProtectedAreasEvidenceError) as captured:
        _build(source)
    assert executed
    assert isinstance(captured.value.__cause__, InpnProtectedAreasSourceError)


def test_builder_and_validator_delegate_once_per_complete_profile_not_per_layer(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    source = _source(
        tmp_path, monkeypatch, layers=(("first", (1, 2)), ("second", (8, 21)))
    )
    calls: list[str] = []
    original_attribute = evidence.validate_inpn_protected_areas_attribute_profile
    original_geometry = evidence.validate_inpn_protected_areas_geometry_profile
    original_source = evidence.validate_inpn_protected_areas_extraction

    def attributes(*args: object, **kwargs: object) -> None:
        calls.append("attributes")
        original_attribute(*args, **kwargs)

    def geometries(*args: object, **kwargs: object) -> None:
        calls.append("geometries")
        original_geometry(*args, **kwargs)

    def extraction(*args: object, **kwargs: object) -> Any:
        calls.append("final-extraction")
        return original_source(*args, **kwargs)

    monkeypatch.setattr(
        evidence, "validate_inpn_protected_areas_attribute_profile", attributes
    )
    monkeypatch.setattr(
        evidence, "validate_inpn_protected_areas_geometry_profile", geometries
    )
    monkeypatch.setattr(
        evidence, "validate_inpn_protected_areas_extraction", extraction
    )
    bundle = _build(source)
    assert calls == ["attributes", "geometries", "final-extraction"]
    calls.clear()
    validate_inpn_protected_areas_evidence_bundle(
        source.extraction, source.config, bundle
    )
    assert calls == ["attributes", "geometries", "final-extraction"]


@pytest.mark.parametrize(
    ("boundary", "error_type"),
    [
        (
            "validate_inpn_protected_areas_attribute_profile",
            InpnProtectedAreasAttributeProfileError,
        ),
        (
            "validate_inpn_protected_areas_attribute_profile",
            InpnProtectedAreasCatalogError,
        ),
        (
            "validate_inpn_protected_areas_geometry_profile",
            InpnProtectedAreasGeometryProfileError,
        ),
        ("validate_inpn_protected_areas_extraction", InpnProtectedAreasSourceError),
    ],
)
def test_controlled_lower_boundary_failure_preserves_cause(
    source: _Source,
    monkeypatch: pytest.MonkeyPatch,
    boundary: str,
    error_type: type[Exception],
) -> None:
    """Fault injection tests error translation, not physical source trust."""
    error = error_type("package EP/one.gpkg layer first: deliberate boundary failure")

    def fail(*args: object, **kwargs: object) -> Any:
        raise error

    monkeypatch.setattr(evidence, boundary, fail)
    with pytest.raises(InpnProtectedAreasEvidenceError) as captured:
        _build(source)
    assert captured.value.__cause__ is error


def test_results_are_deeply_immutable_portable_profiles_not_joined_rows(
    source: _Source,
) -> None:
    bundle = _build(source)

    def walk(value: object) -> None:
        assert not isinstance(
            value,
            (
                dict,
                list,
                set,
                bytes,
                Path,
                np.ndarray,
                pd.DataFrame,
                sqlite3.Connection,
            ),
        )
        assert not hasattr(value, "geom_type")
        if is_dataclass(value) and not isinstance(value, type):
            for field in fields(value):
                walk(getattr(value, field.name))
        elif type(value) is tuple:
            for item in value:
                walk(item)
        else:
            assert type(value) in (str, int, bool, float, type(None))

    walk(bundle)
    with pytest.raises(FrozenInstanceError):
        bundle.layer_alignments = ()
    with pytest.raises(FrozenInstanceError):
        bundle.layer_alignments[0].fid_count = 999
    assert (
        tuple(field.name for field in fields(InpnProtectedAreasLayerAlignment))
        == ALIGNMENT_FIELDS
    )
    assert tuple(field.name for field in fields(InpnProtectedAreasEvidenceBundle)) == (
        "evidence_bundle_schema_version",
        "catalog",
        "attributes",
        "geometries",
        "layer_alignments",
        "complete_evidence_bundle_content_sha256",
    )


def test_module_exposes_only_trusted_public_boundary_and_has_no_third_reader() -> None:
    assert set(evidence.__all__) == EXPECTED_EXPORTS
    assert EXPECTED_EXPORTS <= set(sources.__all__)
    assert all(
        getattr(sources, name) is getattr(evidence, name) for name in EXPECTED_EXPORTS
    )
    assert not hasattr(sources, "_align_layers")
    assert not hasattr(sources, "_bundle_payload")
    tree = ast.parse(inspect.getsource(evidence))
    imports = {
        name.name.split(".")[0]
        for node in ast.walk(tree)
        if isinstance(node, ast.Import)
        for name in node.names
    }
    imports.update(
        node.module.split(".")[0]
        for node in ast.walk(tree)
        if isinstance(node, ast.ImportFrom) and node.module
    )
    assert not imports.intersection(
        {
            "pyogrio",
            "geopandas",
            "pandas",
            "sqlite3",
            "shapely",
            "requests",
            "socket",
            "urllib",
        }
    )
    forbidden = {
        "read_dataframe",
        "read_file",
        "read_arrow",
        "open_arrow",
        "execute",
        "deserialize",
        "from_wkb",
        "read_bytes",
        "open_safe_https",
        "download_inpn_protected_areas_archive",
    }
    calls = {
        node.func.attr if isinstance(node.func, ast.Attribute) else node.func.id
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, (ast.Attribute, ast.Name))
    }
    assert not calls.intersection(forbidden)
```
