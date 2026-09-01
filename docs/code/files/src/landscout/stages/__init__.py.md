# `src/landscout/stages/__init__.py`

## File identity

- Repository path: `src/landscout/stages/__init__.py`
- File type: Python source
- Layer: pipeline stage
- Domain: factual transformation, evidence, or policy boundary
- Responsibility: Re-exports stable stage result, error, loader, validator, and transformation APIs, including factual zoning result/error contracts.
- Source SHA256: `c9f0d43ca4cb37ef2a5a9ca2b25fa5ea18809d4d533644b05f2705f8b62c99be`

## 1. STEP 7F.1A.4 contract delta

- Exports the approved source-bound Cadastre and factual planning-zoning high-level result/error surface without exposing low-level validators as public authority.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Re-exports stable stage result, error, loader, validator, and transformation APIs, including factual zoning result/error contracts.

The file belongs to the **pipeline stage** layer and **factual transformation, evidence, or policy boundary** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- None.

### Third-party packages

- None.

### Internal LandScout imports

- `from landscout.stages.aggregate_bess_planning_feature_policy import (
    BessPlanningFeatureParcelAggregationArtifactManifest,
    BessPlanningFeatureParcelAggregationError,
    BessPlanningFeatureParcelAggregationResult,
    aggregate_bess_planning_feature_policy_to_parcels,
    load_bess_planning_feature_parcel_aggregation_artifacts,
    validate_bess_planning_feature_parcel_aggregation_result,
)`
- `from landscout.stages.apply_bess_planning_feature_policy import (
    BessPlanningFeatureApplicationArtifactManifest,
    BessPlanningFeatureApplicationError,
    BessPlanningFeatureApplicationResult,
    apply_bess_planning_feature_policy,
    load_bess_planning_feature_application_artifacts,
    validate_bess_planning_feature_application_result,
    validate_bess_planning_feature_application_result_envelope,
)`
- `from landscout.stages.apply_road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyApplicationError,
    IgnRoadVehicleProxyApplicationResult,
    apply_ign_road_vehicle_proxy_policy,
)`
- `from landscout.stages.assess_grid_coverage import (
    BoundaryDistanceProfile,
    CoverageStatusCounts,
    GridCoverageAssessmentError,
    GridCoverageAssessmentResult,
    GridCoverageProfile,
    VoltageCoverageStatusProfile,
    assess_grid_coverage,
    profile_grid_coverage,
)`
- `from landscout.stages.assess_road_proximity_coverage import (
    RoadProximityCoverageAssessmentResult,
    RoadProximityCoverageError,
    assess_road_proximity_coverage,
)`
- `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyArtifactManifest,
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyError,
    BessPlanningFeaturePolicyResult,
    compile_bess_planning_feature_policy,
    load_bess_planning_feature_policy_artifacts,
    load_bess_planning_feature_policy_config,
    validate_bess_planning_feature_policy_result,
    validate_bess_planning_feature_policy_result_envelope,
)`
- `from landscout.stages.enrich_grid_proximity import (
    DistanceProfile,
    GridProximityError,
    GridProximityProfile,
    GridProximityResult,
    VoltageLevelCoverage,
    VoltageLevelDistanceProfile,
    enrich_parcel_grid_proximity,
    profile_grid_proximity,
)`
- `from landscout.stages.enrich_planning_features import (
    ParcelPlanningFeaturesResult,
    PlanningFeatureInputValidation,
    PlanningFeaturesError,
    intersect_parcels_with_gpu_planning_features,
    validate_normalized_planning_feature_inputs,
)`
- `from landscout.stages.enrich_planning_zoning import (
    ParcelZoningResult,
    PlanningZoningError,
    intersect_parcels_with_gpu_zoning,
    validate_normalized_planning_zoning_inputs,
)`
- `from landscout.stages.enrich_road_proximity import (
    ParcelRoadProximityResult,
    RoadProximityError,
    RoadProxyClassCoverage,
    enrich_parcel_road_proximity,
)`
- `from landscout.stages.enrich_shape import ShapeEnrichmentError, enrich_parcel_shapes`
- `from landscout.stages.filter_parcels import (
    ParcelFilterError,
    filter_parcels_by_area,
    filter_parcels_by_shape,
)`
- `from landscout.stages.index_planning_regulation import (
    PlanningRegulationIndex,
    PlanningRegulationIndexError,
    PlanningRegulationSearchResult,
    index_planning_regulation,
    search_planning_regulation,
    validate_planning_regulation_index,
    validate_planning_regulation_search_result,
)`
- `from landscout.stages.interpret_bess_zoning import (
    BessZoningPolicyConfig,
    BessZoningPrecheckError,
    BessZoningPrecheckResult,
    interpret_bess_zoning,
    load_bess_zoning_policy_config,
    validate_bess_zoning_precheck,
)`
- `from landscout.stages.normalize_access_ign import (
    IgnRoadNormalizationError,
    NormalizedIgnRoadData,
    normalize_ign_roads,
)`
- `from landscout.stages.normalize_cadastre import (
    CadastreNormalizationError,
    normalize_cadastre_parcels,
)`
- `from landscout.stages.normalize_grid_ign import (
    IgnGridNormalizationError,
    IgnVoltageNormalization,
    NormalizedIgnElectricityData,
    normalize_ign_electricity,
    parse_ign_voltage,
)`
- `from landscout.stages.profile_shape import (
    ShapeDistributionProfile,
    ShapeProfileError,
    profile_shape_distribution,
)`
- `from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeError,
    PlanningFeatureCodeResult,
    load_cnig_feature_code_profile,
    resolve_planning_feature_codes,
    validate_planning_feature_code_result,
    validate_planning_feature_code_result_envelope,
)`
- `from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    IgnRoadVehicleProxyPolicyError,
    load_ign_road_vehicle_proxy_policy,
)`
- `from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureError,
    PlanningRegulationStructureResult,
    load_planning_regulation_structure_config,
    planning_regulation_section_page_fragments,
    structure_planning_regulation,
    validate_planning_regulation_structure,
    validate_planning_regulation_structure_with_fragments,
)`

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `__all__`

