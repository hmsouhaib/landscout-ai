# `tests/unit/test_resolve_planning_feature_codes.py`

- Source: [tests/unit/test_resolve_planning_feature_codes.py](../../../../../tests/unit/test_resolve_planning_feature_codes.py)
- Source SHA256: `f089c7cf174ecf5fa745d5909f817884a6c9df6d52f0e53f8702a639106e574c`
- Source SHA256 basis: `git-content`
- Source lines: 2310; Git blob at R12 start: `44fd1331e011d98b46b926d6529571ade927e9b6`

Git/index/checkout Python bytes remain unchanged. Local semantic closure is not independent approval. [R12 receipt](../../../../../docs/code/audit/R12_CNIG_FEATURE_CODE_RESOLVER.md).

## Evidence scope and fixture ownership

This file has 74 test functions, no decorator-declared pytest fixtures, 101 inventoried functions (including nested callbacks) and one nested class: 102 symbols. Ordinary helper functions are local; no helper is imported from another test file. tmp_path and monkeypatch are pytest-provided. Test-local six/seven-argument wrappers insert a parcel frame; actual production resolver/full validator have seven/eight required inputs. Parameter expansion is reported only from the single authorized execution in the [R12 receipt](../../../audit/R12_CNIG_FEATURE_CODE_RESOLVER.md).

The active _inputs chain uses _integration_inputs and real public factual normalization of synthetic GPKGs. _planning_document writes and Pyogrio-rereads GeoPackages, creates an extraction manifest, loads/revalidates a modified GPU config and returns synthetic source-bound objects. It uses tempfile.mkdtemp outside pytest basetemp; this document does not claim automatic removal of those helper directories. Archive fields are fabricated fixtures, not downloaded official archive bytes. The legacy handwritten helper is not the active chain. Two tests write/reload five Parquet tables with index=True; no production artifact loader/manifest is being tested.

Repository owners imported here are GPU model/config helpers, factual planning schema/normalizer, source-layer summary and the [CNIG resolver](../../src/landscout/stages/resolve_planning_feature_codes.py.md), plus package exports. Standard-library helpers handle tempfile/shutil/path/hash/JSON/importlib/dataclass/introspection; pandas/GeoPandas, Shapely, YAML and pytest own their actual methods. No direct NumPy/PyProj import exists in this test file. Calls to str.replace, Series.eq, set.isdisjoint or geometry array private _crs are not inferred as filesystem writes or spatial overlays. Each literal signature, decorator and expected-exception expression below is extracted from the unchanged body after semantic reading; source snapshot alone is not the review.

The module tests schema/type/text/identity/geometry constraints, exact code lookup, profile reconstruction, nonmutation during coding, source-bound rebuild, local envelope and hash dependencies. Tests never create BESS legal permission, parcel ranking or official-source freshness. [R4 limits](../../../audit/R4_CNIG_CONFIGURATION.md), A-003/A-004 and existing historical reservations remain; source/tests are unchanged.

## Explicit proof limits

- R12-T01: The cross-family-named case removes exact triples but creates no competing inter-family collision. Titles do not enlarge assertions.
- R12-T02: The raising shared-contract sentinel proves invocation/wrapping, whereas delegating spies prove one/two owner calls; neither counts actual disk reads. Setup writes physical fixtures even in envelope-only tests.
- R12-T03: Several broad-regex negatives can fail earlier schema/identity/metric guards. Missing relations retain a noncanonical RangeIndex start; extra relations use unknown parcel. Stale source hashes and coordinated label-only reseal can fail the local envelope before physical rebuild.
- R12-T04: Signature test asserts parameter names/order only; hash-presence test checks hex shape only; root-relocation test asserts one GPU-related digest only. They do not prove defaults, canonical payload recomputation or every hash root-independent.
- R12-T05: Preservation asserts no mutation during a call, not deep immutability; multi-geometry equals is topological, not M/Z byte fidelity; checked-in snapshot constants are offline configuration evidence, not live official/legal research.

These are bounded coverage explanations, not new application bugs or authorization to edit tests. The envelope-empty-output acceptance intentionally separates local consistency from complete physical reconstruction. No imported fixture/gate bypass is invented.

## Module declarations

Exact imports are preserved in the full snapshot. Declarations add no extra historical closure units.

<a id="declaration-p-url"></a>
### `tests.unit.test_resolve_planning_feature_codes.P_URL`

Source lines 76–76. Exact prescription endpoint fixture string.

```python
P_URL = "https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/PrescriptionUrbaType"
```

<a id="declaration-i-url"></a>
### `tests.unit.test_resolve_planning_feature_codes.I_URL`

Source lines 77–77. Exact information endpoint fixture string.

```python
I_URL = "https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/InformationUrbaType"
```

<a id="declaration-text-normalization"></a>
### `tests.unit.test_resolve_planning_feature_codes.TEXT_NORMALIZATION`

Source lines 78–78. Actual module-level fixture/import binding, not an extra public export or closure unit; exact expression follows.

```python
TEXT_NORMALIZATION = "GPU_DISPLAY_TEXT_NFC_WHITESPACE_V1"
```

## Qualified symbol contracts

Each original symbol has a notice and matching owner note. Literal signatures specify actual parameters, defaults, annotations and returns; missing annotations are not None annotations. Private helpers have only the guards/wrappers stated, not universal exception translation.

<a id="_canonical_relation_schema"></a>

<a id="symbol--canonical-relation-schema"></a>
### `tests.unit.test_resolve_planning_feature_codes._canonical_relation_schema`

Source lines 66–73. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def _canonical_relation_schema(frame: pd.DataFrame) -> pd.DataFrame:
```

Deep-copy supplied relation frame, cast each of 28 normalized columns using strict zip against declared dtypes, reset to canonical RangeIndex and return. No column deletion or validation beyond casting; intended fixture normalization, not public production validator.

<a id="_records_hash"></a>

<a id="symbol--records-hash"></a>
### `tests.unit.test_resolve_planning_feature_codes._records_hash`

Source lines 81–93. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def _records_hash(records: list[dict[str, object]]) -> str:
```

Sort a new list by exact family/type/subtype, canonical JSON and SHA256. This fixture helper sorts, unlike production which requires declaration order already sorted; allow_nan=False. Does not mutate caller list.

<a id="_payload_hash"></a>

<a id="symbol--payload-hash"></a>
### `tests.unit.test_resolve_planning_feature_codes._payload_hash`

Source lines 96–105. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def _payload_hash(payload: object) -> str:
```

Canonical JSON SHA256 with default=str for synthetic JSON-friendly payloads. This test helper is not the production arbitrary-value canonicalizer or raw-byte hash.

<a id="_record"></a>

<a id="symbol--record"></a>
### `tests.unit.test_resolve_planning_feature_codes._record`

Source lines 108–122. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def _record(
    family: str,
    type_code: str,
    subtype_code: str,
    label: str,
) -> dict[str, object]:
```

Construct seven-field mutable dict with supplied family/type/subtype/label, two None references and selected family endpoint. No model validation until fixture profile construction.

<a id="_profile_payload"></a>

<a id="symbol--profile-payload"></a>
### `tests.unit.test_resolve_planning_feature_codes._profile_payload`

Source lines 125–144. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def _profile_payload() -> dict[str, object]:
```

Create synthetic schema2 profile, date2026-08-12 and four sorted records: INFORMATION02/00,99/00 and PRESCRIPTION07/00,07/04; compute declared record hash. No official download.

<a id="_profile"></a>

<a id="symbol--profile"></a>
### `tests.unit.test_resolve_planning_feature_codes._profile`

Source lines 147–148. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def _profile() -> CnigFeatureCodeProfile:
```

Model-validate the synthetic profile payload and return frozen profile. Validation errors are not swallowed.

<a id="_physical_inventory"></a>

<a id="symbol--physical-inventory"></a>
### `tests.unit.test_resolve_planning_feature_codes._physical_inventory`

Source lines 151–164. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def _physical_inventory(root: Path) -> tuple[GpuExtractedFile, ...]:
```

Enumerate root.rglob("*"), retain candidates for which item.is_file() is true, then sort by str. Exclude only paths satisfying path.parent == root and path.name == EXTRACTION_MANIFEST_NAME; the imported `landscout.sources.gpu_fr.EXTRACTION_MANIFEST_NAME` equals ".landscout-gpu-extraction.json". A same-named file below another directory is not excluded by this condition. Read each retained file to record relative POSIX path, extension/size/SHA and spatial category; return a tuple of file records. No lstat or explicit symlink-rejection guard is implemented here. This is real synthetic file I/O, not official archive evidence.

<a id="_write_extraction_manifest"></a>

<a id="symbol--write-extraction-manifest"></a>
### `tests.unit.test_resolve_planning_feature_codes._write_extraction_manifest`

Source lines 167–190. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def _write_extraction_manifest(
    root: Path,
    archive_sha256: str,
    files: tuple[GpuExtractedFile, ...],
) -> None:
```

Write schema-2 JSON to root / EXTRACTION_MANIFEST_NAME, using the imported `landscout.sources.gpu_fr.EXTRACTION_MANIFEST_NAME` value ".landscout-gpu-extraction.json". Include archive SHA and inventory relative paths/sizes/hashes as compact sorted JSON UTF-8. This is a real synthetic filesystem write, not a production extraction operation.

<a id="_layer_summary"></a>

<a id="symbol--layer-summary"></a>
### `tests.unit.test_resolve_planning_feature_codes._layer_summary`

Source lines 193–217. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def _layer_summary(frame: gpd.GeoDataFrame, source_layer: str) -> GpuLayerSummary:
```

Build GpuLayerSummary from actual frame counts/CRS/geometry and per-column dtype/null counts, with synthetic document/archive lineage. In-memory summary, not fresh physical verification.

<a id="_planning_document"></a>

<a id="symbol--planning-document"></a>
### `tests.unit.test_resolve_planning_feature_codes._planning_document`

Source lines 220–336. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def _planning_document(
    standard: str = "CNIG PLU v2017",
    related_layers: tuple[GpuInspectedLayer, ...] = (),
) -> GpuPlanningDocument:
```

Create fresh tempfile.mkdtemp(prefix="landscout-code-source-") outside the explicit pytest basetemp; write and reread related GPKGs through Pyogrio, make references/summaries, write and reread physical layer ZONE in zones.gpkg and wrap it as logical role zoning, then build the inventory and extraction manifest. Load checked-in GPU config, alter match tokens via dumped payload, revalidate/hash config, discover spatial references and return synthetic GpuPlanningDocument. Uses fictional archive metadata/path rather than archive acquisition. No helper cleanup is declared; no blanket all-files-under-basetemp claim.

<a id="_base_row"></a>

<a id="symbol--base-row"></a>
### `tests.unit.test_resolve_planning_feature_codes._base_row`

Source lines 339–376. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def _base_row(
    feature_id: str,
    source_id: str,
    family: str,
    layer: str,
    kind: str,
    type_code: str,
    subtype_code: str,
) -> dict[str, object]:
```

Return handwritten legacy normalized raw identity/lineage/text fields. Used by _legacy_inputs, not the active physical-source fixture chain; no file I/O.

<a id="_legacy_inputs"></a>

<a id="symbol--legacy-inputs"></a>
### `tests.unit.test_resolve_planning_feature_codes._legacy_inputs`

Source lines 379–520. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def _legacy_inputs():
```

Construct handwritten catalogs and relations with custom indexes plus a zoning-only synthetic physical document and profile. This legacy six-item helper is not called by active _inputs, so its rows do not describe executed public-fixture coverage.

<a id="_mutated_profile"></a>

<a id="symbol--mutated-profile"></a>
### `tests.unit.test_resolve_planning_feature_codes._mutated_profile`

Source lines 523–527. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def _mutated_profile(**updates: object) -> CnigFeatureCodeProfile:
```

Return profile.model_copy(update=changes), intentionally bypassing validation. The public resolver must reconstruct it; helper itself does not catch or assert errors.

<a id="_empty_catalog"></a>

<a id="symbol--empty-catalog"></a>
### `tests.unit.test_resolve_planning_feature_codes._empty_catalog`

Source lines 530–535. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def _empty_catalog(kind: str) -> gpd.GeoDataFrame:
```

Call active _inputs then select requested kind and return empty copy; setup can create physical GPKGs even though returned frame is empty. Not a production empty-catalog API.

<a id="_integration_source_frame"></a>

<a id="symbol--integration-source-frame"></a>
### `tests.unit.test_resolve_planning_feature_codes._integration_source_frame`

Source lines 538–560. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def _integration_source_frame(
    logical_layer: str,
    geometries: list[object],
    source_ids: list[str],
    type_codes: list[str],
    subtype_codes: list[str],
) -> gpd.GeoDataFrame:
```

Construct EPSG:2154 source GeoDataFrame with actual CNIG raw fields, supplied identifiers/geometries/codes and null TXT/NOMFIC/URLFIC. No write here; later document helper writes it.

<a id="_integration_layer"></a>

<a id="symbol--integration-layer"></a>
### `tests.unit.test_resolve_planning_feature_codes._integration_layer`

Source lines 563–595. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def _integration_layer(
    logical_layer: str,
    frame: gpd.GeoDataFrame,
) -> GpuInspectedLayer:
```

Construct in-memory inspected layer/reference/summary from source frame, logical family and synthetic metadata. Subsequent _planning_document replaces with written/reread physical fixtures.

<a id="_integration_inputs"></a>

<a id="symbol--integration-inputs"></a>
### `tests.unit.test_resolve_planning_feature_codes._integration_inputs`

Source lines 598–662. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def _integration_inputs() -> tuple[
    GpuPlanningDocument,
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    pd.DataFrame,
    CnigFeatureCodeProfile,
]:
```

Create four related layers (two surface features including off-parcel feature, one line, one point), fresh physical document, one synthetic parcel and run real intersect_parcels_with_gpu_planning_features. Return seven inputs including source-complete factual frames and profile. No real Muret/official archive processing.

<a id="_integration_parcels"></a>

<a id="symbol--integration-parcels"></a>
### `tests.unit.test_resolve_planning_feature_codes._integration_parcels`

Source lines 665–671. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def _integration_parcels() -> gpd.GeoDataFrame:
```

Return one EPSG:2154 square parcel area4m2 with parcel_id, existing_fact7 and index91 named parcel_row. New independent frame on each call.

<a id="_inputs"></a>

<a id="symbol--inputs"></a>
### `tests.unit.test_resolve_planning_feature_codes._inputs`

Source lines 674–683. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def _inputs() -> tuple[
    GpuPlanningDocument,
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    pd.DataFrame,
    CnigFeatureCodeProfile,
]:
```

Call _integration_inputs, omit parcels and return legacy-shaped six-argument tuple. Despite historical helper naming, its catalogs/relations originate in real normalization of synthetic physical sources.

<a id="resolve_planning_feature_codes"></a>

<a id="symbol-resolve-planning-feature-codes"></a>
### `tests.unit.test_resolve_planning_feature_codes.resolve_planning_feature_codes`

Source lines 686–704. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def resolve_planning_feature_codes(
    planning_document: GpuPlanningDocument,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
) -> PlanningFeatureCodeResult:
```

Test-local six-argument convenience wrapper inserts fresh _integration_parcels then calls aliased production resolver with seven arguments. Not the production owner or changed public signature.

<a id="validate_planning_feature_code_result"></a>

<a id="symbol-validate-planning-feature-code-result"></a>
### `tests.unit.test_resolve_planning_feature_codes.validate_planning_feature_code_result`

Source lines 707–725. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def validate_planning_feature_code_result(
    planning_document: GpuPlanningDocument,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
    result: PlanningFeatureCodeResult,
) -> None:
```

Test-local seven-argument wrapper inserts parcel fixture then invokes aliased eight-argument public full validator. Real source-complete validation is retained.

<a id="test_exact_family_pair_resolution_and_leading_zeros"></a>

<a id="symbol-test-exact-family-pair-resolution-and-leading-zeros"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_exact_family_pair_resolution_and_leading_zeros`

Source lines 728–745. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_exact_family_pair_resolution_and_leading_zeros() -> None:
```

Resolve active fixtures and index surfaces by planning_feature_id. Assert that GPU:doc-1:prescription_surface:P-1 has official_code_label "Prescription seven" and GPU:doc-1:information_surface:I-1 has "Information two". Assert that the first line has official_code_label "Prescription seven subtype four", type_code_raw "07" and subtype_code_raw "04"; assert that the set of surface official_code_status values is {"RESOLVED_OFFICIAL"}. The two surface-ID lookups are not a cardinality assertion, and no raw surface 07/00 pair is directly asserted. Point meaning is not asserted here. No wildcard or legal-status inference.

<a id="test_no_type_only_or_cross_family_fallback_and_unknown_is_retained"></a>

<a id="symbol-test-no-type-only-or-cross-family-fallback-and-unknown-is-retained"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_no_type_only_or_cross_family_fallback_and_unknown_is_retained`

Source lines 748–768. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_no_type_only_or_cross_family_fallback_and_unknown_is_retained() -> None:
```

Remove PRESCRIPTION07/04 and INFORMATION99/00, reseal records digest and validate profile, resolve; assert line/point UNKNOWN, line null label and one retained row each. The fixture creates no same-pair competing family, so title does not prove inter-family collision handling (R4 limit retained).

<a id="test_in_memory_profile_model_copy_with_wrong_hash_is_revalidated"></a>

<a id="symbol-test-in-memory-profile-model-copy-with-wrong-hash-is-revalidated"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_in_memory_profile_model_copy_with_wrong_hash_is_revalidated`

Source lines 771–775. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_in_memory_profile_model_copy_with_wrong_hash_is_revalidated() -> None:
```

Replace declared records digest by f*64 through unvalidated model_copy; resolver must raise profile/canonical error before factual reconstruction.

Exact expected-exception contexts:

```python
pytest.raises(PlanningFeatureCodeError, match="profile|canonical")
```

<a id="test_in_memory_profile_model_construct_with_invalid_schema_is_revalidated"></a>

<a id="symbol-test-in-memory-profile-model-construct-with-invalid-schema-is-revalidated"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_in_memory_profile_model_construct_with_invalid_schema_is_revalidated`

