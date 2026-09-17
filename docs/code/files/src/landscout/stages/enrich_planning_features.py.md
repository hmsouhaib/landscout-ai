# `src/landscout/stages/enrich_planning_features.py`

## File identity

- Repository path: `src/landscout/stages/enrich_planning_features.py`
- Source SHA256: `01a56b482a3c956d1f8a7069b94c69518758ea3937c3d98ef8ae5d74615d6148`
- Source SHA256 basis: `git-content`
- Binding convention: `SHA256_OF_EXACT_GIT_CONTENT_BYTES`; the complete UTF-8 snapshot below matches those bytes, not an EOL-normalized surrogate.
- R3 review: 84 existing class/field/function records checked against unchanged source; documentation fidelity only, independent review pending. A-003 remains OPEN.
- Navigation: [source](../../../../../../src/landscout/stages/enrich_planning_features.py), [test companion](../../../tests/unit/test_enrich_planning_features.py.md), [technical index](../../../../README.md), [R3 receipt](../../../../audit/R3_PLANNING_FEATURES.md).

## Purpose and two distinct public paths

This is factual GPU prescription/information normalization and full-parcel overlay.
It is not zoning normalization, CNIG meaning resolution, a BESS policy, a score,
a legal authorization or an acquisition API. Public names are exactly
`ParcelPlanningFeaturesResult`, `PlanningFeatureInputValidation`,
`PlanningFeaturesError`, `intersect_parcels_with_gpu_planning_features` and
`validate_normalized_planning_feature_inputs`; [stages](__init__.py.md) reexports all five.

The builder validates parcels, revalidates physical related GPU sources, normalizes
three catalogs, projects a private parcel copy, intersects and summarizes, then
checks its result with `source_inputs_already_rebuilt=True`. That private flag
skips the independent catalog/relation validator; it does not skip physical source
revalidation. The public normalized-input validator separately rebuilds physical
catalogs, checks supplied intrinsic schemas/identities, compares rebuilt catalogs,
reconstructs complete relations and, when present, all parcel output summaries.
It returns scalar integrity evidence, not repaired frames.

The five-frame result is a frozen dataclass envelope, not deeply immutable data.
Every field is required and direct dataclass construction performs no validation.
Caller-held DataFrames can change afterward; consumers must revalidate them.
The source configuration's immutable Pydantic models do not make these frames immutable.

## Ownership and dependency boundary actually checked

| Owner | Responsibility used here |
|---|---|
| [common planning-feature schema](../common/planning_feature_schema.py.md) | Exact ordered columns/dtypes, data-dependent all-null optional types and canonical index/geometry/CRS checks. Imported constants are owned there, not new policy here. |
| [common planning-feature contract](../common/planning_feature_contract.py.md) | Intrinsic relation kind, null, non-negative/positive metric, percentage and point-member coherence. Cannot prove source identity or missing geometric relations. |
| [common planning overlay](../common/planning_overlay.py.md) | `technical_overlay_tolerance`: `max(1e-6, reference * 1e-12)`. Numerical allowance, not a buffer/business threshold. |
| [common frame integrity](../common/frame_integrity.py.md) | Ordered frame columns/dtypes and index class/names/dtypes; GeoDataFrame active-geometry and CRS metadata in schema signatures. |
| [GPU source](../sources/gpu_fr.py.md) | Document/config/extraction and physical source revalidation; GpuPlanningDocument, GpuInspectedLayer, GpuValidatedSpatialLayerSource and GpuSpatialInspectionError are dependency-owned. |
| [CNIG resolver](resolve_planning_feature_codes.py.md) | Its `_build_result` calls the public validator first and copies both source/expected-relation digests into its own result; `resolve_planning_feature_codes` is the downstream public caller. It is not implemented or audited in full here. |

Relevant actual definitions/ranges read are recorded in the R3 receipt. The
resolver test helper `_integration_inputs` also calls this builder and passes
its returned catalog/relation fields onward; its suite was not executed by R3.

GeoPandas owns GeoDataFrame, reprojection and spatial join; pandas/NumPy own
tabular copies, dtype construction, positional arrays and reductions. PyProj
parses/compares CRS. Shapely owns force_2d, coordinate dimension, parts,
contains/covers, intersection/union and planar area/length. These imports are
local calculations, not network clients. Standard-library dataclasses/NamedTuple
supply envelopes, Integral/Real/isfinite supply strict numeric guards, date types
supply ISO serialization and json/hashlib supply deterministic integrity hashes.

### What physical revalidation means here

`_normalized_catalogs` makes one batch call for selected related roles in
LAYER_SPECS order. GPU reconstructs/revalidates the source config and hash,
checks document identity, rehashes extraction files against schema-2 manifest
and supplied inventory, rediscovers physical layers and verifies configured
logical-role completeness. Even absent related layers retain those document checks.

For each selected related dataset, GPU verifies extraction containment and
link/junction constraints, GPKG layer identity/no journal sidecars or exact
Shapefile family/core members. It verifies sizes/hashes, reads the actual path
with Pyogrio `fid_as_index=True`, requires unique non-negative Integral-not-bool
FIDs, compares ordered attributes/dtypes/attrs/WKB/CRS and inspected summary,
then verifies physical family/sizes/hashes again. Source data returned by this
fresh read replace the loaded frame for normalization.

This is path-based before/read/after verification, not an immutable byte snapshot.
The archive ZIP is not freshly downloaded or opened in these stage paths; its SHA
is retained lineage. Zoning's reference and extraction files are checked, but
zoning is not among the related layers selected for geometric rereading here.
The module writes no files and performs no HTTP. Public wrappers do delegate
filesystem reads and hashing; “no direct open()” is not “no filesystem effect”.

## Meaningful constants and ordered contracts

`CALCULATION_CRS = "EPSG:2154"` is canonical catalog storage and planar measurement
CRS. Original parcel CRS/WKB remain unchanged. Input source CRS is retained as
`source_crs` text from the inspected summary, distinct from normalized geometry CRS.
`PARCEL_REQUIRED_COLUMNS` requires parcel_id and geometry. `SURFACE_TYPES`,
`LINE_TYPES`, `POINT_TYPES` and `_CATALOG_GEOMETRY_TYPES` define these exact families:

| LAYER_SPECS order | Family / kind | CNIG ID / type / subtype | Shapely types |
|---|---|---|---|
| prescription_surface | PRESCRIPTION / SURFACE | LIB_IDPSC / TYPEPSC / STYPEPSC | Polygon, MultiPolygon |
| prescription_line | PRESCRIPTION / LINE | LIB_IDPSC / TYPEPSC / STYPEPSC | LineString, MultiLineString |
| prescription_point | PRESCRIPTION / POINT | LIB_IDPSC / TYPEPSC / STYPEPSC | Point, MultiPoint |
| information_surface | INFORMATION / SURFACE | LIB_IDINFO / TYPEINF / STYPEINF | Polygon, MultiPolygon |
| information_line | INFORMATION / LINE | LIB_IDINFO / TYPEINF / STYPEINF | LineString, MultiLineString |
| information_point | INFORMATION / POINT | LIB_IDINFO / TYPEINF / STYPEINF | Point, MultiPoint |

`FeatureFamily`, `GeometryKind` and `SourceIdentityKind` are Literal annotations,
not standalone runtime validators. `SOURCE_IDENTITY_KINDS` is the two-value
CNIG_ATTRIBUTE/ARCHIVE_SCOPED_OGR_FID validation set. Only an absent
prescription-surface identity column permits FID fallback, never a present bad ID.
Planning IDs are `GPU:{document_id}:{logical_layer}:{source_feature_id}`.
The source ID can repeat in different logical roles, not within one role.

`COMMON_SOURCE_FIELDS` maps LIBELLE→label_raw, TXT→text_raw,
NOMFIC→regulation_filename_raw, URLFIC→regulation_url_raw,
IDURBA→source_document_reference_raw and DATVALID→source_validity_date_raw.
`OPTIONAL_SOURCE_FIELDS` declares the five names other than IDURBA but has no
runtime consumer in this module. Required raw codes and IDURBA must be non-null
non-empty unpadded strings; codes are not interpreted. IDURBA must equal archive
name after removing at most one terminal case-insensitive .zip.

`_CATALOG_REQUIRED_EXACT_STRING_COLUMNS` contains the 19 identity/code/document/
source fields listed in the exact declaration below. The six
`_CATALOG_OPTIONAL_EXACT_STRING_COLUMNS` are label_raw, text_raw,
regulation_filename_raw, regulation_url_raw, source_validity_date_raw and
source_standard_model. Optional values may be null; the supplied-catalog
validator nonetheless requires every non-null value to be unpadded non-empty
text. This latter restriction conflicts with raw preservation (A-003).

`LAYER_SPECS`, `COMMON_SOURCE_FIELDS` and `_CATALOG_GEOMETRY_TYPES` are ordinary
module dictionaries, not loaded trust-bearing immutable policy objects.
`PARCEL_OUTPUT_COLUMNS` and `PARCEL_COUNT_COLUMNS` are frozensets of membership
constraints; their set order is not a semantic output sort. The snapshot preserves
all exact declarations, including `__all__`.

## Frame schemas, units and nulls

A normalized catalog has 25 common columns, then geometry and one kind metric:

```text
planning_feature_id, source_feature_id, source_identity_kind, source_identity_field,
logical_layer, feature_family, geometry_kind, type_code_raw, subtype_code_raw,
label_raw, text_raw, regulation_filename_raw, regulation_url_raw,
source_document_reference_raw, source_validity_date_raw, source_provider,
source_portal, source_commune_code, source_document_id, source_document_type,
source_archive_name, source_archive_sha256, source_layer, source_standard_model,
source_crs, geometry, [feature_area_m2 | feature_length_m | point_member_count]
```

Geometry is valid, non-null, non-empty, kind-conforming XY EPSG:2154.
Area/length are full-feature positive finite float64 m2/m, not clipped metrics.
Point member count is positive int64. Other columns are str except
text_raw/regulation_filename_raw/regulation_url_raw: in a nonempty catalog each
is object iff entirely null, otherwise str. Empty base SURFACE uses str/str/object
for those three; LINE/POINT use object/object/object. Label/date/standard model
stay str even if null. Index is unnamed exact zero-based RangeIndex, int64.
Original source Z is dropped by force_2d; supplied canonical catalogs must have
coordinate dimension exactly 2. Original parcels are not subject to that same
2D guard: their stored geometry is preserved while calculations force XY.
No repair, snap, buffer, simplification or null-geometry exclusion is performed.

Relations are a plain DataFrame, with exact order:

```text
parcel_id, planning_feature_id, source_feature_id, source_identity_kind,
source_identity_field, logical_layer, feature_family, geometry_kind,
type_code_raw, subtype_code_raw, label_raw, text_raw, relation_type,
parcel_metric_area_m2, feature_area_m2, source_line_length_m,
intersection_area_m2, intersection_length_m, parcel_share_pct, feature_share_pct,
point_member_count, point_members_inside_count, point_members_boundary_count,
source_document_id, source_archive_sha256, source_layer,
source_validity_date_raw, regulation_filename_raw
```

The seven area/length/percentage fields are float64; three point counts are
nullable Int64; other fields are str. Whole parcel_metric_area_m2 is present
for all kinds. Irrelevant float/count metrics are NaN/NA, not zero. No relation
geometry, regulation URL, provider or full source context is added beyond this
schema. `_RELATION_CATALOG_FIELDS` names the 15 copied source facts checked
null-safely; full source area/length/member metric is checked separately.
Catalog line feature_length_m maps to relation source_line_length_m.

| Kind | Pair rule and emitted measurements |
|---|---|
| SURFACE | Inner intersects join on full polygons, then exact intersection. Area >0 means AREA_OVERLAP, otherwise TOUCH_ONLY. Shares are 100 × clipped area / whole parcel or full feature area. Private clipped geometries feed unions. |
| LINE | Same intersects join; clipped length >0 means LENGTH_OVERLAP, otherwise TOUCH_ONLY. Full source length is separate; no line union and no area share. |
| POINT | Each Point/MultiPoint part is tested against parcel: contains = inside, covers minus contains = boundary. Any inside means INSIDE, otherwise BOUNDARY_TOUCH. Full member count includes outside members; only intersecting features produce rows. |

Relations sort stably by original parcel position then planning_feature_id, not
parcel_id lexical order. Catalogs include source features without a relation.
Empty related kinds return canonical empty catalogs; no matches yield empty
relations and zero numeric parcel summaries, with document/SHA still present.
The helpers handle empty pair tables; this file's tests do not establish every
public zero-parcel case.

### The 21 appended parcel columns

Original parcel columns, index, order, CRS and WKB remain. Counts are int64;
floating summaries float64; document/SHA lineage are strings.

| Columns | Exact meaning |
|---|---|
| planning_surface_relation_count; planning_surface_area_overlap_count; planning_surface_touch_count | All surface pairs, positive-area pairs, zero-area touching pairs. |
| prescription_surface_relation_count; information_surface_relation_count | Surface relation rows per source family, including touches. |
| planning_line_relation_count; planning_line_length_overlap_count; planning_line_touch_count | All line pairs, positive clipped-length pairs, zero-length contacts. |
| planning_point_relation_count | Point feature/parcel pairs, not member count. |
| planning_point_inside_count; planning_point_boundary_count | Sum of inside/boundary source point members. |
| planning_surface_intersection_area_sum_m2 | Sum of positive clipped areas; overlapping features can double count. |
| planning_surface_covered_union_area_m2; planning_surface_covered_pct | Union of all positive clipped surfaces and 100 × union / full parcel area. |
| prescription_surface_covered_union_area_m2; prescription_surface_covered_pct | Separate prescription union and share. |
| information_surface_covered_union_area_m2; information_surface_covered_pct | Separate information union and share. Family unions may overlap each other. |
| planning_line_intersection_length_sum_m | Sum of clipped line lengths, not union length. |
| planning_feature_document_id; planning_feature_archive_sha256 | Document/declared archive lineage copied even when there are no related features. |

Union overshoot beyond tolerance raises; tiny overshoot clamps to parcel area.
Exact union==area yields exactly 100%. `_require_close` uses tolerance of the
larger absolute actual/expected value; summary percentage checks additionally
scale area tolerance by 100/parcel_area. Units follow the metric under comparison.

## Integrity serialization and error limits

Source evidence domain `landscout.planning_features.verified_gpu_sources.v1`
includes archive SHA and layers sorted by logical name. Each layer includes driver,
physical layer, relative dataset path, feature count, source CRS, ordered OGR FIDs
and files sorted by relative path with type/size/SHA/category. It excludes absolute
root paths; no Python repr or address enters it.

Expected relation domain `landscout.planning_features.expected_relations.v2`
includes deterministic frame schema signature, canonical ordered index values
and ordered row cells. Dates become ISO, numpy scalars recurse through item(),
missing scalars become JSON null, bool/int/finite real/string retain scalar
meaning; unsupported leaves fail. Canonical JSON is sorted-key compact UTF-8
with ensure_ascii=False and allow_nan=False. Returned digest hashes the expected
rebuild, not any near-equal supplied floats. No schema/hash change occurs in R3.

Specific schema/intrinsic TypeError/ValueError and physical GPU errors are
translated to PlanningFeaturesError at their owning helper boundaries. GIS
operations have local chained error guards. The public normalized-input wrapper
also catches unexpected Exception; the public builder does not have that
catch-all. A direct private helper call or bare result construction is not the
public trust contract.

## A-003: raw preservation and validator disagreement (OPEN)

