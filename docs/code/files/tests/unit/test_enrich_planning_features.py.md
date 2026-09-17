# `tests/unit/test_enrich_planning_features.py`

## File identity and evidence scope

- Repository path: `tests/unit/test_enrich_planning_features.py`
- Source SHA256: `f742a30c7921e83fd28114c7419ba0d4c2ca36aa0aed5d04c8881cad1feaef57`
- Source SHA256 basis: `git-content`
- Binding convention: `SHA256_OF_EXACT_GIT_CONTENT_BYTES`; complete exact snapshot below.
- Navigation: [unchanged test](../../../../../tests/unit/test_enrich_planning_features.py), [source companion](../../src/landscout/stages/enrich_planning_features.py.md), [R3 receipt](../../../audit/R3_PLANNING_FEATURES.md), [technical index](../../../README.md).
- 122 existing AST symbols: 98 top-level test definitions, 20 top-level helpers and four nested substitutes; zero pytest.fixture decorators. Parametrization expands to 183 cases. These are not 183 separate definitions.

R3 ran this unchanged file once: **183 passed, 2 warnings, 64.14 s; native exit 0
including cleanup**, no failures/skips/xfails/deselections. Exact command/base and
both warnings are retained in the R3 receipt. This is not the full application suite.

[R3.1](../../../audit/R3_1_PLANNING_FIDELITY.md) corrects the specific fixture,
call-order and branch-scope contradictions found by independent R3 review, plus
the bounded helper clarification recorded there. All 122 notices were cross-checked
against unchanged test bodies; no new pytest execution or independent acceptance
is claimed. R3.1 review remains pending.

## Fixture provenance, imports and effects

The builder and public validator are real calls into the unchanged stage; the
private _validate_result is deliberately used by several contract tests.
The shared intrinsic validator belongs to common.planning_feature_contract,
not the stage. GPU models, config validation/discovery, Pyogrio reader and
revalidation functions belong to sources.gpu_fr. stages is imported only for
reexport assertions. GeoPandas/pandas equality helpers supplement AST assert
statements; a zero assert-statement count need not mean no pytest assertion.

Constants are synthetic: DOCUMENT_ID=doc-1, ARCHIVE_NAME=31395_PLU_20240215,
ARCHIVE_SHA=`"a" * 64`, STANDARD=CNIG PLU v2017; LOCAL_ENGINEERING_CRS declares
a local Cartesian engineering CRS used to provoke a transformation failure.
These are not pinned official snapshot identities.

The helpers write real GPKG/Shapefile bytes, read them with the real installed
GeoPandas/Pyogrio stack, calculate inventories and write schema-2 extraction
markers. They load checked-in GPU YAML, specialize role tokens locally, validate
the config and hash it. The archive object is fabricated with a non-acquired ZIP
path and repeated-character SHA; no actual official archive is downloaded/opened.
_parcels starts in EPSG:2154 with 100 m2 square, non-default index and an existing
fact; most source fixtures start in 2154. Relevant variants are explained below.

No fixture invokes the HTTP acquisition path; real DNS/network are not required.
There is no blanket network-blocking monkeypatch in this unchanged test file.
Some roots are tempfile.mkdtemp rather than tmp_path and no cleanup fixture is
declared here; a successful native pytest cleanup exit does not prove those roots
were removed. Parquet round trips and import-isolation child processes are real
local IO. No official-source correctness, GPU/EP prevalence or acquisition
attestation follows from these synthetic source envelopes.

Only four nested substitutes are defined: a real-read FID spy, forced sjoin
failure, synthetic link detector and real-read/changed-returned-FID wrapper.
They do not all mock physical revalidation. Sidecar/attribute/geometry byte
rewrites are distinguished from envelope-only mutations and return-value patches
in the per-symbol explanations.

## Assertion limits and retained findings

- R3-T01: object casts in strict relation-count/seven semantic attacks fail the
  canonical dtype gate first. The five parcel-summary attacks differ: private
  _validate_result reaches its scalar summary guard. For source summary counts,
  True equals 1 in GPU dataclass comparison and reaches stage strict checking;
  the other four cases fail fresh-summary comparison earlier.
- R3-T02: copied global feature ID and the two “coherently renamed” cases break
  deterministic identity before cross-catalog/global/fresh-identity comparisons.
  They do not prove the downstream branch named by the test.
- R3-T03: dropping a relation retains a RangeIndex starting at 1, rejected before
  reconstruction; adding a false row reaches reconstruction but fails rebuilt
  index equality before the explicit count guard. Reordered rows reset their
  index and do reach ordered-cell comparison.
- R3-T04: removing a role/reference/sidecar or changing file size/hash can fail
  config-discovery or whole-extraction-manifest gates before selected-dataset
  containment/family checks. Each below states the actual distinction.
- Positive-case limits: “identical schemas” compares only ordered columns;
  result independence checks saved relations against selected original inputs;
  geometry tests cover XYZ, not M/ZM; sidecar tests do not enumerate every suffix;
  link detection and returned FIDs are simulated, not OS-link/disk-FID changes.
  There is no dedicated A-003 padded-label regression, tiny-tolerance edge case
  or comprehensive zero-parcel public case here.