Source lines 778–786. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_in_memory_profile_model_construct_with_invalid_schema_is_revalidated() -> None:
```

Use model_construct with schema_version1 and otherwise profile values; public resolver rejects during supplied-profile reconstruction.

Exact expected-exception contexts:

```python
pytest.raises(PlanningFeatureCodeError, match="schema|profile")
```

<a id="test_in_memory_profile_model_construct_with_duplicate_pair_is_revalidated"></a>

<a id="symbol-test-in-memory-profile-model-construct-with-duplicate-pair-is-revalidated"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_in_memory_profile_model_construct_with_duplicate_pair_is_revalidated`

Source lines 789–800. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_in_memory_profile_model_construct_with_duplicate_pair_is_revalidated() -> None:
```

Append duplicate record through model_construct without recomputing the original records hash; public resolver must reject duplicate/profile. The duplicate guard precedes checksum comparison during profile reconstruction.

Exact expected-exception contexts:

```python
pytest.raises(PlanningFeatureCodeError, match="duplicate|profile")
```

<a id="test_official_family_endpoints_require_exact_identity"></a>

<a id="symbol-test-official-family-endpoints-require-exact-identity"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_official_family_endpoints_require_exact_identity`

Source lines 827–838. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_official_family_endpoints_require_exact_identity(
    family: str, url: str
) -> None:
```

Ten parameter cases mutate family endpoint and all matching record URLs, then reseal record digest; model_validate must raise ValueError matching official/source/URL. Covers alternate path/query/port/credentials/host/family/fragment/trailing slash/http, not network safety or live endpoint availability.

Exact decorators (not extra units):

```python
@pytest.mark.parametrize(
    ("family", "url"),
    [
        ("prescription", "https://www.geoportail-urbanisme.gouv.fr/another/path"),
        ("prescription", f"{P_URL}?format=json"),
        (
            "prescription",
            "https://www.geoportail-urbanisme.gouv.fr:444/standard/cnig_PLU_2017/codes/PrescriptionUrbaType",
        ),
        (
            "prescription",
            "https://user@www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/PrescriptionUrbaType",
        ),
        (
            "prescription",
            "https://geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/PrescriptionUrbaType",
        ),
        ("prescription", I_URL),
        ("information", P_URL),
        ("information", f"{I_URL}#codes"),
        ("information", f"{I_URL}/"),
        ("information", I_URL.replace("https://", "http://")),
    ],
)
```

Exact expected-exception contexts:

```python
pytest.raises(ValueError, match="official|source|URL")
```

<a id="test_official_text_must_already_be_canonical"></a>

<a id="symbol-test-official-text-must-already-be-canonical"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_official_text_must_already_be_canonical`

Source lines 850–858. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_official_text_must_already_be_canonical(field: str, value: str) -> None:
```

Four cases mutate label double whitespace/decomposed accent, legal newline whitespace or leading annex space; reseal records digest; model_validate must reject canonical-text violation, not normalize accepted records.

Exact decorators (not extra units):

```python
@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("official_label", "Repeated  whitespace"),
        ("official_label", "Decomposed e\u0301"),
        ("legal_reference", "L151-1\n  L151-2"),
        ("regulation_or_annex_reference", " R151-1"),
    ],
)
```

Exact expected-exception contexts:

```python
pytest.raises(
        ValueError,
        match="GPU_DISPLAY_TEXT_NFC_WHITESPACE_V1|canonical|normalization|exact",
    )
```

<a id="test_malformed_code_is_rejected"></a>

<a id="symbol-test-malformed-code-is-rejected"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_malformed_code_is_rejected`

Source lines 862–866. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_malformed_code_is_rejected(code: object) -> None:
```

Set first type_code to 1-digit, 3-digit, nonnumeric, leading/trailing space or integer1; no reseal. Broad ValueError expected; nested field/code validation can reject before record hash.

Exact decorators (not extra units):

```python
@pytest.mark.parametrize("code", ["1", "001", "A1", " 01", "01 ", 1])
```

Exact expected-exception contexts:

```python
pytest.raises(ValueError)
```

<a id="test_duplicate_pair_and_profile_hash_mutation_are_rejected"></a>

<a id="symbol-test-duplicate-pair-and-profile-hash-mutation-are-rejected"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_duplicate_pair_and_profile_hash_mutation_are_rejected`

Source lines 869–877. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_duplicate_pair_and_profile_hash_mutation_are_rejected() -> None:
```

Two fresh payloads: append duplicate record without resealing and expect duplicate error; independently replace declared hash with f*64 and expect canonical error. Does not use public source reconstruction.

Exact expected-exception contexts:

```python
pytest.raises(ValueError, match="duplicate")
pytest.raises(ValueError, match="canonical")
```

<a id="test_wrong_official_host_and_unknown_field_are_rejected"></a>

<a id="symbol-test-wrong-official-host-and-unknown-field-are-rejected"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_wrong_official_host_and_unknown_field_are_rejected`

Source lines 880–888. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_wrong_official_host_and_unknown_field_are_rejected() -> None:
```

Replace declared prescription endpoint with example.com and expect official/exact ValueError; separate payload adds semantic_policy and expects extra-field ValueError. Offline identity validation only.

Exact expected-exception contexts:

```python
pytest.raises(ValueError, match="official|exact")
pytest.raises(ValueError)
```

<a id="test_duplicate_yaml_key_is_rejected"></a>

<a id="symbol-test-duplicate-yaml-key-is-rejected"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_duplicate_yaml_key_is_rejected`

Source lines 891–895. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_duplicate_yaml_key_is_rejected(tmp_path: Path) -> None:
```

Write schema_version twice to tmp_path YAML, then loader must raise Duplicate YAML error before ordinary schema-version checking. Real local file read/write.

Exact expected-exception contexts:

```python
pytest.raises(PlanningFeatureCodeError, match="Duplicate YAML")
```

<a id="test_wrong_planning_standard_is_rejected"></a>

<a id="symbol-test-wrong-planning-standard-is-rejected"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_wrong_planning_standard_is_rejected`

Source lines 898–902. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_wrong_planning_standard_is_rejected() -> None:
```

Create synthetic physical document declaring v2022, then public resolver rejects standard mismatch before shared factual gate; file setup itself already wrote sources.

Exact expected-exception contexts:

```python
pytest.raises(PlanningFeatureCodeError, match="standard")
```

<a id="test_catalogs_and_relations_are_preserved_and_inputs_immutable"></a>

<a id="symbol-test-catalogs-and-relations-are-preserved-and-inputs-immutable"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_catalogs_and_relations_are_preserved_and_inputs_immutable`

Source lines 905–923. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_catalogs_and_relations_are_preserved_and_inputs_immutable() -> None:
```

Deep-copy four input frames before resolve; assert originals unchanged, output factual-column slices frame-equal including geometry, appended official suffix/dictionary order and index values preserved. Proves nonmutation by this call, not impossibility of mutating returned DataFrames.

<a id="test_complete_normalized_catalog_schema_is_required"></a>

<a id="symbol-test-complete-normalized-catalog-schema-is-required"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_complete_normalized_catalog_schema_is_required`

Source lines 936–943. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_complete_normalized_catalog_schema_is_required(
    catalog_position: int,
    column: str,
) -> None:
```

Five cases drop surface area/label/source_crs, line length or point member column. Resolve expects normalized/schema/column error; schema guard can fail before physical reconstruction.

Exact decorators (not extra units):

```python
@pytest.mark.parametrize(
    ("catalog_position", "column"),
    [
        (1, "feature_area_m2"),
        (2, "feature_length_m"),
        (3, "point_member_count"),
        (1, "label_raw"),
        (1, "source_crs"),
    ],
)
```

Exact expected-exception contexts:

```python
pytest.raises(PlanningFeatureCodeError, match="normalized|schema|column")
```

<a id="test_unexpected_factual_catalog_column_is_rejected"></a>

<a id="symbol-test-unexpected-factual-catalog-column-is-rejected"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_unexpected_factual_catalog_column_is_rejected`

Source lines 946–952. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_unexpected_factual_catalog_column_is_rejected() -> None:
```

Add unexpected factual surface column; resolver must reject canonical schema rather than preserve an arbitrary extra input column.

Exact expected-exception contexts:

```python
pytest.raises(PlanningFeatureCodeError, match="normalized|schema|column")
```

<a id="test_cnig_identity_provenance_is_exact"></a>

<a id="symbol-test-cnig-identity-provenance-is-exact"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_cnig_identity_provenance_is_exact`

Source lines 962–970. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_cnig_identity_provenance_is_exact(column: str, value: str) -> None:
```

Mutate source_identity_kind to UNKNOWN_KIND or source_identity_field to LIB_IDINFO in surface; resolve rejects identity/provenance/normalized contract, without resealing any result.

Exact decorators (not extra units):

```python
@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("source_identity_kind", "UNKNOWN_KIND"),
        ("source_identity_field", "LIB_IDINFO"),
    ],
)
```

Exact expected-exception contexts:

```python
pytest.raises(
        PlanningFeatureCodeError, match="identity|provenance|normalized"
    )
```

<a id="test_ogr_fid_provenance_is_restricted"></a>

<a id="symbol-test-ogr-fid-provenance-is-restricted"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_ogr_fid_provenance_is_restricted`

Source lines 980–997. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_ogr_fid_provenance_is_restricted(
    logical_layer: str,
    feature_family: str,
    source_feature_id: str,
) -> None:
```

Two surface-row cases set OGR_FID provenance with wrong information scope or non-OGR source ID "1". Resolver rejects; no physical source mutation and no successful fallback acquisition here.

Exact decorators (not extra units):

```python
@pytest.mark.parametrize(
    ("logical_layer", "feature_family", "source_feature_id"),
    [
        ("information_surface", "INFORMATION", "OGR_FID:1"),
        ("prescription_surface", "PRESCRIPTION", "1"),
    ],
)
```

Exact expected-exception contexts:

```python
pytest.raises(
        PlanningFeatureCodeError, match="OGR|identity|provenance|normalized"
    )
```

<a id="test_source_feature_id_is_unique_inside_logical_layer"></a>

<a id="symbol-test-source-feature-id-is-unique-inside-logical-layer"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_source_feature_id_is_unique_inside_logical_layer`

Source lines 1000–1013. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_source_feature_id_is_unique_inside_logical_layer() -> None:
```

Make second surface row reuse first source_feature_id and logical/family/identity metadata; resolver must reject source_feature_id/unique. Other deterministic identity consistency guards may also reject; no isolated collision proof beyond expected message.

Exact expected-exception contexts:

```python
pytest.raises(PlanningFeatureCodeError, match="source_feature_id|unique")
```

<a id="test_catalog_crs_must_be_canonical_epsg_2154"></a>

<a id="symbol-test-catalog-crs-must-be-canonical-epsg-2154"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_catalog_crs_must_be_canonical_epsg_2154`

Source lines 1016–1020. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_catalog_crs_must_be_canonical_epsg_2154() -> None:
```

Reproject supplied surface to4326 while physical fixture stays2154; resolve expects EPSG:2154/CRS error, not automatic repair.

Exact expected-exception contexts:

```python
pytest.raises(PlanningFeatureCodeError, match="EPSG:2154|CRS")
```

<a id="test_catalog_geometry_metrics_are_revalidated"></a>

<a id="symbol-test-catalog-geometry-metrics-are-revalidated"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_catalog_geometry_metrics_are_revalidated`

Source lines 1031–1041. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_catalog_geometry_metrics_are_revalidated(
    catalog_position: int,
    column: str,
    value: object,
) -> None:
```

Set surface area99, line length99 or point members2 on supplied factual catalog; resolve rejects metric/area/length/member discrepancy against geometry.

Exact decorators (not extra units):

```python
@pytest.mark.parametrize(
    ("catalog_position", "column", "value"),
    [
        (1, "feature_area_m2", 99.0),
        (2, "feature_length_m", 99.0),
        (3, "point_member_count", 2),
    ],
)
```

Exact expected-exception contexts:

```python
pytest.raises(PlanningFeatureCodeError, match="metric|area|length|member")
```

<a id="test_complete_relation_schema_is_required"></a>

<a id="symbol-test-complete-relation-schema-is-required"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_complete_relation_schema_is_required`

Source lines 1044–1048. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_complete_relation_schema_is_required() -> None:
```

Drop intersection_length_m from factual relations; resolver rejects relation/schema/column before coding.

Exact expected-exception contexts:

```python
pytest.raises(PlanningFeatureCodeError, match="relation|schema|column")
```

<a id="test_unexpected_factual_relation_column_is_rejected"></a>

<a id="symbol-test-unexpected-factual-relation-column-is-rejected"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_unexpected_factual_relation_column_is_rejected`

Source lines 1051–1057. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_unexpected_factual_relation_column_is_rejected() -> None:
```

Add extra factual relation metric column; resolver rejects relation/schema. Extra data is not a permitted source extension.

Exact expected-exception contexts:

```python
pytest.raises(PlanningFeatureCodeError, match="relation|schema")
```

<a id="test_cnig_resolver_invokes_shared_factual_contract"></a>

<a id="symbol-test-cnig-resolver-invokes-shared-factual-contract"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_cnig_resolver_invokes_shared_factual_contract`

