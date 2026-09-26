# `tests/unit/test_apply_bess_planning_feature_policy.py`

- Source: [tests/unit/test_apply_bess_planning_feature_policy.py](../../../../../tests/unit/test_apply_bess_planning_feature_policy.py)
- Source SHA256: `563c9382062de5406384bd574df5ca169dde642ae768102c4973bd8d9be68184`
- Source SHA256 basis: `git-content`
- Source lines: 2397; Git blob at R9 start: `5c2fed792f0df5b1fd9b95417dafcda6c3094eca`

Git/index/checkout source bytes are unchanged; the full source snapshot below is exact UTF-8 LF. Semantic local closure is not independent approval. [R9 evidence](../../../../../docs/code/audit/R9_BESS_CNIG_APPLICATION.md).

## Ownership, setup and limits

This file tests [application propagation](../../src/landscout/stages/apply_bess_planning_feature_policy.py.md), not parcel-policy aggregation. It declares no __all__ and no pytest.fixture-decorated function. Pytest discovers the top-level test functions and expands their literal parametrizations; nested callbacks are separate inventoried symbols, not extra tests. Existing source remains unchanged by R9; the receipt records the one actual focused run and full process exit, rather than a count inferred from old prose.

Standard-library imports cover importlib/inspect, JSON, Mapping, dataclass fields/replace, SHA, BytesIO and Path. GeoPandas/Pandas/Pytest/Shapely and their assertion helpers are third-party owners. Imports spelled `test_bess_planning_feature_policy` and `test_resolve_planning_feature_codes` are repository test helpers: qualified documentation owners are tests.unit.test_bess_planning_feature_policy and tests.unit.test_resolve_planning_feature_codes. Application imports include the importable ArtifactRecord as well as public APIs; _load_application_artifacts is the real production loader alias, distinct from this file's adapter. Repository stages and frame_integrity are not external packages.

The fixture chain is _application_fixture → tests.unit.test_bess_planning_feature_policy._compiled_fixture → tests.unit.test_resolve_planning_feature_codes._integration_inputs/_planning_document. It constructs and writes physical temporary GeoPackages through Pyogrio, rereads them, writes an extraction inventory/manifest and binds a modified synthetic source config; normalization/coding/policy/application then use public source-bound paths. Archive metadata is fabricated (synthetic.zip, one byte, repeated-a hash); this is not official GPU acquisition. The four synthetic related objects are prescription surface square(0,0)-(2,2), information surface square(3,0)-(5,2), prescription line(0,1)-(2,1), information point(10,10). There is ONE parcel equal to the first square (index91 named parcel_row); this is not aggregation R8's two-parcel/three-relation fixture. The application catalogs contain unreferenced information surface/point objects.

The normal policy is synthetic_bess_cnig_feature_policy_v1 built from the synthetic dictionary, rotating configured statuses/confidences with source locks. The separate _checked_in_policy_result reads checked-in policy/CNIG configs, replaces a coded envelope's identities/dictionary to those locks and privately builds the policy table; it is NOT a public physical validation of the actual Muret snapshot. _small_catalog is a deliberately minimal Point-based five-column catalog for private propagation tests, not a canonical complete application catalog. Empty-upstream helpers copy empty typed frames/dictionaries/tables and reseal; they do not read a real source.

_application_fixture assigns both _LAST_* globals. The same-named test adapter replaces BOTH supplied upstreams with those globals if EITHER is None, asserts both available, then delegates to the production seven-argument loader. It catches no error and has no unknown-feature fallback. Five-path test calls therefore use last-fixture upstreams; tests using _load_application_artifacts explicitly supply both. There is no inference of missing sources in the public API.

## Reading assertions, not titles

All tests return None; fixture parameters are pytest tmp_path/monkeypatch or literal parametrized values whose exact declarations appear beside each notice. Assertions/helpers and expected exceptions are documented per scenario below. A helper named counted may be a no-op counter, a delegating spy or an AssertionError sentinel: each callback has its own notice. No shared counter is silently multiplied into independent proof.

Guard order matters: canonical schema/dtype/official/identity checks can precede the branch suggested by a title; duplicate-pair scenarios retaining duplicate indices do not independently demonstrate the unique-index case; a later test explicitly supplies unique indices. Rehashing application output does not revalidate policy or coded source authority. A byte-consistent GeoParquet/manifest can still carry stale semantic hashes. A broad raises or regex is not proof of one specific inner exception or complete physical provenance.

R9-T01: the incompatible/empty upstream tests patch Path.read_text, but production reads manifest with Path.read_bytes. Their manifest=0 counters do NOT alone instrument that actual read. Source control flow places upstream checks before manifest.read_bytes; artifact-reader/build sentinels and heavy counters test their own targets correctly. The bad-upstream test separately patches Path.read_bytes, but uses broad pytest.raises(Exception). This is an explicit test-evidence limit, not automatically a new production defect, and no test is altered.

R9-T02: test_source_bound_loader_rejects_unreferenced_feature_and_row_reordering only changes an unreferenced label. The separate all-null-raw-column-transition test also contains the row-reversal scenario. R9-T03: M/ZM coverage here is two Point WKT cases; six geometry kinds are covered for Z, not for every M/ZM variant. R9-T04: captured-byte success proves parsing the captured payload, not a post-read path-integrity check. Several broad checks/first-guard limits are further localized below. These reservations do not erase the positive assertions or extend them to other modules.

## Effects and boundaries

_write_application_artifacts is a TEST helper returning (manifest Path, role→Path dict, manifest dict), not three paths and not a public writer. It writes four synthetic Parquets with stored index and a strict schema2 manifest. Most tests call _application_fixture and therefore indirectly perform physical synthetic GPKG reads/writes before instrumentation is installed. Mutation helpers copy frames before assignment and reseal only the specified envelopes. They can intentionally violate source truth while keeping local hashes consistent. Geometry replacement is adversarial test setup, not production geometry repair.

The source/test full snapshots and all qualified symbol bindings are retained below. Signatures/parametrizations are mechanically quoted; their semantic notices follow manually inspected setup, call order and assertions. No real cache/Muret/GPU/EP download/open, legal research, full-suite run, scoring or environment repair is evidence of this bounded audit. Independent R9 review and visual rendering remain pending.

Inventory: 72 top-level tests, 110 original symbols (including helpers/nested callbacks); parametrized collected cases are reported only after execution.

## Module declarations

These literal declarations add no original symbol credit. Imports and owners are explained above; declaration values are source excerpts, not runtime imports.

<a id="declaration-application-scope"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.APPLICATION_SCOPE`

Source lines 47–47. Test expectation for propagation-only scope; no mutable runtime policy authority.

```python
APPLICATION_SCOPE = "FEATURE_AND_RELATION_POLICY_PROPAGATION_ONLY"
```

<a id="declaration-policy-columns"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.POLICY_COLUMNS`

Source lines 48–67. Independent ordered18-column expected suffix; asserted against every enriched output.

```python
POLICY_COLUMNS = (
    "bess_cnig_policy_application_status",
    "bess_cnig_precheck_status",
    "bess_cnig_precheck_confidence",
    "bess_cnig_status_priority",
    "bess_cnig_rationale",
    "bess_cnig_required_human_action",
    "bess_cnig_limitations",
    "bess_cnig_application_scope",
    "bess_cnig_policy_scope",
    "bess_cnig_local_feature_text_interpreted",
    "bess_cnig_local_regulation_content_interpreted",
    "bess_cnig_legal_conclusion_produced",
    "bess_cnig_parcel_status_aggregated",
    "bess_cnig_parcel_rejection_performed",
    "bess_cnig_score_calculated",
    "bess_cnig_policy_profile",
    "bess_cnig_policy_sha256",
    "bess_cnig_policy_result_sha256",
)
```

<a id="declaration-boundary-flag-columns"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.BOUNDARY_FLAG_COLUMNS`

Source lines 68–75. Six expected row flags; used for all-False assertions and parametrized True rejection.

```python
BOUNDARY_FLAG_COLUMNS = (
    "bess_cnig_local_feature_text_interpreted",
    "bess_cnig_local_regulation_content_interpreted",
    "bess_cnig_legal_conclusion_produced",
    "bess_cnig_parcel_status_aggregated",
    "bess_cnig_parcel_rejection_performed",
    "bess_cnig_score_calculated",
)
```

<a id="declaration-artifact-files"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.ARTIFACT_FILES`

Source lines 76–81. Test-only ordered role→(filename,geospatial bool) mapping for four synthetic Parquets; not a production public writer/config.

```python
ARTIFACT_FILES = {
    "SURFACE_FEATURES": ("surface.parquet", True),
    "LINE_FEATURES": ("line.parquet", True),
    "POINT_FEATURES": ("point.parquet", True),
    "RELATIONS": ("relations.parquet", False),
}
```

<a id="declaration--last-coded-result"></a>
### `tests.unit.test_apply_bess_planning_feature_policy._LAST_CODED_RESULT`

Source lines 82–82. Mutable module global, initially None; _application_fixture assigns latest coded object. Legacy adapter reads it if either supplied upstream is missing.

```python
_LAST_CODED_RESULT: object | None = None
```

<a id="declaration--last-policy-result"></a>
### `tests.unit.test_apply_bess_planning_feature_policy._LAST_POLICY_RESULT`

Source lines 83–83. Mutable module global, initially None; assigned together with coded object. Adapter replaces BOTH upstream arguments when either is None; sequential fixture context, not source inference.

```python
_LAST_POLICY_RESULT: object | None = None
```

## Qualified symbol contracts

Each heading owns exactly one original symbol. Quoted signatures give parameter order/types/defaults and return annotation; notices distinguish actual behavior, callers and effects. Fields are required unless explicitly declared otherwise. Complete bodies, imports and decorators are in the final snapshot.

<a id="symbol--application-artifact-record-payload"></a>
### `tests.unit.test_apply_bess_planning_feature_policy._application_artifact_record_payload`

Source lines 86–109. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def _application_artifact_record_payload() -> dict[str, object]:
```

Return fresh dict for one SURFACE_FEATURES record with geometry-only schema and a minimal CRS dictionary named RGF93 v1 / Lambert-93 (not a complete PyProj CRS validation fixture), one row/byte and repeated-a SHA. The same caller-owned CRS dict appears in schema and crs positions, intentionally exercising alias isolation. No file is created and this payload is not a complete application catalog.

<a id="symbol-test-application-artifact-record-is-deeply-immutable-without-aliases"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_application_artifact_record_is_deeply_immutable_without_aliases`

Source lines 112–140. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_application_artifact_record_is_deeply_immutable_without_aliases() -> None:
```

Validate the fresh payload; mutate caller columns with caller_mutation and add a CRS caller_mutation key. Assert model_dump equals a NEW payload, not a saved dump. Four immediate mutation attempts on retained mapping/sequence/nested CRS/record CRS must fail with TypeError or AttributeError. Asserts Mapping shapes; no filename/CRS-name mutation or artifact I/O is performed.

<a id="symbol--application-fixture"></a>
### `tests.unit.test_apply_bess_planning_feature_policy._application_fixture`

Source lines 143–155. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def _application_fixture() -> tuple[
    tuple[object, ...],
    object,
    object,
    object,
    BessPlanningFeatureApplicationResult,
]:
```

Call repository _compiled_fixture, invoke public application builder with its ten inputs, assign both _LAST_CODED_RESULT/_LAST_POLICY_RESULT globals, return five-tuple (inputs,coded,config,policy,result). No pytest.fixture decorator/cache: each call rebuilds synthetic physical inputs and performs source validation.

<a id="symbol-load-bess-planning-feature-application-artifacts"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.load_bess_planning_feature_application_artifacts`

Source lines 158–182. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def load_bess_planning_feature_application_artifacts(
    manifest_path: str | Path,
    surface_features_path: str | Path,
    line_features_path: str | Path,
    point_features_path: str | Path,
    relations_path: str | Path,
    coded_result: object | None = None,
    policy_result: object | None = None,
) -> BessPlanningFeatureApplicationResult:
```

Test adapter with five required paths and two optional object upstreams default None. If either is None, replace both with latest globals; assert both nonnull, delegate seven arguments to _load_application_artifacts and return production result. No try/except, fallback on unknown feature, mutation of source frames or public omitted-source compatibility.

<a id="symbol--small-catalog"></a>
### `tests.unit.test_apply_bess_planning_feature_policy._small_catalog`

Source lines 185–196. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def _small_catalog(*rows: tuple[str, str, str, str, str]) -> gpd.GeoDataFrame:
```

From variadic five-string row tuples create minimal GeoDataFrame with planning ID/family/type/subtype/official status and generated Point(index,index) geometry in EPSG:2154. Return new frame for private _apply_feature_catalog tests only; lacks full factual schema/lineage and is not evidence of full source-bound acceptance.

<a id="symbol--write-application-artifacts"></a>
### `tests.unit.test_apply_bess_planning_feature_policy._write_application_artifacts`

Source lines 199–252. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def _write_application_artifacts(
    tmp_path: Path,
    result: BessPlanningFeatureApplicationResult,
) -> tuple[Path, dict[str, Path], dict[str, object]]:
```

Write four role-mapped output frames to Parquet(index=True), capture size/raw SHA/schema/CRS and collect all non-frame dataclass fields into schema2 manifest; validate the manifest and write JSON to application.json. Return (manifest_path,paths,payload): Path, dict of Paths, dict. Inputs are read, not mutated; filesystem effects are synthetic test artifacts only.

<a id="symbol--coordinated-policy-mutation"></a>
### `tests.unit.test_apply_bess_planning_feature_policy._coordinated_policy_mutation`

Source lines 255–298. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def _coordinated_policy_mutation(
    result: BessPlanningFeatureApplicationResult,
    column: str,
    value: object,
    *,
    dtype: str | None = None,
) -> BessPlanningFeatureApplicationResult:
```

Select first relation feature ID, deep-copy all three catalogs and relations, change the named column on that feature and all its relations, optionally force supplied dtype (category handled explicitly), then rehash application result. Return forged result; no policy/coded source rebuild. Used to isolate local domain/dtype/global-mapping versus upstream truth checks.

<a id="symbol--coordinated-feature-id-mutation"></a>
### `tests.unit.test_apply_bess_planning_feature_policy._coordinated_feature_id_mutation`

Source lines 301–320. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def _coordinated_feature_id_mutation(
    result: BessPlanningFeatureApplicationResult,
    feature_id: object,
) -> BessPlanningFeatureApplicationResult:
```

Copy three catalogs and relations, replace referenced ID everywhere consistently, rehash result and return it. Invalid value tests can fail full catalog GPU identity before relation checks; no source-file mutation.

<a id="symbol--zero-relation-feature"></a>
### `tests.unit.test_apply_bess_planning_feature_policy._zero_relation_feature`

Source lines 323–332. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def _zero_relation_feature(
    result: BessPlanningFeatureApplicationResult,
) -> tuple[str, gpd.GeoDataFrame, object]:
```

Collect IDs present in result.relations, scan catalogs in surface/line/point order, return (attribute name, ORIGINAL frame, first unreferenced index). Does not copy/mutate; callers copy before altering. Raise AssertionError if fixture has no unreferenced object.

<a id="symbol--surface-touch-with-positive-area"></a>
### `tests.unit.test_apply_bess_planning_feature_policy._surface_touch_with_positive_area`

Source lines 335–345. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def _surface_touch_with_positive_area(
    result: BessPlanningFeatureApplicationResult,
) -> BessPlanningFeatureApplicationResult:
```

Deep-copy relations, locate first SURFACE row, assert its intersection area positive, relabel relation_type TOUCH_ONLY, rehash replacement result and return. Produces an intrinsic metric/type contradiction without changing geometry/files.

<a id="symbol--z-geometry"></a>
### `tests.unit.test_apply_bess_planning_feature_policy._z_geometry`

Source lines 348–359. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def _z_geometry(kind: str) -> object:
```

Return Z=7 geometry for one of six kind strings: square Polygon/MultiPolygon, diagonal LineString/MultiLineString or Point/MultiPoint; unknown kind raises AssertionError. Used in local dimensional tests. No M/ZM generation or I/O.

<a id="symbol-test-exact-policy-is-applied-to-every-feature-and-relation"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_exact_policy_is_applied_to_every_feature_and_relation`

Source lines 362–402. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_exact_policy_is_applied_to_every_feature_and_relation() -> None:
```

Use full synthetic application; assert schema2, application scope and three policy lineage values. For every catalog assert preserved-prefix columns and all APPLIED_EXACT_POLICY, then compare six decisions against exact policy-table triple lookup. Assert relation application statuses all APPLIED_EXACT_POLICY and policy_config.policy_scope equals result.policy_scope. No nonempty-relation or unresolved/null assertion occurs here; those scenarios have separate tests.

<a id="symbol-test-every-output-row-has-all-six-false-boundary-flags"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_every_output_row_has_all_six_false_boundary_flags`

Source lines 405–417. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_every_output_row_has_all_six_false_boundary_flags() -> None:
```

For all four output frames assert each of six flags exists, dtype bool, no null and all False. Fixture setup precedes assertions; does not check scalar flags here (scope test does).

<a id="symbol-test-policy-suffix-has-one-exact-deterministic-dtype-schema"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_policy_suffix_has_one_exact_deterministic_dtype_schema`

Source lines 420–442. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_policy_suffix_has_one_exact_deterministic_dtype_schema() -> None:
```

Assert last18 columns equal expected tuple and suffix dtype mapping is eleven str, Int64 priority, six bool for all four frames. Tests strict representation, including null-compatible priority; no row decision inference.

<a id="symbol-test-schema-v1-dimension-blind-hash-representation-is-rejected-locally"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_schema_v1_dimension_blind_hash_representation_is_rejected_locally`

Source lines 445–467. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_schema_v1_dimension_blind_hash_representation_is_rejected_locally() -> None:
```

Replace surface geometry with Z while retaining old digests; assert dimensions differ but output_dimension=2 WKB would match. Local envelope AND hash rebuilding must raise application error matching 2D/dimension. Demonstrates why current schema2 rejects dimensional loss; not an executed migration.

<a id="symbol-test-every-non-2d-application-geometry-kind-fast-fails-before-source-validation"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_every_non_2d_application_geometry_kind_fast_fails_before_source_validation`

Source lines 481–504. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_every_non_2d_application_geometry_kind_fast_fails_before_source_validation(
    monkeypatch: pytest.MonkeyPatch,
    frame_name: str,
    geometry_kind: str,
) -> None:
```

Six Z geometry kinds/roles: replace first geometry, retain result hashes, install no-op counted heavy owner; full validator must raise 2D/dimension and calls==0. Fixture physical work happened before patch. First local catalog geometry guard suffices; not six M/ZM tests.

Exact decorators/parametrization (not extra closure units):

```python
@pytest.mark.parametrize(
    ("frame_name", "geometry_kind"),
    [
        ("surface_features", "Polygon"),
        ("surface_features", "MultiPolygon"),
        ("line_features", "LineString"),
        ("line_features", "MultiLineString"),
        ("point_features", "Point"),
        ("point_features", "MultiPoint"),
    ],
)
```

<a id="symbol-test-every-non-2d-application-geometry-kind-fast-fails-before-source-validation-counted"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_every_non_2d_application_geometry_kind_fast_fails_before_source_validation.counted`