- Category: explicit package/module export list.
- Exact declaration:

```python
__all__ = [
    "BessPlanningFeatureApplicationArtifactManifest",
    "BessPlanningFeatureApplicationError",
    "BessPlanningFeatureApplicationResult",
    "BessPlanningFeatureParcelAggregationArtifactManifest",
    "BessPlanningFeatureParcelAggregationError",
    "BessPlanningFeatureParcelAggregationResult",
    "BessPlanningFeaturePolicyArtifactManifest",
    "BessPlanningFeaturePolicyConfig",
    "BessPlanningFeaturePolicyError",
    "BessPlanningFeaturePolicyResult",
    "BessZoningPolicyConfig",
    "BessZoningPrecheckError",
    "BessZoningPrecheckResult",
    "BoundaryDistanceProfile",
    "CadastreNormalizationError",
    "CnigFeatureCodeProfile",
    "CoverageStatusCounts",
    "DistanceProfile",
    "GridCoverageAssessmentError",
    "GridCoverageAssessmentResult",
    "GridCoverageProfile",
    "GridProximityError",
    "GridProximityProfile",
    "GridProximityResult",
    "IgnGridNormalizationError",
    "IgnRoadNormalizationError",
    "IgnRoadVehicleProxyApplicationError",
    "IgnRoadVehicleProxyApplicationResult",
    "IgnRoadVehicleProxyPolicy",
    "IgnRoadVehicleProxyPolicyError",
    "IgnVoltageNormalization",
    "NormalizedIgnElectricityData",
    "NormalizedIgnRoadData",
    "ParcelFilterError",
    "ParcelPlanningFeaturesResult",
    "ParcelRoadProximityResult",
    "ParcelZoningResult",
    "PlanningFeatureCodeError",
    "PlanningFeatureCodeResult",
    "PlanningFeatureInputValidation",
    "PlanningFeaturesError",
    "PlanningRegulationIndex",
    "PlanningRegulationIndexError",
    "PlanningRegulationSearchResult",
    "PlanningRegulationStructureConfig",
    "PlanningRegulationStructureError",
    "PlanningRegulationStructureResult",
    "PlanningZoningError",
    "RoadProximityCoverageAssessmentResult",
    "RoadProximityCoverageError",
    "RoadProximityError",
    "RoadProxyClassCoverage",
    "ShapeDistributionProfile",
    "ShapeEnrichmentError",
    "ShapeProfileError",
    "VoltageCoverageStatusProfile",
    "VoltageLevelCoverage",
    "VoltageLevelDistanceProfile",
    "aggregate_bess_planning_feature_policy_to_parcels",
    "apply_bess_planning_feature_policy",
    "apply_ign_road_vehicle_proxy_policy",
    "assess_grid_coverage",
    "assess_road_proximity_coverage",
    "compile_bess_planning_feature_policy",
    "enrich_parcel_grid_proximity",
    "enrich_parcel_road_proximity",
    "enrich_parcel_shapes",
    "filter_parcels_by_area",
    "filter_parcels_by_shape",
    "index_planning_regulation",
    "interpret_bess_zoning",
    "intersect_parcels_with_gpu_planning_features",
    "intersect_parcels_with_gpu_zoning",
    "load_bess_planning_feature_application_artifacts",
    "load_bess_planning_feature_parcel_aggregation_artifacts",
    "load_bess_planning_feature_policy_artifacts",
    "load_bess_planning_feature_policy_config",
    "load_bess_zoning_policy_config",
    "load_cnig_feature_code_profile",
    "load_ign_road_vehicle_proxy_policy",
    "load_planning_regulation_structure_config",
    "normalize_cadastre_parcels",
    "normalize_ign_electricity",
    "normalize_ign_roads",
    "parse_ign_voltage",
    "planning_regulation_section_page_fragments",
    "profile_grid_coverage",
    "profile_grid_proximity",
    "profile_shape_distribution",
    "resolve_planning_feature_codes",
    "search_planning_regulation",
    "structure_planning_regulation",
    "validate_bess_planning_feature_application_result",
    "validate_bess_planning_feature_application_result_envelope",
    "validate_bess_planning_feature_parcel_aggregation_result",
    "validate_bess_planning_feature_policy_result",
    "validate_bess_planning_feature_policy_result_envelope",
    "validate_bess_zoning_precheck",
    "validate_normalized_planning_feature_inputs",
    "validate_normalized_planning_zoning_inputs",
    "validate_planning_feature_code_result",
    "validate_planning_feature_code_result_envelope",
    "validate_planning_regulation_index",
    "validate_planning_regulation_search_result",
    "validate_planning_regulation_structure",
    "validate_planning_regulation_structure_with_fragments",
]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `BessPlanningFeatureApplicationArtifactManifest`
  - `BessPlanningFeatureApplicationError`
  - `BessPlanningFeatureApplicationResult`
  - `BessPlanningFeatureParcelAggregationArtifactManifest`
  - `BessPlanningFeatureParcelAggregationError`
  - `BessPlanningFeatureParcelAggregationResult`
  - `BessPlanningFeaturePolicyArtifactManifest`
  - `BessPlanningFeaturePolicyConfig`
  - `BessPlanningFeaturePolicyError`
  - `BessPlanningFeaturePolicyResult`
  - `BessZoningPolicyConfig`
  - `BessZoningPrecheckError`
  - `BessZoningPrecheckResult`
  - `BoundaryDistanceProfile`
  - `CadastreNormalizationError`
  - `CnigFeatureCodeProfile`
  - `CoverageStatusCounts`
  - `DistanceProfile`
  - `GridCoverageAssessmentError`
  - `GridCoverageAssessmentResult`
  - `GridCoverageProfile`
  - `GridProximityError`
  - `GridProximityProfile`
  - `GridProximityResult`
  - `IgnGridNormalizationError`
  - `IgnRoadNormalizationError`
  - `IgnRoadVehicleProxyApplicationError`
  - `IgnRoadVehicleProxyApplicationResult`
  - `IgnRoadVehicleProxyPolicy`
  - `IgnRoadVehicleProxyPolicyError`
  - `IgnVoltageNormalization`
  - `NormalizedIgnElectricityData`
  - `NormalizedIgnRoadData`
  - `ParcelFilterError`
  - `ParcelPlanningFeaturesResult`
  - `ParcelRoadProximityResult`
  - `ParcelZoningResult`
  - `PlanningFeatureCodeError`
  - `PlanningFeatureCodeResult`
  - `PlanningFeatureInputValidation`
  - `PlanningFeaturesError`
  - `PlanningRegulationIndex`
  - `PlanningRegulationIndexError`
  - `PlanningRegulationSearchResult`
  - `PlanningRegulationStructureConfig`
  - `PlanningRegulationStructureError`
  - `PlanningRegulationStructureResult`
  - `PlanningZoningError`
  - `RoadProximityCoverageAssessmentResult`
  - `RoadProximityCoverageError`
  - `RoadProximityError`
  - `RoadProxyClassCoverage`
  - `ShapeDistributionProfile`
  - `ShapeEnrichmentError`
  - `ShapeProfileError`
  - `VoltageCoverageStatusProfile`
  - `VoltageLevelCoverage`
  - `VoltageLevelDistanceProfile`
  - `aggregate_bess_planning_feature_policy_to_parcels`
  - `apply_bess_planning_feature_policy`
  - `apply_ign_road_vehicle_proxy_policy`
  - `assess_grid_coverage`
  - `assess_road_proximity_coverage`
  - `compile_bess_planning_feature_policy`
  - `enrich_parcel_grid_proximity`
  - `enrich_parcel_road_proximity`
  - `enrich_parcel_shapes`
  - `filter_parcels_by_area`
  - `filter_parcels_by_shape`
  - `index_planning_regulation`
  - `interpret_bess_zoning`
  - `intersect_parcels_with_gpu_planning_features`
  - `intersect_parcels_with_gpu_zoning`
  - `load_bess_planning_feature_application_artifacts`
  - `load_bess_planning_feature_parcel_aggregation_artifacts`
  - `load_bess_planning_feature_policy_artifacts`
  - `load_bess_planning_feature_policy_config`
  - `load_bess_zoning_policy_config`
  - `load_cnig_feature_code_profile`
  - `load_ign_road_vehicle_proxy_policy`
  - `load_planning_regulation_structure_config`
  - `normalize_cadastre_parcels`
  - `normalize_ign_electricity`
  - `normalize_ign_roads`
  - `parse_ign_voltage`
  - `planning_regulation_section_page_fragments`
  - `profile_grid_coverage`
  - `profile_grid_proximity`
  - `profile_shape_distribution`
  - `resolve_planning_feature_codes`
  - `search_planning_regulation`
  - `structure_planning_regulation`
  - `validate_bess_planning_feature_application_result`
  - `validate_bess_planning_feature_application_result_envelope`
  - `validate_bess_planning_feature_parcel_aggregation_result`
  - `validate_bess_planning_feature_policy_result`
  - `validate_bess_planning_feature_policy_result_envelope`
  - `validate_bess_zoning_precheck`
  - `validate_normalized_planning_feature_inputs`
  - `validate_normalized_planning_zoning_inputs`
  - `validate_planning_feature_code_result`
  - `validate_planning_feature_code_result_envelope`
  - `validate_planning_regulation_index`
  - `validate_planning_regulation_search_result`
  - `validate_planning_regulation_structure`
  - `validate_planning_regulation_structure_with_fragments`


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

No top-level class/model/dataclass is declared.

## 6. Functions, methods, validators, fixtures, callbacks, and tests

No function or method is declared.

## 7. Validation and data-contract summary

- Canonical schema/mapping declarations inventoried above: none at module scope.
- Exact value/null/index/CRS/geometry/hash behavior is claimed only where the reproduced validators and operations enforce it.

## 8. Public exports and package ownership

Exact `__all__` members and local origins:

| Export | Local origin binding |
|---|---|
| `BessPlanningFeatureApplicationArtifactManifest` | `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactManifest` |
| `BessPlanningFeatureApplicationError` | `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationError` |
| `BessPlanningFeatureApplicationResult` | `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationResult` |
| `BessPlanningFeatureParcelAggregationArtifactManifest` | `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationArtifactManifest` |
| `BessPlanningFeatureParcelAggregationError` | `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationError` |
| `BessPlanningFeatureParcelAggregationResult` | `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationResult` |
| `BessPlanningFeaturePolicyArtifactManifest` | `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyArtifactManifest` |
| `BessPlanningFeaturePolicyConfig` | `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyConfig` |
| `BessPlanningFeaturePolicyError` | `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyError` |
| `BessPlanningFeaturePolicyResult` | `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyResult` |
| `BessZoningPolicyConfig` | `landscout.stages.interpret_bess_zoning.BessZoningPolicyConfig` |
| `BessZoningPrecheckError` | `landscout.stages.interpret_bess_zoning.BessZoningPrecheckError` |
| `BessZoningPrecheckResult` | `landscout.stages.interpret_bess_zoning.BessZoningPrecheckResult` |
| `BoundaryDistanceProfile` | `landscout.stages.assess_grid_coverage.BoundaryDistanceProfile` |
| `CadastreNormalizationError` | `landscout.stages.normalize_cadastre.CadastreNormalizationError` |
| `CnigFeatureCodeProfile` | `landscout.stages.resolve_planning_feature_codes.CnigFeatureCodeProfile` |
| `CoverageStatusCounts` | `landscout.stages.assess_grid_coverage.CoverageStatusCounts` |
| `DistanceProfile` | `landscout.stages.enrich_grid_proximity.DistanceProfile` |
| `GridCoverageAssessmentError` | `landscout.stages.assess_grid_coverage.GridCoverageAssessmentError` |
| `GridCoverageAssessmentResult` | `landscout.stages.assess_grid_coverage.GridCoverageAssessmentResult` |
| `GridCoverageProfile` | `landscout.stages.assess_grid_coverage.GridCoverageProfile` |
| `GridProximityError` | `landscout.stages.enrich_grid_proximity.GridProximityError` |
| `GridProximityProfile` | `landscout.stages.enrich_grid_proximity.GridProximityProfile` |
| `GridProximityResult` | `landscout.stages.enrich_grid_proximity.GridProximityResult` |
| `IgnGridNormalizationError` | `landscout.stages.normalize_grid_ign.IgnGridNormalizationError` |
| `IgnRoadNormalizationError` | `landscout.stages.normalize_access_ign.IgnRoadNormalizationError` |
| `IgnRoadVehicleProxyApplicationError` | `landscout.stages.apply_road_vehicle_proxy_policy.IgnRoadVehicleProxyApplicationError` |
| `IgnRoadVehicleProxyApplicationResult` | `landscout.stages.apply_road_vehicle_proxy_policy.IgnRoadVehicleProxyApplicationResult` |
| `IgnRoadVehicleProxyPolicy` | `landscout.stages.road_vehicle_proxy_policy.IgnRoadVehicleProxyPolicy` |
| `IgnRoadVehicleProxyPolicyError` | `landscout.stages.road_vehicle_proxy_policy.IgnRoadVehicleProxyPolicyError` |
| `IgnVoltageNormalization` | `landscout.stages.normalize_grid_ign.IgnVoltageNormalization` |
| `NormalizedIgnElectricityData` | `landscout.stages.normalize_grid_ign.NormalizedIgnElectricityData` |
| `NormalizedIgnRoadData` | `landscout.stages.normalize_access_ign.NormalizedIgnRoadData` |
| `ParcelFilterError` | `landscout.stages.filter_parcels.ParcelFilterError` |
| `ParcelPlanningFeaturesResult` | `landscout.stages.enrich_planning_features.ParcelPlanningFeaturesResult` |
| `ParcelRoadProximityResult` | `landscout.stages.enrich_road_proximity.ParcelRoadProximityResult` |
| `ParcelZoningResult` | `landscout.stages.enrich_planning_zoning.ParcelZoningResult` |
| `PlanningFeatureCodeError` | `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeError` |
| `PlanningFeatureCodeResult` | `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeResult` |
| `PlanningFeatureInputValidation` | `landscout.stages.enrich_planning_features.PlanningFeatureInputValidation` |
| `PlanningFeaturesError` | `landscout.stages.enrich_planning_features.PlanningFeaturesError` |
| `PlanningRegulationIndex` | `landscout.stages.index_planning_regulation.PlanningRegulationIndex` |
| `PlanningRegulationIndexError` | `landscout.stages.index_planning_regulation.PlanningRegulationIndexError` |
| `PlanningRegulationSearchResult` | `landscout.stages.index_planning_regulation.PlanningRegulationSearchResult` |
| `PlanningRegulationStructureConfig` | `landscout.stages.structure_planning_regulation.PlanningRegulationStructureConfig` |
| `PlanningRegulationStructureError` | `landscout.stages.structure_planning_regulation.PlanningRegulationStructureError` |
| `PlanningRegulationStructureResult` | `landscout.stages.structure_planning_regulation.PlanningRegulationStructureResult` |
| `PlanningZoningError` | `landscout.stages.enrich_planning_zoning.PlanningZoningError` |
| `RoadProximityCoverageAssessmentResult` | `landscout.stages.assess_road_proximity_coverage.RoadProximityCoverageAssessmentResult` |
| `RoadProximityCoverageError` | `landscout.stages.assess_road_proximity_coverage.RoadProximityCoverageError` |
| `RoadProximityError` | `landscout.stages.enrich_road_proximity.RoadProximityError` |
| `RoadProxyClassCoverage` | `landscout.stages.enrich_road_proximity.RoadProxyClassCoverage` |
| `ShapeDistributionProfile` | `landscout.stages.profile_shape.ShapeDistributionProfile` |
| `ShapeEnrichmentError` | `landscout.stages.enrich_shape.ShapeEnrichmentError` |
| `ShapeProfileError` | `landscout.stages.profile_shape.ShapeProfileError` |
| `VoltageCoverageStatusProfile` | `landscout.stages.assess_grid_coverage.VoltageCoverageStatusProfile` |
| `VoltageLevelCoverage` | `landscout.stages.enrich_grid_proximity.VoltageLevelCoverage` |
| `VoltageLevelDistanceProfile` | `landscout.stages.enrich_grid_proximity.VoltageLevelDistanceProfile` |
| `aggregate_bess_planning_feature_policy_to_parcels` | `landscout.stages.aggregate_bess_planning_feature_policy.aggregate_bess_planning_feature_policy_to_parcels` |
| `apply_bess_planning_feature_policy` | `landscout.stages.apply_bess_planning_feature_policy.apply_bess_planning_feature_policy` |
| `apply_ign_road_vehicle_proxy_policy` | `landscout.stages.apply_road_vehicle_proxy_policy.apply_ign_road_vehicle_proxy_policy` |
| `assess_grid_coverage` | `landscout.stages.assess_grid_coverage.assess_grid_coverage` |
| `assess_road_proximity_coverage` | `landscout.stages.assess_road_proximity_coverage.assess_road_proximity_coverage` |
| `compile_bess_planning_feature_policy` | `landscout.stages.bess_planning_feature_policy.compile_bess_planning_feature_policy` |
| `enrich_parcel_grid_proximity` | `landscout.stages.enrich_grid_proximity.enrich_parcel_grid_proximity` |
| `enrich_parcel_road_proximity` | `landscout.stages.enrich_road_proximity.enrich_parcel_road_proximity` |
| `enrich_parcel_shapes` | `landscout.stages.enrich_shape.enrich_parcel_shapes` |
| `filter_parcels_by_area` | `landscout.stages.filter_parcels.filter_parcels_by_area` |
| `filter_parcels_by_shape` | `landscout.stages.filter_parcels.filter_parcels_by_shape` |
| `index_planning_regulation` | `landscout.stages.index_planning_regulation.index_planning_regulation` |
| `interpret_bess_zoning` | `landscout.stages.interpret_bess_zoning.interpret_bess_zoning` |
| `intersect_parcels_with_gpu_planning_features` | `landscout.stages.enrich_planning_features.intersect_parcels_with_gpu_planning_features` |
| `intersect_parcels_with_gpu_zoning` | `landscout.stages.enrich_planning_zoning.intersect_parcels_with_gpu_zoning` |
| `load_bess_planning_feature_application_artifacts` | `landscout.stages.apply_bess_planning_feature_policy.load_bess_planning_feature_application_artifacts` |
| `load_bess_planning_feature_parcel_aggregation_artifacts` | `landscout.stages.aggregate_bess_planning_feature_policy.load_bess_planning_feature_parcel_aggregation_artifacts` |
| `load_bess_planning_feature_policy_artifacts` | `landscout.stages.bess_planning_feature_policy.load_bess_planning_feature_policy_artifacts` |
| `load_bess_planning_feature_policy_config` | `landscout.stages.bess_planning_feature_policy.load_bess_planning_feature_policy_config` |
| `load_bess_zoning_policy_config` | `landscout.stages.interpret_bess_zoning.load_bess_zoning_policy_config` |
| `load_cnig_feature_code_profile` | `landscout.stages.resolve_planning_feature_codes.load_cnig_feature_code_profile` |
| `load_ign_road_vehicle_proxy_policy` | `landscout.stages.road_vehicle_proxy_policy.load_ign_road_vehicle_proxy_policy` |
| `load_planning_regulation_structure_config` | `landscout.stages.structure_planning_regulation.load_planning_regulation_structure_config` |
| `normalize_cadastre_parcels` | `landscout.stages.normalize_cadastre.normalize_cadastre_parcels` |
| `normalize_ign_electricity` | `landscout.stages.normalize_grid_ign.normalize_ign_electricity` |
| `normalize_ign_roads` | `landscout.stages.normalize_access_ign.normalize_ign_roads` |
| `parse_ign_voltage` | `landscout.stages.normalize_grid_ign.parse_ign_voltage` |
| `planning_regulation_section_page_fragments` | `landscout.stages.structure_planning_regulation.planning_regulation_section_page_fragments` |
| `profile_grid_coverage` | `landscout.stages.assess_grid_coverage.profile_grid_coverage` |
| `profile_grid_proximity` | `landscout.stages.enrich_grid_proximity.profile_grid_proximity` |
| `profile_shape_distribution` | `landscout.stages.profile_shape.profile_shape_distribution` |
| `resolve_planning_feature_codes` | `landscout.stages.resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `search_planning_regulation` | `landscout.stages.index_planning_regulation.search_planning_regulation` |
| `structure_planning_regulation` | `landscout.stages.structure_planning_regulation.structure_planning_regulation` |
| `validate_bess_planning_feature_application_result` | `landscout.stages.apply_bess_planning_feature_policy.validate_bess_planning_feature_application_result` |
| `validate_bess_planning_feature_application_result_envelope` | `landscout.stages.apply_bess_planning_feature_policy.validate_bess_planning_feature_application_result_envelope` |
| `validate_bess_planning_feature_parcel_aggregation_result` | `landscout.stages.aggregate_bess_planning_feature_policy.validate_bess_planning_feature_parcel_aggregation_result` |
| `validate_bess_planning_feature_policy_result` | `landscout.stages.bess_planning_feature_policy.validate_bess_planning_feature_policy_result` |
| `validate_bess_planning_feature_policy_result_envelope` | `landscout.stages.bess_planning_feature_policy.validate_bess_planning_feature_policy_result_envelope` |
| `validate_bess_zoning_precheck` | `landscout.stages.interpret_bess_zoning.validate_bess_zoning_precheck` |
| `validate_normalized_planning_feature_inputs` | `landscout.stages.enrich_planning_features.validate_normalized_planning_feature_inputs` |
| `validate_normalized_planning_zoning_inputs` | `landscout.stages.enrich_planning_zoning.validate_normalized_planning_zoning_inputs` |
| `validate_planning_feature_code_result` | `landscout.stages.resolve_planning_feature_codes.validate_planning_feature_code_result` |
| `validate_planning_feature_code_result_envelope` | `landscout.stages.resolve_planning_feature_codes.validate_planning_feature_code_result_envelope` |
| `validate_planning_regulation_index` | `landscout.stages.index_planning_regulation.validate_planning_regulation_index` |
| `validate_planning_regulation_search_result` | `landscout.stages.index_planning_regulation.validate_planning_regulation_search_result` |
| `validate_planning_regulation_structure` | `landscout.stages.structure_planning_regulation.validate_planning_regulation_structure` |
| `validate_planning_regulation_structure_with_fragments` | `landscout.stages.structure_planning_regulation.validate_planning_regulation_structure_with_fragments` |