Source lines 1060–1082. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_cnig_resolver_invokes_shared_factual_contract(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

Patch resolver-owned shared validator with raising sentinel; resolve active inputs must expose marker as PlanningFeatureCodeError and counter equals1. Sentinel does not delegate: this test proves invocation/wrapping, not execution of physical validation.

Exact expected-exception contexts:

```python
pytest.raises(
        PlanningFeatureCodeError, match="shared factual contract marker"
    )
```

<a id="symbol-test-cnig-resolver-invokes-shared-factual-contract-reject-shared-contract"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_cnig_resolver_invokes_shared_factual_contract.reject_shared_contract`

Source lines 1068–1071. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
    def reject_shared_contract(*args: object) -> None:
```

Increment nonlocal calls then raise ValueError("shared factual contract marker"). No return/delegation or source read in this callback; setup still creates physical fixtures.

<a id="test_complete_relation_catalog_agreement_is_required"></a>

<a id="symbol-test-complete-relation-catalog-agreement-is-required"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_complete_relation_catalog_agreement_is_required`

Source lines 1094–1105. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_complete_relation_catalog_agreement_is_required(
    column: str,
    value: object,
) -> None:
```

Four relation mutations alter label_raw, source_validity_date_raw, regulation_filename_raw or feature_area_m2=3. Resolve rejects catalog/metric/normalized/feature share; broad match allows earlier metric failure rather than proving every final row-comparison path.

Exact decorators (not extra units):

```python
@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("label_raw", "mutated label"),
        ("source_validity_date_raw", "19990101"),
        ("regulation_filename_raw", "other.pdf"),
        ("feature_area_m2", 3.0),
    ],
)
```

Exact expected-exception contexts:

```python
pytest.raises(
        PlanningFeatureCodeError, match="catalog|metric|normalized|feature share"
    )
```

<a id="test_surface_relation_metrics_are_revalidated"></a>

<a id="symbol-test-surface-relation-metrics-are-revalidated"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_surface_relation_metrics_are_revalidated`

Source lines 1117–1125. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_surface_relation_metrics_are_revalidated(column: str, value: object) -> None:
```

Set first surface relation area0, -1, infinity or parcel_share_pct99; resolve expects relation/metric/finite/percentage rejection. These are factual relation constraints, not suitability thresholds.

Exact decorators (not extra units):

```python
@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("intersection_area_m2", 0.0),
        ("intersection_area_m2", -1.0),
        ("intersection_area_m2", float("inf")),
        ("parcel_share_pct", 99.0),
    ],
)
```

Exact expected-exception contexts:

```python
pytest.raises(
        PlanningFeatureCodeError, match="relation|metric|finite|percentage"
    )
```

<a id="test_line_relation_metrics_are_revalidated"></a>

<a id="symbol-test-line-relation-metrics-are-revalidated"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_line_relation_metrics_are_revalidated`

Source lines 1136–1143. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_line_relation_metrics_are_revalidated(column: str, value: object) -> None:
```

Set line relation intersection_length_m0, relation_typeTOUCH_ONLY or source_line_length_m1; resolve rejects relation/length/catalog inconsistency. Type and metric guards can precede source reconstruction.

Exact decorators (not extra units):

```python
@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("intersection_length_m", 0.0),
        ("relation_type", "TOUCH_ONLY"),
        ("source_line_length_m", 1.0),
    ],
)
```

Exact expected-exception contexts:

```python
pytest.raises(PlanningFeatureCodeError, match="relation|length|catalog")
```

<a id="test_duplicate_catalog_columns_are_rejected"></a>

<a id="symbol-test-duplicate-catalog-columns-are-rejected"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_duplicate_catalog_columns_are_rejected`

Source lines 1146–1153. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_duplicate_catalog_columns_are_rejected() -> None:
```

Duplicate the surface planning_feature_id column with pd.concat([surface, surface[["planning_feature_id"]]], axis=1), then wrap as GeoDataFrame with the original geometry and CRS. Resolving this catalog must raise PlanningFeatureCodeError matching "duplicate|columns". This tests a duplicated column, not duplicate row identity.

Exact expected-exception contexts:

```python
pytest.raises(PlanningFeatureCodeError, match="duplicate|columns")
```

<a id="test_missing_catalog_crs_is_rejected"></a>

<a id="symbol-test-missing-catalog-crs-is-rejected"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_missing_catalog_crs_is_rejected`

Source lines 1156–1162. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_missing_catalog_crs_is_rejected() -> None:
```

Copy surface, clear CRS, resolve expects CRS error before coding.

Exact expected-exception contexts:

```python
pytest.raises(PlanningFeatureCodeError, match="CRS")
```

<a id="test_unparseable_catalog_crs_is_rejected"></a>

<a id="symbol-test-unparseable-catalog-crs-is-rejected"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_unparseable_catalog_crs_is_rejected`

Source lines 1165–1172. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_unparseable_catalog_crs_is_rejected() -> None:
```

Corrupt geometry array private _crs with invalid value; resolve controls CRS failure. This intentionally bypasses normal GeoPandas assignment, not supported input coercion.

Exact expected-exception contexts:

```python
pytest.raises(PlanningFeatureCodeError, match="CRS")
```

<a id="test_inactive_or_wrong_geometry_column_is_rejected"></a>

<a id="symbol-test-inactive-or-wrong-geometry-column-is-rejected"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_inactive_or_wrong_geometry_column_is_rejected`

Source lines 1175–1183. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_inactive_or_wrong_geometry_column_is_rejected() -> None:
```

Add alternate geometry and make it active; resolve expects geometry error. Extra-column schema rejection may occur before active-name-specific guard.

Exact expected-exception contexts:

```python
pytest.raises(PlanningFeatureCodeError, match="geometry")
```

<a id="test_surface_geometry_contract_is_enforced"></a>

<a id="symbol-test-surface-geometry-contract-is-enforced"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_surface_geometry_contract_is_enforced`

Source lines 1195–1205. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_surface_geometry_contract_is_enforced(
    geometry: object,
    message: str,
) -> None:
```

Set first surface geometry to None, empty Polygon, self-crossing polygon or LineString; parametrized expected regex requires null/empty/invalid/type geometry rejection. Source fixtures unchanged; no repair expected.

Exact decorators (not extra units):

```python
@pytest.mark.parametrize(
    ("geometry", "message"),
    [
        (None, "null|geometry"),
        (Polygon(), "empty|geometry"),
        (Polygon([(0, 0), (2, 2), (2, 0), (0, 2), (0, 0)]), "invalid|geometry"),
        (LineString([(0, 0), (1, 1)]), "type|geometry|SURFACE"),
    ],
)
```

Exact expected-exception contexts:

```python
pytest.raises(PlanningFeatureCodeError, match=message)
```

<a id="test_valid_multi_geometries_are_accepted"></a>

<a id="symbol-test-valid-multi-geometries-are-accepted"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_valid_multi_geometries_are_accepted`

Source lines 1216–1244. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_valid_multi_geometries_are_accepted(
    catalog_name: str, geometry: object
) -> None:
```

For MultiPolygon/MultiLineString/MultiPoint replace actual source geometry, create fresh physical document and renormalize; resolver accepts and selected output geometry.equals(input) holds. Topological equality assertion is not WKB dimensional fidelity or exhaustive multi-geometry proof.

Exact decorators (not extra units):

```python
@pytest.mark.parametrize(
    ("catalog_name", "geometry"),
    [
        ("surface", MultiPolygon([Polygon([(0, 0), (2, 0), (2, 2), (0, 2)])])),
        ("line", MultiLineString([[(0, 0), (2, 0)]])),
        ("point", MultiPoint([(0, 0), (1, 1)])),
    ],
)
```

<a id="test_catalog_semantic_and_string_contracts_are_enforced"></a>

<a id="symbol-test-catalog-semantic-and-string-contracts-are-enforced"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_catalog_semantic_and_string_contracts_are_enforced`

Source lines 1257–1268. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_catalog_semantic_and_string_contracts_are_enforced(
    column: str,
    value: object,
    message: str,
) -> None:
```

Five surface mutations: wrong geometry_kind/logical_layer/family, null identity kind, padded source_layer; resolve expects case-specific regex. Tests declared identity consistency, not semantic zoning interpretation.

Exact decorators (not extra units):

```python
@pytest.mark.parametrize(
    ("column", "value", "message"),
    [
        ("geometry_kind", "LINE", "geometry kind|SURFACE"),
        ("logical_layer", "prescription_line", "logical layer|surface"),
        ("feature_family", "INFORMATION", "family|logical layer"),
        ("source_identity_kind", None, "source identity|exact string"),
        ("source_layer", " SOURCE ", "source layer|exact string"),
    ],
)
```

Exact expected-exception contexts:

```python
pytest.raises(PlanningFeatureCodeError, match=message)
```

<a id="test_every_required_catalog_identity_is_an_exact_non_null_string"></a>

<a id="symbol-test-every-required-catalog-identity-is-an-exact-non-null-string"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_every_required_catalog_identity_is_an_exact_non_null_string`

Source lines 1284–1299. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_every_required_catalog_identity_is_an_exact_non_null_string(
    column: str,
) -> None:
```

Eight named surface identity fields are set to " invalid "; matching relation field updated when present. Resolve rejects exact string/non-empty. Despite title, this parameter set tests padded text, not null for all eight fields.

Exact decorators (not extra units):

```python
@pytest.mark.parametrize(
    "column",
    [
        "planning_feature_id",
        "source_feature_id",
        "source_identity_kind",
        "source_identity_field",
        "logical_layer",
        "feature_family",
        "geometry_kind",
        "source_layer",
    ],
)
```

Exact expected-exception contexts:

```python
pytest.raises(PlanningFeatureCodeError, match="exact string|non-empty")
```

<a id="test_line_and_point_geometry_types_are_enforced"></a>

<a id="symbol-test-line-and-point-geometry-types-are-enforced"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_line_and_point_geometry_types_are_enforced`

Source lines 1309–1326. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_line_and_point_geometry_types_are_enforced(
    catalog_name: str,
    geometry: object,
) -> None:
```

Supply polygon for LINE or line for POINT; resolve rejects geometry/type before coding. No physical-source rewrite.

Exact decorators (not extra units):

```python
@pytest.mark.parametrize(
    ("catalog_name", "geometry"),
    [
        ("line", Polygon([(0, 0), (1, 0), (1, 1), (0, 1)])),
        ("point", LineString([(0, 0), (1, 1)])),
    ],
)
```

Exact expected-exception contexts:

```python
pytest.raises(PlanningFeatureCodeError, match="geometry|type")
```

<a id="test_planning_feature_ids_are_globally_unique_across_catalogs"></a>

<a id="symbol-test-planning-feature-ids-are-globally-unique-across-catalogs"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_planning_feature_ids_are_globally_unique_across_catalogs`

Source lines 1329–1338. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_planning_feature_ids_are_globally_unique_across_catalogs() -> None:
```

Deep-copy only the line catalog and replace its first planning_feature_id with the first surface planning_feature_id; pass relations unchanged to the resolver. Expect PlanningFeatureCodeError matching "unique|catalog|deterministic". Deterministic per-row identity guard can reject before global uniqueness, so the message alternative does not isolate that guard. This is not a coordinated catalog/relation mutation.

Exact expected-exception contexts:

```python
pytest.raises(PlanningFeatureCodeError, match="unique|catalog|deterministic")
```

<a id="test_valid_empty_optional_catalogs_preserve_schema_and_crs"></a>

<a id="symbol-test-valid-empty-optional-catalogs-preserve-schema-and-crs"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_valid_empty_optional_catalogs_preserve_schema_and_crs`

Source lines 1341–1368. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_valid_empty_optional_catalogs_preserve_schema_and_crs() -> None:
```

Remove line/point layers from a freshly written physical document and renormalize; resolve accepts optional empty outputs with EPSG2154, normalized base and official suffix columns. Not acceptance of arbitrary manually emptied source-bound inputs.

<a id="test_relation_catalog_code_mismatch_is_rejected"></a>

<a id="symbol-test-relation-catalog-code-mismatch-is-rejected"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_relation_catalog_code_mismatch_is_rejected`

Source lines 1371–1382. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_relation_catalog_code_mismatch_is_rejected() -> None:
```

Change relation raw subtype relative to catalog; resolve must reject catalog disagreement. No result reseal.

Exact expected-exception contexts:

```python
pytest.raises(PlanningFeatureCodeError, match="catalog")
```

<a id="test_duplicate_relation_columns_are_rejected"></a>

<a id="symbol-test-duplicate-relation-columns-are-rejected"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_duplicate_relation_columns_are_rejected`

Source lines 1385–1391. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_duplicate_relation_columns_are_rejected() -> None:
```

Concat duplicate relation column then resolve; duplicate/columns expected before coding.

Exact expected-exception contexts:

```python
pytest.raises(PlanningFeatureCodeError, match="duplicate|columns")
```

<a id="test_relation_identity_must_be_an_exact_non_null_string"></a>

<a id="symbol-test-relation-identity-must-be-an-exact-non-null-string"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_relation_identity_must_be_an_exact_non_null_string`

Source lines 1396–1406. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_relation_identity_must_be_an_exact_non_null_string(
    column: str,
    value: object,
) -> None:
```

Cross product parcel_id/planning_feature_id with None or padded invalid text; resolve expects relation/exact-string error. Actual four cases, not arbitrary object coverage.

Exact decorators (not extra units):

```python
@pytest.mark.parametrize("column", ["parcel_id", "planning_feature_id"])
@pytest.mark.parametrize("value", [None, " invalid "])
```

Exact expected-exception contexts:

```python
pytest.raises(PlanningFeatureCodeError, match="relation|exact string")
```

<a id="test_duplicate_parcel_feature_relation_is_rejected"></a>

<a id="symbol-test-duplicate-parcel-feature-relation-is-rejected"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_duplicate_parcel_feature_relation_is_rejected`

Source lines 1409–1416. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_duplicate_parcel_feature_relation_is_rejected() -> None:
```

Concat first relation again, canonicalize dtypes/index and resolve; unique/duplicate rejection. Canonical reset avoids an incidental index failure.

Exact expected-exception contexts:

```python
pytest.raises(PlanningFeatureCodeError, match="unique|duplicate")
```

<a id="test_unknown_relation_feature_id_is_rejected"></a>

<a id="symbol-test-unknown-relation-feature-id-is-rejected"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_unknown_relation_feature_id_is_rejected`

Source lines 1419–1426. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_unknown_relation_feature_id_is_rejected() -> None:
```

Replace relation feature ID with absent ID; resolver rejects unknown feature, no spatial fallback.

Exact expected-exception contexts:

```python
pytest.raises(PlanningFeatureCodeError, match="unknown")
```

<a id="test_relation_type_must_match_catalog_geometry_kind"></a>

<a id="symbol-test-relation-type-must-match-catalog-geometry-kind"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_relation_type_must_match_catalog_geometry_kind`

Source lines 1438–1499. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_relation_type_must_match_catalog_geometry_kind(
    geometry_kind: str,
    relation_type: str,
) -> None:
```

Four bad kind/type combinations construct one relation using target feature identity/raw fields, clear metrics and populate kind-appropriate numbers, then canonicalize schema. Resolve must reject relation type/geometry; no claim to every invalid combination.

Exact decorators (not extra units):

```python
@pytest.mark.parametrize(
    ("geometry_kind", "relation_type"),
    [
        ("SURFACE", "LENGTH_OVERLAP"),
        ("SURFACE", "NOT_A_RELATION"),
        ("LINE", "INSIDE"),
        ("POINT", "AREA_OVERLAP"),
    ],
)
```

Exact expected-exception contexts:

```python
pytest.raises(PlanningFeatureCodeError, match="[Rr]elation type|geometry")
```

<a id="test_valid_relation_types_are_retained"></a>

<a id="symbol-test-valid-relation-types-are-retained"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_valid_relation_types_are_retained`

Source lines 1513–1554. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_valid_relation_types_are_retained(
    geometry_kind: str,
    relation_type: str,
) -> None:
```

Six kind/type cases create physical geometries for SURFACE overlap/touch, LINE overlap/touch, POINT inside/boundary, normalize and resolve. Assert exact singleton relation-type list, not legal applicability or exhaustive geometry topology.

Exact decorators (not extra units):

```python
@pytest.mark.parametrize(
    ("geometry_kind", "relation_type"),
    [
        ("SURFACE", "AREA_OVERLAP"),
        ("SURFACE", "TOUCH_ONLY"),
        ("LINE", "LENGTH_OVERLAP"),
        ("LINE", "TOUCH_ONLY"),
        ("POINT", "INSIDE"),
        ("POINT", "BOUNDARY_TOUCH"),
    ],
)
```

<a id="test_coordinated_output_hash_mutation_is_rejected"></a>

<a id="symbol-test-coordinated-output-hash-mutation-is-rejected"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_coordinated_output_hash_mutation_is_rejected`

Source lines 1557–1564. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_coordinated_output_hash_mutation_is_rejected() -> None:
```

Change coded surface official label to Mutated and recompute result hashes; full public validator raises rebuilt/meaning/dictionary. Intrinsic dictionary disagreement can reject before physical reconstruction; this does not prove coordinated dictionary/profile/source forgery is impossible.

Exact expected-exception contexts:

```python
pytest.raises(PlanningFeatureCodeError, match="rebuilt|meaning|dictionary")
```

<a id="test_parquet_readback_passes_source_complete_validation"></a>

<a id="symbol-test-parquet-readback-passes-source-complete-validation"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_parquet_readback_passes_source_complete_validation`

Source lines 1567–1590. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_parquet_readback_passes_source_complete_validation(tmp_path: Path) -> None:
```

Write all five output tables with index=True under tmp_path; reread using pandas/GeoPandas, replace tables and invoke full validator with original sources/profile. Passing means no exception, not a production artifact manifest/loader test.

<a id="test_record_order_must_be_deterministic"></a>

<a id="symbol-test-record-order-must-be-deterministic"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_record_order_must_be_deterministic`

Source lines 1593–1597. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_record_order_must_be_deterministic() -> None:
```

Reverse profile records without resealing hash; model validation must raise deterministic-order error before checksum comparison.

Exact expected-exception contexts:

```python
pytest.raises(ValueError, match="deterministic order")
```

<a id="test_yaml_snapshot_loads_strictly"></a>

<a id="symbol-test-yaml-snapshot-loads-strictly"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_yaml_snapshot_loads_strictly`

Source lines 1600–1604. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_yaml_snapshot_loads_strictly(tmp_path: Path) -> None:
```

Dump synthetic profile payload as YAML to tmp_path; load and compare model equality with fixture profile. No network retrieval or checked-in byte-hash proof.

<a id="test_stable_public_api_is_exported_from_module_and_stage_package"></a>

<a id="symbol-test-stable-public-api-is-exported-from-module-and-stage-package"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_stable_public_api_is_exported_from_module_and_stage_package`

Source lines 1607–1635. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_stable_public_api_is_exported_from_module_and_stage_package() -> None:
```

Assert seven required names are subsets of module/package __all__, references identical, and five listed low-level names excluded. Does not assert exhaustive export equality, parameter defaults or invocation counts.

<a id="test_checked_in_official_snapshot_is_complete_for_observed_muret_pairs"></a>

<a id="symbol-test-checked-in-official-snapshot-is-complete-for-observed-muret-pairs"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_checked_in_official_snapshot_is_complete_for_observed_muret_pairs`

Source lines 1638–1778. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_checked_in_official_snapshot_is_complete_for_observed_muret_pairs() -> None:
```

Load checked-in YAML; assert exact schema/profile/standard/normalization/date/endpoints, twelve ordered seven-field records and fixed records/profile digests. This locks configured snapshot content; it does not rerun Muret, retrieve official pages or certify legal currency. Existing A-003/A-004 remain.

<a id="test_result_schema_versions_are_strict"></a>

<a id="symbol-test-result-schema-versions-are-strict"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_result_schema_versions_are_strict`

Source lines 1801–1807. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_result_schema_versions_are_strict(field: str, value: object) -> None:
```

Fifteen invalid version field/value cases include bool, older/future numbers, float and numeric string. Replace frozen result scalar without resealing; full validator must reject schema version at envelope guard, not source reconstruction.

Exact decorators (not extra units):

```python
@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("result_hash_schema_version", True),
        ("result_hash_schema_version", 0),
        ("result_hash_schema_version", 1),
        ("result_hash_schema_version", 2),
        ("result_hash_schema_version", 3),
        ("result_hash_schema_version", 4),
        ("result_hash_schema_version", 6),
        ("result_hash_schema_version", 5.0),
        ("result_hash_schema_version", "5"),
        ("profile_schema_version", True),
        ("profile_schema_version", 0),
        ("profile_schema_version", 1),
        ("profile_schema_version", 3),
        ("profile_schema_version", 2.0),
        ("profile_schema_version", "2"),
    ],
)
```

Exact expected-exception contexts:

```python
pytest.raises(PlanningFeatureCodeError, match="schema version")
```

<a id="test_step_7d_3_1_output_integrates_with_public_coding_api"></a>

<a id="symbol-test-step-7d-3-1-output-integrates-with-public-coding-api"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_step_7d_3_1_output_integrates_with_public_coding_api`

Source lines 1810–1820. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_step_7d_3_1_output_integrates_with_public_coding_api() -> None:
```

Call actual seven-argument resolver on physical synthetic normalization output; assert 2surface/1line/1point/2relations, versions and resolved surface status, then actual full validator. No official-source acquisition.

<a id="test_resolver_runs_heavy_factual_validation_once_and_public_validator_repeats"></a>

<a id="symbol-test-resolver-runs-heavy-factual-validation-once-and-public-validator-repeats"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_resolver_runs_heavy_factual_validation_once_and_public_validator_repeats`

Source lines 1823–1852. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_resolver_runs_heavy_factual_validation_once_and_public_validator_repeats(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

Create fixtures before spies; patch enrich owner batch physical validator and expected-relation builder with delegating counters. Real resolver yields1each, real full validator yields2each. Counts are owner invocations, not disk reads, source files or geometry operations.

<a id="symbol-test-resolver-runs-heavy-factual-validation-once-and-public-validator-repeats-counted-physical"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_resolver_runs_heavy_factual_validation_once_and_public_validator_repeats.counted_physical`

Source lines 1835–1837. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
    def counted_physical(*args: object, **kwargs: object) -> object:
```

Increment physical counter then return original physical batch call with unchanged *args/**kwargs; genuine delegate, not no-op/sentinel.

<a id="symbol-test-resolver-runs-heavy-factual-validation-once-and-public-validator-repeats-counted-relations"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_resolver_runs_heavy_factual_validation_once_and_public_validator_repeats.counted_relations`

Source lines 1839–1841. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
    def counted_relations(*args: object, **kwargs: object) -> object:
```

Increment relations counter then return original expected-relations builder with unchanged *args/**kwargs. Real geometry work still executes.

<a id="test_coded_result_persists_all_source_input_hashes"></a>

<a id="symbol-test-coded-result-persists-all-source-input-hashes"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_coded_result_persists_all_source_input_hashes`

Source lines 1855–1868. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_coded_result_persists_all_source_input_hashes() -> None:
```

For six source commitments assert string, length64 and int(value,16) parses. Does not independently recompute digest contents or require lowercase in these assertions.

<a id="test_source_input_hash_mutation_is_rejected"></a>

<a id="symbol-test-source-input-hash-mutation-is-rejected"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_source_input_hash_mutation_is_rejected`

Source lines 1882–1888. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_source_input_hash_mutation_is_rejected(field: str) -> None:
```

Replace each of six source hashes with f*64, without resealing components, then full validator expects hash/rebuilt/source error. Local hash inconsistency is sufficient; not isolated proof of source-rebuild rejection for coherent forgery.

Exact decorators (not extra units):

```python
@pytest.mark.parametrize(
    "field",
    [
        "planning_document_context_sha256",
        "parcel_identity_input_sha256",
        "normalized_catalogs_input_sha256",
        "normalized_relations_input_sha256",
        "gpu_related_source_files_sha256",
        "expected_relations_content_sha256",
    ],
)
```

Exact expected-exception contexts:

```python
pytest.raises(PlanningFeatureCodeError, match="hash|rebuilt|source")
```

<a id="test_gpu_related_source_hash_is_deterministic_across_cache_roots"></a>

<a id="symbol-test-gpu-related-source-hash-is-deterministic-across-cache-roots"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_gpu_related_source_hash_is_deterministic_across_cache_roots`

Source lines 1891–1933. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_gpu_related_source_hash_is_deterministic_across_cache_roots(
    tmp_path: Path,
) -> None:
```

Copy synthetic extraction tree to tmp_path, rebase references/extraction and resolve both sources; assert only gpu_related_source_files_sha256 equal. Real copied files/manifests are read; not proof all contextual/result hashes are root-independent.

<a id="symbol-test-gpu-related-source-hash-is-deterministic-across-cache-roots-relocated-reference"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_gpu_related_source_hash_is_deterministic_across_cache_roots.relocated_reference`

Source lines 1900–1904. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
    def relocated_reference(
        reference: GpuSpatialLayerReference,
    ) -> GpuSpatialLayerReference:
```

Replace only dataset_path using old-root-relative path under copied root; no file copy inside this nested helper. Outer test performs copytree.

<a id="test_source_binding_hashes_bind_every_component_hash"></a>

<a id="symbol-test-source-binding-hashes-bind-every-component-hash"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_source_binding_hashes_bind_every_component_hash`

Source lines 1940–1951. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_source_binding_hashes_bind_every_component_hash(field: str) -> None:
```

Replace GPU-files or expected-relations digest and reseal result; assert all five component hashes and complete hash differ. No validator call; proves hash dependency, not source authority.

Exact decorators (not extra units):

```python
@pytest.mark.parametrize(
    "field",
    ["gpu_related_source_files_sha256", "expected_relations_content_sha256"],
)
```

<a id="test_parcel_source_change_invalidates_coded_result"></a>

<a id="symbol-test-parcel-source-change-invalidates-coded-result"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_parcel_source_change_invalidates_coded_result`

Source lines 1954–1961. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_parcel_source_change_invalidates_coded_result() -> None:
```

Rename parcel ID in source input then full validator rejects parcel/source/rebuilt. Existing relations may reference unknown parcel before final source-hash comparison.

Exact expected-exception contexts:

```python
pytest.raises(PlanningFeatureCodeError, match="parcel|source|rebuilt")
```

<a id="test_gpu_document_context_change_invalidates_coded_result"></a>

<a id="symbol-test-gpu-document-context-change-invalidates-coded-result"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_gpu_document_context_change_invalidates_coded_result`

Source lines 1964–1978. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_gpu_document_context_change_invalidates_coded_result() -> None:
```

Replace document metadata provider while keeping result/source catalogs; full validator rejects document/source/rebuilt. Factual provider agreement may fail before an isolated context-digest comparison.

Exact expected-exception contexts:

```python
pytest.raises(PlanningFeatureCodeError, match="document|source|rebuilt")
```

<a id="test_normalized_catalog_change_invalidates_coded_result_even_when_coherent"></a>

<a id="symbol-test-normalized-catalog-change-invalidates-coded-result-even-when-coherent"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_normalized_catalog_change_invalidates_coded_result_even_when_coherent`

Source lines 1981–1996. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_normalized_catalog_change_invalidates_coded_result_even_when_coherent() -> (
    None
):
```

Change surface label_raw and matching relation label coherently, leave physical source unchanged; full validator rejects normalized/source/rebuilt. Tests source-backed factual comparison, not only internal relation/catalog agreement.

Exact expected-exception contexts:

```python
pytest.raises(PlanningFeatureCodeError, match="normalized|source|rebuilt")
```

<a id="test_normalized_relation_change_invalidates_coded_result"></a>

<a id="symbol-test-normalized-relation-change-invalidates-coded-result"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_normalized_relation_change_invalidates_coded_result`

Source lines 1999–2007. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_normalized_relation_change_invalidates_coded_result() -> None:
```

Change line relation parcel_metric_area_m2 to8, full validator rejects relation/source/rebuilt. Parcel-metric guard can fail before relation-hash comparison.

Exact expected-exception contexts:

```python
pytest.raises(PlanningFeatureCodeError, match="[Rr]elation|source|rebuilt")
```

<a id="test_coding_api_rejects_relation_set_not_rebuilt_from_geometry"></a>

<a id="symbol-test-coding-api-rejects-relation-set-not-rebuilt-from-geometry"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_coding_api_rejects_relation_set_not_rebuilt_from_geometry`

Source lines 2011–2032. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_coding_api_rejects_relation_set_not_rebuilt_from_geometry(
    mutation: str,
) -> None:
```

Four mutations: remove first row without resetting resulting RangeIndex start, append unknown parcel, reverse/reset order, or change line overlap metric. Resolver expects broad relation/parcel/source/rebuilt/normalized regex. Missing/extra can fail canonical-index/identity guards; reordered/plausible metric cases exercise expected relation agreement. Does not isolate completeness guard in every branch.

Exact decorators (not extra units):

```python
@pytest.mark.parametrize("mutation", ["missing", "extra", "reordered", "metric"])
```

Exact expected-exception contexts:

```python
pytest.raises(
        PlanningFeatureCodeError,
        match="relation|parcel|source|rebuilt|normalized",
    )
```

<a id="test_schema_v5_parquet_readback_preserves_source_hash_envelope"></a>

<a id="symbol-test-schema-v5-parquet-readback-preserves-source-hash-envelope"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_schema_v5_parquet_readback_preserves_source_hash_envelope`

Source lines 2035–2060. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_schema_v5_parquet_readback_preserves_source_hash_envelope(
    tmp_path: Path,
) -> None:
```

Write/reload all five index-preserving Parquet frames and call actual full validator with seven original inputs. Successful source-complete validation, no manifest or production artifact loader invoked.

<a id="test_schema_v5_public_api_signatures_remain_source_complete"></a>

<a id="symbol-test-schema-v5-public-api-signatures-remain-source-complete"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_schema_v5_public_api_signatures_remain_source_complete`

Source lines 2063–2086. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_schema_v5_public_api_signatures_remain_source_complete() -> None:
```

Inspect actual resolver and validator parameter-name tuples, assert seven/eight names in order. No assertion of defaults, annotations or keyword-only shape; literal signatures in production companion provide those.

<a id="test_step_7d_5b_2b_5_exposes_lightweight_coded_result_validator"></a>

<a id="symbol-test-step-7d-5b-2b-5-exposes-lightweight-coded-result-validator"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_step_7d_5b_2b_5_exposes_lightweight_coded_result_validator`

Source lines 2089–2098. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_step_7d_5b_2b_5_exposes_lightweight_coded_result_validator() -> None:
```

Assert hasattr(module, public envelope name), call it successfully with a valid result, then replace complete digest by zeros and expect hash/invalid error. No explicit callable assertion; this boundary does not reread sources.

Exact expected-exception contexts:

```python
pytest.raises(PlanningFeatureCodeError, match="hash|invalid")
```

<a id="_schema_v5_envelope_result"></a>

<a id="symbol--schema-v5-envelope-result"></a>
### `tests.unit.test_resolve_planning_feature_codes._schema_v5_envelope_result`

Source lines 2101–2102. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def _schema_v5_envelope_result() -> PlanningFeatureCodeResult:
```

Resolve active physical synthetic fixtures to get valid schema5 envelope. Even lightweight-envelope tests incur setup I/O before their local validation call.

<a id="_canonical_empty_coded_result"></a>

<a id="symbol--canonical-empty-coded-result"></a>
### `tests.unit.test_resolve_planning_feature_codes._canonical_empty_coded_result`

Source lines 2105–2137. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def _canonical_empty_coded_result(
    result: PlanningFeatureCodeResult,
    *,
    empty_dictionary: bool,
) -> PlanningFeatureCodeResult:
```

Empty all three coded catalogs and relations preserving schema, assign canonical plain int64 Index, optionally empty dictionary, reseal components/complete result. Keeps old source-input commitments; helper intentionally constructs locally coherent but not rebuilt source outputs.

<a id="test_schema_v5_envelope_rejects_canonical_empty_code_dictionary"></a>

<a id="symbol-test-schema-v5-envelope-rejects-canonical-empty-code-dictionary"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_schema_v5_envelope_rejects_canonical_empty_code_dictionary`

Source lines 2140–2146. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_schema_v5_envelope_rejects_canonical_empty_code_dictionary() -> None:
```

Use empty-output helper including dictionary; envelope rejects dictionary/empty/record despite coherent hashes and schema. No physical-source reconstruction.

Exact expected-exception contexts:

```python
pytest.raises(PlanningFeatureCodeError, match="dictionary|empty|record")
```

<a id="test_schema_v5_envelope_accepts_nonempty_dictionary_with_empty_outputs"></a>

<a id="symbol-test-schema-v5-envelope-accepts-nonempty-dictionary-with-empty-outputs"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_schema_v5_envelope_accepts_nonempty_dictionary_with_empty_outputs`

Source lines 2149–2167. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_schema_v5_envelope_accepts_nonempty_dictionary_with_empty_outputs() -> None:
```

Retain nonempty dictionary but empty four outputs with coherent schema/hashes; envelope accepts, assert dictionary nonempty and all outputs empty. This explicitly proves local envelope acceptance is not source completeness.

<a id="test_schema_v5_envelope_controls_malformed_dictionary_type"></a>

<a id="symbol-test-schema-v5-envelope-controls-malformed-dictionary-type"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_schema_v5_envelope_controls_malformed_dictionary_type`

Source lines 2171–2179. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_schema_v5_envelope_controls_malformed_dictionary_type(
    dictionary: object,
) -> None:
```

Replace dictionary by None or string without resealing, call public envelope and expect controlled PlanningFeatureCodeError. No claim private helper catches every unexpected exception alone.

Exact decorators (not extra units):

```python
@pytest.mark.parametrize("dictionary", [None, "not-a-frame"])
```

Exact expected-exception contexts:

```python
pytest.raises(PlanningFeatureCodeError)
```

<a id="test_schema_v5_envelope_rejects_geospatial_code_dictionary"></a>

<a id="symbol-test-schema-v5-envelope-rejects-geospatial-code-dictionary"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_schema_v5_envelope_rejects_geospatial_code_dictionary`

Source lines 2182–2189. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_schema_v5_envelope_rejects_geospatial_code_dictionary() -> None:
```

Wrap dictionary in GeoDataFrame and replace; local envelope rejects dictionary/DataFrame exact-type contract, no reseal needed.

Exact expected-exception contexts:

```python
pytest.raises(PlanningFeatureCodeError, match="dictionary|DataFrame")
```

<a id="test_schema_v5_dictionary_schema_is_explicit"></a>

<a id="symbol-test-schema-v5-dictionary-schema-is-explicit"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_schema_v5_dictionary_schema_is_explicit`

Source lines 2195–2209. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_schema_v5_dictionary_schema_is_explicit(mutation: str) -> None:
```

Four dictionary changes: label category dtype, RangeIndex, named Index, uint64 Index; reseal full result and call envelope. Require dictionary/schema/dtype/index rejection independent of stale hash.

Exact decorators (not extra units):

```python
@pytest.mark.parametrize(
    "mutation", ["dtype", "range-index", "index-name", "index-dtype"]
)
```

Exact expected-exception contexts:

```python
pytest.raises(PlanningFeatureCodeError, match="dictionary|schema|dtype|index")
```

<a id="test_schema_v5_dictionary_rows_are_intrinsically_validated"></a>

<a id="symbol-test-schema-v5-dictionary-rows-are-intrinsically-validated"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_schema_v5_dictionary_rows_are_intrinsically_validated`

Source lines 2226–2258. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_schema_v5_dictionary_rows_are_intrinsically_validated(mutation: str) -> None:
```

Nine resealed dictionary mutations: duplicate/reversed triples, malformed type/subtype, wrong family/URL/profile/profile SHA and literal-null reference. Local envelope rejects row/lineage/order contract with broad listed regex; no source completeness test.

Exact decorators (not extra units):

```python
@pytest.mark.parametrize(
    "mutation",
    [
        "duplicate-pair",
        "unsorted-pairs",
        "malformed-type",
        "malformed-subtype",
        "wrong-family",
        "wrong-url",
        "wrong-profile",
        "wrong-profile-sha",
        "literal-null-reference",
    ],
)
```

Exact expected-exception contexts:

```python
pytest.raises(
        PlanningFeatureCodeError, match="dictionary|pair|code|family|URL|profile|order"
    )
```

<a id="test_schema_v5_scalar_lineage_contracts_are_intrinsic"></a>

<a id="symbol-test-schema-v5-scalar-lineage-contracts-are-intrinsic"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_schema_v5_scalar_lineage_contracts_are_intrinsic`

Source lines 2261–2272. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_schema_v5_scalar_lineage_contracts_are_intrinsic() -> None:
```

Replace standard with v2099 or planning context SHA by malformed value; reseal and call envelope, expect standard/SHA/sha/lineage error. Recomputed hashes cannot waive scalar guards.

Exact expected-exception contexts:

```python
pytest.raises(PlanningFeatureCodeError, match="standard|SHA|sha|lineage")
```

<a id="test_schema_v5_official_rows_and_relation_feature_agreement_are_intrinsic"></a>

<a id="symbol-test-schema-v5-official-rows-and-relation-feature-agreement-are-intrinsic"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_schema_v5_official_rows_and_relation_feature_agreement_are_intrinsic`

Source lines 2275–2295. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_schema_v5_official_rows_and_relation_feature_agreement_are_intrinsic() -> None:
```

Three independently resealed mutations: null resolved surface label, known row claims UNKNOWN with existing meanings, or relation label differs. Envelope rejects official/meaning/UNKNOWN/relation/feature, with no source reread.

Exact expected-exception contexts:

```python
pytest.raises(
            PlanningFeatureCodeError,
            match="official|meaning|UNKNOWN|relation|feature",
        )
```

<a id="test_schema_v5_envelope_requires_exact_result_type_and_accepts_valid_result"></a>

<a id="symbol-test-schema-v5-envelope-requires-exact-result-type-and-accepts-valid-result"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_schema_v5_envelope_requires_exact_result_type_and_accepts_valid_result`

Source lines 2298–2310. Kind: function. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
def test_schema_v5_envelope_requires_exact_result_type_and_accepts_valid_result() -> (
    None
):
```

Instantiate nested derived type from result.__dict__, require type/result error, then validate original envelope successfully. Exact type check precedes hash/row checks.

Exact expected-exception contexts:

```python
pytest.raises(PlanningFeatureCodeError, match="type|result")
```

<a id="symbol-test-schema-v5-envelope-requires-exact-result-type-and-accepts-valid-result-derivedplanningfeaturecoderesult"></a>
### `tests.unit.test_resolve_planning_feature_codes.test_schema_v5_envelope_requires_exact_result_type_and_accepts_valid_result.DerivedPlanningFeatureCodeResult`

Source lines 2304–2305. Kind: class. Owner: `tests.unit.test_resolve_planning_feature_codes`.

```python
    class DerivedPlanningFeatureCodeResult(PlanningFeatureCodeResult):
```

Empty subclass of PlanningFeatureCodeResult used only to demonstrate exact-type rejection. No new field or validator; inherited constructor does not confer envelope acceptance.

## Complete source snapshot

Exact full Git-content UTF-8 source. Byte identity supports provenance, not semantic correctness by itself.

```python
from __future__ import annotations

import importlib
import inspect
import json
import shutil
import tempfile
from dataclasses import replace
from hashlib import sha256
from pathlib import Path

import geopandas as gpd  # type: ignore[import-untyped]
import pandas as pd
import pytest
import yaml  # type: ignore[import-untyped]
from geopandas.testing import assert_geodataframe_equal
from shapely.geometry import (
    LineString,
    MultiLineString,
    MultiPoint,
    MultiPolygon,
    Point,
    Polygon,
)

from landscout.common.planning_feature_schema import (
    NORMALIZED_RELATION_DTYPES,
    feature_dtypes,
    relation_dtypes,
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
from landscout.stages.enrich_planning_features import (
    RELATION_COLUMNS,
    intersect_parcels_with_gpu_planning_features,
)
from landscout.stages.resolve_planning_feature_codes import (
    CODE_DICTIONARY_COLUMNS,
    OFFICIAL_CODE_COLUMNS,
    CnigFeatureCodeProfile,
    PlanningFeatureCodeError,
    PlanningFeatureCodeResult,
    _result_with_hashes,
    load_cnig_feature_code_profile,
)
from landscout.stages.resolve_planning_feature_codes import (
    resolve_planning_feature_codes as _public_resolve_planning_feature_codes,
)
from landscout.stages.resolve_planning_feature_codes import (
    validate_planning_feature_code_result as _public_validate_planning_feature_code_result,
)


def _canonical_relation_schema(frame: pd.DataFrame) -> pd.DataFrame:
    output = frame.copy(deep=True)
    for column, dtype in zip(RELATION_COLUMNS, NORMALIZED_RELATION_DTYPES, strict=True):
        output[column] = pd.Series(
            output[column].tolist(), index=output.index, dtype=dtype
        )
    output.index = pd.RangeIndex(len(output))
    return output


P_URL = "https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/PrescriptionUrbaType"
I_URL = "https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/InformationUrbaType"
TEXT_NORMALIZATION = "GPU_DISPLAY_TEXT_NFC_WHITESPACE_V1"


def _records_hash(records: list[dict[str, object]]) -> str:
    ordered = sorted(
        records,
        key=lambda row: (row["feature_family"], row["type_code"], row["subtype_code"]),
    )
    payload = json.dumps(
        ordered,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode()
    return sha256(payload).hexdigest()


def _payload_hash(payload: object) -> str:
    encoded = json.dumps(
        payload,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
        default=str,
    ).encode("utf-8")
    return sha256(encoded).hexdigest()


def _record(
    family: str,
    type_code: str,
    subtype_code: str,
    label: str,
) -> dict[str, object]:
    return {
        "feature_family": family,
        "type_code": type_code,
        "subtype_code": subtype_code,
        "official_label": label,
        "legal_reference": None,
        "regulation_or_annex_reference": None,
        "official_source_url": P_URL if family == "PRESCRIPTION" else I_URL,
    }


def _profile_payload() -> dict[str, object]:
    records = [
        _record("INFORMATION", "02", "00", "Information two"),
        _record("INFORMATION", "99", "00", "Other information"),
        _record("PRESCRIPTION", "07", "00", "Prescription seven"),
        _record("PRESCRIPTION", "07", "04", "Prescription seven subtype four"),
    ]
    return {
        "schema_version": 2,
        "profile": "synthetic_cnig_plu_2017",
        "standard_model": "CNIG PLU v2017",
        "official_text_normalization": TEXT_NORMALIZATION,
        "official_sources": {
            "prescription": P_URL,
            "information": I_URL,
        },
        "retrieval_date": "2026-08-12",
        "canonical_records_sha256": _records_hash(records),
        "records": records,
    }


def _profile() -> CnigFeatureCodeProfile:
    return CnigFeatureCodeProfile.model_validate(_profile_payload())


def _physical_inventory(root: Path) -> tuple[GpuExtractedFile, ...]:
    return tuple(
        GpuExtractedFile(
            relative_path=path.relative_to(root).as_posix(),
            file_type=path.suffix.casefold().lstrip(".") or "none",
            size_bytes=path.stat().st_size,
            sha256=sha256(path.read_bytes()).hexdigest(),
            category="SPATIAL_DATA",
        )
        for path in sorted(
            (item for item in root.rglob("*") if item.is_file()), key=str
        )
        if not (path.parent == root and path.name == EXTRACTION_MANIFEST_NAME)
    )


def _write_extraction_manifest(
    root: Path,
    archive_sha256: str,
    files: tuple[GpuExtractedFile, ...],
) -> None:
    (root / EXTRACTION_MANIFEST_NAME).write_text(
        json.dumps(
            {
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
            },
            sort_keys=True,
            separators=(",", ":"),
        ),
        encoding="utf-8",
    )


def _layer_summary(frame: gpd.GeoDataFrame, source_layer: str) -> GpuLayerSummary:
    geometry = frame.geometry
    non_null = ~geometry.isna()
    non_empty = non_null & ~geometry.is_empty
    return GpuLayerSummary(
        source_document_id="doc-1",
        source_archive_sha256="a" * 64,
        source_layer=source_layer,
        crs=frame.crs.to_string(),
        feature_count=len(frame),
        columns=tuple(str(column) for column in frame.columns),
        dtypes=tuple(
            (str(column), str(dtype)) for column, dtype in frame.dtypes.items()
        ),
        null_counts=tuple(
            (str(column), int(frame[column].isna().sum())) for column in frame.columns
        ),
        geometry_types=tuple(
            (str(name), int(count))
            for name, count in geometry.geom_type.value_counts().sort_index().items()
        ),
        null_geometry_count=int((~non_null).sum()),
        empty_geometry_count=int((non_null & geometry.is_empty).sum()),
        invalid_geometry_count=int((non_empty & ~geometry.is_valid).sum()),
    )


def _planning_document(
    standard: str = "CNIG PLU v2017",
    related_layers: tuple[GpuInspectedLayer, ...] = (),
) -> GpuPlanningDocument:
    extraction_root = Path(tempfile.mkdtemp(prefix="landscout-code-source-"))
    physical_layers: list[GpuInspectedLayer] = []
    for layer in related_layers:
        path = extraction_root / f"{layer.logical_name}.gpkg"
        layer.data.to_file(
            path,
            layer=layer.reference.source_layer,
            driver="GPKG",
            engine="pyogrio",
            index=False,
        )
        reread = gpd.read_file(
            path, layer=layer.reference.source_layer, engine="pyogrio"
        )
        reference = replace(
            layer.reference,
            dataset_path=path,
            driver="GPKG",
        )
        physical_layers.append(
            replace(
                layer,
                reference=reference,
                data=reread,
                summary=_layer_summary(reread, reference.source_layer),
            )
        )
    related_layers = tuple(physical_layers)
    document = GpuDocumentMetadata(
        provider="Géoportail de l'Urbanisme",
        portal="G\u00e9oportail de l'Urbanisme",
        commune_code="31395",
        partition="DU_31395",
        document_id="doc-1",
        document_family="DU",
        document_type="PLU",
        document_title=None,
        status="document.production",
        legal_status="APPROVED",
        effective_status="EN_VIGUEUR",
        version="10",
        archive_name="31395_PLU_20240215",
        publication_timestamp=None,
        update_timestamp=None,
        revision_date=None,
        producer=None,
        standard_model=None,
        projection="EPSG:2154",
        metadata_identifier=None,
        source_url="https://www.geoportail-urbanisme.gouv.fr/api/document/download-by-partition/DU_31395",
        written_files=(),
    )
    archive = GpuArchiveDownload(
        document=document,
        download_timestamp="2026-08-12T00:00:00Z",
        filename="31395_PLU_20240215.zip",
        archive_format="zip",
        file_size=1,
        sha256="a" * 64,
        path=Path("synthetic.zip"),
        cache_hit=True,
    )
    zoning_data = gpd.GeoDataFrame(
        {"LIB_IDZONE": ["Z1"]},
        geometry=[Polygon([(0, 0), (1, 0), (1, 1), (0, 1)])],
        crs="EPSG:2154",
    )
    zoning_path = extraction_root / "zones.gpkg"
    zoning_data.to_file(
        zoning_path,
        layer="ZONE",
        driver="GPKG",
        engine="pyogrio",
        index=False,
    )
    zoning_data = gpd.read_file(zoning_path, layer="ZONE", engine="pyogrio")
    reference = GpuSpatialLayerReference(zoning_path, "ZONE", "GPKG")
    summary = _layer_summary(zoning_data, "ZONE")
    zoning = GpuInspectedLayer("zoning", reference, zoning_data, summary)
    inventory = _physical_inventory(extraction_root)
    _write_extraction_manifest(extraction_root, archive.sha256, inventory)
    extraction = GpuExtraction(
        archive=archive,
        extraction_root=extraction_root,
        files=inventory,
        standard_models=(standard,),
        cache_hit=True,
    )
    config_payload = load_gpu_source_config(
        Path("configs/sources/gpu_fr.yaml")
    ).model_dump(mode="python")
    for role in config_payload["spatial_layers"]:
        config_payload["spatial_layers"][role]["match_tokens"] = [f"unused_{role}"]
    config_payload["spatial_layers"]["zoning"]["match_tokens"] = ["ZONE"]
    for layer in related_layers:
        config_payload["spatial_layers"][layer.logical_name]["match_tokens"] = [
            layer.reference.source_layer
        ]
    source_config = GpuSourceConfig.model_validate(config_payload)
    related_by_logical_name = {layer.logical_name: layer for layer in related_layers}
    related_layers = tuple(
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
        related_layers=related_layers,
    )


def _base_row(
    feature_id: str,
    source_id: str,
    family: str,
    layer: str,
    kind: str,
    type_code: str,
    subtype_code: str,
) -> dict[str, object]:
    return {
        "planning_feature_id": feature_id,
        "source_feature_id": source_id,
        "source_identity_kind": "CNIG_ATTRIBUTE",
        "source_identity_field": "LIB_IDPSC"
        if family == "PRESCRIPTION"
        else "LIB_IDINFO",
        "logical_layer": layer,
        "feature_family": family,
        "geometry_kind": kind,
        "type_code_raw": type_code,
        "subtype_code_raw": subtype_code,
        "label_raw": None,
        "text_raw": None,
        "regulation_filename_raw": None,
        "regulation_url_raw": None,
        "source_document_reference_raw": "31395_PLU_20240215",
        "source_validity_date_raw": "20240215",
        "source_provider": "Géoportail de l'Urbanisme",
        "source_portal": "https://www.geoportail-urbanisme.gouv.fr",
        "source_commune_code": "31395",
        "source_document_id": "doc-1",
        "source_document_type": "PLU",
        "source_archive_name": "31395_PLU_20240215",
        "source_archive_sha256": "a" * 64,
        "source_layer": layer.upper(),
        "source_standard_model": "CNIG PLU v2017",
        "source_crs": "EPSG:2154",
    }


def _legacy_inputs():
    surface_rows = [
        _base_row(
            "F-P-0700",
            "P-1",
            "PRESCRIPTION",
            "prescription_surface",
            "SURFACE",
            "07",
            "00",
        ),
        _base_row(
            "F-I-0200",
            "I-1",
            "INFORMATION",
            "information_surface",
            "SURFACE",
            "02",
            "00",
        ),
    ]
    surface = gpd.GeoDataFrame(
        surface_rows,
        geometry=[
            Polygon([(0, 0), (2, 0), (2, 2), (0, 2)]),
            Polygon([(3, 0), (5, 0), (5, 2), (3, 2)]),
        ],
        crs="EPSG:2154",
        index=pd.Index([11, 22], name="source_row"),
    )
    surface["feature_area_m2"] = [4.0, 4.0]
    line = gpd.GeoDataFrame(
        [
            _base_row(
                "F-P-0704",
                "P-2",
                "PRESCRIPTION",
                "prescription_line",
                "LINE",
                "07",
                "04",
            )
        ],
        geometry=[LineString([(0, 0), (2, 0)])],
        crs="EPSG:2154",
        index=pd.Index([33], name="source_row"),
    )
    line["feature_length_m"] = [2.0]
    point = gpd.GeoDataFrame(
        [
            _base_row(
                "F-I-9900",
                "I-2",
                "INFORMATION",
                "information_point",
                "POINT",
                "99",
                "00",
            )
        ],
        geometry=[Point(1, 1)],
        crs="EPSG:2154",
        index=pd.Index([44], name="source_row"),
    )
    point["point_member_count"] = [1]
    relations = pd.DataFrame(
        [
            {
                "parcel_id": "PARCEL-1",
                **{
                    key: surface.iloc[0][key]
                    for key in (
                        "planning_feature_id",
                        "source_feature_id",
                        "source_identity_kind",
                        "source_identity_field",
                        "logical_layer",
                        "feature_family",
                        "geometry_kind",
                        "type_code_raw",
                        "subtype_code_raw",
                        "label_raw",
                        "text_raw",
                        "source_document_id",
                        "source_archive_sha256",
                        "source_layer",
                        "source_validity_date_raw",
                        "regulation_filename_raw",
                    )
                },
                "relation_type": "AREA_OVERLAP",
                "parcel_metric_area_m2": 4.0,
                "feature_area_m2": 4.0,
                "source_line_length_m": None,
                "intersection_area_m2": 4.0,
                "intersection_length_m": None,
                "parcel_share_pct": 100.0,
                "feature_share_pct": 100.0,
                "point_member_count": None,
                "point_members_inside_count": None,
                "point_members_boundary_count": None,
            },
            {
                "parcel_id": "PARCEL-1",
                **{
                    key: line.iloc[0][key]
                    for key in (
                        "planning_feature_id",
                        "source_feature_id",
                        "source_identity_kind",
                        "source_identity_field",
                        "logical_layer",
                        "feature_family",
                        "geometry_kind",
                        "type_code_raw",
                        "subtype_code_raw",
                        "label_raw",
                        "text_raw",
                        "source_document_id",
                        "source_archive_sha256",
                        "source_layer",
                        "source_validity_date_raw",
                        "regulation_filename_raw",
                    )
                },
                "relation_type": "LENGTH_OVERLAP",
                "parcel_metric_area_m2": 4.0,
                "feature_area_m2": None,
                "source_line_length_m": 2.0,
                "intersection_area_m2": None,
                "intersection_length_m": 2.0,
                "parcel_share_pct": None,
                "feature_share_pct": None,
                "point_member_count": None,
                "point_members_inside_count": None,
                "point_members_boundary_count": None,
            },
        ],
        index=pd.Index([101, 102], name="relation_row"),
    )
    relations = relations.loc[:, list(RELATION_COLUMNS)]
    return _planning_document(), surface, line, point, relations, _profile()


def _mutated_profile(**updates: object) -> CnigFeatureCodeProfile:
    """Build a deliberately unvalidated frozen profile for boundary tests."""

    profile = _profile()
    return profile.model_copy(update=updates)


def _empty_catalog(kind: str) -> gpd.GeoDataFrame:
    """Return an optional empty catalog with the deterministic source schema."""

    _, surface, line, point, _, _ = _inputs()
    template = {"SURFACE": surface, "LINE": line, "POINT": point}[kind]
    return template.iloc[0:0].copy()


def _integration_source_frame(
    logical_layer: str,
    geometries: list[object],
    source_ids: list[str],
    type_codes: list[str],
    subtype_codes: list[str],
) -> gpd.GeoDataFrame:
    prescription = logical_layer.startswith("prescription")
    return gpd.GeoDataFrame(
        {
            "LIBELLE": [f"Label {identifier}" for identifier in source_ids],
            "TXT": [None] * len(source_ids),
            ("TYPEPSC" if prescription else "TYPEINF"): type_codes,
            ("STYPEPSC" if prescription else "STYPEINF"): subtype_codes,
            "NOMFIC": [None] * len(source_ids),
            "URLFIC": [None] * len(source_ids),
            "IDURBA": ["31395_PLU_20240215"] * len(source_ids),
            "DATVALID": ["20240215"] * len(source_ids),
            ("LIB_IDPSC" if prescription else "LIB_IDINFO"): source_ids,
        },
        geometry=geometries,
        crs="EPSG:2154",
    )


def _integration_layer(
    logical_layer: str,
    frame: gpd.GeoDataFrame,
) -> GpuInspectedLayer:
    source_layer = logical_layer.upper()
    reference = GpuSpatialLayerReference(
        Path(f"{logical_layer}.gpkg"), source_layer, "GPKG"
    )
    geometry = frame.geometry
    non_null = ~geometry.isna()
    non_empty = non_null & ~geometry.is_empty
    summary = GpuLayerSummary(
        source_document_id="doc-1",
        source_archive_sha256="a" * 64,
        source_layer=source_layer,
        crs=frame.crs.to_string(),
        feature_count=len(frame),
        columns=tuple(str(column) for column in frame.columns),
        dtypes=tuple(
            (str(column), str(dtype)) for column, dtype in frame.dtypes.items()
        ),
        null_counts=tuple(
            (str(column), int(frame[column].isna().sum())) for column in frame.columns
        ),
        geometry_types=tuple(
            (str(name), int(count))
            for name, count in geometry.geom_type.value_counts().sort_index().items()
        ),
        null_geometry_count=int((~non_null).sum()),
        empty_geometry_count=int((non_null & geometry.is_empty).sum()),
        invalid_geometry_count=int((non_empty & ~geometry.is_valid).sum()),
    )
    return GpuInspectedLayer(logical_layer, reference, frame, summary)  # type: ignore[arg-type]


def _integration_inputs() -> tuple[
    GpuPlanningDocument,
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    pd.DataFrame,
    CnigFeatureCodeProfile,
]:
    layers = (
        _integration_layer(
            "prescription_surface",
            _integration_source_frame(
                "prescription_surface",
                [Polygon([(0, 0), (2, 0), (2, 2), (0, 2)])],
                ["P-1"],
                ["07"],
                ["00"],
            ),
        ),
        _integration_layer(
            "information_surface",
            _integration_source_frame(
                "information_surface",
                [Polygon([(3, 0), (5, 0), (5, 2), (3, 2)])],
                ["I-1"],
                ["02"],
                ["00"],
            ),
        ),
        _integration_layer(
            "prescription_line",
            _integration_source_frame(
                "prescription_line",
                [LineString([(0, 1), (2, 1)])],
                ["P-2"],
                ["07"],
                ["04"],
            ),
        ),
        _integration_layer(
            "information_point",
            _integration_source_frame(
                "information_point",
                [Point(10, 10)],
                ["I-2"],
                ["99"],
                ["00"],
            ),
        ),
    )
    planning_document = _planning_document(related_layers=layers)
    parcels = _integration_parcels()
    normalized = intersect_parcels_with_gpu_planning_features(
        parcels, planning_document
    )
    return (
        planning_document,
        parcels,
        normalized.surface_features,
        normalized.line_features,
        normalized.point_features,
        normalized.relations,
        _profile(),
    )


def _integration_parcels() -> gpd.GeoDataFrame:
    return gpd.GeoDataFrame(
        {"parcel_id": ["PARCEL-1"], "existing_fact": [7]},
        geometry=[Polygon([(0, 0), (2, 0), (2, 2), (0, 2)])],
        crs="EPSG:2154",
        index=pd.Index([91], name="parcel_row"),
    )


def _inputs() -> tuple[
    GpuPlanningDocument,
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    pd.DataFrame,
    CnigFeatureCodeProfile,
]:
    document, _, surface, line, point, relations, profile = _integration_inputs()
    return document, surface, line, point, relations, profile


def resolve_planning_feature_codes(
    planning_document: GpuPlanningDocument,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
) -> PlanningFeatureCodeResult:
    """Exercise the new bound API while keeping legacy unit call sites compact."""

    return _public_resolve_planning_feature_codes(
        planning_document,
        _integration_parcels(),
        surface_features,
        line_features,
        point_features,
        relations,
        code_profile,
    )


def validate_planning_feature_code_result(
    planning_document: GpuPlanningDocument,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
    result: PlanningFeatureCodeResult,
) -> None:
    _public_validate_planning_feature_code_result(
        planning_document,
        _integration_parcels(),
        surface_features,
        line_features,
        point_features,
        relations,
        code_profile,
        result,
    )


def test_exact_family_pair_resolution_and_leading_zeros() -> None:
    result = resolve_planning_feature_codes(*_inputs())
    surface = result.surface_features.set_index("planning_feature_id")
    assert (
        surface.loc["GPU:doc-1:prescription_surface:P-1", "official_code_label"]
        == "Prescription seven"
    )
    assert (
        surface.loc["GPU:doc-1:information_surface:I-1", "official_code_label"]
        == "Information two"
    )
    assert (
        result.line_features.iloc[0]["official_code_label"]
        == "Prescription seven subtype four"
    )
    assert result.line_features.iloc[0]["type_code_raw"] == "07"
    assert result.line_features.iloc[0]["subtype_code_raw"] == "04"
    assert set(surface["official_code_status"]) == {"RESOLVED_OFFICIAL"}


def test_no_type_only_or_cross_family_fallback_and_unknown_is_retained() -> None:
    document, surface, line, point, relations, profile = _inputs()
    payload = _profile_payload()
    payload["records"] = [
        record
        for record in payload["records"]
        if not (
            (record["feature_family"], record["type_code"], record["subtype_code"])
            in {("PRESCRIPTION", "07", "04"), ("INFORMATION", "99", "00")}
        )
    ]
    payload["canonical_records_sha256"] = _records_hash(payload["records"])
    profile = CnigFeatureCodeProfile.model_validate(payload)
    result = resolve_planning_feature_codes(
        document, surface, line, point, relations, profile
    )
    assert result.line_features.iloc[0]["official_code_status"] == "UNKNOWN_CODE_PAIR"
    assert pd.isna(result.line_features.iloc[0]["official_code_label"])
    assert result.point_features.iloc[0]["official_code_status"] == "UNKNOWN_CODE_PAIR"
    assert len(result.line_features) == 1
    assert len(result.point_features) == 1


def test_in_memory_profile_model_copy_with_wrong_hash_is_revalidated() -> None:
    inputs = list(_inputs())
    inputs[-1] = _mutated_profile(canonical_records_sha256="f" * 64)
    with pytest.raises(PlanningFeatureCodeError, match="profile|canonical"):
        resolve_planning_feature_codes(*inputs)


def test_in_memory_profile_model_construct_with_invalid_schema_is_revalidated() -> None:
    profile = _profile()
    invalid = CnigFeatureCodeProfile.model_construct(
        **{**profile.model_dump(mode="python"), "schema_version": 1}
    )
    inputs = list(_inputs())
    inputs[-1] = invalid
    with pytest.raises(PlanningFeatureCodeError, match="schema|profile"):
        resolve_planning_feature_codes(*inputs)


def test_in_memory_profile_model_construct_with_duplicate_pair_is_revalidated() -> None:
    profile = _profile()
    invalid = CnigFeatureCodeProfile.model_construct(
        **{
            **profile.model_dump(mode="python"),
            "records": (*profile.records, profile.records[0]),
        }
    )
    inputs = list(_inputs())
    inputs[-1] = invalid
    with pytest.raises(PlanningFeatureCodeError, match="duplicate|profile"):
        resolve_planning_feature_codes(*inputs)


@pytest.mark.parametrize(
    ("family", "url"),
    [
        ("prescription", "https://www.geoportail-urbanisme.gouv.fr/another/path"),
        ("prescription", f"{P_URL}?format=json"),
        (
            "prescription",
            "https://www.geoportail-urbanisme.gouv.fr:444/standard/cnig_PLU_2017/codes/PrescriptionUrbaType",
        ),
        (
            "prescription",
            "https://user@www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/PrescriptionUrbaType",
        ),
        (
            "prescription",
            "https://geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/PrescriptionUrbaType",
        ),
        ("prescription", I_URL),
        ("information", P_URL),
        ("information", f"{I_URL}#codes"),
        ("information", f"{I_URL}/"),
        ("information", I_URL.replace("https://", "http://")),
    ],
)
def test_official_family_endpoints_require_exact_identity(
    family: str, url: str
) -> None:
    payload = _profile_payload()
    payload["official_sources"][family] = url
    family_name = family.upper()
    for record in payload["records"]:
        if record["feature_family"] == family_name:
            record["official_source_url"] = url
    payload["canonical_records_sha256"] = _records_hash(payload["records"])
    with pytest.raises(ValueError, match="official|source|URL"):
        CnigFeatureCodeProfile.model_validate(payload)


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("official_label", "Repeated  whitespace"),
        ("official_label", "Decomposed e\u0301"),
        ("legal_reference", "L151-1\n  L151-2"),
        ("regulation_or_annex_reference", " R151-1"),
    ],
)
def test_official_text_must_already_be_canonical(field: str, value: str) -> None:
    payload = _profile_payload()
    payload["records"][0][field] = value
    payload["canonical_records_sha256"] = _records_hash(payload["records"])
    with pytest.raises(
        ValueError,
        match="GPU_DISPLAY_TEXT_NFC_WHITESPACE_V1|canonical|normalization|exact",
    ):
        CnigFeatureCodeProfile.model_validate(payload)


@pytest.mark.parametrize("code", ["1", "001", "A1", " 01", "01 ", 1])
def test_malformed_code_is_rejected(code: object) -> None:
    payload = _profile_payload()
    payload["records"][0]["type_code"] = code
    with pytest.raises(ValueError):
        CnigFeatureCodeProfile.model_validate(payload)


def test_duplicate_pair_and_profile_hash_mutation_are_rejected() -> None:
    payload = _profile_payload()
    payload["records"].append(dict(payload["records"][0]))
    with pytest.raises(ValueError, match="duplicate"):
        CnigFeatureCodeProfile.model_validate(payload)
    payload = _profile_payload()
    payload["canonical_records_sha256"] = "f" * 64
    with pytest.raises(ValueError, match="canonical"):
        CnigFeatureCodeProfile.model_validate(payload)


def test_wrong_official_host_and_unknown_field_are_rejected() -> None:
    payload = _profile_payload()
    payload["official_sources"]["prescription"] = "https://example.com/codes"
    with pytest.raises(ValueError, match="official|exact"):
        CnigFeatureCodeProfile.model_validate(payload)
    payload = _profile_payload()
    payload["semantic_policy"] = "BLOCK"
    with pytest.raises(ValueError):
        CnigFeatureCodeProfile.model_validate(payload)


def test_duplicate_yaml_key_is_rejected(tmp_path: Path) -> None:
    path = tmp_path / "codes.yaml"
    path.write_text("schema_version: 1\nschema_version: 1\n", encoding="utf-8")
    with pytest.raises(PlanningFeatureCodeError, match="Duplicate YAML"):
        load_cnig_feature_code_profile(path)


def test_wrong_planning_standard_is_rejected() -> None:
    inputs = list(_inputs())
    inputs[0] = _planning_document("CNIG PLU v2022")
    with pytest.raises(PlanningFeatureCodeError, match="standard"):
        resolve_planning_feature_codes(*inputs)


def test_catalogs_and_relations_are_preserved_and_inputs_immutable() -> None:
    inputs = _inputs()
    snapshots = [frame.copy(deep=True) for frame in inputs[1:5]]
    result = resolve_planning_feature_codes(*inputs)
    for original, snapshot, coded in zip(
        inputs[1:4],
        snapshots[:3],
        (result.surface_features, result.line_features, result.point_features),
        strict=True,
    ):
        assert_geodataframe_equal(original, snapshot)
        assert_geodataframe_equal(coded.loc[:, original.columns], original)
        assert (
            tuple(coded.columns[-len(OFFICIAL_CODE_COLUMNS) :]) == OFFICIAL_CODE_COLUMNS
        )
    pd.testing.assert_frame_equal(inputs[4], snapshots[3])
    pd.testing.assert_frame_equal(result.relations.loc[:, inputs[4].columns], inputs[4])
    assert tuple(result.code_dictionary.columns) == CODE_DICTIONARY_COLUMNS
    assert result.relations.index.equals(inputs[4].index)


@pytest.mark.parametrize(
    ("catalog_position", "column"),
    [
        (1, "feature_area_m2"),
        (2, "feature_length_m"),
        (3, "point_member_count"),
        (1, "label_raw"),
        (1, "source_crs"),
    ],
)
def test_complete_normalized_catalog_schema_is_required(
    catalog_position: int,
    column: str,
) -> None:
    inputs = list(_inputs())
    inputs[catalog_position] = inputs[catalog_position].drop(columns=column)
    with pytest.raises(PlanningFeatureCodeError, match="normalized|schema|column"):
        resolve_planning_feature_codes(*inputs)


def test_unexpected_factual_catalog_column_is_rejected() -> None:
    inputs = list(_inputs())
    surface = inputs[1].copy(deep=True)
    surface["unexpected_fact"] = "not-produced-by-step-7d-3-1"
    inputs[1] = surface
    with pytest.raises(PlanningFeatureCodeError, match="normalized|schema|column"):
        resolve_planning_feature_codes(*inputs)


@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("source_identity_kind", "UNKNOWN_KIND"),
        ("source_identity_field", "LIB_IDINFO"),
    ],
)
def test_cnig_identity_provenance_is_exact(column: str, value: str) -> None:
    inputs = list(_inputs())
    surface = inputs[1].copy(deep=True)
    surface.loc[surface.index[0], column] = value
    inputs[1] = surface
    with pytest.raises(
        PlanningFeatureCodeError, match="identity|provenance|normalized"
    ):
        resolve_planning_feature_codes(*inputs)