Source lines 495–497. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
    def counted(*args: object, **kwargs: object) -> None:
```

Nested no-op replacement for the heavy policy-owner validator in test_every_non_2d_application_geometry_kind_fast_fails_before_source_validation. Increment captured calls and return None; no delegation or source I/O. Parent asserts calls==0 after local/lock rejection; fixture work precedes installation.

<a id="symbol-test-m-and-zm-application-geometries-are-rejected"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_m_and_zm_application_geometries_are_rejected`

Source lines 508–516. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_m_and_zm_application_geometries_are_rejected(wkt: str) -> None:
```

Two parameter values POINT M and POINT ZM replace a point geometry; local envelope raises 2D/dimension. Coverage is these two Points only, with no additional equality or heavy-counter assertion.

Exact decorators/parametrization (not extra closure units):

```python
@pytest.mark.parametrize("wkt", ["POINT M (1 1 7)", "POINT ZM (1 1 7 8)"])
```

<a id="symbol-test-valid-empty-optional-application-catalog-retains-schema-and-crs"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_valid_empty_optional_application_catalog_retains_schema_and_crs`

Source lines 519–531. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_valid_empty_optional_application_catalog_retains_schema_and_crs() -> None:
```

Apply private catalog helper to empty copy of coded optional point catalog; assert empty, original-prefix columns, exact suffix, same CRS and geometry name. Does not build/validate a new source-complete result. It also explicitly calls _validate_application_geometry on the empty output; this is not the full application envelope.

<a id="symbol-test-exact-pair-identity-keeps-family-subtype-and-leading-zeroes-distinct"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_exact_pair_identity_keeps_family_subtype_and_leading_zeroes_distinct`

Source lines 534–558. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_exact_pair_identity_keeps_family_subtype_and_leading_zeroes_distinct() -> None:
```

Use checked-in-policy helper plus minimal private catalog: prescription15/00 and15/01 both DESIGN_REVIEW_REQUIRED but MEDIUM versus HIGH; mismatched subtype/family remain unresolved; leading01/00 strings preserved. No public source validation of the locked checked-in Muret identity is performed by that helper.

<a id="symbol-test-unknown-pair-remains-present-with-true-null-decision-fields"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_unknown_pair_remains_present_with_true_null_decision_fields`

Source lines 561–576. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_unknown_pair_remains_present_with_true_null_decision_fields() -> None:
```

Private minimal catalog with98/00 remains present under same ID; assert UNRESOLVED_CODE_PAIR and six null values, not textual None/nan/<NA>. This is unresolved evidence, not an exact configured UNKNOWN decision.

<a id="symbol-test-inconsistent-official-status-and-policy-match-is-rejected"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_inconsistent_official_status_and_policy_match_is_rejected`

Source lines 586–593. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_inconsistent_official_status_and_policy_match_is_rejected(
    row: tuple[str, str, str, str, str],
) -> None:
```

Two private catalog cases: missing98/00 entry declared RESOLVED_OFFICIAL, or known15/00 entry declared UNKNOWN_CODE_PAIR. Each raises application error matching policy/official; no public canonical-catalog acceptance is implied.

Exact decorators/parametrization (not extra closure units):

```python
@pytest.mark.parametrize(
    "row",
    [
        ("F-MISSING", "PRESCRIPTION", "98", "00", "RESOLVED_OFFICIAL"),
        ("F-UNEXPECTED", "PRESCRIPTION", "15", "00", "UNKNOWN_CODE_PAIR"),
    ],
)
```

<a id="symbol-test-feature-and-relation-inputs-are-preserved-and-not-mutated"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_feature_and_relation_inputs_are_preserved_and_not_mutated`

Source lines 596–623. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_feature_and_relation_inputs_are_preserved_and_not_mutated() -> None:
```

Save deep copies of coded three catalogs/relations and source parcels, run public application, compare original inputs unchanged and output factual prefixes exactly (including dtypes/index/geometry/CRS), suffix ordered. No independent physical source acquisition beyond synthetic fixture.

<a id="symbol-test-relations-inherit-only-from-referenced-enriched-feature"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_relations_inherit_only_from_referenced_enriched_feature`

Source lines 626–639. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_relations_inherit_only_from_referenced_enriched_feature() -> None:
```

Map all enriched catalog rows by planning_feature_id and assert every relation's18 policy cells match its referenced feature (nulls handled). This is object-based inheritance, not a new code/parcel lookup.

<a id="symbol-test-complete-relation-facts-must-match-referenced-feature"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_complete_relation_facts_must_match_referenced_feature`

Source lines 661–673. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_complete_relation_facts_must_match_referenced_feature(
    column: str, value: object
) -> None:
```

Fourteen mutations of relation factual/official/area fields; rehash changed application then private local envelope must raise relation/feature error. Broad regex can match earlier intrinsic lineage/metric checks, not necessarily the22-column comparison for every case.

Exact decorators/parametrization (not extra closure units):

```python
@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("source_feature_id", "MUTATED"),
        ("source_identity_kind", "MUTATED"),
        ("source_identity_field", "MUTATED"),
        ("logical_layer", "information_surface"),
        ("label_raw", "MUTATED"),
        ("text_raw", "MUTATED"),
        ("source_document_id", "MUTATED"),
        ("source_archive_sha256", "f" * 64),
        ("source_layer", "MUTATED"),
        ("source_validity_date_raw", "2099-01-01"),
        ("regulation_filename_raw", "MUTATED.pdf"),
        ("official_code_label", "MUTATED"),
        ("official_code_profile", "MUTATED"),
        ("feature_area_m2", 999.0),
    ],
)
```

<a id="symbol-test-unknown-relation-feature-id-is-rejected"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_unknown_relation_feature_id_is_rejected`

Source lines 676–690. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_unknown_relation_feature_id_is_rejected() -> None:
```

Copy coded relations, assign unknown feature ID, call private _apply_relations with enriched catalogs and require feature-ID error. The additional assertion is policy is not None, not an input-preservation comparison. Directly targets lookup, without rebuilding a full application envelope.

<a id="symbol-test-scope-has-no-parcel-output-aggregation-rejection-or-score"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_scope_has_no_parcel_output_aggregation_rejection_or_score`

Source lines 693–703. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_scope_has_no_parcel_output_aggregation_rejection_or_score() -> None:
```

Assert absence of parcels attribute, six scalar flags False, and no parcel_id in surface catalog. Also assert len(source parcels)>0. No legal/BESS authorization or absence-of-constraint conclusion is asserted.

<a id="symbol-test-coordinated-feature-or-relation-policy-mutation-is-rejected"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_coordinated_feature_or_relation_policy_mutation_is_rejected`

Source lines 706–724. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_coordinated_feature_or_relation_policy_mutation_is_rejected() -> None:
```

Two subcases mutate surface precheck_status=UNKNOWN OR relation precheck_confidence=LOW separately, rehash, then full validator rejects. Despite title, each case changes one side, not both coherently; local object/relation disagreement may stop before source reconstruction.

<a id="symbol-test-duplicate-application-relation-pair-is-rejected-locally"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_duplicate_application_relation_pair_is_rejected_locally`

Source lines 727–735. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_duplicate_application_relation_pair_is_rejected_locally() -> None:
```

Concatenate first relation without resetting index, rehash and call local envelope expecting duplicate/unique error. This does not isolate duplicate-pair detection from any earlier guard; the later unique-index test does.

<a id="symbol-test-application-relation-feature-id-is-exact-and-portable"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_application_relation_feature_id_is_exact_and_portable`

Source lines 742–751. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_application_relation_feature_id_is_exact_and_portable(
    feature_id: object,
) -> None:
```

Six bad ID values including None, empty, textual None, absolute POSIX/Windows and whitespace; coordinated catalog+relation ID mutation then local envelope error feature/identity. Catalog GPU identity may be first guard, not a relation-only test.

Exact decorators/parametrization (not extra closure units):

```python
@pytest.mark.parametrize(
    "feature_id",
    [None, "", "None", "/tmp/feature", r"C:\feature", " GPU:F "],
)
```

<a id="symbol-test-application-relation-parcel-id-is-exact"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_application_relation_parcel_id_is_exact`

Source lines 755–764. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_application_relation_parcel_id_is_exact(parcel_id: object) -> None:
```

Four parcel ID values None/empty/textualNone/padded modify a relation then rehash; local envelope raises parcel/identity. Checks exact existing relation identity, not source parcel membership.

Exact decorators/parametrization (not extra closure units):

```python
@pytest.mark.parametrize("parcel_id", [None, "", "None", " PARCEL-1 "])
```

<a id="symbol-test-unknown-application-relation-type-is-rejected-locally"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_unknown_application_relation_type_is_rejected_locally`

Source lines 767–776. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_unknown_application_relation_type_is_rejected_locally() -> None:
```

Set first relation type BUFFERED_NEARBY, rehash, expect local relation-type application error. Does not infer a distance relation or add geometry algorithm.

<a id="symbol-test-coordinated-invalid-policy-domains-fail-local-validation"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_coordinated_invalid_policy_domains_fail_local_validation`

Source lines 794–805. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_coordinated_invalid_policy_domains_fail_local_validation(
    column: str,
    value: object,
    message: str,
) -> None:
```

Ten coordinated catalog/relation mutations: three forbidden invented statuses, CERTAIN confidence, priorities0/-1, invalid rationale/action/limitations strings. Local envelope rejects with parameter-specific regex after application reseal; no upstream policy mutation or repair.

Exact decorators/parametrization (not extra closure units):

```python
@pytest.mark.parametrize(
    ("column", "value", "message"),
    [
        ("bess_cnig_precheck_status", "AUTHORIZED", "status|domain"),
        ("bess_cnig_precheck_status", "FORBIDDEN", "status|domain"),
        ("bess_cnig_precheck_status", "PROHIBITED", "status|domain"),
        ("bess_cnig_precheck_confidence", "CERTAIN", "confidence|domain"),
        ("bess_cnig_status_priority", 0, "priority|positive"),
        ("bess_cnig_status_priority", -1, "priority|positive"),
        ("bess_cnig_rationale", "", "rationale|exact|non-empty"),
        ("bess_cnig_rationale", " leading", "rationale|exact|whitespace"),
        ("bess_cnig_required_human_action", "trailing ", "action|exact|whitespace"),
        ("bess_cnig_limitations", "", "limitations|exact|non-empty"),
    ],
)
```

<a id="symbol-test-literal-null-replacements-are-rejected"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_literal_null_replacements_are_rejected`

Source lines 809–816. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_literal_null_replacements_are_rejected(literal: str) -> None:
```

For textual None/nan/<NA> rationale on catalog and relations, rehash then local envelope rejects literal/missing. Distinct from permitted true null decisions for unresolved pairs.

Exact decorators/parametrization (not extra closure units):

```python
@pytest.mark.parametrize("literal", ["None", "nan", "<NA>"])
```

<a id="symbol-test-self-consistent-wrong-policy-suffix-dtype-is-rejected"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_self_consistent_wrong_policy_suffix_dtype_is_rejected`

Source lines 830–841. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_self_consistent_wrong_policy_suffix_dtype_is_rejected(
    column: str,
    dtype: str,
    value: object,
) -> None:
```

Six coordinated suffix casts: object status/rationale, category confidence, Float64/string priority, nullable boolean flag. Rehash, then local envelope schema/dtype rejection; valid-looking values do not excuse representation drift.

Exact decorators/parametrization (not extra closure units):

```python
@pytest.mark.parametrize(
    ("column", "dtype", "value"),
    [
        ("bess_cnig_precheck_status", "object", "UNKNOWN"),
        ("bess_cnig_precheck_confidence", "category", "HIGH"),
        ("bess_cnig_rationale", "object", "Still a factual policy rationale."),
        ("bess_cnig_status_priority", "Float64", 1.0),
        ("bess_cnig_status_priority", "str", "1"),
        ("bess_cnig_parcel_status_aggregated", "boolean", False),
    ],
)
```

<a id="symbol-test-official-and-application-statuses-cannot-contradict"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_official_and_application_statuses_cannot_contradict`

Source lines 851–877. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_official_and_application_statuses_cannot_contradict(
    official_status: str,
    application_status: str,
) -> None:
```

Two contradictory official/application status combinations are forged in copies and rehashed. Local envelope raises official/status; UNKNOWN_CODE_PAIR with retained meaning may fail official-null requirements before application-status consistency.

Exact decorators/parametrization (not extra closure units):

```python
@pytest.mark.parametrize(
    ("official_status", "application_status"),
    [
        ("RESOLVED_OFFICIAL", "UNRESOLVED_CODE_PAIR"),
        ("UNKNOWN_CODE_PAIR", "APPLIED_EXACT_POLICY"),
    ],
)
```

<a id="symbol-test-any-true-row-boundary-flag-is-rejected"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_any_true_row_boundary_flag_is_rejected`

Source lines 881–888. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_any_true_row_boundary_flag_is_rejected(column: str) -> None:
```

Each of six flags set True consistently in catalog/relations through helper, rehash, require local flag/false failure. Scalar flags remain unchanged; row invariants are tested.

Exact decorators/parametrization (not extra closure units):

```python
@pytest.mark.parametrize("column", BOUNDARY_FLAG_COLUMNS)
```

<a id="symbol-test-application-and-public-validator-heavy-validation-counts"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_application_and_public_validator_heavy_validation_counts`