These are bounded documentation/test-evidence findings, not proof of a new
application defect and not authorization to rewrite tests. Earlier five global
test-evidence limitations remain separately open. [A-003](../../../audit/RECOVERY_STATUS_2026-09-17.md#application-findings)
is an archived synthetic reproduction: physical padded LIBELLE is preserved by
builder but rejected by public catalog-text validation after physical rebuild.
It was read, not rerun or repaired in R3. Intended raw-text preservation remains.

## Per-symbol explanations

Qualified owner is `tests.unit.test_enrich_planning_features` plus each heading;
nested substitutes retain their parent name. Signatures/defaults are exact
source excerpts; parametrize expressions are exact decorators and specify every
case value. Cases shown are static expansion counts, reconciled with the actual
183-pass run, not extra executions. Every test's expected exception/success and
the reached branch are explained; the complete source snapshot supplies the exact
assertions/regexes without replacing the behavioral explanation.

<a id="r3-rectangle"></a>

### `_rectangle`

function; source lines 67–68. Signature SHA256: `1dff32c347a43fe840648d6cf98a91ab41df8526786886c740fa307d9e6defa2`.

```python
def _rectangle(x1: float, y1: float, x2: float, y2: float) -> Polygon:
```

Returns a closed axis-aligned Shapely Polygon from four float bounds; used by square/overlap/tamper fixtures. Pure geometry construction, no CRS itself and no assertions.

<a id="r3-parcels"></a>

### `_parcels`

function; source lines 71–89. Signature SHA256: `36b31b7c909578f0bae5fe17d724c2129b08860f5f175a8c783a5d5597d313ec`.

```python
def _parcels(
    geometries: list[object] | None = None,
    *,
    ids: list[object] | None = None,
    crs: str | None = "EPSG:2154",
) -> gpd.GeoDataFrame:
```

Builds EPSG:2154 polygons with parcel_id and existing_zoning_fact (7 upward), index 50 upward. Defaults to one 10 x 10 square; optional CRS is assigned None or reprojected. Uses geometries or [...] and ids or [...], so passing an empty list selects defaults, not a true zero-parcel fixture. No disk IO or test assertion.

<a id="r3-source-frame"></a>

### `_source_frame`

function; source lines 92–125. Signature SHA256: `44add4ccf5ced4fc4d171039d76634a2372910e256b0e8da65c55171dd5a2a7c`.

```python
def _source_frame(
    logical: str,
    geometries: list[object],
    *,
    ids: list[object] | None = None,
    type_codes: list[object] | None = None,
    subtype_codes: list[object] | None = None,
    document_refs: list[object] | None = None,
    crs: str | None = "EPSG:2154",
) -> gpd.GeoDataFrame:
```

Constructs raw EPSG:2154 source geometry and prescription LIB_IDPSC/TYPEPSC/STYPEPSC or information LIB_IDINFO/TYPEINF/STYPEINF fields. IDs/codes/document refs use supplied lists or defaults; labels Label n, alternating nullable text/file names, all-null URL and raw date. IGNF:LAMB93 is assigned without coordinate change; other non-2154 CRS reproject; None removes CRS. No source authority until materialized.

<a id="r3-summary"></a>

### `_summary`

function; source lines 128–158. Signature SHA256: `a9b1c1cff59fed27a0a46c70021d19cda4ba3dbe68890397412d58e0e95953f2`.

```python
def _summary(
    frame: gpd.GeoDataFrame,
    source_layer: str,
    *,
    document_id: str = DOCUMENT_ID,
    archive_sha: str = ARCHIVE_SHA,
) -> GpuLayerSummary:
```

Computes the supplied frame's ordered columns/dtypes/nulls, sorted geometry counts, feature/null/empty/invalid counts and CRS; puts synthetic document/archive identity into GpuLayerSummary. In-memory asserted metadata, not a read or integrity proof. Called before/after materialization and in envelope-mutation helpers.

<a id="r3-inspected"></a>

### `_inspected`

function; source lines 161–173. Signature SHA256: `abd3a6f5d7b427587a4ed711b64eee931e50fa5e2bb137ab7b618fc9f70f35d0`.

```python
def _inspected(logical: str, frame: gpd.GeoDataFrame) -> GpuInspectedLayer:
```

Wraps frame and _summary in GpuInspectedLayer with SOURCE_<LOGICAL> and an initially nonexistent synthetic GPKG path. Retains the mutable frame reference. _planning_document later materializes it; this helper alone has no physical provenance.

<a id="r3-physical-inventory"></a>

### `_physical_inventory`

function; source lines 176–191. Signature SHA256: `91e04b54be2eda2bdf03a8b5dabd45af5e5fbfc86d1689fb81aba58f5c2b0f2d`.

```python
def _physical_inventory(root: Path) -> tuple[GpuExtractedFile, ...]:
```

Walks regular files beneath the selected fixture root in sorted order, excludes the root extraction manifest, records relative POSIX paths, suffix type, actual size and SHA256, category SPATIAL_DATA. Reads/hashes actual synthetic bytes, returns tuple; no official archive proof.

<a id="r3-write-extraction-manifest"></a>

### `_write_extraction_manifest`

function; source lines 194–214. Signature SHA256: `14cb19fe07220cead4d0407e66c5dd1433acaf8681eaa2280e531401aeaecfef`.

```python
def _write_extraction_manifest(
    root: Path,
    archive_sha256: str,
    files: tuple[GpuExtractedFile, ...],
) -> None:
```

Writes schema_version 2, synthetic archive SHA and each relative file path/size/hash as sorted compact JSON to EXTRACTION_MANIFEST_NAME. Real local write; no assertion, archive download or schema migration.

<a id="r3-materialize-layer"></a>

### `_materialize_layer`

function; source lines 217–241. Signature SHA256: `8bb8d5b16c2436d94b8f919ac93aaa1857ee4225c1b78cb1d037f8117a06c054`.

```python
def _materialize_layer(root: Path, layer: GpuInspectedLayer) -> GpuInspectedLayer:
```

Uses an existing physical dataset's resolved path if present; otherwise writes raw frame to a GPKG under root. Always rereads it with GeoPandas/Pyogrio, then dataclasses.replace supplies updated reference/data/summary. Fixture setup performs real IO before the application revalidates again.

<a id="r3-planning-document"></a>

### `_planning_document`

function; source lines 244–347. Signature SHA256: `a8bca6acee99e4b2d4055878cc12aef68795aae1fc746e7f727046a6c0071dad`.

```python
def _planning_document(
    layers: list[GpuInspectedLayer] | None = None,
) -> GpuPlanningDocument:
```

Materializes related layers, writes and rereads a real zoning GPKG, inventories files and writes the schema-2 marker. Root is first existing source parent or tempfile.mkdtemp (not necessarily pytest basetemp; no cleanup fixture here). Loads checked-in GPU YAML then changes match_tokens locally to these synthetic roles, validates/hashes config and discovers physical inventory. Returns GpuPlanningDocument with fabricated metadata/archive SHA and a ZIP path that is not downloaded or opened. Tests prove local physical contracts, not official acquisition.

<a id="r3-run"></a>

### `_run`

function; source lines 350–357. Signature SHA256: `d63624fd06a1bad42a069d956fe2b5e011f302f82557418d9e2ca010c991fe24`.

```python
def _run(
    layers: list[GpuInspectedLayer],
    parcels: gpd.GeoDataFrame | None = None,
) -> ParcelPlanningFeaturesResult:
```

Uses supplied parcels or _parcels, calls _planning_document and the real public intersection builder. Returns ParcelPlanningFeaturesResult. Implicit filesystem work is delegated to fixture setup and GPU revalidation; no network adapter invoked.

<a id="r3-test-only-high-level-api-is-exported"></a>

### `test_only_high_level_api_is_exported`

function; source lines 360–369. Signature SHA256: `2eeb1bf3a44d38ff25d516f08b9258ac18cab0da572d613ec204b8b7207281f1`.

```python
def test_only_high_level_api_is_exported() -> None:
```

No fixture IO. Six assertions check builder, PlanningFeaturesError and ParcelPlanningFeaturesResult object identity through stages and membership in stages.__all__. Despite its name, does not assert that only these three symbols exist; a separate test covers the other two exports.

Collected-case expansion: 1. AST assert statements: 6; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-result-is-frozen"></a>

### `test_result_is_frozen`

function; source lines 372–375. Signature SHA256: `ac29cde29c5dfed7afe3c77d6b72c6f7e94c23402f4e56dd9265855f4124541d`.

```python
def test_result_is_frozen() -> None:
```

Builds an empty-related-layer result with one parcel, attempts result.parcels assignment and requires FrozenInstanceError. Does not attempt mutation inside any contained DataFrame or assert deep immutability.

Collected-case expansion: 1. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-surface-full-overlap-normalizes-raw-values-and-lineage"></a>

### `test_surface_full_overlap_normalizes_raw_values_and_lineage`

function; source lines 378–427. Signature SHA256: `602976d72f437290f72a9aa5a5a6139ff8038e487e3d67169a3f62b1220af5a6`.

```python
def test_surface_full_overlap_normalizes_raw_values_and_lineage() -> None:
```

Real synthetic prescription GPKG, one 100 m2 surface matching a 100 m2 parcel, source CRS alias IGNF:LAMB93. Asserts deterministic/CNIG IDs, family/kind, exact DYNAMIC-18 and 04 codes, label/text, document/SHA/layer/canonical source CRS, full area, output EPSG:2154, AREA_OVERLAP and 100 m2/100% shares, null line metric and parcel/family counts/union. Does not decode the dynamic code or test padded text.

Collected-case expansion: 1. AST assert statements: 29; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-surface-partial-and-touch-relations"></a>

### `test_surface_partial_and_touch_relations`

function; source lines 430–442. Signature SHA256: `422f5a9f94856c4815fb40e70cb161f3237ea55b03f9a8da233bf16c01b46426`.

```python
def test_surface_partial_and_touch_relations() -> None:
```

Two physical prescription polygons: half-parcel overlap and boundary-only contact. Asserts PART AREA_OVERLAP 50 m2, TOUCH TOUCH_ONLY 0 m2 and one touch summary. Real join/intersection, not a mocked candidate table.

Collected-case expansion: 1. AST assert statements: 5; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-overlapping-surface-union-is-not-double-counted"></a>

### `test_overlapping_surface_union_is_not_double_counted`

function; source lines 445–469. Signature SHA256: `8bf32b6e24295eb1713025efbde6204bb0fd3db2b5e4040fbb8be37f8fb41c4a`.

```python
def test_overlapping_surface_union_is_not_double_counted() -> None:
```

Physical prescription/information surfaces overlap on the 100 m2 parcel. Asserts raw clipped area sum 150 m2 but all-family union 100 m2/100%, prescription union 100 and information union 50. Proves overlap distinction, not numerical-tolerance edge handling.

Collected-case expansion: 1. AST assert statements: 5; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-polygon-and-multipolygon-surfaces"></a>

### `test_polygon_and_multipolygon_surfaces`

function; source lines 479–488. Signature SHA256: `e7e3011c8a3f69871d409425e0739d396423fbaed95e19530112b8acecf3e29c`.

```python
def test_polygon_and_multipolygon_surfaces(geometry: object) -> None:
```

Two parametrized geometries, square Polygon or separated two-part MultiPolygon; each becomes a physical information_surface (INFORMATION / SURFACE). Asserts one relation and positive intersection area only, not an exact area for the multipolygon.

Collected-case expansion: 2. AST assert statements: 2; exception contexts/equality helpers and no-exception success are also assertions, as described above.

Exact case decorators:

```python
@pytest.mark.parametrize(
    "geometry",
    [
        _rectangle(0, 0, 10, 10),
        MultiPolygon([_rectangle(0, 0, 4, 10), _rectangle(6, 0, 10, 10)]),
    ],
)
```

<a id="r3-test-line-crossing-and-partly-inside"></a>

### `test_line_crossing_and_partly_inside`

function; source lines 491–507. Signature SHA256: `76d38c21d907a1795012a6ded3916dda4caba4797e2db5056f5ae0caf1349d5d`.

```python
def test_line_crossing_and_partly_inside() -> None:
```

Two physical prescription lines cross or partly enter the parcel. Asserts crossing LENGTH_OVERLAP, clipped 10 m versus full source 20 m, partial 5 m, two line relations and sum 15 m. Confirms full and clipped metrics are distinct.

Collected-case expansion: 1. AST assert statements: 6; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-line-boundary-touch-is-zero-length"></a>

### `test_line_boundary_touch_is_zero_length`

function; source lines 510–519. Signature SHA256: `dc26d9dab1079b748d819c1c5463201add54915858f244afbe9862f99a4a7430`.

```python
def test_line_boundary_touch_is_zero_length() -> None:
```

Physical prescription_line from (10, 5) to (15, 5), starting at the boundary of the (0, 0)-(10, 10) parcel and extending outside. Requires TOUCH_ONLY, intersection length 0 and one line-touch summary. No road/access meaning is implied.

Collected-case expansion: 1. AST assert statements: 3; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-linestring-and-multilinestring"></a>

### `test_linestring_and_multilinestring`

function; source lines 529–537. Signature SHA256: `00907ba7ef305a2b6707a2010dff11ebef013f69cf39bb16fc3c6298d5de6de9`.

```python
def test_linestring_and_multilinestring(geometry: object) -> None:
```

Two parametrized physical prescription sources, one LineString or two-part MultiLineString; only asserts positive clipped length. Does not assert exact part count, exact length or all relation schema fields.

Collected-case expansion: 2. AST assert statements: 1; exception contexts/equality helpers and no-exception success are also assertions, as described above.

Exact case decorators:

```python
@pytest.mark.parametrize(
    "geometry",
    [
        LineString([(-1, 5), (11, 5)]),
        MultiLineString([[(-1, 2), (11, 2)], [(-1, 8), (11, 8)]]),
    ],
)
```

<a id="r3-test-points-inside-boundary-outside-and-multipoint"></a>

### `test_points_inside_boundary_outside_and_multipoint`

function; source lines 540–564. Signature SHA256: `1bfc14cca0f5c1e505f1f125ed2d0e531fc3d4d1a90e5bf77d536aa9311d6455`.

```python
def test_points_inside_boundary_outside_and_multipoint() -> None:
```

Physical prescription_point features IN, BOUNDARY, OUT and a three-member MULTI with one inside, one boundary, one outside. Asserts only IN/BOUNDARY/MULTI relate; types for IN and BOUNDARY; full MULTI count 3, inside/boundary 1 each; three relation rows but parcel inside/boundary member totals 2 each.

Collected-case expansion: 1. AST assert statements: 9; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-missing-optional-layer-families-return-stable-empty-catalogs"></a>

### `test_missing_optional_layer_families_return_stable_empty_catalogs`

function; source lines 567–575. Signature SHA256: `fc12f9500af2298d3cd9b89e0b7e8438d6d17beeeb7ac47557212cb0bad6085b`.

```python
def test_missing_optional_layer_families_return_stable_empty_catalogs() -> None:
```

Builds real zoning-only document. Asserts three catalogs and relations empty, surface CRS EPSG:2154, relation point_member_count nullable Int64 and zero surface relation count. Does not prove every empty dtype or public zero-parcel behavior.

Collected-case expansion: 1. AST assert statements: 7; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-optional-raw-source-fields-are-not-fabricated"></a>

### `test_optional_raw_source_fields_are_not_fabricated`

function; source lines 578–591. Signature SHA256: `f9e79e6f29914eb12788a1b78e2f6f39ce1e01e6978b62bfd081d915bd18aa41`.

```python
def test_optional_raw_source_fields_are_not_fabricated() -> None:
```

Drops LIBELLE/TXT/NOMFIC/URLFIC/DATVALID from a physical prescription line fixture before build. Iterates five output fields requiring missing values. No whitespace or invalid-type optional-text test; A-003 is not covered.

Collected-case expansion: 1. AST assert statements: 1; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-epsg4326-parcels-are-measured-in-lambert93-but-preserved"></a>

### `test_epsg4326_parcels_are_measured_in_lambert93_but_preserved`

function; source lines 594–608. Signature SHA256: `a0e926f6ba8b0f41e9041060fce8ba277d69c38c3445d9c70c833f7f666bbd3d`.

```python
def test_epsg4326_parcels_are_measured_in_lambert93_but_preserved() -> None:
```

_parcels starts with a synthetic (0, 0)-(10, 10) square assigned EPSG:2154, then reprojects it to EPSG:4326. Intersects a matching physical prescription surface. Asserts output CRS and exact parcel WKB match the geographic input and relation area approximately 100 m2. Real projection/overlay of synthetic coordinates, not geographically representative or official-source evidence.

Collected-case expansion: 1. AST assert statements: 3; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-invalid-parcel-ids-are-rejected"></a>

### `test_invalid_parcel_ids_are_rejected`

function; source lines 612–614. Signature SHA256: `7eb8879e2041e4a5a2b6b962a90d09f2e78afd6b24eb9db317e637dab373b9bf`.

```python
def test_invalid_parcel_ids_are_rejected(bad_id: object) -> None:
```

Six inputs None, empty, whitespace, leading/trailing spaces and integer 7. _run still materializes source fixture before invoking builder; builder's parcel-id gate requires PlanningFeaturesError matching parcel_id. No coercion permitted.

Collected-case expansion: 6. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

Exact case decorators:

```python
@pytest.mark.parametrize("bad_id", [None, "", "   ", " X", "X ", 7])
```

<a id="r3-test-duplicate-parcel-ids-are-rejected"></a>

### `test_duplicate_parcel_ids_are_rejected`

function; source lines 617–622. Signature SHA256: `8fa73512481068bbd64e84eacdd55f9ec226aeec31736a4060f58ced748c8e42`.

```python
def test_duplicate_parcel_ids_are_rejected() -> None:
```

Two valid different-sized squares, (0, 0)-(2, 2) and (3, 3)-(4, 4), have IDs ["P", "P"]; expects PlanningFeaturesError matching unique at initial parcel check. Does not require GPU physical revalidation to be reached.

Collected-case expansion: 1. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-duplicate-source-ids-are-rejected"></a>

### `test_duplicate_source_ids_are_rejected`

function; source lines 625–632. Signature SHA256: `53e5e3642eada3bf7046ad2849f70880b093fb942f8a648e8a690340043ceba7`.

```python
def test_duplicate_source_ids_are_rejected() -> None:
```

Two physical information_surface features have IDs ["SAME", "SAME"]. Parcel checks pass, real physical batch read succeeds, then source-ID uniqueness rejects with PlanningFeaturesError matching unique. This is per-role uniqueness, not a cross-layer uniqueness attack.

Collected-case expansion: 1. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-prescription-surface-uses-validated-source-ogr-fid-when-cnig-id-absent"></a>

### `test_prescription_surface_uses_validated_source_ogr_fid_when_cnig_id_absent`

function; source lines 635–666. Signature SHA256: `2b3a86fd17f33faea43a312635090e97135310b2fb64d835781a1003231969d4`.

```python
def test_prescription_surface_uses_validated_source_ogr_fid_when_cnig_id_absent(
    tmp_path: Path,
) -> None:
```

Writes/rereads a real Shapefile lacking LIB_IDPSC in tmp_path, assembles local document and builds. Asserts source OGR_FID:0, ARCHIVE_SCOPED_OGR_FID, OGR_FID field and full deterministic planning ID. Synthetic archive lineage; no official ZIP.

Collected-case expansion: 1. AST assert statements: 4; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-geopackage-prescription-surface-uses-sealed-ogr-fid-fallback"></a>

### `test_geopackage_prescription_surface_uses_sealed_ogr_fid_fallback`

function; source lines 669–680. Signature SHA256: `3ef78806985052420d82712b5ecafc9f7476fae29ab41d4dc93205a060c44f3a`.

```python
def test_geopackage_prescription_surface_uses_sealed_ogr_fid_fallback() -> None:
```

Drops LIB_IDPSC before physical GPKG materialization. Asserts OGR_FID:1 and its three provenance/ID fields. Demonstrates driver-specific physical FID instead of assuming pandas row 0.

Collected-case expansion: 1. AST assert statements: 4; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-idurba-mismatch-is-rejected"></a>

### `test_idurba_mismatch_is_rejected`

function; source lines 683–688. Signature SHA256: `e6520c23e9cd7cec52c9f04a1f94a3312f6fe8d4a01807cbaade769adcab0fe3`.

```python
def test_idurba_mismatch_is_rejected() -> None:
```

Physical source raw IDURBA is OTHER instead of archive basename. Requires PlanningFeaturesError matching IDURBA after physical source validation; no rewriting to the configured value.

Collected-case expansion: 1. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-missing-required-source-fields-fail"></a>

### `test_missing_required_source_fields_fail`

function; source lines 692–697. Signature SHA256: `1a8e25f73527f5d1b158d087f58e9cc5d8b938ecf0a8a97fa41a3df87451eaca`.

```python
def test_missing_required_source_fields_fail(missing: str) -> None:
```

Four prescription-line cases omit TYPEPSC, STYPEPSC, IDURBA or LIB_IDPSC. Requires PlanningFeaturesError mentioning omitted field. Unlike prescription_surface, a line does not permit missing-CNIG-ID FID fallback.

Collected-case expansion: 4. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

Exact case decorators:

```python
@pytest.mark.parametrize("missing", ["TYPEPSC", "STYPEPSC", "IDURBA", "LIB_IDPSC"])
```

<a id="r3-test-wrong-geometry-kind-is-rejected"></a>

### `test_wrong_geometry_kind_is_rejected`

function; source lines 708–710. Signature SHA256: `89193ebe2834d122a84ded5831748ba9bece6ff495e86dfc346b4e3b1998eafb`.

```python
def test_wrong_geometry_kind_is_rejected(logical: str, geometry: object) -> None:
```

Three physical wrong-family cases: surface with line, line with point, point with line. Requires PlanningFeaturesError matching geometry after local materialization. No repair or geometry-type reinterpretation.

Collected-case expansion: 3. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

Exact case decorators:

```python
@pytest.mark.parametrize(
    ("logical", "geometry"),
    [
        ("prescription_surface", LineString([(0, 0), (1, 1)])),
        ("prescription_line", Point(1, 1)),
        ("prescription_point", LineString([(0, 0), (1, 1)])),
    ],
)
```

<a id="r3-test-invalid-surface-geometry-is-rejected-without-repair"></a>

### `test_invalid_surface_geometry_is_rejected_without_repair`

function; source lines 713–723. Signature SHA256: `5258e5fd334795f442438aebe82eb4b40010b381f8a07d8c7d911a8d493361c1`.

```python
def test_invalid_surface_geometry_is_rejected_without_repair() -> None:
```

Physical bow-tie polygon; expects PlanningFeaturesError matching valid. No repaired geometry or success output is asserted.

Collected-case expansion: 1. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-null-or-empty-source-geometry-is-rejected"></a>

### `test_null_or_empty_source_geometry_is_rejected`

function; source lines 727–732. Signature SHA256: `e6115f89932bd36df265edc454134188083b08b8130ffd256b70fb06a4e4e84e`.

```python
def test_null_or_empty_source_geometry_is_rejected(geometry: object) -> None:
```

Two physical surface fixtures replace valid geometry with None or Polygon(). Requires PlanningFeaturesError matching geometry. Empty case emits the recorded GeoSeries.notna UserWarning during GPU summary evaluation, not a skipped case.

Collected-case expansion: 2. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

Exact case decorators:

```python
@pytest.mark.parametrize("geometry", [None, Polygon()])
```

<a id="r3-test-missing-crs-is-rejected"></a>

### `test_missing_crs_is_rejected`

function; source lines 736–744. Signature SHA256: `378e4fcaf4b6fe42f68e8ec0421306bb7a3e3c11c7ce9b45754886f57ac149af`.

```python
def test_missing_crs_is_rejected(target: str) -> None:
```

Two cases remove parcel or source CRS. Requires PlanningFeaturesError matching CRS or physical revalidation. Parcel case reaches initial parcel gate; source case can fail during delegated physical checks and emits the recorded Pyogrio write warning. Does not prove one shared rejection site.

Collected-case expansion: 2. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

Exact case decorators:

```python
@pytest.mark.parametrize("target", ["parcel", "source"])
```

<a id="r3-test-unusable-source-crs-is-rejected"></a>

### `test_unusable_source_crs_is_rejected`

function; source lines 747–752. Signature SHA256: `c1ef100378a858ebc42cfe4fee231e95b41bea713c4b43b6fc4e0cbdb4e8993c`.

```python
def test_unusable_source_crs_is_rejected() -> None:
```

Assigns a local engineering CRS without changing line coordinates, then physically builds; expects PlanningFeaturesError matching CRS when metric transformation cannot be formed. This is not an EPSG correctness audit.

Collected-case expansion: 1. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-mutated-source-summary-is-rejected"></a>

### `test_mutated_source_summary_is_rejected`

function; source lines 765–775. Signature SHA256: `129fd92496253dd33f7c883e2111128196c1e9b928fad98a517cddf55feddd0e`.

```python
def test_mutated_source_summary_is_rejected(field: str, value: object) -> None:
```

Five envelope-only changes after actual files are created: document ID, archive SHA, source layer, count 99, geometry-type counts. Builder rejects through GPU physical summary comparison before the stage's own _validate_layer_summary need run. Regex allows summary or physical revalidation.

Collected-case expansion: 5. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

Exact case decorators:

```python
@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("source_document_id", "other"),
        ("source_archive_sha256", "b" * 64),
        ("source_layer", "other"),
        ("feature_count", 99),
        ("geometry_types", (("Point", 1),)),
    ],
)
```

<a id="r3-test-source-summary-counts-are-strict-integers"></a>

### `test_source_summary_counts_are_strict_integers`

function; source lines 779–794. Signature SHA256: `73cc5afd920c6bb844eb60b9458418c09376ae3c7a0d52376c335034ff16591b`.

```python
def test_source_summary_counts_are_strict_integers(bad_count: object) -> None:
```

Five envelope counts True, -1, 1.5, infinity and string 1. Four unequal-to-1 values fail GPU fresh-summary dataclass comparison; True compares equal to integer 1 there, survives physical revalidation and is rejected by stage _validate_layer_summary/_strict_nonnegative_integer. Broad regex allows both sites. Thus only the bool case here isolates the stage's strict-count branch.

Collected-case expansion: 5. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

Exact case decorators:

```python
@pytest.mark.parametrize("bad_count", [True, -1, 1.5, float("inf"), "1"])
```

<a id="r3-test-reserved-output-column-collision-is-rejected"></a>

### `test_reserved_output_column_collision_is_rejected`

function; source lines 797–801. Signature SHA256: `db2c189cbbcb78fd4e83c495c49a53eb3933124be4b35e960dc4348df21c30f9`.

```python
def test_reserved_output_column_collision_is_rejected() -> None:
```

Adds planning_surface_relation_count=99 to input parcels. Builder requires PlanningFeaturesError matching output columns before normalizing related source. Prevents overwriting preexisting output-named facts.

Collected-case expansion: 1. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-inputs-and-all-existing-parcel-fields-are-preserved"></a>

### `test_inputs_and_all_existing_parcel_fields_are_preserved`

function; source lines 804–820. Signature SHA256: `d5ebe6473d84541673e656202cb1e5f0a5c197137a9425b39e1abca6050af905`.

```python
def test_inputs_and_all_existing_parcel_fields_are_preserved() -> None:
```

Saves original parcels and actual document-held source frame; builds physical features, compares both originals with GeoPandas equality helpers, then output IDs/order/index/existing_zoning_fact/WKB. Proves these fixture fields survive, not recursive freezing of arbitrary object cells.

Collected-case expansion: 1. AST assert statements: 4; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-relations-are-unique-deterministic-and-summaries-agree"></a>

### `test_relations_are_unique_deterministic_and_summaries_agree`

function; source lines 823–851. Signature SHA256: `7c5a3dc80364ffe1e00e54c6c1c0b7a60f4a4e966f818f749ce929a5e49d2d04`.

```python
def test_relations_are_unique_deterministic_and_summaries_agree() -> None:
```

Two parcels in input order P-B then P-A, synthetic surface/line sources. Asserts no duplicate parcel/feature key, relation parcel order P-B/P-B/P-A and P-B surface count/line sum agreement. A single execution, not repeated-run or all tie-order equivalence proof.

Collected-case expansion: 1. AST assert statements: 4; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-result-frames-are-independent-from-mutable-inputs"></a>

### `test_result_frames_are_independent_from_mutable_inputs`

function; source lines 854–864. Signature SHA256: `69ba740dc1f206f33b473efb80650476addbc3a4864efa9417e27f6d26919164`.

```python
def test_result_frames_are_independent_from_mutable_inputs() -> None:
```

Saves result.relations, mutates original parcel fact and the pre-materialization input layer label, then pandas assert_frame_equal on relations. Does not mutate the fresh document-held source frame or inspect independence of all five outputs.

Collected-case expansion: 1. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-present-empty-optional-layer-is-valid"></a>

### `test_present_empty_optional_layer_is_valid`

function; source lines 875–905. Signature SHA256: `a2190b21281014ed64ce71e1574de862574a911857f5366d595ced54f1c370c8`.

```python
def test_present_empty_optional_layer_is_valid(
    logical: str,
    catalog_name: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

Three real empty prescription source kinds. All cases assert empty corresponding catalog/relations, EPSG:2154 catalog CRS, one retained parcel and document lineage. Only prescription_surface drops LIB_IDPSC, installs the delegating Pyogrio reader spy and asserts fid_reads == 1. That empty surface still undergoes a physical FID read; line and point variants have no measured reader-call-count assertion.

Collected-case expansion: 3. AST assert statements: 6; exception contexts/equality helpers and no-exception success are also assertions, as described above.

Exact case decorators:

```python
@pytest.mark.parametrize(
    ("logical", "catalog_name"),
    [
        ("prescription_surface", "surface_features"),
        ("prescription_line", "line_features"),
        ("prescription_point", "point_features"),
    ],
)
```

<a id="r3-test-present-empty-optional-layer-is-valid-unexpected-fid-read"></a>

### `test_present_empty_optional_layer_is_valid.unexpected_fid_read`

function; source lines 886–890. Signature SHA256: `3a03b77e6af2477f8eb47a965a89cc47919c830b716be085e1a8debc3a15c593`.

```python
        def unexpected_fid_read(*args: object, **kwargs: object) -> object:
```

Defined and installed only in the prescription_surface branch. The monkeypatched reader delegates every call to the real Pyogrio read_dataframe; increments nonlocal fid_reads only for fid_as_index. It does not raise or forbid reads despite its name, and it does not fabricate data.

<a id="r3-contract-result"></a>

### `_contract_result`

function; source lines 908–941. Signature SHA256: `6a3ad5788df6e3a8b7e8b11f725a4f77c07f9be0780e96f2d0e2a546668368ff`.

```python
def _contract_result() -> tuple[
    GpuPlanningDocument,
    gpd.GeoDataFrame,
    ParcelPlanningFeaturesResult,
]:
```

Builds one 100 m2 parcel with physical prescription surface, line and point using default raw codes; returns document, original parcels and actual builder result. Shared synthetic source fixture for private _validate_result and intrinsic attacks, not a fully mocked relation factory.

<a id="r3-source-complete-contract"></a>

### `_source_complete_contract`

function; source lines 944–984. Signature SHA256: `f4363f80dfd033ebd01917d70168b5789fc98a92f14dd3ed887a0e6ecca17aca`.

```python
def _source_complete_contract() -> tuple[
    GpuPlanningDocument,
    gpd.GeoDataFrame,
    ParcelPlanningFeaturesResult,
]:
```

Same three physical geometry kinds but explicit raw code pairs 07/04, 15/00 and 07/00. Returns real builder output with its source document/parcels; downstream validations reread those files. These codes are fixtures, not policy interpretation.

<a id="r3-two-parcel-source-complete-contract"></a>

### `_two_parcel_source_complete_contract`

function; source lines 987–1022. Signature SHA256: `bb23ebd28b2b346d3a8ccc871d679cd2a42148f54df830fe467645aeb5f4ec58`.

```python
def _two_parcel_source_complete_contract() -> tuple[
    GpuPlanningDocument,
    gpd.GeoDataFrame,
    ParcelPlanningFeaturesResult,
]:
```

Creates two equal 100 m2 parcels P-1/P-2, surface and line affecting P-1 only. Real physical build. Equal areas prevent an incorrectly associated relation from being detected merely through area inequality; used for reconstruction attacks.

<a id="r3-validate-source-complete"></a>

### `_validate_source_complete`

function; source lines 1025–1037. Signature SHA256: `3f3d6c1634a435656765e036dda4aaec1d540ffc40d963d98edfc37b68ce7578`.

```python
def _validate_source_complete(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    result: ParcelPlanningFeaturesResult,
) -> PlanningFeatureInputValidation:
```

Calls the public six-argument normalized-input validator with document, chosen parcels and four frames from result; returns PlanningFeatureInputValidation. Does not pass result.parcels unless caller explicitly supplies it as parcels.

<a id="r3-replace-related-layer"></a>

### `_replace_related_layer`

function; source lines 1040–1057. Signature SHA256: `447f71f0e4a721b0b6498e265db3bfef2ec23701b048a03c4e5aebcf01e604b1`.

```python
def _replace_related_layer(
    planning_document: GpuPlanningDocument,
    logical_name: str,
    frame: gpd.GeoDataFrame,
) -> GpuPlanningDocument:
```

Creates a new document envelope replacing one loaded source DataFrame and recomputed in-memory summary; leaves physical files, manifest and inventory unchanged. Deliberate discrepancy helper, not source-authorized normalization.

<a id="r3-without-related-layer"></a>

### `_without_related_layer`

function; source lines 1060–1071. Signature SHA256: `e6133c005bcd788e68e8715b5bf1ff185a5129603c772102740db76c6f1c72c0`.

```python
def _without_related_layer(
    planning_document: GpuPlanningDocument,
    logical_name: str,
) -> GpuPlanningDocument:
```

Returns document with one logical role removed from related_layers only. Configured match tokens, physical file and all_spatial_layers remain, so subsequent role-discovery consistency can reject before supplied catalog comparison.

<a id="r3-refresh-extraction-inventory"></a>

### `_refresh_extraction_inventory`

function; source lines 1074–1091. Signature SHA256: `93ce06e88b29dafe77e12e7c5e54c14cbe0ab0b07fc245b910d4021e600dafe6`.

```python
def _refresh_extraction_inventory(
    planning_document: GpuPlanningDocument,
) -> GpuPlanningDocument:
```

Rehashes current synthetic files, rewrites manifest and replaces extraction/all_spatial_layers through real discovery. Leaves loaded source data/summary stale, allowing tests to distinguish file-inventory coherence from loaded-versus-reread equality.

<a id="r3-replace-layer-reference"></a>

### `_replace_layer_reference`

function; source lines 1094–1118. Signature SHA256: `b0396e9adc6d0f3b71cae876dabb6c91535d808cb9a640e4012c1d4911d83f46`.

```python
def _replace_layer_reference(
    planning_document: GpuPlanningDocument,
    logical_name: str,
    reference: GpuSpatialLayerReference,
) -> GpuPlanningDocument:
```

Replaces the selected related reference and matching all_spatial_layers entry, not physical extraction data/config. Used to point at a copied outside file; configured discovery still sees original inside dataset.

<a id="r3-test-public-normalized-input-contract-validates-step-7d-3-1-result"></a>

### `test_public_normalized_input_contract_validates_step_7d_3_1_result`

function; source lines 1121–1140. Signature SHA256: `0a76f117177f4efb2bf37fc54cba007407d57a28d0737ee67f08e7a6b59b574b`.

```python
def test_public_normalized_input_contract_validates_step_7d_3_1_result() -> None:
```

Runs real public revalidation on three physical GPKGs. Asserts record type, three layers/files, rebuilt relation count equals result length, each hash length 64 and parseable hexadecimal via int(value,16). No pinned expected digest assertion.

Collected-case expansion: 1. AST assert statements: 5; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-public-normalized-input-contract-wraps-malformed-document-context"></a>

### `test_public_normalized_input_contract_wraps_malformed_document_context`

function; source lines 1143–1148. Signature SHA256: `b028ca07ee101528b1684cba4599882ae41efeb46d6df0e51432c00135321cd5`.

```python
def test_public_normalized_input_contract_wraps_malformed_document_context() -> None:
```

Replaces related_layers with (None,), invokes public validator and requires PlanningFeaturesError with AttributeError or TypeError cause. The malformed reference fails before normal physical-batch completion; proves catch-all wrapper, not official metadata validation.

Collected-case expansion: 1. AST assert statements: 1; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-source-complete-contract-binds-inspected-spatial-inventory"></a>

### `test_source_complete_contract_binds_inspected_spatial_inventory`

function; source lines 1151–1155. Signature SHA256: `634a4f3b71e011300bdaf8d50ebc8b5bd53d42611319b1bb746da928b9168d58`.

```python
def test_source_complete_contract_binds_inspected_spatial_inventory() -> None:
```

Removes all_spatial_layers entries while retaining inspected layers. Requires PlanningFeaturesError matching inventory/reference from exact-reference membership gate before physical revalidation.

Collected-case expansion: 1. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-public-normalized-input-contract-is-exported"></a>

### `test_public_normalized_input_contract_is_exported`

function; source lines 1158–1167. Signature SHA256: `3440b826ddb26985dc36de4baae289ccf215984d2f5e1e52f0f6f17e5b1a74b0`.

```python
def test_public_normalized_input_contract_is_exported() -> None:
```

No physical fixture. Four assertions bind public validator and PlanningFeatureInputValidation to stages reexports and __all__; complements, rather than replaces, the three-export test.

Collected-case expansion: 1. AST assert statements: 4; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-public-source-validation-hashes-survive-parquet-readback"></a>

### `test_public_source_validation_hashes_survive_parquet_readback`

function; source lines 1170–1193. Signature SHA256: `3577d78bec634d8c300467fee6bde81d330afa77e60e5e6fc18e568de8092796`.

```python
def test_public_source_validation_hashes_survive_parquet_readback(
    tmp_path: Path,
) -> None:
```

Validates physical fixture, writes/rereads three GeoParquet catalogs and one plain Parquet relation table in tmp_path, validates again, asserts entire scalar validation records equal. Real local serialization/readback, no artifact-manifest or official-source acquisition test.

Collected-case expansion: 1. AST assert statements: 1; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-public-normalized-input-contract-rejects-stripped-catalog"></a>

### `test_public_normalized_input_contract_rejects_stripped_catalog`

function; source lines 1196–1207. Signature SHA256: `24be94fca0f72d20f3161ddd20de4c13c8a26797662acc812336338be392648d`.

```python
def test_public_normalized_input_contract_rejects_stripped_catalog() -> None:
```

Drops label_raw from supplied surface catalog, retains real physical source, calls public validator expecting schema/label_raw error. Physical normalization occurs first, then canonical column-schema gate rejects; no raw-value comparison reached.

Collected-case expansion: 1. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-empty-and-nonempty-catalogs-have-identical-kind-schemas"></a>

### `test_empty_and_nonempty_catalogs_have_identical_kind_schemas`

function; source lines 1210–1222. Signature SHA256: `e1425cf41dd5a09d5f451a2a8a6b7cde3b59a9e476d7caf9d291db1cb7a9f4a9`.

```python
def test_empty_and_nonempty_catalogs_have_identical_kind_schemas() -> None:
```

Builds zoning-only and three-kind populated physical fixtures, compares list(columns) for each kind only. Does not assert dtype, index or full schema equality; optional all-null dtype variants remain meaningful.

Collected-case expansion: 1. AST assert statements: 1; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-strict-relation-integer-counts-are-enforced"></a>

### `test_strict_relation_integer_counts_are_enforced`

function; source lines 1226–1239. Signature SHA256: `51470fe1fddcc8e8d494de085792fc9d7b2218cfc51235037235afadf1200f55`.

```python
def test_strict_relation_integer_counts_are_enforced(bad_count: object) -> None:
```

Five bad point_member_count values -1, 1.5, infinity, string 2, True, after casting column to object. _validate_result defaults to source-complete public validation; canonical Int64 dtype rejection precedes scalar integer semantics. Regex explicitly accepts dtype/schema. R3-T01 limitation.

Collected-case expansion: 5. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

Exact case decorators:

```python
@pytest.mark.parametrize("bad_count", [-1, 1.5, float("inf"), "2", True])
```

<a id="r3-test-strict-parcel-summary-integer-counts-are-enforced"></a>

### `test_strict_parcel_summary_integer_counts_are_enforced`

function; source lines 1243–1257. Signature SHA256: `160005fc9c9a93e3fb70d0a9c43fb3f9afac498d64295e2ae51977aa3573bc1d`.

```python
def test_strict_parcel_summary_integer_counts_are_enforced(
    bad_count: object,
) -> None:
```

Same five bad values in object-typed parcel planning_line_relation_count. _validate_result revalidates source parcels and unaffected catalogs/relations, then its local summary check reaches _strict_nonnegative_integer. Requires integer-count/non-negative error; unlike relation attack, corrupted output summary dtype is not passed through the public complete-output comparison here.

Collected-case expansion: 5. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

Exact case decorators:

```python
@pytest.mark.parametrize("bad_count", [-1, 1.5, float("inf"), "2", True])
```

<a id="r3-test-corrupted-relation-semantics-are-rejected"></a>

### `test_corrupted_relation_semantics_are_rejected`

function; source lines 1272–1287. Signature SHA256: `847abd715cac58cf579991218fb8a39747c1073f8e5c323c01c8e3a61a918c2e`.

```python
def test_corrupted_relation_semantics_are_rejected(
    kind: str,
    column: str,
    value: object,
) -> None:
```

Seven mutations (surface type/share/null area/irrelevant line metric, line type/oversize clipped length, point boundary type), each after casting affected column to object. Public canonical dtype gate rejects all before intended semantic rule; only PlanningFeaturesError required. Separate 13-case intrinsic test actually exercises semantics. R3-T01.

Collected-case expansion: 7. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

Exact case decorators:

```python
@pytest.mark.parametrize(
    ("kind", "column", "value"),
    [
        ("SURFACE", "relation_type", "TOUCH_ONLY"),
        ("SURFACE", "parcel_share_pct", 42.0),
        ("SURFACE", "intersection_area_m2", None),
        ("SURFACE", "source_line_length_m", 0.0),
        ("LINE", "relation_type", "TOUCH_ONLY"),
        ("LINE", "intersection_length_m", 999.0),
        ("POINT", "relation_type", "BOUNDARY_TOUCH"),
    ],
)
```

<a id="r3-test-point-member-relation-semantics-are-exact"></a>

### `test_point_member_relation_semantics_are_exact`

function; source lines 1290–1301. Signature SHA256: `23aae65d750ab6e7f84da0a1fb4bced77c7e796667108ac7a796cc28b927851d`.

```python
def test_point_member_relation_semantics_are_exact() -> None:
```

Changes point inside count to 0 and boundary to 1 while relation_type remains INSIDE; preserves canonical count dtype. _validate_result/public path reaches intrinsic kind/count/type coherence and requires relation type error.

Collected-case expansion: 1. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-shared-intrinsic-relation-semantics-reject-every-invalid-case"></a>

### `test_shared_intrinsic_relation_semantics_reject_every_invalid_case`

function; source lines 1322–1362. Signature SHA256: `73d7642a471072d4ea8d7e7e71b0ed24733ed8596ac0e365231914a255721ab5`.

```python
def test_shared_intrinsic_relation_semantics_reject_every_invalid_case(
    case: str,
) -> None:
```

Direct common validator call after constructing valid physical fixture, with 13 named mutations: incompatible surface/line/point types; zero overlap metrics; positive touch metrics; INSIDE with zero inside; boundary with inside; area above feature; inconsistent share; nonfinite share; negative area. Requires TypeError or ValueError without source reread in attacked call. The area-exceeds-feature value also exceeds equal parcel area and is caught by that earlier bound. Not exhaustive over all invalid inputs.

Collected-case expansion: 13. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

Exact case decorators:

```python
@pytest.mark.parametrize(
    "case",
    [
        "surface-inside",
        "line-area",
        "point-touch",
        "area-zero",
        "surface-touch-positive",
        "length-zero",
        "line-touch-positive",
        "inside-zero",
        "boundary-with-inside",
        "area-exceeds-feature",
        "share-inconsistent",
        "non-finite",
        "negative",
    ],
)
```

<a id="r3-test-relation-must-match-feature-catalog"></a>

### `test_relation_must_match_feature_catalog`

function; source lines 1376–1394. Signature SHA256: `9b5056880108df50972f723f0ed19886c4aa8e87a8502d21d5f646ee9a86456c`.

```python
def test_relation_must_match_feature_catalog(
    column: str,
    value: object,
) -> None:
```

Six same-dtype relation mutations: identity kind/field, family, geometry kind, raw type code, archive SHA. _validate_result triggers source-complete path. Five reach copied-catalog-fact comparison; changed geometry kind LINE can fail intrinsic incompatible/irrelevant-metric checks first. Regex permits these branches.

Collected-case expansion: 6. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

Exact case decorators:

```python
@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("source_identity_kind", "NOT_A_KIND"),
        ("source_identity_field", "WRONG_FIELD"),
        ("feature_family", "INFORMATION"),
        ("geometry_kind", "LINE"),
        ("type_code_raw", "MUTATED"),
        ("source_archive_sha256", "b" * 64),
    ],
)
```

<a id="r3-test-feature-ids-are-globally-unique-across-catalogs"></a>

### `test_feature_ids_are_globally_unique_across_catalogs`

function; source lines 1397–1408. Signature SHA256: `27c260b0ab237025974908336502208fd00df35753d95f34a1acd6562d9b7595`.

```python
def test_feature_ids_are_globally_unique_across_catalogs() -> None:
```

Copies surface planning ID into point catalog without altering point logical/source identity. Public intrinsic deterministic-ID check rejects before global cross-catalog duplicate guard; regex accepts deterministic or globally unique. R3-T02, not direct proof of the latter branch.

Collected-case expansion: 1. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-same-source-id-is-allowed-in-distinct-logical-layers"></a>

### `test_same_source_id_is_allowed_in_distinct_logical_layers`

function; source lines 1411–1429. Signature SHA256: `b1a374d9f942cd84515ace473dc6b568a8b9eaa3bf066575c2e80f281398c640`.

```python
def test_same_source_id_is_allowed_in_distinct_logical_layers() -> None:
```

Physical prescription_line and prescription_point fixtures both use SHARED as source ID; real builder produces two relation rows with two distinct planning_feature_id values. Confirms logical-role scoping of source IDs.

Collected-case expansion: 1. AST assert statements: 2; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-corrupted-parcel-summary-is-rejected"></a>

### `test_corrupted_parcel_summary_is_rejected`

function; source lines 1432–1441. Signature SHA256: `12475d970f9161fefa4452c061f9dc412d515d10f5b328962d7a49732fc293a4`.

```python
def test_corrupted_parcel_summary_is_rejected() -> None:
```

Increments output surface relation count, retains original source parcels and valid relations. Private _validate_result reaches local summary-vs-relations check after public source revalidation; requires inconsistent with relations error.

Collected-case expansion: 1. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-corrupted-surface-union-contract-is-rejected"></a>

### `test_corrupted_surface_union_contract_is_rejected`

function; source lines 1444–1453. Signature SHA256: `8021091232d9aff4caa2df2b9c9f62688c5fa9c72bb0050c94b5dccd6e1b4f35`.

```python
def test_corrupted_surface_union_contract_is_rejected() -> None:
```

Sets output all-family covered union to 1000 m2 on 100 m2 parcel with smaller raw sum. Private _validate_result's local summary guard rejects union bound without supplied surface_work; not a test of recomputed-union geometry or tiny clamp.

Collected-case expansion: 1. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-geospatial-operation-failure-is-controlled-and-chained"></a>

### `test_geospatial_operation_failure_is_controlled_and_chained`

function; source lines 1456–1469. Signature SHA256: `640c28c177f28b4b6fe51f0ccf6f2479856bc68d0b5020754ae4c241fb8d6507`.

```python
def test_geospatial_operation_failure_is_controlled_and_chained(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

Uses real physical line fixture, monkeypatches gpd.sjoin to fail_join, then builder must raise PlanningFeaturesError matching spatial join with RuntimeError cause. Source revalidation itself is not mocked.

Collected-case expansion: 1. AST assert statements: 1; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-geospatial-operation-failure-is-controlled-and-chained-fail-join"></a>

### `test_geospatial_operation_failure_is_controlled_and_chained.fail_join`

function; source lines 1459–1460. Signature SHA256: `8f899cb46246720a848868bd09a0e417978c19c06102abc4d1ce9f1f2fd01188`.

```python
    def fail_join(*args: object, **kwargs: object) -> object:
```

Substitute for gpd.sjoin accepting arbitrary args/kwargs and always raising RuntimeError('synthetic spatial-index failure'); no geometry calculation in substitute.

<a id="r3-test-source-complete-contract-rejects-unknown-relation-parcel"></a>

### `test_source_complete_contract_rejects_unknown_relation_parcel`

function; source lines 1472–1478. Signature SHA256: `c9919db98caf30037509d12e6d8e2c67f885a4ae50cc684c4d799f8519fc4ee9`.

```python
def test_source_complete_contract_rejects_unknown_relation_parcel() -> None:
```

Changes first supplied relation parcel_id to NOT-A-SOURCE-PARCEL without changing dtype; public validator rejects membership against actual source parcels before intrinsic semantics/reconstruction.

Collected-case expansion: 1. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-source-complete-contract-rejects-coherent-parcel-metric-mutation"></a>

### `test_source_complete_contract_rejects_coherent_parcel_metric_mutation`

function; source lines 1481–1489. Signature SHA256: `d6de3e8cb247bf2ae99a343a55061b72eb6c85d12aef968d1308a6c9a7eb4fa9`.

```python
def test_source_complete_contract_rejects_coherent_parcel_metric_mutation() -> None:
```

Sets surface parcel_metric_area_m2=200 and parcel_share_pct=50 (internally coherent for 100 m2 clip) while real parcel remains 100. Public validator compares actual parcel area and rejects before reconstructing relations.

Collected-case expansion: 1. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-source-complete-contract-rejects-same-area-wrong-parcel-relation"></a>

### `test_source_complete_contract_rejects_same_area_wrong_parcel_relation`

function; source lines 1492–1498. Signature SHA256: `ef2024a244d1b972d7a951068d38b9bb525aa45fdbcbcf28a89bd2f759660cc5`.

```python
def test_source_complete_contract_rejects_same_area_wrong_parcel_relation() -> None:
```

Moves a P-1 relation to equal-area nonintersecting P-2 while keeping schema and metrics. Intrinsic/catalog checks can pass; complete rebuilt ordered row comparison rejects parcel association. Real physical and spatial reconstruction, no monkeypatch.

Collected-case expansion: 1. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-source-complete-contract-rejects-missing-expected-relation"></a>

### `test_source_complete_contract_rejects_missing_expected_relation`

function; source lines 1501–1505. Signature SHA256: `f8ee732c4f29ed0a0b4a86e48a08bd3beb8270505e85b0562270ba81cbb4e64e`.

```python
def test_source_complete_contract_rejects_missing_expected_relation() -> None:
```

Drops first row via iloc[1:].copy without resetting index. Remaining RangeIndex starts at 1, so canonical zero-based index check rejects before rebuilt relation completeness/count comparison. R3-T03; no assertion isolates missing-row detection.

Collected-case expansion: 1. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-source-complete-contract-rejects-extra-geometrically-false-relation"></a>

### `test_source_complete_contract_rejects_extra_geometrically_false_relation`

function; source lines 1508–1515. Signature SHA256: `4a01f294af4d2e7fb43bef282fb2dcad935390bb87e9e9cec984f814d0e1783f`.

```python
def test_source_complete_contract_rejects_extra_geometrically_false_relation() -> None:
```

Duplicates one relation onto nonintersecting equal-area P-2 and concat(ignore_index=True). Canonical schema passes and real expected relations are rebuilt; _compare_rebuilt_relations rejects unequal index lengths before its explicit count guard. Evidence of reconstruction rejection, not that exact count-error branch.

Collected-case expansion: 1. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-source-complete-contract-rejects-reordered-relations"></a>

### `test_source_complete_contract_rejects_reordered_relations`

function; source lines 1518–1523. Signature SHA256: `9ce8df73906f5e18c5ad355a27eda0b3ac24c118a056566baf82d21a7931f477`.

```python
def test_source_complete_contract_rejects_reordered_relations() -> None:
```

Reverses relation order then resets RangeIndex, preserving canonical shape and values. Source-complete comparison reaches expected ordered cells and rejects; does not rely on a noncanonical index.

Collected-case expansion: 1. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-source-complete-contract-rejects-noncanonical-relation-dtype"></a>

### `test_source_complete_contract_rejects_noncanonical_relation_dtype`

function; source lines 1534–1544. Signature SHA256: `d950f2c2cc92bff2f34856f07dcce18ba35905905e914980bb23b0139774ab52`.

```python
def test_source_complete_contract_rejects_noncanonical_relation_dtype(
    column: str,
    dtype: str,
) -> None:
```

Three cases cast intersection_area_m2 or point_member_count to object, or relation_type to category. Public canonical dtype check rejects after physical catalogs rebuilt; no need for geometric mutation.

Collected-case expansion: 3. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

Exact case decorators:

```python
@pytest.mark.parametrize(
    ("column", "dtype"),
    [
        ("intersection_area_m2", "object"),
        ("point_member_count", "object"),
        ("relation_type", "category"),
    ],
)
```

<a id="r3-test-source-complete-contract-rejects-relation-index-name-change"></a>

### `test_source_complete_contract_rejects_relation_index_name_change`

function; source lines 1547–1554. Signature SHA256: `0a668a41640ee7c189285a8e6c287631a5cb7ee2ec95ff59dae2f60648ab4ab7`.

```python
def test_source_complete_contract_rejects_relation_index_name_change() -> None:
```

Renames relation index changed_relation_row only; public canonical schema rejects non-null index name. Numeric row values stay unchanged.

Collected-case expansion: 1. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-source-complete-contract-rejects-relation-index-dtype-change"></a>

### `test_source_complete_contract_rejects_relation_index_dtype_change`

function; source lines 1557–1568. Signature SHA256: `6b8f3a1eec70834cc304fa7bbc52704e02da4bd0695e6f71c2a9cf008c91a7e8`.

```python
def test_source_complete_contract_rejects_relation_index_dtype_change() -> None:
```

Replaces relation index with pandas Index of int32, asserts dtype int32 and expects canonical schema error. Both index class and dtype change, so this does not isolate dtype from class.

Collected-case expansion: 1. AST assert statements: 1; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-source-complete-contract-rejects-relation-index-class-change"></a>

### `test_source_complete_contract_rejects_relation_index_class_change`

function; source lines 1571–1585. Signature SHA256: `a04f96b49a46c245acad3300399c154ca7e6cdf51d1de1b7fcd47d603cbeec25`.

```python
def test_source_complete_contract_rejects_relation_index_class_change() -> None:
```

Replaces RangeIndex with int64 pandas Index of same values, explicitly asserts original/replacement exact classes; public validation rejects class despite matching numbers.

Collected-case expansion: 1. AST assert statements: 2; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-expected-relation-hash-binds-dtype-and-index-metadata"></a>

### `test_expected_relation_hash_binds_dtype_and_index_metadata`

function; source lines 1588–1617. Signature SHA256: `7d5f1904842356fd5481c4392070146ab28dcd6095fee361093d1c2b229f2906`.

```python
def test_expected_relation_hash_binds_dtype_and_index_metadata() -> None:
```

Calls private expected-relation hasher on original and four modified frames (object metric dtype, index name, int32 index, plain int64 Index) and asserts each digest differs. No source-complete acceptance of malformed frames and no fixed cross-version golden digest claimed.

Collected-case expansion: 1. AST assert statements: 4; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-source-complete-contract-rejects-coherent-but-wrong-line-metric"></a>

### `test_source_complete_contract_rejects_coherent_but_wrong_line_metric`

function; source lines 1620–1627. Signature SHA256: `1579a7e1ebadb2cffc077cf02b3ac1a4517533f3240d84752ab297458b5b8234`.

```python
def test_source_complete_contract_rejects_coherent_but_wrong_line_metric() -> None:
```

Changes clipped length to 5 m although geometry rebuild yields 10 m, within full source length and positive. Public intrinsic coherence is insufficient; reconstructed float comparison rejects.

Collected-case expansion: 1. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-source-complete-contract-accepts-complete-parcel-output-summaries"></a>

### `test_source_complete_contract_accepts_complete_parcel_output_summaries`

function; source lines 1630–1632. Signature SHA256: `b7b48025188aa53af916341eb63f534a20a3b309c1b0a5807676ab2bffb66fda`.

```python
def test_source_complete_contract_accepts_complete_parcel_output_summaries() -> None:
```

Passes result.parcels with all 21 outputs to public validator. Normal return is the only assertion (no explicit assert); physical/catalog/relation/full-summary rebuild must complete.

Collected-case expansion: 1. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-source-complete-contract-rejects-partial-parcel-output-columns"></a>

### `test_source_complete_contract_rejects_partial_parcel_output_columns`

function; source lines 1635–1640. Signature SHA256: `929112ae1f36f480b9e20652c3232aa09b0053bdc7a2dd06c2041cb8c7d2944c`.

```python
def test_source_complete_contract_rejects_partial_parcel_output_columns() -> None:
```

Adds only planning_surface_relation_count to original parcels. Public validator rejects incomplete 21-column output set before physical source normalization.

Collected-case expansion: 1. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-source-complete-contract-rejects-corrupted-complete-parcel-summaries"></a>

### `test_source_complete_contract_rejects_corrupted_complete_parcel_summaries`

function; source lines 1643–1648. Signature SHA256: `0252b5a23dc8b27c42ce7b31430e8844fd759995d388a41212d8fd1583f1bd09`.

```python
def test_source_complete_contract_rejects_corrupted_complete_parcel_summaries() -> None:
```

Increments count in full parcel output and passes it to public validator. Rebuilt full-output column equality rejects after source/catalog/relation checks; distinct from private local summary test.

Collected-case expansion: 1. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-source-complete-contract-rejects-noncanonical-parcel-summary-dtype"></a>

### `test_source_complete_contract_rejects_noncanonical_parcel_summary_dtype`

function; source lines 1651–1658. Signature SHA256: `3ac8964df8ef874b53f0fcaa299d6302aa2f61381df8d734408520d16af7b4b1`.

```python
def test_source_complete_contract_rejects_noncanonical_parcel_summary_dtype() -> None:
```

Casts full-output covered percentage to float32 without changing value. Rebuilt parcel schema comparison rejects; this is dtype evidence, not a percentage formula attack.

Collected-case expansion: 1. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-source-complete-contract-rejects-each-corrupted-parcel-summary-fact"></a>

### `test_source_complete_contract_rejects_each_corrupted_parcel_summary_fact`

function; source lines 1672–1683. Signature SHA256: `cc774fbc2b0e05e4f0c7630937750f6c4b8294d7c7e1a6d50ac679cab94fb456`.

```python
def test_source_complete_contract_rejects_each_corrupted_parcel_summary_fact(
    column: str,
    value: object,
) -> None:
```

Six full-output changes: document ID, archive SHA, total union50, percentage50, clipped line sum5, inside-point count0. Public rebuilt parcel output comparison rejects scalar/column mismatch before later redundant local summary/lineage checks; regex is intentionally broad.

Collected-case expansion: 6. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

Exact case decorators:

```python
@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("planning_feature_document_id", "other-document"),
        ("planning_feature_archive_sha256", "f" * 64),
        ("planning_surface_covered_union_area_m2", 50.0),
        ("planning_surface_covered_pct", 50.0),
        ("planning_line_intersection_length_sum_m", 5.0),
        ("planning_point_inside_count", 0),
    ],
)
```

<a id="r3-test-source-complete-contract-rejects-duplicate-parcel-ids"></a>

### `test_source_complete_contract_rejects_duplicate_parcel_ids`

function; source lines 1686–1691. Signature SHA256: `f00fe9f0278f3f3735cdea70d7c04d0847228d9928d866305bda279dfa965dc1`.

```python
def test_source_complete_contract_rejects_duplicate_parcel_ids() -> None:
```

Duplicates original parcel row with concat(ignore_index=True); public initial parcel uniqueness gate rejects before physical source rebuild.

Collected-case expansion: 1. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-source-complete-contract-rejects-invalid-parcel-geometry"></a>

### `test_source_complete_contract_rejects_invalid_parcel_geometry`

function; source lines 1694–1701. Signature SHA256: `288ea0c82c7d9a911a99c0b444c317724c0de8cc1a00d8e370eda33e2a5973f3`.

```python
def test_source_complete_contract_rejects_invalid_parcel_geometry() -> None:
```

Changes original parcel geometry to bow-tie, preserving other input data. Public initial valid-polygon gate rejects, no repair or expected-relation comparison reached.

Collected-case expansion: 1. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-source-complete-contract-accepts-epsg4326-parcels"></a>

### `test_source_complete_contract_accepts_epsg4326_parcels`

function; source lines 1704–1708. Signature SHA256: `acf9d0e83c88f1982a454e380797dc9a93a91efb6cba72839ab37c72f49cb127`.

```python
def test_source_complete_contract_accepts_epsg4326_parcels() -> None:
```

Discards the earlier _source_complete_contract result via _, reprojects its parcels to EPSG:4326, calls intersect_parcels_with_gpu_planning_features again with the geographic parcels and same document, then validates that newly built result with those parcels. Success/no exception is the assertion; no transformed coordinates are pinned and no reuse of an old result across changed parcel inputs is proved.

Collected-case expansion: 1. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-source-document-reference-allows-one-archive-zip-suffix"></a>

### `test_source_document_reference_allows_one_archive_zip_suffix`

function; source lines 1711–1729. Signature SHA256: `77ba58cf982c357fbd0cdf1e32fbdfde0d851c70f87d09f8d012a37e74a4cb8b`.

```python
def test_source_document_reference_allows_one_archive_zip_suffix() -> None:
```

Changes synthetic archive metadata name to basename.zip, rebuilds, asserts source_archive_name keeps suffix while source_document_reference_raw stays basename, then validates successfully. One suffix case only; does not test multiple suffixes/case variants.

Collected-case expansion: 1. AST assert statements: 2; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-source-complete-contract-rejects-coherently-renamed-feature-identity"></a>

### `test_source_complete_contract_rejects_coherently_renamed_feature_identity`

function; source lines 1735–1751. Signature SHA256: `fb87936a7b88e7162a9b11f791db8f934f1829dba4e4680f15b171073c3416d2`.

```python
def test_source_complete_contract_rejects_coherently_renamed_feature_identity(
    identity_column: str,
) -> None:
```

Two cases alter either planning_feature_id OR source_feature_id in catalog and corresponding relation rows, not both identity components together. Deterministic GPU ID consistency rejects before fresh-catalog equality; not a fully coherent source-identity forgery. R3-T02.

Collected-case expansion: 2. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

Exact case decorators:

```python
@pytest.mark.parametrize(
    "identity_column", ["planning_feature_id", "source_feature_id"]
)
```

<a id="r3-test-source-complete-contract-rejects-independent-gpu-lineage-mutation"></a>

### `test_source_complete_contract_rejects_independent_gpu_lineage_mutation`

function; source lines 1767–1780. Signature SHA256: `424b6527252fa86a46af145864ca1884b0aaabbfe796e9a9a425cad24ee727a3`.

```python
def test_source_complete_contract_rejects_independent_gpu_lineage_mutation(
    column: str,
    value: str,
) -> None:
```

Eight catalog changes (provider, portal, commune, document type, archive name, IDURBA, layer, source CRS), mirrored in relations only when field exists. Intrinsic strings/schema remain valid; fresh normalized catalog comparison binds these values to physical/document context.

Collected-case expansion: 8. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

Exact case decorators:

```python
@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("source_provider", "Another provider"),
        ("source_portal", "https://example.invalid"),
        ("source_commune_code", "99999"),
        ("source_document_type", "CC"),
        ("source_archive_name", "OTHER_ARCHIVE"),
        ("source_document_reference_raw", "OTHER_ARCHIVE"),
        ("source_layer", "OTHER_SOURCE_LAYER"),
        ("source_crs", "EPSG:4326"),
    ],
)
```

<a id="r3-test-source-complete-contract-binds-gpu-document-context"></a>

### `test_source_complete_contract_binds_gpu_document_context`

function; source lines 1793–1811. Signature SHA256: `9fe99c2062a00d5c6053c9ecfc3f4662481a520df9bd7868d40660bb061efd57`.

```python
def test_source_complete_contract_binds_gpu_document_context(
    metadata_field: str,
    value: str,
) -> None:
```

Five changes to document metadata: provider/portal/commune fail config identity; changed document_type CC reaches catalog/context disagreement; changed archive name fails IDURBA during normalization. Requires PlanningFeaturesError with broad source/context patterns, not one universal lineage branch.

Collected-case expansion: 5. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

Exact case decorators:

```python
@pytest.mark.parametrize(
    ("metadata_field", "value"),
    [
        ("provider", "Another provider"),
        ("portal", "https://example.invalid"),
        ("commune_code", "99999"),
        ("document_type", "CC"),
        ("archive_name", "OTHER_ARCHIVE"),
    ],
)
```

<a id="r3-test-source-complete-contract-reloads-and-compares-source-catalog"></a>

### `test_source_complete_contract_reloads_and_compares_source_catalog`

function; source lines 1815–1846. Signature SHA256: `63d0c20a768a58e3381d0c6916cbf7d7c2974eb5cbeca0e38903798e3aae4046`.

```python
def test_source_complete_contract_reloads_and_compares_source_catalog(
    mutation: str,
) -> None:
```

Five changes to caller-held loaded frame plus its summary: geometry, label, codes, missing row or extra row. Actual GPKG bytes stay unchanged. GPU fresh-read-versus-loaded equality rejects before normalized-catalog rebuild comparison; real file reads, not physical disk rewrite.

Collected-case expansion: 5. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

Exact case decorators:

```python
@pytest.mark.parametrize("mutation", ["geometry", "raw", "code", "remove", "extra"])
```

<a id="r3-test-source-complete-contract-rejects-catalog-for-absent-gpu-layer"></a>

### `test_source_complete_contract_rejects_catalog_for_absent_gpu_layer`

function; source lines 1849–1853. Signature SHA256: `5b75121107f3d233d99c4a128ccf2cd05ea273ec84904242f6dae2fe469a417c`.

```python
def test_source_complete_contract_rejects_catalog_for_absent_gpu_layer() -> None:
```

Removes prescription_surface from related_layers only. Files/config/all_spatial_layers still declare it; GPU configured-role completeness rejects before a rebuilt empty-catalog comparison. R3-T04.

Collected-case expansion: 1. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-three-dimensional-normalized-catalogs-are-rejected"></a>

### `test_three_dimensional_normalized_catalogs_are_rejected`

function; source lines 1867–1876. Signature SHA256: `17921a8a7fa04bb130878531d7441d22f558aa041266ba6c8a6a1d9db29922ea`.

```python
def test_three_dimensional_normalized_catalogs_are_rejected(
    catalog_name: str,
    geometry: object,
) -> None:
```

Three cases inject Z polygon/line/point into supplied canonical catalog while physical source stays XY. After source rebuild, intrinsic catalog coordinate-dimension guard rejects; no M or ZM injection.

Collected-case expansion: 3. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

Exact case decorators:

```python
@pytest.mark.parametrize(
    ("catalog_name", "geometry"),
    [
        (
            "surface_features",
            Polygon([(0, 0, 1), (0, 10, 1), (10, 10, 1), (10, 0, 1)]),
        ),
        ("line_features", LineString([(-1, 5, 1), (11, 5, 1)])),
        ("point_features", Point(5, 5, 1)),
    ],
)
```

<a id="r3-test-two-dimensional-normalized-catalogs-remain-valid"></a>

### `test_two_dimensional_normalized_catalogs_remain_valid`

function; source lines 1879–1887. Signature SHA256: `331e97acb81ecca6b799076357accfaac5b7e80cc9552f9787b7477145efac58`.

```python
def test_two_dimensional_normalized_catalogs_remain_valid() -> None:
```

Asserts no has_z in each catalog and successfully runs public validator on physical fixture. Assertion alone does not detect M, although the validator uses coordinate dimension ==2.

Collected-case expansion: 1. AST assert statements: 1; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-gpu-source-z-is-normalized-to-canonical-2d"></a>

### `test_gpu_source_z_is_normalized_to_canonical_2d`

function; source lines 1906–1913. Signature SHA256: `cd80cd7ffe85865f5bcde2d360c59af20135b8de7b77317ea6f480feba04967f`.

```python
def test_gpu_source_z_is_normalized_to_canonical_2d(
    logical: str,
    geometry: object,
    catalog_name: str,
) -> None:
```

Three physical XYZ source kinds pass real builder; test asserts resulting catalog has no Z. Proves these Z fixtures are dropped, not tested preservation/rejection of M/ZM across drivers.

Collected-case expansion: 3. AST assert statements: 1; exception contexts/equality helpers and no-exception success are also assertions, as described above.

Exact case decorators:

```python
@pytest.mark.parametrize(
    ("logical", "geometry", "catalog_name"),
    [
        (
            "prescription_surface",
            Polygon([(0, 0, 1), (0, 10, 1), (10, 10, 1), (10, 0, 1)]),
            "surface_features",
        ),
        (
            "prescription_line",
            LineString([(0, 5, 1), (10, 5, 1)]),
            "line_features",
        ),
        ("prescription_point", Point(5, 5, 1), "point_features"),
    ],
)
```

<a id="r3-test-source-complete-contract-rejects-tampered-gpkg-inventory-hash"></a>

### `test_source_complete_contract_rejects_tampered_gpkg_inventory_hash`

function; source lines 1916–1931. Signature SHA256: `7b0d55c68a914db691bd4e8b85afb5304b13a5016d25297c2c3257a54e5a3c00`.

```python
def test_source_complete_contract_rejects_tampered_gpkg_inventory_hash() -> None:
```

Changes one envelope file SHA to "f" * 64, leaves manifest and physical GPKG bytes unchanged. Public GPU extraction-manifest/inventory consistency rejects before selected-dataset per-file validation. Broad source/file/inventory/SHA regex.

Collected-case expansion: 1. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-source-complete-contract-rejects-tampered-gpkg-size"></a>

### `test_source_complete_contract_rejects_tampered_gpkg_size`

function; source lines 1934–1951. Signature SHA256: `596229ccf1a75bb968fcad6f79e63bca19ce7106598bed5f28973c00befdea46`.

```python
def test_source_complete_contract_rejects_tampered_gpkg_size() -> None:
```

Changes one envelope file size by +1 with unchanged marker/disk. Same early extraction-manifest mismatch; does not isolate selected-dataset size guard.

Collected-case expansion: 1. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-source-complete-contract-rejects-changed-gpkg-bytes"></a>

### `test_source_complete_contract_rejects_changed_gpkg_bytes`

function; source lines 1954–1960. Signature SHA256: `c0b68226be0694538f014d1c842026856b4cb67d50203beecae84be79c8f74ca`.

```python
def test_source_complete_contract_rejects_changed_gpkg_bytes() -> None:
```

Appends bytes to real synthetic GPKG with unchanged manifest/envelope. Recomputed extraction inventory no longer matches marker; public validation rejects before driver read. Real disk tampering, no redownload.

Collected-case expansion: 1. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-source-complete-contract-rejects-same-size-gpkg-byte-tamper"></a>

### `test_source_complete_contract_rejects_same_size_gpkg_byte_tamper`

function; source lines 1963–1970. Signature SHA256: `66b8704753781b7c57e8e35a9bb6ad2b379410dbf67ebbde344c708c8ce790e0`.

```python
def test_source_complete_contract_rejects_same_size_gpkg_byte_tamper() -> None:
```

Reads GPKG bytes, flips last byte and rewrites same length. Manifest SHA mismatch rejects even though size unchanged; no assumption that driver must parse corruption.

Collected-case expansion: 1. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-source-complete-contract-rejects-coherently-changed-physical-gpkg"></a>

### `test_source_complete_contract_rejects_coherently_changed_physical_gpkg`

function; source lines 1973–1987. Signature SHA256: `395d0fd6419f29a3b972b743dbd5df71dc1c367eaba7e41834b1ef8d8ec3e8bb`.

```python
def test_source_complete_contract_rejects_coherently_changed_physical_gpkg() -> None:
```

Rewrites actual GPKG LIBELLE, refreshes inventory/manifest/discovery, keeps loaded source data stale. Public physical reread passes refreshed byte inventory but rejects loaded-versus-fresh attributes. Not a bypass test with every envelope/data value regenerated.

Collected-case expansion: 1. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-source-complete-contract-rejects-changed-physical-gpkg-geometry"></a>

### `test_source_complete_contract_rejects_changed_physical_gpkg_geometry`

function; source lines 1990–2004. Signature SHA256: `a347e9995042c6e9c9df104027e3847cbdeec89fdbfe92270c4a5a31cc00d7c0`.

```python
def test_source_complete_contract_rejects_changed_physical_gpkg_geometry() -> None:
```

Rewrites physical polygon to half area and refreshes manifest/inventory but retains original loaded data. GPU WKB equality rejects after real reread, before normalized catalog comparison.

Collected-case expansion: 1. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-source-complete-contract-rejects-reordered-physical-gpkg-rows"></a>

### `test_source_complete_contract_rejects_reordered_physical_gpkg_rows`

function; source lines 2007–2034. Signature SHA256: `02f87716731a01dc2a044c3d52eddf0c0493958c05da3896863f445ee11761fa`.

```python
def test_source_complete_contract_rejects_reordered_physical_gpkg_rows() -> None:
```

Builds two source rows, reverses them in real GPKG write, resets physical write index and refreshes file inventory. Loaded frame remains original order; ordered data comparison rejects.

Collected-case expansion: 1. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-source-complete-contract-rejects-loaded-source-attrs-not-on-disk"></a>

### `test_source_complete_contract_rejects_loaded_source_attrs_not_on_disk`

function; source lines 2037–2050. Signature SHA256: `47f88667c59c8ac67bf2aa8712e31b22d10ee0c8af80abf274e74171857236d5`.

```python
def test_source_complete_contract_rejects_loaded_source_attrs_not_on_disk() -> None:
```

Adds unpersisted_source_note to loaded GeoDataFrame.attrs only; replaces envelope layer, leaves file intact. Real reread lacks attrs and GPU exact loaded-frame metadata comparison rejects.

Collected-case expansion: 1. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-source-complete-contract-rejects-dataset-outside-extraction-root"></a>

### `test_source_complete_contract_rejects_dataset_outside_extraction_root`

function; source lines 2053–2063. Signature SHA256: `d6d5dfdaceb69a18fdbdfc288e73ed85d81983cce2e93cd4ec83b0c8745fce78`.

```python
def test_source_complete_contract_rejects_dataset_outside_extraction_root(
    tmp_path: Path,
) -> None:
```

Copies selected GPKG to tmp_path outside fixture extraction and swaps inspected/all-spatial references only. Configured discovery still returns original inside reference, so source inventory/discovery mismatch rejects before selected-dataset containment guard. Real copy, but not a branch-isolated path-escape regression. R3-T04.

Collected-case expansion: 1. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-source-complete-contract-rejects-linked-spatial-dataset"></a>

### `test_source_complete_contract_rejects_linked_spatial_dataset`

function; source lines 2066–2082. Signature SHA256: `9cd1e6fe494dec0f62327821f0f46384fd56a44d8efaba5bad6c4226c873a1cf`.

```python
def test_source_complete_contract_rejects_linked_spatial_dataset(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

Monkeypatches GPU _is_link_or_junction to report true for actual dataset; public extraction inventory rejects link during root walk before selected reader. No OS symlink/junction created; simulates detector outcome only.

Collected-case expansion: 1. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-source-complete-contract-rejects-linked-spatial-dataset-synthetic-link"></a>

### `test_source_complete_contract_rejects_linked_spatial_dataset.synthetic_link`

function; source lines 2073–2074. Signature SHA256: `24c9e5a33b551c65a92c28708830e0a04af004f2804325cd6fb21d1bf7215a19`.

```python
    def synthetic_link(path: Path) -> bool:
```

Returns true for the selected dataset without calling the real detector; for every other path, returns actual_link_check(path), which can also be true. Used solely by parent test; no filesystem mutation.

<a id="r3-shapefile-source-complete-contract"></a>

### `_shapefile_source_complete_contract`

function; source lines 2085–2107. Signature SHA256: `ee0d906ab25fa8afae64d84d6d090301b3f3deceeef5fbf5f3ab830fce1b1bef`.

```python
def _shapefile_source_complete_contract(
    root: Path,
) -> tuple[GpuPlanningDocument, gpd.GeoDataFrame, ParcelPlanningFeaturesResult]:
```

Writes and rereads real prescription-surface Shapefile with CNIG ID SHAPE-1 and code pair 07/04; builds local document and 100 m2 parcel result. Returns document, parcels, result for sidecar tests; core/optional files are real temp bytes, archive envelope fabricated.

<a id="r3-shapefile-ogr-fid-source-complete-contract"></a>

### `_shapefile_ogr_fid_source_complete_contract`

function; source lines 2110–2132. Signature SHA256: `4512feea4d0a117263d88459cab3cd0f8798ae0ef0abe0bff90fbe8ec3e8ad9f`.

```python
def _shapefile_ogr_fid_source_complete_contract(
    root: Path,
) -> tuple[GpuPlanningDocument, gpd.GeoDataFrame, ParcelPlanningFeaturesResult]:
```

Writes two adjacent 50 m2 polygons to real Shapefile after dropping LIB_IDPSC; source reread has physical FIDs0/1. Builds document/result used by changed-returned-FID tests; no official archive.

<a id="r3-test-source-complete-contract-binds-every-shapefile-sidecar"></a>

### `test_source_complete_contract_binds_every_shapefile_sidecar`

function; source lines 2135–2157. Signature SHA256: `4f0da6dddb059b9c5463f03abaad094e20b9bf38f82c34fb8dd5ff70aa7c9345`.

```python
def test_source_complete_contract_binds_every_shapefile_sidecar(
    tmp_path: Path,
) -> None:
```

Removes .prj record only from envelope inventory, retaining actual file and manifest. Public extraction manifest consistency rejects before dataset sidecar-family enumeration. Does not test every sidecar extension despite name. R3-T04.

Collected-case expansion: 1. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-source-complete-contract-rejects-changed-or-reordered-ogr-fids"></a>

### `test_source_complete_contract_rejects_changed_or_reordered_ogr_fids`

function; source lines 2161–2183. Signature SHA256: `b803c2d03c356068fc56e5401f01ec63bd1d309121d8a5dd52bf7919457fa524`.

```python
def test_source_complete_contract_rejects_changed_or_reordered_ogr_fids(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    changed_fids: tuple[int, int],
) -> None:
```

Two monkeypatched returned indexes (10,11) or (1,0) on real reread of no-CNIG-ID two-row Shapefile. Stored FIDs/bytes unchanged; refreshed validated FID identities yield normalized catalog mismatch against original result. Expected controlled source/FID/identity/catalog error, not proof of disk FID rewriting detection.

Collected-case expansion: 2. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

Exact case decorators:

```python
@pytest.mark.parametrize("changed_fids", [(10, 11), (1, 0)])
```

<a id="r3-test-source-complete-contract-rejects-changed-or-reordered-ogr-fids-changed-fid-read"></a>

### `test_source_complete_contract_rejects_changed_or_reordered_ogr_fids.changed_fid_read`

function; source lines 2171–2175. Signature SHA256: `17d7cd7d479d3f429a3688ca2bbbafd0369801929bd72801a068963564ee4203`.

```python
    def changed_fid_read(*args: object, **kwargs: object) -> gpd.GeoDataFrame:
```

Delegates to actual Pyogrio then, only when fid_as_index requested, replaces returned frame index with changed_fids/name fid. Preserves real attributes/geometries; mutates returned frame, not file.

<a id="r3-test-source-complete-contract-requires-shapefile-core-members"></a>

### `test_source_complete_contract_requires_shapefile_core_members`

function; source lines 2186–2193. Signature SHA256: `3e0af5a5a911f84d2ff587bb306857c3853607f4aec24dd85e67cdf5df46a946`.

```python
def test_source_complete_contract_requires_shapefile_core_members(
    tmp_path: Path,
) -> None:
```

Deletes actual .shx after valid fixture build, keeps manifest unchanged. Root inventory mismatch rejects before selected Shapefile required-core branch. No assertions about missing .shp/.dbf; R3-T04.

Collected-case expansion: 1. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-source-complete-contract-rejects-changed-shapefile-sidecar-bytes"></a>

### `test_source_complete_contract_rejects_changed_shapefile_sidecar_bytes`

function; source lines 2196–2207. Signature SHA256: `748bcfae9c06222fef73d5b8c0467f1394a0ce091fd58852365eed33842af64e`.

```python
def test_source_complete_contract_rejects_changed_shapefile_sidecar_bytes(
    tmp_path: Path,
) -> None:
```

Rewrites the actual .cpg using cpg.write_text("UTF-8\n", encoding="utf-8"), leaving the inventory/manifest stale. This writes UTF-8 text with a trailing newline (platform text-mode newline translation), not a change to the Latin-1 charset family. Extraction inventory SHA/size mismatch rejects before selected sidecar family comparison or driver read. Real local tamper of one extension.

Collected-case expansion: 1. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-dotted-sibling-dataset-is-not-a-sidecar-and-makes-role-ambiguous"></a>

### `test_dotted_sibling_dataset_is_not_a_sidecar_and_makes_role_ambiguous`

function; source lines 2210–2227. Signature SHA256: `6e1b324b40eaa7ccec3cb6b23beee3f57ae9dbd7eb5c24980faa2739d4efedab`.

```python
def test_dotted_sibling_dataset_is_not_a_sidecar_and_makes_role_ambiguous(
    tmp_path: Path,
) -> None:
```

First validates original Shapefile fixture successfully; writes separate <stem>.archive.shp and refreshes inventory/manifest/discovery. Both physical datasets match role tokens, so configured logical discovery is ambiguous and public wrapper requires exact physical revalidation error. Real separate dataset, not just a renamed .prj.

Collected-case expansion: 1. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-batch-gpu-revalidation-rejects-malformed-layer-items"></a>

### `test_batch_gpu_revalidation_rejects_malformed_layer_items`

function; source lines 2231–2239. Signature SHA256: `8854cd63d243281b24d814a8e4bda368a4b8b330c65f1d63d08bc3048b16b6a5`.

```python
def test_batch_gpu_revalidation_rejects_malformed_layer_items(
    bad_item: object,
) -> None:
```

Two direct GPU batch calls with None/object as requested layer item in otherwise valid physical document; require GpuSpatialInspectionError. Exercises dependency API, not stage wrapper; fixture setup is real.

Collected-case expansion: 2. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

Exact case decorators:

```python
@pytest.mark.parametrize("bad_item", [None, object()])
```

<a id="r3-test-batch-gpu-revalidation-rejects-malformed-planning-document"></a>

### `test_batch_gpu_revalidation_rejects_malformed_planning_document`

function; source lines 2242–2247. Signature SHA256: `0c65b6fae55e6504ed4bcab48b254dbc0d4d17b259bc9975fc5890145a272a9e`.

```python
def test_batch_gpu_revalidation_rejects_malformed_planning_document() -> None:
```

Direct GPU batch call with object() and empty layers; requires GpuSpatialInspectionError before source IO. No planning stage call or downloaded source.

Collected-case expansion: 1. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-batch-gpu-revalidation-rejects-duplicate-logical-name"></a>

### `test_batch_gpu_revalidation_rejects_duplicate_logical_name`

function; source lines 2250–2257. Signature SHA256: `6b81f31521caa2d9a05726f39a5c1aa712330e17b360cede325e9604d9a9982d`.

```python
def test_batch_gpu_revalidation_rejects_duplicate_logical_name() -> None:
```

Direct GPU batch call with same real inspected layer twice; requires GpuSpatialInspectionError matching duplicate. Does not test a duplicate physical-file collision across different roles.

Collected-case expansion: 1. AST assert statements: 0; exception contexts/equality helpers and no-exception success are also assertions, as described above.

<a id="r3-test-common-planning-contracts-import-without-initializing-stages"></a>

### `test_common_planning_contracts_import_without_initializing_stages`

function; source lines 2273–2287. Signature SHA256: `ad21e4d4cbb032a672b4559d37c00bc3dacbcf84bffda3eef7347ceed3cbca9b`.

```python
def test_common_planning_contracts_import_without_initializing_stages(
    statement: str,
) -> None:
```

Two real fresh Python subprocesses import common planning-feature or BESS application contract, then assert landscout.stages absent from sys.modules; parent requires exit0 with stderr on failure. Tests these imports only, not every cycle. Existing subprocess.run has no timeout argument; unchanged in R3, distinct from auditor subprocess tests.

Collected-case expansion: 2. AST assert statements: 1; exception contexts/equality helpers and no-exception success are also assertions, as described above.

Exact case decorators:

```python
@pytest.mark.parametrize(
    "statement",
    [
        (
            "from landscout.common.planning_feature_contract import "
            "validate_intrinsic_planning_feature_relations"
        ),
        (
            "from landscout.common.bess_application_contract import "
            "validate_bess_application_feature_catalogs"
        ),
    ],
)
```

## Change impact and exact source snapshot

A source change requires review of this companion, its exact fingerprint/snapshot,
qualified signatures, schemas, callers and assertion limits. R3 changes documentation
only; no schema/hash migration, code/test edit or new authority is introduced.

The following complete UTF-8 file is an aid to verification, not a substitute for
the semantic explanations above. It reproduces exact Git content bytes inside the fence.

```python
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from copy import deepcopy
from dataclasses import FrozenInstanceError, replace
from hashlib import sha256
from pathlib import Path

import geopandas as gpd  # type: ignore[import-untyped]
import numpy as np
import pandas as pd
import pytest
from geopandas.testing import assert_geodataframe_equal
from pandas.testing import assert_frame_equal
from shapely.geometry import (
    LineString,
    MultiLineString,
    MultiPoint,
    MultiPolygon,
    Point,
    Polygon,
)

from landscout import stages
from landscout.common.planning_feature_contract import (
    validate_intrinsic_planning_feature_relations,
)
from landscout.sources import gpu_fr as gpu_source_module
from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialLayerReference,
    load_gpu_source_config,
)
from landscout.stages import enrich_planning_features as planning_features_module
from landscout.stages.enrich_planning_features import (
    ParcelPlanningFeaturesResult,
    PlanningFeatureInputValidation,
    PlanningFeaturesError,
    _validate_result,
    intersect_parcels_with_gpu_planning_features,
    validate_normalized_planning_feature_inputs,
)

