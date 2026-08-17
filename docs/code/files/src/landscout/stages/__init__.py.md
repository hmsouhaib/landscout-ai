# `src/landscout/stages/__init__.py`

## File identity

- Repository path: `src/landscout/stages/__init__.py`
- File type: Python source
- Layer: processing/policy stage
- Domain: project
- Responsibility: Re-exports stable stage result, error, loader, validator, and transformation APIs.
- Source SHA256: `486c673828a9bdc77ca594316d86e3ab8b026cda42dec33326dc8f6dc12f28d5`

## 1. Purpose

Re-exports stable stage result, error, loader, validator, and transformation APIs.

## 2. Position in LandScout architecture

This file belongs to the **processing/policy stage** layer and the **project** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `None.`

### Third-party packages

- `None.`

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

### A. Python constants

No meaningful module constant is declared.

### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

- `__all__` — explicit public export allow-list.
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


### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

No class/model/dataclass is declared.

## 6. Functions and methods

No function or method is declared.

## 7. Data contracts

No module-level canonical frame schema, mapping, or dtype declaration is present. Any frame interaction is recoverable from the complete function implementations below; no string literal is promoted to a column merely because it appears in code.

No enum/status/Literal value is classified as a column unless it is separately present in a canonical schema declaration. Mapping keys, JSON keys, dataclass fields, and configuration leaves remain distinct categories.

## 8. Interfaces

This module defines an exact `__all__` contract:

| Export | Kind | Origin | Included in `__all__` |
|---|---|---|---|
| `BessPlanningFeatureApplicationArtifactManifest` | re-exported/defined Python symbol | `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactManifest` | yes |
| `BessPlanningFeatureApplicationError` | re-exported/defined Python symbol | `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationError` | yes |
| `BessPlanningFeatureApplicationResult` | re-exported/defined Python symbol | `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationResult` | yes |
| `BessPlanningFeatureParcelAggregationArtifactManifest` | re-exported/defined Python symbol | `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationArtifactManifest` | yes |
| `BessPlanningFeatureParcelAggregationError` | re-exported/defined Python symbol | `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationError` | yes |
| `BessPlanningFeatureParcelAggregationResult` | re-exported/defined Python symbol | `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationResult` | yes |
| `BessPlanningFeaturePolicyArtifactManifest` | re-exported/defined Python symbol | `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyArtifactManifest` | yes |
| `BessPlanningFeaturePolicyConfig` | re-exported/defined Python symbol | `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyConfig` | yes |
| `BessPlanningFeaturePolicyError` | re-exported/defined Python symbol | `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyError` | yes |
| `BessPlanningFeaturePolicyResult` | re-exported/defined Python symbol | `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyResult` | yes |
| `BessZoningPolicyConfig` | re-exported/defined Python symbol | `landscout.stages.interpret_bess_zoning.BessZoningPolicyConfig` | yes |
| `BessZoningPrecheckError` | re-exported/defined Python symbol | `landscout.stages.interpret_bess_zoning.BessZoningPrecheckError` | yes |
| `BessZoningPrecheckResult` | re-exported/defined Python symbol | `landscout.stages.interpret_bess_zoning.BessZoningPrecheckResult` | yes |
| `BoundaryDistanceProfile` | re-exported/defined Python symbol | `landscout.stages.assess_grid_coverage.BoundaryDistanceProfile` | yes |
| `CadastreNormalizationError` | re-exported/defined Python symbol | `landscout.stages.normalize_cadastre.CadastreNormalizationError` | yes |
| `CnigFeatureCodeProfile` | re-exported/defined Python symbol | `landscout.stages.resolve_planning_feature_codes.CnigFeatureCodeProfile` | yes |
| `CoverageStatusCounts` | re-exported/defined Python symbol | `landscout.stages.assess_grid_coverage.CoverageStatusCounts` | yes |
| `DistanceProfile` | re-exported/defined Python symbol | `landscout.stages.enrich_grid_proximity.DistanceProfile` | yes |
| `GridCoverageAssessmentError` | re-exported/defined Python symbol | `landscout.stages.assess_grid_coverage.GridCoverageAssessmentError` | yes |
| `GridCoverageAssessmentResult` | re-exported/defined Python symbol | `landscout.stages.assess_grid_coverage.GridCoverageAssessmentResult` | yes |
| `GridCoverageProfile` | re-exported/defined Python symbol | `landscout.stages.assess_grid_coverage.GridCoverageProfile` | yes |
| `GridProximityError` | re-exported/defined Python symbol | `landscout.stages.enrich_grid_proximity.GridProximityError` | yes |
| `GridProximityProfile` | re-exported/defined Python symbol | `landscout.stages.enrich_grid_proximity.GridProximityProfile` | yes |
| `GridProximityResult` | re-exported/defined Python symbol | `landscout.stages.enrich_grid_proximity.GridProximityResult` | yes |
| `IgnGridNormalizationError` | re-exported/defined Python symbol | `landscout.stages.normalize_grid_ign.IgnGridNormalizationError` | yes |
| `IgnRoadNormalizationError` | re-exported/defined Python symbol | `landscout.stages.normalize_access_ign.IgnRoadNormalizationError` | yes |
| `IgnRoadVehicleProxyApplicationError` | re-exported/defined Python symbol | `landscout.stages.apply_road_vehicle_proxy_policy.IgnRoadVehicleProxyApplicationError` | yes |
| `IgnRoadVehicleProxyApplicationResult` | re-exported/defined Python symbol | `landscout.stages.apply_road_vehicle_proxy_policy.IgnRoadVehicleProxyApplicationResult` | yes |
| `IgnRoadVehicleProxyPolicy` | re-exported/defined Python symbol | `landscout.stages.road_vehicle_proxy_policy.IgnRoadVehicleProxyPolicy` | yes |
| `IgnRoadVehicleProxyPolicyError` | re-exported/defined Python symbol | `landscout.stages.road_vehicle_proxy_policy.IgnRoadVehicleProxyPolicyError` | yes |
| `IgnVoltageNormalization` | re-exported/defined Python symbol | `landscout.stages.normalize_grid_ign.IgnVoltageNormalization` | yes |
| `NormalizedIgnElectricityData` | re-exported/defined Python symbol | `landscout.stages.normalize_grid_ign.NormalizedIgnElectricityData` | yes |
| `NormalizedIgnRoadData` | re-exported/defined Python symbol | `landscout.stages.normalize_access_ign.NormalizedIgnRoadData` | yes |
| `ParcelFilterError` | re-exported/defined Python symbol | `landscout.stages.filter_parcels.ParcelFilterError` | yes |
| `ParcelPlanningFeaturesResult` | re-exported/defined Python symbol | `landscout.stages.enrich_planning_features.ParcelPlanningFeaturesResult` | yes |
| `ParcelRoadProximityResult` | re-exported/defined Python symbol | `landscout.stages.enrich_road_proximity.ParcelRoadProximityResult` | yes |
| `PlanningFeatureCodeError` | re-exported/defined Python symbol | `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeError` | yes |
| `PlanningFeatureCodeResult` | re-exported/defined Python symbol | `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeResult` | yes |
| `PlanningFeatureInputValidation` | re-exported/defined Python symbol | `landscout.stages.enrich_planning_features.PlanningFeatureInputValidation` | yes |
| `PlanningFeaturesError` | re-exported/defined Python symbol | `landscout.stages.enrich_planning_features.PlanningFeaturesError` | yes |
| `PlanningRegulationIndex` | re-exported/defined Python symbol | `landscout.stages.index_planning_regulation.PlanningRegulationIndex` | yes |
| `PlanningRegulationIndexError` | re-exported/defined Python symbol | `landscout.stages.index_planning_regulation.PlanningRegulationIndexError` | yes |
| `PlanningRegulationSearchResult` | re-exported/defined Python symbol | `landscout.stages.index_planning_regulation.PlanningRegulationSearchResult` | yes |
| `PlanningRegulationStructureConfig` | re-exported/defined Python symbol | `landscout.stages.structure_planning_regulation.PlanningRegulationStructureConfig` | yes |
| `PlanningRegulationStructureError` | re-exported/defined Python symbol | `landscout.stages.structure_planning_regulation.PlanningRegulationStructureError` | yes |
| `PlanningRegulationStructureResult` | re-exported/defined Python symbol | `landscout.stages.structure_planning_regulation.PlanningRegulationStructureResult` | yes |
| `RoadProximityCoverageAssessmentResult` | re-exported/defined Python symbol | `landscout.stages.assess_road_proximity_coverage.RoadProximityCoverageAssessmentResult` | yes |
| `RoadProximityCoverageError` | re-exported/defined Python symbol | `landscout.stages.assess_road_proximity_coverage.RoadProximityCoverageError` | yes |
| `RoadProximityError` | re-exported/defined Python symbol | `landscout.stages.enrich_road_proximity.RoadProximityError` | yes |
| `RoadProxyClassCoverage` | re-exported/defined Python symbol | `landscout.stages.enrich_road_proximity.RoadProxyClassCoverage` | yes |
| `ShapeDistributionProfile` | re-exported/defined Python symbol | `landscout.stages.profile_shape.ShapeDistributionProfile` | yes |
| `ShapeEnrichmentError` | re-exported/defined Python symbol | `landscout.stages.enrich_shape.ShapeEnrichmentError` | yes |
| `ShapeProfileError` | re-exported/defined Python symbol | `landscout.stages.profile_shape.ShapeProfileError` | yes |
| `VoltageCoverageStatusProfile` | re-exported/defined Python symbol | `landscout.stages.assess_grid_coverage.VoltageCoverageStatusProfile` | yes |
| `VoltageLevelCoverage` | re-exported/defined Python symbol | `landscout.stages.enrich_grid_proximity.VoltageLevelCoverage` | yes |
| `VoltageLevelDistanceProfile` | re-exported/defined Python symbol | `landscout.stages.enrich_grid_proximity.VoltageLevelDistanceProfile` | yes |
| `aggregate_bess_planning_feature_policy_to_parcels` | re-exported/defined Python symbol | `landscout.stages.aggregate_bess_planning_feature_policy.aggregate_bess_planning_feature_policy_to_parcels` | yes |
| `apply_bess_planning_feature_policy` | re-exported/defined Python symbol | `landscout.stages.apply_bess_planning_feature_policy.apply_bess_planning_feature_policy` | yes |
| `apply_ign_road_vehicle_proxy_policy` | re-exported/defined Python symbol | `landscout.stages.apply_road_vehicle_proxy_policy.apply_ign_road_vehicle_proxy_policy` | yes |
| `assess_grid_coverage` | re-exported/defined Python symbol | `landscout.stages.assess_grid_coverage.assess_grid_coverage` | yes |
| `assess_road_proximity_coverage` | re-exported/defined Python symbol | `landscout.stages.assess_road_proximity_coverage.assess_road_proximity_coverage` | yes |
| `compile_bess_planning_feature_policy` | re-exported/defined Python symbol | `landscout.stages.bess_planning_feature_policy.compile_bess_planning_feature_policy` | yes |
| `enrich_parcel_grid_proximity` | re-exported/defined Python symbol | `landscout.stages.enrich_grid_proximity.enrich_parcel_grid_proximity` | yes |
| `enrich_parcel_road_proximity` | re-exported/defined Python symbol | `landscout.stages.enrich_road_proximity.enrich_parcel_road_proximity` | yes |
| `enrich_parcel_shapes` | re-exported/defined Python symbol | `landscout.stages.enrich_shape.enrich_parcel_shapes` | yes |
| `filter_parcels_by_area` | re-exported/defined Python symbol | `landscout.stages.filter_parcels.filter_parcels_by_area` | yes |
| `filter_parcels_by_shape` | re-exported/defined Python symbol | `landscout.stages.filter_parcels.filter_parcels_by_shape` | yes |
| `index_planning_regulation` | re-exported/defined Python symbol | `landscout.stages.index_planning_regulation.index_planning_regulation` | yes |
| `interpret_bess_zoning` | re-exported/defined Python symbol | `landscout.stages.interpret_bess_zoning.interpret_bess_zoning` | yes |
| `intersect_parcels_with_gpu_planning_features` | re-exported/defined Python symbol | `landscout.stages.enrich_planning_features.intersect_parcels_with_gpu_planning_features` | yes |
| `intersect_parcels_with_gpu_zoning` | re-exported/defined Python symbol | `landscout.stages.enrich_planning_zoning.intersect_parcels_with_gpu_zoning` | yes |
| `load_bess_planning_feature_application_artifacts` | re-exported/defined Python symbol | `landscout.stages.apply_bess_planning_feature_policy.load_bess_planning_feature_application_artifacts` | yes |
| `load_bess_planning_feature_parcel_aggregation_artifacts` | re-exported/defined Python symbol | `landscout.stages.aggregate_bess_planning_feature_policy.load_bess_planning_feature_parcel_aggregation_artifacts` | yes |
| `load_bess_planning_feature_policy_artifacts` | re-exported/defined Python symbol | `landscout.stages.bess_planning_feature_policy.load_bess_planning_feature_policy_artifacts` | yes |
| `load_bess_planning_feature_policy_config` | re-exported/defined Python symbol | `landscout.stages.bess_planning_feature_policy.load_bess_planning_feature_policy_config` | yes |
| `load_bess_zoning_policy_config` | re-exported/defined Python symbol | `landscout.stages.interpret_bess_zoning.load_bess_zoning_policy_config` | yes |
| `load_cnig_feature_code_profile` | re-exported/defined Python symbol | `landscout.stages.resolve_planning_feature_codes.load_cnig_feature_code_profile` | yes |
| `load_ign_road_vehicle_proxy_policy` | re-exported/defined Python symbol | `landscout.stages.road_vehicle_proxy_policy.load_ign_road_vehicle_proxy_policy` | yes |
| `load_planning_regulation_structure_config` | re-exported/defined Python symbol | `landscout.stages.structure_planning_regulation.load_planning_regulation_structure_config` | yes |
| `normalize_cadastre_parcels` | re-exported/defined Python symbol | `landscout.stages.normalize_cadastre.normalize_cadastre_parcels` | yes |
| `normalize_ign_electricity` | re-exported/defined Python symbol | `landscout.stages.normalize_grid_ign.normalize_ign_electricity` | yes |
| `normalize_ign_roads` | re-exported/defined Python symbol | `landscout.stages.normalize_access_ign.normalize_ign_roads` | yes |
| `parse_ign_voltage` | re-exported/defined Python symbol | `landscout.stages.normalize_grid_ign.parse_ign_voltage` | yes |
| `planning_regulation_section_page_fragments` | re-exported/defined Python symbol | `landscout.stages.structure_planning_regulation.planning_regulation_section_page_fragments` | yes |
| `profile_grid_coverage` | re-exported/defined Python symbol | `landscout.stages.assess_grid_coverage.profile_grid_coverage` | yes |
| `profile_grid_proximity` | re-exported/defined Python symbol | `landscout.stages.enrich_grid_proximity.profile_grid_proximity` | yes |
| `profile_shape_distribution` | re-exported/defined Python symbol | `landscout.stages.profile_shape.profile_shape_distribution` | yes |
| `resolve_planning_feature_codes` | re-exported/defined Python symbol | `landscout.stages.resolve_planning_feature_codes.resolve_planning_feature_codes` | yes |
| `search_planning_regulation` | re-exported/defined Python symbol | `landscout.stages.index_planning_regulation.search_planning_regulation` | yes |
| `structure_planning_regulation` | re-exported/defined Python symbol | `landscout.stages.structure_planning_regulation.structure_planning_regulation` | yes |
| `validate_bess_planning_feature_application_result` | re-exported/defined Python symbol | `landscout.stages.apply_bess_planning_feature_policy.validate_bess_planning_feature_application_result` | yes |
| `validate_bess_planning_feature_application_result_envelope` | re-exported/defined Python symbol | `landscout.stages.apply_bess_planning_feature_policy.validate_bess_planning_feature_application_result_envelope` | yes |
| `validate_bess_planning_feature_parcel_aggregation_result` | re-exported/defined Python symbol | `landscout.stages.aggregate_bess_planning_feature_policy.validate_bess_planning_feature_parcel_aggregation_result` | yes |
| `validate_bess_planning_feature_policy_result` | re-exported/defined Python symbol | `landscout.stages.bess_planning_feature_policy.validate_bess_planning_feature_policy_result` | yes |
| `validate_bess_planning_feature_policy_result_envelope` | re-exported/defined Python symbol | `landscout.stages.bess_planning_feature_policy.validate_bess_planning_feature_policy_result_envelope` | yes |
| `validate_bess_zoning_precheck` | re-exported/defined Python symbol | `landscout.stages.interpret_bess_zoning.validate_bess_zoning_precheck` | yes |
| `validate_normalized_planning_feature_inputs` | re-exported/defined Python symbol | `landscout.stages.enrich_planning_features.validate_normalized_planning_feature_inputs` | yes |
| `validate_normalized_planning_zoning_inputs` | re-exported/defined Python symbol | `landscout.stages.enrich_planning_zoning.validate_normalized_planning_zoning_inputs` | yes |
| `validate_planning_feature_code_result` | re-exported/defined Python symbol | `landscout.stages.resolve_planning_feature_codes.validate_planning_feature_code_result` | yes |
| `validate_planning_feature_code_result_envelope` | re-exported/defined Python symbol | `landscout.stages.resolve_planning_feature_codes.validate_planning_feature_code_result_envelope` | yes |
| `validate_planning_regulation_index` | re-exported/defined Python symbol | `landscout.stages.index_planning_regulation.validate_planning_regulation_index` | yes |
| `validate_planning_regulation_search_result` | re-exported/defined Python symbol | `landscout.stages.index_planning_regulation.validate_planning_regulation_search_result` | yes |
| `validate_planning_regulation_structure` | re-exported/defined Python symbol | `landscout.stages.structure_planning_regulation.validate_planning_regulation_structure` | yes |
| `validate_planning_regulation_structure_with_fragments` | re-exported/defined Python symbol | `landscout.stages.structure_planning_regulation.validate_planning_regulation_structure_with_fragments` | yes |