@pytest.mark.parametrize(
    ("logical_layer", "feature_family", "source_feature_id"),
    [
        ("information_surface", "INFORMATION", "OGR_FID:1"),
        ("prescription_surface", "PRESCRIPTION", "1"),
    ],
)
def test_ogr_fid_provenance_is_restricted(
    logical_layer: str,
    feature_family: str,
    source_feature_id: str,
) -> None:
    inputs = list(_inputs())
    surface = inputs[1].copy(deep=True)
    row_index = surface.index[0]
    surface.loc[row_index, "logical_layer"] = logical_layer
    surface.loc[row_index, "feature_family"] = feature_family
    surface.loc[row_index, "source_identity_kind"] = "ARCHIVE_SCOPED_OGR_FID"
    surface.loc[row_index, "source_identity_field"] = "OGR_FID"
    surface.loc[row_index, "source_feature_id"] = source_feature_id
    inputs[1] = surface
    with pytest.raises(
        PlanningFeatureCodeError, match="OGR|identity|provenance|normalized"
    ):
        resolve_planning_feature_codes(*inputs)


def test_source_feature_id_is_unique_inside_logical_layer() -> None:
    inputs = list(_inputs())
    surface = inputs[1].copy(deep=True)
    surface.loc[surface.index[1], "logical_layer"] = surface.iloc[0]["logical_layer"]
    surface.loc[surface.index[1], "feature_family"] = surface.iloc[0]["feature_family"]
    surface.loc[surface.index[1], "source_identity_field"] = surface.iloc[0][
        "source_identity_field"
    ]
    surface.loc[surface.index[1], "source_feature_id"] = surface.iloc[0][
        "source_feature_id"
    ]
    inputs[1] = surface
    with pytest.raises(PlanningFeatureCodeError, match="source_feature_id|unique"):
        resolve_planning_feature_codes(*inputs)