DOCUMENT_ID = "doc-1"
ARCHIVE_NAME = "31395_PLU_20240215"
ARCHIVE_SHA = "a" * 64
STANDARD = "CNIG PLU v2017"
LOCAL_ENGINEERING_CRS = (
    'ENGCRS["Local",EDATUM["Unknown"],CS[Cartesian,2],'
    'AXIS["x",east,LENGTHUNIT["metre",1]],'
    'AXIS["y",north,LENGTHUNIT["metre",1]]]'
)


def _rectangle(x1: float, y1: float, x2: float, y2: float) -> Polygon:
    return Polygon([(x1, y1), (x1, y2), (x2, y2), (x2, y1), (x1, y1)])


def _parcels(
    geometries: list[object] | None = None,
    *,
    ids: list[object] | None = None,
    crs: str | None = "EPSG:2154",
) -> gpd.GeoDataFrame:
    values = geometries or [_rectangle(0, 0, 10, 10)]
    frame = gpd.GeoDataFrame(
        {
            "parcel_id": ids or [f"P-{index + 1}" for index in range(len(values))],
            "existing_zoning_fact": np.arange(len(values), dtype="int64") + 7,
        },
        geometry=values,
        crs="EPSG:2154",
        index=[50 + index for index in range(len(values))],
    )
    if crs is None:
        return frame.set_crs(None, allow_override=True)
    return frame if crs == "EPSG:2154" else frame.to_crs(crs)