## 9. Error handling

Controlled exceptions, local raise guards, delegated validators, and framework assertions are documented per exact function implementation. No broader error guarantee is inferred.

## 10. Side effects

Network I/O, filesystem reads/writes, in-memory mutation, input mutation, geometry/CRS calculations, hashing, and process/environment effects are listed separately for every function.

## 11. Security / trust boundaries

Textual URL/provider/hash fields are provenance claims, not physical proof. Physical proof exists only where the reproduced implementation revalidates transport, bytes, archive structure, source layers, geometry, or result hashes.


## 12. GIS / CRS rules

Only the explicit CRS/geometry validators and calculation copies in this module establish GIS behavior. No geometry repair, reprojection, or metric meaning is inferred from a field name alone.

## 13. Provenance rules

Configured identity, row lineage, byte identity, cache metadata, and source-complete revalidation are separate levels. This companion claims only the levels implemented above.

## 14. Business meaning

The module contributes to the project flow through the exact facts, proxy evidence, policy results, diagnostics, or prechecks identified above.

## 15. Explicit non-goals

- Project/configuration metadata does not itself measure parcels, acquire source bytes, apply policy, rank land, or produce a legal conclusion.

## 16. Tests

Test consumers and framework invocation are included in per-symbol interfaces. Test modules distinguish fixture injection from parameterized values and reproduce setup/action/assertion source.

## 17. Change impact

Any source-byte change invalidates the SHA above. Review exact exports, aliases, canonical frame schemas/dtypes, configured source/policy identities, callers, framework hooks, artifacts, and all linked tests before updating this companion.