Archived [synthetic physical reproduction](../../../../audit/RECOVERY_STATUS_2026-09-17.md#application-findings):
LIBELLE = `" Label "` in a real local synthetic GPKG is copied by
_optional_values/_normalize_layer to label_raw unchanged. The builder's optimized
_validate_result path does not invoke _validate_catalog_identity. The public
validator first physically rebuilds expected catalogs, then validates the supplied
catalog; _validate_optional_exact_strings calls _strict_string and raises
`Feature catalog label raw must be a non-empty exact string` before catalog
equality/relation reconstruction/hash return. It is not a failure before all
physical revalidation.

Preserving raw text remains the intended contract. R3 does not strip it, endorse
the stricter rule, repair production or add a regression. The archived reproduction
uses a fabricated archive envelope and synthetic local files, not official GPU
acquisition or evidence of official-data prevalence. A-001/A-002/A-003 stay open.

## Compact synthetic call/data-flow example

Assume `planning_document: GpuPlanningDocument` has already been assembled with
valid local physical-source evidence, and `parcels: gpd.GeoDataFrame` contains
one 100 m2 XY2154 polygon P-1. Suppose one prescription surface PSC-1 exactly
matches it, with clean label `"Label 0"`, valid raw codes and matching IDURBA.
This describes a synthetic example, not a way to bypass source construction.

```python
result = intersect_parcels_with_gpu_planning_features(parcels, planning_document)
# result.parcels: original geometry + count 1, union 100 m2, covered 100%
# result.surface_features: full PSC-1 geometry, feature_area_m2 100
# result.line_features / result.point_features: canonical empty catalogs
# result.relations: one AREA_OVERLAP row, intersection_area_m2 100
evidence = validate_normalized_planning_feature_inputs(
    planning_document,
    parcels,
    result.surface_features,
    result.line_features,
    result.point_features,
    result.relations,
)
# evidence.expected_relation_count == 1; two source/rebuild hashes + layer/file counts
```

The actual builder and validator signatures are reproduced per symbol below.
Replacing the example label with `" Label "` changes the outcome to A-003:
builder returns raw text, second call raises. Success on clean fixture values
is not proof that every builder output satisfies the separate validator.

## Symbol-by-symbol review

Every heading below binds the qualified owner
`landscout.stages.enrich_planning_features` plus the displayed name, exact
signature/defaults/annotation and source line range. Methods nested in a function
retain that qualified owner. Record fields have no defaults. Notes state concrete
behavior; test links are related evidence with the limits explained in the test
companion, not assertions of exhaustive/direct coverage. An empty test-reference
list is explicitly a missing dedicated regression, not an application defect.

<a id="r3-layerspec"></a>

### `_LayerSpec`

class; source lines 79–86. Signature SHA256: `c6c4259139fb7b0be8775ab83f74a11983f956b19f251eaf828d5bd3b009e136`.

```python
class _LayerSpec(NamedTuple):
```

Immutable seven-item NamedTuple selected from LAYER_SPECS, not a validated source object. Every argument is required. _normalize_layer consumes its CNIG fields/geometry family; _validate_catalog_identity checks their resulting identity. It neither reads files nor validates values on construction.

Related evidence (limits in linked test explanation): [test_surface_full_overlap_normalizes_raw_values_and_lineage](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-surface-full-overlap-normalizes-raw-values-and-lineage), [test_wrong_geometry_kind_is_rejected](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-wrong-geometry-kind-is-rejected).

<a id="r3-layerspec-logical-layer"></a>

### `_LayerSpec.logical_layer`

field; source lines 80–80. Signature SHA256: `cb3ad333bab898721e9e7bd2fbf01868676bccf860cf3a64946c849ab0d3de4f`.

```python
logical_layer: str
```

Configured logical role (one of the six LAYER_SPECS keys), not the physical dataset/layer name. Used in deterministic feature IDs and ordering.

Related evidence (limits in linked test explanation): [test_same_source_id_is_allowed_in_distinct_logical_layers](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-same-source-id-is-allowed-in-distinct-logical-layers).

<a id="r3-layerspec-feature-family"></a>

### `_LayerSpec.feature_family`

field; source lines 81–81. Signature SHA256: `d57d5bf4caaa3ba564b0ce20c0947ea07ae2b0346a426f298a9b1c4adbd5f894`.

```python
feature_family: FeatureFamily
```

PRESCRIPTION or INFORMATION; distinguishes the two source families and family-specific surface summaries without interpreting the raw CNIG code.

Related evidence (limits in linked test explanation): [test_overlapping_surface_union_is_not_double_counted](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-overlapping-surface-union-is-not-double-counted).

<a id="r3-layerspec-geometry-kind"></a>

### `_LayerSpec.geometry_kind`

field; source lines 82–82. Signature SHA256: `b965b9a4cf30b971f9ef741ddfbf250bf2337fd78e52b1e286896dcd933d75b2`.

```python
geometry_kind: GeometryKind
```

SURFACE, LINE or POINT chooses normalization metrics, accepted Shapely types and the relation algorithm. Literal annotations alone are not runtime validation.

Related evidence (limits in linked test explanation): [test_wrong_geometry_kind_is_rejected](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-wrong-geometry-kind-is-rejected).

<a id="r3-layerspec-identity-field"></a>

### `_LayerSpec.identity_field`

field; source lines 83–83. Signature SHA256: `f8175f2de29e251967dad741dfbf41e55101427da338f050269b02703385fb27`.

```python
identity_field: str
```

LIB_IDPSC for prescriptions; LIB_IDINFO for information. Only a missing prescription-surface field permits archive-scoped OGR_FID fallback; present bad values are errors.

Related evidence (limits in linked test explanation): [test_prescription_surface_uses_validated_source_ogr_fid_when_cnig_id_absent](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-prescription-surface-uses-validated-source-ogr-fid-when-cnig-id-absent), [test_missing_required_source_fields_fail](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-missing-required-source-fields-fail).

<a id="r3-layerspec-type-field"></a>

### `_LayerSpec.type_field`

field; source lines 84–84. Signature SHA256: `ab3907405b78854bf1af7af375596b32bd22b15f911936e29b27b80964b01031`.

```python
type_field: str
```

Required raw TYPEPSC or TYPEINF string column. Values remain exact source strings, not decoded meanings.

Related evidence (limits in linked test explanation): [test_surface_full_overlap_normalizes_raw_values_and_lineage](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-surface-full-overlap-normalizes-raw-values-and-lineage).

<a id="r3-layerspec-subtype-field"></a>

### `_LayerSpec.subtype_field`

field; source lines 85–85. Signature SHA256: `62688bc9fe72c68481cb9a09dbd75240e291cd5d3d00129f7a5690e8a72e430e`.

```python
subtype_field: str
```

Required raw STYPEPSC or STYPEINF string column; no numeric coercion or meaning lookup. Leading zeros such as 04 survive.

Related evidence (limits in linked test explanation): [test_surface_full_overlap_normalizes_raw_values_and_lineage](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-surface-full-overlap-normalizes-raw-values-and-lineage).

<a id="r3-layerspec-allowed-geometry-types"></a>

### `_LayerSpec.allowed_geometry_types`

field; source lines 86–86. Signature SHA256: `d0f926c294105d8bc3b0f886772fe8ad621bbc90a9b33d87671d948e1251d2c4`.

```python
allowed_geometry_types: frozenset[str]
```

frozenset of Polygon/MultiPolygon, LineString/MultiLineString or Point/MultiPoint as selected by kind; consumed by _validate_geometries, not a geometry-repair policy.

Related evidence (limits in linked test explanation): [test_polygon_and_multipolygon_surfaces](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-polygon-and-multipolygon-surfaces), [test_linestring_and_multilinestring](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-linestring-and-multilinestring), [test_wrong_geometry_kind_is_rejected](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-wrong-geometry-kind-is-rejected).

<a id="r3-planningfeatureserror"></a>

### `PlanningFeaturesError`

class; source lines 242–243. Signature SHA256: `ecad671780eb7f1ed69369729809e0324c0436c1e07a5aa0f9645aaad67934e5`.

```python
class PlanningFeaturesError(ValueError):
```

Public ValueError subclass for planning factual-contract failures. It adds no methods or fields. Specific GIS/schema/source boundaries translate errors with causes; only the public normalized-input validator supplies a catch-all Exception wrapper. The builder has no universal wrapper.

Related evidence (limits in linked test explanation): [test_geospatial_operation_failure_is_controlled_and_chained](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-geospatial-operation-failure-is-controlled-and-chained), [test_public_normalized_input_contract_wraps_malformed_document_context](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-public-normalized-input-contract-wraps-malformed-document-context).

<a id="r3-parcelplanningfeaturesresult"></a>

### `ParcelPlanningFeaturesResult`

class; source lines 247–254. Signature SHA256: `bd81d79b2e9f91eeaea2d4582969814c7d6b1fe07d85789300763431d45fd347`.

```python
class ParcelPlanningFeaturesResult:
```

Frozen dataclass with five required frame fields and no constructor validation. Attribute reassignment fails, but contained pandas/GeoPandas frames remain mutable. The builder constructs independent output frames; this envelope alone proves neither physical provenance nor deep immutability.

Related evidence (limits in linked test explanation): [test_result_is_frozen](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-result-is-frozen), [test_inputs_and_all_existing_parcel_fields_are_preserved](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-inputs-and-all-existing-parcel-fields-are-preserved), [test_result_frames_are_independent_from_mutable_inputs](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-result-frames-are-independent-from-mutable-inputs).

<a id="r3-parcelplanningfeaturesresult-parcels"></a>

### `ParcelPlanningFeaturesResult.parcels`

field; source lines 250–250. Signature SHA256: `3ba865416777c701681539c5022c23763600601dd993d74f273c69c3553e329a`.

```python
parcels: gpd.GeoDataFrame
```

Original parcel rows, order, index, CRS, WKB and existing columns copied, with 21 factual summary/lineage columns appended. Geometry is not replaced by the metric projection. DataFrame deep copy is not a recursive freeze of arbitrary object-valued cells.

Related evidence (limits in linked test explanation): [test_inputs_and_all_existing_parcel_fields_are_preserved](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-inputs-and-all-existing-parcel-fields-are-preserved), [test_epsg4326_parcels_are_measured_in_lambert93_but_preserved](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-epsg4326-parcels-are-measured-in-lambert93-but-preserved).

<a id="r3-parcelplanningfeaturesresult-surface-features"></a>

### `ParcelPlanningFeaturesResult.surface_features`

field; source lines 251–251. Signature SHA256: `98b1bf6020fb918d730d9ef04bcadc3b81c34ac142a757e8bf92742fd7253196`.

```python
surface_features: gpd.GeoDataFrame
```

Complete normalized PRESCRIPTION/INFORMATION surface catalog, including features with no parcel relation; XY EPSG:2154, 27 columns, full feature_area_m2. Not parcel-clipped geometry.

Related evidence (limits in linked test explanation): [test_surface_partial_and_touch_relations](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-surface-partial-and-touch-relations), [test_overlapping_surface_union_is_not_double_counted](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-overlapping-surface-union-is-not-double-counted).

<a id="r3-parcelplanningfeaturesresult-line-features"></a>

### `ParcelPlanningFeaturesResult.line_features`

field; source lines 252–252. Signature SHA256: `0d3690554c2195254ddcd7c1d1efde2e7c8b991352d319ee8d012da6cb521776`.

```python
line_features: gpd.GeoDataFrame
```

Complete normalized XY EPSG:2154 line catalog with full feature_length_m; relation intersection_length_m is a separate clipped measurement.

Related evidence (limits in linked test explanation): [test_line_crossing_and_partly_inside](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-line-crossing-and-partly-inside).

<a id="r3-parcelplanningfeaturesresult-point-features"></a>

### `ParcelPlanningFeaturesResult.point_features`

field; source lines 253–253. Signature SHA256: `8ddf4b6fefb5c18c8f5df075b7b8795f7c60e3e0b7d356cfb0db126285beb5e9`.

```python
point_features: gpd.GeoDataFrame
```

Complete normalized XY EPSG:2154 point catalog; point_member_count counts all parts of each Point/MultiPoint, including parts outside a given parcel.

Related evidence (limits in linked test explanation): [test_points_inside_boundary_outside_and_multipoint](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-points-inside-boundary-outside-and-multipoint).

<a id="r3-parcelplanningfeaturesresult-relations"></a>

### `ParcelPlanningFeaturesResult.relations`

field; source lines 254–254. Signature SHA256: `58fbae92e1f38605ac945bcdf5d1fb239d8601781a10d4f4e3e9549540ffad7f`.

```python
relations: pd.DataFrame
```

Plain 28-column DataFrame without geometry, canonical RangeIndex, one row per intersecting parcel/feature pair. Stable parcel input position then planning_feature_id order; no non-intersecting pairs.

Related evidence (limits in linked test explanation): [test_relations_are_unique_deterministic_and_summaries_agree](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-relations-are-unique-deterministic-and-summaries-agree).

<a id="r3-planningfeatureinputvalidation"></a>

### `PlanningFeatureInputValidation`

class; source lines 258–265. Signature SHA256: `a73340f41fc4f35ee2b7c6aef979fcc8a36afeb49a8cde07718f16b1d2309c67`.

```python
class PlanningFeatureInputValidation:
```

Frozen scalar evidence record returned only after the public validator reconstructs sources, catalogs and expected relations. Five required fields, no constructor validator: manually instantiating this dataclass does not confer source authority.

Related evidence (limits in linked test explanation): [test_public_normalized_input_contract_validates_step_7d_3_1_result](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-public-normalized-input-contract-validates-step-7d-3-1-result), [test_public_source_validation_hashes_survive_parquet_readback](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-public-source-validation-hashes-survive-parquet-readback).

<a id="r3-planningfeatureinputvalidation-gpu-related-source-files-sha256"></a>

### `PlanningFeatureInputValidation.gpu_related_source_files_sha256`

field; source lines 261–261. Signature SHA256: `b8ee395981fbc67c786d21d46b08cc6377528acc43cbc69f112b401a78b77ec9`.

```python
gpu_related_source_files_sha256: str
```

Hex SHA256 of verified related-layer evidence under verified_gpu_sources.v1: archive SHA, logical/physical identifiers, relative files and ordered FIDs. Absolute cache-root paths are excluded. Not a fresh hash of the archive ZIP bytes.

Related evidence (limits in linked test explanation): [test_public_source_validation_hashes_survive_parquet_readback](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-public-source-validation-hashes-survive-parquet-readback).

<a id="r3-planningfeatureinputvalidation-expected-relations-content-sha256"></a>

### `PlanningFeatureInputValidation.expected_relations_content_sha256`

field; source lines 262–262. Signature SHA256: `872594b40015b5719782af04d1bc1a7ee28c448c1ec1d97bb1b72ade431a656b`.

```python
expected_relations_content_sha256: str
```

Hex SHA256 of reconstructed expected relations under expected_relations.v2, including frame schema/index metadata and canonical ordered index/row values. It hashes the rebuild, not tolerance-accepted caller floats.

Related evidence (limits in linked test explanation): [test_expected_relation_hash_binds_dtype_and_index_metadata](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-expected-relation-hash-binds-dtype-and-index-metadata), [test_public_source_validation_hashes_survive_parquet_readback](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-public-source-validation-hashes-survive-parquet-readback).

<a id="r3-planningfeatureinputvalidation-related-source-layer-count"></a>

### `PlanningFeatureInputValidation.related_source_layer_count`

field; source lines 263–263. Signature SHA256: `6db4c19fb9b43ae9b3e09d0b0133bf74cc8556e03e7b3772671079359f8dd5a5`.

```python
related_source_layer_count: int
```

Number of revalidated selected related logical layers; zoning is not counted. Zero is possible when all related roles are absent. The dataclass itself does not enforce non-negative integers.

Related evidence (limits in linked test explanation): [test_public_normalized_input_contract_validates_step_7d_3_1_result](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-public-normalized-input-contract-validates-step-7d-3-1-result).

<a id="r3-planningfeatureinputvalidation-related-source-file-count"></a>

### `PlanningFeatureInputValidation.related_source_file_count`

field; source lines 264–264. Signature SHA256: `18ddb08494d0ef1102da5a252fe61722475cc615c5ba233d55d647a81e2ad9f4`.

```python
related_source_file_count: int
```

Count of distinct relative file paths across validated related sources; several Shapefile sidecars contribute, a shared GPKG path contributes once. The three-GPKG fixture asserts 3; there is no direct shared-container count regression here.

Related evidence (limits in linked test explanation): [test_public_normalized_input_contract_validates_step_7d_3_1_result](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-public-normalized-input-contract-validates-step-7d-3-1-result).

<a id="r3-planningfeatureinputvalidation-expected-relation-count"></a>

### `PlanningFeatureInputValidation.expected_relation_count`

field; source lines 265–265. Signature SHA256: `7bf7b134945bf0b0d3db06672d6ff93fbe7c6e1c81bb856e4027095aeef441a4`.

```python
expected_relation_count: int
```

Length of the independently rebuilt complete relation table, not simply the supplied row count. Returned after comparison.

Related evidence (limits in linked test explanation): [test_public_normalized_input_contract_validates_step_7d_3_1_result](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-public-normalized-input-contract-validates-step-7d-3-1-result), [test_source_complete_contract_rejects_extra_geometrically_false_relation](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-source-complete-contract-rejects-extra-geometrically-false-relation).

<a id="r3-planningcontext"></a>

### `_PlanningContext`

class; source lines 269–277. Signature SHA256: `5d83e29530e3f1094b6dade2fa7eaa3074ad3dab316456572a9471b1675ce272`.

```python
class _PlanningContext:
```

Private frozen dataclass of eight lineage scalars, all required at construction (standard_model permits None). _planning_context builds it from the supplied document; this local context check is not physical source revalidation.

Related evidence (limits in linked test explanation): [test_source_complete_contract_binds_gpu_document_context](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-source-complete-contract-binds-gpu-document-context).

<a id="r3-planningcontext-provider"></a>

### `_PlanningContext.provider`

field; source lines 270–270. Signature SHA256: `4667aee004a3c25155cc86e608930c2e6c99291a6b4d6dc408ea8da773d7237f`.

```python
provider: str
```

Archive-document provider, locally checked as exact non-empty string and copied to source_provider. Official configured identity is checked later by the GPU dependency.

Related evidence (limits in linked test explanation): [test_source_complete_contract_binds_gpu_document_context](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-source-complete-contract-binds-gpu-document-context).

<a id="r3-planningcontext-portal"></a>

### `_PlanningContext.portal`

field; source lines 271–271. Signature SHA256: `ce03170a7ff2cc0e4f952194e74d3213e46a372bba19714a466b354101e22163`.

```python
portal: str
```

Archive-document portal string copied to source_portal. This field does not trigger HTTP; GPU config/metadata revalidation owns source identity.

Related evidence (limits in linked test explanation): [test_source_complete_contract_binds_gpu_document_context](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-source-complete-contract-binds-gpu-document-context).

<a id="r3-planningcontext-commune-code"></a>

### `_PlanningContext.commune_code`

field; source lines 272–272. Signature SHA256: `9f1cccf4242aa43aea2cfed72fab73e8bcd3eefccff2de9b0b93913fd36480ca`.

```python
commune_code: str
```

Archive-document commune string copied to source_commune_code. Local exact-string validation is weaker than the upstream commune/config binding.

Related evidence (limits in linked test explanation): [test_source_complete_contract_binds_gpu_document_context](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-source-complete-contract-binds-gpu-document-context).

<a id="r3-planningcontext-document-id"></a>

### `_PlanningContext.document_id`

field; source lines 273–273. Signature SHA256: `91d7a6f0e3572072c6933a8641dc696623d6d3238c3b814bc43b3385d06bb66c`.

```python
document_id: str
```

Archive-document identifier used in planning_feature_id and parcel/relation lineage. It is not itself a source-file digest.

Related evidence (limits in linked test explanation): [test_surface_full_overlap_normalizes_raw_values_and_lineage](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-surface-full-overlap-normalizes-raw-values-and-lineage).

<a id="r3-planningcontext-document-type"></a>

### `_PlanningContext.document_type`

field; source lines 274–274. Signature SHA256: `baa770619480902bf35d5296c2c46c71b51eb4aa2518bb6261446731180ef92c`.

```python
document_type: str
```

Archive-document type copied to source_document_type. The local helper does not interpret PLU/CC semantics; physical/config comparison is separate.

Related evidence (limits in linked test explanation): [test_source_complete_contract_binds_gpu_document_context](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-source-complete-contract-binds-gpu-document-context).

<a id="r3-planningcontext-archive-name"></a>

### `_PlanningContext.archive_name`

field; source lines 275–275. Signature SHA256: `5439b291f5af885f975dc95e157d1b6074dca48360f8c844d9808f4df2951afd`.

```python
archive_name: str
```

Exact archive-document name used for source_archive_name and IDURBA comparison, with at most one case-insensitive terminal .zip removed for that comparison only. Local _strict_string is not a portable-filename validator.

Related evidence (limits in linked test explanation): [test_source_document_reference_allows_one_archive_zip_suffix](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-source-document-reference-allows-one-archive-zip-suffix), [test_idurba_mismatch_is_rejected](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-idurba-mismatch-is-rejected).

<a id="r3-planningcontext-archive-sha256"></a>

### `_PlanningContext.archive_sha256`

field; source lines 276–276. Signature SHA256: `0e7464db3547b287b4da67097f9d7cffe8345e9e344cb22bb54a487ee2e282cc`.

```python
archive_sha256: str
```

64-character hexadecimal archive SHA as supplied by the archive envelope. Case is not normalized here. Copied to catalogs, relations, parcel lineage and integrity payload; this helper does not read the ZIP.

Related evidence (limits in linked test explanation): [test_surface_full_overlap_normalizes_raw_values_and_lineage](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-surface-full-overlap-normalizes-raw-values-and-lineage), [test_source_complete_contract_rejects_independent_gpu_lineage_mutation](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-source-complete-contract-rejects-independent-gpu-lineage-mutation).

<a id="r3-planningcontext-standard-model"></a>

### `_PlanningContext.standard_model`

field; source lines 277–277. Signature SHA256: `513a661807ee7b98035ef16597a56afbad704a827298380f2f1a8ed17ae3e719`.

```python
standard_model: str | None
```

Optional sole standard model after strict validation and ordered deduplication of archive singular standard_model and extraction.standard_models. None if absent; disagreement raises. Copied to source_standard_model. No isolated ambiguity regression in this file.

Dedicated regression in this test file: none; reviewed against implementation and callers, not promoted to executable proof.

<a id="r3-strict-string"></a>

### `_strict_string`

function; source lines 280–283. Signature SHA256: `d17a85b13a52009c058a875ca8f3e4130e23961af7c1593d298a227eb795fc3a`.

```python
def _strict_string(value: object, label: str) -> str:
```

Returns the same isinstance(str) value only when non-empty and equal to strip(); otherwise PlanningFeaturesError names the label. Never strips, coerces numbers or opens a path. Used by identity/context guards.

Related evidence (limits in linked test explanation): [test_invalid_parcel_ids_are_rejected](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-invalid-parcel-ids-are-rejected).

<a id="r3-strict-nonnegative-integer"></a>

### `_strict_nonnegative_integer`

function; source lines 286–291. Signature SHA256: `d21c292bca764a08354dd86ed2f4faedd810d78acad42f0a3b7f4784a7ae3284`.

```python
def _strict_nonnegative_integer(value: object, label: str) -> int:
```

Rejects bool and non-Integral values, rejects negatives, then returns built-in int. Used for inspected-summary and integer metric/count validation; physical OGR FID type validation is owned by the GPU dependency, not this helper.

Related evidence (limits in linked test explanation): [test_strict_parcel_summary_integer_counts_are_enforced](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-strict-parcel-summary-integer-counts-are-enforced).

<a id="r3-validate-ids"></a>

### `_validate_ids`

function; source lines 294–297. Signature SHA256: `59f767a75604e6c526e51b8575dfc8609c858bf9d2b2863aa7aa6eff2cdc31c5`.

```python
def _validate_ids(values: pd.Series, label: str) -> None:
```

First calls _validate_exact_strings (including null/text checks), then rejects duplicate values. Used for parcel IDs, source IDs and normalized planning IDs; returns None without generating or modifying identifiers.

Related evidence (limits in linked test explanation): [test_duplicate_parcel_ids_are_rejected](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-duplicate-parcel-ids-are-rejected), [test_duplicate_source_ids_are_rejected](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-duplicate-source-ids-are-rejected), [test_invalid_parcel_ids_are_rejected](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-invalid-parcel-ids-are-rejected).

<a id="r3-validate-exact-strings"></a>

### `_validate_exact_strings`

function; source lines 300–304. Signature SHA256: `6fb14cfc7544f1f144e8d129946d259750607d4300d765aab1519ad737d4ba7c`.

```python
def _validate_exact_strings(values: pd.Series, label: str) -> None:
```

Rejects any null and then applies _strict_string to each value, returning None. Required raw codes and lineage cannot be missing or padded; repeated codes are allowed.

Related evidence (limits in linked test explanation): [test_missing_required_source_fields_fail](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-missing-required-source-fields-fail), [test_surface_full_overlap_normalizes_raw_values_and_lineage](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-surface-full-overlap-normalizes-raw-values-and-lineage).

<a id="r3-validate-optional-exact-strings"></a>

### `_validate_optional_exact_strings`

function; source lines 307–311. Signature SHA256: `3b880dbd208288bc1a92981293fc2f11b276797964a3132916051a11dd6700fa`.

```python
def _validate_optional_exact_strings(values: pd.Series, label: str) -> None:
```

Iterates the values, skips scalar pd.isna values and calls _strict_string otherwise; no actual column trimming or copying. Creates A-003 for padded optional raw labels preserved by builder. Archived synthetic reproduction, no permanent padded-label regression in this test file.

Dedicated regression in this test file: none; reviewed against implementation and callers, not promoted to executable proof.

<a id="r3-crs"></a>

### `_crs`

function; source lines 314–320. Signature SHA256: `986d6beb9e05ea7f098621f8a648267d64fe13e516e5246974db0f1d886f240c`.

```python
def _crs(value: object, label: str) -> CRS:
```

Requires a present CRS and parses it through pyproj.CRS.from_user_input, translating parse Exception to PlanningFeaturesError with cause. Returns a CRS object; arbitrary readable source/parcel CRS is accepted here, not necessarily EPSG:2154.

Related evidence (limits in linked test explanation): [test_missing_crs_is_rejected](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-missing-crs-is-rejected), [test_unusable_source_crs_is_rejected](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-unusable-source-crs-is-rejected).

<a id="r3-active-geometry"></a>

### `_active_geometry`

function; source lines 323–331. Signature SHA256: `3bb89325512bae5e2675476c164d19af32c89f30e86193109e61323564170b84`.

```python
def _active_geometry(frame: gpd.GeoDataFrame, label: str) -> None:
```

Returns None after requiring literal geometry column and active_geometry_name == 'geometry'. Translates AttributeError from active-name access to PlanningFeaturesError. Does not return a GeoSeries, copy or modify geometry; no direct adversarial active-column regression in this file.

Dedicated regression in this test file: none; reviewed against implementation and callers, not promoted to executable proof.

<a id="r3-validate-geometries"></a>

### `_validate_geometries`

function; source lines 334–351. Signature SHA256: `f83e3779f88fc6d22bc2d8eb2385c3170d8c7f83683e0ae913075ca3978aec87`.

```python
def _validate_geometries(
    frame: gpd.GeoDataFrame,
    allowed: frozenset[str],
    label: str,
) -> None:
```

Reads frame.geometry, rejects null, empty, invalid and wrong-family members in that order; returns None. Active-column checks are performed by callers, not this helper. Empty series pass the universal checks. No repair, buffering or row dropping.

Related evidence (limits in linked test explanation): [test_wrong_geometry_kind_is_rejected](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-wrong-geometry-kind-is-rejected), [test_invalid_surface_geometry_is_rejected_without_repair](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-invalid-surface-geometry-is-rejected-without-repair), [test_null_or_empty_source_geometry_is_rejected](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-null-or-empty-source-geometry-is-rejected).

<a id="r3-validate-two-dimensional-geometry"></a>

### `_validate_two_dimensional_geometry`

function; source lines 354–369. Signature SHA256: `656fbc2b76715a518d133850093a2cd504531d5b7abf86270831171dcbaa5057`.

```python
def _validate_two_dimensional_geometry(
    frame: gpd.GeoDataFrame,
    label: str,
) -> None:
```

Computes Shapely coordinate dimensions as int64 and requires every dimension ==2, reraising PlanningFeaturesError and translating other Exception. Empty arrays pass the any() check (no separate early return). Applied to supplied normalized catalogs, not original parcels. Tests inject Z, not M/ZM.

Related evidence (limits in linked test explanation): [test_three_dimensional_normalized_catalogs_are_rejected](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-three-dimensional-normalized-catalogs-are-rejected), [test_two_dimensional_normalized_catalogs_remain_valid](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-two-dimensional-normalized-catalogs-remain-valid).

<a id="r3-validate-parcels"></a>

### `_validate_parcels`

function; source lines 372–396. Signature SHA256: `add12109a99f129ee2c3f9c55764c8bdf416fc05749059356470f9032dbf2d69`.

```python
def _validate_parcels(
    parcels: gpd.GeoDataFrame,
    *,
    allow_output_columns: bool = False,
) -> CRS:
```

Requires GeoDataFrame, unique columns, parcel_id/geometry and no reserved summary collisions unless allow_output_columns=True. Then checks active geometry, parses CRS, validates exact unique IDs and valid Polygon/MultiPolygon geometry; returns parsed source CRS. Does not force original geometry to 2D or rewrite it; metric area positivity is later.

Related evidence (limits in linked test explanation): [test_invalid_parcel_ids_are_rejected](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-invalid-parcel-ids-are-rejected), [test_reserved_output_column_collision_is_rejected](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-reserved-output-column-collision-is-rejected), [test_source_complete_contract_rejects_invalid_parcel_geometry](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-source-complete-contract-rejects-invalid-parcel-geometry).

<a id="r3-standard-model"></a>

### `_standard_model`

function; source lines 399–410. Signature SHA256: `12a0af9358946880268e2a0f9eebffd83fd2cd5546c9a9336c7bc319b737e67b`.

```python
def _standard_model(document: GpuPlanningDocument) -> str | None:
```

Reads the optional singular archive.document.standard_model first, then strict-validates each extraction.standard_models value and appends only unseen values to a local list. Returns None or the sole value; rejects multiple distinct models. No file IO or isolated conflicting-standard regression in this file.

Dedicated regression in this test file: none; reviewed against implementation and callers, not promoted to executable proof.

<a id="r3-planning-context"></a>

### `_planning_context`

function; source lines 413–430. Signature SHA256: `3c5faa1194069b3426f0964b35e505eb6e8f7f8eddb9fc1e98f435ee65c97c27`.

```python
def _planning_context(document: GpuPlanningDocument) -> _PlanningContext:
```

Requires isinstance(GpuPlanningDocument), strict-validates archive SHA then its 64 hexadecimal characters, six other metadata strings and reconciled standard model; returns _PlanningContext. No file acquisition or proof of config agreement in this local helper.

Related evidence (limits in linked test explanation): [test_source_complete_contract_binds_gpu_document_context](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-source-complete-contract-binds-gpu-document-context).

<a id="r3-summary-geometry-types"></a>

### `_summary_geometry_types`

function; source lines 433–435. Signature SHA256: `80093165b6932684463b35a01652c47d4c7eca64a185f1f887268fd672aafae4`.

```python
def _summary_geometry_types(frame: gpd.GeoDataFrame) -> tuple[tuple[str, int], ...]:
```

Returns sorted (Shapely type name, integer count) tuples from a frame. Pure in-memory calculation used to compare inspected summary geometry counts; not physical validation.

Related evidence (limits in linked test explanation): [test_mutated_source_summary_is_rejected](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-mutated-source-summary-is-rejected).

<a id="r3-validate-layer-summary"></a>

### `_validate_layer_summary`

function; source lines 438–485. Signature SHA256: `5784db59a13931a4a430bb0b91af926eb8c5304ff0989330c46bf1d68b14a8c4`.

```python
def _validate_layer_summary(
    layer: GpuInspectedLayer,
    context: _PlanningContext,
) -> None:
```

After raw geometry checks in _normalize_layer, validates readable equivalent frame/summary CRS; strict count types, exact document/SHA/layer/count/ordered columns/dtypes/null/type counts. Returns None without IO. GPU physical comparison precedes this: four bad-count cases fail there, but feature_count=True equals 1 under dataclass equality and reaches this stage's strict integer rejection.

Related evidence (limits in linked test explanation): [test_mutated_source_summary_is_rejected](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-mutated-source-summary-is-rejected), [test_source_summary_counts_are_strict_integers](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-source-summary-counts-are-strict-integers).

<a id="r3-project-geometry"></a>

### `_project_geometry`

function; source lines 488–501. Signature SHA256: `3631c701b1d1e7ddcd7967475c627a1586cc79d17b166423c23458b944d54fae`.

```python
def _project_geometry(frame: gpd.GeoDataFrame, label: str) -> gpd.GeoSeries:
```

Copies geometry if source CRS equals EPSG:2154, otherwise uses frame.to_crs(target).geometry, then always force_2d into a fresh GeoSeries with default positional index. The original frame index is not carried to this series; callers deliberately use geometry arrays/positions. Wraps transformation failures; stored input geometry remains unchanged.

Related evidence (limits in linked test explanation): [test_epsg4326_parcels_are_measured_in_lambert93_but_preserved](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-epsg4326-parcels-are-measured-in-lambert93-but-preserved), [test_unusable_source_crs_is_rejected](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-unusable-source-crs-is-rejected), [test_gpu_source_z_is_normalized_to_canonical_2d](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-gpu-source-z-is-normalized-to-canonical-2d).

<a id="r3-source-feature-ids"></a>

### `_source_feature_ids`

function; source lines 504–532. Signature SHA256: `04c0feb9b754aa9b6a906c877fe013d4832c1a9651390f3bdb2e158bbf2319b4`.

```python
def _source_feature_ids(
    layer: GpuInspectedLayer,
    spec: _LayerSpec,
    validated_source: GpuValidatedSpatialLayerSource,
) -> tuple[pd.Series, SourceIdentityKind, str]:
```

If CNIG field exists, reset its index, copy and validate exact unique strings, returning CNIG_ATTRIBUTE and field name. Otherwise only prescription_surface is allowed: empty frame returns empty object Series, nonempty requires verified ogr_fids length alignment, formats OGR_FID:<n> and validates unique strings. GPU dependency already checked physical FIDs as non-negative Integral-not-bool; this helper does not repeat numeric checks.

Related evidence (limits in linked test explanation): [test_prescription_surface_uses_validated_source_ogr_fid_when_cnig_id_absent](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-prescription-surface-uses-validated-source-ogr-fid-when-cnig-id-absent), [test_geopackage_prescription_surface_uses_sealed_ogr_fid_fallback](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-geopackage-prescription-surface-uses-sealed-ogr-fid-fallback), [test_present_empty_optional_layer_is_valid](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-present-empty-optional-layer-is-valid).

<a id="r3-optional-values"></a>

### `_optional_values`

function; source lines 535–538. Signature SHA256: `f16ffe38ae7f1f602f143a79f1bc51a215d66970589f0a27949e438ad5fcdbb2`.

```python
def _optional_values(frame: gpd.GeoDataFrame, source_field: str) -> np.ndarray:
```

Returns a copied numpy array when a raw field exists, otherwise a length-matched None object array. No trimming or optional-text validation. Called for COMMON_SOURCE_FIELDS during normalization; A-003 depends on this preservation.

Related evidence (limits in linked test explanation): [test_optional_raw_source_fields_are_not_fabricated](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-optional-raw-source-fields-are-not-fabricated).

<a id="r3-normalize-layer"></a>

### `_normalize_layer`

function; source lines 541–648. Signature SHA256: `470073ea665e88cf167e305493c40ece55e2bddc174bf45a4454c39df6c4312a`.

```python
def _normalize_layer(
    layer: GpuInspectedLayer,
    spec: _LayerSpec,
    context: _PlanningContext,
    validated_source: GpuValidatedSpatialLayerSource,
) -> gpd.GeoDataFrame:
```

Requires GeoDataFrame/active geometry and code/subcode/IDURBA/geometry fields, validates required raw strings, valid allowed family, then inspected summary. Verifies IDURBA against archive basename, chooses CNIG/FID identity, projects XY2154 and constructs a fresh frame of identity/lineage/raw values with RangeIndex. Rechecks projected geometry, computes positive finite full area/length or part count and returns it. Canonical dtype conversion happens later in _combine_catalogs, not here; no separate duplicate-column guard here. Source rows are not filtered by parcel intersections.

Related evidence (limits in linked test explanation): [test_surface_full_overlap_normalizes_raw_values_and_lineage](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-surface-full-overlap-normalizes-raw-values-and-lineage), [test_idurba_mismatch_is_rejected](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-idurba-mismatch-is-rejected), [test_line_crossing_and_partly_inside](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-line-crossing-and-partly-inside), [test_points_inside_boundary_outside_and_multipoint](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-points-inside-boundary-outside-and-multipoint).

<a id="r3-canonical-catalog-dtypes"></a>

### `_canonical_catalog_dtypes`

function; source lines 651–666. Signature SHA256: `94a9f2324c49148cba2776d530fc0f144678e7dc74239272974d3a10a360aa82`.

```python
def _canonical_catalog_dtypes(
    catalog: gpd.GeoDataFrame,
    kind: GeometryKind,
) -> gpd.GeoDataFrame:
```

Mutates and returns the same newly constructed catalog argument: rebuilds each nongeometry column as a Series of the normalized_feature_dtypes(kind, frame) dtype on current index, then sets unnamed zero-based RangeIndex. No copy/freeze guarantee for direct private callers. Dynamic all-null optional dtypes belong to the common schema module.

Related evidence (limits in linked test explanation): [test_public_source_validation_hashes_survive_parquet_readback](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-public-source-validation-hashes-survive-parquet-readback).

<a id="r3-empty-catalog"></a>

### `_empty_catalog`

function; source lines 669–682. Signature SHA256: `ef25d58404e7a8906c901ca142e733927f124e16b3605d3c70cb9192af0ffb9f`.

```python
def _empty_catalog(kind: GeometryKind) -> gpd.GeoDataFrame:
```

Creates all required columns with base dtypes, empty active geometry and EPSG:2154, then canonicalizes; returns a new GeoDataFrame for the specified kind. Base text/file dtypes depend on kind; not a universal object schema.

Related evidence (limits in linked test explanation): [test_missing_optional_layer_families_return_stable_empty_catalogs](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-missing-optional-layer-families-return-stable-empty-catalogs), [test_empty_and_nonempty_catalogs_have_identical_kind_schemas](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-empty-and-nonempty-catalogs-have-identical-kind-schemas).

<a id="r3-combine-catalogs"></a>

### `_combine_catalogs`

function; source lines 685–694. Signature SHA256: `5176e3ca975f1e66ccf2a3e70fa324dd47fe73d557949f0d7cb23c6c68917311`.

```python
def _combine_catalogs(
    frames: list[gpd.GeoDataFrame], kind: GeometryKind
) -> gpd.GeoDataFrame:
```

Returns _empty_catalog for no frames; otherwise concatenates in caller order with ignore_index, fixes CRS/geometry, validates planning IDs and canonicalizes dtypes/index. New frame, not a parcel filter. Ordering comes from fixed LAYER_SPECS selection.

Related evidence (limits in linked test explanation): [test_overlapping_surface_union_is_not_double_counted](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-overlapping-surface-union-is-not-double-counted), [test_same_source_id_is_allowed_in_distinct_logical_layers](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-same-source-id-is-allowed-in-distinct-logical-layers).

<a id="r3-normalized-catalogs"></a>

### `_normalized_catalogs`

function; source lines 697–762. Signature SHA256: `f2aea9adea2929620bcc9b5c03bd0a7f6a159004eb1102acc8a10ba88309749a`.

```python
def _normalized_catalogs(
    planning_document: GpuPlanningDocument,
) -> tuple[
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    tuple[GpuValidatedSpatialLayerSource, ...],
]:
```

Checks document context, every inspected zoning/related reference occurs exactly once in all_spatial_layers, and related logical roles are known and unique. Orders selected related layers by LAYER_SPECS; calls GPU batch physical revalidation once; translates GpuSpatialInspectionError. For each fresh source, replaces only the inspected frame with verified data, normalizes, then combines three kind catalogs; returns these plus validated sources. No selected related layers still triggers document/config/extraction/role validation; zoning is not selected for geometric reread here.

Related evidence (limits in linked test explanation): [test_source_complete_contract_binds_inspected_spatial_inventory](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-source-complete-contract-binds-inspected-spatial-inventory), [test_source_complete_contract_reloads_and_compares_source_catalog](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-source-complete-contract-reloads-and-compares-source-catalog), [test_missing_optional_layer_families_return_stable_empty_catalogs](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-missing-optional-layer-families-return-stable-empty-catalogs).

<a id="r3-normalized-catalogs-combined"></a>

### `_normalized_catalogs.combined`

function; source lines 747–755. Signature SHA256: `61894940c07e0baa73abadca422c9261a0858f0d90bb37a56515768a147272be`.

```python
    def combined(kind: GeometryKind) -> gpd.GeoDataFrame:
```

Closure over the newly built catalogs; gathers matching geometry-kind entries in LAYER_SPECS order and calls _combine_catalogs, yielding canonical empty output when none exist. No extra physical read.

Related evidence (limits in linked test explanation): [test_missing_optional_layer_families_return_stable_empty_catalogs](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-missing-optional-layer-families-return-stable-empty-catalogs).

<a id="r3-metric-parcels"></a>

### `_metric_parcels`

function; source lines 765–782. Signature SHA256: `ef600db2bdc98beee1f280906921baf5af47b12a8ffc4263f783531e1e3b2939`.

```python
def _metric_parcels(parcels: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
```

Projects a private XY2154 copy, requires each whole-parcel area finite and >0, and returns only original row position, parcel_id, metric area and metric geometry on a positional index. Stored parcel geometry/index remain untouched.

Related evidence (limits in linked test explanation): [test_epsg4326_parcels_are_measured_in_lambert93_but_preserved](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-epsg4326-parcels-are-measured-in-lambert93-but-preserved), [test_source_complete_contract_rejects_coherent_parcel_metric_mutation](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-source-complete-contract-rejects-coherent-parcel-metric-mutation).

<a id="r3-relation-base"></a>

### `_relation_base`

function; source lines 785–846. Signature SHA256: `e1a03e009c2a23bcc5a29f4e528a8f5adef52d278c2323fd6225ad9e3bccb3e3`.

```python
def _relation_base(
    metric: gpd.GeoDataFrame,
    catalog: gpd.GeoDataFrame,
) -> tuple[pd.DataFrame, np.ndarray, np.ndarray]:
```

Returns empty DataFrame and two empty int64 arrays for empty parcels or features. Otherwise inner GeoPandas sjoin(predicate='intersects') against full projected polygons, translating join failures; records parcel/feature positions and copies relation identity/raw fields. This is the shared candidate-pair gate, not distance or centroid matching.

Related evidence (limits in linked test explanation): [test_geospatial_operation_failure_is_controlled_and_chained](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-geospatial-operation-failure-is-controlled-and-chained), [test_surface_partial_and_touch_relations](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-surface-partial-and-touch-relations), [test_points_inside_boundary_outside_and_multipoint](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-points-inside-boundary-outside-and-multipoint).

<a id="r3-surface-relations"></a>

### `_surface_relations`

function; source lines 849–879. Signature SHA256: `99bc72c0f56aefc94134c1cde48e74cd6e7251973aad02c275d37c40b9d76ef5`.

```python
def _surface_relations(
    metric: gpd.GeoDataFrame,
    catalog: gpd.GeoDataFrame,
) -> pd.DataFrame:
```

Uses _relation_base, intersects matched full geometries, computes clipped area m2 and shares 100*area/whole parcel or full feature area. Positive area => AREA_OVERLAP; zero => TOUCH_ONLY. Retains private clipped geometry for union summaries; unrelated line floats are NaN and point counts are nullable NA. Empty candidates return immediately; intersection failures are controlled.

Related evidence (limits in linked test explanation): [test_surface_partial_and_touch_relations](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-surface-partial-and-touch-relations), [test_overlapping_surface_union_is_not_double_counted](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-overlapping-surface-union-is-not-double-counted).

<a id="r3-line-relations"></a>

### `_line_relations`

function; source lines 882–909. Signature SHA256: `cd3fdf523ed9fc0a3411e645bf36e3040fa07180249b71a02c570fd33a7fdd87`.

```python
def _line_relations(
    metric: gpd.GeoDataFrame,
    catalog: gpd.GeoDataFrame,
) -> pd.DataFrame:
```

Intersects each matched line with parcel and measures length m; positive => LENGTH_OVERLAP, zero => TOUCH_ONLY. Copies full feature_length_m as source_line_length_m; no union across lines. Sets irrelevant metrics to null. Empty candidates return immediately; intersection failures are translated.

Related evidence (limits in linked test explanation): [test_line_crossing_and_partly_inside](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-line-crossing-and-partly-inside), [test_line_boundary_touch_is_zero_length](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-line-boundary-touch-is-zero-length).

<a id="r3-point-relations"></a>

### `_point_relations`

function; source lines 912–948. Signature SHA256: `4e94cf32a7cb6bfd0869ee1db6802f8a0b9f91977cfba485f7df8fe6bb844e4c`.

```python
def _point_relations(
    metric: gpd.GeoDataFrame,
    catalog: gpd.GeoDataFrame,
) -> pd.DataFrame:
```

Explodes matched Point/MultiPoint parts, counts strict contains as inside and covers-minus-contains as boundary via position bincount. Keeps full-source part count, including outside parts; rejects a candidate with no covered part. Any inside => INSIDE, otherwise BOUNDARY_TOUCH. Unrelated floats are null. Empty candidates return immediately; part/containment operation failures are translated.

Related evidence (limits in linked test explanation): [test_points_inside_boundary_outside_and_multipoint](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-points-inside-boundary-outside-and-multipoint).

<a id="r3-empty-relations"></a>

### `_empty_relations`

function; source lines 951–967. Signature SHA256: `4cddb8417d552f2888b592299ab752bb21b18d166480bd8b67e0e1d1e695b52c`.

```python
def _empty_relations() -> pd.DataFrame:
```

Creates a new plain DataFrame in RELATION_COLUMNS order: seven float64 metric columns, three nullable Int64 count columns and remaining str columns, canonical RangeIndex. No geometry or file IO.

Related evidence (limits in linked test explanation): [test_missing_optional_layer_families_return_stable_empty_catalogs](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-missing-optional-layer-families-return-stable-empty-catalogs).

<a id="r3-build-relation-tables"></a>

### `_build_relation_tables`

function; source lines 970–994. Signature SHA256: `146c2db9caae53e1f6071cae93b3cde6c33d7e15fd9fb486706116ea2d08711e`.

```python
def _build_relation_tables(
    metric: gpd.GeoDataFrame,
    surfaces: gpd.GeoDataFrame,
    lines: gpd.GeoDataFrame,
    points: gpd.GeoDataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
```

Builds surface, line and point work tables in order; if all empty returns those plus _empty_relations. Otherwise concatenates, stable-sorts by original parcel position then planning_feature_id, selects 28 public columns, casts str/count dtypes and RangeIndex. Returns three work tables plus public plain relation table; private clipped geometry is not exposed there.

Related evidence (limits in linked test explanation): [test_relations_are_unique_deterministic_and_summaries_agree](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-relations-are-unique-deterministic-and-summaries-agree), [test_source_complete_contract_rejects_reordered_relations](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-source-complete-contract-rejects-reordered-relations).

<a id="r3-canonical-integrity-value"></a>

### `_canonical_integrity_value`

function; source lines 997–1025. Signature SHA256: `452b0f8e045c7e76d753a9892f0e2e8804151c3f02208fc81d285bd4b5e67501`.

```python
def _canonical_integrity_value(value: object) -> object:
```

Converts date/datetime/Timestamp to ISO first, numpy scalar recursively via item(), None/pd.NA/scalar-isna to null, then bool, Integral, finite Real and str. Unsupported objects or remaining nonfinite numbers raise PlanningFeaturesError. NaN is treated as missing before numeric finiteness. This scalar canonicalizer does not recursively accept arbitrary containers. No dedicated malformed-leaf regression in this test file.

Related evidence (limits in linked test explanation): [test_public_source_validation_hashes_survive_parquet_readback](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-public-source-validation-hashes-survive-parquet-readback).

<a id="r3-canonical-integrity-sha256"></a>

### `_canonical_integrity_sha256`

function; source lines 1028–1041. Signature SHA256: `e74d3e776526e4f42c9244d197e171a2783b7295287828f63f82073ee71d1bf1`.

```python
def _canonical_integrity_sha256(payload: object) -> str:
```

JSON dumps with sorted keys, compact separators, ensure_ascii=False, allow_nan=False, encodes UTF-8 and returns lowercase SHA256. Serialization exceptions become chained PlanningFeaturesError. It expects an already prepared payload; no file IO or repr-based hash.

Related evidence (limits in linked test explanation): [test_expected_relation_hash_binds_dtype_and_index_metadata](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-expected-relation-hash-binds-dtype-and-index-metadata).

<a id="r3-gpu-related-source-files-sha256"></a>

### `_gpu_related_source_files_sha256`

function; source lines 1044–1077. Signature SHA256: `621fee78af957ddbb29d438eae550e3f91c9885be91df424d8fc38826d1e501c`.

```python
def _gpu_related_source_files_sha256(
    planning_document: GpuPlanningDocument,
    sources: tuple[GpuValidatedSpatialLayerSource, ...],
) -> str:
```

Builds the verified_gpu_sources.v1 payload described in the hash section: sorts layers by logical name and files by relative path but preserves FID order. Consumes verified records, hashes no newly opened paths, excludes absolute cache root and includes archive SHA. Used by the source-complete validator only.

Related evidence (limits in linked test explanation): [test_public_source_validation_hashes_survive_parquet_readback](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-public-source-validation-hashes-survive-parquet-readback).

<a id="r3-expected-relations-content-sha256"></a>

### `_expected_relations_content_sha256`

function; source lines 1080–1093. Signature SHA256: `324fe7e80f49a4b020453c1117a3f4221b4b64a7ea2cc0857f0a9f088a3a1d79`.

```python
def _expected_relations_content_sha256(relations: pd.DataFrame) -> str:
```

Builds expected_relations.v2 from deterministic_frame_schema_signature, canonical index values and ordered tuples of all cells; then SHA256 of canonical JSON. Private function can hash noncanonical frame schemas; the public validator calls it on its canonical rebuild. Four direct schema/index mutations prove digest sensitivity, not all possible leaf encodings.

Related evidence (limits in linked test explanation): [test_expected_relation_hash_binds_dtype_and_index_metadata](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-expected-relation-hash-binds-dtype-and-index-metadata).

<a id="r3-technical-tolerance"></a>

### `_technical_tolerance`

function; source lines 1096–1097. Signature SHA256: `3f0809e5fc62cef272ea41bb03599d05f658a243dae4b9c812eaf5dbed20a26c`.

```python
def _technical_tolerance(parcel_area: float) -> float:
```

Thin delegate returning common technical_overlay_tolerance(parcel_area): max(1e-6, parcel_area*1e-12). Used for tiny union overshoot in _surface_union_summary. Other comparisons call the common tolerance directly with their own reference magnitudes. Pure numerical allowance, not buffer distance or business threshold; no direct threshold-edge regression in this file.

Dedicated regression in this test file: none; reviewed against implementation and callers, not promoted to executable proof.

<a id="r3-surface-union-summary"></a>

### `_surface_union_summary`

function; source lines 1100–1128. Signature SHA256: `939bc17603fbff72abb14ddf9d48ae99bac035fc603bb2b8608f525da3400809`.

```python
def _surface_union_summary(
    positive: pd.DataFrame,
    parcel_areas: np.ndarray,
    count: int,
) -> np.ndarray:
```

Starts a zero float64 array of parcel count; groups positive clipped surfaces by parcel position, union_all then area. Rejects nonfinite/negative union and overshoot beyond common tolerance; clamps only tiny overshoot to whole parcel area. Empty input returns zeros. Caller runs all-family and separate-family unions. No direct tiny-overshoot regression here.

Related evidence (limits in linked test explanation): [test_overlapping_surface_union_is_not_double_counted](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-overlapping-surface-union-is-not-double-counted), [test_corrupted_surface_union_contract_is_rejected](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-corrupted-surface-union-contract-is-rejected).

<a id="r3-attach-parcel-summaries"></a>

### `_attach_parcel_summaries`

function; source lines 1131–1242. Signature SHA256: `2938b56f1539437f24d7fb9326afd83db903c87779d21b9a7423b93e686deb1a`.

```python
def _attach_parcel_summaries(
    parcels: gpd.GeoDataFrame,
    metric: gpd.GeoDataFrame,
    surface_work: pd.DataFrame,
    line_work: pd.DataFrame,
    point_work: pd.DataFrame,
    context: _PlanningContext,
) -> gpd.GeoDataFrame:
```

Deep-copies source parcels, appends 11 count, eight float and two lineage columns. Counts relation rows except point inside/boundary member sums; raw surface area and line length sums retain overlap double counting. Computes all-family and family-specific surface unions and percentages; exact 100 when union equals area, zero for no matches. Uses positional arrays to preserve arbitrary parcel index. No persistence or caller mutation.

Related evidence (limits in linked test explanation): [test_inputs_and_all_existing_parcel_fields_are_preserved](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-inputs-and-all-existing-parcel-fields-are-preserved), [test_overlapping_surface_union_is_not_double_counted](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-overlapping-surface-union-is-not-double-counted), [test_points_inside_boundary_outside_and_multipoint](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-points-inside-boundary-outside-and-multipoint).

<a id="r3-attach-parcel-summaries-relation-counts"></a>

### `_attach_parcel_summaries.relation_counts`

function; source lines 1143–1153. Signature SHA256: `255ff1e7758d02c09f8641ab10e6e2e538efbd8614030a42d751fde02f91f1ea`.

```python
    def relation_counts(
        frame: pd.DataFrame, mask: pd.Series | None = None
    ) -> np.ndarray:
```

Closure over parcel count; returns zero int64 array for empty work, otherwise counts grouped rows by _parcel_position into that array. Used for surface/line/point and family relation counts, not point member counts.

Related evidence (limits in linked test explanation): [test_relations_are_unique_deterministic_and_summaries_agree](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-relations-are-unique-deterministic-and-summaries-agree).

<a id="r3-numeric-values"></a>

### `_numeric_values`

function; source lines 1245–1269. Signature SHA256: `f9088d0bfc3ea0c8b6aee2a6bb140fe915f78e9d3946ee4e91c4d09416c59fc4`.

```python
def _numeric_values(
    frame: pd.DataFrame,
    columns: set[str] | frozenset[str] | tuple[str, ...],
    label: str,
    *,
    allow_null: bool,
) -> None:
```

Returns None after iterating each named frame column and cell: missing is accepted only with allow_null=True, otherwise requires Real-not-bool, float conversion, finite and >=0. Conversion TypeError/ValueError/OverflowError are chained PlanningFeaturesError. No output array, positivity option, coercion of text or caller mutation; later kind-specific catalog guards require >0.

Related evidence (limits in linked test explanation): [test_corrupted_surface_union_contract_is_rejected](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-corrupted-surface-union-contract-is-rejected).

<a id="r3-integer-values"></a>

### `_integer_values`

function; source lines 1272–1285. Signature SHA256: `9a4941a6ce55bd7e8dc4c7795df23a753c1c6aac47058f8514f603c27a53cc6d`.

```python
def _integer_values(
    frame: pd.DataFrame,
    columns: set[str] | frozenset[str] | tuple[str, ...],
    label: str,
    *,
    allow_null: bool,
) -> None:
```

Returns None after iterating each named frame column and cell, accepting missing only when allow_null=True and applying _strict_nonnegative_integer otherwise. Does not convert the stored frame or return an array. Used for point metrics and parcel summary counts.

Related evidence (limits in linked test explanation): [test_strict_parcel_summary_integer_counts_are_enforced](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-strict-parcel-summary-integer-counts-are-enforced).

<a id="r3-null-safe-equal"></a>

### `_null_safe_equal`

function; source lines 1288–1305. Signature SHA256: `7a0dc2522de10ef547c8d5199a821d14b479f37cdb59560756092fc341a05611`.

```python
def _null_safe_equal(left: object, right: object) -> bool:
```

Computes pd.isna on both values and requires scalar bool/np.bool_ missing flags; two missing values compare equal, one missing unequal. Otherwise returns bool(left == right). TypeError/ValueError in missing/equality checks yield false. Used for copied relation facts and rebuild comparisons; not a tolerant numerical comparison.

Related evidence (limits in linked test explanation): [test_relation_must_match_feature_catalog](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-relation-must-match-feature-catalog).

<a id="r3-require-close"></a>

### `_require_close`

function; source lines 1308–1319. Signature SHA256: `4f980f1f04edbdb8d908981036ff8fca042b4b84f34d0f7f18b97a3d55af0d60`.

```python
def _require_close(actual: object, expected: float, label: str) -> None:
```

Requires a finite Real-not-bool actual, converting to float with controlled conversion errors. Compares abs(actual-expected) to common technical_overlay_tolerance(max(abs(actual), abs(expected))). Raises labeled PlanningFeaturesError on mismatch; never modifies supplied values. Used for recomputed metrics and union/formula comparisons.

Related evidence (limits in linked test explanation): [test_source_complete_contract_rejects_coherent_parcel_metric_mutation](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-source-complete-contract-rejects-coherent-parcel-metric-mutation), [test_source_complete_contract_rejects_coherent_but_wrong_line_metric](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-source-complete-contract-rejects-coherent-but-wrong-line-metric).

<a id="r3-validate-catalog-identity"></a>

### `_validate_catalog_identity`

function; source lines 1322–1368. Signature SHA256: `b329fec14b20f2cfaca65b162462c424600aef66e32999a762f84fa9355a44a3`.

```python
def _validate_catalog_identity(catalog: gpd.GeoDataFrame) -> None:
```

Checks 19 required and six optional exact-string columns, unique planning IDs, each known logical role/family/kind, permitted identity kind/field and deterministic GPU:document:logical:source ID. Allows archive-scoped OGR_FID only for prescription surfaces with its required prefix/field. Intrinsic, not physical: public orchestration already rebuilt physical catalogs before this guard, then compares them afterward. Optional exact-string rejection is A-003.

Related evidence (limits in linked test explanation): [test_feature_ids_are_globally_unique_across_catalogs](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-feature-ids-are-globally-unique-across-catalogs), [test_source_complete_contract_rejects_coherently_renamed_feature_identity](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-source-complete-contract-rejects-coherently-renamed-feature-identity).

<a id="r3-validate-catalog-contract"></a>

### `_validate_catalog_contract`

function; source lines 1371–1452. Signature SHA256: `a816a627f75631453f7a5cfdc14d7e059bfa41ac8e72fdcae5616c6f6cbc0e57`.

```python
def _validate_catalog_contract(
    catalog: object,
    geometry_kind: GeometryKind,
) -> gpd.GeoDataFrame:
```

Requires GeoDataFrame and canonical kind-specific column order/dtypes/RangeIndex/active geometry/2154. Checks identities, valid allowed geometry, exactly 2D and positive full metrics; recomputes area/length within tolerance or part count exactly. Returns the same validated frame without mutation. Common schema TypeError/ValueError become PlanningFeaturesError.

Related evidence (limits in linked test explanation): [test_public_normalized_input_contract_rejects_stripped_catalog](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-public-normalized-input-contract-rejects-stripped-catalog), [test_three_dimensional_normalized_catalogs_are_rejected](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-three-dimensional-normalized-catalogs-are-rejected).

<a id="r3-compare-normalized-catalog"></a>

### `_compare_normalized_catalog`

function; source lines 1455–1486. Signature SHA256: `ff151557866aa429f88a14d6ab29c30f75bc6c6aa69d3b36d6084c815c4d9ea1`.

```python
def _compare_normalized_catalog(
    supplied: gpd.GeoDataFrame,
    expected: gpd.GeoDataFrame,
    label: str,
) -> None:
```

Requires equal deterministic schema signatures, equivalent CRS, exact ordered WKB and pandas equality of nongeometry data against the freshly normalized catalog. No tolerance for changed catalog WKB or attributes; no source-file reading in this comparison helper.

Related evidence (limits in linked test explanation): [test_source_complete_contract_rejects_independent_gpu_lineage_mutation](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-source-complete-contract-rejects-independent-gpu-lineage-mutation).

<a id="r3-validate-relation-catalog-consistency"></a>

### `_validate_relation_catalog_consistency`

function; source lines 1508–1551. Signature SHA256: `1a3dec07c51f20841fe39af3bba9044fb94f4c0b2bd090e93098b83e1c368ff9`.

```python
def _validate_relation_catalog_consistency(
    relations: pd.DataFrame,
    catalogs: tuple[gpd.GeoDataFrame, gpd.GeoDataFrame, gpd.GeoDataFrame],
) -> None:
```

Concatenates catalog nongeometry rows, rejects global duplicate IDs and unknown feature references, compares all 15 copied facts null-safely, then exact full feature metric (line source_line_length_m maps to feature_length_m). No GIS or IO. The global-ID test fails earlier at deterministic identity, so it is not a direct regression of this duplicate branch.

Related evidence (limits in linked test explanation): [test_relation_must_match_feature_catalog](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-relation-must-match-feature-catalog).

<a id="r3-validate-relation-semantics"></a>

### `_validate_relation_semantics`

function; source lines 1554–1558. Signature SHA256: `f1d6fbd1f5e361861075a7010ac0df9fc32af526d0138a6c66bac292f1ec4593`.

```python
def _validate_relation_semantics(relations: pd.DataFrame) -> None:
```

Delegates to common validate_intrinsic_planning_feature_relations and translates TypeError/ValueError to chained PlanningFeaturesError. This checks kind/relation/metric/null/count/formula coherence, not source provenance or geometric completeness.

Related evidence (limits in linked test explanation): [test_point_member_relation_semantics_are_exact](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-point-member-relation-semantics-are-exact), [test_shared_intrinsic_relation_semantics_reject_every_invalid_case](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-shared-intrinsic-relation-semantics-reject-every-invalid-case).

<a id="r3-compare-rebuilt-relations"></a>

### `_compare_rebuilt_relations`

function; source lines 1561–1599. Signature SHA256: `9f5d5f9b4a0ee03ce5f193711fb13c30fcf7efee323871a70f5ffdf1e8a63fbb`.

```python
def _compare_rebuilt_relations(
    supplied: pd.DataFrame,
    expected: pd.DataFrame,
) -> None:
```

Requires exact schema, then equal index, then equal row count, before ordered cell comparisons. Thus extra-row cases with a reset RangeIndex fail the rebuilt-index comparison before the explicit count branch; the count guard follows an index equality that already constrains length. Float null patterns must match and finite values agree within tolerance; other cells compare null-safely. Missing-row test is stopped still earlier by canonical zero-based RangeIndex validation. No repair.

Related evidence (limits in linked test explanation): [test_source_complete_contract_rejects_extra_geometrically_false_relation](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-source-complete-contract-rejects-extra-geometrically-false-relation), [test_source_complete_contract_rejects_same_area_wrong_parcel_relation](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-source-complete-contract-rejects-same-area-wrong-parcel-relation), [test_source_complete_contract_rejects_reordered_relations](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-source-complete-contract-rejects-reordered-relations), [test_source_complete_contract_rejects_coherent_but_wrong_line_metric](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-source-complete-contract-rejects-coherent-but-wrong-line-metric).

<a id="r3-compare-rebuilt-parcel-output"></a>

### `_compare_rebuilt_parcel_output`

function; source lines 1602–1646. Signature SHA256: `427ceadb09cbf834d082605bd1405b203c4ae045b96a68564596ba0b114bece5`.

```python
def _compare_rebuilt_parcel_output(
    supplied: gpd.GeoDataFrame,
    expected: gpd.GeoDataFrame,
) -> None:
```

Compares full schema, exact index, equivalent CRS and ordered WKB with newly rebuilt parcel output. Planning floating summaries compare cellwise through _require_close; every other nongeometry column uses Series.equals (including dtype/order/null equality). Called only when public validator receives all 21 output fields; no physical read or mutation inside this comparison.

Related evidence (limits in linked test explanation): [test_source_complete_contract_rejects_noncanonical_parcel_summary_dtype](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-source-complete-contract-rejects-noncanonical-parcel-summary-dtype), [test_source_complete_contract_rejects_each_corrupted_parcel_summary_fact](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-source-complete-contract-rejects-each-corrupted-parcel-summary-fact).

<a id="r3-validate-normalized-planning-feature-inputs"></a>

### `_validate_normalized_planning_feature_inputs`

function; source lines 1649–1787. Signature SHA256: `14e9e05f7a84581924315d580f40be8e99d174a2cb58cd2248c811b609fdc088`.

```python
def _validate_normalized_planning_feature_inputs(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
) -> PlanningFeatureInputValidation:
```

Ordered source-complete boundary: require none/all 21 parcel outputs, validate baseline parcels and metric copy; physically rebuild catalogs; intrinsically validate supplied catalogs then compare exact rebuilds; check canonical plain relations, IDs and actual parcel areas, intrinsic semantics and catalog consistency; reconstruct all relations and compare. If complete parcel outputs supplied, rebuild/compare/check summaries and lineage. Return hashes/counts of verified sources and rebuilt relations. Accepts no arbitrary precompiled trust substitute; no mutation or network.

Related evidence (limits in linked test explanation): [test_public_normalized_input_contract_validates_step_7d_3_1_result](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-public-normalized-input-contract-validates-step-7d-3-1-result), [test_source_complete_contract_rejects_partial_parcel_output_columns](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-source-complete-contract-rejects-partial-parcel-output-columns), [test_source_complete_contract_accepts_complete_parcel_output_summaries](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-source-complete-contract-accepts-complete-parcel-output-summaries).

<a id="r3-validate-normalized-planning-feature-inputs"></a>

### `validate_normalized_planning_feature_inputs`

function; source lines 1790–1814. Signature SHA256: `4953e65f3ca9247ce04718697539810c6f5f0c1bc8e1c39e558887eb50f8ae15`.

```python
def validate_normalized_planning_feature_inputs(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
) -> PlanningFeatureInputValidation:
```

Public six-argument wrapper returning PlanningFeatureInputValidation. Reraises PlanningFeaturesError unchanged; chains any other Exception into a generic safe PlanningFeaturesError. Does not return or repair supplied frames. Downstream CNIG resolver invokes this before applying meanings. A-003 demonstrates that a builder output is not unconditionally accepted.

Related evidence (limits in linked test explanation): [test_public_normalized_input_contract_wraps_malformed_document_context](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-public-normalized-input-contract-wraps-malformed-document-context), [test_public_normalized_input_contract_is_exported](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-public-normalized-input-contract-is-exported), [test_public_source_validation_hashes_survive_parquet_readback](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-public-source-validation-hashes-survive-parquet-readback).

<a id="r3-validate-parcel-summaries"></a>

### `_validate_parcel_summaries`

function; source lines 1817–1936. Signature SHA256: `9754a50d3924d6db4f47e2eba4e58c0cdd05f3709e001bb73bb6a64b28358095`.

```python
def _validate_parcel_summaries(
    source: gpd.GeoDataFrame,
    output: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    surface_work: pd.DataFrame | None,
) -> None:
```

Validates strict count fields against relation counts, finite non-negative sums against related metric totals, full parcel-area bounds and percentage formulas for union fields. If surface_work is provided, recomputes actual unions; otherwise only available intrinsic/cross-table checks apply. Rebuilds metric parcel geometry locally, no disk reads of its own. Does not establish provenance alone.

Related evidence (limits in linked test explanation): [test_strict_parcel_summary_integer_counts_are_enforced](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-strict-parcel-summary-integer-counts-are-enforced), [test_corrupted_parcel_summary_is_rejected](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-corrupted-parcel-summary-is-rejected), [test_corrupted_surface_union_contract_is_rejected](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-corrupted-surface-union-contract-is-rejected).

<a id="r3-validate-result"></a>

### `_validate_result`

function; source lines 1939–2020. Signature SHA256: `0b23f58a74aebffcddbbadfc0af1bc3c7f5c1844354854d322249183a0d5eaca`.

```python
def _validate_result(
    source: gpd.GeoDataFrame,
    result: ParcelPlanningFeaturesResult,
    surface_work: pd.DataFrame | None = None,
    *,
    planning_document: GpuPlanningDocument,
    source_inputs_already_rebuilt: bool = False,
) -> None:
```

Checks preserved parcel row count/IDs/index/CRS/geometry and original columns, complete outputs and lineage. By default calls public source-complete input validation on source parcels plus result catalogs/relations. Builder passes source_inputs_already_rebuilt=True to skip that independent catalog/relation pass, then checks references and summaries with work geometry. This optimization is why A-003 can leave the builder unnoticed; the flag is private, not public authority.

Related evidence (limits in linked test explanation): [test_inputs_and_all_existing_parcel_fields_are_preserved](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-inputs-and-all-existing-parcel-fields-are-preserved), [test_corrupted_parcel_summary_is_rejected](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-corrupted-parcel-summary-is-rejected).

<a id="r3-intersect-parcels-with-gpu-planning-features"></a>

### `intersect_parcels_with_gpu_planning_features`

function; source lines 2023–2057. Signature SHA256: `5a76cdce6f2f1c255f3f6dffe485050987a86f4bf1b47643a0489ef53dc71a0d`.

```python
def intersect_parcels_with_gpu_planning_features(
    parcels: gpd.GeoDataFrame,
    planning_document: GpuPlanningDocument,
) -> ParcelPlanningFeaturesResult:
```

Public builder: validate original parcels, build context, physically normalize related GPU sources once, make metric parcel copy, build all relation/work tables, attach summaries, wrap five frames, then _validate_result with source_inputs_already_rebuilt=True. Returns factual evidence only, no code interpretation or legal/BESS decision. Specific helpers translate expected errors; there is no catch-all around this whole function. Optional raw strings are preserved (A-003 remains open).

Related evidence (limits in linked test explanation): [test_surface_full_overlap_normalizes_raw_values_and_lineage](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-surface-full-overlap-normalizes-raw-values-and-lineage), [test_line_crossing_and_partly_inside](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-line-crossing-and-partly-inside), [test_points_inside_boundary_outside_and_multipoint](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-points-inside-boundary-outside-and-multipoint), [test_only_high_level_api_is_exported](../../../tests/unit/test_enrich_planning_features.py.md#r3-test-only-high-level-api-is-exported).

## Change impact and exact source snapshot

A source change requires review of this companion, its exact fingerprint/snapshot,
qualified signatures, schemas, callers and assertion limits. R3 changes documentation
only; no schema/hash migration, code/test edit or new authority is introduced.

The following complete UTF-8 file is an aid to verification, not a substitute for
the semantic explanations above. It reproduces exact Git content bytes inside the fence.

```python
"""Normalize and intersect factual GPU prescription/information features."""

from __future__ import annotations

import json
from dataclasses import dataclass, replace
from datetime import date, datetime
from hashlib import sha256
from math import isfinite
from numbers import Integral, Real
from typing import Literal, NamedTuple

import geopandas as gpd  # type: ignore[import-untyped]
import numpy as np
import pandas as pd  # type: ignore[import-untyped]
from pyproj import CRS
from shapely import (  # type: ignore[import-untyped]
    area as shapely_area,
)
from shapely import (
    contains,
    covers,
    force_2d,
    get_coordinate_dimension,
    get_parts,
    intersection,
    union_all,
)
from shapely import (
    length as shapely_length,
)

from landscout.common.frame_integrity import deterministic_frame_schema_signature
from landscout.common.planning_feature_contract import (
    validate_intrinsic_planning_feature_relations,
)
from landscout.common.planning_feature_schema import (
    NORMALIZED_FEATURE_COLUMNS,
    NORMALIZED_FEATURE_DTYPES,
    NORMALIZED_RELATION_DTYPES,
    RELATION_COLUMNS,
    RELATION_COUNT_COLUMNS,
    RELATION_FLOAT_COLUMNS,
    RELATION_STRING_COLUMNS,
    normalized_feature_dtypes,
    validate_canonical_frame_schema,
)
from landscout.common.planning_overlay import technical_overlay_tolerance
from landscout.sources.gpu_fr import (
    GpuInspectedLayer,
    GpuPlanningDocument,
    GpuSpatialInspectionError,
    GpuValidatedSpatialLayerSource,
    revalidate_gpu_spatial_layer_sources,
)

__all__ = [
    "ParcelPlanningFeaturesResult",
    "PlanningFeatureInputValidation",
    "PlanningFeaturesError",
    "intersect_parcels_with_gpu_planning_features",
    "validate_normalized_planning_feature_inputs",
]

CALCULATION_CRS = "EPSG:2154"
PARCEL_REQUIRED_COLUMNS = frozenset({"parcel_id", "geometry"})

FeatureFamily = Literal["PRESCRIPTION", "INFORMATION"]
GeometryKind = Literal["SURFACE", "LINE", "POINT"]
SourceIdentityKind = Literal["CNIG_ATTRIBUTE", "ARCHIVE_SCOPED_OGR_FID"]

SOURCE_IDENTITY_KINDS = frozenset({"CNIG_ATTRIBUTE", "ARCHIVE_SCOPED_OGR_FID"})

SURFACE_TYPES = frozenset({"Polygon", "MultiPolygon"})
LINE_TYPES = frozenset({"LineString", "MultiLineString"})
POINT_TYPES = frozenset({"Point", "MultiPoint"})


class _LayerSpec(NamedTuple):
    logical_layer: str
    feature_family: FeatureFamily
    geometry_kind: GeometryKind
    identity_field: str
    type_field: str
    subtype_field: str
    allowed_geometry_types: frozenset[str]


LAYER_SPECS = {
    "prescription_surface": _LayerSpec(
        "prescription_surface",
        "PRESCRIPTION",
        "SURFACE",
        "LIB_IDPSC",
        "TYPEPSC",
        "STYPEPSC",
        SURFACE_TYPES,
    ),
    "prescription_line": _LayerSpec(
        "prescription_line",
        "PRESCRIPTION",
        "LINE",
        "LIB_IDPSC",
        "TYPEPSC",
        "STYPEPSC",
        LINE_TYPES,
    ),
    "prescription_point": _LayerSpec(
        "prescription_point",
        "PRESCRIPTION",
        "POINT",
        "LIB_IDPSC",
        "TYPEPSC",
        "STYPEPSC",
        POINT_TYPES,
    ),
    "information_surface": _LayerSpec(
        "information_surface",
        "INFORMATION",
        "SURFACE",
        "LIB_IDINFO",
        "TYPEINF",
        "STYPEINF",
        SURFACE_TYPES,
    ),
    "information_line": _LayerSpec(
        "information_line",
        "INFORMATION",
        "LINE",
        "LIB_IDINFO",
        "TYPEINF",
        "STYPEINF",
        LINE_TYPES,
    ),
    "information_point": _LayerSpec(
        "information_point",
        "INFORMATION",
        "POINT",
        "LIB_IDINFO",
        "TYPEINF",
        "STYPEINF",
        POINT_TYPES,
    ),
}

COMMON_SOURCE_FIELDS = {
    "label_raw": "LIBELLE",
    "text_raw": "TXT",
    "regulation_filename_raw": "NOMFIC",
    "regulation_url_raw": "URLFIC",
    "source_document_reference_raw": "IDURBA",
    "source_validity_date_raw": "DATVALID",
}
OPTIONAL_SOURCE_FIELDS = frozenset(
    {
        "LIBELLE",
        "TXT",
        "NOMFIC",
        "URLFIC",
        "DATVALID",
    }
)

_CATALOG_GEOMETRY_TYPES = {
    "SURFACE": SURFACE_TYPES,
    "LINE": LINE_TYPES,
    "POINT": POINT_TYPES,
}
_CATALOG_REQUIRED_EXACT_STRING_COLUMNS = (
    "planning_feature_id",
    "source_feature_id",
    "source_identity_kind",
    "source_identity_field",
    "logical_layer",
    "feature_family",
    "geometry_kind",
    "type_code_raw",
    "subtype_code_raw",
    "source_document_reference_raw",
    "source_provider",
    "source_portal",
    "source_commune_code",
    "source_document_id",
    "source_document_type",
    "source_archive_name",
    "source_archive_sha256",
    "source_layer",
    "source_crs",
)
_CATALOG_OPTIONAL_EXACT_STRING_COLUMNS = (
    "label_raw",
    "text_raw",
    "regulation_filename_raw",
    "regulation_url_raw",
    "source_validity_date_raw",
    "source_standard_model",
)

PARCEL_OUTPUT_COLUMNS = frozenset(
    {
        "planning_surface_relation_count",
        "planning_surface_area_overlap_count",
        "planning_surface_touch_count",
        "planning_surface_intersection_area_sum_m2",
        "planning_surface_covered_union_area_m2",
        "planning_surface_covered_pct",
        "prescription_surface_relation_count",
        "prescription_surface_covered_union_area_m2",
        "prescription_surface_covered_pct",
        "information_surface_relation_count",
        "information_surface_covered_union_area_m2",
        "information_surface_covered_pct",
        "planning_line_relation_count",
        "planning_line_length_overlap_count",
        "planning_line_touch_count",
        "planning_line_intersection_length_sum_m",
        "planning_point_relation_count",
        "planning_point_inside_count",
        "planning_point_boundary_count",
        "planning_feature_document_id",
        "planning_feature_archive_sha256",
    }
)

PARCEL_COUNT_COLUMNS = frozenset(
    {
        "planning_surface_relation_count",
        "planning_surface_area_overlap_count",
        "planning_surface_touch_count",
        "prescription_surface_relation_count",
        "information_surface_relation_count",
        "planning_line_relation_count",
        "planning_line_length_overlap_count",
        "planning_line_touch_count",
        "planning_point_relation_count",
        "planning_point_inside_count",
        "planning_point_boundary_count",
    }
)


class PlanningFeaturesError(ValueError):
    """Raised when factual GPU feature measurement cannot be completed safely."""


@dataclass(frozen=True)
class ParcelPlanningFeaturesResult:
    """Normalized feature catalogs, parcel enrichment, and factual relations."""

    parcels: gpd.GeoDataFrame
    surface_features: gpd.GeoDataFrame
    line_features: gpd.GeoDataFrame
    point_features: gpd.GeoDataFrame
    relations: pd.DataFrame


@dataclass(frozen=True)
class PlanningFeatureInputValidation:
    """Immutable source-completeness evidence for normalized planning facts."""

    gpu_related_source_files_sha256: str
    expected_relations_content_sha256: str
    related_source_layer_count: int
    related_source_file_count: int
    expected_relation_count: int


@dataclass(frozen=True)
class _PlanningContext:
    provider: str
    portal: str
    commune_code: str
    document_id: str
    document_type: str
    archive_name: str
    archive_sha256: str
    standard_model: str | None


def _strict_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise PlanningFeaturesError(f"{label} must be a non-empty exact string")
    return value


def _strict_nonnegative_integer(value: object, label: str) -> int:
    if isinstance(value, bool) or not isinstance(value, Integral):
        raise PlanningFeaturesError(f"{label} must be an integer count")
    if value < 0:
        raise PlanningFeaturesError(f"{label} must be non-negative")
    return int(value)


def _validate_ids(values: pd.Series, label: str) -> None:
    _validate_exact_strings(values, label)
    if values.duplicated().any():
        raise PlanningFeaturesError(f"{label} values must be unique")


def _validate_exact_strings(values: pd.Series, label: str) -> None:
    if values.isna().any():
        raise PlanningFeaturesError(f"{label} values must not be null")
    for value in values.tolist():
        _strict_string(value, label)


def _validate_optional_exact_strings(values: pd.Series, label: str) -> None:
    for value in values.tolist():
        if pd.isna(value):
            continue
        _strict_string(value, label)


def _crs(value: object, label: str) -> CRS:
    if value is None:
        raise PlanningFeaturesError(f"{label} CRS is required")
    try:
        return CRS.from_user_input(value)
    except Exception as error:
        raise PlanningFeaturesError(f"{label} CRS is unreadable") from error


def _active_geometry(frame: gpd.GeoDataFrame, label: str) -> None:
    if "geometry" not in frame.columns:
        raise PlanningFeaturesError(f"{label} geometry column is required")
    try:
        active = frame.active_geometry_name
    except AttributeError as error:
        raise PlanningFeaturesError(f"{label} geometry must be active") from error
    if active != "geometry":
        raise PlanningFeaturesError(f"{label} geometry must be active")


def _validate_geometries(
    frame: gpd.GeoDataFrame,
    allowed: frozenset[str],
    label: str,
) -> None:
    geometry = frame.geometry
    if geometry.isna().any():
        raise PlanningFeaturesError(f"{label} geometry must not be null")
    if geometry.is_empty.any():
        raise PlanningFeaturesError(f"{label} geometry must not be empty")
    if not geometry.is_valid.all():
        raise PlanningFeaturesError(f"{label} geometry must be valid")
    found = set(geometry.geom_type)
    if not found.issubset(allowed):
        raise PlanningFeaturesError(
            f"{label} has unsupported geometry types: "
            + ", ".join(sorted(found - allowed))
        )


def _validate_two_dimensional_geometry(
    frame: gpd.GeoDataFrame,
    label: str,
) -> None:
    try:
        dimensions = np.asarray(
            get_coordinate_dimension(frame.geometry.array), dtype="int64"
        )
        if (dimensions != 2).any():
            raise PlanningFeaturesError(f"{label} geometry must be canonical 2D")
    except PlanningFeaturesError:
        raise
    except Exception as error:
        raise PlanningFeaturesError(
            f"{label} geometry dimensionality cannot be validated"
        ) from error


def _validate_parcels(
    parcels: gpd.GeoDataFrame,
    *,
    allow_output_columns: bool = False,
) -> CRS:
    if not isinstance(parcels, gpd.GeoDataFrame):
        raise PlanningFeaturesError("Parcels must be a GeoDataFrame")
    if parcels.columns.duplicated().any():
        raise PlanningFeaturesError("Parcels contain duplicate columns")
    missing = sorted(PARCEL_REQUIRED_COLUMNS - set(parcels.columns))
    if missing:
        raise PlanningFeaturesError(
            "Parcels are missing required columns: " + ", ".join(missing)
        )
    collisions = sorted(PARCEL_OUTPUT_COLUMNS & set(parcels.columns))
    if collisions and not allow_output_columns:
        raise PlanningFeaturesError(
            "Parcels already contain planning-feature output columns: "
            + ", ".join(collisions)
        )
    _active_geometry(parcels, "Parcel")
    source_crs = _crs(parcels.crs, "Parcel")
    _validate_ids(parcels["parcel_id"], "parcel_id")
    _validate_geometries(parcels, SURFACE_TYPES, "Parcel")
    return source_crs


def _standard_model(document: GpuPlanningDocument) -> str | None:
    values: list[str] = []
    model = document.extraction.archive.document.standard_model
    if model is not None:
        values.append(_strict_string(model, "GPU standard model"))
    for value in document.extraction.standard_models:
        validated = _strict_string(value, "GPU extracted standard model")
        if validated not in values:
            values.append(validated)
    if len(values) > 1:
        raise PlanningFeaturesError("GPU standard-model lineage is ambiguous")
    return values[0] if values else None


def _planning_context(document: GpuPlanningDocument) -> _PlanningContext:
    if not isinstance(document, GpuPlanningDocument):
        raise PlanningFeaturesError("planning_document must be a GpuPlanningDocument")
    archive = document.extraction.archive
    metadata = archive.document
    sha = _strict_string(archive.sha256, "GPU archive SHA256")
    if len(sha) != 64 or any(c not in "0123456789abcdefABCDEF" for c in sha):
        raise PlanningFeaturesError("GPU archive SHA256 must contain 64 hex chars")
    return _PlanningContext(
        provider=_strict_string(metadata.provider, "GPU provider"),
        portal=_strict_string(metadata.portal, "GPU portal"),
        commune_code=_strict_string(metadata.commune_code, "GPU commune code"),
        document_id=_strict_string(metadata.document_id, "GPU document ID"),
        document_type=_strict_string(metadata.document_type, "GPU document type"),
        archive_name=_strict_string(metadata.archive_name, "GPU archive name"),
        archive_sha256=sha,
        standard_model=_standard_model(document),
    )


def _summary_geometry_types(frame: gpd.GeoDataFrame) -> tuple[tuple[str, int], ...]:
    counts = frame.geometry.geom_type.value_counts().sort_index()
    return tuple((str(key), int(value)) for key, value in counts.items())


def _validate_layer_summary(
    layer: GpuInspectedLayer,
    context: _PlanningContext,
) -> None:
    frame = layer.data
    summary = layer.summary
    actual_crs = _crs(frame.crs, f"{layer.logical_name} source")
    summary_crs = _crs(summary.crs, f"{layer.logical_name} summary")
    expected_nulls = tuple(
        (str(column), int(frame[column].isna().sum())) for column in frame.columns
    )
    expected_dtypes = tuple(
        (str(column), str(dtype)) for column, dtype in frame.dtypes.items()
    )
    geometry = frame.geometry
    non_null = geometry.notna()
    non_empty = non_null & ~geometry.is_empty
    _strict_nonnegative_integer(summary.feature_count, "summary feature_count")
    _strict_nonnegative_integer(
        summary.null_geometry_count, "summary null_geometry_count"
    )
    _strict_nonnegative_integer(
        summary.empty_geometry_count, "summary empty_geometry_count"
    )
    _strict_nonnegative_integer(
        summary.invalid_geometry_count, "summary invalid_geometry_count"
    )
    for column, value in summary.null_counts:
        _strict_nonnegative_integer(value, f"summary {column} null count")
    for geometry_type, value in summary.geometry_types:
        _strict_nonnegative_integer(value, f"summary {geometry_type} count")
    if (
        summary.source_document_id != context.document_id
        or summary.source_archive_sha256 != context.archive_sha256
        or summary.source_layer != layer.reference.source_layer
        or summary.feature_count != len(frame)
        or not actual_crs.equals(summary_crs)
        or summary.columns != tuple(str(column) for column in frame.columns)
        or summary.dtypes != expected_dtypes
        or summary.null_counts != expected_nulls
        or summary.geometry_types != _summary_geometry_types(frame)
        or summary.null_geometry_count != int((~non_null).sum())
        or summary.empty_geometry_count != int((non_null & geometry.is_empty).sum())
        or summary.invalid_geometry_count != int((non_empty & ~geometry.is_valid).sum())
    ):
        raise PlanningFeaturesError(
            f"{layer.logical_name} source summary is inconsistent with loaded data"
        )


def _project_geometry(frame: gpd.GeoDataFrame, label: str) -> gpd.GeoSeries:
    source = _crs(frame.crs, label)
    target = CRS.from_epsg(2154)
    try:
        projected = (
            frame.geometry.copy()
            if source.equals(target)
            else frame.to_crs(target).geometry
        )
        return gpd.GeoSeries(force_2d(projected.array), crs=target)
    except Exception as error:
        raise PlanningFeaturesError(
            f"{label} CRS cannot be transformed safely to EPSG:2154"
        ) from error


def _source_feature_ids(
    layer: GpuInspectedLayer,
    spec: _LayerSpec,
    validated_source: GpuValidatedSpatialLayerSource,
) -> tuple[pd.Series, SourceIdentityKind, str]:
    if spec.identity_field in layer.data.columns:
        result = layer.data[spec.identity_field].reset_index(drop=True).copy()
        _validate_ids(result, spec.identity_field)
        return result, "CNIG_ATTRIBUTE", spec.identity_field
    if spec.logical_layer == "prescription_surface":
        if layer.data.empty:
            return (
                pd.Series(dtype="object"),
                "ARCHIVE_SCOPED_OGR_FID",
                "OGR_FID",
            )
        if len(validated_source.ogr_fids) != len(layer.data):
            raise PlanningFeaturesError(
                f"{layer.logical_name} verified source FIDs are unavailable"
            )
        values = pd.Series(
            [f"OGR_FID:{value}" for value in validated_source.ogr_fids],
            dtype="object",
        )
        _validate_ids(values, f"{layer.logical_name} OGR FID")
        return values, "ARCHIVE_SCOPED_OGR_FID", "OGR_FID"
    raise PlanningFeaturesError(
        f"{spec.logical_layer} is missing required identity field {spec.identity_field}"
    )


def _optional_values(frame: gpd.GeoDataFrame, source_field: str) -> np.ndarray:
    if source_field not in frame.columns:
        return np.full(len(frame), None, dtype="object")
    return frame[source_field].to_numpy(copy=True)


def _normalize_layer(
    layer: GpuInspectedLayer,
    spec: _LayerSpec,
    context: _PlanningContext,
    validated_source: GpuValidatedSpatialLayerSource,
) -> gpd.GeoDataFrame:
    frame = layer.data
    if not isinstance(frame, gpd.GeoDataFrame):
        raise PlanningFeaturesError(f"{spec.logical_layer} must be a GeoDataFrame")
    _active_geometry(frame, spec.logical_layer)
    required = {spec.type_field, spec.subtype_field, "IDURBA", "geometry"}
    missing = sorted(required - set(frame.columns))
    if missing:
        raise PlanningFeaturesError(
            f"{spec.logical_layer} is missing required source fields: "
            + ", ".join(missing)
        )
    # Raw classification codes may repeat; validate hygiene without uniqueness.
    for field in (spec.type_field, spec.subtype_field, "IDURBA"):
        if frame[field].isna().any():
            raise PlanningFeaturesError(
                f"{spec.logical_layer} {field} must not be null"
            )
        for value in frame[field].tolist():
            _strict_string(value, f"{spec.logical_layer} {field}")
    _validate_geometries(frame, spec.allowed_geometry_types, spec.logical_layer)
    _validate_layer_summary(layer, context)
    expected_reference = (
        context.archive_name[:-4]
        if context.archive_name.casefold().endswith(".zip")
        else context.archive_name
    )
    if not frame["IDURBA"].eq(expected_reference).all():
        raise PlanningFeaturesError(
            f"{spec.logical_layer} IDURBA does not match planning archive identity"
        )

    source_ids, identity_kind, identity_field = _source_feature_ids(
        layer, spec, validated_source
    )
    planning_ids = source_ids.map(
        lambda value: f"GPU:{context.document_id}:{spec.logical_layer}:{value}"
    )
    geometry = _project_geometry(frame, spec.logical_layer)
    projected = gpd.GeoDataFrame(
        {
            "planning_feature_id": planning_ids.to_numpy(copy=True),
            "source_feature_id": source_ids.to_numpy(copy=True),
            "source_identity_kind": np.repeat(identity_kind, len(frame)),
            "source_identity_field": np.repeat(identity_field, len(frame)),
            "logical_layer": np.repeat(spec.logical_layer, len(frame)),
            "feature_family": np.repeat(spec.feature_family, len(frame)),
            "geometry_kind": np.repeat(spec.geometry_kind, len(frame)),
            "type_code_raw": frame[spec.type_field].to_numpy(copy=True),
            "subtype_code_raw": frame[spec.subtype_field].to_numpy(copy=True),
            **{
                normalized: _optional_values(frame, source)
                for normalized, source in COMMON_SOURCE_FIELDS.items()
            },
            "source_provider": np.repeat(context.provider, len(frame)),
            "source_portal": np.repeat(context.portal, len(frame)),
            "source_commune_code": np.repeat(context.commune_code, len(frame)),
            "source_document_id": np.repeat(context.document_id, len(frame)),
            "source_document_type": np.repeat(context.document_type, len(frame)),
            "source_archive_name": np.repeat(context.archive_name, len(frame)),
            "source_archive_sha256": np.repeat(context.archive_sha256, len(frame)),
            "source_layer": np.repeat(layer.reference.source_layer, len(frame)),
            "source_standard_model": np.full(
                len(frame), context.standard_model, dtype="object"
            ),
            "source_crs": np.repeat(layer.summary.crs, len(frame)),
        },
        geometry=geometry.to_numpy(copy=True),
        crs=CALCULATION_CRS,
    ).reset_index(drop=True)
    _validate_geometries(projected, spec.allowed_geometry_types, spec.logical_layer)
    if spec.geometry_kind == "SURFACE":
        try:
            values = projected.geometry.area.to_numpy(dtype="float64")
        except Exception as error:
            raise PlanningFeaturesError(
                f"{spec.logical_layer} area calculation failed"
            ) from error
        if not np.isfinite(values).all() or (values <= 0).any():
            raise PlanningFeaturesError(f"{spec.logical_layer} areas must be positive")
        projected["feature_area_m2"] = values
    elif spec.geometry_kind == "LINE":
        try:
            values = projected.geometry.length.to_numpy(dtype="float64")
        except Exception as error:
            raise PlanningFeaturesError(
                f"{spec.logical_layer} length calculation failed"
            ) from error
        if not np.isfinite(values).all() or (values <= 0).any():
            raise PlanningFeaturesError(
                f"{spec.logical_layer} lengths must be positive"
            )
        projected["feature_length_m"] = values
    else:
        try:
            projected["point_member_count"] = [
                len(get_parts(value)) for value in projected.geometry.array
            ]
        except Exception as error:
            raise PlanningFeaturesError(
                f"{spec.logical_layer} point-member calculation failed"
            ) from error
    return projected


def _canonical_catalog_dtypes(
    catalog: gpd.GeoDataFrame,
    kind: GeometryKind,
) -> gpd.GeoDataFrame:
    for column, dtype in zip(
        NORMALIZED_FEATURE_COLUMNS[kind],
        normalized_feature_dtypes(kind, catalog),
        strict=True,
    ):
        if column == "geometry":
            continue
        catalog[column] = pd.Series(
            catalog[column].tolist(), index=catalog.index, dtype=dtype
        )
    catalog.index = pd.RangeIndex(len(catalog))
    return catalog


def _empty_catalog(kind: GeometryKind) -> gpd.GeoDataFrame:
    data: dict[str, object] = {}
    for column, dtype in zip(
        NORMALIZED_FEATURE_COLUMNS[kind],
        NORMALIZED_FEATURE_DTYPES[kind],
        strict=True,
    ):
        data[column] = (
            gpd.GeoSeries([], crs=CALCULATION_CRS)
            if column == "geometry"
            else pd.Series(dtype=dtype)
        )
    output = gpd.GeoDataFrame(data, geometry="geometry", crs=CALCULATION_CRS)
    return _canonical_catalog_dtypes(output, kind)


def _combine_catalogs(
    frames: list[gpd.GeoDataFrame], kind: GeometryKind
) -> gpd.GeoDataFrame:
    if not frames:
        return _empty_catalog(kind)
    combined = gpd.GeoDataFrame(
        pd.concat(frames, ignore_index=True), geometry="geometry", crs=CALCULATION_CRS
    )
    _validate_ids(combined["planning_feature_id"], "planning_feature_id")
    return _canonical_catalog_dtypes(combined, kind)


def _normalized_catalogs(
    planning_document: GpuPlanningDocument,
) -> tuple[
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    tuple[GpuValidatedSpatialLayerSource, ...],
]:
    """Rebuild canonical catalogs from the inspected GPU related layers only."""

    context = _planning_context(planning_document)
    spatial_inventory = tuple(planning_document.all_spatial_layers)
    inspected_layers = (planning_document.zoning, *planning_document.related_layers)
    for layer in inspected_layers:
        if sum(reference == layer.reference for reference in spatial_inventory) != 1:
            raise PlanningFeaturesError(
                f"{layer.logical_name} inspected reference must occur exactly once "
                "in the GPU spatial-layer inventory"
            )
    layer_map: dict[str, GpuInspectedLayer] = {}
    for inspected_layer in planning_document.related_layers:
        logical = str(inspected_layer.logical_name)
        if logical not in LAYER_SPECS:
            raise PlanningFeaturesError(f"Unsupported related layer: {logical}")
        if logical in layer_map:
            raise PlanningFeaturesError(f"Duplicate related layer: {logical}")
        layer_map[logical] = inspected_layer

    try:
        validated_sources = revalidate_gpu_spatial_layer_sources(
            planning_document,
            tuple(
                layer_map[logical] for logical in LAYER_SPECS if logical in layer_map
            ),
        )
    except GpuSpatialInspectionError as error:
        raise PlanningFeaturesError(
            "Related GPU spatial sources failed physical revalidation"
        ) from error
    source_by_logical: dict[str, GpuValidatedSpatialLayerSource] = {
        source.logical_name: source for source in validated_sources
    }
    normalized: dict[str, gpd.GeoDataFrame] = {}
    for logical, layer in layer_map.items():
        source = source_by_logical[logical]
        fresh_layer = replace(layer, data=source.data)
        normalized[logical] = _normalize_layer(
            fresh_layer, LAYER_SPECS[logical], context, source
        )

    def combined(kind: GeometryKind) -> gpd.GeoDataFrame:
        return _combine_catalogs(
            [
                normalized[logical]
                for logical, spec in LAYER_SPECS.items()
                if spec.geometry_kind == kind and logical in normalized
            ],
            kind,
        )

    return (
        combined("SURFACE"),
        combined("LINE"),
        combined("POINT"),
        validated_sources,
    )


def _metric_parcels(parcels: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    geometry = _project_geometry(parcels, "Parcel")
    result = gpd.GeoDataFrame(
        {
            "_parcel_position": np.arange(len(parcels), dtype="int64"),
            "parcel_id": parcels["parcel_id"].to_numpy(copy=True),
        },
        geometry=geometry.to_numpy(copy=True),
        crs=CALCULATION_CRS,
    )
    try:
        areas = result.geometry.area.to_numpy(dtype="float64")
    except Exception as error:
        raise PlanningFeaturesError("Parcel metric-area calculation failed") from error
    if not np.isfinite(areas).all() or (areas <= 0).any():
        raise PlanningFeaturesError("Parcel metric areas must be finite and positive")
    result["_parcel_area_m2"] = areas
    return result


def _relation_base(
    metric: gpd.GeoDataFrame,
    catalog: gpd.GeoDataFrame,
) -> tuple[pd.DataFrame, np.ndarray, np.ndarray]:
    if catalog.empty or metric.empty:
        return pd.DataFrame(), np.array([], dtype="int64"), np.array([], dtype="int64")
    try:
        candidates = gpd.sjoin(
            metric[["_parcel_position", "parcel_id", "geometry"]],
            gpd.GeoDataFrame(
                {"_feature_position": np.arange(len(catalog), dtype="int64")},
                geometry=catalog.geometry.to_numpy(copy=True),
                crs=CALCULATION_CRS,
            ),
            how="inner",
            predicate="intersects",
        )
    except Exception as error:
        raise PlanningFeaturesError("Planning-feature spatial join failed") from error
    if candidates.empty:
        return pd.DataFrame(), np.array([], dtype="int64"), np.array([], dtype="int64")
    parcel_positions = candidates["_parcel_position"].to_numpy(dtype="int64")
    feature_positions = candidates["_feature_position"].to_numpy(dtype="int64")
    selected = catalog.iloc[feature_positions]
    base = pd.DataFrame(
        {
            "_parcel_position": parcel_positions,
            "_feature_position": feature_positions,
            "parcel_id": metric["parcel_id"].to_numpy()[parcel_positions],
            **{
                column: selected[column].to_numpy(copy=True)
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
                    "label_raw",
                    "text_raw",
                )
            },
            "parcel_metric_area_m2": metric["_parcel_area_m2"].to_numpy()[
                parcel_positions
            ],
            "source_document_id": selected["source_document_id"].to_numpy(copy=True),
            "source_archive_sha256": selected["source_archive_sha256"].to_numpy(
                copy=True
            ),
            "source_layer": selected["source_layer"].to_numpy(copy=True),
            "source_validity_date_raw": selected["source_validity_date_raw"].to_numpy(
                copy=True
            ),
            "regulation_filename_raw": selected["regulation_filename_raw"].to_numpy(
                copy=True
            ),
        }
    )
    return base, parcel_positions, feature_positions


def _surface_relations(
    metric: gpd.GeoDataFrame,
    catalog: gpd.GeoDataFrame,
) -> pd.DataFrame:
    base, parcel_positions, feature_positions = _relation_base(metric, catalog)
    if base.empty:
        return base
    try:
        geometries = intersection(
            metric.geometry.iloc[parcel_positions].array,
            catalog.geometry.iloc[feature_positions].array,
        )
        areas = np.asarray(shapely_area(geometries), dtype="float64")
    except Exception as error:
        raise PlanningFeaturesError(
            "Surface intersection calculation failed"
        ) from error
    feature_areas = catalog["feature_area_m2"].to_numpy(dtype="float64")[
        feature_positions
    ]
    base["_intersection_geometry"] = list(geometries)
    base["relation_type"] = np.where(areas > 0, "AREA_OVERLAP", "TOUCH_ONLY")
    base["feature_area_m2"] = feature_areas
    base["source_line_length_m"] = np.nan
    base["intersection_area_m2"] = areas
    base["intersection_length_m"] = np.nan
    base["parcel_share_pct"] = 100.0 * areas / base["parcel_metric_area_m2"]
    base["feature_share_pct"] = 100.0 * areas / feature_areas
    for column in RELATION_COUNT_COLUMNS:
        base[column] = pd.array([pd.NA] * len(base), dtype="Int64")
    return base


def _line_relations(
    metric: gpd.GeoDataFrame,
    catalog: gpd.GeoDataFrame,
) -> pd.DataFrame:
    base, parcel_positions, feature_positions = _relation_base(metric, catalog)
    if base.empty:
        return base
    try:
        geometries = intersection(
            metric.geometry.iloc[parcel_positions].array,
            catalog.geometry.iloc[feature_positions].array,
        )
        lengths = np.asarray(shapely_length(geometries), dtype="float64")
    except Exception as error:
        raise PlanningFeaturesError("Line intersection calculation failed") from error
    source_lengths = catalog["feature_length_m"].to_numpy(dtype="float64")[
        feature_positions
    ]
    base["relation_type"] = np.where(lengths > 0, "LENGTH_OVERLAP", "TOUCH_ONLY")
    base["feature_area_m2"] = np.nan
    base["source_line_length_m"] = source_lengths
    base["intersection_area_m2"] = np.nan
    base["intersection_length_m"] = lengths
    base["parcel_share_pct"] = np.nan
    base["feature_share_pct"] = np.nan
    for column in RELATION_COUNT_COLUMNS:
        base[column] = pd.array([pd.NA] * len(base), dtype="Int64")
    return base


def _point_relations(
    metric: gpd.GeoDataFrame,
    catalog: gpd.GeoDataFrame,
) -> pd.DataFrame:
    base, parcel_positions, feature_positions = _relation_base(metric, catalog)
    if base.empty:
        return base
    try:
        members, relation_positions = get_parts(
            catalog.geometry.iloc[feature_positions].array,
            return_index=True,
        )
        relation_positions = np.asarray(relation_positions, dtype="int64")
        member_parcels = metric.geometry.iloc[
            parcel_positions[relation_positions]
        ].array
        inside_mask = np.asarray(contains(member_parcels, members), dtype="bool")
        covered_mask = np.asarray(covers(member_parcels, members), dtype="bool")
    except Exception as error:
        raise PlanningFeaturesError("Point intersection calculation failed") from error
    member_counts = np.bincount(relation_positions, minlength=len(base))
    inside_counts = np.bincount(
        relation_positions, weights=inside_mask, minlength=len(base)
    ).astype("int64")
    covered_counts = np.bincount(
        relation_positions, weights=covered_mask, minlength=len(base)
    ).astype("int64")
    boundary_counts = covered_counts - inside_counts
    if ((inside_counts + boundary_counts) <= 0).any():
        raise PlanningFeaturesError("Point candidate has no covered source member")
    base["relation_type"] = np.where(inside_counts > 0, "INSIDE", "BOUNDARY_TOUCH")
    for column in RELATION_FLOAT_COLUMNS - {"parcel_metric_area_m2"}:
        base[column] = np.nan
    base["point_member_count"] = pd.array(member_counts, dtype="Int64")
    base["point_members_inside_count"] = pd.array(inside_counts, dtype="Int64")
    base["point_members_boundary_count"] = pd.array(boundary_counts, dtype="Int64")
    return base


def _empty_relations() -> pd.DataFrame:
    output = pd.DataFrame(
        {
            column: pd.Series(
                dtype=(
                    "float64"
                    if column in RELATION_FLOAT_COLUMNS
                    else "Int64"
                    if column in RELATION_COUNT_COLUMNS
                    else "str"
                )
            )
            for column in RELATION_COLUMNS
        }
    )
    output.index = pd.RangeIndex(0)
    return output


def _build_relation_tables(
    metric: gpd.GeoDataFrame,
    surfaces: gpd.GeoDataFrame,
    lines: gpd.GeoDataFrame,
    points: gpd.GeoDataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    surface_work = _surface_relations(metric, surfaces)
    line_work = _line_relations(metric, lines)
    point_work = _point_relations(metric, points)
    work_frames = [
        frame for frame in (surface_work, line_work, point_work) if not frame.empty
    ]
    if not work_frames:
        return surface_work, line_work, point_work, _empty_relations()
    combined = pd.concat(work_frames, ignore_index=True)
    combined = combined.sort_values(
        ["_parcel_position", "planning_feature_id"], kind="stable"
    ).reset_index(drop=True)
    relations = combined.loc[:, RELATION_COLUMNS].copy()
    for column in RELATION_STRING_COLUMNS:
        relations[column] = relations[column].astype("str")
    for column in RELATION_COUNT_COLUMNS:
        relations[column] = pd.array(relations[column], dtype="Int64")
    relations.index = pd.RangeIndex(len(relations))
    return surface_work, line_work, point_work, relations


def _canonical_integrity_value(value: object) -> object:
    if isinstance(value, (datetime, date, pd.Timestamp)):
        return value.isoformat()
    if isinstance(value, np.generic):
        return _canonical_integrity_value(value.item())
    if value is None or value is pd.NA:
        return None
    try:
        missing = pd.isna(value)
    except (TypeError, ValueError):
        missing = False
    if isinstance(missing, (bool, np.bool_)) and bool(missing):
        return None
    if isinstance(value, bool):
        return value
    if isinstance(value, Integral):
        return int(value)
    if isinstance(value, Real):
        number = float(value)
        if not isfinite(number):
            raise PlanningFeaturesError(
                "Integrity payload contains non-finite numeric data"
            )
        return number
    if isinstance(value, str):
        return value
    raise PlanningFeaturesError(
        f"Integrity payload contains unsupported value {type(value).__name__}"
    )


def _canonical_integrity_sha256(payload: object) -> str:
    try:
        encoded = json.dumps(
            payload,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    except Exception as error:
        raise PlanningFeaturesError(
            "Planning-feature integrity payload cannot be serialized"
        ) from error
    return sha256(encoded).hexdigest()


def _gpu_related_source_files_sha256(
    planning_document: GpuPlanningDocument,
    sources: tuple[GpuValidatedSpatialLayerSource, ...],
) -> str:
    return _canonical_integrity_sha256(
        {
            "domain": "landscout.planning_features.verified_gpu_sources.v1",
            "source_archive_sha256": planning_document.extraction.archive.sha256,
            "layers": [
                {
                    "logical_layer": source.logical_name,
                    "driver": source.driver,
                    "source_layer": source.source_layer,
                    "dataset_relative_path": source.dataset_relative_path,
                    "source_feature_count": source.feature_count,
                    "source_crs": source.source_crs,
                    "ogr_fids": list(source.ogr_fids),
                    "files": [
                        {
                            "relative_path": item.relative_path,
                            "file_type": item.file_type,
                            "size_bytes": item.size_bytes,
                            "sha256": item.sha256,
                            "category": item.category,
                        }
                        for item in sorted(
                            source.files, key=lambda value: value.relative_path
                        )
                    ],
                }
                for source in sorted(sources, key=lambda value: value.logical_name)
            ],
        }
    )


def _expected_relations_content_sha256(relations: pd.DataFrame) -> str:
    return _canonical_integrity_sha256(
        {
            "domain": "landscout.planning_features.expected_relations.v2",
            "schema": deterministic_frame_schema_signature(relations),
            "index": [
                _canonical_integrity_value(value) for value in relations.index.tolist()
            ],
            "rows": [
                [_canonical_integrity_value(value) for value in row]
                for row in relations.itertuples(index=False, name=None)
            ],
        }
    )


def _technical_tolerance(parcel_area: float) -> float:
    return technical_overlay_tolerance(parcel_area)


def _surface_union_summary(
    positive: pd.DataFrame,
    parcel_areas: np.ndarray,
    count: int,
) -> np.ndarray:
    output = np.zeros(count, dtype="float64")
    if positive.empty:
        return output
    for position_value, group in positive.groupby("_parcel_position", sort=False):
        position = int(position_value)
        try:
            value = float(
                shapely_area(union_all(group["_intersection_geometry"].to_numpy()))
            )
        except Exception as error:
            raise PlanningFeaturesError(
                "Surface covered-union calculation failed"
            ) from error
        if not isfinite(value) or value < 0:
            raise PlanningFeaturesError("Surface covered-union area is invalid")
        area = float(parcel_areas[position])
        if value > area:
            if value - area > _technical_tolerance(area):
                raise PlanningFeaturesError(
                    "Surface covered-union area exceeds parcel area"
                )
            value = area
        output[position] = value
    return output


def _attach_parcel_summaries(
    parcels: gpd.GeoDataFrame,
    metric: gpd.GeoDataFrame,
    surface_work: pd.DataFrame,
    line_work: pd.DataFrame,
    point_work: pd.DataFrame,
    context: _PlanningContext,
) -> gpd.GeoDataFrame:
    count = len(parcels)
    areas = metric["_parcel_area_m2"].to_numpy(dtype="float64")
    output = parcels.copy(deep=True)

    def relation_counts(
        frame: pd.DataFrame, mask: pd.Series | None = None
    ) -> np.ndarray:
        result = np.zeros(count, dtype="int64")
        selected = frame if mask is None else frame.loc[mask]
        if not selected.empty:
            counts = selected.groupby("_parcel_position", sort=False).size()
            result[counts.index.to_numpy(dtype="int64")] = counts.to_numpy(
                dtype="int64"
            )
        return result

    surface_positive = (
        surface_work.loc[surface_work["relation_type"] == "AREA_OVERLAP"]
        if not surface_work.empty
        else surface_work
    )
    surface_union = _surface_union_summary(surface_positive, areas, count)
    output["planning_surface_relation_count"] = relation_counts(surface_work)
    output["planning_surface_area_overlap_count"] = relation_counts(
        surface_work,
        surface_work["relation_type"].eq("AREA_OVERLAP")
        if not surface_work.empty
        else None,
    )
    output["planning_surface_touch_count"] = relation_counts(
        surface_work,
        surface_work["relation_type"].eq("TOUCH_ONLY")
        if not surface_work.empty
        else None,
    )
    raw_sum = np.zeros(count, dtype="float64")
    if not surface_positive.empty:
        sums = surface_positive.groupby("_parcel_position", sort=False)[
            "intersection_area_m2"
        ].sum()
        raw_sum[sums.index.to_numpy(dtype="int64")] = sums.to_numpy(dtype="float64")
    output["planning_surface_intersection_area_sum_m2"] = raw_sum
    output["planning_surface_covered_union_area_m2"] = surface_union
    output["planning_surface_covered_pct"] = np.where(
        surface_union == areas, 100.0, 100.0 * surface_union / areas
    )

    for family, prefix in (
        ("PRESCRIPTION", "prescription"),
        ("INFORMATION", "information"),
    ):
        family_work = (
            surface_work.loc[surface_work["feature_family"] == family]
            if not surface_work.empty
            else surface_work
        )
        family_positive = (
            family_work.loc[family_work["relation_type"] == "AREA_OVERLAP"]
            if not family_work.empty
            else family_work
        )
        union = _surface_union_summary(family_positive, areas, count)
        output[f"{prefix}_surface_relation_count"] = relation_counts(family_work)
        output[f"{prefix}_surface_covered_union_area_m2"] = union
        output[f"{prefix}_surface_covered_pct"] = np.where(
            union == areas, 100.0, 100.0 * union / areas
        )

    output["planning_line_relation_count"] = relation_counts(line_work)
    output["planning_line_length_overlap_count"] = relation_counts(
        line_work,
        line_work["relation_type"].eq("LENGTH_OVERLAP")
        if not line_work.empty
        else None,
    )
    output["planning_line_touch_count"] = relation_counts(
        line_work,
        line_work["relation_type"].eq("TOUCH_ONLY") if not line_work.empty else None,
    )
    line_sum = np.zeros(count, dtype="float64")
    if not line_work.empty:
        values = line_work.groupby("_parcel_position", sort=False)[
            "intersection_length_m"
        ].sum()
        line_sum[values.index.to_numpy(dtype="int64")] = values.to_numpy(
            dtype="float64"
        )
    output["planning_line_intersection_length_sum_m"] = line_sum

    output["planning_point_relation_count"] = relation_counts(point_work)
    for source, target in (
        ("point_members_inside_count", "planning_point_inside_count"),
        ("point_members_boundary_count", "planning_point_boundary_count"),
    ):
        values = np.zeros(count, dtype="int64")
        if not point_work.empty:
            grouped = point_work.groupby("_parcel_position", sort=False)[source].sum()
            values[grouped.index.to_numpy(dtype="int64")] = grouped.to_numpy(
                dtype="int64"
            )
        output[target] = values
    output["planning_feature_document_id"] = context.document_id
    output["planning_feature_archive_sha256"] = context.archive_sha256
    return output


def _numeric_values(
    frame: pd.DataFrame,
    columns: set[str] | frozenset[str] | tuple[str, ...],
    label: str,
    *,
    allow_null: bool,
) -> None:
    for column in columns:
        for value in frame[column].tolist():
            if pd.isna(value):
                if allow_null:
                    continue
                raise PlanningFeaturesError(f"{label} {column} must not be null")
            if isinstance(value, bool) or not isinstance(value, Real):
                raise PlanningFeaturesError(f"{label} {column} must be numeric")
            try:
                number = float(value)
            except (TypeError, ValueError, OverflowError) as error:
                raise PlanningFeaturesError(
                    f"{label} {column} must be finite"
                ) from error
            if not isfinite(number) or number < 0:
                raise PlanningFeaturesError(
                    f"{label} {column} must be finite and non-negative"
                )


def _integer_values(
    frame: pd.DataFrame,
    columns: set[str] | frozenset[str] | tuple[str, ...],
    label: str,
    *,
    allow_null: bool,
) -> None:
    for column in columns:
        for value in frame[column].tolist():
            if pd.isna(value):
                if allow_null:
                    continue
                raise PlanningFeaturesError(f"{label} {column} must not be null")
            _strict_nonnegative_integer(value, f"{label} {column}")


def _null_safe_equal(left: object, right: object) -> bool:
    try:
        left_missing = pd.isna(left)
        right_missing = pd.isna(right)
    except (TypeError, ValueError):
        return False
    if not isinstance(left_missing, (bool, np.bool_)) or not isinstance(
        right_missing, (bool, np.bool_)
    ):
        return False
    left_null = bool(left_missing)
    right_null = bool(right_missing)
    if left_null or right_null:
        return left_null and right_null
    try:
        return bool(left == right)
    except (TypeError, ValueError):
        return False


def _require_close(actual: object, expected: float, label: str) -> None:
    if isinstance(actual, bool) or not isinstance(actual, Real):
        raise PlanningFeaturesError(f"{label} must be numeric")
    try:
        number = float(actual)
    except (TypeError, ValueError, OverflowError) as error:
        raise PlanningFeaturesError(f"{label} must be finite") from error
    if not isfinite(number):
        raise PlanningFeaturesError(f"{label} must be finite")
    reference = max(abs(number), abs(expected))
    if abs(number - expected) > technical_overlay_tolerance(reference):
        raise PlanningFeaturesError(f"{label} is inconsistent")


def _validate_catalog_identity(catalog: gpd.GeoDataFrame) -> None:
    for column in _CATALOG_REQUIRED_EXACT_STRING_COLUMNS:
        _validate_exact_strings(
            catalog[column], f"Feature catalog {column.replace('_', ' ')}"
        )
    for column in _CATALOG_OPTIONAL_EXACT_STRING_COLUMNS:
        _validate_optional_exact_strings(
            catalog[column], f"Feature catalog {column.replace('_', ' ')}"
        )
    _validate_ids(catalog["planning_feature_id"], "planning_feature_id")
    for logical_layer, group in catalog.groupby("logical_layer", sort=False):
        _validate_ids(group["source_feature_id"], f"{logical_layer} source_feature_id")
    for _, row in catalog.iterrows():
        logical = _strict_string(row["logical_layer"], "logical_layer")
        if logical not in LAYER_SPECS:
            raise PlanningFeaturesError("Feature catalog logical layer is invalid")
        spec = LAYER_SPECS[logical]
        if row["feature_family"] != spec.feature_family:
            raise PlanningFeaturesError("Feature catalog family is inconsistent")
        if row["geometry_kind"] != spec.geometry_kind:
            raise PlanningFeaturesError(
                "Feature catalog logical layer and geometry kind are inconsistent"
            )
        expected_planning_id = (
            f"GPU:{row['source_document_id']}:{logical}:{row['source_feature_id']}"
        )
        if row["planning_feature_id"] != expected_planning_id:
            raise PlanningFeaturesError(
                "planning_feature_id differs from deterministic GPU identity"
            )
        kind = row["source_identity_kind"]
        field = row["source_identity_field"]
        if kind not in SOURCE_IDENTITY_KINDS:
            raise PlanningFeaturesError("Feature source identity kind is invalid")
        if kind == "CNIG_ATTRIBUTE":
            if field != spec.identity_field:
                raise PlanningFeaturesError(
                    "CNIG source identity field is inconsistent"
                )
        elif (
            logical != "prescription_surface"
            or field != "OGR_FID"
            or not str(row["source_feature_id"]).startswith("OGR_FID:")
        ):
            raise PlanningFeaturesError(
                "Archive-scoped OGR FID provenance is inconsistent"
            )


def _validate_catalog_contract(
    catalog: object,
    geometry_kind: GeometryKind,
) -> gpd.GeoDataFrame:
    label = f"{geometry_kind} feature catalog"
    if not isinstance(catalog, gpd.GeoDataFrame):
        raise PlanningFeaturesError(f"{label} must be a GeoDataFrame")
    try:
        validate_canonical_frame_schema(
            catalog,
            columns=NORMALIZED_FEATURE_COLUMNS[geometry_kind],
            dtypes=normalized_feature_dtypes(geometry_kind, catalog),
            label=label,
            geospatial=True,
            index_class="RangeIndex",
        )
    except (TypeError, ValueError) as error:
        raise PlanningFeaturesError(str(error)) from error
    _active_geometry(catalog, label)
    _validate_catalog_identity(catalog)
    if not catalog.empty and not catalog["geometry_kind"].eq(geometry_kind).all():
        raise PlanningFeaturesError(f"{label} geometry kind is invalid")
    _validate_geometries(catalog, _CATALOG_GEOMETRY_TYPES[geometry_kind], label)
    _validate_two_dimensional_geometry(catalog, label)
    if geometry_kind == "SURFACE":
        _numeric_values(
            catalog,
            ("feature_area_m2",),
            "Surface feature",
            allow_null=False,
        )
        if (catalog["feature_area_m2"] <= 0).any():
            raise PlanningFeaturesError("Surface feature areas must be positive")
        try:
            measured = catalog.geometry.area.to_numpy(dtype="float64")
        except Exception as error:
            raise PlanningFeaturesError(
                "Surface feature metric validation failed"
            ) from error
        for actual, expected in zip(
            catalog["feature_area_m2"].tolist(), measured, strict=True
        ):
            _require_close(actual, float(expected), "feature_area_m2")
    elif geometry_kind == "LINE":
        _numeric_values(
            catalog,
            ("feature_length_m",),
            "Line feature",
            allow_null=False,
        )
        if (catalog["feature_length_m"] <= 0).any():
            raise PlanningFeaturesError("Line feature lengths must be positive")
        try:
            measured = catalog.geometry.length.to_numpy(dtype="float64")
        except Exception as error:
            raise PlanningFeaturesError(
                "Line feature metric validation failed"
            ) from error
        for actual, expected in zip(
            catalog["feature_length_m"].tolist(), measured, strict=True
        ):
            _require_close(actual, float(expected), "feature_length_m")
    else:
        _integer_values(
            catalog,
            ("point_member_count",),
            "Point feature",
            allow_null=False,
        )
        if (catalog["point_member_count"] < 1).any():
            raise PlanningFeaturesError("Point features must contain a member")
        try:
            member_counts = [len(get_parts(value)) for value in catalog.geometry.array]
        except Exception as error:
            raise PlanningFeaturesError(
                "Point feature member validation failed"
            ) from error
        if catalog["point_member_count"].tolist() != member_counts:
            raise PlanningFeaturesError(
                "Point feature member count is inconsistent with geometry"
            )
    return catalog


def _compare_normalized_catalog(
    supplied: gpd.GeoDataFrame,
    expected: gpd.GeoDataFrame,
    label: str,
) -> None:
    if deterministic_frame_schema_signature(
        supplied
    ) != deterministic_frame_schema_signature(expected):
        raise PlanningFeaturesError(
            f"{label} schema differs from normalized GPU source"
        )
    try:
        supplied_crs = _crs(supplied.crs, label)
        expected_crs = _crs(expected.crs, f"expected {label}")
        geometry_equal = np.array_equal(
            supplied.geometry.to_wkb(), expected.geometry.to_wkb()
        )
        attributes_equal = supplied.drop(columns="geometry").equals(
            expected.drop(columns="geometry")
        )
    except PlanningFeaturesError:
        raise
    except Exception as error:
        raise PlanningFeaturesError(
            f"{label} cannot be compared with normalized GPU source"
        ) from error
    if (
        not supplied_crs.equals(expected_crs)
        or not geometry_equal
        or not attributes_equal
    ):
        raise PlanningFeaturesError(f"{label} differs from normalized GPU source")


_RELATION_CATALOG_FIELDS = (
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


def _validate_relation_catalog_consistency(
    relations: pd.DataFrame,
    catalogs: tuple[gpd.GeoDataFrame, gpd.GeoDataFrame, gpd.GeoDataFrame],
) -> None:
    feature_rows = pd.concat(
        [catalog.drop(columns="geometry") for catalog in catalogs],
        ignore_index=True,
    )
    if feature_rows["planning_feature_id"].duplicated().any():
        raise PlanningFeaturesError(
            "planning_feature_id values must be globally unique"
        )
    indexed = feature_rows.set_index("planning_feature_id", drop=False)
    for _, relation in relations.iterrows():
        identifier = relation["planning_feature_id"]
        if identifier not in indexed.index:
            raise PlanningFeaturesError(
                "Planning relation references an unknown feature"
            )
        feature = indexed.loc[identifier]
        for column in _RELATION_CATALOG_FIELDS:
            if not _null_safe_equal(relation[column], feature[column]):
                raise PlanningFeaturesError(
                    f"Relation {column} is inconsistent with feature catalog"
                )
        kind = relation["geometry_kind"]
        metric_column = {
            "SURFACE": "feature_area_m2",
            "LINE": "source_line_length_m",
            "POINT": "point_member_count",
        }.get(kind)
        catalog_column = {
            "SURFACE": "feature_area_m2",
            "LINE": "feature_length_m",
            "POINT": "point_member_count",
        }.get(kind)
        if (
            metric_column is None
            or catalog_column is None
            or not _null_safe_equal(relation[metric_column], feature[catalog_column])
        ):
            raise PlanningFeaturesError(
                "Relation feature metric is inconsistent with feature catalog"
            )


def _validate_relation_semantics(relations: pd.DataFrame) -> None:
    try:
        validate_intrinsic_planning_feature_relations(relations)
    except (TypeError, ValueError) as error:
        raise PlanningFeaturesError(str(error)) from error


def _compare_rebuilt_relations(
    supplied: pd.DataFrame,
    expected: pd.DataFrame,
) -> None:
    if deterministic_frame_schema_signature(
        supplied
    ) != deterministic_frame_schema_signature(expected):
        raise PlanningFeaturesError(
            "Planning relation schema differs from the spatial reconstruction"
        )
    if not supplied.index.equals(expected.index):
        raise PlanningFeaturesError(
            "Planning relation index or row order differs from the spatial reconstruction"
        )
    if len(supplied) != len(expected):
        raise PlanningFeaturesError(
            "Planning relation count differs from the spatial reconstruction"
        )
    for column in RELATION_COLUMNS:
        actual_values = supplied[column].tolist()
        expected_values = expected[column].tolist()
        for position, (actual, rebuilt) in enumerate(
            zip(actual_values, expected_values, strict=True)
        ):
            label = f"Planning relation {column} at row {position}"
            if column in RELATION_FLOAT_COLUMNS:
                actual_missing = bool(pd.isna(actual))
                expected_missing = bool(pd.isna(rebuilt))
                if actual_missing or expected_missing:
                    if actual_missing != expected_missing:
                        raise PlanningFeaturesError(
                            f"{label} null pattern differs from spatial reconstruction"
                        )
                    continue
                _require_close(actual, float(rebuilt), label)
            elif not _null_safe_equal(actual, rebuilt):
                raise PlanningFeaturesError(
                    f"{label} differs from the spatial reconstruction"
                )


def _compare_rebuilt_parcel_output(
    supplied: gpd.GeoDataFrame,
    expected: gpd.GeoDataFrame,
) -> None:
    if deterministic_frame_schema_signature(
        supplied
    ) != deterministic_frame_schema_signature(expected):
        raise PlanningFeaturesError(
            "Planning-feature parcel output schema differs from reconstruction"
        )
    if not supplied.index.equals(expected.index):
        raise PlanningFeaturesError(
            "Planning-feature parcel output index differs from reconstruction"
        )
    if not _crs(supplied.crs, "Parcel output").equals(
        _crs(expected.crs, "Expected parcel output")
    ) or not np.array_equal(supplied.geometry.to_wkb(), expected.geometry.to_wkb()):
        raise PlanningFeaturesError(
            "Planning-feature parcel geometry or CRS differs from reconstruction"
        )
    summary_float_columns = (
        PARCEL_OUTPUT_COLUMNS
        - PARCEL_COUNT_COLUMNS
        - {"planning_feature_document_id", "planning_feature_archive_sha256"}
    )
    for column in supplied.columns:
        if column == "geometry":
            continue
        if column in summary_float_columns:
            for position, (actual, rebuilt) in enumerate(
                zip(
                    supplied[column].tolist(),
                    expected[column].tolist(),
                    strict=True,
                )
            ):
                _require_close(
                    actual,
                    float(rebuilt),
                    f"Parcel summary {column} at row {position}",
                )
        elif not supplied[column].equals(expected[column]):
            raise PlanningFeaturesError(
                f"Planning-feature parcel column {column} differs from reconstruction"
            )


def _validate_normalized_planning_feature_inputs(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
) -> PlanningFeatureInputValidation:
    """Validate exact STEP 7D.3.1 facts against their document and parcels."""

    present_outputs = PARCEL_OUTPUT_COLUMNS & set(parcels.columns)
    if present_outputs and present_outputs != PARCEL_OUTPUT_COLUMNS:
        missing = sorted(PARCEL_OUTPUT_COLUMNS - present_outputs)
        raise PlanningFeaturesError(
            "Parcel planning-feature summaries are incomplete: " + ", ".join(missing)
        )
    _validate_parcels(parcels, allow_output_columns=True)
    source_parcels = (
        parcels.drop(columns=list(PARCEL_OUTPUT_COLUMNS))
        if present_outputs
        else parcels
    )
    _validate_parcels(source_parcels)
    metric_parcels = _metric_parcels(source_parcels)
    surfaces, lines, points, validated_sources = _normalized_catalogs(planning_document)
    expected_catalogs = (surfaces, lines, points)

    catalogs = (
        _validate_catalog_contract(surface_features, "SURFACE"),
        _validate_catalog_contract(line_features, "LINE"),
        _validate_catalog_contract(point_features, "POINT"),
    )
    for supplied, expected, label in zip(
        catalogs,
        expected_catalogs,
        ("SURFACE feature catalog", "LINE feature catalog", "POINT feature catalog"),
        strict=True,
    ):
        _compare_normalized_catalog(supplied, expected, label)
    all_feature_ids = [
        identifier
        for catalog in catalogs
        for identifier in catalog["planning_feature_id"].tolist()
    ]
    if len(all_feature_ids) != len(set(all_feature_ids)):
        raise PlanningFeaturesError(
            "planning_feature_id values must be globally unique"
        )

    if not isinstance(relations, pd.DataFrame) or isinstance(
        relations, gpd.GeoDataFrame
    ):
        raise PlanningFeaturesError("Planning relations must be a DataFrame")
    try:
        validate_canonical_frame_schema(
            relations,
            columns=RELATION_COLUMNS,
            dtypes=NORMALIZED_RELATION_DTYPES,
            label="Planning relations",
            geospatial=False,
            index_class="RangeIndex",
        )
    except (TypeError, ValueError) as error:
        raise PlanningFeaturesError(str(error)) from error
    _validate_exact_strings(relations["parcel_id"], "planning relation parcel_id")
    _validate_exact_strings(
        relations["planning_feature_id"], "planning relation planning_feature_id"
    )
    if relations.duplicated(["parcel_id", "planning_feature_id"]).any():
        raise PlanningFeaturesError("Parcel/planning-feature relations must be unique")
    if not set(relations["planning_feature_id"]).issubset(set(all_feature_ids)):
        raise PlanningFeaturesError("Planning relation references an unknown feature")
    parcel_areas = dict(
        zip(
            metric_parcels["parcel_id"].tolist(),
            metric_parcels["_parcel_area_m2"].tolist(),
            strict=True,
        )
    )
    for parcel_id, actual_area in relations[
        ["parcel_id", "parcel_metric_area_m2"]
    ].itertuples(index=False, name=None):
        if parcel_id not in parcel_areas:
            raise PlanningFeaturesError(
                "Planning relation references an unknown source parcel"
            )
        _require_close(
            actual_area,
            float(parcel_areas[parcel_id]),
            "Relation parcel metric area",
        )
    _validate_relation_semantics(relations)
    _validate_relation_catalog_consistency(relations, catalogs)
    surface_work, line_work, point_work, expected_relations = _build_relation_tables(
        metric_parcels, *expected_catalogs
    )
    _compare_rebuilt_relations(relations, expected_relations)

    if present_outputs:
        context = _planning_context(planning_document)
        expected_output = _attach_parcel_summaries(
            source_parcels,
            metric_parcels,
            surface_work,
            line_work,
            point_work,
            context,
        )
        _compare_rebuilt_parcel_output(parcels, expected_output)
        _validate_parcel_summaries(
            source_parcels, parcels, expected_relations, surface_work
        )
        if not parcels["planning_feature_document_id"].eq(context.document_id).all():
            raise PlanningFeaturesError(
                "Parcel planning-feature document lineage differs"
            )
        if (
            not parcels["planning_feature_archive_sha256"]
            .eq(context.archive_sha256)
            .all()
        ):
            raise PlanningFeaturesError(
                "Parcel planning-feature archive lineage differs"
            )

    unique_files = {
        item.relative_path for source in validated_sources for item in source.files
    }
    return PlanningFeatureInputValidation(
        gpu_related_source_files_sha256=_gpu_related_source_files_sha256(
            planning_document, validated_sources
        ),
        expected_relations_content_sha256=(
            _expected_relations_content_sha256(expected_relations)
        ),
        related_source_layer_count=len(validated_sources),
        related_source_file_count=len(unique_files),
        expected_relation_count=len(expected_relations),
    )


def validate_normalized_planning_feature_inputs(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
) -> PlanningFeatureInputValidation:
    """Validate exact STEP 7D.3.1 facts against their document and parcels."""

    try:
        return _validate_normalized_planning_feature_inputs(
            planning_document,
            parcels,
            surface_features,
            line_features,
            point_features,
            relations,
        )
    except PlanningFeaturesError:
        raise
    except Exception as error:
        raise PlanningFeaturesError(
            "Normalized planning-feature input validation failed safely"
        ) from error


def _validate_parcel_summaries(
    source: gpd.GeoDataFrame,
    output: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    surface_work: pd.DataFrame | None,
) -> None:
    metric = _metric_parcels(source)
    metric_areas = dict(
        zip(
            metric["parcel_id"].tolist(),
            metric["_parcel_area_m2"].tolist(),
            strict=True,
        )
    )
    _integer_values(output, PARCEL_COUNT_COLUMNS, "Parcel summary", allow_null=False)
    float_columns = tuple(
        PARCEL_OUTPUT_COLUMNS
        - PARCEL_COUNT_COLUMNS
        - {"planning_feature_document_id", "planning_feature_archive_sha256"}
    )
    _numeric_values(output, float_columns, "Parcel summary", allow_null=False)

    for _, parcel in output.iterrows():
        parcel_id = parcel["parcel_id"]
        rows = relations.loc[relations["parcel_id"] == parcel_id]
        surfaces = rows.loc[rows["geometry_kind"] == "SURFACE"]
        positive_surfaces = surfaces.loc[surfaces["relation_type"] == "AREA_OVERLAP"]
        lines = rows.loc[rows["geometry_kind"] == "LINE"]
        points = rows.loc[rows["geometry_kind"] == "POINT"]
        exact_counts = {
            "planning_surface_relation_count": len(surfaces),
            "planning_surface_area_overlap_count": len(positive_surfaces),
            "planning_surface_touch_count": int(
                surfaces["relation_type"].eq("TOUCH_ONLY").sum()
            ),
            "prescription_surface_relation_count": int(
                surfaces["feature_family"].eq("PRESCRIPTION").sum()
            ),
            "information_surface_relation_count": int(
                surfaces["feature_family"].eq("INFORMATION").sum()
            ),
            "planning_line_relation_count": len(lines),
            "planning_line_length_overlap_count": int(
                lines["relation_type"].eq("LENGTH_OVERLAP").sum()
            ),
            "planning_line_touch_count": int(
                lines["relation_type"].eq("TOUCH_ONLY").sum()
            ),
            "planning_point_relation_count": len(points),
            "planning_point_inside_count": int(
                points["point_members_inside_count"].sum()
            ),
            "planning_point_boundary_count": int(
                points["point_members_boundary_count"].sum()
            ),
        }
        for column, expected in exact_counts.items():
            if parcel[column] != expected:
                raise PlanningFeaturesError(
                    f"Parcel summary {column} is inconsistent with relations"
                )
        raw_sum = float(positive_surfaces["intersection_area_m2"].sum())
        line_sum = float(lines["intersection_length_m"].sum())
        _require_close(
            parcel["planning_surface_intersection_area_sum_m2"],
            raw_sum,
            "planning_surface_intersection_area_sum_m2",
        )
        _require_close(
            parcel["planning_line_intersection_length_sum_m"],
            line_sum,
            "planning_line_intersection_length_sum_m",
        )
        parcel_area = float(metric_areas[parcel_id])
        planning_union = float(parcel["planning_surface_covered_union_area_m2"])
        if planning_union - raw_sum > technical_overlay_tolerance(raw_sum):
            raise PlanningFeaturesError("Surface union exceeds raw intersection sum")
        if planning_union - parcel_area > technical_overlay_tolerance(parcel_area):
            raise PlanningFeaturesError("Surface union exceeds parcel area")
        for prefix in ("planning", "prescription", "information"):
            union = float(parcel[f"{prefix}_surface_covered_union_area_m2"])
            pct = float(parcel[f"{prefix}_surface_covered_pct"])
            if union - planning_union > technical_overlay_tolerance(planning_union):
                raise PlanningFeaturesError("Family surface union exceeds total union")
            expected_pct = (
                100.0 if union == parcel_area else 100.0 * union / parcel_area
            )
            pct_tolerance = (
                100.0 * technical_overlay_tolerance(parcel_area) / parcel_area
            )
            if abs(pct - expected_pct) > pct_tolerance:
                raise PlanningFeaturesError(
                    f"{prefix} surface percentage is inconsistent"
                )

    if surface_work is not None:
        areas = metric["_parcel_area_m2"].to_numpy(dtype="float64")
        positive = (
            surface_work.loc[surface_work["relation_type"] == "AREA_OVERLAP"]
            if not surface_work.empty
            else surface_work
        )
        expected_total = _surface_union_summary(positive, areas, len(output))
        for family, column in (
            (None, "planning_surface_covered_union_area_m2"),
            ("PRESCRIPTION", "prescription_surface_covered_union_area_m2"),
            ("INFORMATION", "information_surface_covered_union_area_m2"),
        ):
            expected_union = expected_total
            if family is not None:
                family_rows = (
                    positive.loc[positive["feature_family"] == family]
                    if not positive.empty
                    else positive
                )
                expected_union = _surface_union_summary(family_rows, areas, len(output))
            for actual, value in zip(
                output[column].tolist(), expected_union, strict=True
            ):
                _require_close(actual, float(value), column)


def _validate_result(
    source: gpd.GeoDataFrame,
    result: ParcelPlanningFeaturesResult,
    surface_work: pd.DataFrame | None = None,
    *,
    planning_document: GpuPlanningDocument,
    source_inputs_already_rebuilt: bool = False,
) -> None:
    output = result.parcels
    missing_output = sorted(PARCEL_OUTPUT_COLUMNS - set(output.columns))
    if missing_output:
        raise PlanningFeaturesError(
            "Planning-feature parcel output is missing columns: "
            + ", ".join(missing_output)
        )
    if len(output) != len(source):
        raise PlanningFeaturesError("Planning-feature parcel count changed")
    if output["parcel_id"].tolist() != source["parcel_id"].tolist():
        raise PlanningFeaturesError("Planning-feature parcel IDs or order changed")
    if not output.index.equals(source.index):
        raise PlanningFeaturesError("Planning-feature parcel index changed")
    if output.crs != source.crs or not np.array_equal(
        output.geometry.to_wkb(), source.geometry.to_wkb()
    ):
        raise PlanningFeaturesError("Planning-feature parcel geometry or CRS changed")
    for column in source.columns:
        if column == "geometry":
            continue
        if not output[column].equals(source[column]):
            raise PlanningFeaturesError(f"Existing parcel column changed: {column}")

    catalogs = (
        result.surface_features,
        result.line_features,
        result.point_features,
    )
    if not source_inputs_already_rebuilt:
        validate_normalized_planning_feature_inputs(
            planning_document,
            source,
            *catalogs,
            result.relations,
        )
    all_feature_ids = [
        identifier
        for catalog in catalogs
        for identifier in catalog["planning_feature_id"].tolist()
    ]
    known_features = set(all_feature_ids)

    relations = result.relations
    if not set(relations["parcel_id"]).issubset(set(output["parcel_id"])):
        raise PlanningFeaturesError("Planning relation references an unknown parcel")
    if not set(relations["planning_feature_id"]).issubset(known_features):
        raise PlanningFeaturesError("Planning relation references an unknown feature")
    _validate_parcel_summaries(source, output, relations, surface_work)
    for column in (
        "planning_feature_document_id",
        "planning_feature_archive_sha256",
    ):
        _validate_exact_strings(output[column], column)
    nonempty_catalogs = [catalog for catalog in catalogs if not catalog.empty]
    if nonempty_catalogs:
        expected_document_ids = {
            value
            for catalog in nonempty_catalogs
            for value in catalog["source_document_id"].tolist()
        }
        expected_archive_hashes = {
            value
            for catalog in nonempty_catalogs
            for value in catalog["source_archive_sha256"].tolist()
        }
        if (
            len(expected_document_ids) != 1
            or len(expected_archive_hashes) != 1
            or set(output["planning_feature_document_id"]) != expected_document_ids
            or set(output["planning_feature_archive_sha256"]) != expected_archive_hashes
        ):
            raise PlanningFeaturesError(
                "Parcel planning-feature lineage is inconsistent with catalogs"
            )


def intersect_parcels_with_gpu_planning_features(
    parcels: gpd.GeoDataFrame,
    planning_document: GpuPlanningDocument,
) -> ParcelPlanningFeaturesResult:
    """Measure factual GPU prescription/information relations to full parcels.

    All metric work is planar XY in EPSG:2154.  Raw codes are preserved without
    interpretation, and every pre-existing parcel field and geometry is copied.
    """

    _validate_parcels(parcels)
    context = _planning_context(planning_document)
    surfaces, lines, points, _ = _normalized_catalogs(planning_document)
    metric = _metric_parcels(parcels)
    surface_work, line_work, point_work, relations = _build_relation_tables(
        metric, surfaces, lines, points
    )
    parcel_output = _attach_parcel_summaries(
        parcels, metric, surface_work, line_work, point_work, context
    )
    result = ParcelPlanningFeaturesResult(
        parcels=parcel_output,
        surface_features=surfaces,
        line_features=lines,
        point_features=points,
        relations=relations,
    )
    _validate_result(
        parcels,
        result,
        surface_work,
        planning_document=planning_document,
        source_inputs_already_rebuilt=True,
    )
    return result
```