def _source_frame(
    logical: str,
    geometries: list[object],
    *,
    ids: list[object] | None = None,
    type_codes: list[object] | None = None,
    subtype_codes: list[object] | None = None,
    document_refs: list[object] | None = None,
    crs: str | None = "EPSG:2154",
) -> gpd.GeoDataFrame:
    count = len(geometries)
    prescription = logical.startswith("prescription")
    identity = "LIB_IDPSC" if prescription else "LIB_IDINFO"
    type_field = "TYPEPSC" if prescription else "TYPEINF"
    subtype_field = "STYPEPSC" if prescription else "STYPEINF"
    data: dict[str, object] = {
        "LIBELLE": [f"Label {index}" for index in range(count)],
        "TXT": [None if index % 2 else f"Text {index}" for index in range(count)],
        type_field: type_codes or [f"T{index}" for index in range(count)],
        subtype_field: subtype_codes or [f"S{index}" for index in range(count)],
        "NOMFIC": [
            None if index % 2 else f"rule-{index}.pdf" for index in range(count)
        ],
        "URLFIC": [None] * count,
        "IDURBA": document_refs or [ARCHIVE_NAME] * count,
        "DATVALID": ["20240215"] * count,
        identity: ids or [f"SRC-{logical}-{index}" for index in range(count)],
    }
    frame = gpd.GeoDataFrame(data, geometry=geometries, crs="EPSG:2154")
    if crs is None:
        return frame.set_crs(None, allow_override=True)
    if crs == "IGNF:LAMB93":
        return frame.set_crs(crs, allow_override=True)
    return frame if crs == "EPSG:2154" else frame.to_crs(crs)