## 9. Trust, provenance, side effects, and business boundary

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.
- Configured identity, textual lineage, byte identity, physical source reconstruction, local envelope validation, and source-complete validation remain distinct trust levels. This companion attributes only the levels implemented in the exact source.
- Filesystem, network, hashing, CRS/geometry, process, mutation, and expected-exception evidence is listed per callable; an empty category is not silently promoted to an effect.

## 10. Change impact

A source-byte change invalidates the SHA above and requires re-auditing imports/re-exports, constants/aliases/schemas, model fields/immutability, qualified callers, side effects, controlled errors, tests, source/artifact locks, and the exact full snapshot.

## 11. Exact complete current file content

The following UTF-8 snapshot is the complete current repository file, not an excerpt. Its raw-byte SHA256 is the value in **File identity**.

```python
from landscout.stages.aggregate_bess_planning_feature_policy import (
    BessPlanningFeatureParcelAggregationArtifactManifest,
    BessPlanningFeatureParcelAggregationError,
    BessPlanningFeatureParcelAggregationResult,
    aggregate_bess_planning_feature_policy_to_parcels,
    load_bess_planning_feature_parcel_aggregation_artifacts,
    validate_bess_planning_feature_parcel_aggregation_result,
)
from landscout.stages.apply_bess_planning_feature_policy import (
    BessPlanningFeatureApplicationArtifactManifest,
    BessPlanningFeatureApplicationError,
    BessPlanningFeatureApplicationResult,
    apply_bess_planning_feature_policy,
    load_bess_planning_feature_application_artifacts,
    validate_bess_planning_feature_application_result,
    validate_bess_planning_feature_application_result_envelope,
)
from landscout.stages.apply_road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyApplicationError,
    IgnRoadVehicleProxyApplicationResult,
    apply_ign_road_vehicle_proxy_policy,
)
from landscout.stages.assess_grid_coverage import (
    BoundaryDistanceProfile,
    CoverageStatusCounts,
    GridCoverageAssessmentError,
    GridCoverageAssessmentResult,
    GridCoverageProfile,
    VoltageCoverageStatusProfile,
    assess_grid_coverage,
    profile_grid_coverage,
)
from landscout.stages.assess_road_proximity_coverage import (
    RoadProximityCoverageAssessmentResult,
    RoadProximityCoverageError,
    assess_road_proximity_coverage,
)
from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyArtifactManifest,
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyError,
    BessPlanningFeaturePolicyResult,
    compile_bess_planning_feature_policy,
    load_bess_planning_feature_policy_artifacts,
    load_bess_planning_feature_policy_config,
    validate_bess_planning_feature_policy_result,
    validate_bess_planning_feature_policy_result_envelope,
)
from landscout.stages.enrich_grid_proximity import (
    DistanceProfile,
    GridProximityError,
    GridProximityProfile,
    GridProximityResult,
    VoltageLevelCoverage,
    VoltageLevelDistanceProfile,
    enrich_parcel_grid_proximity,
    profile_grid_proximity,
)
from landscout.stages.enrich_planning_features import (
    ParcelPlanningFeaturesResult,
    PlanningFeatureInputValidation,
    PlanningFeaturesError,
    intersect_parcels_with_gpu_planning_features,
    validate_normalized_planning_feature_inputs,
)
from landscout.stages.enrich_planning_zoning import (
    ParcelZoningResult,
    PlanningZoningError,
    intersect_parcels_with_gpu_zoning,
    validate_normalized_planning_zoning_inputs,
)
from landscout.stages.enrich_road_proximity import (
    ParcelRoadProximityResult,
    RoadProximityError,
    RoadProxyClassCoverage,
    enrich_parcel_road_proximity,
)
from landscout.stages.enrich_shape import ShapeEnrichmentError, enrich_parcel_shapes
from landscout.stages.filter_parcels import (
    ParcelFilterError,
    filter_parcels_by_area,
    filter_parcels_by_shape,
)
from landscout.stages.index_planning_regulation import (
    PlanningRegulationIndex,
    PlanningRegulationIndexError,
    PlanningRegulationSearchResult,
    index_planning_regulation,
    search_planning_regulation,
    validate_planning_regulation_index,
    validate_planning_regulation_search_result,
)
from landscout.stages.interpret_bess_zoning import (
    BessZoningPolicyConfig,
    BessZoningPrecheckError,
    BessZoningPrecheckResult,
    interpret_bess_zoning,
    load_bess_zoning_policy_config,
    validate_bess_zoning_precheck,
)
from landscout.stages.normalize_access_ign import (
    IgnRoadNormalizationError,
    NormalizedIgnRoadData,
    normalize_ign_roads,
)
from landscout.stages.normalize_cadastre import (
    CadastreNormalizationError,
    normalize_cadastre_parcels,
)
from landscout.stages.normalize_grid_ign import (
    IgnGridNormalizationError,
    IgnVoltageNormalization,
    NormalizedIgnElectricityData,
    normalize_ign_electricity,
    parse_ign_voltage,
)
from landscout.stages.profile_shape import (
    ShapeDistributionProfile,
    ShapeProfileError,
    profile_shape_distribution,
)
from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeError,
    PlanningFeatureCodeResult,
    load_cnig_feature_code_profile,
    resolve_planning_feature_codes,
    validate_planning_feature_code_result,
    validate_planning_feature_code_result_envelope,
)
from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    IgnRoadVehicleProxyPolicyError,
    load_ign_road_vehicle_proxy_policy,
)
from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureError,
    PlanningRegulationStructureResult,
    load_planning_regulation_structure_config,
    planning_regulation_section_page_fragments,
    structure_planning_regulation,
    validate_planning_regulation_structure,
    validate_planning_regulation_structure_with_fragments,
)

__all__ = [
    "BessPlanningFeatureApplicationArtifactManifest",
    "BessPlanningFeatureApplicationError",
    "BessPlanningFeatureApplicationResult",
    "BessPlanningFeatureParcelAggregationArtifactManifest",
    "BessPlanningFeatureParcelAggregationError",
    "BessPlanningFeatureParcelAggregationResult",
    "BessPlanningFeaturePolicyArtifactManifest",
    "BessPlanningFeaturePolicyConfig",
    "BessPlanningFeaturePolicyError",
    "BessPlanningFeaturePolicyResult",
    "BessZoningPolicyConfig",
    "BessZoningPrecheckError",
    "BessZoningPrecheckResult",
    "BoundaryDistanceProfile",
    "CadastreNormalizationError",
    "CnigFeatureCodeProfile",
    "CoverageStatusCounts",
    "DistanceProfile",
    "GridCoverageAssessmentError",
    "GridCoverageAssessmentResult",
    "GridCoverageProfile",
    "GridProximityError",
    "GridProximityProfile",
    "GridProximityResult",
    "IgnGridNormalizationError",
    "IgnRoadNormalizationError",
    "IgnRoadVehicleProxyApplicationError",
    "IgnRoadVehicleProxyApplicationResult",
    "IgnRoadVehicleProxyPolicy",
    "IgnRoadVehicleProxyPolicyError",
    "IgnVoltageNormalization",
    "NormalizedIgnElectricityData",
    "NormalizedIgnRoadData",
    "ParcelFilterError",
    "ParcelPlanningFeaturesResult",
    "ParcelRoadProximityResult",
    "ParcelZoningResult",
    "PlanningFeatureCodeError",
    "PlanningFeatureCodeResult",
    "PlanningFeatureInputValidation",
    "PlanningFeaturesError",
    "PlanningRegulationIndex",
    "PlanningRegulationIndexError",
    "PlanningRegulationSearchResult",
    "PlanningRegulationStructureConfig",
    "PlanningRegulationStructureError",
    "PlanningRegulationStructureResult",
    "PlanningZoningError",
    "RoadProximityCoverageAssessmentResult",
    "RoadProximityCoverageError",
    "RoadProximityError",
    "RoadProxyClassCoverage",
    "ShapeDistributionProfile",
    "ShapeEnrichmentError",
    "ShapeProfileError",
    "VoltageCoverageStatusProfile",
    "VoltageLevelCoverage",
    "VoltageLevelDistanceProfile",
    "aggregate_bess_planning_feature_policy_to_parcels",
    "apply_bess_planning_feature_policy",
    "apply_ign_road_vehicle_proxy_policy",
    "assess_grid_coverage",
    "assess_road_proximity_coverage",
    "compile_bess_planning_feature_policy",
    "enrich_parcel_grid_proximity",
    "enrich_parcel_road_proximity",
    "enrich_parcel_shapes",
    "filter_parcels_by_area",
    "filter_parcels_by_shape",
    "index_planning_regulation",
    "interpret_bess_zoning",
    "intersect_parcels_with_gpu_planning_features",
    "intersect_parcels_with_gpu_zoning",
    "load_bess_planning_feature_application_artifacts",
    "load_bess_planning_feature_parcel_aggregation_artifacts",
    "load_bess_planning_feature_policy_artifacts",
    "load_bess_planning_feature_policy_config",
    "load_bess_zoning_policy_config",
    "load_cnig_feature_code_profile",
    "load_ign_road_vehicle_proxy_policy",
    "load_planning_regulation_structure_config",
    "normalize_cadastre_parcels",
    "normalize_ign_electricity",
    "normalize_ign_roads",
    "parse_ign_voltage",
    "planning_regulation_section_page_fragments",
    "profile_grid_coverage",
    "profile_grid_proximity",
    "profile_shape_distribution",
    "resolve_planning_feature_codes",
    "search_planning_regulation",
    "structure_planning_regulation",
    "validate_bess_planning_feature_application_result",
    "validate_bess_planning_feature_application_result_envelope",
    "validate_bess_planning_feature_parcel_aggregation_result",
    "validate_bess_planning_feature_policy_result",
    "validate_bess_planning_feature_policy_result_envelope",
    "validate_bess_zoning_precheck",
    "validate_normalized_planning_feature_inputs",
    "validate_normalized_planning_zoning_inputs",
    "validate_planning_feature_code_result",
    "validate_planning_feature_code_result_envelope",
    "validate_planning_regulation_index",
    "validate_planning_regulation_search_result",
    "validate_planning_regulation_structure",
    "validate_planning_regulation_structure_with_fragments",
]
```