Source lines 891–912. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_application_and_public_validator_heavy_validation_counts(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

After full fixture setup, replace policy-owner full validator with delegating counted spy. Public builder increments to1; public full application validator increments to2. Measures owner invocations, not physical file reads or internal passes.

<a id="symbol-test-application-and-public-validator-heavy-validation-counts-counted"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_application_and_public_validator_heavy_validation_counts.counted`

Source lines 901–904. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
    def counted(*args: object, **kwargs: object) -> None:
```

Nested delegating spy: increment calls, invoke actual(*args,**kwargs), then return None implicitly. Counts real full policy-owner invocations during builder/full-validator calls, not individual source reads.

<a id="symbol-test-malformed-local-result-fast-fails-before-heavy-validation"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_malformed_local_result_fast_fails_before_heavy_validation`

Source lines 915–936. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_malformed_local_result_fast_fails_before_heavy_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

Install no-op counted heavy callback, replace complete application digest with syntactically valid but incorrect repeated-f 64-hex digest and call full validator. Require hash/SHA/invalid error and calls0. Local validation prevents heavy call; fixture already performed heavy work before instrumentation.

<a id="symbol-test-malformed-local-result-fast-fails-before-heavy-validation-counted"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_malformed_local_result_fast_fails_before_heavy_validation.counted`

Source lines 924–926. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
    def counted(*args: object, **kwargs: object) -> None:
```

Nested no-op replacement for the heavy policy-owner validator in test_malformed_local_result_fast_fails_before_heavy_validation. Increment captured calls and return None; no delegation or source I/O. Parent asserts calls==0 after local/lock rejection; fixture work precedes installation.

<a id="symbol-test-coordinated-application-source-lock-mutation-fast-fails"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_coordinated_application_source_lock_mutation_fast_fails`

Source lines 939–969. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_coordinated_application_source_lock_mutation_fast_fails(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

Change policy_sha256 scalar and all row suffix hashes to valid-looking foreign digest, rehash application; no-op counted source owner remains uncalled. Full validator requires source-lock error/calls0, separating internal consistency from external identity.

<a id="symbol-test-coordinated-application-source-lock-mutation-fast-fails-counted"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_coordinated_application_source_lock_mutation_fast_fails.counted`

Source lines 948–950. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
    def counted(*args: object, **kwargs: object) -> None:
```

Nested no-op replacement for the heavy policy-owner validator in test_coordinated_application_source_lock_mutation_fast_fails. Increment captured calls and return None; no delegation or source I/O. Parent asserts calls==0 after local/lock rejection; fixture work precedes installation.

<a id="symbol-test-valid-four-file-manifest-and-verified-byte-readback"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_valid_four_file_manifest_and_verified_byte_readback`

Source lines 972–988. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_valid_four_file_manifest_and_verified_byte_readback(tmp_path: Path) -> None:
```

Write synthetic artifacts, load through five-path test adapter using fixture globals, compare all three GeoDataFrames and relations with assertion helpers, then invoke full source-complete validator on loaded result. Readback itself is lightweight; final explicit validation is the heavy call.

<a id="symbol-test-duplicate-relation-pair-artifact-fails-local-loading"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_duplicate_relation_pair_artifact_fails_local_loading`

Source lines 991–1006. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_duplicate_relation_pair_artifact_fails_local_loading(tmp_path: Path) -> None:
```

Write duplicated first relation (retained duplicate index) plus updated application hashes/manifest. Adapter loader rejects duplicate/unique locally; broad guard match does not uniquely isolate pair check.

<a id="symbol-test-document-wide-mapping-conflict-artifact-fails-local-loading"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_document_wide_mapping_conflict_artifact_fails_local_loading`

Source lines 1009–1032. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_document_wide_mapping_conflict_artifact_fails_local_loading(
    tmp_path: Path,
) -> None:
```

Forge status/priority contradiction consistently across referenced object and relations, reseal/write artifacts; loader rejects priority/mapping. Common catalog mapping includes all objects, not only a selected parcel.

<a id="symbol-test-positive-surface-overlap-cannot-be-relabelled-touch-only-in-artifact"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_positive_surface_overlap_cannot_be_relabelled_touch_only_in_artifact`

Source lines 1035–1050. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_positive_surface_overlap_cannot_be_relabelled_touch_only_in_artifact(
    tmp_path: Path,
) -> None:
```

Write helper-forged positive surface area with TOUCH_ONLY, require loader surface/metric/type error. Stored relation metrics, not a new overlay computation in loader, establish contradiction.

<a id="symbol-test-wrong-2d-feature-geometry-fails-local-artifact-loading"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_wrong_2d_feature_geometry_fails_local_artifact_loading`

Source lines 1053–1069. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_wrong_2d_feature_geometry_fails_local_artifact_loading(tmp_path: Path) -> None:
```

Replace surface geometry with 2D Point, rehash and write byte-sealed artifacts; loader raises surface/geometry. Exactly2D alone is insufficient: role geometry type matters.

<a id="symbol-test-feature-catalog-geometry-role-is-intrinsic"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_feature_catalog_geometry_role_is_intrinsic`

Source lines 1086–1097. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_feature_catalog_geometry_role_is_intrinsic(
    frame_name: str, geometry: object
) -> None:
```

Five local cases: wrong type in each role, empty Polygon, invalid bowtie Polygon. Replace copied geometry/reseal, local envelope must reject geometry. No geometry repair; CRS remains synthetic canonical.

Exact decorators/parametrization (not extra closure units):

```python
@pytest.mark.parametrize(
    ("frame_name", "geometry"),
    [
        ("surface_features", Point(0, 0)),
        ("line_features", Polygon([(0, 0), (1, 0), (1, 1), (0, 0)])),
        ("point_features", LineString([(0, 0), (1, 1)])),
        ("surface_features", Polygon()),
        (
            "surface_features",
            Polygon([(0, 0), (2, 2), (0, 2), (2, 0), (0, 0)]),
        ),
    ],
    ids=["surface-point", "line-polygon", "point-line", "empty", "invalid"],
)
```

<a id="symbol-test-feature-catalog-metric-must-match-geometry"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_feature_catalog_metric_must_match_geometry`

Source lines 1108–1121. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_feature_catalog_metric_must_match_geometry(
    frame_name: str, metric: str
) -> None:
```

For surface area/line length/point member count perturb catalog metric and reseal; local envelope rejects metric/geometry/count. Tests measured source metric agreement for all three roles.

Exact decorators/parametrization (not extra closure units):

```python
@pytest.mark.parametrize(
    ("frame_name", "metric"),
    [
        ("surface_features", "feature_area_m2"),
        ("line_features", "feature_length_m"),
        ("point_features", "point_member_count"),
    ],
)
```

<a id="symbol-test-unreferenced-feature-catalog-identity-fields-are-intrinsic"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_unreferenced_feature_catalog_identity_fields_are_intrinsic`

Source lines 1132–1146. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_unreferenced_feature_catalog_identity_fields_are_intrinsic(
    column: str, value: str
) -> None:
```

Find first unreferenced feature, copy it, mutate GPU ID/logical layer/geometry kind in three cases, reseal, local envelope rejects identity/layer/kind. Absence of relations does not bypass catalog validation.

Exact decorators/parametrization (not extra closure units):

```python
@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("planning_feature_id", "GPU:malformed"),
        ("logical_layer", "prescription_line"),
        ("geometry_kind", "LINE"),
    ],
)
```

<a id="symbol-test-feature-catalog-requires-canonical-crs-and-global-identity"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_feature_catalog_requires_canonical_crs_and_global_identity`

Source lines 1149–1166. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_feature_catalog_requires_canonical_crs_and_global_identity() -> None:
```

Two local cases: reproject a surface copy with to_crs(EPSG:4326), then duplicate cross-catalog feature ID; reseal, require CRS and identity/unique failures respectively. GPU namespace mismatch may precede global duplicate guard in second case.

<a id="symbol-test-unreferenced-feature-identity-is-validated-locally"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_unreferenced_feature_identity_is_validated_locally`

Source lines 1170–1191. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_unreferenced_feature_identity_is_validated_locally(
    tmp_path: Path, feature_id: str
) -> None:
```

Four invalid unreferenced feature IDs (textualNone,absolute POSIX/Windows,padded) written to artifacts after reseal; loader rejects feature/identity/GPU. No relation references are needed to trigger catalog integrity checks.

Exact decorators/parametrization (not extra closure units):

```python
@pytest.mark.parametrize("feature_id", ["None", "/tmp/feature", r"C:\feature", " bad "])
```

<a id="symbol-test-unreferenced-feature-participates-in-global-policy-mapping"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_unreferenced_feature_participates_in_global_policy_mapping`

Source lines 1194–1221. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_unreferenced_feature_participates_in_global_policy_mapping(
    tmp_path: Path,
) -> None:
```

Give unreferenced applied object a conflicting priority, reseal/write, loader rejects priority/mapping. Tests document-wide mapping including zero-relation feature, not parcel priority selection.

<a id="symbol-test-application-locks-policy-result-schema-exactly"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_application_locks_policy_result_schema_exactly`

Source lines 1225–1234. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_application_locks_policy_result_schema_exactly(policy_schema: int) -> None:
```

Replace upstream policy result version on application result with0/2/999, reseal then local envelope raises policy-schema. Tests these integral versions, not every bool/float coercion possibility.

Exact decorators/parametrization (not extra closure units):

```python
@pytest.mark.parametrize("policy_schema", [0, 2, 999])
```

<a id="symbol-test-application-locks-cnig-result-schema-exactly"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_application_locks_cnig_result_schema_exactly`

Source lines 1238–1247. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_application_locks_cnig_result_schema_exactly(cnig_schema: int) -> None:
```

Replace application CNIG result version with1/4/6/999, reseal then local envelope raises CNIG/schema. Does not alter actual coded upstream or test all scalar Python types.

Exact decorators/parametrization (not extra closure units):

```python
@pytest.mark.parametrize("cnig_schema", [1, 4, 6, 999])
```

<a id="symbol-test-application-accepts-only-current-policy-and-cnig-source-schemas"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_application_accepts_only_current_policy_and_cnig_source_schemas`

Source lines 1250–1257. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_application_accepts_only_current_policy_and_cnig_source_schemas() -> None:
```

Assert valid fixture application holds policy version1 and CNIG version5 and local envelope returns normally. Two version assertions, not exhaustive type-rejection coverage.

<a id="symbol-test-duplicate-relation-identity-fast-fails-before-policy-source-validation"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_duplicate_relation_identity_fast_fails_before_policy_source_validation`

Source lines 1260–1283. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_duplicate_relation_identity_fast_fails_before_policy_source_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

Concatenate duplicate relation THEN reset to unnamed int64 unique Index; reseal, install no-op heavy counter, full validator rejects duplicate/unique and calls0. More precise pair-identity evidence than the retained-duplicate-index cases.

<a id="symbol-test-duplicate-relation-identity-fast-fails-before-policy-source-validation-counted"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_duplicate_relation_identity_fast_fails_before_policy_source_validation.counted`

Source lines 1274–1276. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
    def counted(*args: object, **kwargs: object) -> None:
```

Nested no-op replacement for the heavy policy-owner validator in test_duplicate_relation_identity_fast_fails_before_policy_source_validation. Increment captured calls and return None; no delegation or source I/O. Parent asserts calls==0 after local/lock rejection; fixture work precedes installation.

<a id="symbol-test-self-consistent-z-geoparquet-artifact-is-rejected"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_self_consistent_z_geoparquet_artifact_is_rejected`

Source lines 1286–1302. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_self_consistent_z_geoparquet_artifact_is_rejected(tmp_path: Path) -> None:
```

Write Z surface using result replacement with existing semantic digests; helper regenerates physical sizes/SHAs/schema in manifest. Loader raises2D/dimension before digest comparison. Byte-consistent artifact metadata is NOT proof all semantic hashes were recomputed.

<a id="symbol-test-self-consistent-wrong-dtype-artifact-is-rejected"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_self_consistent_wrong_dtype_artifact_is_rejected`

Source lines 1305–1321. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_self_consistent_wrong_dtype_artifact_is_rejected(tmp_path: Path) -> None:
```

Coordinated status=UNKNOWN/object dtype mutation in catalog and relations through helper, with application hashes recomputed; write physical Parquet metadata and require loader dtype/schema error. The representation is invalid despite internally resealed digests; this is not a stale-hash-only test.

<a id="symbol-test-artifact-manifest-rejects-invalid-contract"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_artifact_manifest_rejects_invalid_contract`

Source lines 1371–1391. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_artifact_manifest_rejects_invalid_contract(
    tmp_path: Path,
    mutation: object,
    message: str,
) -> None:
```

Sixteen literal manifest mutations cover version/missing-extra-duplicate role records, bad/mismatched/duplicate filenames, size/SHA/rows/schema/CRS/geoflag/unknownfield. Write mutated JSON; adapter loader raises parameter-specific application error. No permutation of two otherwise-valid ordered records is present; some cases fail Pydantic before artifact reads.

Exact decorators/parametrization (not extra closure units):

```python
@pytest.mark.parametrize(
    ("mutation", "message"),
    [
        (lambda value: value.update(schema_version=1), "schema"),
        (lambda value: value["artifacts"].pop(), "role|artifact"),
        (
            lambda value: value["artifacts"].append(
                {**value["artifacts"][0], "artifact_role": "EXTRA"}
            ),
            "role|artifact",
        ),
        (
            lambda value: value["artifacts"].append(dict(value["artifacts"][0])),
            "duplicate|role|artifact",
        ),
        (
            lambda value: value["artifacts"][0].update(filename="wrong.parquet"),
            "filename",
        ),
        (
            lambda value: value["artifacts"][1].update(
                filename=value["artifacts"][0]["filename"]
            ),
            "duplicate|filename",
        ),
        (
            lambda value: value["artifacts"][0].update(
                filename="C:/absolute/surface.parquet"
            ),
            "filename",
        ),
        (lambda value: value["artifacts"][0].update(size_bytes=1), "size"),
        (lambda value: value["artifacts"][0].update(sha256="f" * 64), "SHA|hash"),
        (lambda value: value["artifacts"][0].update(sha256="bad"), "SHA|hash"),
        (lambda value: value["artifacts"][0].update(row_count=999), "row"),
        (
            lambda value: value["artifacts"][0]["frame_schema_signature"].update(
                index_names=["wrong"]
            ),
            "schema",
        ),
        (lambda value: value["artifacts"][0].update(crs={"wrong": True}), "CRS|crs"),
        (lambda value: value["artifacts"][0].update(crs=None), "CRS|crs"),
        (lambda value: value["artifacts"][0].update(geospatial=False), "geospatial"),
        (lambda value: value.update(unknown=True), "manifest|artifact"),
    ],
)
```

<a id="symbol-test-application-manifest-uses-strict-json-before-artifact-read"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_application_manifest_uses_strict_json_before_artifact_read`

Source lines 1404–1442. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_application_manifest_uses_strict_json_before_artifact_read(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    document: str,
) -> None:
```

Four documents: duplicate schema key,NaN,Infinity,non-object array. Replace manifest text; patch Path.read_bytes with delegating artifact-conditional counter and module.pd.read_parquet with one increment-and-raise sentinel; loader must raise strictJSON/invalid error and shared artifact_reads0. Manifest bytes are deliberately excluded from artifact counter.

Exact decorators/parametrization (not extra closure units):

```python
@pytest.mark.parametrize(
    "document",
    [
        '{"schema_version": 2, "schema_version": 2}\n',
        '{"schema_version": NaN}\n',
        '{"schema_version": Infinity}\n',
        "[]\n",
    ],
    ids=["duplicate-key", "nan", "infinity", "non-object"],
)
```

<a id="symbol-test-application-manifest-uses-strict-json-before-artifact-read-counted-bytes"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_application_manifest_uses_strict_json_before_artifact_read.counted_bytes`

Source lines 1418–1422. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
    def counted_bytes(path: Path) -> bytes:
```

Nested Path.read_bytes spy: increment shared artifact_reads only if path is one of four artifact Paths, then delegate to original_read_bytes. Manifest read excluded. Combined with Parquet sentinel; parent asserts shared artifact_reads0, not separate counters.

<a id="symbol-test-application-manifest-uses-strict-json-before-artifact-read-counted"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_application_manifest_uses_strict_json_before_artifact_read.counted`

Source lines 1424–1427. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
    def counted(*args: object, **kwargs: object) -> object:
```

Nested module.pd.read_parquet sentinel: increment shared artifact_reads then raise AssertionError; DOES NOT delegate and is not installed on gpd.read_parquet. Parent expects strict JSON failure before this sentinel and artifact read_bytes calls.

<a id="symbol-test-artifact-loader-parses-only-verified-bytes"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_artifact_loader_parses_only_verified_bytes`

Source lines 1445–1488. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_artifact_loader_parses_only_verified_bytes(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

Capture original relation Parquet bytes; patched read_bytes replaces its path immediately after returning captured payload, while patched pd.read_parquet records BytesIO and delegates. Assert replacement occurred, observed buffer matches verified bytes, and loaded relation frame equals original. Does not assert path unchanged or a post-read path-integrity guarantee.

<a id="symbol-test-artifact-loader-parses-only-verified-bytes-replace-after-read"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_artifact_loader_parses_only_verified_bytes.replace_after_read`

Source lines 1464–1470. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
    def replace_after_read(path: Path) -> bytes:
```

Nested Path.read_bytes spy: first obtain actual payload; for target relation file once, overwrite path with precreated replacement bytes and set replaced=True; return original captured payload. Deliberate synthetic filesystem mutation after capture; no claim of path stability.

<a id="symbol-test-artifact-loader-parses-only-verified-bytes-observed-read"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_artifact_loader_parses_only_verified_bytes.observed_read`

Source lines 1472–1475. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
    def observed_read(source: object, *args: object, **kwargs: object) -> object:
```

Nested pd.read_parquet spy: if passed BytesIO, append (buffer,getvalue()) to observed, then delegate actual_read_parquet with original arguments. Return parsed frame; no replacement of byte stream.

<a id="symbol-test-physical-replacement-before-loading-is-rejected"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_physical_replacement_before_loading_is_rejected`

Source lines 1491–1502. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_physical_replacement_before_loading_is_rejected(tmp_path: Path) -> None:
```

Append tamper bytes to relation file before load, without updating manifest; loader fails size/SHA/hash (size is first applicable guard). No atomic-read or after-capture guarantee is tested.

<a id="symbol-test-public-application-api-exports-only-stable-symbols"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_public_application_api_exports_only_stable_symbols`

Source lines 1505–1520. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_public_application_api_exports_only_stable_symbols() -> None:
```

Assert module.__all__ equals exact seven-name set, package exports include it, and module exports contain no underscore names. Record importability is not public export; package has other component exports.

<a id="symbol--replace-application-frame"></a>
### `tests.unit.test_apply_bess_planning_feature_policy._replace_application_frame`

Source lines 1523–1531. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def _replace_application_frame(
    result: BessPlanningFeatureApplicationResult,
    frame_name: str,
    frame: pd.DataFrame,
) -> BessPlanningFeatureApplicationResult:
```

Replace named result frame with supplied object and call application _result_with_hashes; return resealed result. Does not copy supplied frame or validate upstream provenance; callers copy before mutation.

<a id="symbol--coordinated-referenced-lineage-mutation"></a>
### `tests.unit.test_apply_bess_planning_feature_policy._coordinated_referenced_lineage_mutation`

Source lines 1534–1565. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def _coordinated_referenced_lineage_mutation(
    result: BessPlanningFeatureApplicationResult,
    column: str,
    value: str,
    *,
    rename_id: bool = False,
) -> BessPlanningFeatureApplicationResult:
```

Select first relation feature; copy catalogs/relations, update named source lineage field on both, optionally regenerate GPU feature ID for altered document, then reseal. Returns coordinated forgery for envelope lineage guards; no physical source changes.

<a id="symbol-test-unreferenced-feature-document-lineage-is-bound-to-envelope-artifact"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_unreferenced_feature_document_lineage_is_bound_to_envelope_artifact`

Source lines 1568–1588. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_unreferenced_feature_document_lineage_is_bound_to_envelope_artifact(
    tmp_path: Path,
) -> None:
```

Alter unreferenced object document and regenerate its GPU ID consistently, reseal/write, loader rejects document/lineage. Coherent ID does not bypass envelope document authority.

<a id="symbol-test-feature-row-lineage-must-match-application-envelope"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_feature_row_lineage_must_match_application_envelope`

Source lines 1595–1614. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_feature_row_lineage_must_match_application_envelope(mutation: str) -> None:
```

Three local mutations: row archive SHA, official profile AND its SHA, or envelope document ID; reseal and require lineage/document error. Does not need actual GPU read to reject these internal inconsistencies.

Exact decorators/parametrization (not extra closure units):

```python
@pytest.mark.parametrize(
    "mutation",
    ["archive", "official-profile", "envelope-document"],
)
```

<a id="symbol-test-coordinated-referenced-row-lineage-cannot-bypass-envelope"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_coordinated_referenced_row_lineage_cannot_bypass_envelope`

Source lines 1624–1637. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_coordinated_referenced_row_lineage_cannot_bypass_envelope(
    column: str,
    value: str,
    rename_id: bool,
) -> None:
```

Mutate document+GPU ID or archive consistently across referenced catalog/relations, rehash; local envelope still rejects lineage/document against envelope scalar. Guards are not limited to pairwise row agreement.

Exact decorators/parametrization (not extra closure units):

```python
@pytest.mark.parametrize(
    ("column", "value", "rename_id"),
    [
        ("source_document_id", "MUTATED-DOCUMENT", True),
        ("source_archive_sha256", "f" * 64, False),
    ],
)
```

<a id="symbol-test-resolved-official-row-requires-label-and-envelope-profile"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_resolved_official_row_requires_label_and_envelope_profile`

Source lines 1640–1656. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_resolved_official_row_requires_label_and_envelope_profile() -> None:
```

On unreferenced resolved row, separately null official label or change profile; local envelope rejects official/profile/label. Both label completeness and envelope lineage remain required without a relation.

<a id="symbol-test-unknown-official-row-rejects-invented-label-or-url"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_unknown_official_row_rejects_invented_label_or_url`

Source lines 1659–1689. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_unknown_official_row_rejects_invented_label_or_url() -> None:
```

Prepare unknown unreferenced row with all official meaning and decision values null, then invent official label or URL in two iterations; rehash and require official/null error. Unknown meaning is not a place for synthetic explanations.

<a id="symbol-test-application-feature-prefix-has-exact-canonical-schema"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_application_feature_prefix_has_exact_canonical_schema`

Source lines 1707–1749. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_application_feature_prefix_has_exact_canonical_schema(
    frame_name: str,
    mutation: str,
) -> None:
```

Ten role/mutation combinations: missing/extra/reordered prefix, object area/length/count, object official code, index name/int32, malformed empty point. Reseal then envelope raises schema/dtype/index. All-null optional raw variants have separate scenario; no prefix normalization is done here.

Exact decorators/parametrization (not extra closure units):

```python
@pytest.mark.parametrize(
    ("frame_name", "mutation"),
    [
        ("surface_features", "missing-column"),
        ("surface_features", "unexpected-column"),
        ("surface_features", "reordered-columns"),
        ("surface_features", "metric-object"),
        ("line_features", "metric-object"),
        ("point_features", "metric-object"),
        ("surface_features", "official-object"),
        ("surface_features", "index-name"),
        ("surface_features", "index-dtype"),
        ("point_features", "malformed-empty"),
    ],
)
```

<a id="symbol-test-application-relation-prefix-has-exact-canonical-schema"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_application_relation_prefix_has_exact_canonical_schema`

Source lines 1764–1797. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_application_relation_prefix_has_exact_canonical_schema(
    mutation: str,
) -> None:
```

Seven mutations: missing/extra/reordered factual columns, object float/count, categorical official status, malformed empty relations. Reseal; local envelope schema/dtype failure. Empty frames still require exact schema.

Exact decorators/parametrization (not extra closure units):

```python
@pytest.mark.parametrize(
    "mutation",
    [
        "missing-column",
        "unexpected-column",
        "reordered-columns",
        "float-object",
        "count-object",
        "official-category",
        "malformed-empty",
    ],
)
```

<a id="symbol-test-self-consistent-factual-prefix-dtype-artifact-is-rejected"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_self_consistent_factual_prefix_dtype_artifact_is_rejected`

Source lines 1800–1817. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_self_consistent_factual_prefix_dtype_artifact_is_rejected(
    tmp_path: Path,
) -> None:
```

Cast surface area to object and write artifact with measured metadata. Require loader schema/dtype rejection; Parquet may roundtrip numeric object back to float so record-vs-measured signature mismatch can precede intrinsic schema guard. Regex does not isolate the latter.

<a id="symbol-test-lineage-defect-fast-fails-before-policy-source-validation"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_lineage_defect_fast_fails_before_policy_source_validation`

Source lines 1820–1842. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_lineage_defect_fast_fails_before_policy_source_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

Coordinated referenced document mutation (including ID), no-op heavy counter; full validator raises application error and calls0. Broad raises proves local stopping, not one selected error message.

<a id="symbol-test-lineage-defect-fast-fails-before-policy-source-validation-counted"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_lineage_defect_fast_fails_before_policy_source_validation.counted`

Source lines 1829–1831. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
    def counted(*args: object, **kwargs: object) -> None:
```

Nested no-op replacement for the heavy policy-owner validator in test_lineage_defect_fast_fails_before_policy_source_validation. Increment captured calls and return None; no delegation or source I/O. Parent asserts calls==0 after local/lock rejection; fixture work precedes installation.

<a id="symbol-test-step-7d-5b-2b-5-application-loader-requires-exact-upstreams"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_step_7d_5b_2b_5_application_loader_requires_exact_upstreams`

Source lines 1845–1868. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_step_7d_5b_2b_5_application_loader_requires_exact_upstreams() -> None:
```

Inspect real loader signature and assert ordered seven parameter NAMES, not default values; assert public envelope validator exists, validate good result and reject bad complete hash. The test-only adapter signature is not the public contract.

<a id="symbol-test-source-bound-application-loader-rejects-locally-valid-rationale-change"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_source_bound_application_loader_rejects_locally_valid_rationale_change`

Source lines 1871–1894. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_source_bound_application_loader_rejects_locally_valid_rationale_change(
    tmp_path: Path,
) -> None:
```

Coherently mutate catalog+relation rationale/reseal; explicitly validate local envelope successfully; write and call real loader with exact coded/policy upstreams, expecting upstream/rebuilt failure. Shows local self-consistency is not source-content equivalence.

<a id="symbol-test-application-manifest-filenames-are-casefold-unique"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_application_manifest_filenames_are_casefold_unique`

Source lines 1897–1904. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_application_manifest_filenames_are_casefold_unique(tmp_path: Path) -> None:
```

Change second filename to uppercase first basename in in-memory manifest payload; Pydantic model_validate raises ValueError filename/duplicate. No public loader wrapping or artifact reread is involved.

<a id="symbol--swap-referenced-feature-values"></a>
### `tests.unit.test_apply_bess_planning_feature_policy._swap_referenced_feature_values`

Source lines 1907–1945. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def _swap_referenced_feature_values(
    result: BessPlanningFeatureApplicationResult,
    columns: tuple[str, ...],
) -> BessPlanningFeatureApplicationResult:
```

Choose two referenced APPLIED objects with distinct statuses, swap specified columns in copies of all catalogs/relations, reseal application. ID identities retained. Used for coordinated valid-domain policy/official text swaps; no upstream source rebuild.

<a id="symbol-test-source-bound-loader-rejects-valid-domain-cross-pair-swaps"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_source_bound_loader_rejects_valid_domain_cross_pair_swaps`

Source lines 1967–1998. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_source_bound_loader_rejects_valid_domain_cross_pair_swaps(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    columns: tuple[str, ...],
) -> None:
```

Two column groups (six decisions or four official meanings) swapped coherently; local envelope explicitly passes; real seven-argument loader rejects upstream mismatch. No-op heavy callback remains calls0. Does not assert heavy validator would accept the forgery.

Exact decorators/parametrization (not extra closure units):

```python
@pytest.mark.parametrize(
    "columns",
    [
        (
            "bess_cnig_precheck_status",
            "bess_cnig_precheck_confidence",
            "bess_cnig_status_priority",
            "bess_cnig_rationale",
            "bess_cnig_required_human_action",
            "bess_cnig_limitations",
        ),
        (
            "official_code_label",
            "official_legal_reference",
            "official_regulation_reference",
            "official_code_source_url",
        ),
    ],
)
```

<a id="symbol-test-source-bound-loader-rejects-valid-domain-cross-pair-swaps-forbidden-heavy"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_source_bound_loader_rejects_valid_domain_cross_pair_swaps.forbidden_heavy`

Source lines 1981–1983. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
    def forbidden_heavy(*args: object, **kwargs: object) -> None:
```

Despite name, callback only increments heavy_calls and returns None; it does not raise or delegate. Parent asserts zero during lightweight source-bound artifact rejection.

<a id="symbol-test-source-bound-loader-rejects-factual-prefix-lineage-change"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_source_bound_loader_rejects_factual_prefix_lineage_change`

Source lines 2002–2017. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_source_bound_loader_rejects_factual_prefix_lineage_change(
    tmp_path: Path, column: str
) -> None:
```

Change surface source_provider or source_portal, reseal; envelope passes because these are not22 agreement fields, then real loader rejects upstream reconstruction. Complete prefix comparison supplies binding not duplicated by local row guards.

Exact decorators/parametrization (not extra closure units):

```python
@pytest.mark.parametrize("column", ["source_provider", "source_portal"])
```

<a id="symbol-test-source-bound-loader-rejects-all-null-raw-column-transition"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_source_bound_loader_rejects_all_null_raw_column_transition`

Source lines 2020–2093. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_source_bound_loader_rejects_all_null_raw_column_transition(
    tmp_path: Path,
) -> None:
```

First forge coded surface text and corresponding relations, reseal coded+policy lineage and privately build application; mutate surface text to all-null object and relation text to null str, reseal. Envelope passes allowed schema variant, real loader rejects changed upstream content. Second subscenario reverses surface rows, writes separate directory and again requires upstream rejection after envelope passes. Row-order proof is HERE, not in next title.

<a id="symbol-test-source-bound-loader-rejects-unreferenced-feature-and-row-reordering"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_source_bound_loader_rejects_unreferenced_feature_and_row_reordering`

Source lines 2096–2114. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_source_bound_loader_rejects_unreferenced_feature_and_row_reordering(
    tmp_path: Path,
) -> None:
```

Actual body only copies unreferenced feature, changes label_raw, reseals, validates envelope, writes separate directory and requires real loader upstream error. Despite name no row reordering occurs here; preceding all-null test covers reversal.

<a id="symbol-test-application-loader-validates-upstreams-and-rebuilds-once-lightweight"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_application_loader_validates_upstreams_and_rebuilds_once_lightweight`

Source lines 2117–2167. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_application_loader_validates_upstreams_and_rebuilds_once_lightweight(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

After fixture/files, install delegating coded-envelope,policy-envelope,build spies and no-op heavy counter. Real loader succeeds, complete digest matches, counts exactly coded1/policy1/build1/heavy0; assert coded.surface_features and policy.policy_table unchanged. Does not assert all upstream frames or physical read count.

<a id="symbol-test-application-loader-validates-upstreams-and-rebuilds-once-lightweight-coded-envelope"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_application_loader_validates_upstreams_and_rebuilds_once_lightweight.coded_envelope`

Source lines 2134–2136. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
    def coded_envelope(value: object) -> None:
```

Nested one-value delegating spy: increment calls[coded], invoke actual_coded_envelope(value), then return None implicitly. Parent asserts this envelope owner invoked once, not a physical-file count.

<a id="symbol-test-application-loader-validates-upstreams-and-rebuilds-once-lightweight-policy-envelope"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_application_loader_validates_upstreams_and_rebuilds_once_lightweight.policy_envelope`

Source lines 2138–2140. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
    def policy_envelope(value: object) -> None:
```

Nested one-value delegating spy: increment calls[policy], invoke actual_policy_envelope(value), then return None implicitly. Parent asserts this envelope owner invoked once, not a physical-file count.

<a id="symbol-test-application-loader-validates-upstreams-and-rebuilds-once-lightweight-build"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_application_loader_validates_upstreams_and_rebuilds_once_lightweight.build`

Source lines 2142–2144. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
    def build(*args: object, **kwargs: object) -> object:
```

Nested delegating spy: increment calls[build] and return actual_build(*args,**kwargs). Parent asserts this owner invoked once; count is not physical-file count.

<a id="symbol-test-application-loader-validates-upstreams-and-rebuilds-once-lightweight-heavy"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_application_loader_validates_upstreams_and_rebuilds_once_lightweight.heavy`

Source lines 2146–2147. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
    def heavy(*args: object, **kwargs: object) -> None:
```

Nested no-op policy-owner replacement increments calls[heavy], no delegation/raise; parent expects zero. It does not simulate successful physical validation.

<a id="symbol-test-application-loader-rejects-bad-upstream-before-artifact-reads"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_application_loader_rejects_bad_upstream_before_artifact_reads`

Source lines 2170–2187. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_application_loader_rejects_bad_upstream_before_artifact_reads(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

Invalidate coded complete digest, patch ALL Path.read_bytes with delegating count spy, real loader raises broad Exception matching hash/SHA/invalid and reads0. Proves no such reads during instrumented call, not specific exception subclass or fixture no-I/O.

<a id="symbol-test-application-loader-rejects-bad-upstream-before-artifact-reads-counted"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_application_loader_rejects_bad_upstream_before_artifact_reads.counted`

Source lines 2178–2181. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
    def counted(path: Path) -> bytes:
```

Nested Path.read_bytes spy increments reads for every path and delegates original(path), returning bytes. Parent asserts zero after bad upstream failure; no independent count for manifest versus artifacts.

<a id="symbol-test-application-manifest-rejects-nonportable-filename"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_application_manifest_rejects_nonportable_filename`

Source lines 2229–2236. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_application_manifest_rejects_nonportable_filename(
    tmp_path: Path, filename: str
) -> None:
```

Thirty-four literal unsafe filename values cover POSIX/Windows paths, reserved names including superscript ports, forbidden separators/characters/controls. In-memory manifest validation raises ValueError filename/basename/portable; no filesystem or loader invocation for the rejection itself.

Exact decorators/parametrization (not extra closure units):

```python
@pytest.mark.parametrize(
    "filename",
    [
        "/tmp/file.parquet",
        "../file.parquet",
        "subdir/file.parquet",
        r"C:\absolute\file.parquet",
        "C:/absolute/file.parquet",
        r"\\server\share\file.parquet",
        r"subdir\file.parquet",
        "CON.parquet",
        "con.PARQUET",
        "NUL.parquet",
        "PRN.parquet",
        "AUX.parquet",
        "CLOCK$.parquet",
        "COM1.parquet",
        "COM9.parquet",
        "LPT1.parquet",
        "LPT9.parquet",
        "COM¹.parquet",
        "COM².parquet",
        "COM³.parquet",
        "LPT¹.parquet",
        "LPT².parquet",
        "LPT³.parquet",
        "file:name.parquet",
        "base.parquet:stream.parquet",
        "file?.parquet",
        "file*.parquet",
        "file<.parquet",
        "file>.parquet",
        "file|.parquet",
        'file".parquet',
        "nul\x00.parquet",
        "line\nbreak.parquet",
        "del\x7f.parquet",
    ],
)
```

<a id="symbol--compatible-policy-mutation"></a>
### `tests.unit.test_apply_bess_planning_feature_policy._compatible_policy_mutation`

Source lines 2239–2281. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def _compatible_policy_mutation(policy: object, mutation: str) -> object:
```

Deep-copy table and forge one of eleven version/key/text/source identities, update associated row lineage where applicable and use policy-owner _result_with_hashes. Return resealed policy; schema-profile3 may fail upstream envelope before compatibility helper. Extra98 pair/missing last pair preserve canonical index/order setup. No configs/GPU are revalidated.

<a id="symbol-test-application-loader-rejects-incompatible-upstreams-before-io-or-rebuild"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild`

Source lines 2300–2339. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    mutation: str,
) -> None:
```

Eleven forged upstream mutations, real loader expected application error with broad policy/CNIG/source/schema/text regex and four counters0. Artifact reader/build are increment-and-raise sentinels; heavy no-op. Manifest sentinel patches Path.read_text whereas actual loader uses read_bytes: that counter alone cannot prove no manifest I/O. Source guard order supports pre-read failure; some mutations fail upstream envelope earlier than pair-compatibility.

Exact decorators/parametrization (not extra closure units):

```python
@pytest.mark.parametrize(
    "mutation",
    [
        "profile-schema",
        "extra-pair",
        "missing-pair",
        "official-label",
        "legal-reference",
        "regulation-reference",
        "document",
        "archive",
        "profile",
        "profile-sha",
        "complete-result-sha",
    ],
)
```

<a id="symbol-test-application-loader-rejects-incompatible-upstreams-before-io-or-rebuild-manifest-read"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild.manifest_read`

Source lines 2313–2315. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
    def manifest_read(*args: object, **kwargs: object) -> str:
```

Nested increment-and-raise AssertionError sentinel installed on Path.read_text, returning no value despite str annotation. Production uses read_bytes, so zero calls alone does not instrument real manifest reads. Parent/source-order evidence must remain distinct.

<a id="symbol-test-application-loader-rejects-incompatible-upstreams-before-io-or-rebuild-read"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild.read`

Source lines 2317–2319. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
    def read(*args: object, **kwargs: object) -> object:
```

Nested artifact-reader sentinel increments calls[read] then raises AssertionError; no delegation/Parquet parsing. Parent asserts zero after upstream rejection.

<a id="symbol-test-application-loader-rejects-incompatible-upstreams-before-io-or-rebuild-build"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild.build`

Source lines 2321–2323. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
    def build(*args: object, **kwargs: object) -> object:
```

Nested private-builder sentinel increments calls[build] then raises AssertionError; no delegation/reconstruction. Parent asserts zero after upstream rejection.

<a id="symbol-test-application-loader-rejects-incompatible-upstreams-before-io-or-rebuild-heavy"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild.heavy`

Source lines 2325–2326. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
    def heavy(*args: object, **kwargs: object) -> None:
```

Nested no-op heavy policy validator increments calls[heavy] and returns None; does not raise/delegate. Parent asserts zero; fixture validation occurred earlier.

<a id="symbol-test-application-loader-rejects-empty-upstreams-before-any-io-or-rebuild"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild`

Source lines 2343–2397. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
def test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    empty_upstream: str,
) -> None:
```

Three cases empty coded dictionary,empty policy table,both; canonical empty helpers reseal and both-case updates policy coded digest. Real loader rejects dictionary/policy/table/pair/empty/record/entry with all counters0. Upstream envelope nonempty guards may fire before compatibility. Same read_text-versus-read_bytes manifest instrumentation limitation; artifact/build sentinels and heavy counter remain correctly scoped.

Exact decorators/parametrization (not extra closure units):

```python
@pytest.mark.parametrize("empty_upstream", ["coded", "policy", "both"])
```

<a id="symbol-test-application-loader-rejects-empty-upstreams-before-any-io-or-rebuild-manifest-read"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild.manifest_read`

Source lines 2371–2373. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
    def manifest_read(*args: object, **kwargs: object) -> str:
```

Nested increment-and-raise AssertionError sentinel installed on Path.read_text, returning no value despite str annotation. Production uses read_bytes, so zero calls alone does not instrument real manifest reads. Parent/source-order evidence must remain distinct.

<a id="symbol-test-application-loader-rejects-empty-upstreams-before-any-io-or-rebuild-artifact-read"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild.artifact_read`

Source lines 2375–2377. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
    def artifact_read(*args: object, **kwargs: object) -> object:
```

Nested artifact-reader sentinel increments calls[read] then raises AssertionError; no delegation/Parquet parsing. Parent asserts zero after upstream rejection.

<a id="symbol-test-application-loader-rejects-empty-upstreams-before-any-io-or-rebuild-build"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild.build`

Source lines 2379–2381. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
    def build(*args: object, **kwargs: object) -> object:
```

Nested private-builder sentinel increments calls[build] then raises AssertionError; no delegation/reconstruction. Parent asserts zero after upstream rejection.

<a id="symbol-test-application-loader-rejects-empty-upstreams-before-any-io-or-rebuild-heavy"></a>
### `tests.unit.test_apply_bess_planning_feature_policy.test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild.heavy`

Source lines 2383–2384. Kind: function. Owner: `tests.unit.test_apply_bess_planning_feature_policy`.

```python
    def heavy(*args: object, **kwargs: object) -> None:
```

Nested no-op heavy policy validator increments calls[heavy] and returns None; does not raise/delegate. Parent asserts zero; fixture validation occurred earlier.

## Complete source snapshot

One exact full source snapshot follows. Byte equality does not substitute for the semantic explanations above.

```python
from __future__ import annotations

import importlib
import inspect
import json
from collections.abc import Mapping
from dataclasses import fields, replace
from hashlib import sha256
from io import BytesIO
from pathlib import Path

import geopandas as gpd
import pandas as pd
import pytest
from geopandas.testing import assert_geodataframe_equal
from pandas.testing import assert_frame_equal
from shapely import from_wkt, get_coordinate_dimension, to_wkb
from shapely.geometry import (
    LineString,
    MultiLineString,
    MultiPoint,
    MultiPolygon,
    Point,
    Polygon,
)
from test_bess_planning_feature_policy import (
    _canonical_empty_policy_result,
    _checked_in_policy_result,
    _compiled_fixture,
)
from test_resolve_planning_feature_codes import _canonical_empty_coded_result

from landscout import stages
from landscout.common.frame_integrity import deterministic_frame_schema_signature
from landscout.stages.apply_bess_planning_feature_policy import (
    BessPlanningFeatureApplicationArtifactManifest,
    BessPlanningFeatureApplicationArtifactRecord,
    BessPlanningFeatureApplicationError,
    BessPlanningFeatureApplicationResult,
    apply_bess_planning_feature_policy,
    validate_bess_planning_feature_application_result,
)
from landscout.stages.apply_bess_planning_feature_policy import (
    load_bess_planning_feature_application_artifacts as _load_application_artifacts,
)

APPLICATION_SCOPE = "FEATURE_AND_RELATION_POLICY_PROPAGATION_ONLY"
POLICY_COLUMNS = (
    "bess_cnig_policy_application_status",
    "bess_cnig_precheck_status",
    "bess_cnig_precheck_confidence",
    "bess_cnig_status_priority",
    "bess_cnig_rationale",
    "bess_cnig_required_human_action",
    "bess_cnig_limitations",
    "bess_cnig_application_scope",
    "bess_cnig_policy_scope",
    "bess_cnig_local_feature_text_interpreted",
    "bess_cnig_local_regulation_content_interpreted",
    "bess_cnig_legal_conclusion_produced",
    "bess_cnig_parcel_status_aggregated",
    "bess_cnig_parcel_rejection_performed",
    "bess_cnig_score_calculated",
    "bess_cnig_policy_profile",
    "bess_cnig_policy_sha256",
    "bess_cnig_policy_result_sha256",
)
BOUNDARY_FLAG_COLUMNS = (
    "bess_cnig_local_feature_text_interpreted",
    "bess_cnig_local_regulation_content_interpreted",
    "bess_cnig_legal_conclusion_produced",
    "bess_cnig_parcel_status_aggregated",
    "bess_cnig_parcel_rejection_performed",
    "bess_cnig_score_calculated",
)
ARTIFACT_FILES = {
    "SURFACE_FEATURES": ("surface.parquet", True),
    "LINE_FEATURES": ("line.parquet", True),
    "POINT_FEATURES": ("point.parquet", True),
    "RELATIONS": ("relations.parquet", False),
}
_LAST_CODED_RESULT: object | None = None
_LAST_POLICY_RESULT: object | None = None


def _application_artifact_record_payload() -> dict[str, object]:
    crs = {
        "type": "ProjectedCRS",
        "name": "RGF93 v1 / Lambert-93",
        "coordinate_system": {"axis": [{"name": "Easting"}]},
    }
    return {
        "artifact_role": "SURFACE_FEATURES",
        "filename": "surface.parquet",
        "row_count": 1,
        "size_bytes": 1,
        "sha256": "a" * 64,
        "frame_schema_signature": {
            "columns": ["geometry"],
            "dtypes": ["geometry"],
            "index_class": "pandas.core.indexes.range.RangeIndex",
            "index_names": [None],
            "index_level_dtypes": ["int64"],
            "geometry_column": "geometry",
            "crs": crs,
        },
        "geospatial": True,
        "crs": crs,
    }


def test_application_artifact_record_is_deeply_immutable_without_aliases() -> None:
    payload = _application_artifact_record_payload()
    record = BessPlanningFeatureApplicationArtifactRecord.model_validate(payload)

    payload_signature = payload["frame_schema_signature"]
    assert isinstance(payload_signature, dict)
    payload_columns = payload_signature["columns"]
    assert isinstance(payload_columns, list)
    payload_columns.append("caller_mutation")
    payload_crs = payload["crs"]
    assert isinstance(payload_crs, dict)
    payload_crs["caller_mutation"] = True

    assert record.frame_schema_signature["columns"] == ("geometry",)
    assert record.crs is not None
    assert "caller_mutation" not in record.crs
    assert record.model_dump(mode="json", warnings="error") == (
        _application_artifact_record_payload()
    )
    with pytest.raises(TypeError, match="frozen"):
        record.frame_schema_signature["new"] = "value"
    with pytest.raises(AttributeError):
        record.frame_schema_signature["columns"].append("new")
    with pytest.raises(TypeError, match="frozen"):
        record.crs["new"] = "value"
    coordinate_system = record.crs["coordinate_system"]
    assert isinstance(coordinate_system, Mapping)
    with pytest.raises(TypeError, match="frozen"):
        coordinate_system["new"] = "value"


def _application_fixture() -> tuple[
    tuple[object, ...],
    object,
    object,
    object,
    BessPlanningFeatureApplicationResult,
]:
    global _LAST_CODED_RESULT, _LAST_POLICY_RESULT
    inputs, coded, config, policy = _compiled_fixture()
    result = apply_bess_planning_feature_policy(*inputs, coded, config, policy)
    _LAST_CODED_RESULT = coded
    _LAST_POLICY_RESULT = policy
    return inputs, coded, config, policy, result


def load_bess_planning_feature_application_artifacts(
    manifest_path: str | Path,
    surface_features_path: str | Path,
    line_features_path: str | Path,
    point_features_path: str | Path,
    relations_path: str | Path,
    coded_result: object | None = None,
    policy_result: object | None = None,
) -> BessPlanningFeatureApplicationResult:
    """Test adapter supplying the newly mandatory exact upstream envelopes."""

    if coded_result is None or policy_result is None:
        coded_result = _LAST_CODED_RESULT
        policy_result = _LAST_POLICY_RESULT
    assert coded_result is not None
    assert policy_result is not None
    return _load_application_artifacts(
        manifest_path,
        surface_features_path,
        line_features_path,
        point_features_path,
        relations_path,
        coded_result,
        policy_result,
    )


def _small_catalog(*rows: tuple[str, str, str, str, str]) -> gpd.GeoDataFrame:
    return gpd.GeoDataFrame(
        {
            "planning_feature_id": [row[0] for row in rows],
            "feature_family": [row[1] for row in rows],
            "type_code_raw": [row[2] for row in rows],
            "subtype_code_raw": [row[3] for row in rows],
            "official_code_status": [row[4] for row in rows],
        },
        geometry=[Point(position, position) for position in range(len(rows))],
        crs="EPSG:2154",
    )


def _write_application_artifacts(
    tmp_path: Path,
    result: BessPlanningFeatureApplicationResult,
) -> tuple[Path, dict[str, Path], dict[str, object]]:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    frames = {
        "SURFACE_FEATURES": result.surface_features,
        "LINE_FEATURES": result.line_features,
        "POINT_FEATURES": result.point_features,
        "RELATIONS": result.relations,
    }
    paths: dict[str, Path] = {}
    records: list[dict[str, object]] = []
    for role, (filename, geospatial) in ARTIFACT_FILES.items():
        path = tmp_path / filename
        frame = frames[role]
        frame.to_parquet(path, index=True)
        paths[role] = path
        signature = deterministic_frame_schema_signature(frame)
        records.append(
            {
                "artifact_role": role,
                "filename": filename,
                "row_count": len(frame),
                "size_bytes": path.stat().st_size,
                "sha256": sha256(path.read_bytes()).hexdigest(),
                "frame_schema_signature": signature,
                "geospatial": geospatial,
                "crs": signature.get("crs"),
            }
        )
    scalar_names = tuple(
        field.name
        for field in fields(BessPlanningFeatureApplicationResult)
        if field.name
        not in {"surface_features", "line_features", "point_features", "relations"}
    )
    manifest = {
        "schema_version": 2,
        "artifact_kind": "BESS_PLANNING_FEATURE_POLICY_APPLICATION_RESULT",
        **{name: getattr(result, name) for name in scalar_names},
        "artifacts": records,
    }
    validated = BessPlanningFeatureApplicationArtifactManifest.model_validate(manifest)
    assert validated.schema_version == 2
    manifest_path = tmp_path / "application.json"
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    assert module is not None
    return manifest_path, paths, manifest


def _coordinated_policy_mutation(
    result: BessPlanningFeatureApplicationResult,
    column: str,
    value: object,
    *,
    dtype: str | None = None,
) -> BessPlanningFeatureApplicationResult:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    feature_id = str(result.relations.iloc[0]["planning_feature_id"])
    changed = result
    for frame_name in ("surface_features", "line_features", "point_features"):
        frame = getattr(changed, frame_name).copy(deep=True)
        mask = frame["planning_feature_id"].eq(feature_id)
        if mask.any():
            values = frame[column].tolist()
            for position, selected in enumerate(mask.tolist()):
                if selected:
                    values[position] = value
            if dtype == "category":
                frame[column] = pd.Series(pd.Categorical(values), index=frame.index)
            elif dtype is not None:
                frame[column] = pd.Series(values, index=frame.index, dtype=dtype)
            else:
                frame.loc[mask, column] = value
            changed = replace(changed, **{frame_name: frame})
    relation_frame = changed.relations.copy(deep=True)
    relation_mask = relation_frame["planning_feature_id"].eq(feature_id)
    relation_values = relation_frame[column].tolist()
    for position, selected in enumerate(relation_mask.tolist()):
        if selected:
            relation_values[position] = value
    if dtype == "category":
        relation_frame[column] = pd.Series(
            pd.Categorical(relation_values), index=relation_frame.index
        )
    elif dtype is not None:
        relation_frame[column] = pd.Series(
            relation_values, index=relation_frame.index, dtype=dtype
        )
    else:
        relation_frame.loc[relation_mask, column] = value
    return module._result_with_hashes(replace(changed, relations=relation_frame))


def _coordinated_feature_id_mutation(
    result: BessPlanningFeatureApplicationResult,
    feature_id: object,
) -> BessPlanningFeatureApplicationResult:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    original = result.relations.iloc[0]["planning_feature_id"]
    changed = result
    for frame_name in ("surface_features", "line_features", "point_features"):
        frame = getattr(changed, frame_name).copy(deep=True)
        frame.loc[frame["planning_feature_id"].eq(original), "planning_feature_id"] = (
            feature_id
        )
        changed = replace(changed, **{frame_name: frame})
    relations = changed.relations.copy(deep=True)
    relations.loc[
        relations["planning_feature_id"].eq(original), "planning_feature_id"
    ] = feature_id
    return module._result_with_hashes(replace(changed, relations=relations))


def _zero_relation_feature(
    result: BessPlanningFeatureApplicationResult,
) -> tuple[str, gpd.GeoDataFrame, object]:
    related = set(result.relations["planning_feature_id"])
    for name in ("surface_features", "line_features", "point_features"):
        frame = getattr(result, name)
        unmatched = frame.loc[~frame["planning_feature_id"].isin(related)]
        if not unmatched.empty:
            return name, frame, unmatched.index[0]
    raise AssertionError("fixture must contain a feature having zero relations")


def _surface_touch_with_positive_area(
    result: BessPlanningFeatureApplicationResult,
) -> BessPlanningFeatureApplicationResult:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    relations = result.relations.copy(deep=True)
    index = relations.index[relations["geometry_kind"].eq("SURFACE")][0]
    assert relations.loc[index, "intersection_area_m2"] > 0
    relations.loc[index, "relation_type"] = "TOUCH_ONLY"
    return module._result_with_hashes(replace(result, relations=relations))


def _z_geometry(kind: str) -> object:
    polygon = Polygon([(0, 0, 7), (2, 0, 7), (2, 2, 7), (0, 2, 7)])
    line = LineString([(0, 0, 7), (2, 0, 7)])
    point = Point(1, 1, 7)
    return {
        "Polygon": polygon,
        "MultiPolygon": MultiPolygon([polygon]),
        "LineString": line,
        "MultiLineString": MultiLineString([line]),
        "Point": point,
        "MultiPoint": MultiPoint([point]),
    }[kind]


def test_exact_policy_is_applied_to_every_feature_and_relation() -> None:
    _, coded, policy_config, policy, result = _application_fixture()
    assert result.result_hash_schema_version == 2
    assert result.application_scope == APPLICATION_SCOPE
    assert result.policy_profile == policy.policy_profile
    assert result.policy_sha256 == policy.policy_sha256
    assert result.policy_complete_result_content_sha256 == (
        policy.complete_result_content_sha256
    )
    lookup = policy.policy_table.set_index(
        ["feature_family", "type_code", "subtype_code"]
    )
    for source, applied in (
        (coded.surface_features, result.surface_features),
        (coded.line_features, result.line_features),
        (coded.point_features, result.point_features),
    ):
        assert tuple(applied.columns[: len(source.columns)]) == tuple(source.columns)
        assert (
            applied["bess_cnig_policy_application_status"]
            .eq("APPLIED_EXACT_POLICY")
            .all()
        )
        for row in applied.itertuples(index=False):
            expected = lookup.loc[
                (row.feature_family, row.type_code_raw, row.subtype_code_raw)
            ]
            assert row.bess_cnig_precheck_status == expected.precheck_status
            assert row.bess_cnig_precheck_confidence == expected.confidence
            assert row.bess_cnig_status_priority == expected.status_priority
            assert row.bess_cnig_rationale == expected.rationale
            assert row.bess_cnig_required_human_action == (
                expected.required_human_action
            )
            assert row.bess_cnig_limitations == expected.limitations
    assert (
        result.relations["bess_cnig_policy_application_status"]
        .eq("APPLIED_EXACT_POLICY")
        .all()
    )
    assert policy_config.policy_scope == result.policy_scope


def test_every_output_row_has_all_six_false_boundary_flags() -> None:
    _, _, _, _, result = _application_fixture()
    for frame in (
        result.surface_features,
        result.line_features,
        result.point_features,
        result.relations,
    ):
        assert all(column in frame.columns for column in BOUNDARY_FLAG_COLUMNS)
        for column in BOUNDARY_FLAG_COLUMNS:
            assert str(frame[column].dtype) == "bool"
            assert frame[column].notna().all()
            assert frame[column].eq(False).all()


def test_policy_suffix_has_one_exact_deterministic_dtype_schema() -> None:
    _, _, _, _, result = _application_fixture()
    expected = {
        column: "str"
        for column in POLICY_COLUMNS
        if column
        not in {
            "bess_cnig_status_priority",
            *BOUNDARY_FLAG_COLUMNS,
        }
    }
    expected["bess_cnig_status_priority"] = "Int64"
    expected.update({column: "bool" for column in BOUNDARY_FLAG_COLUMNS})
    for frame in (
        result.surface_features,
        result.line_features,
        result.point_features,
        result.relations,
    ):
        assert tuple(frame.columns[-len(POLICY_COLUMNS) :]) == POLICY_COLUMNS
        assert {column: str(frame[column].dtype) for column in POLICY_COLUMNS} == (
            expected
        )


def test_schema_v1_dimension_blind_hash_representation_is_rejected_locally() -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    surface = result.surface_features.copy(deep=True)
    original = surface.geometry.iloc[0]
    polygon_z = Polygon([(x, y, 7) for x, y in original.exterior.coords])
    assert get_coordinate_dimension(original) == 2
    assert get_coordinate_dimension(polygon_z) == 3
    assert to_wkb(original, hex=True, output_dimension=2) == to_wkb(
        polygon_z, hex=True, output_dimension=2
    )
    surface.at[surface.index[0], surface.geometry.name] = polygon_z
    blind = replace(result, surface_features=surface)
    assert blind.surface_features_content_sha256 == (
        result.surface_features_content_sha256
    )
    assert blind.complete_result_content_sha256 == result.complete_result_content_sha256
    with pytest.raises(BessPlanningFeatureApplicationError, match="2D|dimension"):
        module._validate_result_envelope(blind)
    with pytest.raises(BessPlanningFeatureApplicationError, match="2D|dimension"):
        module._result_with_hashes(blind)


@pytest.mark.parametrize(
    ("frame_name", "geometry_kind"),
    [
        ("surface_features", "Polygon"),
        ("surface_features", "MultiPolygon"),
        ("line_features", "LineString"),
        ("line_features", "MultiLineString"),
        ("point_features", "Point"),
        ("point_features", "MultiPoint"),
    ],
)
def test_every_non_2d_application_geometry_kind_fast_fails_before_source_validation(
    monkeypatch: pytest.MonkeyPatch,
    frame_name: str,
    geometry_kind: str,
) -> None:
    inputs, coded, config, policy, result = _application_fixture()
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    frame = getattr(result, frame_name).copy(deep=True)
    frame.at[frame.index[0], frame.geometry.name] = _z_geometry(geometry_kind)
    changed = replace(result, **{frame_name: frame})
    calls = 0

    def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1

    monkeypatch.setattr(module, "validate_bess_planning_feature_policy_result", counted)
    with pytest.raises(BessPlanningFeatureApplicationError, match="2D|dimension"):
        module.validate_bess_planning_feature_application_result(
            *inputs, coded, config, policy, changed
        )
    assert calls == 0


@pytest.mark.parametrize("wkt", ["POINT M (1 1 7)", "POINT ZM (1 1 7 8)"])
def test_m_and_zm_application_geometries_are_rejected(wkt: str) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    point = result.point_features.copy(deep=True)
    point.at[point.index[0], point.geometry.name] = from_wkt(wkt)
    with pytest.raises(BessPlanningFeatureApplicationError, match="2D|dimension"):
        module._validate_result_envelope(replace(result, point_features=point))


def test_valid_empty_optional_application_catalog_retains_schema_and_crs() -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, coded, _, policy, _ = _application_fixture()
    empty = coded.point_features.iloc[0:0].copy()
    applied = module._apply_feature_catalog(empty, policy)
    assert applied.empty
    assert tuple(applied.columns[: len(empty.columns)]) == tuple(empty.columns)
    assert tuple(applied.columns[-len(POLICY_COLUMNS) :]) == POLICY_COLUMNS
    assert applied.geometry.name == empty.geometry.name
    assert applied.crs == empty.crs
    module._validate_application_geometry(applied, "empty point features")


def test_exact_pair_identity_keeps_family_subtype_and_leading_zeroes_distinct() -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    policy = _checked_in_policy_result()
    catalog = _small_catalog(
        ("F-1500", "PRESCRIPTION", "15", "00", "RESOLVED_OFFICIAL"),
        ("F-1501", "PRESCRIPTION", "15", "01", "RESOLVED_OFFICIAL"),
        ("F-NO-SUBTYPE", "PRESCRIPTION", "15", "99", "UNKNOWN_CODE_PAIR"),
        ("F-NO-FAMILY", "INFORMATION", "15", "00", "UNKNOWN_CODE_PAIR"),
        ("F-0100", "PRESCRIPTION", "01", "00", "RESOLVED_OFFICIAL"),
    )
    applied = module._apply_feature_catalog(catalog, policy)
    assert applied.loc[0, "bess_cnig_precheck_confidence"] == "MEDIUM"
    assert applied.loc[1, "bess_cnig_precheck_confidence"] == "HIGH"
    assert applied.loc[0, "bess_cnig_precheck_status"] == "DESIGN_REVIEW_REQUIRED"
    assert applied.loc[1, "bess_cnig_precheck_status"] == "DESIGN_REVIEW_REQUIRED"
    assert applied.loc[2, "bess_cnig_policy_application_status"] == (
        "UNRESOLVED_CODE_PAIR"
    )
    assert applied.loc[3, "bess_cnig_policy_application_status"] == (
        "UNRESOLVED_CODE_PAIR"
    )
    assert applied.loc[4, "type_code_raw"] == "01"
    assert applied.loc[4, "subtype_code_raw"] == "00"


def test_unknown_pair_remains_present_with_true_null_decision_fields() -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    policy = _checked_in_policy_result()
    catalog = _small_catalog(
        ("F-UNKNOWN", "PRESCRIPTION", "98", "00", "UNKNOWN_CODE_PAIR"),
    )
    applied = module._apply_feature_catalog(catalog, policy)
    assert applied["planning_feature_id"].tolist() == ["F-UNKNOWN"]
    assert applied.loc[0, "bess_cnig_policy_application_status"] == (
        "UNRESOLVED_CODE_PAIR"
    )
    for column in POLICY_COLUMNS[1:7]:
        assert pd.isna(applied.loc[0, column])
        assert not isinstance(applied.loc[0, column], str)


@pytest.mark.parametrize(
    "row",
    [
        ("F-MISSING", "PRESCRIPTION", "98", "00", "RESOLVED_OFFICIAL"),
        ("F-UNEXPECTED", "PRESCRIPTION", "15", "00", "UNKNOWN_CODE_PAIR"),
    ],
)
def test_inconsistent_official_status_and_policy_match_is_rejected(
    row: tuple[str, str, str, str, str],
) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    with pytest.raises(BessPlanningFeatureApplicationError, match="policy|official"):
        module._apply_feature_catalog(_small_catalog(row), _checked_in_policy_result())


def test_feature_and_relation_inputs_are_preserved_and_not_mutated() -> None:
    inputs, coded, config, policy = _compiled_fixture()
    coded_copies = (
        coded.surface_features.copy(deep=True),
        coded.line_features.copy(deep=True),
        coded.point_features.copy(deep=True),
        coded.relations.copy(deep=True),
    )
    parcels_copy = inputs[1].copy(deep=True)
    result = apply_bess_planning_feature_policy(*inputs, coded, config, policy)
    assert_geodataframe_equal(coded_copies[0], coded.surface_features)
    assert_geodataframe_equal(coded_copies[1], coded.line_features)
    assert_geodataframe_equal(coded_copies[2], coded.point_features)
    assert_frame_equal(coded_copies[3], coded.relations)
    assert_geodataframe_equal(parcels_copy, inputs[1])
    for source, applied in (
        (coded.surface_features, result.surface_features),
        (coded.line_features, result.line_features),
        (coded.point_features, result.point_features),
    ):
        prefix = applied.loc[:, source.columns]
        assert_geodataframe_equal(source, prefix, check_dtype=True, check_crs=True)
        assert tuple(applied.columns[-len(POLICY_COLUMNS) :]) == POLICY_COLUMNS
        assert type(applied.index) is type(source.index)
        assert applied.index.equals(source.index)
    relation_prefix = result.relations.loc[:, coded.relations.columns]
    assert_frame_equal(coded.relations, relation_prefix, check_dtype=True)
    assert tuple(result.relations.columns[-len(POLICY_COLUMNS) :]) == POLICY_COLUMNS


def test_relations_inherit_only_from_referenced_enriched_feature() -> None:
    _, _, _, _, result = _application_fixture()
    features = pd.concat(
        [
            result.surface_features.drop(columns="geometry"),
            result.line_features.drop(columns="geometry"),
            result.point_features.drop(columns="geometry"),
        ],
        ignore_index=True,
    ).set_index("planning_feature_id")
    for relation in result.relations.itertuples(index=False):
        feature = features.loc[relation.planning_feature_id]
        for column in POLICY_COLUMNS:
            assert getattr(relation, column) == feature[column]


@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("source_feature_id", "MUTATED"),
        ("source_identity_kind", "MUTATED"),
        ("source_identity_field", "MUTATED"),
        ("logical_layer", "information_surface"),
        ("label_raw", "MUTATED"),
        ("text_raw", "MUTATED"),
        ("source_document_id", "MUTATED"),
        ("source_archive_sha256", "f" * 64),
        ("source_layer", "MUTATED"),
        ("source_validity_date_raw", "2099-01-01"),
        ("regulation_filename_raw", "MUTATED.pdf"),
        ("official_code_label", "MUTATED"),
        ("official_code_profile", "MUTATED"),
        ("feature_area_m2", 999.0),
    ],
)
def test_complete_relation_facts_must_match_referenced_feature(
    column: str, value: object
) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    relations = result.relations.copy(deep=True)
    index = relations.index[relations["geometry_kind"].eq("SURFACE")][0]
    relations.loc[index, column] = value
    changed = module._result_with_hashes(replace(result, relations=relations))
    with pytest.raises(BessPlanningFeatureApplicationError, match="relation|feature"):
        module._validate_result_envelope(changed)