def _summary(
    frame: gpd.GeoDataFrame,
    source_layer: str,
    *,
    document_id: str = DOCUMENT_ID,
    archive_sha: str = ARCHIVE_SHA,
) -> GpuLayerSummary:
    geometry = frame.geometry
    non_null = ~geometry.isna()
    non_empty = non_null & ~geometry.is_empty
    return GpuLayerSummary(
        source_document_id=document_id,
        source_archive_sha256=archive_sha,
        source_layer=source_layer,
        crs="UNKNOWN" if frame.crs is None else frame.crs.to_string(),
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


def _inspected(logical: str, frame: gpd.GeoDataFrame) -> GpuInspectedLayer:
    source_layer = f"SOURCE_{logical.upper()}"
    reference = GpuSpatialLayerReference(
        dataset_path=Path(f"synthetic-{logical}.gpkg"),
        source_layer=source_layer,
        driver="GPKG",
    )
    return GpuInspectedLayer(
        logical_name=logical,  # type: ignore[arg-type]
        reference=reference,
        data=frame,
        summary=_summary(frame, source_layer),
    )


def _physical_inventory(root: Path) -> tuple[GpuExtractedFile, ...]:
    records: list[GpuExtractedFile] = []
    for path in sorted((item for item in root.rglob("*") if item.is_file()), key=str):
        if path.parent == root and path.name == EXTRACTION_MANIFEST_NAME:
            continue
        suffix = path.suffix.casefold()
        records.append(
            GpuExtractedFile(
                relative_path=path.relative_to(root).as_posix(),
                file_type=suffix.lstrip(".") or "none",
                size_bytes=path.stat().st_size,
                sha256=sha256(path.read_bytes()).hexdigest(),
                category="SPATIAL_DATA",
            )
        )
    return tuple(records)


def _write_extraction_manifest(
    root: Path,
    archive_sha256: str,
    files: tuple[GpuExtractedFile, ...],
) -> None:
    payload = {
        "schema_version": 2,
        "archive_sha256": archive_sha256,
        "files": [
            {
                "relative_path": item.relative_path,
                "size_bytes": item.size_bytes,
                "sha256": item.sha256,
            }
            for item in files
        ],
    }
    (root / EXTRACTION_MANIFEST_NAME).write_text(
        json.dumps(payload, sort_keys=True, separators=(",", ":")),
        encoding="utf-8",
    )


def _materialize_layer(root: Path, layer: GpuInspectedLayer) -> GpuInspectedLayer:
    reference = layer.reference
    if reference.dataset_path.is_file():
        path = reference.dataset_path.resolve()
    else:
        path = root / f"{layer.logical_name}.gpkg"
        layer.data.to_file(
            path,
            layer=reference.source_layer,
            driver="GPKG",
            engine="pyogrio",
            index=False,
        )
        reference = replace(reference, dataset_path=path, driver="GPKG")
    reread = gpd.read_file(
        path,
        layer=reference.source_layer if reference.driver == "GPKG" else None,
        engine="pyogrio",
    )
    return replace(
        layer,
        reference=replace(reference, dataset_path=path),
        data=reread,
        summary=_summary(reread, reference.source_layer),
    )


def _planning_document(
    layers: list[GpuInspectedLayer] | None = None,
) -> GpuPlanningDocument:
    requested_layers = list(layers or [])
    existing_paths = [
        layer.reference.dataset_path.resolve()
        for layer in requested_layers
        if layer.reference.dataset_path.is_file()
    ]
    extraction_root = (
        existing_paths[0].parent
        if existing_paths
        else Path(tempfile.mkdtemp(prefix="landscout-feature-source-"))
    )
    related = tuple(
        _materialize_layer(extraction_root, layer) for layer in requested_layers
    )
    metadata = GpuDocumentMetadata(
        provider="Géoportail de l'Urbanisme",
        portal="G\u00e9oportail de l'Urbanisme",
        commune_code="31395",
        partition="DU_31395",
        document_id=DOCUMENT_ID,
        document_family="DU",
        document_type="PLU",
        document_title="Muret PLU",
        status="document.production",
        legal_status="APPROVED",
        effective_status="EN_VIGUEUR",
        version="10",
        archive_name=ARCHIVE_NAME,
        publication_timestamp=None,
        update_timestamp=None,
        revision_date=None,
        producer=None,
        standard_model=STANDARD,
        projection="EPSG:2154",
        metadata_identifier=None,
        source_url="https://www.geoportail-urbanisme.gouv.fr/api/document/download-by-partition/DU_31395",
        written_files=(),
    )
    archive = GpuArchiveDownload(
        document=metadata,
        download_timestamp="2026-08-12T12:00:00+00:00",
        filename=f"{ARCHIVE_NAME}.zip",
        archive_format="zip",
        file_size=1,
        sha256=ARCHIVE_SHA,
        path=Path("synthetic.zip"),
        cache_hit=True,
    )
    zoning_frame = gpd.GeoDataFrame(
        {"zone": ["Z"]}, geometry=[_rectangle(-10, -10, 20, 20)], crs="EPSG:2154"
    )
    zoning_path = extraction_root / "zoning.gpkg"
    zoning_frame.to_file(
        zoning_path,
        layer="ZONING",
        driver="GPKG",
        engine="pyogrio",
        index=False,
    )
    zoning_frame = gpd.read_file(zoning_path, layer="ZONING", engine="pyogrio")
    zoning_ref = GpuSpatialLayerReference(zoning_path, "ZONING", "GPKG")
    zoning = GpuInspectedLayer(
        logical_name="zoning",
        reference=zoning_ref,
        data=zoning_frame,
        summary=_summary(zoning_frame, "ZONING"),
    )
    inventory = _physical_inventory(extraction_root)
    _write_extraction_manifest(extraction_root, ARCHIVE_SHA, inventory)
    extraction = GpuExtraction(
        archive=archive,
        extraction_root=extraction_root,
        files=inventory,
        standard_models=(STANDARD,),
        cache_hit=True,
    )
    config_payload = load_gpu_source_config(
        Path("configs/sources/gpu_fr.yaml")
    ).model_dump(mode="python")
    for role in config_payload["spatial_layers"]:
        config_payload["spatial_layers"][role]["match_tokens"] = [f"unused_{role}"]
    config_payload["spatial_layers"]["zoning"]["match_tokens"] = ["ZONING"]
    for layer in related:
        config_payload["spatial_layers"][layer.logical_name]["match_tokens"] = [
            layer.reference.source_layer
        ]
    source_config = GpuSourceConfig.model_validate(config_payload)
    related_by_logical_name = {layer.logical_name: layer for layer in related}
    related = tuple(
        related_by_logical_name[logical_name]
        for logical_name in gpu_source_module._GPU_LOGICAL_LAYER_NAMES
        if logical_name != "zoning" and logical_name in related_by_logical_name
    )
    return GpuPlanningDocument(
        source_config=source_config,
        source_config_sha256=gpu_source_module._source_config_sha256(source_config),
        extraction=extraction,
        all_spatial_layers=gpu_source_module.discover_gpu_spatial_layers(extraction),
        zoning=zoning,
        related_layers=related,
    )


def _run(
    layers: list[GpuInspectedLayer],
    parcels: gpd.GeoDataFrame | None = None,
) -> ParcelPlanningFeaturesResult:
    return intersect_parcels_with_gpu_planning_features(
        parcels if parcels is not None else _parcels(),
        _planning_document(layers),
    )


def test_only_high_level_api_is_exported() -> None:
    assert (
        stages.intersect_parcels_with_gpu_planning_features
        is intersect_parcels_with_gpu_planning_features
    )
    assert "intersect_parcels_with_gpu_planning_features" in stages.__all__
    assert stages.PlanningFeaturesError is PlanningFeaturesError
    assert stages.ParcelPlanningFeaturesResult is ParcelPlanningFeaturesResult
    assert "PlanningFeaturesError" in stages.__all__
    assert "ParcelPlanningFeaturesResult" in stages.__all__


def test_result_is_frozen() -> None:
    result = _run([])
    with pytest.raises(FrozenInstanceError):
        result.parcels = result.parcels.copy()  # type: ignore[misc]


def test_surface_full_overlap_normalizes_raw_values_and_lineage() -> None:
    layer = _inspected(
        "prescription_surface",
        _source_frame(
            "prescription_surface",
            [_rectangle(0, 0, 10, 10)],
            ids=["PSC-1"],
            type_codes=["DYNAMIC-18"],
            subtype_codes=["04"],
            crs="IGNF:LAMB93",
        ),
    )
    result = _run([layer])

    feature = result.surface_features.iloc[0]
    assert feature["planning_feature_id"] == (
        f"GPU:{DOCUMENT_ID}:prescription_surface:PSC-1"
    )
    assert feature["source_feature_id"] == "PSC-1"
    assert feature["source_identity_kind"] == "CNIG_ATTRIBUTE"
    assert feature["source_identity_field"] == "LIB_IDPSC"
    assert feature["feature_family"] == "PRESCRIPTION"
    assert feature["geometry_kind"] == "SURFACE"
    assert feature["type_code_raw"] == "DYNAMIC-18"
    assert feature["subtype_code_raw"] == "04"
    assert feature["label_raw"] == "Label 0"
    assert feature["text_raw"] == "Text 0"
    assert feature["source_document_id"] == DOCUMENT_ID
    assert feature["source_archive_sha256"] == ARCHIVE_SHA
    assert feature["source_layer"] == "SOURCE_PRESCRIPTION_SURFACE"
    # The physical GPKG round-trip exposes the equivalent canonical CRS identity.
    assert feature["source_crs"] == "EPSG:2154"
    assert feature["feature_area_m2"] == pytest.approx(100.0)
    assert result.surface_features.crs.to_epsg() == 2154

    relation = result.relations.iloc[0]
    assert relation["source_identity_kind"] == "CNIG_ATTRIBUTE"
    assert relation["source_identity_field"] == "LIB_IDPSC"
    assert relation["relation_type"] == "AREA_OVERLAP"
    assert relation["intersection_area_m2"] == pytest.approx(100.0)
    assert relation["parcel_share_pct"] == pytest.approx(100.0)
    assert relation["feature_share_pct"] == pytest.approx(100.0)
    assert pd.isna(relation["intersection_length_m"])
    parcel = result.parcels.iloc[0]
    assert parcel["planning_surface_relation_count"] == 1
    assert parcel["planning_surface_area_overlap_count"] == 1
    assert parcel["planning_surface_covered_union_area_m2"] == pytest.approx(100.0)
    assert parcel["planning_surface_covered_pct"] == pytest.approx(100.0)
    assert parcel["prescription_surface_relation_count"] == 1
    assert parcel["information_surface_relation_count"] == 0


def test_surface_partial_and_touch_relations() -> None:
    frame = _source_frame(
        "prescription_surface",
        [_rectangle(0, 0, 5, 10), _rectangle(10, 0, 20, 10)],
        ids=["PART", "TOUCH"],
    )
    result = _run([_inspected("prescription_surface", frame)])
    relations = result.relations.set_index("source_feature_id")
    assert relations.loc["PART", "relation_type"] == "AREA_OVERLAP"
    assert relations.loc["PART", "intersection_area_m2"] == pytest.approx(50.0)
    assert relations.loc["TOUCH", "relation_type"] == "TOUCH_ONLY"
    assert relations.loc["TOUCH", "intersection_area_m2"] == pytest.approx(0.0)
    assert result.parcels.iloc[0]["planning_surface_touch_count"] == 1


def test_overlapping_surface_union_is_not_double_counted() -> None:
    prescription = _inspected(
        "prescription_surface",
        _source_frame(
            "prescription_surface",
            [_rectangle(0, 0, 10, 10)],
            ids=["WHOLE"],
        ),
    )
    information = _inspected(
        "information_surface",
        _source_frame(
            "information_surface",
            [_rectangle(0, 0, 5, 10)],
            ids=["HALF"],
            type_codes=["99"],
            subtype_codes=["00"],
        ),
    )
    parcel = _run([prescription, information]).parcels.iloc[0]
    assert parcel["planning_surface_intersection_area_sum_m2"] == pytest.approx(150.0)
    assert parcel["planning_surface_covered_union_area_m2"] == pytest.approx(100.0)
    assert parcel["planning_surface_covered_pct"] == pytest.approx(100.0)
    assert parcel["prescription_surface_covered_union_area_m2"] == pytest.approx(100.0)
    assert parcel["information_surface_covered_union_area_m2"] == pytest.approx(50.0)


@pytest.mark.parametrize(
    "geometry",
    [
        _rectangle(0, 0, 10, 10),
        MultiPolygon([_rectangle(0, 0, 4, 10), _rectangle(6, 0, 10, 10)]),
    ],
)
def test_polygon_and_multipolygon_surfaces(geometry: object) -> None:
    result = _run(
        [
            _inspected(
                "information_surface", _source_frame("information_surface", [geometry])
            )
        ]
    )
    assert len(result.relations) == 1
    assert result.relations.iloc[0]["intersection_area_m2"] > 0


def test_line_crossing_and_partly_inside() -> None:
    frame = _source_frame(
        "prescription_line",
        [LineString([(-5, 5), (15, 5)]), LineString([(5, 5), (15, 5)])],
        ids=["CROSS", "PART"],
        type_codes=["15", "15"],
        subtype_codes=["01", "00"],
    )
    result = _run([_inspected("prescription_line", frame)])
    relations = result.relations.set_index("source_feature_id")
    assert relations.loc["CROSS", "relation_type"] == "LENGTH_OVERLAP"
    assert relations.loc["CROSS", "intersection_length_m"] == pytest.approx(10.0)
    assert relations.loc["CROSS", "source_line_length_m"] == pytest.approx(20.0)
    assert relations.loc["PART", "intersection_length_m"] == pytest.approx(5.0)
    parcel = result.parcels.iloc[0]
    assert parcel["planning_line_relation_count"] == 2
    assert parcel["planning_line_intersection_length_sum_m"] == pytest.approx(15.0)


def test_line_boundary_touch_is_zero_length() -> None:
    frame = _source_frame(
        "prescription_line",
        [LineString([(10, 5), (15, 5)])],
        ids=["TOUCH"],
    )
    result = _run([_inspected("prescription_line", frame)])
    assert result.relations.iloc[0]["relation_type"] == "TOUCH_ONLY"
    assert result.relations.iloc[0]["intersection_length_m"] == pytest.approx(0.0)
    assert result.parcels.iloc[0]["planning_line_touch_count"] == 1


@pytest.mark.parametrize(
    "geometry",
    [
        LineString([(-1, 5), (11, 5)]),
        MultiLineString([[(-1, 2), (11, 2)], [(-1, 8), (11, 8)]]),
    ],
)
def test_linestring_and_multilinestring(geometry: object) -> None:
    result = _run(
        [
            _inspected(
                "prescription_line", _source_frame("prescription_line", [geometry])
            )
        ]
    )
    assert result.relations.iloc[0]["intersection_length_m"] > 0


def test_points_inside_boundary_outside_and_multipoint() -> None:
    frame = _source_frame(
        "prescription_point",
        [
            Point(5, 5),
            Point(10, 5),
            Point(20, 20),
            MultiPoint([(3, 3), (10, 4), (30, 30)]),
        ],
        ids=["IN", "BOUNDARY", "OUT", "MULTI"],
        type_codes=["07"] * 4,
        subtype_codes=["00"] * 4,
    )
    result = _run([_inspected("prescription_point", frame)])
    relations = result.relations.set_index("source_feature_id")
    assert set(relations.index) == {"IN", "BOUNDARY", "MULTI"}
    assert relations.loc["IN", "relation_type"] == "INSIDE"
    assert relations.loc["BOUNDARY", "relation_type"] == "BOUNDARY_TOUCH"
    assert relations.loc["MULTI", "point_member_count"] == 3
    assert relations.loc["MULTI", "point_members_inside_count"] == 1
    assert relations.loc["MULTI", "point_members_boundary_count"] == 1
    parcel = result.parcels.iloc[0]
    assert parcel["planning_point_relation_count"] == 3
    assert parcel["planning_point_inside_count"] == 2
    assert parcel["planning_point_boundary_count"] == 2


def test_missing_optional_layer_families_return_stable_empty_catalogs() -> None:
    result = _run([])
    assert result.surface_features.empty
    assert result.line_features.empty
    assert result.point_features.empty
    assert result.relations.empty
    assert result.surface_features.crs.to_epsg() == 2154
    assert str(result.relations["point_member_count"].dtype) == "Int64"
    assert result.parcels.iloc[0]["planning_surface_relation_count"] == 0


def test_optional_raw_source_fields_are_not_fabricated() -> None:
    frame = _source_frame("prescription_line", [LineString([(0, 5), (10, 5)])]).drop(
        columns=["LIBELLE", "TXT", "NOMFIC", "URLFIC", "DATVALID"]
    )
    result = _run([_inspected("prescription_line", frame)])
    feature = result.line_features.iloc[0]
    for column in (
        "label_raw",
        "text_raw",
        "regulation_filename_raw",
        "regulation_url_raw",
        "source_validity_date_raw",
    ):
        assert pd.isna(feature[column])


def test_epsg4326_parcels_are_measured_in_lambert93_but_preserved() -> None:
    parcel = _parcels(crs="EPSG:4326")
    original = parcel.copy(deep=True)
    result = _run(
        [
            _inspected(
                "prescription_surface",
                _source_frame("prescription_surface", [_rectangle(0, 0, 10, 10)]),
            )
        ],
        parcel,
    )
    assert result.parcels.crs == original.crs
    assert np.array_equal(result.parcels.geometry.to_wkb(), original.geometry.to_wkb())
    assert result.relations.iloc[0]["intersection_area_m2"] == pytest.approx(100.0)


@pytest.mark.parametrize("bad_id", [None, "", "   ", " X", "X ", 7])
def test_invalid_parcel_ids_are_rejected(bad_id: object) -> None:
    with pytest.raises(PlanningFeaturesError, match="parcel_id"):
        _run([], _parcels(ids=[bad_id]))


def test_duplicate_parcel_ids_are_rejected() -> None:
    with pytest.raises(PlanningFeaturesError, match="unique"):
        _run(
            [],
            _parcels([_rectangle(0, 0, 2, 2), _rectangle(3, 3, 4, 4)], ids=["P", "P"]),
        )


def test_duplicate_source_ids_are_rejected() -> None:
    frame = _source_frame(
        "information_surface",
        [_rectangle(0, 0, 2, 2), _rectangle(3, 3, 4, 4)],
        ids=["SAME", "SAME"],
    )
    with pytest.raises(PlanningFeaturesError, match="unique"):
        _run([_inspected("information_surface", frame)])


def test_prescription_surface_uses_validated_source_ogr_fid_when_cnig_id_absent(
    tmp_path: Path,
) -> None:
    source_layer = "PRESCRIPTION_SURFACE"
    path = tmp_path / f"{source_layer}.shp"
    frame = _source_frame("prescription_surface", [_rectangle(0, 0, 10, 10)]).drop(
        columns="LIB_IDPSC"
    )
    frame.to_file(path, engine="pyogrio")
    loaded = gpd.read_file(path, engine="pyogrio")
    layer = _inspected("prescription_surface", loaded)
    reference = replace(
        layer.reference,
        dataset_path=path,
        source_layer=source_layer,
        driver="ESRI Shapefile",
    )
    layer = replace(
        layer,
        reference=reference,
        summary=_summary(loaded, source_layer),
    )
    result = _run([layer])
    assert result.surface_features.iloc[0]["source_feature_id"] == "OGR_FID:0"
    assert (
        result.surface_features.iloc[0]["source_identity_kind"]
        == "ARCHIVE_SCOPED_OGR_FID"
    )
    assert result.surface_features.iloc[0]["source_identity_field"] == "OGR_FID"
    assert result.surface_features.iloc[0]["planning_feature_id"] == (
        f"GPU:{DOCUMENT_ID}:prescription_surface:OGR_FID:0"
    )


def test_geopackage_prescription_surface_uses_sealed_ogr_fid_fallback() -> None:
    frame = _source_frame("prescription_surface", [_rectangle(0, 0, 10, 10)]).drop(
        columns="LIB_IDPSC"
    )
    result = _run([_inspected("prescription_surface", frame)])
    feature = result.surface_features.iloc[0]
    assert feature["source_feature_id"] == "OGR_FID:1"
    assert feature["source_identity_kind"] == "ARCHIVE_SCOPED_OGR_FID"
    assert feature["source_identity_field"] == "OGR_FID"
    assert feature["planning_feature_id"] == (
        f"GPU:{DOCUMENT_ID}:prescription_surface:OGR_FID:1"
    )


def test_idurba_mismatch_is_rejected() -> None:
    frame = _source_frame(
        "prescription_line", [LineString([(0, 5), (10, 5)])], document_refs=["OTHER"]
    )
    with pytest.raises(PlanningFeaturesError, match="IDURBA"):
        _run([_inspected("prescription_line", frame)])


@pytest.mark.parametrize("missing", ["TYPEPSC", "STYPEPSC", "IDURBA", "LIB_IDPSC"])
def test_missing_required_source_fields_fail(missing: str) -> None:
    frame = _source_frame("prescription_line", [LineString([(0, 5), (10, 5)])]).drop(
        columns=missing
    )
    with pytest.raises(PlanningFeaturesError, match=missing):
        _run([_inspected("prescription_line", frame)])


@pytest.mark.parametrize(
    ("logical", "geometry"),
    [
        ("prescription_surface", LineString([(0, 0), (1, 1)])),
        ("prescription_line", Point(1, 1)),
        ("prescription_point", LineString([(0, 0), (1, 1)])),
    ],
)
def test_wrong_geometry_kind_is_rejected(logical: str, geometry: object) -> None:
    with pytest.raises(PlanningFeaturesError, match="geometry"):
        _run([_inspected(logical, _source_frame(logical, [geometry]))])


def test_invalid_surface_geometry_is_rejected_without_repair() -> None:
    bowtie = Polygon([(0, 0), (2, 2), (2, 0), (0, 2), (0, 0)])
    with pytest.raises(PlanningFeaturesError, match="valid"):
        _run(
            [
                _inspected(
                    "information_surface",
                    _source_frame("information_surface", [bowtie]),
                )
            ]
        )


@pytest.mark.parametrize("geometry", [None, Polygon()])
def test_null_or_empty_source_geometry_is_rejected(geometry: object) -> None:
    frame = _source_frame("information_surface", [_rectangle(0, 0, 1, 1)])
    frame.geometry = [geometry]
    layer = _inspected("information_surface", frame)
    with pytest.raises(PlanningFeaturesError, match="geometry"):
        _run([layer])


@pytest.mark.parametrize("target", ["parcel", "source"])
def test_missing_crs_is_rejected(target: str) -> None:
    parcel = _parcels(crs=None) if target == "parcel" else _parcels()
    frame = _source_frame(
        "prescription_line",
        [LineString([(0, 5), (10, 5)])],
        crs=None if target == "source" else "EPSG:2154",
    )
    with pytest.raises(PlanningFeaturesError, match="CRS|physical revalidation"):
        _run([_inspected("prescription_line", frame)], parcel)


def test_unusable_source_crs_is_rejected() -> None:
    frame = _source_frame("prescription_line", [LineString([(0, 5), (10, 5)])]).set_crs(
        LOCAL_ENGINEERING_CRS, allow_override=True
    )
    with pytest.raises(PlanningFeaturesError, match="CRS"):
        _run([_inspected("prescription_line", frame)])


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("source_document_id", "other"),
        ("source_archive_sha256", "b" * 64),
        ("source_layer", "other"),
        ("feature_count", 99),
        ("geometry_types", (("Point", 1),)),
    ],
)
def test_mutated_source_summary_is_rejected(field: str, value: object) -> None:
    layer = _inspected(
        "prescription_line",
        _source_frame("prescription_line", [LineString([(0, 5), (10, 5)])]),
    )
    planning_document = _planning_document([layer])
    stored = planning_document.related_layers[0]
    corrupted = replace(stored, summary=replace(stored.summary, **{field: value}))
    changed = replace(planning_document, related_layers=(corrupted,))
    with pytest.raises(PlanningFeaturesError, match="summary|physical revalidation"):
        intersect_parcels_with_gpu_planning_features(_parcels(), changed)