def test_catalog_crs_must_be_canonical_epsg_2154() -> None:
    inputs = list(_inputs())
    inputs[1] = inputs[1].to_crs("EPSG:4326")
    with pytest.raises(PlanningFeatureCodeError, match="EPSG:2154|CRS"):
        resolve_planning_feature_codes(*inputs)


@pytest.mark.parametrize(
    ("catalog_position", "column", "value"),
    [
        (1, "feature_area_m2", 99.0),
        (2, "feature_length_m", 99.0),
        (3, "point_member_count", 2),
    ],
)
def test_catalog_geometry_metrics_are_revalidated(
    catalog_position: int,
    column: str,
    value: object,
) -> None:
    inputs = list(_inputs())
    catalog = inputs[catalog_position].copy(deep=True)
    catalog.loc[catalog.index[0], column] = value
    inputs[catalog_position] = catalog
    with pytest.raises(PlanningFeatureCodeError, match="metric|area|length|member"):
        resolve_planning_feature_codes(*inputs)


def test_complete_relation_schema_is_required() -> None:
    inputs = list(_inputs())
    inputs[4] = inputs[4].drop(columns="intersection_length_m")
    with pytest.raises(PlanningFeatureCodeError, match="relation|schema|column"):
        resolve_planning_feature_codes(*inputs)