def test_unknown_relation_feature_id_is_rejected() -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, coded, _, policy, result = _application_fixture()
    relations = coded.relations.copy(deep=True)
    relations.loc[relations.index[0], "planning_feature_id"] = "GPU:UNKNOWN"
    with pytest.raises(BessPlanningFeatureApplicationError, match="feature ID"):
        module._apply_relations(
            relations,
            result.surface_features,
            result.line_features,
            result.point_features,
        )
    assert policy is not None


def test_scope_has_no_parcel_output_aggregation_rejection_or_score() -> None:
    inputs, _, _, _, result = _application_fixture()
    assert not hasattr(result, "parcels")
    assert result.local_feature_text_interpreted is False
    assert result.local_regulation_content_interpreted is False
    assert result.legal_conclusion_produced is False
    assert result.parcel_status_aggregated is False
    assert result.parcel_rejection_performed is False
    assert result.score_calculated is False
    assert "parcel_id" not in result.surface_features.columns
    assert len(inputs[1]) > 0


def test_coordinated_feature_or_relation_policy_mutation_is_rejected() -> None:
    inputs, coded, config, policy, result = _application_fixture()
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    surface = result.surface_features.copy(deep=True)
    surface.loc[surface.index[0], "bess_cnig_precheck_status"] = "UNKNOWN"
    coordinated = module._result_with_hashes(replace(result, surface_features=surface))
    with pytest.raises(BessPlanningFeatureApplicationError, match="rebuilt|feature"):
        validate_bess_planning_feature_application_result(
            *inputs, coded, config, policy, coordinated
        )
    relations = result.relations.copy(deep=True)
    relations.loc[relations.index[0], "bess_cnig_precheck_confidence"] = "LOW"
    coordinated = module._result_with_hashes(replace(result, relations=relations))
    with pytest.raises(BessPlanningFeatureApplicationError, match="relation|rebuilt"):
        validate_bess_planning_feature_application_result(
            *inputs, coded, config, policy, coordinated
        )