@pytest.mark.parametrize("bad_count", [True, -1, 1.5, float("inf"), "1"])
def test_source_summary_counts_are_strict_integers(bad_count: object) -> None:
    layer = _inspected(
        "prescription_line",
        _source_frame("prescription_line", [LineString([(0, 5), (10, 5)])]),
    )
    planning_document = _planning_document([layer])
    stored = planning_document.related_layers[0]
    corrupted = replace(
        stored, summary=replace(stored.summary, feature_count=bad_count)
    )
    changed = replace(planning_document, related_layers=(corrupted,))
    with pytest.raises(
        PlanningFeaturesError,
        match="integer count|non-negative|summary|physical revalidation",
    ):
        intersect_parcels_with_gpu_planning_features(_parcels(), changed)


def test_reserved_output_column_collision_is_rejected() -> None:
    parcels = _parcels()
    parcels["planning_surface_relation_count"] = 99
    with pytest.raises(PlanningFeaturesError, match="output columns"):
        _run([], parcels)


def test_inputs_and_all_existing_parcel_fields_are_preserved() -> None:
    parcels = _parcels([_rectangle(0, 0, 10, 10), _rectangle(20, 20, 30, 30)])
    frame = _source_frame(
        "prescription_surface", [_rectangle(0, 0, 5, 10)], ids=["PSC"]
    )
    planning = _planning_document([_inspected("prescription_surface", frame)])
    parcels_before = parcels.copy(deep=True)
    zoning_before = planning.related_layers[0].data.copy(deep=True)
    result = intersect_parcels_with_gpu_planning_features(parcels, planning)
    assert_geodataframe_equal(parcels, parcels_before)
    assert_geodataframe_equal(planning.related_layers[0].data, zoning_before)
    assert result.parcels["parcel_id"].tolist() == parcels["parcel_id"].tolist()
    assert result.parcels.index.equals(parcels.index)
    assert result.parcels["existing_zoning_fact"].equals(
        parcels["existing_zoning_fact"]
    )
    assert np.array_equal(result.parcels.geometry.to_wkb(), parcels.geometry.to_wkb())


def test_relations_are_unique_deterministic_and_summaries_agree() -> None:
    parcels = _parcels(
        [_rectangle(0, 0, 10, 10), _rectangle(20, 20, 30, 30)], ids=["P-B", "P-A"]
    )
    surface = _inspected(
        "information_surface",
        _source_frame("information_surface", [_rectangle(-1, -1, 31, 31)], ids=["I"]),
    )
    line = _inspected(
        "prescription_line",
        _source_frame("prescription_line", [LineString([(-1, 5), (11, 5)])], ids=["L"]),
    )
    result = _run([surface, line], parcels)
    assert not result.relations.duplicated(["parcel_id", "planning_feature_id"]).any()
    assert result.relations["parcel_id"].tolist() == ["P-B", "P-B", "P-A"]
    first = result.parcels.iloc[0]
    assert first["planning_surface_relation_count"] == int(
        (
            (result.relations["parcel_id"] == "P-B")
            & (result.relations["geometry_kind"] == "SURFACE")
        ).sum()
    )
    assert first["planning_line_intersection_length_sum_m"] == pytest.approx(
        result.relations.loc[
            (result.relations["parcel_id"] == "P-B")
            & (result.relations["geometry_kind"] == "LINE"),
            "intersection_length_m",
        ].sum()
    )


def test_result_frames_are_independent_from_mutable_inputs() -> None:
    parcels = _parcels()
    layer = _inspected(
        "prescription_line",
        _source_frame("prescription_line", [LineString([(0, 5), (10, 5)])]),
    )
    result = _run([layer], parcels)
    snapshot = deepcopy(result.relations)
    parcels.loc[50, "existing_zoning_fact"] = -1
    layer.data.loc[0, "LIBELLE"] = "mutated"
    assert_frame_equal(result.relations, snapshot)