def test_unexpected_factual_relation_column_is_rejected() -> None:
    inputs = list(_inputs())
    relations = inputs[4].copy(deep=True)
    relations["unexpected_metric"] = 0.0
    inputs[4] = relations
    with pytest.raises(PlanningFeatureCodeError, match="relation|schema"):
        resolve_planning_feature_codes(*inputs)


def test_cnig_resolver_invokes_shared_factual_contract(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    coding_module = importlib.import_module(
        "landscout.stages.resolve_planning_feature_codes"
    )
    calls = 0

    def reject_shared_contract(*args: object) -> None:
        nonlocal calls
        calls += 1
        raise ValueError("shared factual contract marker")

    monkeypatch.setattr(
        coding_module,
        "validate_normalized_planning_feature_inputs",
        reject_shared_contract,
    )
    with pytest.raises(
        PlanningFeatureCodeError, match="shared factual contract marker"
    ):
        resolve_planning_feature_codes(*_inputs())
    assert calls == 1


@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("label_raw", "mutated label"),
        ("source_validity_date_raw", "19990101"),
        ("regulation_filename_raw", "other.pdf"),
        ("feature_area_m2", 3.0),
    ],
)
def test_complete_relation_catalog_agreement_is_required(
    column: str,
    value: object,
) -> None:
    inputs = list(_inputs())
    relations = inputs[4].copy(deep=True)
    relations.loc[relations.index[0], column] = value
    inputs[4] = relations
    with pytest.raises(
        PlanningFeatureCodeError, match="catalog|metric|normalized|feature share"
    ):
        resolve_planning_feature_codes(*inputs)


@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("intersection_area_m2", 0.0),
        ("intersection_area_m2", -1.0),
        ("intersection_area_m2", float("inf")),
        ("parcel_share_pct", 99.0),
    ],
)
def test_surface_relation_metrics_are_revalidated(column: str, value: object) -> None:
    inputs = list(_inputs())
    relations = inputs[4].copy(deep=True)
    relations.loc[relations.index[0], column] = value
    inputs[4] = relations
    with pytest.raises(
        PlanningFeatureCodeError, match="relation|metric|finite|percentage"
    ):
        resolve_planning_feature_codes(*inputs)


@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("intersection_length_m", 0.0),
        ("relation_type", "TOUCH_ONLY"),
        ("source_line_length_m", 1.0),
    ],
)
def test_line_relation_metrics_are_revalidated(column: str, value: object) -> None:
    inputs = list(_inputs())
    relations = inputs[4].copy(deep=True)
    line_index = relations.index[relations["geometry_kind"].eq("LINE")][0]
    relations.loc[line_index, column] = value
    inputs[4] = relations
    with pytest.raises(PlanningFeatureCodeError, match="relation|length|catalog"):
        resolve_planning_feature_codes(*inputs)


def test_duplicate_catalog_columns_are_rejected() -> None:
    document, surface, line, point, relations, profile = _inputs()
    duplicate = pd.concat([surface, surface[["planning_feature_id"]]], axis=1)
    duplicate = gpd.GeoDataFrame(duplicate, geometry="geometry", crs=surface.crs)
    with pytest.raises(PlanningFeatureCodeError, match="duplicate|columns"):
        resolve_planning_feature_codes(
            document, duplicate, line, point, relations, profile
        )


def test_missing_catalog_crs_is_rejected() -> None:
    document, surface, line, point, relations, profile = _inputs()
    surface = surface.set_crs(None, allow_override=True)
    with pytest.raises(PlanningFeatureCodeError, match="CRS"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )


def test_unparseable_catalog_crs_is_rejected() -> None:
    document, surface, line, point, relations, profile = _inputs()
    surface = surface.copy(deep=True)
    surface.geometry.array._crs = "definitely-not-a-crs"  # type: ignore[attr-defined]
    with pytest.raises(PlanningFeatureCodeError, match="CRS"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )


def test_inactive_or_wrong_geometry_column_is_rejected() -> None:
    document, surface, line, point, relations, profile = _inputs()
    surface = surface.copy(deep=True)
    surface["alternate_geometry"] = surface.geometry.copy()
    surface = surface.set_geometry("alternate_geometry")
    with pytest.raises(PlanningFeatureCodeError, match="geometry"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )


@pytest.mark.parametrize(
    ("geometry", "message"),
    [
        (None, "null|geometry"),
        (Polygon(), "empty|geometry"),
        (Polygon([(0, 0), (2, 2), (2, 0), (0, 2), (0, 0)]), "invalid|geometry"),
        (LineString([(0, 0), (1, 1)]), "type|geometry|SURFACE"),
    ],
)
def test_surface_geometry_contract_is_enforced(
    geometry: object,
    message: str,
) -> None:
    document, surface, line, point, relations, profile = _inputs()
    surface = surface.copy(deep=True)
    surface.at[surface.index[0], "geometry"] = geometry
    with pytest.raises(PlanningFeatureCodeError, match=message):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )


@pytest.mark.parametrize(
    ("catalog_name", "geometry"),
    [
        ("surface", MultiPolygon([Polygon([(0, 0), (2, 0), (2, 2), (0, 2)])])),
        ("line", MultiLineString([[(0, 0), (2, 0)]])),
        ("point", MultiPoint([(0, 0), (1, 1)])),
    ],
)
def test_valid_multi_geometries_are_accepted(
    catalog_name: str, geometry: object
) -> None:
    document, parcels, _, _, _, _, profile = _integration_inputs()
    target_logical = {
        "surface": "prescription_surface",
        "line": "prescription_line",
        "point": "information_point",
    }[catalog_name]
    changed_layers: list[GpuInspectedLayer] = []
    for layer in document.related_layers:
        if layer.logical_name != target_logical:
            changed_layers.append(layer)
            continue
        source = layer.data.copy(deep=True)
        source.at[source.index[0], "geometry"] = geometry
        changed_layers.append(_integration_layer(target_logical, source))
    changed_document = _planning_document(related_layers=tuple(changed_layers))
    normalized = intersect_parcels_with_gpu_planning_features(parcels, changed_document)
    result = _public_resolve_planning_feature_codes(
        changed_document,
        parcels,
        normalized.surface_features,
        normalized.line_features,
        normalized.point_features,
        normalized.relations,
        profile,
    )
    assert getattr(result, f"{catalog_name}_features").geometry.iloc[0].equals(geometry)