def test_duplicate_application_relation_pair_is_rejected_locally() -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    relations = pd.concat([result.relations, result.relations.iloc[[0]]])
    changed = module._result_with_hashes(replace(result, relations=relations))
    with pytest.raises(BessPlanningFeatureApplicationError, match="duplicate|unique"):
        module._validate_result_envelope(changed)


@pytest.mark.parametrize(
    "feature_id",
    [None, "", "None", "/tmp/feature", r"C:\feature", " GPU:F "],
)
def test_application_relation_feature_id_is_exact_and_portable(
    feature_id: object,
) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    changed = _coordinated_feature_id_mutation(result, feature_id)
    with pytest.raises(BessPlanningFeatureApplicationError, match="feature|identity"):
        module._validate_result_envelope(changed)


@pytest.mark.parametrize("parcel_id", [None, "", "None", " PARCEL-1 "])
def test_application_relation_parcel_id_is_exact(parcel_id: object) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    relations = result.relations.copy(deep=True)
    relations.loc[relations.index[0], "parcel_id"] = parcel_id
    changed = module._result_with_hashes(replace(result, relations=relations))
    with pytest.raises(BessPlanningFeatureApplicationError, match="parcel|identity"):
        module._validate_result_envelope(changed)


def test_unknown_application_relation_type_is_rejected_locally() -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    relations = result.relations.copy(deep=True)
    relations.loc[relations.index[0], "relation_type"] = "BUFFERED_NEARBY"
    changed = module._result_with_hashes(replace(result, relations=relations))
    with pytest.raises(BessPlanningFeatureApplicationError, match="relation type"):
        module._validate_result_envelope(changed)