@pytest.mark.parametrize(
    ("logical", "catalog_name"),
    [
        ("prescription_surface", "surface_features"),
        ("prescription_line", "line_features"),
        ("prescription_point", "point_features"),
    ],
)
def test_present_empty_optional_layer_is_valid(
    logical: str,
    catalog_name: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    frame = _source_frame(logical, [])
    fid_reads = 0
    if logical == "prescription_surface":
        frame = frame.drop(columns="LIB_IDPSC")
        real_read_dataframe = gpu_source_module.pyogrio.read_dataframe

        def unexpected_fid_read(*args: object, **kwargs: object) -> object:
            nonlocal fid_reads
            if kwargs.get("fid_as_index"):
                fid_reads += 1
            return real_read_dataframe(*args, **kwargs)

        monkeypatch.setattr(
            gpu_source_module.pyogrio,
            "read_dataframe",
            unexpected_fid_read,
        )
    result = _run([_inspected(logical, frame)])
    catalog = getattr(result, catalog_name)
    assert catalog.empty
    assert catalog.crs.to_epsg() == 2154
    assert result.relations.empty
    assert len(result.parcels) == 1
    assert result.parcels.iloc[0]["planning_feature_document_id"] == DOCUMENT_ID
    if logical == "prescription_surface":
        assert fid_reads == 1


def _contract_result() -> tuple[
    GpuPlanningDocument,
    gpd.GeoDataFrame,
    ParcelPlanningFeaturesResult,
]:
    parcels = _parcels()
    layers = [
        _inspected(
            "prescription_surface",
            _source_frame(
                "prescription_surface",
                [_rectangle(0, 0, 10, 10)],
                ids=["SURFACE"],
            ),
        ),
        _inspected(
            "prescription_line",
            _source_frame(
                "prescription_line",
                [LineString([(-1, 5), (11, 5)])],
                ids=["LINE"],
            ),
        ),
        _inspected(
            "prescription_point",
            _source_frame("prescription_point", [Point(5, 5)], ids=["POINT"]),
        ),
    ]
    planning_document = _planning_document(layers)
    return (
        planning_document,
        parcels,
        intersect_parcels_with_gpu_planning_features(parcels, planning_document),
    )


def _source_complete_contract() -> tuple[
    GpuPlanningDocument,
    gpd.GeoDataFrame,
    ParcelPlanningFeaturesResult,
]:
    parcels = _parcels()
    layers = [
        _inspected(
            "prescription_surface",
            _source_frame(
                "prescription_surface",
                [_rectangle(0, 0, 10, 10)],
                ids=["SURFACE"],
                type_codes=["07"],
                subtype_codes=["04"],
            ),
        ),
        _inspected(
            "prescription_line",
            _source_frame(
                "prescription_line",
                [LineString([(-1, 5), (11, 5)])],
                ids=["LINE"],
                type_codes=["15"],
                subtype_codes=["00"],
            ),
        ),
        _inspected(
            "prescription_point",
            _source_frame(
                "prescription_point",
                [Point(5, 5)],
                ids=["POINT"],
                type_codes=["07"],
                subtype_codes=["00"],
            ),
        ),
    ]
    planning_document = _planning_document(layers)
    result = intersect_parcels_with_gpu_planning_features(parcels, planning_document)
    return planning_document, parcels, result


def _two_parcel_source_complete_contract() -> tuple[
    GpuPlanningDocument,
    gpd.GeoDataFrame,
    ParcelPlanningFeaturesResult,
]:
    """Build equal-area parcels so relation identity cannot hide behind area checks."""

    parcels = _parcels(
        [_rectangle(0, 0, 10, 10), _rectangle(20, 0, 30, 10)],
        ids=["P-1", "P-2"],
    )
    layers = [
        _inspected(
            "prescription_surface",
            _source_frame(
                "prescription_surface",
                [_rectangle(0, 0, 10, 10)],
                ids=["SURFACE"],
                type_codes=["07"],
                subtype_codes=["04"],
            ),
        ),
        _inspected(
            "prescription_line",
            _source_frame(
                "prescription_line",
                [LineString([(0, 5), (10, 5)])],
                ids=["LINE"],
                type_codes=["15"],
                subtype_codes=["00"],
            ),
        ),
    ]
    planning_document = _planning_document(layers)
    result = intersect_parcels_with_gpu_planning_features(parcels, planning_document)
    return planning_document, parcels, result


def _validate_source_complete(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    result: ParcelPlanningFeaturesResult,
) -> PlanningFeatureInputValidation:
    return validate_normalized_planning_feature_inputs(
        planning_document,
        parcels,
        result.surface_features,
        result.line_features,
        result.point_features,
        result.relations,
    )


def _replace_related_layer(
    planning_document: GpuPlanningDocument,
    logical_name: str,
    frame: gpd.GeoDataFrame,
) -> GpuPlanningDocument:
    related: list[GpuInspectedLayer] = []
    for layer in planning_document.related_layers:
        if layer.logical_name != logical_name:
            related.append(layer)
            continue
        related.append(
            replace(
                layer,
                data=frame,
                summary=_summary(frame, layer.reference.source_layer),
            )
        )
    return replace(planning_document, related_layers=tuple(related))


def _without_related_layer(
    planning_document: GpuPlanningDocument,
    logical_name: str,
) -> GpuPlanningDocument:
    return replace(
        planning_document,
        related_layers=tuple(
            layer
            for layer in planning_document.related_layers
            if layer.logical_name != logical_name
        ),
    )


def _refresh_extraction_inventory(
    planning_document: GpuPlanningDocument,
) -> GpuPlanningDocument:
    extraction = planning_document.extraction
    files = _physical_inventory(extraction.extraction_root)
    _write_extraction_manifest(
        extraction.extraction_root,
        extraction.archive.sha256,
        files,
    )
    updated_extraction = replace(extraction, files=files)
    return replace(
        planning_document,
        extraction=updated_extraction,
        all_spatial_layers=gpu_source_module.discover_gpu_spatial_layers(
            updated_extraction
        ),
    )


def _replace_layer_reference(
    planning_document: GpuPlanningDocument,
    logical_name: str,
    reference: GpuSpatialLayerReference,
) -> GpuPlanningDocument:
    related = tuple(
        replace(layer, reference=reference)
        if layer.logical_name == logical_name
        else layer
        for layer in planning_document.related_layers
    )
    old_reference = next(
        layer.reference
        for layer in planning_document.related_layers
        if layer.logical_name == logical_name
    )
    spatial = tuple(
        reference if item == old_reference else item
        for item in planning_document.all_spatial_layers
    )
    return replace(
        planning_document,
        related_layers=related,
        all_spatial_layers=spatial,
    )


def test_public_normalized_input_contract_validates_step_7d_3_1_result() -> None:
    planning_document, parcels, result = _source_complete_contract()
    validation = validate_normalized_planning_feature_inputs(
        planning_document,
        parcels,
        result.surface_features,
        result.line_features,
        result.point_features,
        result.relations,
    )
    assert isinstance(validation, PlanningFeatureInputValidation)
    assert validation.related_source_layer_count == 3
    assert validation.related_source_file_count == 3
    assert validation.expected_relation_count == len(result.relations)
    for value in (
        validation.gpu_related_source_files_sha256,
        validation.expected_relations_content_sha256,
    ):
        assert len(value) == 64
        int(value, 16)


def test_public_normalized_input_contract_wraps_malformed_document_context() -> None:
    planning_document, parcels, result = _source_complete_contract()
    malformed = replace(planning_document, related_layers=(None,))  # type: ignore[arg-type]
    with pytest.raises(PlanningFeaturesError) as caught:
        _validate_source_complete(malformed, parcels, result)
    assert isinstance(caught.value.__cause__, (AttributeError, TypeError))


def test_source_complete_contract_binds_inspected_spatial_inventory() -> None:
    planning_document, parcels, result = _source_complete_contract()
    missing_inventory = replace(planning_document, all_spatial_layers=())
    with pytest.raises(PlanningFeaturesError, match="inventory|reference"):
        _validate_source_complete(missing_inventory, parcels, result)


def test_public_normalized_input_contract_is_exported() -> None:
    from landscout import stages

    assert (
        stages.validate_normalized_planning_feature_inputs
        is validate_normalized_planning_feature_inputs
    )
    assert "validate_normalized_planning_feature_inputs" in stages.__all__
    assert stages.PlanningFeatureInputValidation is PlanningFeatureInputValidation
    assert "PlanningFeatureInputValidation" in stages.__all__


def test_public_source_validation_hashes_survive_parquet_readback(
    tmp_path: Path,
) -> None:
    planning_document, parcels, result = _source_complete_contract()
    original = _validate_source_complete(planning_document, parcels, result)
    paths = {
        "surface_features": tmp_path / "surface.parquet",
        "line_features": tmp_path / "line.parquet",
        "point_features": tmp_path / "point.parquet",
        "relations": tmp_path / "relations.parquet",
    }
    result.surface_features.to_parquet(paths["surface_features"], index=False)
    result.line_features.to_parquet(paths["line_features"], index=False)
    result.point_features.to_parquet(paths["point_features"], index=False)
    result.relations.to_parquet(paths["relations"], index=False)
    validation = validate_normalized_planning_feature_inputs(
        planning_document,
        parcels,
        gpd.read_parquet(paths["surface_features"]),
        gpd.read_parquet(paths["line_features"]),
        gpd.read_parquet(paths["point_features"]),
        pd.read_parquet(paths["relations"]),
    )
    assert validation == original


def test_public_normalized_input_contract_rejects_stripped_catalog() -> None:
    planning_document, parcels, result = _source_complete_contract()
    surface = result.surface_features.drop(columns="label_raw")
    with pytest.raises(PlanningFeaturesError, match="schema|label_raw"):
        validate_normalized_planning_feature_inputs(
            planning_document,
            parcels,
            surface,
            result.line_features,
            result.point_features,
            result.relations,
        )


def test_empty_and_nonempty_catalogs_have_identical_kind_schemas() -> None:
    _, _, populated = _contract_result()
    empty = _run([])
    for populated_catalog, empty_catalog in zip(
        (
            populated.surface_features,
            populated.line_features,
            populated.point_features,
        ),
        (empty.surface_features, empty.line_features, empty.point_features),
        strict=True,
    ):
        assert list(empty_catalog.columns) == list(populated_catalog.columns)


@pytest.mark.parametrize("bad_count", [-1, 1.5, float("inf"), "2", True])
def test_strict_relation_integer_counts_are_enforced(bad_count: object) -> None:
    planning_document, source, result = _contract_result()
    relations = result.relations.copy(deep=True)
    relations["point_member_count"] = relations["point_member_count"].astype(object)
    point_index = relations.index[relations["geometry_kind"] == "POINT"][0]
    relations.loc[point_index, "point_member_count"] = bad_count
    with pytest.raises(
        PlanningFeaturesError, match="integer count|non-negative|dtype|schema"
    ):
        _validate_result(
            source,
            replace(result, relations=relations),
            planning_document=planning_document,
        )


@pytest.mark.parametrize("bad_count", [-1, 1.5, float("inf"), "2", True])
def test_strict_parcel_summary_integer_counts_are_enforced(
    bad_count: object,
) -> None:
    planning_document, source, result = _contract_result()
    parcels = result.parcels.copy(deep=True)
    parcels["planning_line_relation_count"] = parcels[
        "planning_line_relation_count"
    ].astype(object)
    parcels.loc[parcels.index[0], "planning_line_relation_count"] = bad_count
    with pytest.raises(PlanningFeaturesError, match="integer count|non-negative"):
        _validate_result(
            source,
            replace(result, parcels=parcels),
            planning_document=planning_document,
        )


@pytest.mark.parametrize(
    ("kind", "column", "value"),
    [
        ("SURFACE", "relation_type", "TOUCH_ONLY"),
        ("SURFACE", "parcel_share_pct", 42.0),
        ("SURFACE", "intersection_area_m2", None),
        ("SURFACE", "source_line_length_m", 0.0),
        ("LINE", "relation_type", "TOUCH_ONLY"),
        ("LINE", "intersection_length_m", 999.0),
        ("POINT", "relation_type", "BOUNDARY_TOUCH"),
    ],
)
def test_corrupted_relation_semantics_are_rejected(
    kind: str,
    column: str,
    value: object,
) -> None:
    planning_document, source, result = _contract_result()
    relations = result.relations.copy(deep=True)
    index = relations.index[relations["geometry_kind"] == kind][0]
    relations[column] = relations[column].astype(object)
    relations.loc[index, column] = value
    with pytest.raises(PlanningFeaturesError):
        _validate_result(
            source,
            replace(result, relations=relations),
            planning_document=planning_document,
        )


def test_point_member_relation_semantics_are_exact() -> None:
    planning_document, source, result = _contract_result()
    relations = result.relations.copy(deep=True)
    index = relations.index[relations["geometry_kind"] == "POINT"][0]
    relations.loc[index, "point_members_inside_count"] = 0
    relations.loc[index, "point_members_boundary_count"] = 1
    with pytest.raises(PlanningFeaturesError, match="relation type"):
        _validate_result(
            source,
            replace(result, relations=relations),
            planning_document=planning_document,
        )


@pytest.mark.parametrize(
    "case",
    [
        "surface-inside",
        "line-area",
        "point-touch",
        "area-zero",
        "surface-touch-positive",
        "length-zero",
        "line-touch-positive",
        "inside-zero",
        "boundary-with-inside",
        "area-exceeds-feature",
        "share-inconsistent",
        "non-finite",
        "negative",
    ],
)
def test_shared_intrinsic_relation_semantics_reject_every_invalid_case(
    case: str,
) -> None:
    _, _, result = _contract_result()
    relations = result.relations.copy(deep=True)
    surface = relations.index[relations["geometry_kind"].eq("SURFACE")][0]
    line = relations.index[relations["geometry_kind"].eq("LINE")][0]
    point = relations.index[relations["geometry_kind"].eq("POINT")][0]
    if case == "surface-inside":
        relations.loc[surface, "relation_type"] = "INSIDE"
    elif case == "line-area":
        relations.loc[line, "relation_type"] = "AREA_OVERLAP"
    elif case == "point-touch":
        relations.loc[point, "relation_type"] = "TOUCH_ONLY"
    elif case == "area-zero":
        relations.loc[
            surface, ["intersection_area_m2", "parcel_share_pct", "feature_share_pct"]
        ] = 0.0
    elif case == "surface-touch-positive":
        relations.loc[surface, "relation_type"] = "TOUCH_ONLY"
    elif case == "length-zero":
        relations.loc[line, "intersection_length_m"] = 0.0
    elif case == "line-touch-positive":
        relations.loc[line, "relation_type"] = "TOUCH_ONLY"
    elif case == "inside-zero":
        relations.loc[point, "point_members_inside_count"] = 0
    elif case == "boundary-with-inside":
        relations.loc[point, "relation_type"] = "BOUNDARY_TOUCH"
        relations.loc[point, "point_members_boundary_count"] = 1
    elif case == "area-exceeds-feature":
        relations.loc[surface, "intersection_area_m2"] = (
            float(relations.loc[surface, "feature_area_m2"]) + 1.0
        )
    elif case == "share-inconsistent":
        relations.loc[surface, "parcel_share_pct"] = 42.0
    elif case == "non-finite":
        relations.loc[surface, "feature_share_pct"] = float("inf")
    else:
        relations.loc[surface, "intersection_area_m2"] = -1.0
    with pytest.raises((TypeError, ValueError)):
        validate_intrinsic_planning_feature_relations(relations)


@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("source_identity_kind", "NOT_A_KIND"),
        ("source_identity_field", "WRONG_FIELD"),
        ("feature_family", "INFORMATION"),
        ("geometry_kind", "LINE"),
        ("type_code_raw", "MUTATED"),
        ("source_archive_sha256", "b" * 64),
    ],
)
def test_relation_must_match_feature_catalog(
    column: str,
    value: object,
) -> None:
    planning_document, source, result = _contract_result()
    relations = result.relations.copy(deep=True)
    index = relations.index[0]
    if column == "geometry_kind":
        index = relations.index[relations["geometry_kind"].eq("SURFACE")][0]
    relations.loc[index, column] = value
    with pytest.raises(
        PlanningFeaturesError,
        match="catalog|geometry kind|LINE relation|unrelated metric",
    ):
        _validate_result(
            source,
            replace(result, relations=relations),
            planning_document=planning_document,
        )


def test_feature_ids_are_globally_unique_across_catalogs() -> None:
    planning_document, source, result = _contract_result()
    points = result.point_features.copy(deep=True)
    points.loc[points.index[0], "planning_feature_id"] = result.surface_features.iloc[
        0
    ]["planning_feature_id"]
    with pytest.raises(PlanningFeaturesError, match="globally unique|deterministic"):
        _validate_result(
            source,
            replace(result, point_features=points),
            planning_document=planning_document,
        )


def test_same_source_id_is_allowed_in_distinct_logical_layers() -> None:
    result = _run(
        [
            _inspected(
                "prescription_line",
                _source_frame(
                    "prescription_line",
                    [LineString([(0, 2), (10, 2)])],
                    ids=["SHARED"],
                ),
            ),
            _inspected(
                "prescription_point",
                _source_frame("prescription_point", [Point(5, 5)], ids=["SHARED"]),
            ),
        ]
    )
    assert len(result.relations) == 2
    assert result.relations["planning_feature_id"].nunique() == 2


def test_corrupted_parcel_summary_is_rejected() -> None:
    planning_document, source, result = _contract_result()
    parcels = result.parcels.copy(deep=True)
    parcels.loc[parcels.index[0], "planning_surface_relation_count"] += 1
    with pytest.raises(PlanningFeaturesError, match="inconsistent with relations"):
        _validate_result(
            source,
            replace(result, parcels=parcels),
            planning_document=planning_document,
        )


def test_corrupted_surface_union_contract_is_rejected() -> None:
    planning_document, source, result = _contract_result()
    parcels = result.parcels.copy(deep=True)
    parcels.loc[parcels.index[0], "planning_surface_covered_union_area_m2"] = 1000.0
    with pytest.raises(PlanningFeaturesError, match="union"):
        _validate_result(
            source,
            replace(result, parcels=parcels),
            planning_document=planning_document,
        )


def test_geospatial_operation_failure_is_controlled_and_chained(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def fail_join(*args: object, **kwargs: object) -> object:
        raise RuntimeError("synthetic spatial-index failure")

    monkeypatch.setattr(planning_features_module.gpd, "sjoin", fail_join)
    layer = _inspected(
        "prescription_line",
        _source_frame("prescription_line", [LineString([(0, 5), (10, 5)])]),
    )
    with pytest.raises(PlanningFeaturesError, match="spatial join") as caught:
        _run([layer])
    assert isinstance(caught.value.__cause__, RuntimeError)


def test_source_complete_contract_rejects_unknown_relation_parcel() -> None:
    planning_document, parcels, result = _source_complete_contract()
    relations = result.relations.copy(deep=True)
    relations.loc[relations.index[0], "parcel_id"] = "NOT-A-SOURCE-PARCEL"
    corrupted = replace(result, relations=relations)
    with pytest.raises(PlanningFeaturesError, match="parcel|source"):
        _validate_source_complete(planning_document, parcels, corrupted)


def test_source_complete_contract_rejects_coherent_parcel_metric_mutation() -> None:
    planning_document, parcels, result = _source_complete_contract()
    relations = result.relations.copy(deep=True)
    surface_mask = relations["geometry_kind"].eq("SURFACE")
    relations.loc[surface_mask, "parcel_metric_area_m2"] = 200.0
    relations.loc[surface_mask, "parcel_share_pct"] = 50.0
    corrupted = replace(result, relations=relations)
    with pytest.raises(PlanningFeaturesError, match="parcel|metric|source"):
        _validate_source_complete(planning_document, parcels, corrupted)


def test_source_complete_contract_rejects_same_area_wrong_parcel_relation() -> None:
    planning_document, parcels, result = _two_parcel_source_complete_contract()
    relations = result.relations.copy(deep=True)
    relations.loc[relations.index[0], "parcel_id"] = "P-2"
    corrupted = replace(result, relations=relations)
    with pytest.raises(PlanningFeaturesError, match="relation|parcel|rebuilt|source"):
        _validate_source_complete(planning_document, parcels, corrupted)


def test_source_complete_contract_rejects_missing_expected_relation() -> None:
    planning_document, parcels, result = _two_parcel_source_complete_contract()
    corrupted = replace(result, relations=result.relations.iloc[1:].copy())
    with pytest.raises(PlanningFeaturesError, match="relation|rebuilt|source"):
        _validate_source_complete(planning_document, parcels, corrupted)


def test_source_complete_contract_rejects_extra_geometrically_false_relation() -> None:
    planning_document, parcels, result = _two_parcel_source_complete_contract()
    extra = result.relations.iloc[[0]].copy(deep=True)
    extra.loc[extra.index[0], "parcel_id"] = "P-2"
    relations = pd.concat([result.relations, extra], ignore_index=True)
    corrupted = replace(result, relations=relations)
    with pytest.raises(PlanningFeaturesError, match="relation|rebuilt|source"):
        _validate_source_complete(planning_document, parcels, corrupted)


def test_source_complete_contract_rejects_reordered_relations() -> None:
    planning_document, parcels, result = _two_parcel_source_complete_contract()
    relations = result.relations.iloc[::-1].reset_index(drop=True)
    corrupted = replace(result, relations=relations)
    with pytest.raises(PlanningFeaturesError, match="relation|order|rebuilt"):
        _validate_source_complete(planning_document, parcels, corrupted)


@pytest.mark.parametrize(
    ("column", "dtype"),
    [
        ("intersection_area_m2", "object"),
        ("point_member_count", "object"),
        ("relation_type", "category"),
    ],
)
def test_source_complete_contract_rejects_noncanonical_relation_dtype(
    column: str,
    dtype: str,
) -> None:
    planning_document, parcels, result = _source_complete_contract()
    relations = result.relations.copy(deep=True)
    relations[column] = relations[column].astype(dtype)
    with pytest.raises(PlanningFeaturesError, match="schema|dtype|relation"):
        _validate_source_complete(
            planning_document, parcels, replace(result, relations=relations)
        )


def test_source_complete_contract_rejects_relation_index_name_change() -> None:
    planning_document, parcels, result = _source_complete_contract()
    relations = result.relations.copy(deep=True)
    relations.index = relations.index.rename("changed_relation_row")
    with pytest.raises(PlanningFeaturesError, match="schema|index|relation"):
        _validate_source_complete(
            planning_document, parcels, replace(result, relations=relations)
        )


def test_source_complete_contract_rejects_relation_index_dtype_change() -> None:
    planning_document, parcels, result = _source_complete_contract()
    relations = result.relations.copy(deep=True)
    relations.index = pd.Index(
        np.asarray(relations.index, dtype="int32"),
        name=relations.index.name,
    )
    assert str(relations.index.dtype) == "int32"
    with pytest.raises(PlanningFeaturesError, match="schema|index|relation"):
        _validate_source_complete(
            planning_document, parcels, replace(result, relations=relations)
        )


def test_source_complete_contract_rejects_relation_index_class_change() -> None:
    planning_document, parcels, result = _source_complete_contract()
    assert type(result.relations.index) is pd.RangeIndex
    relations = result.relations.copy(deep=True)
    relations.index = pd.Index(relations.index.to_numpy(), dtype="int64")
    assert type(relations.index) is pd.Index
    with pytest.raises(PlanningFeaturesError, match="schema|index|relation"):
        validate_normalized_planning_feature_inputs(
            planning_document,
            parcels,
            result.surface_features,
            result.line_features,
            result.point_features,
            relations,
        )


def test_expected_relation_hash_binds_dtype_and_index_metadata() -> None:
    _, _, result = _source_complete_contract()
    original = planning_features_module._expected_relations_content_sha256(
        result.relations
    )
    object_dtype = result.relations.copy(deep=True)
    object_dtype["intersection_area_m2"] = object_dtype["intersection_area_m2"].astype(
        "object"
    )
    named_index = result.relations.copy(deep=True)
    named_index.index = named_index.index.rename("relation_row")
    int32_index = result.relations.copy(deep=True)
    int32_index.index = pd.Index(
        np.asarray(int32_index.index, dtype="int32"),
        name=int32_index.index.name,
    )
    index_class = result.relations.copy(deep=True)
    index_class.index = pd.Index(index_class.index.to_numpy(), dtype="int64")
    assert original != planning_features_module._expected_relations_content_sha256(
        object_dtype
    )
    assert original != planning_features_module._expected_relations_content_sha256(
        named_index
    )
    assert original != planning_features_module._expected_relations_content_sha256(
        int32_index
    )
    assert original != planning_features_module._expected_relations_content_sha256(
        index_class
    )


def test_source_complete_contract_rejects_coherent_but_wrong_line_metric() -> None:
    planning_document, parcels, result = _two_parcel_source_complete_contract()
    relations = result.relations.copy(deep=True)
    line_mask = relations["geometry_kind"].eq("LINE")
    relations.loc[line_mask, "intersection_length_m"] = 5.0
    corrupted = replace(result, relations=relations)
    with pytest.raises(PlanningFeaturesError, match="relation|metric|rebuilt"):
        _validate_source_complete(planning_document, parcels, corrupted)


def test_source_complete_contract_accepts_complete_parcel_output_summaries() -> None:
    planning_document, _, result = _source_complete_contract()
    _validate_source_complete(planning_document, result.parcels, result)


def test_source_complete_contract_rejects_partial_parcel_output_columns() -> None:
    planning_document, parcels, result = _source_complete_contract()
    partial = parcels.copy(deep=True)
    partial["planning_surface_relation_count"] = 1
    with pytest.raises(PlanningFeaturesError, match="[Pp]arcel|output|summary|columns"):
        _validate_source_complete(planning_document, partial, result)


def test_source_complete_contract_rejects_corrupted_complete_parcel_summaries() -> None:
    planning_document, _, result = _source_complete_contract()
    corrupted = result.parcels.copy(deep=True)
    corrupted.loc[corrupted.index[0], "planning_surface_relation_count"] += 1
    with pytest.raises(PlanningFeaturesError, match="parcel|summary|relation"):
        _validate_source_complete(planning_document, corrupted, result)


def test_source_complete_contract_rejects_noncanonical_parcel_summary_dtype() -> None:
    planning_document, _, result = _source_complete_contract()
    corrupted = result.parcels.copy(deep=True)
    corrupted["planning_surface_covered_pct"] = corrupted[
        "planning_surface_covered_pct"
    ].astype("float32")
    with pytest.raises(PlanningFeaturesError, match="parcel|schema|dtype|summary"):
        _validate_source_complete(planning_document, corrupted, result)


@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("planning_feature_document_id", "other-document"),
        ("planning_feature_archive_sha256", "f" * 64),
        ("planning_surface_covered_union_area_m2", 50.0),
        ("planning_surface_covered_pct", 50.0),
        ("planning_line_intersection_length_sum_m", 5.0),
        ("planning_point_inside_count", 0),
    ],
)
def test_source_complete_contract_rejects_each_corrupted_parcel_summary_fact(
    column: str,
    value: object,
) -> None:
    planning_document, _, result = _source_complete_contract()
    corrupted = result.parcels.copy(deep=True)
    corrupted.loc[corrupted.index[0], column] = value
    with pytest.raises(
        PlanningFeaturesError,
        match="parcel|summary|relation|lineage|document|archive|union|percentage",
    ):
        _validate_source_complete(planning_document, corrupted, result)


def test_source_complete_contract_rejects_duplicate_parcel_ids() -> None:
    planning_document, parcels, result = _source_complete_contract()
    duplicate = pd.concat([parcels, parcels], ignore_index=True)
    duplicate = gpd.GeoDataFrame(duplicate, geometry="geometry", crs=parcels.crs)
    with pytest.raises(PlanningFeaturesError, match="parcel_id|unique"):
        _validate_source_complete(planning_document, duplicate, result)


def test_source_complete_contract_rejects_invalid_parcel_geometry() -> None:
    planning_document, parcels, result = _source_complete_contract()
    invalid = parcels.copy(deep=True)
    invalid.at[invalid.index[0], "geometry"] = Polygon(
        [(0, 0), (10, 10), (10, 0), (0, 10), (0, 0)]
    )
    with pytest.raises(PlanningFeaturesError, match="valid|geometry"):
        _validate_source_complete(planning_document, invalid, result)