@pytest.mark.parametrize(
    ("column", "value", "message"),
    [
        ("geometry_kind", "LINE", "geometry kind|SURFACE"),
        ("logical_layer", "prescription_line", "logical layer|surface"),
        ("feature_family", "INFORMATION", "family|logical layer"),
        ("source_identity_kind", None, "source identity|exact string"),
        ("source_layer", " SOURCE ", "source layer|exact string"),
    ],
)
def test_catalog_semantic_and_string_contracts_are_enforced(
    column: str,
    value: object,
    message: str,
) -> None:
    document, surface, line, point, relations, profile = _inputs()
    surface = surface.copy(deep=True)
    surface.loc[surface.index[0], column] = value
    with pytest.raises(PlanningFeatureCodeError, match=message):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )


@pytest.mark.parametrize(
    "column",
    [
        "planning_feature_id",
        "source_feature_id",
        "source_identity_kind",
        "source_identity_field",
        "logical_layer",
        "feature_family",
        "geometry_kind",
        "source_layer",
    ],
)
def test_every_required_catalog_identity_is_an_exact_non_null_string(
    column: str,
) -> None:
    document, surface, line, point, relations, profile = _inputs()
    surface = surface.copy(deep=True)
    relations = relations.copy(deep=True)
    feature_id = surface.iloc[0]["planning_feature_id"]
    surface.loc[surface.index[0], column] = " invalid "
    if column in relations.columns:
        relations.loc[relations["planning_feature_id"].eq(feature_id), column] = (
            " invalid "
        )
    with pytest.raises(PlanningFeatureCodeError, match="exact string|non-empty"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )


@pytest.mark.parametrize(
    ("catalog_name", "geometry"),
    [
        ("line", Polygon([(0, 0), (1, 0), (1, 1), (0, 1)])),
        ("point", LineString([(0, 0), (1, 1)])),
    ],
)
def test_line_and_point_geometry_types_are_enforced(
    catalog_name: str,
    geometry: object,
) -> None:
    document, surface, line, point, relations, profile = _inputs()
    catalogs = {"line": line.copy(deep=True), "point": point.copy(deep=True)}
    catalog = catalogs[catalog_name]
    catalog.at[catalog.index[0], "geometry"] = geometry
    catalogs[catalog_name] = catalog
    with pytest.raises(PlanningFeatureCodeError, match="geometry|type"):
        resolve_planning_feature_codes(
            document,
            surface,
            catalogs["line"],
            catalogs["point"],
            relations,
            profile,
        )


def test_planning_feature_ids_are_globally_unique_across_catalogs() -> None:
    document, surface, line, point, relations, profile = _inputs()
    line = line.copy(deep=True)
    line.loc[line.index[0], "planning_feature_id"] = surface.iloc[0][
        "planning_feature_id"
    ]
    with pytest.raises(PlanningFeatureCodeError, match="unique|catalog|deterministic"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )


def test_valid_empty_optional_catalogs_preserve_schema_and_crs() -> None:
    document, parcels, _, _, _, _, profile = _integration_inputs()
    surface_layers = tuple(
        layer
        for layer in document.related_layers
        if layer.logical_name in {"prescription_surface", "information_surface"}
    )
    document = _planning_document(related_layers=surface_layers)
    normalized = intersect_parcels_with_gpu_planning_features(parcels, document)
    result = _public_resolve_planning_feature_codes(
        document,
        parcels,
        normalized.surface_features,
        normalized.line_features,
        normalized.point_features,
        normalized.relations,
        profile,
    )
    for original, coded in (
        (normalized.line_features, result.line_features),
        (normalized.point_features, result.point_features),
    ):
        assert coded.empty
        assert coded.crs == original.crs
        assert tuple(coded.columns[: len(original.columns)]) == tuple(original.columns)
        assert (
            tuple(coded.columns[-len(OFFICIAL_CODE_COLUMNS) :]) == OFFICIAL_CODE_COLUMNS
        )


def test_relation_catalog_code_mismatch_is_rejected() -> None:
    document, surface, line, point, relations, profile = _inputs()
    relations = relations.copy(deep=True)
    relation_index = relations.index[0]
    original = relations.loc[relation_index, "subtype_code_raw"]
    relations.loc[relation_index, "subtype_code_raw"] = (
        "04" if original != "04" else "00"
    )
    with pytest.raises(PlanningFeatureCodeError, match="catalog"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )


def test_duplicate_relation_columns_are_rejected() -> None:
    document, surface, line, point, relations, profile = _inputs()
    duplicate = pd.concat([relations, relations[["parcel_id"]]], axis=1)
    with pytest.raises(PlanningFeatureCodeError, match="duplicate|columns"):
        resolve_planning_feature_codes(
            document, surface, line, point, duplicate, profile
        )


@pytest.mark.parametrize("column", ["parcel_id", "planning_feature_id"])
@pytest.mark.parametrize("value", [None, " invalid "])
def test_relation_identity_must_be_an_exact_non_null_string(
    column: str,
    value: object,
) -> None:
    document, surface, line, point, relations, profile = _inputs()
    relations = relations.copy(deep=True)
    relations.loc[relations.index[0], column] = value
    with pytest.raises(PlanningFeatureCodeError, match="relation|exact string"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )


def test_duplicate_parcel_feature_relation_is_rejected() -> None:
    document, surface, line, point, relations, profile = _inputs()
    relations = pd.concat([relations, relations.iloc[[0]]], ignore_index=True)
    relations = _canonical_relation_schema(relations)
    with pytest.raises(PlanningFeatureCodeError, match="unique|duplicate"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )


def test_unknown_relation_feature_id_is_rejected() -> None:
    document, surface, line, point, relations, profile = _inputs()
    relations = relations.copy(deep=True)
    relations.loc[relations.index[0], "planning_feature_id"] = "UNKNOWN"
    with pytest.raises(PlanningFeatureCodeError, match="unknown"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )


@pytest.mark.parametrize(
    ("geometry_kind", "relation_type"),
    [
        ("SURFACE", "LENGTH_OVERLAP"),
        ("SURFACE", "NOT_A_RELATION"),
        ("LINE", "INSIDE"),
        ("POINT", "AREA_OVERLAP"),
    ],
)
def test_relation_type_must_match_catalog_geometry_kind(
    geometry_kind: str,
    relation_type: str,
) -> None:
    document, surface, line, point, relations, profile = _inputs()
    catalogs = {"SURFACE": surface, "LINE": line, "POINT": point}
    feature = catalogs[geometry_kind].iloc[0]
    row = relations.iloc[0].copy()
    for column in (
        "planning_feature_id",
        "source_feature_id",
        "source_identity_kind",
        "source_identity_field",
        "logical_layer",
        "feature_family",
        "geometry_kind",
        "type_code_raw",
        "subtype_code_raw",
        "source_document_id",
        "source_archive_sha256",
        "source_layer",
        "label_raw",
        "text_raw",
        "source_validity_date_raw",
        "regulation_filename_raw",
    ):
        row[column] = feature[column]
    row["relation_type"] = relation_type
    metric_columns = (
        "feature_area_m2",
        "source_line_length_m",
        "intersection_area_m2",
        "intersection_length_m",
        "parcel_share_pct",
        "feature_share_pct",
        "point_member_count",
        "point_members_inside_count",
        "point_members_boundary_count",
    )
    for column in metric_columns:
        row[column] = None
    if geometry_kind == "SURFACE":
        area = 4.0 if relation_type == "AREA_OVERLAP" else 0.0
        row["feature_area_m2"] = 4.0
        row["intersection_area_m2"] = area
        row["parcel_share_pct"] = 100.0 if area else 0.0
        row["feature_share_pct"] = 100.0 if area else 0.0
    elif geometry_kind == "LINE":
        row["source_line_length_m"] = 2.0
        row["intersection_length_m"] = 2.0 if relation_type == "LENGTH_OVERLAP" else 0.0
    else:
        row["point_member_count"] = 1
        row["point_members_inside_count"] = 1 if relation_type == "INSIDE" else 0
        row["point_members_boundary_count"] = (
            1 if relation_type == "BOUNDARY_TOUCH" else 0
        )
    candidate = pd.DataFrame([row], columns=relations.columns)
    candidate = _canonical_relation_schema(candidate)
    with pytest.raises(PlanningFeatureCodeError, match="[Rr]elation type|geometry"):
        resolve_planning_feature_codes(
            document, surface, line, point, candidate, profile
        )


@pytest.mark.parametrize(
    ("geometry_kind", "relation_type"),
    [
        ("SURFACE", "AREA_OVERLAP"),
        ("SURFACE", "TOUCH_ONLY"),
        ("LINE", "LENGTH_OVERLAP"),
        ("LINE", "TOUCH_ONLY"),
        ("POINT", "INSIDE"),
        ("POINT", "BOUNDARY_TOUCH"),
    ],
)
def test_valid_relation_types_are_retained(
    geometry_kind: str,
    relation_type: str,
) -> None:
    geometry: object
    if geometry_kind == "SURFACE":
        logical = "prescription_surface"
        geometry = (
            Polygon([(0, 0), (2, 0), (2, 2), (0, 2)])
            if relation_type == "AREA_OVERLAP"
            else Polygon([(2, 0), (4, 0), (4, 2), (2, 2)])
        )
    elif geometry_kind == "LINE":
        logical = "prescription_line"
        geometry = (
            LineString([(0, 1), (2, 1)])
            if relation_type == "LENGTH_OVERLAP"
            else LineString([(-1, 0), (0, 0)])
        )
    else:
        logical = "information_point"
        geometry = Point(1, 1) if relation_type == "INSIDE" else Point(0, 1)
    source = _integration_source_frame(
        logical,
        [geometry],
        ["FEATURE-1"],
        ["07" if logical.startswith("prescription") else "99"],
        ["00"],
    )
    document = _planning_document(related_layers=(_integration_layer(logical, source),))
    parcels = _integration_parcels()
    normalized = intersect_parcels_with_gpu_planning_features(parcels, document)
    result = _public_resolve_planning_feature_codes(
        document,
        parcels,
        normalized.surface_features,
        normalized.line_features,
        normalized.point_features,
        normalized.relations,
        _profile(),
    )
    assert result.relations["relation_type"].tolist() == [relation_type]


def test_coordinated_output_hash_mutation_is_rejected() -> None:
    inputs = _inputs()
    result = resolve_planning_feature_codes(*inputs)
    surface = result.surface_features.copy(deep=True)
    surface.loc[surface.index[0], "official_code_label"] = "Mutated"
    mutated = _result_with_hashes(replace(result, surface_features=surface))
    with pytest.raises(PlanningFeatureCodeError, match="rebuilt|meaning|dictionary"):
        validate_planning_feature_code_result(*inputs, mutated)


def test_parquet_readback_passes_source_complete_validation(tmp_path: Path) -> None:
    inputs = _inputs()
    result = resolve_planning_feature_codes(*inputs)
    paths = {
        name: tmp_path / f"{name}.parquet"
        for name in (
            "code_dictionary",
            "surface_features",
            "line_features",
            "point_features",
            "relations",
        )
    }
    for name, path in paths.items():
        getattr(result, name).to_parquet(path, index=True)
    persisted = replace(
        result,
        code_dictionary=pd.read_parquet(paths["code_dictionary"]),
        surface_features=gpd.read_parquet(paths["surface_features"]),
        line_features=gpd.read_parquet(paths["line_features"]),
        point_features=gpd.read_parquet(paths["point_features"]),
        relations=pd.read_parquet(paths["relations"]),
    )
    validate_planning_feature_code_result(*inputs, persisted)


def test_record_order_must_be_deterministic() -> None:
    payload = _profile_payload()
    payload["records"] = list(reversed(payload["records"]))
    with pytest.raises(ValueError, match="deterministic order"):
        CnigFeatureCodeProfile.model_validate(payload)


def test_yaml_snapshot_loads_strictly(tmp_path: Path) -> None:
    payload = _profile_payload()
    path = tmp_path / "profile.yaml"
    path.write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")
    assert load_cnig_feature_code_profile(path) == _profile()


def test_stable_public_api_is_exported_from_module_and_stage_package() -> None:
    from landscout import stages

    coding_module = importlib.import_module(
        "landscout.stages.resolve_planning_feature_codes"
    )

    required = {
        "CnigFeatureCodeProfile",
        "PlanningFeatureCodeError",
        "PlanningFeatureCodeResult",
        "load_cnig_feature_code_profile",
        "resolve_planning_feature_codes",
        "validate_planning_feature_code_result",
        "validate_planning_feature_code_result_envelope",
    }
    low_level = {
        "_canonical_json_sha256",
        "_coded_catalog",
        "_lookup",
        "_profile_sha256",
        "_result_with_hashes",
    }
    assert required.issubset(set(coding_module.__all__))
    assert required.issubset(set(stages.__all__))
    for name in required:
        assert getattr(stages, name) is getattr(coding_module, name)
    assert low_level.isdisjoint(coding_module.__all__)
    assert low_level.isdisjoint(stages.__all__)


def test_checked_in_official_snapshot_is_complete_for_observed_muret_pairs() -> None:
    path = Path("configs/planning/cnig_plu_2017_feature_codes.yaml")
    profile = load_cnig_feature_code_profile(path)
    expected_records = (
        (
            "INFORMATION",
            "02",
            "00",
            "Zone d'aménagement concerté",
            "L311-1 code de l’urbanisme",
            "R151-52 8°",
            I_URL,
        ),
        (
            "INFORMATION",
            "14",
            "00",
            "Périmètre de voisinage d'infrastructure de transport terrestre (secteur affecté par le bruit)",
            "L571-10 code de l’environnement",
            "R151-53 5°",
            I_URL,
        ),
        (
            "INFORMATION",
            "27",
            "00",
            "Plan d'exposition au bruit des aérodromes",
            "L112-6 code de l’urbanisme",
            "R151-52 2°",
            I_URL,
        ),
        (
            "INFORMATION",
            "99",
            "00",
            "Autre périmètre, secteur, plan, document, site, projet, espace.",
            None,
            None,
            I_URL,
        ),
        (
            "PRESCRIPTION",
            "01",
            "00",
            "Espace boisé classé",
            "L113-1",
            "R151-31 1°",
            P_URL,
        ),
        (
            "PRESCRIPTION",
            "05",
            "00",
            "Emplacement réservé",
            "L151-41 1° à 3°",
            "R151-34 4°, R151-38 1°, R151-43 3°, R151-48 2°, R151-50 1°",
            P_URL,
        ),
        (
            "PRESCRIPTION",
            "07",
            "00",
            "Patrimoine bâti, paysager ou éléments de paysages à protéger pour des motifs d'ordre culturel, historique, architectural ou écologique",
            "L151-19 et L151-23",
            "R151-41 3° Et R151-43",
            P_URL,
        ),
        (
            "PRESCRIPTION",
            "07",
            "04",
            "Éléments de paysage, (sites et secteurs) à préserver pour des motifs d'ordre écologique",
            "L151-23",
            "R151-43 5°",
            P_URL,
        ),
        (
            "PRESCRIPTION",
            "15",
            "00",
            "Règles d’implantation des constructions",
            "L151-17 et L151-18",
            "R151-39 dernier al.",
            P_URL,
        ),
        (
            "PRESCRIPTION",
            "15",
            "01",
            "Implantation des constructions par rapport aux voies et aux emprises publiques",
            "L151-17 et L151-18",
            "R151-39",
            P_URL,
        ),
        (
            "PRESCRIPTION",
            "17",
            "00",
            "Secteur à programme de logements mixité sociale en zone U et AU",
            "L151-15",
            "R151-38 3°",
            P_URL,
        ),
        (
            "PRESCRIPTION",
            "18",
            "00",
            "Périmètre comportant des orientations d’aménagement et de programmation (OAP)",
            "L151-6 et L151-7",
            "R151-6 à R151-8-1",
            P_URL,
        ),
    )
    actual_records = tuple(
        (
            record.feature_family,
            record.type_code,
            record.subtype_code,
            record.official_label,
            record.legal_reference,
            record.regulation_or_annex_reference,
            record.official_source_url,
        )
        for record in profile.records
    )
    assert profile.schema_version == 2
    assert profile.profile == "cnig_plu_2017_muret_observed_pairs_v2"
    assert profile.standard_model == "CNIG PLU v2017"
    assert profile.official_text_normalization == TEXT_NORMALIZATION
    assert profile.retrieval_date.isoformat() == "2026-08-12"
    assert profile.official_sources.prescription == P_URL
    assert profile.official_sources.information == I_URL
    assert (
        profile.canonical_records_sha256
        == "5990552a681a9e50c072eb207bf88d25c876f61c89eeb88618e74d905487672c"
    )
    assert (
        _payload_hash(profile.model_dump(mode="json"))
        == "5611b814eb4bc057578b908c6505094f9df5d2c2bf4ca126629b1362983c47ee"
    )
    assert actual_records == expected_records


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("result_hash_schema_version", True),
        ("result_hash_schema_version", 0),
        ("result_hash_schema_version", 1),
        ("result_hash_schema_version", 2),
        ("result_hash_schema_version", 3),
        ("result_hash_schema_version", 4),
        ("result_hash_schema_version", 6),
        ("result_hash_schema_version", 5.0),
        ("result_hash_schema_version", "5"),
        ("profile_schema_version", True),
        ("profile_schema_version", 0),
        ("profile_schema_version", 1),
        ("profile_schema_version", 3),
        ("profile_schema_version", 2.0),
        ("profile_schema_version", "2"),
    ],
)
def test_result_schema_versions_are_strict(field: str, value: object) -> None:
    inputs = _inputs()
    result = resolve_planning_feature_codes(*inputs)
    with pytest.raises(PlanningFeatureCodeError, match="schema version"):
        validate_planning_feature_code_result(
            *inputs, replace(result, **{field: value})
        )


def test_step_7d_3_1_output_integrates_with_public_coding_api() -> None:
    inputs = _integration_inputs()
    result = _public_resolve_planning_feature_codes(*inputs)
    assert result.result_hash_schema_version == 5
    assert result.profile_schema_version == 2
    assert len(result.surface_features) == 2
    assert len(result.line_features) == 1
    assert len(result.point_features) == 1
    assert len(result.relations) == 2
    assert set(result.surface_features["official_code_status"]) == {"RESOLVED_OFFICIAL"}
    _public_validate_planning_feature_code_result(*inputs, result)