@pytest.mark.parametrize(
    ("column", "value", "message"),
    [
        ("bess_cnig_precheck_status", "AUTHORIZED", "status|domain"),
        ("bess_cnig_precheck_status", "FORBIDDEN", "status|domain"),
        ("bess_cnig_precheck_status", "PROHIBITED", "status|domain"),
        ("bess_cnig_precheck_confidence", "CERTAIN", "confidence|domain"),
        ("bess_cnig_status_priority", 0, "priority|positive"),
        ("bess_cnig_status_priority", -1, "priority|positive"),
        ("bess_cnig_rationale", "", "rationale|exact|non-empty"),
        ("bess_cnig_rationale", " leading", "rationale|exact|whitespace"),
        ("bess_cnig_required_human_action", "trailing ", "action|exact|whitespace"),
        ("bess_cnig_limitations", "", "limitations|exact|non-empty"),
    ],
)
def test_coordinated_invalid_policy_domains_fail_local_validation(
    column: str,
    value: object,
    message: str,
) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    changed = _coordinated_policy_mutation(result, column, value)
    with pytest.raises(BessPlanningFeatureApplicationError, match=message):
        module._validate_result_envelope(changed)


@pytest.mark.parametrize("literal", ["None", "nan", "<NA>"])
def test_literal_null_replacements_are_rejected(literal: str) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    changed = _coordinated_policy_mutation(result, "bess_cnig_rationale", literal)
    with pytest.raises(BessPlanningFeatureApplicationError, match="literal|missing"):
        module._validate_result_envelope(changed)


@pytest.mark.parametrize(
    ("column", "dtype", "value"),
    [
        ("bess_cnig_precheck_status", "object", "UNKNOWN"),
        ("bess_cnig_precheck_confidence", "category", "HIGH"),
        ("bess_cnig_rationale", "object", "Still a factual policy rationale."),
        ("bess_cnig_status_priority", "Float64", 1.0),
        ("bess_cnig_status_priority", "str", "1"),
        ("bess_cnig_parcel_status_aggregated", "boolean", False),
    ],
)
def test_self_consistent_wrong_policy_suffix_dtype_is_rejected(
    column: str,
    dtype: str,
    value: object,
) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    changed = _coordinated_policy_mutation(result, column, value, dtype=dtype)
    with pytest.raises(BessPlanningFeatureApplicationError, match="dtype|schema"):
        module._validate_result_envelope(changed)


@pytest.mark.parametrize(
    ("official_status", "application_status"),
    [
        ("RESOLVED_OFFICIAL", "UNRESOLVED_CODE_PAIR"),
        ("UNKNOWN_CODE_PAIR", "APPLIED_EXACT_POLICY"),
    ],
)
def test_official_and_application_statuses_cannot_contradict(
    official_status: str,
    application_status: str,
) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    changed = _coordinated_policy_mutation(
        result,
        "bess_cnig_policy_application_status",
        application_status,
    )
    feature_id = str(changed.relations.iloc[0]["planning_feature_id"])
    for frame_name in ("surface_features", "line_features", "point_features"):
        frame = getattr(changed, frame_name).copy(deep=True)
        mask = frame["planning_feature_id"].eq(feature_id)
        if mask.any():
            frame.loc[mask, "official_code_status"] = official_status
            changed = replace(changed, **{frame_name: frame})
    relation_frame = changed.relations.copy(deep=True)
    relation_frame.loc[
        relation_frame["planning_feature_id"].eq(feature_id), "official_code_status"
    ] = official_status
    changed = module._result_with_hashes(replace(changed, relations=relation_frame))
    with pytest.raises(BessPlanningFeatureApplicationError, match="official|status"):
        module._validate_result_envelope(changed)


@pytest.mark.parametrize("column", BOUNDARY_FLAG_COLUMNS)
def test_any_true_row_boundary_flag_is_rejected(column: str) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    changed = _coordinated_policy_mutation(result, column, True)
    with pytest.raises(BessPlanningFeatureApplicationError, match="flag|false"):
        module._validate_result_envelope(changed)


def test_application_and_public_validator_heavy_validation_counts(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inputs, coded, config, policy = _compiled_fixture()
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    actual = module.validate_bess_planning_feature_policy_result
    calls = 0

    def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1
        actual(*args, **kwargs)

    monkeypatch.setattr(module, "validate_bess_planning_feature_policy_result", counted)
    result = module.apply_bess_planning_feature_policy(*inputs, coded, config, policy)
    assert calls == 1
    module.validate_bess_planning_feature_application_result(
        *inputs, coded, config, policy, result
    )
    assert calls == 2


def test_malformed_local_result_fast_fails_before_heavy_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inputs, coded, config, policy, result = _application_fixture()
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    calls = 0

    def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1

    monkeypatch.setattr(module, "validate_bess_planning_feature_policy_result", counted)
    invalid = replace(result, complete_result_content_sha256="f" * 64)
    with pytest.raises(
        BessPlanningFeatureApplicationError, match="hash|SHA|sha256|invalid"
    ):
        module.validate_bess_planning_feature_application_result(
            *inputs, coded, config, policy, invalid
        )
    assert calls == 0


def test_coordinated_application_source_lock_mutation_fast_fails(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inputs, coded, config, policy, result = _application_fixture()
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    calls = 0

    def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1

    changed = replace(result, policy_sha256="f" * 64)
    for frame_name in ("surface_features", "line_features", "point_features"):
        frame = getattr(changed, frame_name).copy(deep=True)
        frame["bess_cnig_policy_sha256"] = pd.array(
            ["f" * 64] * len(frame), dtype="str"
        )
        changed = replace(changed, **{frame_name: frame})
    relation_frame = changed.relations.copy(deep=True)
    relation_frame["bess_cnig_policy_sha256"] = pd.array(
        ["f" * 64] * len(relation_frame), dtype="str"
    )
    changed = module._result_with_hashes(replace(changed, relations=relation_frame))
    monkeypatch.setattr(module, "validate_bess_planning_feature_policy_result", counted)
    with pytest.raises(BessPlanningFeatureApplicationError, match="source lock"):
        module.validate_bess_planning_feature_application_result(
            *inputs, coded, config, policy, changed
        )
    assert calls == 0


def test_valid_four_file_manifest_and_verified_byte_readback(tmp_path: Path) -> None:
    inputs, coded, config, policy, result = _application_fixture()
    manifest_path, paths, _ = _write_application_artifacts(tmp_path, result)
    loaded = load_bess_planning_feature_application_artifacts(
        manifest_path,
        paths["SURFACE_FEATURES"],
        paths["LINE_FEATURES"],
        paths["POINT_FEATURES"],
        paths["RELATIONS"],
    )
    assert_geodataframe_equal(result.surface_features, loaded.surface_features)
    assert_geodataframe_equal(result.line_features, loaded.line_features)
    assert_geodataframe_equal(result.point_features, loaded.point_features)
    assert_frame_equal(result.relations, loaded.relations)
    validate_bess_planning_feature_application_result(
        *inputs, coded, config, policy, loaded
    )


def test_duplicate_relation_pair_artifact_fails_local_loading(tmp_path: Path) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    relations = pd.concat([result.relations, result.relations.iloc[[0]]])
    changed = module._result_with_hashes(replace(result, relations=relations))
    manifest_path, paths, _ = _write_application_artifacts(tmp_path, changed)
    with pytest.raises(BessPlanningFeatureApplicationError, match="duplicate|unique"):
        load_bess_planning_feature_application_artifacts(
            manifest_path,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )


def test_document_wide_mapping_conflict_artifact_fails_local_loading(
    tmp_path: Path,
) -> None:
    _, _, _, _, result = _application_fixture()
    first = result.relations.iloc[0]
    different = result.relations[
        result.relations["bess_cnig_precheck_status"].ne(
            first["bess_cnig_precheck_status"]
        )
    ].iloc[0]
    changed = _coordinated_policy_mutation(
        result,
        "bess_cnig_status_priority",
        int(different["bess_cnig_status_priority"]),
    )
    manifest_path, paths, _ = _write_application_artifacts(tmp_path, changed)
    with pytest.raises(BessPlanningFeatureApplicationError, match="priority|mapping"):
        load_bess_planning_feature_application_artifacts(
            manifest_path,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )


def test_positive_surface_overlap_cannot_be_relabelled_touch_only_in_artifact(
    tmp_path: Path,
) -> None:
    _, _, _, _, result = _application_fixture()
    changed = _surface_touch_with_positive_area(result)
    manifest_path, paths, _ = _write_application_artifacts(tmp_path, changed)
    with pytest.raises(
        BessPlanningFeatureApplicationError, match="surface|metric|type"
    ):
        load_bess_planning_feature_application_artifacts(
            manifest_path,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )


def test_wrong_2d_feature_geometry_fails_local_artifact_loading(tmp_path: Path) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    surface = result.surface_features.copy(deep=True)
    surface.at[surface.index[0], surface.geometry.name] = Point(0, 0)
    changed = module._result_with_hashes(replace(result, surface_features=surface))
    manifest_path, paths, _ = _write_application_artifacts(tmp_path, changed)
    with pytest.raises(BessPlanningFeatureApplicationError, match="surface|geometry"):
        load_bess_planning_feature_application_artifacts(
            manifest_path,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )


@pytest.mark.parametrize(
    ("frame_name", "geometry"),
    [
        ("surface_features", Point(0, 0)),
        ("line_features", Polygon([(0, 0), (1, 0), (1, 1), (0, 0)])),
        ("point_features", LineString([(0, 0), (1, 1)])),
        ("surface_features", Polygon()),
        (
            "surface_features",
            Polygon([(0, 0), (2, 2), (0, 2), (2, 0), (0, 0)]),
        ),
    ],
    ids=["surface-point", "line-polygon", "point-line", "empty", "invalid"],
)
def test_feature_catalog_geometry_role_is_intrinsic(
    frame_name: str, geometry: object
) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    frame = getattr(result, frame_name).copy(deep=True)
    frame.at[frame.index[0], frame.geometry.name] = geometry
    changed = module._result_with_hashes(replace(result, **{frame_name: frame}))
    with pytest.raises(BessPlanningFeatureApplicationError, match="geometry"):
        module._validate_result_envelope(changed)


@pytest.mark.parametrize(
    ("frame_name", "metric"),
    [
        ("surface_features", "feature_area_m2"),
        ("line_features", "feature_length_m"),
        ("point_features", "point_member_count"),
    ],
)
def test_feature_catalog_metric_must_match_geometry(
    frame_name: str, metric: str
) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    frame = getattr(result, frame_name).copy(deep=True)
    frame.loc[frame.index[0], metric] += 1
    changed = module._result_with_hashes(replace(result, **{frame_name: frame}))
    with pytest.raises(
        BessPlanningFeatureApplicationError, match="metric|geometry|count"
    ):
        module._validate_result_envelope(changed)


@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("planning_feature_id", "GPU:malformed"),
        ("logical_layer", "prescription_line"),
        ("geometry_kind", "LINE"),
    ],
)
def test_unreferenced_feature_catalog_identity_fields_are_intrinsic(
    column: str, value: str
) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    name, source, index = _zero_relation_feature(result)
    frame = source.copy(deep=True)
    frame.loc[index, column] = value
    changed = module._result_with_hashes(replace(result, **{name: frame}))
    with pytest.raises(
        BessPlanningFeatureApplicationError, match="identity|layer|kind"
    ):
        module._validate_result_envelope(changed)


def test_feature_catalog_requires_canonical_crs_and_global_identity() -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    surface = result.surface_features.to_crs("EPSG:4326")
    with pytest.raises(BessPlanningFeatureApplicationError, match="EPSG:2154|CRS"):
        module._validate_result_envelope(
            module._result_with_hashes(replace(result, surface_features=surface))
        )
    point = result.point_features.copy(deep=True)
    point.loc[point.index[0], "planning_feature_id"] = result.surface_features.iloc[0][
        "planning_feature_id"
    ]
    with pytest.raises(BessPlanningFeatureApplicationError, match="identity|unique"):
        module._validate_result_envelope(
            module._result_with_hashes(replace(result, point_features=point))
        )


@pytest.mark.parametrize("feature_id", ["None", "/tmp/feature", r"C:\feature", " bad "])
def test_unreferenced_feature_identity_is_validated_locally(
    tmp_path: Path, feature_id: str
) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    name, source, index = _zero_relation_feature(result)
    frame = source.copy(deep=True)
    frame.loc[index, "planning_feature_id"] = feature_id
    changed = module._result_with_hashes(replace(result, **{name: frame}))
    manifest_path, paths, _ = _write_application_artifacts(tmp_path, changed)
    with pytest.raises(
        BessPlanningFeatureApplicationError, match="feature|identity|GPU"
    ):
        load_bess_planning_feature_application_artifacts(
            manifest_path,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )


def test_unreferenced_feature_participates_in_global_policy_mapping(
    tmp_path: Path,
) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    name, source, index = _zero_relation_feature(result)
    frame = source.copy(deep=True)
    status = frame.loc[index, "bess_cnig_precheck_status"]
    conflicting = pd.concat(
        [result.surface_features, result.line_features, result.point_features],
        ignore_index=True,
    )
    conflicting = conflicting.loc[conflicting["bess_cnig_precheck_status"].ne(status)]
    frame.loc[index, "bess_cnig_status_priority"] = int(
        conflicting.iloc[0]["bess_cnig_status_priority"]
    )
    changed = module._result_with_hashes(replace(result, **{name: frame}))
    manifest_path, paths, _ = _write_application_artifacts(tmp_path, changed)
    with pytest.raises(BessPlanningFeatureApplicationError, match="priority|mapping"):
        load_bess_planning_feature_application_artifacts(
            manifest_path,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )


@pytest.mark.parametrize("policy_schema", [0, 2, 999])
def test_application_locks_policy_result_schema_exactly(policy_schema: int) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    changed = module._result_with_hashes(
        replace(result, policy_result_hash_schema_version=policy_schema)
    )
    with pytest.raises(BessPlanningFeatureApplicationError, match="policy.*schema"):
        module._validate_result_envelope(changed)


@pytest.mark.parametrize("cnig_schema", [1, 4, 6, 999])
def test_application_locks_cnig_result_schema_exactly(cnig_schema: int) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    changed = module._result_with_hashes(
        replace(result, cnig_result_hash_schema_version=cnig_schema)
    )
    with pytest.raises(BessPlanningFeatureApplicationError, match="CNIG|cnig.*schema"):
        module._validate_result_envelope(changed)


def test_application_accepts_only_current_policy_and_cnig_source_schemas() -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    assert result.policy_result_hash_schema_version == 1
    assert result.cnig_result_hash_schema_version == 5
    module._validate_result_envelope(result)


def test_duplicate_relation_identity_fast_fails_before_policy_source_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inputs, coded, config, policy, result = _application_fixture()
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    relations = pd.concat(
        [result.relations, result.relations.iloc[[0]]], ignore_index=True
    )
    relations.index = pd.Index(relations.index.to_numpy(), dtype="int64")
    changed = module._result_with_hashes(replace(result, relations=relations))
    calls = 0

    def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1

    monkeypatch.setattr(module, "validate_bess_planning_feature_policy_result", counted)
    with pytest.raises(BessPlanningFeatureApplicationError, match="duplicate|unique"):
        module.validate_bess_planning_feature_application_result(
            *inputs, coded, config, policy, changed
        )
    assert calls == 0


def test_self_consistent_z_geoparquet_artifact_is_rejected(tmp_path: Path) -> None:
    _, _, _, _, result = _application_fixture()
    surface = result.surface_features.copy(deep=True)
    original = surface.geometry.iloc[0]
    surface.at[surface.index[0], surface.geometry.name] = Polygon(
        [(x, y, 9) for x, y in original.exterior.coords]
    )
    changed = replace(result, surface_features=surface)
    manifest_path, paths, _ = _write_application_artifacts(tmp_path, changed)
    with pytest.raises(BessPlanningFeatureApplicationError, match="2D|dimension"):
        load_bess_planning_feature_application_artifacts(
            manifest_path,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )


def test_self_consistent_wrong_dtype_artifact_is_rejected(tmp_path: Path) -> None:
    _, _, _, _, result = _application_fixture()
    changed = _coordinated_policy_mutation(
        result,
        "bess_cnig_precheck_status",
        "UNKNOWN",
        dtype="object",
    )
    manifest_path, paths, _ = _write_application_artifacts(tmp_path, changed)
    with pytest.raises(BessPlanningFeatureApplicationError, match="dtype|schema"):
        load_bess_planning_feature_application_artifacts(
            manifest_path,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )


@pytest.mark.parametrize(
    ("mutation", "message"),
    [
        (lambda value: value.update(schema_version=1), "schema"),
        (lambda value: value["artifacts"].pop(), "role|artifact"),
        (
            lambda value: value["artifacts"].append(
                {**value["artifacts"][0], "artifact_role": "EXTRA"}
            ),
            "role|artifact",
        ),
        (
            lambda value: value["artifacts"].append(dict(value["artifacts"][0])),
            "duplicate|role|artifact",
        ),
        (
            lambda value: value["artifacts"][0].update(filename="wrong.parquet"),
            "filename",
        ),
        (
            lambda value: value["artifacts"][1].update(
                filename=value["artifacts"][0]["filename"]
            ),
            "duplicate|filename",
        ),
        (
            lambda value: value["artifacts"][0].update(
                filename="C:/absolute/surface.parquet"
            ),
            "filename",
        ),
        (lambda value: value["artifacts"][0].update(size_bytes=1), "size"),
        (lambda value: value["artifacts"][0].update(sha256="f" * 64), "SHA|hash"),
        (lambda value: value["artifacts"][0].update(sha256="bad"), "SHA|hash"),
        (lambda value: value["artifacts"][0].update(row_count=999), "row"),
        (
            lambda value: value["artifacts"][0]["frame_schema_signature"].update(
                index_names=["wrong"]
            ),
            "schema",
        ),
        (lambda value: value["artifacts"][0].update(crs={"wrong": True}), "CRS|crs"),
        (lambda value: value["artifacts"][0].update(crs=None), "CRS|crs"),
        (lambda value: value["artifacts"][0].update(geospatial=False), "geospatial"),
        (lambda value: value.update(unknown=True), "manifest|artifact"),
    ],
)
def test_artifact_manifest_rejects_invalid_contract(
    tmp_path: Path,
    mutation: object,
    message: str,
) -> None:
    _, _, _, _, result = _application_fixture()
    manifest_path, paths, manifest = _write_application_artifacts(tmp_path, result)
    assert callable(mutation)
    mutation(manifest)
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    with pytest.raises(BessPlanningFeatureApplicationError, match=message):
        load_bess_planning_feature_application_artifacts(
            manifest_path,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )


@pytest.mark.parametrize(
    "document",
    [
        '{"schema_version": 2, "schema_version": 2}\n',
        '{"schema_version": NaN}\n',
        '{"schema_version": Infinity}\n',
        "[]\n",
    ],
    ids=["duplicate-key", "nan", "infinity", "non-object"],
)
def test_application_manifest_uses_strict_json_before_artifact_read(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    document: str,
) -> None:
    _, _, _, _, result = _application_fixture()
    manifest_path, paths, _ = _write_application_artifacts(tmp_path, result)
    manifest_path.write_text(document, encoding="utf-8")
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    artifact_reads = 0
    original_read_bytes = Path.read_bytes

    def counted_bytes(path: Path) -> bytes:
        nonlocal artifact_reads
        if path in paths.values():
            artifact_reads += 1
        return original_read_bytes(path)

    def counted(*args: object, **kwargs: object) -> object:
        nonlocal artifact_reads
        artifact_reads += 1
        raise AssertionError("Artifact read preceded strict manifest validation")

    monkeypatch.setattr(Path, "read_bytes", counted_bytes)
    monkeypatch.setattr(module.pd, "read_parquet", counted)
    with pytest.raises(
        BessPlanningFeatureApplicationError,
        match="Duplicate JSON|finite|top-level|invalid",
    ):
        load_bess_planning_feature_application_artifacts(
            manifest_path,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )
    assert artifact_reads == 0


