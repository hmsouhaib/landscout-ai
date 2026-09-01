# Cadastre pipeline

## Implemented flow

```mermaid
flowchart TD
    Commune[Canonical commune code] --> Url[build_cadastre_parcelles_url]
    Url --> Download[download_cadastre_parcelles]
    Download --> Envelope[CadastreDownload]
    Envelope --> Load[load_cadastre_parcels]
    Load --> Source[CadastreParcelSource download plus parcels]
    Source --> Normalize[normalize_cadastre_parcels]
    Normalize --> Area[filter_parcels_by_area]
    Area --> Shape[enrich_parcel_shapes]
    Shape --> Screen[filter_parcels_by_shape]
    Shape --> Profile[profile_shape_distribution]
```

## Acquisition

`build_cadastre_parcelles_url` validates a canonical French commune identifier, derives the department path (including Corsican handling), and builds the official Etalab Cadastre parcels gzip URL. `download_cadastre_parcelles` uses shared safe HTTPS, streams exact bytes, validates gzip, computes size/SHA, and creates a frozen `CadastreDownload`. See [CACHE_AND_RECOVERY.md](CACHE_AND_RECOVERY.md) for hit/refresh/rollback behavior.

## Source-bound load and fresh revalidation

`load_cadastre_parcels(download)` accepts the exact result object rather than a caller path. `_validate_download` binds its canonical commune to the exact URL produced by `build_cadastre_parcelles_url`, requires the exact official filename/path, regular non-linked gzip, strict positive size, canonical lowercase SHA256, UTC timestamp, and current/stable physical size/SHA. It parses only nonempty, exactly 2D Polygon/MultiPolygon GeoJSON and returns `CadastreParcelSource(download, parcels)`.

`revalidate_cadastre_parcel_source(source)` repeats download/physical validation, rereads the gzip, exact-compares the supplied frame's columns, dtypes, index, CRS, active geometry, non-geometry values, WKB, and contractual attrs, then returns the fresh physical frame. `normalize_cadastre_parcels` must use that returned frame; validating one frame and then normalizing the caller's frame is forbidden.

## Normalization

`normalize_cadastre_parcels` requires an exact `CadastreParcelSource`. Its fresh frame must use EPSG:4326, contain the exact cadastral identity fields, agree with the download commune, and avoid every normalized/generated target-column collision. It validates unique exact parcel IDs and canonical commune identities. Output preserves source row order and geometry/CRS, resets to deterministic RangeIndex, and does not add download lineage columns.

The complete ordered output has exactly 12 columns:

| Position | Column | Source/calculation and contract |
|---:|---|---|
| 1 | `parcel_id` | Etalab `id`; exact non-empty string, unique. |
| 2 | `commune_code` | Etalab `commune`; canonical French INSEE string. |
| 3 | `section_prefix` | Etalab `prefixe`; exact non-empty string. |
| 4 | `section` | Etalab `section`; exact non-empty string. |
| 5 | `parcel_number` | Etalab `numero`; exact non-empty string. |
| 6 | `source_contenance` | Etalab `contenance`, value/null/dtype preserved; all-null column inserted if absent. |
| 7 | `source_arpente` | Etalab `arpente`, value/null/dtype preserved; all-null column inserted if absent. |
| 8 | `source_created_at` | Etalab `created`, value/null/dtype preserved; all-null column inserted if absent. |
| 9 | `source_updated_at` | Etalab `updated`, value/null/dtype preserved; all-null column inserted if absent. |
| 10 | `geometry_status` | Non-null and exactly `VALID` or `INVALID`; source geometry is never repaired. |
| 11 | `area_m2` | `float64`; finite positive area on an EPSG:2154 calculation copy for VALID rows, NaN for INVALID rows. |
| 12 | `geometry` | Original active EPSG:4326 Polygon/MultiPolygon geometry, including preserved null/empty/invalid values. |

## Area filter

`filter_parcels_by_area` reconstructs and revalidates an exact immutable `ParcelConfig` before masks, rejects a pre-existing `rejection_reason`, and invokes the shared canonical parcel validator. That validator requires the exact 12-column prefix, IDs, WGS84 geometry/status facts, a finite positive EPSG:2154-recomputed area for every `VALID` row, and null area for every `INVALID` row. Candidates preserve the input schema. Rejected rows append `rejection_reason`, exactly one of `AREA_UNKNOWN`, `INVALID_GEOMETRY`, `AREA_BELOW_MIN`, or `AREA_ABOVE_MAX`. Both subsets preserve source-relative order and original index labels. The configured minimum/maximum are policy thresholds, not geometry measurements; no ranking occurs.

## Shape enrichment

`enrich_parcel_shapes` validates the complete canonical parcel envelope, including recomputed area, and rejects any pre-existing generated shape column. For valid geometries it creates EPSG:2154 calculation copies and adds:

- `length_m` and `width_m` from the minimum rotated rectangle;
- `length_width_ratio`;
- `compactness`;
- centroid longitude/latitude derived from the geometric centroid transformed to EPSG:4326;
- `shape_status`, initialized to `ERROR` and changed to `VALID` only after every measurement succeeds.

All input columns/values and row order are preserved, but the result index is reset to RangeIndex. Invalid/non-measurable source geometry is preserved and receives NaN for all six metrics plus `shape_status=ERROR`. The input is not mutated.

## Shape screening and profiling

`filter_parcels_by_shape` reconstructs and revalidates the exact immutable `ShapeScreeningConfig`, rejects every pre-existing generated policy/reason column, and applies configured thresholds to already computed metrics. When disabled, retained is an unchanged copy of every input row and rejected is an empty same-schema copy; no policy columns are added. When enabled, both outputs append `shape_policy_version`, `shape_policy_min_width_m`, and `shape_policy_max_ratio`; rejected rows also append `shape_rejection_reason` (`RATIO_ABOVE_MAX`, `WIDTH_BELOW_MIN`, or `SHAPE_ERROR`). It preserves each subset's input order/index and does not recalculate geometry or infer planning/access/grid/environment meaning. `profile_shape_distribution` invokes the shared parcel contract, validates physical metric domains, excludes error rows from percentiles/buckets, and returns frozen profile dataclasses with scenario counts/percentages.

## GIS rules

- Storage parcel CRS: EPSG:4326.
- Metric calculation CRS: EPSG:2154.
- Supported valid geometry: Polygon/MultiPolygon.
- No silent repair or row drop in normalization/enrichment.
- Minimum rotated rectangle dimensions are factual geometric proxies, not a usable BESS footprint.

## Errors and tests

Controlled errors are `CadastreDownloadError`, loader-specific errors, `CadastreNormalizationError`, `ParcelFilterError`, `ShapeEnrichmentError`, and `ShapeProfileError`. The companions for `test_cadastre_fr.py`, `test_cadastre_loader_fr.py`, `test_normalize_cadastre.py`, `test_filter_parcels.py`, `test_filter_shape.py`, `test_enrich_shape.py`, and `test_profile_shape.py` map every test and failure injection.

## Explicit non-goals

This pipeline does not prove ownership/contact details, legal title, buildability, planning authorization, grid/road/environment suitability, or a BESS score. A kept parcel is only one that passed the coded factual area/shape screens.