def test_resolver_runs_heavy_factual_validation_once_and_public_validator_repeats(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inputs = _integration_inputs()
    coding_module = importlib.import_module(
        "landscout.stages.resolve_planning_feature_codes"
    )
    enrich_module = importlib.import_module("landscout.stages.enrich_planning_features")
    actual_physical = enrich_module.revalidate_gpu_spatial_layer_sources
    actual_relations = enrich_module._build_relation_tables
    calls = {"physical": 0, "relations": 0}

    def counted_physical(*args: object, **kwargs: object) -> object:
        calls["physical"] += 1
        return actual_physical(*args, **kwargs)

    def counted_relations(*args: object, **kwargs: object) -> object:
        calls["relations"] += 1
        return actual_relations(*args, **kwargs)

    monkeypatch.setattr(
        enrich_module, "revalidate_gpu_spatial_layer_sources", counted_physical
    )
    monkeypatch.setattr(enrich_module, "_build_relation_tables", counted_relations)

    result = coding_module.resolve_planning_feature_codes(*inputs)
    assert calls == {"physical": 1, "relations": 1}

    coding_module.validate_planning_feature_code_result(*inputs, result)
    assert calls == {"physical": 2, "relations": 2}


def test_coded_result_persists_all_source_input_hashes() -> None:
    result = _public_resolve_planning_feature_codes(*_integration_inputs())
    for hash_field in (
        "planning_document_context_sha256",
        "parcel_identity_input_sha256",
        "normalized_catalogs_input_sha256",
        "normalized_relations_input_sha256",
        "gpu_related_source_files_sha256",
        "expected_relations_content_sha256",
    ):
        value = getattr(result, hash_field)
        assert isinstance(value, str)
        assert len(value) == 64
        int(value, 16)


@pytest.mark.parametrize(
    "field",
    [
        "planning_document_context_sha256",
        "parcel_identity_input_sha256",
        "normalized_catalogs_input_sha256",
        "normalized_relations_input_sha256",
        "gpu_related_source_files_sha256",
        "expected_relations_content_sha256",
    ],
)
def test_source_input_hash_mutation_is_rejected(field: str) -> None:
    inputs = _integration_inputs()
    result = _public_resolve_planning_feature_codes(*inputs)
    with pytest.raises(PlanningFeatureCodeError, match="hash|rebuilt|source"):
        _public_validate_planning_feature_code_result(
            *inputs, replace(result, **{field: "f" * 64})
        )


def test_gpu_related_source_hash_is_deterministic_across_cache_roots(
    tmp_path: Path,
) -> None:
    first_inputs = _integration_inputs()
    first_document = first_inputs[0]
    source_root = first_document.extraction.extraction_root
    relocated_root = tmp_path / "relocated-extraction"
    shutil.copytree(source_root, relocated_root)

    def relocated_reference(
        reference: GpuSpatialLayerReference,
    ) -> GpuSpatialLayerReference:
        relative = reference.dataset_path.relative_to(source_root)
        return replace(reference, dataset_path=relocated_root / relative)

    reference_map = {
        reference: relocated_reference(reference)
        for reference in first_document.all_spatial_layers
    }
    relocated_document = replace(
        first_document,
        extraction=replace(
            first_document.extraction,
            extraction_root=relocated_root,
        ),
        all_spatial_layers=tuple(
            reference_map[reference] for reference in first_document.all_spatial_layers
        ),
        zoning=replace(
            first_document.zoning,
            reference=reference_map[first_document.zoning.reference],
        ),
        related_layers=tuple(
            replace(layer, reference=reference_map[layer.reference])
            for layer in first_document.related_layers
        ),
    )
    second_inputs = (relocated_document, *first_inputs[1:])
    first = _public_resolve_planning_feature_codes(*first_inputs)
    second = _public_resolve_planning_feature_codes(*second_inputs)
    assert (
        first.gpu_related_source_files_sha256 == second.gpu_related_source_files_sha256
    )


@pytest.mark.parametrize(
    "field",
    ["gpu_related_source_files_sha256", "expected_relations_content_sha256"],
)
def test_source_binding_hashes_bind_every_component_hash(field: str) -> None:
    result = _public_resolve_planning_feature_codes(*_integration_inputs())
    changed = _result_with_hashes(replace(result, **{field: "f" * 64}))
    for hash_field in (
        "code_dictionary_content_sha256",
        "surface_features_content_sha256",
        "line_features_content_sha256",
        "point_features_content_sha256",
        "relations_content_sha256",
        "complete_result_content_sha256",
    ):
        assert getattr(changed, hash_field) != getattr(result, hash_field)


def test_parcel_source_change_invalidates_coded_result() -> None:
    inputs = list(_integration_inputs())
    result = _public_resolve_planning_feature_codes(*inputs)
    parcels = inputs[1].copy(deep=True)
    parcels.loc[parcels.index[0], "parcel_id"] = "CHANGED-PARCEL"
    inputs[1] = parcels
    with pytest.raises(PlanningFeatureCodeError, match="parcel|source|rebuilt"):
        _public_validate_planning_feature_code_result(*inputs, result)


def test_gpu_document_context_change_invalidates_coded_result() -> None:
    inputs = list(_integration_inputs())
    result = _public_resolve_planning_feature_codes(*inputs)
    planning_document = inputs[0]
    archive = planning_document.extraction.archive
    changed_document = replace(archive.document, provider="Changed provider")
    inputs[0] = replace(
        planning_document,
        extraction=replace(
            planning_document.extraction,
            archive=replace(archive, document=changed_document),
        ),
    )
    with pytest.raises(PlanningFeatureCodeError, match="document|source|rebuilt"):
        _public_validate_planning_feature_code_result(*inputs, result)


def test_normalized_catalog_change_invalidates_coded_result_even_when_coherent() -> (
    None
):
    inputs = list(_integration_inputs())
    result = _public_resolve_planning_feature_codes(*inputs)
    surface = inputs[2].copy(deep=True)
    relations = inputs[5].copy(deep=True)
    feature_id = surface.iloc[0]["planning_feature_id"]
    surface.loc[surface.index[0], "label_raw"] = "Coherently changed"
    relations.loc[relations["planning_feature_id"].eq(feature_id), "label_raw"] = (
        "Coherently changed"
    )
    inputs[2] = surface
    inputs[5] = relations
    with pytest.raises(PlanningFeatureCodeError, match="normalized|source|rebuilt"):
        _public_validate_planning_feature_code_result(*inputs, result)


def test_normalized_relation_change_invalidates_coded_result() -> None:
    inputs = list(_integration_inputs())
    result = _public_resolve_planning_feature_codes(*inputs)
    relations = inputs[5].copy(deep=True)
    line_mask = relations["geometry_kind"].eq("LINE")
    relations.loc[line_mask, "parcel_metric_area_m2"] = 8.0
    inputs[5] = relations
    with pytest.raises(PlanningFeatureCodeError, match="[Rr]elation|source|rebuilt"):
        _public_validate_planning_feature_code_result(*inputs, result)


@pytest.mark.parametrize("mutation", ["missing", "extra", "reordered", "metric"])
def test_coding_api_rejects_relation_set_not_rebuilt_from_geometry(
    mutation: str,
) -> None:
    inputs = list(_integration_inputs())
    relations = inputs[5].copy(deep=True)
    if mutation == "missing":
        relations = relations.iloc[1:].copy()
    elif mutation == "extra":
        extra = relations.iloc[[0]].copy(deep=True)
        extra.loc[extra.index[0], "parcel_id"] = "PARCEL-OTHER"
        relations = pd.concat([relations, extra], ignore_index=True)
    elif mutation == "reordered":
        relations = relations.iloc[::-1].reset_index(drop=True)
    else:
        line_mask = relations["geometry_kind"].eq("LINE")
        relations.loc[line_mask, "intersection_length_m"] = 1.0
    inputs[5] = relations
    with pytest.raises(
        PlanningFeatureCodeError,
        match="relation|parcel|source|rebuilt|normalized",
    ):
        _public_resolve_planning_feature_codes(*inputs)


def test_schema_v5_parquet_readback_preserves_source_hash_envelope(
    tmp_path: Path,
) -> None:
    inputs = _integration_inputs()
    result = _public_resolve_planning_feature_codes(*inputs)
    paths = {
        name: tmp_path / f"integrated-{name}.parquet"
        for name in (
            "code_dictionary",
            "surface_features",
            "line_features",
            "point_features",
            "relations",
        )
    }
    for name, path in paths.items():
        getattr(result, name).to_parquet(path, index=True)
    persisted = replace(
        result,
        code_dictionary=pd.read_parquet(paths["code_dictionary"]),
        surface_features=gpd.read_parquet(paths["surface_features"]),
        line_features=gpd.read_parquet(paths["line_features"]),
        point_features=gpd.read_parquet(paths["point_features"]),
        relations=pd.read_parquet(paths["relations"]),
    )
    _public_validate_planning_feature_code_result(*inputs, persisted)


def test_schema_v5_public_api_signatures_remain_source_complete() -> None:
    assert tuple(
        inspect.signature(_public_resolve_planning_feature_codes).parameters
    ) == (
        "planning_document",
        "parcels",
        "surface_features",
        "line_features",
        "point_features",
        "relations",
        "code_profile",
    )
    assert tuple(
        inspect.signature(_public_validate_planning_feature_code_result).parameters
    ) == (
        "planning_document",
        "parcels",
        "surface_features",
        "line_features",
        "point_features",
        "relations",
        "code_profile",
        "result",
    )


def test_step_7d_5b_2b_5_exposes_lightweight_coded_result_validator() -> None:
    module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
    assert hasattr(module, "validate_planning_feature_code_result_envelope")
    inputs = _inputs()
    result = resolve_planning_feature_codes(*inputs)
    module.validate_planning_feature_code_result_envelope(result)
    with pytest.raises(PlanningFeatureCodeError, match="hash|invalid"):
        module.validate_planning_feature_code_result_envelope(
            replace(result, complete_result_content_sha256="0" * 64)
        )


def _schema_v5_envelope_result() -> PlanningFeatureCodeResult:
    return resolve_planning_feature_codes(*_inputs())


def _canonical_empty_coded_result(
    result: PlanningFeatureCodeResult,
    *,
    empty_dictionary: bool,
) -> PlanningFeatureCodeResult:
    catalogs: dict[str, gpd.GeoDataFrame] = {}
    for field, kind in (
        ("surface_features", "SURFACE"),
        ("line_features", "LINE"),
        ("point_features", "POINT"),
    ):
        output = getattr(result, field).iloc[0:0].copy(deep=True)
        for column, dtype in zip(output.columns, feature_dtypes(kind), strict=True):
            if dtype != "geometry":
                output[column] = pd.Series(index=output.index, dtype=dtype)
        output.index = pd.Index([], dtype="int64")
        catalogs[field] = output
    relations = result.relations.iloc[0:0].copy(deep=True)
    for column, dtype in zip(relations.columns, relation_dtypes(), strict=True):
        relations[column] = pd.Series(index=relations.index, dtype=dtype)
    relations.index = pd.Index([], dtype="int64")
    dictionary = result.code_dictionary.copy(deep=True)
    if empty_dictionary:
        dictionary = dictionary.iloc[0:0].copy(deep=True)
        dictionary.index = pd.Index([], dtype="int64")
    return _result_with_hashes(
        replace(
            result,
            code_dictionary=dictionary,
            relations=relations,
            **catalogs,
        )
    )


def test_schema_v5_envelope_rejects_canonical_empty_code_dictionary() -> None:
    module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
    result = _canonical_empty_coded_result(
        _schema_v5_envelope_result(), empty_dictionary=True
    )
    with pytest.raises(PlanningFeatureCodeError, match="dictionary|empty|record"):
        module.validate_planning_feature_code_result_envelope(result)


def test_schema_v5_envelope_accepts_nonempty_dictionary_with_empty_outputs() -> None:
    module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
    result = _canonical_empty_coded_result(
        _schema_v5_envelope_result(), empty_dictionary=False
    )
    assert len(result.code_dictionary) >= 1
    assert (
        sum(
            len(frame)
            for frame in (
                result.surface_features,
                result.line_features,
                result.point_features,
                result.relations,
            )
        )
        == 0
    )
    module.validate_planning_feature_code_result_envelope(result)


@pytest.mark.parametrize("dictionary", [None, "not-a-frame"])
def test_schema_v5_envelope_controls_malformed_dictionary_type(
    dictionary: object,
) -> None:
    module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
    result = _schema_v5_envelope_result()
    with pytest.raises(PlanningFeatureCodeError):
        module.validate_planning_feature_code_result_envelope(
            replace(result, code_dictionary=dictionary)
        )


def test_schema_v5_envelope_rejects_geospatial_code_dictionary() -> None:
    module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
    result = _schema_v5_envelope_result()
    dictionary = gpd.GeoDataFrame(result.code_dictionary.copy(deep=True))
    with pytest.raises(PlanningFeatureCodeError, match="dictionary|DataFrame"):
        module.validate_planning_feature_code_result_envelope(
            replace(result, code_dictionary=dictionary)
        )


@pytest.mark.parametrize(
    "mutation", ["dtype", "range-index", "index-name", "index-dtype"]
)
def test_schema_v5_dictionary_schema_is_explicit(mutation: str) -> None:
    module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
    result = _schema_v5_envelope_result()
    dictionary = result.code_dictionary.copy(deep=True)
    if mutation == "dtype":
        dictionary["official_label"] = dictionary["official_label"].astype("category")
    elif mutation == "range-index":
        dictionary.index = pd.RangeIndex(len(dictionary))
    elif mutation == "index-name":
        dictionary.index = dictionary.index.rename("changed")
    else:
        dictionary.index = pd.Index(dictionary.index.to_numpy(), dtype="uint64")
    changed = _result_with_hashes(replace(result, code_dictionary=dictionary))
    with pytest.raises(PlanningFeatureCodeError, match="dictionary|schema|dtype|index"):
        module.validate_planning_feature_code_result_envelope(changed)


@pytest.mark.parametrize(
    "mutation",
    [
        "duplicate-pair",
        "unsorted-pairs",
        "malformed-type",
        "malformed-subtype",
        "wrong-family",
        "wrong-url",
        "wrong-profile",
        "wrong-profile-sha",
        "literal-null-reference",
    ],
)
def test_schema_v5_dictionary_rows_are_intrinsically_validated(mutation: str) -> None:
    module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
    result = _schema_v5_envelope_result()
    dictionary = result.code_dictionary.copy(deep=True)
    if mutation == "duplicate-pair":
        dictionary.loc[
            dictionary.index[1], ["feature_family", "type_code", "subtype_code"]
        ] = dictionary.loc[
            dictionary.index[0], ["feature_family", "type_code", "subtype_code"]
        ].tolist()
    elif mutation == "unsorted-pairs":
        dictionary = dictionary.iloc[::-1].copy(deep=True)
    elif mutation == "malformed-type":
        dictionary.loc[dictionary.index[0], "type_code"] = "1"
    elif mutation == "malformed-subtype":
        dictionary.loc[dictionary.index[0], "subtype_code"] = "000"
    elif mutation == "wrong-family":
        dictionary.loc[dictionary.index[0], "feature_family"] = "ZONING"
    elif mutation == "wrong-url":
        dictionary.loc[dictionary.index[0], "official_source_url"] = (
            "https://example.com/codes"
        )
    elif mutation == "wrong-profile":
        dictionary.loc[dictionary.index[0], "profile"] = "other-profile"
    elif mutation == "wrong-profile-sha":
        dictionary.loc[dictionary.index[0], "profile_sha256"] = "a" * 64
    else:
        dictionary.loc[dictionary.index[0], "legal_reference"] = "None"
    changed = _result_with_hashes(replace(result, code_dictionary=dictionary))
    with pytest.raises(
        PlanningFeatureCodeError, match="dictionary|pair|code|family|URL|profile|order"
    ):
        module.validate_planning_feature_code_result_envelope(changed)


def test_schema_v5_scalar_lineage_contracts_are_intrinsic() -> None:
    module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
    result = _schema_v5_envelope_result()
    changed_standard = _result_with_hashes(
        replace(result, standard_model="CNIG PLU v2099")
    )
    malformed_sha = _result_with_hashes(
        replace(result, planning_document_context_sha256="not-a-sha")
    )
    for changed in (changed_standard, malformed_sha):
        with pytest.raises(PlanningFeatureCodeError, match="standard|SHA|sha|lineage"):
            module.validate_planning_feature_code_result_envelope(changed)


def test_schema_v5_official_rows_and_relation_feature_agreement_are_intrinsic() -> None:
    module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
    result = _schema_v5_envelope_result()
    surface = result.surface_features.copy(deep=True)
    surface.loc[surface.index[0], "official_code_label"] = pd.NA
    missing_meaning = _result_with_hashes(replace(result, surface_features=surface))

    surface = result.surface_features.copy(deep=True)
    surface.loc[surface.index[0], "official_code_status"] = "UNKNOWN_CODE_PAIR"
    invented_unknown = _result_with_hashes(replace(result, surface_features=surface))

    relations = result.relations.copy(deep=True)
    relations.loc[relations.index[0], "official_code_label"] = "Other official meaning"
    mismatched_relation = _result_with_hashes(replace(result, relations=relations))

    for changed in (missing_meaning, invented_unknown, mismatched_relation):
        with pytest.raises(
            PlanningFeatureCodeError,
            match="official|meaning|UNKNOWN|relation|feature",
        ):
            module.validate_planning_feature_code_result_envelope(changed)


def test_schema_v5_envelope_requires_exact_result_type_and_accepts_valid_result() -> (
    None
):
    module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
    result = _schema_v5_envelope_result()

    class DerivedPlanningFeatureCodeResult(PlanningFeatureCodeResult):
        pass

    derived = DerivedPlanningFeatureCodeResult(**result.__dict__)
    with pytest.raises(PlanningFeatureCodeError, match="type|result"):
        module.validate_planning_feature_code_result_envelope(derived)
    module.validate_planning_feature_code_result_envelope(result)
```