def test_artifact_loader_parses_only_verified_bytes(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _, _, _, _, result = _application_fixture()
    manifest_path, paths, _ = _write_application_artifacts(tmp_path, result)
    target = paths["RELATIONS"]
    replacement = tmp_path / "replacement.parquet"
    result.relations.to_parquet(replacement, index=True, compression="gzip")
    original_read_bytes = Path.read_bytes
    verified = original_read_bytes(target)
    replacement_bytes = original_read_bytes(replacement)
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    original_read_parquet = module.pd.read_parquet
    replaced = False
    observed: list[tuple[str, bytes]] = []

    def replace_after_read(path: Path) -> bytes:
        nonlocal replaced
        payload = original_read_bytes(path)
        if path == target and not replaced:
            path.write_bytes(replacement_bytes)
            replaced = True
        return payload

    def observed_read(source: object, *args: object, **kwargs: object) -> object:
        if isinstance(source, BytesIO):
            observed.append(("buffer", source.getvalue()))
        return original_read_parquet(source, *args, **kwargs)

    monkeypatch.setattr(Path, "read_bytes", replace_after_read)
    monkeypatch.setattr(module.pd, "read_parquet", observed_read)
    loaded = load_bess_planning_feature_application_artifacts(
        manifest_path,
        paths["SURFACE_FEATURES"],
        paths["LINE_FEATURES"],
        paths["POINT_FEATURES"],
        paths["RELATIONS"],
    )
    assert replaced
    assert ("buffer", verified) in observed
    assert_frame_equal(result.relations, loaded.relations)


def test_physical_replacement_before_loading_is_rejected(tmp_path: Path) -> None:
    _, _, _, _, result = _application_fixture()
    manifest_path, paths, _ = _write_application_artifacts(tmp_path, result)
    paths["RELATIONS"].write_bytes(paths["RELATIONS"].read_bytes() + b"tamper")
    with pytest.raises(BessPlanningFeatureApplicationError, match="size|SHA|hash"):
        load_bess_planning_feature_application_artifacts(
            manifest_path,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )


def test_public_application_api_exports_only_stable_symbols() -> None:
    required = {
        "BessPlanningFeatureApplicationArtifactManifest",
        "BessPlanningFeatureApplicationError",
        "BessPlanningFeatureApplicationResult",
        "apply_bess_planning_feature_policy",
        "load_bess_planning_feature_application_artifacts",
        "validate_bess_planning_feature_application_result",
        "validate_bess_planning_feature_application_result_envelope",
    }
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    assert set(module.__all__) == required
    assert required.issubset(set(stages.__all__))
    assert not any(name.startswith("_") for name in module.__all__)


def _replace_application_frame(
    result: BessPlanningFeatureApplicationResult,
    frame_name: str,
    frame: pd.DataFrame,
) -> BessPlanningFeatureApplicationResult:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    return module._result_with_hashes(replace(result, **{frame_name: frame}))


def _coordinated_referenced_lineage_mutation(
    result: BessPlanningFeatureApplicationResult,
    column: str,
    value: str,
    *,
    rename_id: bool = False,
) -> BessPlanningFeatureApplicationResult:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    feature_id = str(result.relations.iloc[0]["planning_feature_id"])
    changed = result
    replacement_id = feature_id
    for frame_name in ("surface_features", "line_features", "point_features"):
        frame = getattr(changed, frame_name).copy(deep=True)
        mask = frame["planning_feature_id"].eq(feature_id)
        if mask.any():
            frame.loc[mask, column] = value
            if rename_id:
                row = frame.loc[mask].iloc[0]
                replacement_id = (
                    f"GPU:{row['source_document_id']}:"
                    f"{row['logical_layer']}:{row['source_feature_id']}"
                )
                frame.loc[mask, "planning_feature_id"] = replacement_id
            changed = replace(changed, **{frame_name: frame})
    relations = changed.relations.copy(deep=True)
    mask = relations["planning_feature_id"].eq(feature_id)
    relations.loc[mask, column] = value
    if rename_id:
        relations.loc[mask, "planning_feature_id"] = replacement_id
    return module._result_with_hashes(replace(changed, relations=relations))


def test_unreferenced_feature_document_lineage_is_bound_to_envelope_artifact(
    tmp_path: Path,
) -> None:
    _, _, _, _, result = _application_fixture()
    name, source, index = _zero_relation_feature(result)
    frame = source.copy(deep=True)
    frame.loc[index, "source_document_id"] = "MUTATED-DOCUMENT"
    frame.loc[index, "planning_feature_id"] = (
        f"GPU:MUTATED-DOCUMENT:{frame.loc[index, 'logical_layer']}:"
        f"{frame.loc[index, 'source_feature_id']}"
    )
    changed = _replace_application_frame(result, name, frame)
    manifest, paths, _ = _write_application_artifacts(tmp_path, changed)
    with pytest.raises(BessPlanningFeatureApplicationError, match="document|lineage"):
        load_bess_planning_feature_application_artifacts(
            manifest,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )


@pytest.mark.parametrize(
    "mutation",
    ["archive", "official-profile", "envelope-document"],
)
def test_feature_row_lineage_must_match_application_envelope(mutation: str) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    if mutation == "envelope-document":
        changed = module._result_with_hashes(
            replace(result, source_document_id="MUTATED-DOCUMENT")
        )
    else:
        name, source, index = _zero_relation_feature(result)
        frame = source.copy(deep=True)
        if mutation == "archive":
            frame.loc[index, "source_archive_sha256"] = "f" * 64
        else:
            frame.loc[index, "official_code_profile"] = "mutated_profile"
            frame.loc[index, "official_code_profile_sha256"] = "f" * 64
        changed = _replace_application_frame(result, name, frame)
    with pytest.raises(BessPlanningFeatureApplicationError, match="lineage|document"):
        module._validate_result_envelope(changed)


@pytest.mark.parametrize(
    ("column", "value", "rename_id"),
    [
        ("source_document_id", "MUTATED-DOCUMENT", True),
        ("source_archive_sha256", "f" * 64, False),
    ],
)
def test_coordinated_referenced_row_lineage_cannot_bypass_envelope(
    column: str,
    value: str,
    rename_id: bool,
) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    changed = _coordinated_referenced_lineage_mutation(
        result, column, value, rename_id=rename_id
    )
    with pytest.raises(BessPlanningFeatureApplicationError, match="lineage|document"):
        module._validate_result_envelope(changed)


def test_resolved_official_row_requires_label_and_envelope_profile() -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    name, source, index = _zero_relation_feature(result)
    for column, value in (
        ("official_code_label", pd.NA),
        ("official_code_profile", "wrong_profile"),
    ):
        frame = source.copy(deep=True)
        frame.loc[index, column] = value
        changed = _replace_application_frame(result, name, frame)
        with pytest.raises(
            BessPlanningFeatureApplicationError, match="official|profile|label"
        ):
            module._validate_result_envelope(changed)


def test_unknown_official_row_rejects_invented_label_or_url() -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    name, source, index = _zero_relation_feature(result)
    for invented_column in ("official_code_label", "official_code_source_url"):
        frame = source.copy(deep=True)
        frame.loc[index, "official_code_status"] = "UNKNOWN_CODE_PAIR"
        frame.loc[index, "bess_cnig_policy_application_status"] = "UNRESOLVED_CODE_PAIR"
        for column in (
            "official_code_label",
            "official_legal_reference",
            "official_regulation_reference",
            "official_code_source_url",
            "bess_cnig_precheck_status",
            "bess_cnig_precheck_confidence",
            "bess_cnig_rationale",
            "bess_cnig_required_human_action",
            "bess_cnig_limitations",
        ):
            frame.loc[index, column] = pd.NA
        frame.loc[index, "bess_cnig_status_priority"] = pd.NA
        frame.loc[index, invented_column] = (
            "Invented label"
            if invented_column == "official_code_label"
            else "https://example.invalid/invented"
        )
        changed = _replace_application_frame(result, name, frame)
        with pytest.raises(BessPlanningFeatureApplicationError, match="official|null"):
            module._validate_result_envelope(changed)


@pytest.mark.parametrize(
    ("frame_name", "mutation"),
    [
        ("surface_features", "missing-column"),
        ("surface_features", "unexpected-column"),
        ("surface_features", "reordered-columns"),
        ("surface_features", "metric-object"),
        ("line_features", "metric-object"),
        ("point_features", "metric-object"),
        ("surface_features", "official-object"),
        ("surface_features", "index-name"),
        ("surface_features", "index-dtype"),
        ("point_features", "malformed-empty"),
    ],
)
def test_application_feature_prefix_has_exact_canonical_schema(
    frame_name: str,
    mutation: str,
) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    frame = getattr(result, frame_name).copy(deep=True)
    if mutation == "missing-column":
        frame = frame.drop(columns="regulation_url_raw")
    elif mutation == "unexpected-column":
        position = frame.columns.get_loc(POLICY_COLUMNS[0])
        frame.insert(position, "unexpected_factual", pd.array(["x"] * len(frame)))
    elif mutation == "reordered-columns":
        columns = list(frame.columns)
        columns[0], columns[1] = columns[1], columns[0]
        frame = frame.loc[:, columns]
    elif mutation == "metric-object":
        metric = {
            "surface_features": "feature_area_m2",
            "line_features": "feature_length_m",
            "point_features": "point_member_count",
        }[frame_name]
        frame[metric] = pd.Series(
            frame[metric].tolist(), index=frame.index, dtype="object"
        )
    elif mutation == "official-object":
        frame["official_legal_reference"] = pd.Series(
            frame["official_legal_reference"].tolist(),
            index=frame.index,
            dtype="object",
        )
    elif mutation == "index-name":
        frame.index = frame.index.rename("wrong")
    elif mutation == "index-dtype":
        frame.index = pd.Index(frame.index.to_numpy(dtype="int32"), dtype="int32")
    else:
        frame = frame.iloc[0:0].copy()
        frame["point_member_count"] = pd.Series(dtype="object")
    changed = _replace_application_frame(result, frame_name, frame)
    with pytest.raises(BessPlanningFeatureApplicationError, match="schema|dtype|index"):
        module._validate_result_envelope(changed)


@pytest.mark.parametrize(
    "mutation",
    [
        "missing-column",
        "unexpected-column",
        "reordered-columns",
        "float-object",
        "count-object",
        "official-category",
        "malformed-empty",
    ],
)
def test_application_relation_prefix_has_exact_canonical_schema(
    mutation: str,
) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    frame = result.relations.copy(deep=True)
    if mutation == "missing-column":
        frame = frame.drop(columns="label_raw")
    elif mutation == "unexpected-column":
        position = frame.columns.get_loc(POLICY_COLUMNS[0])
        frame.insert(position, "unexpected_factual", pd.array(["x"] * len(frame)))
    elif mutation == "reordered-columns":
        columns = list(frame.columns)
        columns[0], columns[1] = columns[1], columns[0]
        frame = frame.loc[:, columns]
    elif mutation == "float-object":
        frame["intersection_area_m2"] = pd.Series(
            frame["intersection_area_m2"].tolist(), index=frame.index, dtype="object"
        )
    elif mutation == "count-object":
        frame["point_member_count"] = pd.Series(
            frame["point_member_count"].tolist(), index=frame.index, dtype="object"
        )
    elif mutation == "official-category":
        frame["official_code_label"] = pd.Series(
            pd.Categorical(frame["official_code_label"]), index=frame.index
        )
    else:
        frame = frame.iloc[0:0].drop(columns="label_raw")
    changed = _replace_application_frame(result, "relations", frame)
    with pytest.raises(BessPlanningFeatureApplicationError, match="schema|dtype"):
        module._validate_result_envelope(changed)


def test_self_consistent_factual_prefix_dtype_artifact_is_rejected(
    tmp_path: Path,
) -> None:
    _, _, _, _, result = _application_fixture()
    surface = result.surface_features.copy(deep=True)
    surface["feature_area_m2"] = pd.Series(
        surface["feature_area_m2"].tolist(), index=surface.index, dtype="object"
    )
    changed = _replace_application_frame(result, "surface_features", surface)
    manifest, paths, _ = _write_application_artifacts(tmp_path, changed)
    with pytest.raises(BessPlanningFeatureApplicationError, match="schema|dtype"):
        load_bess_planning_feature_application_artifacts(
            manifest,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )


def test_lineage_defect_fast_fails_before_policy_source_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inputs, coded, config, policy, result = _application_fixture()
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    calls = 0

    def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1

    name, source, index = _zero_relation_feature(result)
    frame = source.copy(deep=True)
    frame.loc[index, "source_archive_sha256"] = "f" * 64
    changed = _replace_application_frame(result, name, frame)
    monkeypatch.setattr(module, "validate_bess_planning_feature_policy_result", counted)
    with pytest.raises(BessPlanningFeatureApplicationError):
        validate_bess_planning_feature_application_result(
            *inputs, coded, config, policy, changed
        )
    assert calls == 0


def test_step_7d_5b_2b_5_application_loader_requires_exact_upstreams() -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    assert tuple(
        inspect.signature(
            module.load_bess_planning_feature_application_artifacts
        ).parameters
    ) == (
        "manifest_path",
        "surface_features_path",
        "line_features_path",
        "point_features_path",
        "relations_path",
        "coded_result",
        "policy_result",
    )
    assert hasattr(module, "validate_bess_planning_feature_application_result_envelope")
    _, _, _, _, result = _application_fixture()
    module.validate_bess_planning_feature_application_result_envelope(result)
    with pytest.raises(BessPlanningFeatureApplicationError, match="hash|invalid"):
        module.validate_bess_planning_feature_application_result_envelope(
            replace(result, complete_result_content_sha256="0" * 64)
        )


def test_source_bound_application_loader_rejects_locally_valid_rationale_change(
    tmp_path: Path,
) -> None:
    _, coded, _, policy, result = _application_fixture()
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    changed = _coordinated_policy_mutation(
        result,
        "bess_cnig_rationale",
        "A different exact non-empty rationale.",
    )
    module._validate_result_envelope(changed)
    manifest, paths, _ = _write_application_artifacts(tmp_path, changed)
    with pytest.raises(BessPlanningFeatureApplicationError, match="upstream|rebuilt"):
        module.load_bess_planning_feature_application_artifacts(
            manifest,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
            coded,
            policy,
        )


def test_application_manifest_filenames_are_casefold_unique(tmp_path: Path) -> None:
    _, _, _, _, result = _application_fixture()
    _, _, payload = _write_application_artifacts(tmp_path, result)
    payload["artifacts"][1]["filename"] = str(
        payload["artifacts"][0]["filename"]
    ).upper()
    with pytest.raises(ValueError, match="filename|duplicate"):
        BessPlanningFeatureApplicationArtifactManifest.model_validate(payload)


def _swap_referenced_feature_values(
    result: BessPlanningFeatureApplicationResult,
    columns: tuple[str, ...],
) -> BessPlanningFeatureApplicationResult:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    referenced = result.relations.loc[
        result.relations["bess_cnig_policy_application_status"].eq(
            "APPLIED_EXACT_POLICY"
        )
    ]
    first = referenced.iloc[0]
    second = referenced.loc[
        referenced["bess_cnig_precheck_status"].ne(first["bess_cnig_precheck_status"])
    ].iloc[0]
    first_id = str(first["planning_feature_id"])
    second_id = str(second["planning_feature_id"])
    changed = result
    for frame_name in ("surface_features", "line_features", "point_features"):
        frame = getattr(changed, frame_name).copy(deep=True)
        first_mask = frame["planning_feature_id"].eq(first_id)
        second_mask = frame["planning_feature_id"].eq(second_id)
        if first_mask.any() or second_mask.any():
            for column in columns:
                first_value = first[column]
                second_value = second[column]
                frame.loc[first_mask, column] = second_value
                frame.loc[second_mask, column] = first_value
            changed = replace(changed, **{frame_name: frame})
    relations = changed.relations.copy(deep=True)
    first_mask = relations["planning_feature_id"].eq(first_id)
    second_mask = relations["planning_feature_id"].eq(second_id)
    for column in columns:
        first_value = first[column]
        second_value = second[column]
        relations.loc[first_mask, column] = second_value
        relations.loc[second_mask, column] = first_value
    return module._result_with_hashes(replace(changed, relations=relations))


@pytest.mark.parametrize(
    "columns",
    [
        (
            "bess_cnig_precheck_status",
            "bess_cnig_precheck_confidence",
            "bess_cnig_status_priority",
            "bess_cnig_rationale",
            "bess_cnig_required_human_action",
            "bess_cnig_limitations",
        ),
        (
            "official_code_label",
            "official_legal_reference",
            "official_regulation_reference",
            "official_code_source_url",
        ),
    ],
)
def test_source_bound_loader_rejects_valid_domain_cross_pair_swaps(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    columns: tuple[str, ...],
) -> None:
    _, coded, _, policy, result = _application_fixture()
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    changed = _swap_referenced_feature_values(result, columns)
    module._validate_result_envelope(changed)
    manifest, paths, _ = _write_application_artifacts(tmp_path, changed)
    heavy_calls = 0

    def forbidden_heavy(*args: object, **kwargs: object) -> None:
        nonlocal heavy_calls
        heavy_calls += 1

    monkeypatch.setattr(
        module, "validate_bess_planning_feature_policy_result", forbidden_heavy
    )
    with pytest.raises(BessPlanningFeatureApplicationError, match="upstream"):
        module.load_bess_planning_feature_application_artifacts(
            manifest,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
            coded,
            policy,
        )
    assert heavy_calls == 0


@pytest.mark.parametrize("column", ["source_provider", "source_portal"])
def test_source_bound_loader_rejects_factual_prefix_lineage_change(
    tmp_path: Path, column: str
) -> None:
    _, coded, _, policy, result = _application_fixture()
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    surface = result.surface_features.copy(deep=True)
    surface.loc[surface.index[0], column] = f"changed-{column}"
    changed = module._result_with_hashes(replace(result, surface_features=surface))
    module._validate_result_envelope(changed)
    manifest, paths, _ = _write_application_artifacts(tmp_path, changed)
    with pytest.raises(BessPlanningFeatureApplicationError, match="upstream"):
        module.load_bess_planning_feature_application_artifacts(
            manifest, *paths.values(), coded, policy
        )


def test_source_bound_loader_rejects_all_null_raw_column_transition(
    tmp_path: Path,
) -> None:
    _, coded, _, policy, _ = _application_fixture()
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    coding_module = importlib.import_module(
        "landscout.stages.resolve_planning_feature_codes"
    )
    policy_module = importlib.import_module(
        "landscout.stages.bess_planning_feature_policy"
    )
    coded_surface = coded.surface_features.copy(deep=True)
    coded_surface["text_raw"] = pd.Series(
        ["source text"] * len(coded_surface), index=coded_surface.index, dtype="str"
    )
    coded_relations = coded.relations.copy(deep=True)
    surface_ids = set(coded_surface["planning_feature_id"])
    coded_relations.loc[
        coded_relations["planning_feature_id"].isin(surface_ids), "text_raw"
    ] = "source text"
    coded_relations["text_raw"] = pd.Series(
        coded_relations["text_raw"].tolist(),
        index=coded_relations.index,
        dtype="str",
    )
    coded = coding_module._result_with_hashes(
        replace(
            coded,
            surface_features=coded_surface,
            relations=coded_relations,
        )
    )
    policy_table = policy.policy_table.copy(deep=True)
    policy_table["cnig_complete_result_content_sha256"] = pd.array(
        [coded.complete_result_content_sha256] * len(policy_table), dtype="str"
    )
    policy = policy_module._result_with_hashes(
        replace(
            policy,
            cnig_complete_result_content_sha256=coded.complete_result_content_sha256,
            policy_table=policy_table,
        )
    )
    result = module._build_result(coded, policy)
    surface = result.surface_features.copy(deep=True)
    surface["text_raw"] = pd.Series(None, index=surface.index, dtype="object")
    relations = result.relations.copy(deep=True)
    mask = relations["geometry_kind"].eq("SURFACE")
    relations.loc[mask, "text_raw"] = pd.NA
    relations["text_raw"] = pd.Series(
        relations["text_raw"].tolist(), index=relations.index, dtype="str"
    )
    changed = module._result_with_hashes(
        replace(result, surface_features=surface, relations=relations)
    )
    module._validate_result_envelope(changed)
    manifest, paths, _ = _write_application_artifacts(tmp_path, changed)
    with pytest.raises(BessPlanningFeatureApplicationError, match="upstream"):
        module.load_bess_planning_feature_application_artifacts(
            manifest, *paths.values(), coded, policy
        )

    reordered = result.surface_features.iloc[::-1].copy(deep=True)
    changed = module._result_with_hashes(replace(result, surface_features=reordered))
    module._validate_result_envelope(changed)
    reordered_dir = tmp_path / "reordered"
    reordered_dir.mkdir()
    manifest, paths, _ = _write_application_artifacts(reordered_dir, changed)
    with pytest.raises(BessPlanningFeatureApplicationError, match="upstream"):
        module.load_bess_planning_feature_application_artifacts(
            manifest, *paths.values(), coded, policy
        )


def test_source_bound_loader_rejects_unreferenced_feature_and_row_reordering(
    tmp_path: Path,
) -> None:
    _, coded, _, policy, result = _application_fixture()
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    name, source, index = _zero_relation_feature(result)
    unreferenced = source.copy(deep=True)
    unreferenced.loc[index, "label_raw"] = "changed unreferenced label"
    changed = module._result_with_hashes(replace(result, **{name: unreferenced}))
    module._validate_result_envelope(changed)
    unreferenced_dir = tmp_path / "unreferenced"
    unreferenced_dir.mkdir()
    manifest, paths, _ = _write_application_artifacts(unreferenced_dir, changed)
    with pytest.raises(BessPlanningFeatureApplicationError, match="upstream"):
        module.load_bess_planning_feature_application_artifacts(
            manifest, *paths.values(), coded, policy
        )


def test_application_loader_validates_upstreams_and_rebuilds_once_lightweight(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _, coded, _, policy, result = _application_fixture()
    manifest, paths, _ = _write_application_artifacts(tmp_path, result)
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    coded_before = coded.surface_features.copy(deep=True)
    policy_before = policy.policy_table.copy(deep=True)
    actual_coded_envelope = module.validate_planning_feature_code_result_envelope
    actual_policy_envelope = (
        module.validate_bess_planning_feature_policy_result_envelope
    )
    actual_build = module._build_result
    calls = {"coded": 0, "policy": 0, "build": 0, "heavy": 0}

    def coded_envelope(value: object) -> None:
        calls["coded"] += 1
        actual_coded_envelope(value)

    def policy_envelope(value: object) -> None:
        calls["policy"] += 1
        actual_policy_envelope(value)

    def build(*args: object, **kwargs: object) -> object:
        calls["build"] += 1
        return actual_build(*args, **kwargs)

    def heavy(*args: object, **kwargs: object) -> None:
        calls["heavy"] += 1

    monkeypatch.setattr(
        module, "validate_planning_feature_code_result_envelope", coded_envelope
    )
    monkeypatch.setattr(
        module,
        "validate_bess_planning_feature_policy_result_envelope",
        policy_envelope,
    )
    monkeypatch.setattr(module, "_build_result", build)
    monkeypatch.setattr(module, "validate_bess_planning_feature_policy_result", heavy)
    loaded = module.load_bess_planning_feature_application_artifacts(
        manifest, *paths.values(), coded, policy
    )
    assert (
        loaded.complete_result_content_sha256 == result.complete_result_content_sha256
    )
    assert calls == {"coded": 1, "policy": 1, "build": 1, "heavy": 0}
    assert_geodataframe_equal(coded.surface_features, coded_before)
    assert_frame_equal(policy.policy_table, policy_before)


def test_application_loader_rejects_bad_upstream_before_artifact_reads(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _, coded, _, policy, result = _application_fixture()
    manifest, paths, _ = _write_application_artifacts(tmp_path, result)
    reads = 0
    original = Path.read_bytes

    def counted(path: Path) -> bytes:
        nonlocal reads
        reads += 1
        return original(path)

    monkeypatch.setattr(Path, "read_bytes", counted)
    forged = replace(coded, complete_result_content_sha256="0" * 64)
    with pytest.raises(Exception, match="hash|SHA|invalid"):
        _load_application_artifacts(manifest, *paths.values(), forged, policy)
    assert reads == 0


@pytest.mark.parametrize(
    "filename",
    [
        "/tmp/file.parquet",
        "../file.parquet",
        "subdir/file.parquet",
        r"C:\absolute\file.parquet",
        "C:/absolute/file.parquet",
        r"\\server\share\file.parquet",
        r"subdir\file.parquet",
        "CON.parquet",
        "con.PARQUET",
        "NUL.parquet",
        "PRN.parquet",
        "AUX.parquet",
        "CLOCK$.parquet",
        "COM1.parquet",
        "COM9.parquet",
        "LPT1.parquet",
        "LPT9.parquet",
        "COM¹.parquet",
        "COM².parquet",
        "COM³.parquet",
        "LPT¹.parquet",
        "LPT².parquet",
        "LPT³.parquet",
        "file:name.parquet",
        "base.parquet:stream.parquet",
        "file?.parquet",
        "file*.parquet",
        "file<.parquet",
        "file>.parquet",
        "file|.parquet",
        'file".parquet',
        "nul\x00.parquet",
        "line\nbreak.parquet",
        "del\x7f.parquet",
    ],
)
def test_application_manifest_rejects_nonportable_filename(
    tmp_path: Path, filename: str
) -> None:
    _, _, _, _, result = _application_fixture()
    _, _, payload = _write_application_artifacts(tmp_path, result)
    payload["artifacts"][0]["filename"] = filename
    with pytest.raises(ValueError, match="filename|basename|portable"):
        BessPlanningFeatureApplicationArtifactManifest.model_validate(payload)


def _compatible_policy_mutation(policy: object, mutation: str) -> object:
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    table = policy.policy_table.copy(deep=True)
    scalar_changes: dict[str, object] = {}
    if mutation == "profile-schema":
        scalar_changes["cnig_profile_schema_version"] = 3
    elif mutation == "extra-pair":
        extra = table.iloc[[0]].copy(deep=True)
        extra["type_code"] = pd.array(["98"], dtype="str")
        table = pd.concat([table, extra], ignore_index=True).sort_values(
            ["feature_family", "type_code", "subtype_code"], kind="stable"
        )
        table.index = pd.Index(table.index.to_numpy(), dtype="int64")
    elif mutation == "missing-pair":
        table = table.iloc[:-1].copy(deep=True)
        table.index = pd.Index(range(len(table)), dtype="int64")
    elif mutation == "official-label":
        table.loc[table.index[0], "official_label"] = "Another exact official label"
    elif mutation == "legal-reference":
        table.loc[table.index[0], "official_legal_reference"] = "Changed legal ref"
    elif mutation == "regulation-reference":
        table.loc[table.index[0], "official_regulation_reference"] = (
            "Changed regulation ref"
        )
    elif mutation == "document":
        scalar_changes["source_document_id"] = "OTHER-DOCUMENT"
    elif mutation == "archive":
        scalar_changes["source_archive_sha256"] = "b" * 64
    elif mutation == "profile":
        scalar_changes["cnig_profile"] = "other-cnig-profile"
        table["cnig_profile"] = pd.array(
            ["other-cnig-profile"] * len(table), dtype="str"
        )
    elif mutation == "profile-sha":
        scalar_changes["cnig_profile_sha256"] = "a" * 64
        table["cnig_profile_sha256"] = pd.array(["a" * 64] * len(table), dtype="str")
    else:
        scalar_changes["cnig_complete_result_content_sha256"] = "a" * 64
        table["cnig_complete_result_content_sha256"] = pd.array(
            ["a" * 64] * len(table), dtype="str"
        )
    changed = replace(policy, policy_table=table, **scalar_changes)
    return module._result_with_hashes(changed)


@pytest.mark.parametrize(
    "mutation",
    [
        "profile-schema",
        "extra-pair",
        "missing-pair",
        "official-label",
        "legal-reference",
        "regulation-reference",
        "document",
        "archive",
        "profile",
        "profile-sha",
        "complete-result-sha",
    ],
)
def test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    mutation: str,
) -> None:
    _, coded, _, policy, result = _application_fixture()
    manifest, paths, _ = _write_application_artifacts(tmp_path, result)
    changed_policy = _compatible_policy_mutation(policy, mutation)
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    calls = {"manifest": 0, "read": 0, "build": 0, "heavy": 0}

    def manifest_read(*args: object, **kwargs: object) -> str:
        calls["manifest"] += 1
        raise AssertionError("manifest read must not run")

    def read(*args: object, **kwargs: object) -> object:
        calls["read"] += 1
        raise AssertionError("artifact read must not run")

    def build(*args: object, **kwargs: object) -> object:
        calls["build"] += 1
        raise AssertionError("application rebuild must not run")

    def heavy(*args: object, **kwargs: object) -> None:
        calls["heavy"] += 1

    monkeypatch.setattr(module, "_read_verified_artifact", read)
    monkeypatch.setattr(module, "_build_result", build)
    monkeypatch.setattr(module, "validate_bess_planning_feature_policy_result", heavy)
    monkeypatch.setattr(Path, "read_text", manifest_read)
    with pytest.raises(
        BessPlanningFeatureApplicationError,
        match="Policy|policy|CNIG|pair|source|schema|official|reference",
    ):
        module.load_bess_planning_feature_application_artifacts(
            manifest, *paths.values(), coded, changed_policy
        )
    assert calls == {"manifest": 0, "read": 0, "build": 0, "heavy": 0}


@pytest.mark.parametrize("empty_upstream", ["coded", "policy", "both"])
def test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    empty_upstream: str,
) -> None:
    _, coded, _, policy, result = _application_fixture()
    manifest, paths, _ = _write_application_artifacts(tmp_path, result)
    if empty_upstream in {"coded", "both"}:
        coded = _canonical_empty_coded_result(coded, empty_dictionary=True)
    if empty_upstream in {"policy", "both"}:
        policy = _canonical_empty_policy_result(policy)
    if empty_upstream == "both":
        policy_module = importlib.import_module(
            "landscout.stages.bess_planning_feature_policy"
        )
        policy = policy_module._result_with_hashes(
            replace(
                policy,
                cnig_complete_result_content_sha256=(
                    coded.complete_result_content_sha256
                ),
            )
        )
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    calls = {"manifest": 0, "read": 0, "build": 0, "heavy": 0}

    def manifest_read(*args: object, **kwargs: object) -> str:
        calls["manifest"] += 1
        raise AssertionError("manifest read must not run")

    def artifact_read(*args: object, **kwargs: object) -> object:
        calls["read"] += 1
        raise AssertionError("Parquet read must not run")

    def build(*args: object, **kwargs: object) -> object:
        calls["build"] += 1
        raise AssertionError("application rebuild must not run")

    def heavy(*args: object, **kwargs: object) -> None:
        calls["heavy"] += 1

    monkeypatch.setattr(Path, "read_text", manifest_read)
    monkeypatch.setattr(module, "_read_verified_artifact", artifact_read)
    monkeypatch.setattr(module, "_build_result", build)
    monkeypatch.setattr(module, "validate_bess_planning_feature_policy_result", heavy)
    with pytest.raises(
        BessPlanningFeatureApplicationError,
        match="dictionary|policy|table|pair|empty|record|entry",
    ):
        module.load_bess_planning_feature_application_artifacts(
            manifest, *paths.values(), coded, policy
        )
    assert calls == {"manifest": 0, "read": 0, "build": 0, "heavy": 0}
```