def test_source_complete_contract_accepts_epsg4326_parcels() -> None:
    planning_document, parcels, _ = _source_complete_contract()
    geographic = parcels.to_crs("EPSG:4326")
    result = intersect_parcels_with_gpu_planning_features(geographic, planning_document)
    _validate_source_complete(planning_document, geographic, result)


def test_source_document_reference_allows_one_archive_zip_suffix() -> None:
    planning_document, parcels, _ = _source_complete_contract()
    archive = planning_document.extraction.archive
    metadata = replace(archive.document, archive_name=f"{ARCHIVE_NAME}.zip")
    suffixed = replace(
        planning_document,
        extraction=replace(
            planning_document.extraction,
            archive=replace(archive, document=metadata),
        ),
    )
    result = intersect_parcels_with_gpu_planning_features(parcels, suffixed)
    assert (
        result.surface_features["source_archive_name"].eq(f"{ARCHIVE_NAME}.zip").all()
    )
    assert (
        result.surface_features["source_document_reference_raw"].eq(ARCHIVE_NAME).all()
    )
    _validate_source_complete(suffixed, parcels, result)


@pytest.mark.parametrize(
    "identity_column", ["planning_feature_id", "source_feature_id"]
)
def test_source_complete_contract_rejects_coherently_renamed_feature_identity(
    identity_column: str,
) -> None:
    planning_document, parcels, result = _source_complete_contract()
    surface = result.surface_features.copy(deep=True)
    relations = result.relations.copy(deep=True)
    old = surface.iloc[0][identity_column]
    new = (
        f"GPU:{DOCUMENT_ID}:prescription_surface:RENAMED"
        if identity_column == "planning_feature_id"
        else "RENAMED"
    )
    surface.loc[surface.index[0], identity_column] = new
    relations.loc[relations[identity_column].eq(old), identity_column] = new
    corrupted = replace(result, surface_features=surface, relations=relations)
    with pytest.raises(PlanningFeaturesError, match="source|identity|rebuilt|catalog"):
        _validate_source_complete(planning_document, parcels, corrupted)


@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("source_provider", "Another provider"),
        ("source_portal", "https://example.invalid"),
        ("source_commune_code", "99999"),
        ("source_document_type", "CC"),
        ("source_archive_name", "OTHER_ARCHIVE"),
        ("source_document_reference_raw", "OTHER_ARCHIVE"),
        ("source_layer", "OTHER_SOURCE_LAYER"),
        ("source_crs", "EPSG:4326"),
    ],
)
def test_source_complete_contract_rejects_independent_gpu_lineage_mutation(
    column: str,
    value: str,
) -> None:
    planning_document, parcels, result = _source_complete_contract()
    surface = result.surface_features.copy(deep=True)
    relations = result.relations.copy(deep=True)
    surface.loc[surface.index[0], column] = value
    if column in relations.columns:
        feature_id = result.surface_features.iloc[0]["planning_feature_id"]
        relations.loc[relations["planning_feature_id"].eq(feature_id), column] = value
    corrupted = replace(result, surface_features=surface, relations=relations)
    with pytest.raises(PlanningFeaturesError, match="source|lineage|catalog|rebuilt"):
        _validate_source_complete(planning_document, parcels, corrupted)


@pytest.mark.parametrize(
    ("metadata_field", "value"),
    [
        ("provider", "Another provider"),
        ("portal", "https://example.invalid"),
        ("commune_code", "99999"),
        ("document_type", "CC"),
        ("archive_name", "OTHER_ARCHIVE"),
    ],
)
def test_source_complete_contract_binds_gpu_document_context(
    metadata_field: str,
    value: str,
) -> None:
    planning_document, parcels, result = _source_complete_contract()
    archive = planning_document.extraction.archive
    metadata = replace(archive.document, **{metadata_field: value})
    changed = replace(
        planning_document,
        extraction=replace(
            planning_document.extraction,
            archive=replace(archive, document=metadata),
        ),
    )
    with pytest.raises(
        PlanningFeaturesError,
        match="source|lineage|document|rebuilt|IDURBA|archive",
    ):
        _validate_source_complete(changed, parcels, result)


@pytest.mark.parametrize("mutation", ["geometry", "raw", "code", "remove", "extra"])
def test_source_complete_contract_reloads_and_compares_source_catalog(
    mutation: str,
) -> None:
    planning_document, parcels, result = _source_complete_contract()
    layer = next(
        layer
        for layer in planning_document.related_layers
        if layer.logical_name == "prescription_surface"
    )
    frame = layer.data.copy(deep=True)
    if mutation == "geometry":
        frame.at[frame.index[0], "geometry"] = _rectangle(0, 0, 5, 10)
    elif mutation == "raw":
        frame.loc[frame.index[0], "LIBELLE"] = "Changed source label"
    elif mutation == "code":
        frame.loc[frame.index[0], ["TYPEPSC", "STYPEPSC"]] = ["01", "00"]
    elif mutation == "remove":
        frame = frame.iloc[0:0].copy()
    else:
        extra = frame.copy(deep=True)
        extra.loc[extra.index[0], "LIB_IDPSC"] = "EXTRA"
        extra.at[extra.index[0], "geometry"] = _rectangle(20, 20, 21, 21)
        frame = gpd.GeoDataFrame(
            pd.concat([frame, extra], ignore_index=True),
            geometry="geometry",
            crs=frame.crs,
        )
    changed = _replace_related_layer(planning_document, "prescription_surface", frame)
    with pytest.raises(
        PlanningFeaturesError, match="source|catalog|rebuilt|normalized"
    ):
        _validate_source_complete(changed, parcels, result)


def test_source_complete_contract_rejects_catalog_for_absent_gpu_layer() -> None:
    planning_document, parcels, result = _source_complete_contract()
    changed = _without_related_layer(planning_document, "prescription_surface")
    with pytest.raises(PlanningFeaturesError, match="source|layer|catalog|rebuilt"):
        _validate_source_complete(changed, parcels, result)


@pytest.mark.parametrize(
    ("catalog_name", "geometry"),
    [
        (
            "surface_features",
            Polygon([(0, 0, 1), (0, 10, 1), (10, 10, 1), (10, 0, 1)]),
        ),
        ("line_features", LineString([(-1, 5, 1), (11, 5, 1)])),
        ("point_features", Point(5, 5, 1)),
    ],
)
def test_three_dimensional_normalized_catalogs_are_rejected(
    catalog_name: str,
    geometry: object,
) -> None:
    planning_document, parcels, result = _source_complete_contract()
    catalog = getattr(result, catalog_name).copy(deep=True)
    catalog.at[catalog.index[0], "geometry"] = geometry
    corrupted = replace(result, **{catalog_name: catalog})
    with pytest.raises(PlanningFeaturesError, match="2D|dimensional|Z"):
        _validate_source_complete(planning_document, parcels, corrupted)


def test_two_dimensional_normalized_catalogs_remain_valid() -> None:
    planning_document, parcels, result = _source_complete_contract()
    for catalog in (
        result.surface_features,
        result.line_features,
        result.point_features,
    ):
        assert not catalog.geometry.has_z.any()
    _validate_source_complete(planning_document, parcels, result)


@pytest.mark.parametrize(
    ("logical", "geometry", "catalog_name"),
    [
        (
            "prescription_surface",
            Polygon([(0, 0, 1), (0, 10, 1), (10, 10, 1), (10, 0, 1)]),
            "surface_features",
        ),
        (
            "prescription_line",
            LineString([(0, 5, 1), (10, 5, 1)]),
            "line_features",
        ),
        ("prescription_point", Point(5, 5, 1), "point_features"),
    ],
)
def test_gpu_source_z_is_normalized_to_canonical_2d(
    logical: str,
    geometry: object,
    catalog_name: str,
) -> None:
    result = _run([_inspected(logical, _source_frame(logical, [geometry]))])
    catalog = getattr(result, catalog_name)
    assert not catalog.geometry.has_z.any()


def test_source_complete_contract_rejects_tampered_gpkg_inventory_hash() -> None:
    planning_document, parcels, result = _source_complete_contract()
    layer = planning_document.related_layers[0]
    relative = layer.reference.dataset_path.relative_to(
        planning_document.extraction.extraction_root
    ).as_posix()
    files = tuple(
        replace(item, sha256="f" * 64) if item.relative_path == relative else item
        for item in planning_document.extraction.files
    )
    changed = replace(
        planning_document,
        extraction=replace(planning_document.extraction, files=files),
    )
    with pytest.raises(PlanningFeaturesError, match="source|file|inventory|SHA"):
        _validate_source_complete(changed, parcels, result)


def test_source_complete_contract_rejects_tampered_gpkg_size() -> None:
    planning_document, parcels, result = _source_complete_contract()
    layer = planning_document.related_layers[0]
    relative = layer.reference.dataset_path.relative_to(
        planning_document.extraction.extraction_root
    ).as_posix()
    files = tuple(
        replace(item, size_bytes=item.size_bytes + 1)
        if item.relative_path == relative
        else item
        for item in planning_document.extraction.files
    )
    changed = replace(
        planning_document,
        extraction=replace(planning_document.extraction, files=files),
    )
    with pytest.raises(PlanningFeaturesError, match="source|file|inventory|size"):
        _validate_source_complete(changed, parcels, result)


def test_source_complete_contract_rejects_changed_gpkg_bytes() -> None:
    planning_document, parcels, result = _source_complete_contract()
    path = planning_document.related_layers[0].reference.dataset_path
    with path.open("ab") as stream:
        stream.write(b"tamper")
    with pytest.raises(PlanningFeaturesError, match="source|file|inventory|size|SHA"):
        _validate_source_complete(planning_document, parcels, result)


def test_source_complete_contract_rejects_same_size_gpkg_byte_tamper() -> None:
    planning_document, parcels, result = _source_complete_contract()
    path = planning_document.related_layers[0].reference.dataset_path
    payload = bytearray(path.read_bytes())
    payload[-1] ^= 1
    path.write_bytes(payload)
    with pytest.raises(PlanningFeaturesError, match="source|file|inventory|SHA"):
        _validate_source_complete(planning_document, parcels, result)


def test_source_complete_contract_rejects_coherently_changed_physical_gpkg() -> None:
    planning_document, parcels, result = _source_complete_contract()
    layer = planning_document.related_layers[0]
    changed_source = layer.data.copy(deep=True)
    changed_source.loc[changed_source.index[0], "LIBELLE"] = "Changed on disk"
    changed_source.to_file(
        layer.reference.dataset_path,
        layer=layer.reference.source_layer,
        driver="GPKG",
        engine="pyogrio",
        index=False,
    )
    coherent_inventory = _refresh_extraction_inventory(planning_document)
    with pytest.raises(PlanningFeaturesError, match="source|file|loaded|changed"):
        _validate_source_complete(coherent_inventory, parcels, result)


def test_source_complete_contract_rejects_changed_physical_gpkg_geometry() -> None:
    planning_document, parcels, result = _source_complete_contract()
    layer = planning_document.related_layers[0]
    changed_source = layer.data.copy(deep=True)
    changed_source.at[changed_source.index[0], "geometry"] = _rectangle(0, 0, 5, 10)
    changed_source.to_file(
        layer.reference.dataset_path,
        layer=layer.reference.source_layer,
        driver="GPKG",
        engine="pyogrio",
        index=False,
    )
    coherent_inventory = _refresh_extraction_inventory(planning_document)
    with pytest.raises(PlanningFeaturesError, match="source|geometry|loaded|changed"):
        _validate_source_complete(coherent_inventory, parcels, result)


def test_source_complete_contract_rejects_reordered_physical_gpkg_rows() -> None:
    parcels = _parcels(
        [_rectangle(0, 0, 10, 10), _rectangle(20, 0, 30, 10)],
        ids=["P-1", "P-2"],
    )
    layer = _inspected(
        "prescription_surface",
        _source_frame(
            "prescription_surface",
            [_rectangle(0, 0, 10, 10), _rectangle(20, 0, 30, 10)],
            ids=["ONE", "TWO"],
            type_codes=["07", "07"],
            subtype_codes=["04", "04"],
        ),
    )
    planning_document = _planning_document([layer])
    result = intersect_parcels_with_gpu_planning_features(parcels, planning_document)
    stored = planning_document.related_layers[0]
    stored.data.iloc[::-1].reset_index(drop=True).to_file(
        stored.reference.dataset_path,
        layer=stored.reference.source_layer,
        driver="GPKG",
        engine="pyogrio",
        index=False,
    )
    coherent_inventory = _refresh_extraction_inventory(planning_document)
    with pytest.raises(PlanningFeaturesError, match="source|order|loaded|changed"):
        _validate_source_complete(coherent_inventory, parcels, result)


def test_source_complete_contract_rejects_loaded_source_attrs_not_on_disk() -> None:
    planning_document, parcels, result = _source_complete_contract()
    layer = planning_document.related_layers[0]
    loaded = layer.data.copy(deep=True)
    loaded.attrs["unpersisted_source_note"] = "tampered"
    changed = replace(
        planning_document,
        related_layers=tuple(
            replace(item, data=loaded) if item is layer else item
            for item in planning_document.related_layers
        ),
    )
    with pytest.raises(PlanningFeaturesError, match="source|attrs|metadata|loaded"):
        _validate_source_complete(changed, parcels, result)


def test_source_complete_contract_rejects_dataset_outside_extraction_root(
    tmp_path: Path,
) -> None:
    planning_document, parcels, result = _source_complete_contract()
    layer = planning_document.related_layers[0]
    outside = tmp_path / "outside.gpkg"
    shutil.copyfile(layer.reference.dataset_path, outside)
    reference = replace(layer.reference, dataset_path=outside)
    changed = _replace_layer_reference(planning_document, layer.logical_name, reference)
    with pytest.raises(PlanningFeaturesError, match="source|root|outside|contain"):
        _validate_source_complete(changed, parcels, result)


def test_source_complete_contract_rejects_linked_spatial_dataset(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    planning_document, parcels, result = _source_complete_contract()
    dataset = planning_document.related_layers[0].reference.dataset_path
    actual_link_check = gpu_source_module._is_link_or_junction

    def synthetic_link(path: Path) -> bool:
        return path == dataset or actual_link_check(path)

    monkeypatch.setattr(
        gpu_source_module,
        "_is_link_or_junction",
        synthetic_link,
    )
    with pytest.raises(PlanningFeaturesError, match="source|link|junction|dataset"):
        _validate_source_complete(planning_document, parcels, result)


def _shapefile_source_complete_contract(
    root: Path,
) -> tuple[GpuPlanningDocument, gpd.GeoDataFrame, ParcelPlanningFeaturesResult]:
    source_layer = "PRESCRIPTION_SURFACE"
    path = root / f"{source_layer}.shp"
    frame = _source_frame(
        "prescription_surface",
        [_rectangle(0, 0, 10, 10)],
        ids=["SHAPE-1"],
        type_codes=["07"],
        subtype_codes=["04"],
    )
    frame.to_file(path, driver="ESRI Shapefile", engine="pyogrio", index=False)
    loaded = gpd.read_file(path, engine="pyogrio")
    layer = replace(
        _inspected("prescription_surface", loaded),
        reference=GpuSpatialLayerReference(path, source_layer, "ESRI Shapefile"),
        summary=_summary(loaded, source_layer),
    )
    document = _planning_document([layer])
    parcels = _parcels()
    result = intersect_parcels_with_gpu_planning_features(parcels, document)
    return document, parcels, result


def _shapefile_ogr_fid_source_complete_contract(
    root: Path,
) -> tuple[GpuPlanningDocument, gpd.GeoDataFrame, ParcelPlanningFeaturesResult]:
    source_layer = "PRESCRIPTION_SURFACE"
    path = root / f"{source_layer}.shp"
    frame = _source_frame(
        "prescription_surface",
        [_rectangle(0, 0, 5, 10), _rectangle(5, 0, 10, 10)],
        ids=["DROP-ONE", "DROP-TWO"],
        type_codes=["07", "07"],
        subtype_codes=["04", "04"],
    ).drop(columns="LIB_IDPSC")
    frame.to_file(path, driver="ESRI Shapefile", engine="pyogrio", index=False)
    loaded = gpd.read_file(path, engine="pyogrio")
    layer = replace(
        _inspected("prescription_surface", loaded),
        reference=GpuSpatialLayerReference(path, source_layer, "ESRI Shapefile"),
        summary=_summary(loaded, source_layer),
    )
    document = _planning_document([layer])
    parcels = _parcels()
    result = intersect_parcels_with_gpu_planning_features(parcels, document)
    return document, parcels, result


def test_source_complete_contract_binds_every_shapefile_sidecar(
    tmp_path: Path,
) -> None:
    planning_document, parcels, result = _shapefile_source_complete_contract(tmp_path)
    sidecar = next(
        item
        for item in planning_document.extraction.files
        if item.relative_path.casefold().endswith(".prj")
    )
    files = tuple(
        item
        for item in planning_document.extraction.files
        if item.relative_path != sidecar.relative_path
    )
    changed = replace(
        planning_document,
        extraction=replace(planning_document.extraction, files=files),
    )
    with pytest.raises(
        PlanningFeaturesError,
        match="shapefile|sidecar|inventory|physical revalidation",
    ):
        _validate_source_complete(changed, parcels, result)


@pytest.mark.parametrize("changed_fids", [(10, 11), (1, 0)])
def test_source_complete_contract_rejects_changed_or_reordered_ogr_fids(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    changed_fids: tuple[int, int],
) -> None:
    planning_document, parcels, result = _shapefile_ogr_fid_source_complete_contract(
        tmp_path
    )
    actual_read = gpu_source_module.pyogrio.read_dataframe

    def changed_fid_read(*args: object, **kwargs: object) -> gpd.GeoDataFrame:
        reread = actual_read(*args, **kwargs)
        if kwargs.get("fid_as_index"):
            reread.index = pd.Index(changed_fids, name="fid")
        return reread

    monkeypatch.setattr(
        gpu_source_module.pyogrio,
        "read_dataframe",
        changed_fid_read,
    )
    with pytest.raises(PlanningFeaturesError, match="source|FID|identity|catalog"):
        _validate_source_complete(planning_document, parcels, result)


def test_source_complete_contract_requires_shapefile_core_members(
    tmp_path: Path,
) -> None:
    planning_document, parcels, result = _shapefile_source_complete_contract(tmp_path)
    layer = planning_document.related_layers[0]
    layer.reference.dataset_path.with_suffix(".shx").unlink()
    with pytest.raises(PlanningFeaturesError, match="shapefile|shx|source|file"):
        _validate_source_complete(planning_document, parcels, result)


def test_source_complete_contract_rejects_changed_shapefile_sidecar_bytes(
    tmp_path: Path,
) -> None:
    planning_document, parcels, result = _shapefile_source_complete_contract(tmp_path)
    layer = planning_document.related_layers[0]
    cpg = layer.reference.dataset_path.with_suffix(".cpg")
    cpg.write_text("UTF-8\n", encoding="utf-8")
    with pytest.raises(
        PlanningFeaturesError,
        match="shapefile|sidecar|size|SHA|physical revalidation",
    ):
        _validate_source_complete(planning_document, parcels, result)


def test_dotted_sibling_dataset_is_not_a_sidecar_and_makes_role_ambiguous(
    tmp_path: Path,
) -> None:
    planning_document, parcels, result = _shapefile_source_complete_contract(tmp_path)
    _validate_source_complete(planning_document, parcels, result)
    primary = planning_document.related_layers[0].reference.dataset_path
    sibling = primary.with_name(f"{primary.stem}.archive.shp")
    gpd.GeoDataFrame(
        {"sibling": [1]},
        geometry=[_rectangle(20, 20, 21, 21)],
        crs="EPSG:2154",
    ).to_file(sibling, driver="ESRI Shapefile", engine="pyogrio", index=False)
    refreshed = _refresh_extraction_inventory(planning_document)
    with pytest.raises(
        PlanningFeaturesError,
        match="Related GPU spatial sources failed physical revalidation",
    ):
        _validate_source_complete(refreshed, parcels, result)


@pytest.mark.parametrize("bad_item", [None, object()])
def test_batch_gpu_revalidation_rejects_malformed_layer_items(
    bad_item: object,
) -> None:
    planning_document, _, _ = _source_complete_contract()
    with pytest.raises(gpu_source_module.GpuSpatialInspectionError):
        gpu_source_module.revalidate_gpu_spatial_layer_sources(
            planning_document,
            (bad_item,),  # type: ignore[arg-type]
        )


def test_batch_gpu_revalidation_rejects_malformed_planning_document() -> None:
    with pytest.raises(gpu_source_module.GpuSpatialInspectionError):
        gpu_source_module.revalidate_gpu_spatial_layer_sources(
            object(),  # type: ignore[arg-type]
            (),
        )


def test_batch_gpu_revalidation_rejects_duplicate_logical_name() -> None:
    planning_document, _, _ = _source_complete_contract()
    layer = planning_document.related_layers[0]
    with pytest.raises(gpu_source_module.GpuSpatialInspectionError, match="duplicate"):
        gpu_source_module.revalidate_gpu_spatial_layer_sources(
            planning_document,
            (layer, layer),
        )


@pytest.mark.parametrize(
    "statement",
    [
        (
            "from landscout.common.planning_feature_contract import "
            "validate_intrinsic_planning_feature_relations"
        ),
        (
            "from landscout.common.bess_application_contract import "
            "validate_bess_application_feature_catalogs"
        ),
    ],
)
def test_common_planning_contracts_import_without_initializing_stages(
    statement: str,
) -> None:
    completed = subprocess.run(
        [
            sys.executable,
            "-c",
            f"import sys; {statement}; assert 'landscout.stages' not in sys.modules",
        ],
        cwd=Path(__file__).resolve().parents[2],
        capture_output=True,
        check=False,
        text=True,
    )
    assert completed.returncode == 0, completed.stderr
```
