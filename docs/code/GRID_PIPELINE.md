# Grid pipeline

## Implemented flow

```mermaid
flowchart TD
    Config[IgnBdTopoSourceConfig] --> Download[download_ign_bdtopo_archive]
    Download --> Extract[extract_ign_bdtopo_archive]
    Extract --> Load[load_ign_bdtopo_electricity]
    Load --> Source[IgnBdTopoElectricityData]
    Source --> Normalize[normalize_ign_electricity source config]
    Normalize --> Facts[NormalizedIgnElectricityData]
    Source --> Proximity[enrich_parcel_grid_proximity parcels source config]
    Proximity --> Result[GridProximityResult]
    Result --> Profile[profile_grid_proximity]
    Source --> Coverage[assess_grid_coverage parcels source config]
    Coverage --> Diagnostic[GridCoverageAssessmentResult]
    Diagnostic --> CoverageProfile[profile_grid_coverage]
```

## Physical IGN source

The checked-in IGN configuration identifies BD TOPO D031 package lineage and logical match rules for an electric-line layer, a transformation-post layer, road access, and department coverage. `load_ign_bdtopo_electricity` validates the extraction envelope and reproduces configured line/post physical roles from the verified GeoPackage inventory. It reads both layers in one verified batch, with GeoPackage hash checks before and after access, and returns frames plus deterministic `IgnBdTopoLayerSummary` objects.

An IGN transformation post is an IGN mapped feature. It is not an RTE connection node, an offered substation bay, or proof that the feature can accept a BESS connection.

## Source-complete normalization

`normalize_ign_electricity(source, config)` validates exact public types and calls a config-aware physical revalidator. Fresh configured line/post frames and summaries are exact-compared with the supplied source, so a coherent object for another physical layer cannot pass.

Normalization creates stable identities and factual lineage while preserving row order, geometry, CRS, Z coordinates, null/empty/invalid rows, and source attributes. Output includes separate electric-line and transformation-post GeoDataFrames with deterministic column order and RangeIndex.

### Voltage parsing

`parse_ign_voltage` interprets only the coded source voltage representation required by the normalizer:

- exact finite numeric voltage evidence becomes exact kilovolts/status;
- bounded/range evidence remains non-exact;
- de-energized/unknown/unexpected/malformed values receive explicit statuses;
- source asset status is not overwritten;
- nonfinite values never become numeric voltage output.

The parser is a factual vocabulary normalizer, not a capacity or compatibility model.

## Public proximity boundary

`enrich_parcel_grid_proximity(parcels, electricity_source, source_config)` accepts verified `IgnBdTopoElectricityData`, not normalized caller frames. It invokes source-complete normalization exactly once, validates parcels and normalized catalogs, and then calls a private frame-computation helper.

For each parcel it computes:

- nearest electric-line proxy distance and representative/tie identity;
- nearest transformation-post proxy distance and representative/tie identity;
- source provider/product/department/edition/archive/layer lineage for selected features;
- exact-voltage line/post views for every exact voltage level found in the normalized source;
- `VoltageLevelCoverage` counts indicating what source evidence was available.

## Nearest-feature algorithm

1. Validate parcel IDs, Polygon/MultiPolygon geometry, active geometry, CRS, and source facts.
2. Make EPSG:2154 force-2D calculation copies; never replace stored parcel/source geometry.
3. Select only rows whose geometry contract permits distance.
4. Build Shapely STRtree indexes.
5. Use `query_nearest(..., all_matches=True)` so equal nearest features are retained.
6. Calculate finite nonnegative Shapely distances in metres.
7. Sort deterministically by parcel, distance, and lexical feature ID.
8. Retain representative feature fields plus exact tie count/canonical tie-ID evidence.
9. Validate that broad and exact-voltage views represent consistent source features.
10. Return an exact parcel copy and deterministic proximity tables.

## Coverage boundary

`assess_grid_coverage(parcels, electricity_source, source_config)` owns one public proximity call and one `load_ign_bdtopo_department_coverage(electricity_source.extraction, config)` call. It validates that coverage is the configured layer/department-field selection from the same extraction.

On calculation copies it evaluates full parcels against the one EPSG:2154 department Polygon/MultiPolygon. Strictly interior parcels receive a distance to the coverage boundary. Touching/crossing/outside parcels receive zero and an outside/crossing position. For a matched grid feature:

- nearest distance less than boundary margin -> `NOT_BOUNDARY_LIMITED`;
- nearest distance equal to or greater than margin -> `BOUNDARY_LIMITED`;
- outside/crossing -> `OUTSIDE_OR_CROSSING_COVERAGE`;
- no selected feature -> `NO_MATCH` with precedence.

Coverage diagnosis warns about the finite verified package boundary. It does not search outside D031 or prove a global nearest feature.

## RTE / ODRÉ role

The RTE/ODRÉ adapter independently acquires configured official GeoJSON datasets and preserves metadata/geometry evidence. It does not replace the IGN transformation-post proxy with an RTE connection node inside this current proximity pipeline, and no code equates the two.

## Profiling

`profile_grid_proximity` and `profile_grid_coverage` validate existing result contracts and return count/quantile dataclasses. Profiling does not change rows, set thresholds, or decide feasibility.

## Explicit non-goals

Distance does not prove capacity, voltage compatibility for a project, ownership, connection point availability, queue status, network reinforcement, cost, schedule, feasibility, authorization, or a parcel score.
