# `configs/access/ign_bdtopo_vehicle_proxy_policy.yaml`

## File identity

- Repository path: `configs/access/ign_bdtopo_vehicle_proxy_policy.yaml`
- File type: YAML checked-in configuration/policy/source lock
- Responsibility: Defines the approved versioned IGN general-car/light-vehicle evidence policy, source references, vocabularies, outcomes, and exact precedence.
- Source SHA256: `2092bc620063ec1176b2abebaefafcc108a42793992dd18f869d44fdb07ca166`

## 1. Purpose

Defines the approved versioned IGN general-car/light-vehicle evidence policy, source references, vocabularies, outcomes, and exact precedence.

## 2. Position in LandScout architecture

The exact YAML bytes are parsed by `landscout.stages.road_vehicle_proxy_policy.load_ign_road_vehicle_proxy_policy` into `landscout.stages.road_vehicle_proxy_policy.IgnRoadVehicleProxyPolicy`. Runtime consumers include `apply_ign_road_vehicle_proxy_policy`.

## 3. Imports and dependencies

Not applicable to YAML. Python/Pydantic consumers are named above and reproduced below.

## 4. Contract taxonomy

Every row below is a configuration field/list leaf. It is not a DataFrame column unless a consuming stage explicitly copies it into a documented result schema.

| Exact YAML path | Checked-in value | Runtime type | Required/nullability/allowed-domain/unit contract | Semantic role | Consumers |
|---|---|---|---|---|---|
| `policy_id` | `"ign_bdtopo_general_vehicle_proxy_v2"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Identifies the compiled policy lineage propagated to result rows. | `apply_ign_road_vehicle_proxy_policy` |
| `schema_version` | `2` | `int` | path is a mapping key/list member validated by the enclosing model and validators; required supported schema integer; accepted versions are pinned by the owning Literal/validator | Selects the strict configuration schema; unsupported versions are rejected. | `apply_ign_road_vehicle_proxy_policy` |
| `scope` | `"OFFICIAL_IGN_CAR_ROUTING_EVIDENCE_ONLY"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `scope` under the exact parent path `<root>`. | `apply_ign_road_vehicle_proxy_policy` |
| `references.navigation.publisher` | `"IGN"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `publisher` under the exact parent path `references.navigation`. | `apply_ign_road_vehicle_proxy_policy` |
| `references.navigation.title` | `"Calcul d’itinéraire"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `title` under the exact parent path `references.navigation`. | `apply_ign_road_vehicle_proxy_policy` |
| `references.navigation.revision` | `"2026-05-27"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `revision` under the exact parent path `references.navigation`. | `apply_ign_road_vehicle_proxy_policy` |
| `references.navigation.evidence_scope` | `"GENERAL_CAR_ROUTING_RULES"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence scope` under the exact parent path `references.navigation`. | `apply_ign_road_vehicle_proxy_policy` |
| `references.bdtopo_product.publisher` | `"IGN"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `publisher` under the exact parent path `references.bdtopo_product`. | `apply_ign_road_vehicle_proxy_policy` |
| `references.bdtopo_product.title` | `"BD TOPO® Version 3.5 - Descriptif de contenu"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `title` under the exact parent path `references.bdtopo_product`. | `apply_ign_road_vehicle_proxy_policy` |
| `references.bdtopo_product.document_id` | `"DC_BDTOPO_3-5"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `document id` under the exact parent path `references.bdtopo_product`. | `apply_ign_road_vehicle_proxy_policy` |
| `references.bdtopo_product.revision` | `"2025-11"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `revision` under the exact parent path `references.bdtopo_product`. | `apply_ign_road_vehicle_proxy_policy` |
| `references.bdtopo_product.evidence_scope` | `"SOURCE_ATTRIBUTE_SEMANTICS"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence scope` under the exact parent path `references.bdtopo_product`. | `apply_ign_road_vehicle_proxy_policy` |
| `evidence_checked_on` | `"2026-08-16"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence checked on` under the exact parent path `<root>`. | `apply_ign_road_vehicle_proxy_policy` |
| `vehicle_scope` | `"LIGHT_VEHICLE_AND_GENERAL_CAR_NETWORK"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `vehicle scope` under the exact parent path `<root>`. | `apply_ign_road_vehicle_proxy_policy` |
| `heavy_vehicle_access` | `"NOT_PROVEN"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `heavy vehicle access` under the exact parent path `<root>`. | `apply_ign_road_vehicle_proxy_policy` |
| `classes.general_vehicle_proxy` | `"GENERAL_VEHICLE_PROXY"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `general vehicle proxy` under the exact parent path `classes`. | `apply_ign_road_vehicle_proxy_policy` |
| `classes.limited_vehicle_proxy` | `"LIMITED_VEHICLE_PROXY"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `limited vehicle proxy` under the exact parent path `classes`. | `apply_ign_road_vehicle_proxy_policy` |
| `classes.restricted_review` | `"RESTRICTED_REVIEW"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `restricted review` under the exact parent path `classes`. | `apply_ign_road_vehicle_proxy_policy` |
| `classes.not_general_vehicle_proxy` | `"NOT_GENERAL_VEHICLE_PROXY"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `not general vehicle proxy` under the exact parent path `classes`. | `apply_ign_road_vehicle_proxy_policy` |
| `classes.not_distance_proxy` | `"NOT_DISTANCE_PROXY"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `not distance proxy` under the exact parent path `classes`. | `apply_ign_road_vehicle_proxy_policy` |
| `classes.unknown_review` | `"UNKNOWN_REVIEW"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `unknown review` under the exact parent path `classes`. | `apply_ign_road_vehicle_proxy_policy` |
| `source_values.asset_state.in_service[0]` | `"En service"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `source_values.asset_state.in_service`; order and uniqueness are validated/consumed where required. | `apply_ign_road_vehicle_proxy_policy` |
| `source_values.asset_state.project_geometry_not_significant[0]` | `"En projet"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `source_values.asset_state.project_geometry_not_significant`; order and uniqueness are validated/consumed where required. | `apply_ign_road_vehicle_proxy_policy` |
| `source_values.asset_state.under_construction[0]` | `"En construction"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `source_values.asset_state.under_construction`; order and uniqueness are validated/consumed where required. | `apply_ign_road_vehicle_proxy_policy` |
| `source_values.light_vehicle_access.open[0]` | `"Libre"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `source_values.light_vehicle_access.open`; order and uniqueness are validated/consumed where required. | `apply_ign_road_vehicle_proxy_policy` |
| `source_values.light_vehicle_access.toll[0]` | `"A péage"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `source_values.light_vehicle_access.toll`; order and uniqueness are validated/consumed where required. | `apply_ign_road_vehicle_proxy_policy` |
| `source_values.light_vehicle_access.rights_restricted[0]` | `"Restreint aux ayants droit"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `source_values.light_vehicle_access.rights_restricted`; order and uniqueness are validated/consumed where required. | `apply_ign_road_vehicle_proxy_policy` |
| `source_values.light_vehicle_access.physically_impossible[0]` | `"Physiquement impossible"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `source_values.light_vehicle_access.physically_impossible`; order and uniqueness are validated/consumed where required. | `apply_ign_road_vehicle_proxy_policy` |
| `source_values.nature.general_motor_road[0]` | `"Route à 1 chaussée"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `source_values.nature.general_motor_road`; order and uniqueness are validated/consumed where required. | `apply_ign_road_vehicle_proxy_policy` |
| `source_values.nature.general_motor_road[1]` | `"Route à 2 chaussées"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `source_values.nature.general_motor_road`; order and uniqueness are validated/consumed where required. | `apply_ign_road_vehicle_proxy_policy` |
| `source_values.nature.general_motor_road[2]` | `"Rond-point"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `source_values.nature.general_motor_road`; order and uniqueness are validated/consumed where required. | `apply_ign_road_vehicle_proxy_policy` |
| `source_values.nature.general_motor_road[3]` | `"Bretelle"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `source_values.nature.general_motor_road`; order and uniqueness are validated/consumed where required. | `apply_ign_road_vehicle_proxy_policy` |
| `source_values.nature.general_motor_road[4]` | `"Type autoroutier"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `source_values.nature.general_motor_road`; order and uniqueness are validated/consumed where required. | `apply_ign_road_vehicle_proxy_policy` |
| `source_values.nature.limited_motor_proxy[0]` | `"Route empierrée"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `source_values.nature.limited_motor_proxy`; order and uniqueness are validated/consumed where required. | `apply_ign_road_vehicle_proxy_policy` |
| `source_values.nature.limited_motor_proxy[1]` | `"Chemin"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `source_values.nature.limited_motor_proxy`; order and uniqueness are validated/consumed where required. | `apply_ign_road_vehicle_proxy_policy` |
| `source_values.nature.non_general_vehicle[0]` | `"Escalier"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `source_values.nature.non_general_vehicle`; order and uniqueness are validated/consumed where required. | `apply_ign_road_vehicle_proxy_policy` |
| `source_values.nature.non_general_vehicle[1]` | `"Sentier"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `source_values.nature.non_general_vehicle`; order and uniqueness are validated/consumed where required. | `apply_ign_road_vehicle_proxy_policy` |
| `source_values.nature.non_general_vehicle[2]` | `"Piste cyclable"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `source_values.nature.non_general_vehicle`; order and uniqueness are validated/consumed where required. | `apply_ign_road_vehicle_proxy_policy` |
| `source_values.nature.special_review[0]` | `"Bac ou liaison maritime"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `source_values.nature.special_review`; order and uniqueness are validated/consumed where required. | `apply_ign_road_vehicle_proxy_policy` |
| `source_values.known_restriction_review[0]` | `"Plot amovible"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `source_values.known_restriction_review`; order and uniqueness are validated/consumed where required. | `apply_ign_road_vehicle_proxy_policy` |
| `source_values.known_restriction_review[1]` | `"Voie de tramway utilisable par les véhicules de secours"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `source_values.known_restriction_review`; order and uniqueness are validated/consumed where required. | `apply_ign_road_vehicle_proxy_policy` |
| `source_values.known_restriction_review[2]` | `"Voie verte"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `source_values.known_restriction_review`; order and uniqueness are validated/consumed where required. | `apply_ign_road_vehicle_proxy_policy` |
| `source_values.known_restriction_review[3]` | `"Aménagement mixte hors voie verte"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `source_values.known_restriction_review`; order and uniqueness are validated/consumed where required. | `apply_ign_road_vehicle_proxy_policy` |
| `source_values.known_restriction_review[4]` | `"Piste cyclable"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `source_values.known_restriction_review`; order and uniqueness are validated/consumed where required. | `apply_ign_road_vehicle_proxy_policy` |
| `source_values.known_restriction_review[5]` | `"Entrée avec gardien"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `source_values.known_restriction_review`; order and uniqueness are validated/consumed where required. | `apply_ign_road_vehicle_proxy_policy` |
| `source_values.known_restriction_review[6]` | `"Passage barré"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `source_values.known_restriction_review`; order and uniqueness are validated/consumed where required. | `apply_ign_road_vehicle_proxy_policy` |
| `source_values.importance.known[0]` | `"1"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `source_values.importance.known`; order and uniqueness are validated/consumed where required. | `apply_ign_road_vehicle_proxy_policy` |
| `source_values.importance.known[1]` | `"2"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `source_values.importance.known`; order and uniqueness are validated/consumed where required. | `apply_ign_road_vehicle_proxy_policy` |
| `source_values.importance.known[2]` | `"3"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `source_values.importance.known`; order and uniqueness are validated/consumed where required. | `apply_ign_road_vehicle_proxy_policy` |
| `source_values.importance.known[3]` | `"4"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `source_values.importance.known`; order and uniqueness are validated/consumed where required. | `apply_ign_road_vehicle_proxy_policy` |
| `source_values.importance.known[4]` | `"5"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `source_values.importance.known`; order and uniqueness are validated/consumed where required. | `apply_ign_road_vehicle_proxy_policy` |
| `source_values.importance.known[5]` | `"6"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `source_values.importance.known`; order and uniqueness are validated/consumed where required. | `apply_ign_road_vehicle_proxy_policy` |
| `source_values.importance.limited[0]` | `"6"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `source_values.importance.limited`; order and uniqueness are validated/consumed where required. | `apply_ign_road_vehicle_proxy_policy` |
| `source_values.width_below_m` | `2.9` | `float` | path is a mapping key/list member validated by the enclosing model and validators; finite numeric value; Boolean coercion is rejected where the owning strict-number alias/validator applies | Configures width below m in metres. | `apply_ign_road_vehicle_proxy_policy` |
| `decision_precedence[0]` | `"FICTITIOUS_GEOMETRY"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `decision_precedence`; order and uniqueness are validated/consumed where required. | `apply_ign_road_vehicle_proxy_policy` |
| `decision_precedence[1]` | `"PROJECT_GEOMETRY_NOT_SIGNIFICANT"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `decision_precedence`; order and uniqueness are validated/consumed where required. | `apply_ign_road_vehicle_proxy_policy` |
| `decision_precedence[2]` | `"NOT_IN_SERVICE"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `decision_precedence`; order and uniqueness are validated/consumed where required. | `apply_ign_road_vehicle_proxy_policy` |
| `decision_precedence[3]` | `"PHYSICALLY_IMPOSSIBLE"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `decision_precedence`; order and uniqueness are validated/consumed where required. | `apply_ign_road_vehicle_proxy_policy` |
| `decision_precedence[4]` | `"NON_GENERAL_VEHICLE_NATURE"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `decision_precedence`; order and uniqueness are validated/consumed where required. | `apply_ign_road_vehicle_proxy_policy` |
| `decision_precedence[5]` | `"RIGHTS_RESTRICTED"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `decision_precedence`; order and uniqueness are validated/consumed where required. | `apply_ign_road_vehicle_proxy_policy` |
| `decision_precedence[6]` | `"PRIVATE_ROAD"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `decision_precedence`; order and uniqueness are validated/consumed where required. | `apply_ign_road_vehicle_proxy_policy` |
| `decision_precedence[7]` | `"TEMPORAL_CLOSURE"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `decision_precedence`; order and uniqueness are validated/consumed where required. | `apply_ign_road_vehicle_proxy_policy` |
| `decision_precedence[8]` | `"KNOWN_RESTRICTION"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `decision_precedence`; order and uniqueness are validated/consumed where required. | `apply_ign_road_vehicle_proxy_policy` |
| `decision_precedence[9]` | `"OTHER_RECORDED_RESTRICTION"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `decision_precedence`; order and uniqueness are validated/consumed where required. | `apply_ign_road_vehicle_proxy_policy` |
| `decision_precedence[10]` | `"SPECIAL_NATURE"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `decision_precedence`; order and uniqueness are validated/consumed where required. | `apply_ign_road_vehicle_proxy_policy` |
| `decision_precedence[11]` | `"LIMITED_NATURE"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `decision_precedence`; order and uniqueness are validated/consumed where required. | `apply_ign_road_vehicle_proxy_policy` |
| `decision_precedence[12]` | `"IMPORTANCE_6"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `decision_precedence`; order and uniqueness are validated/consumed where required. | `apply_ign_road_vehicle_proxy_policy` |
| `decision_precedence[13]` | `"NARROW_CARRIAGEWAY"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `decision_precedence`; order and uniqueness are validated/consumed where required. | `apply_ign_road_vehicle_proxy_policy` |
| `decision_precedence[14]` | `"OPEN_OR_TOLL"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `decision_precedence`; order and uniqueness are validated/consumed where required. | `apply_ign_road_vehicle_proxy_policy` |
| `decision_precedence[15]` | `"UNKNOWN"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `decision_precedence`; order and uniqueness are validated/consumed where required. | `apply_ign_road_vehicle_proxy_policy` |
| `decision_outcomes.fictitious_geometry` | `"NOT_DISTANCE_PROXY"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `fictitious geometry` under the exact parent path `decision_outcomes`. | `apply_ign_road_vehicle_proxy_policy` |
| `decision_outcomes.project_geometry_not_significant` | `"NOT_DISTANCE_PROXY"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `project geometry not significant` under the exact parent path `decision_outcomes`. | `apply_ign_road_vehicle_proxy_policy` |
| `decision_outcomes.not_in_service` | `"NOT_GENERAL_VEHICLE_PROXY"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `not in service` under the exact parent path `decision_outcomes`. | `apply_ign_road_vehicle_proxy_policy` |
| `decision_outcomes.physically_impossible` | `"NOT_GENERAL_VEHICLE_PROXY"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `physically impossible` under the exact parent path `decision_outcomes`. | `apply_ign_road_vehicle_proxy_policy` |
| `decision_outcomes.non_general_vehicle_nature` | `"NOT_GENERAL_VEHICLE_PROXY"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `non general vehicle nature` under the exact parent path `decision_outcomes`. | `apply_ign_road_vehicle_proxy_policy` |
| `decision_outcomes.rights_restricted` | `"RESTRICTED_REVIEW"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `rights restricted` under the exact parent path `decision_outcomes`. | `apply_ign_road_vehicle_proxy_policy` |
| `decision_outcomes.private_road` | `"RESTRICTED_REVIEW"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `private road` under the exact parent path `decision_outcomes`. | `apply_ign_road_vehicle_proxy_policy` |
| `decision_outcomes.temporal_closure` | `"RESTRICTED_REVIEW"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `temporal closure` under the exact parent path `decision_outcomes`. | `apply_ign_road_vehicle_proxy_policy` |
| `decision_outcomes.known_restriction` | `"RESTRICTED_REVIEW"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `known restriction` under the exact parent path `decision_outcomes`. | `apply_ign_road_vehicle_proxy_policy` |
| `decision_outcomes.other_recorded_restriction` | `"RESTRICTED_REVIEW"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `other recorded restriction` under the exact parent path `decision_outcomes`. | `apply_ign_road_vehicle_proxy_policy` |
| `decision_outcomes.special_nature` | `"RESTRICTED_REVIEW"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `special nature` under the exact parent path `decision_outcomes`. | `apply_ign_road_vehicle_proxy_policy` |
| `decision_outcomes.limited_nature` | `"LIMITED_VEHICLE_PROXY"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `limited nature` under the exact parent path `decision_outcomes`. | `apply_ign_road_vehicle_proxy_policy` |
| `decision_outcomes.importance_6` | `"LIMITED_VEHICLE_PROXY"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `importance 6` under the exact parent path `decision_outcomes`. | `apply_ign_road_vehicle_proxy_policy` |
| `decision_outcomes.narrow_carriageway` | `"LIMITED_VEHICLE_PROXY"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `narrow carriageway` under the exact parent path `decision_outcomes`. | `apply_ign_road_vehicle_proxy_policy` |
| `decision_outcomes.open_or_toll` | `"GENERAL_VEHICLE_PROXY"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `open or toll` under the exact parent path `decision_outcomes`. | `apply_ign_road_vehicle_proxy_policy` |
| `decision_outcomes.unknown` | `"UNKNOWN_REVIEW"` | `str` | path is a mapping key/list member validated by the enclosing model and validators; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `unknown` under the exact parent path `decision_outcomes`. | `apply_ign_road_vehicle_proxy_policy` |

## STEP 7F.1A.4 dependent-model refresh

- The YAML bytes and checked-in values are unchanged. STEP 7F.1A.4 changes their owning validation/authority boundary through `landscout.stages.road_vehicle_proxy_policy.load_ign_road_vehicle_proxy_policy`; section 5 now embeds the exact current owning model sources and qualified consumers.
- Decision-input models are frozen/deeply immutable where their current source declares that contract; trust-bearing YAML is decoded through the shared duplicate-rejecting loader where the owning loader source shows that call.
- No configured policy meaning, source identity, threshold, artifact schema, or output schema is changed by this dependent documentation refresh.

## 5. Classes / models / dataclasses

- Exact checked-in configuration SHA256 remains `2092bc620063ec1176b2abebaefafcc108a42793992dd18f869d44fdb07ca166`; its values are unchanged by STEP 7F.1A.4.
- Authoritative loader/config boundary: `landscout.stages.road_vehicle_proxy_policy.load_ign_road_vehicle_proxy_policy`.
- Owning Python module: `landscout.stages.road_vehicle_proxy_policy`.
- The owning model declarations below are refreshed from the current source so frozen/deeply immutable fields, strict serialization, exact domains, validators, and internal metadata schemas cannot remain stale merely because the YAML bytes did not change.

### `_StrictPolicyModel`

**Source purpose:** Defines `_StrictPolicyModel`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class _StrictPolicyModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)
```

### `_NavigationReferenceConfig`

**Source purpose:** Defines `_NavigationReferenceConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictPolicyModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `publisher` | `Literal['IGN']` | `required` | `publisher: Literal["IGN"]` |
| `title` | `Literal['Calcul d’itinéraire']` | `required` | `title: Literal["Calcul d’itinéraire"]` |
| `revision` | `Literal['2026-05-27']` | `required` | `revision: Literal["2026-05-27"]` |
| `evidence_scope` | `Literal['GENERAL_CAR_ROUTING_RULES']` | `required` | `evidence_scope: Literal["GENERAL_CAR_ROUTING_RULES"]` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class _NavigationReferenceConfig(_StrictPolicyModel):
    publisher: Literal["IGN"]
    title: Literal["Calcul d’itinéraire"]
    revision: Literal["2026-05-27"]
    evidence_scope: Literal["GENERAL_CAR_ROUTING_RULES"]
```

### `_BdTopoProductReferenceConfig`

**Source purpose:** Defines `_BdTopoProductReferenceConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictPolicyModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `publisher` | `Literal['IGN']` | `required` | `publisher: Literal["IGN"]` |
| `title` | `Literal['BD TOPO® Version 3.5 - Descriptif de contenu']` | `required` | `title: Literal["BD TOPO® Version 3.5 - Descriptif de contenu"]` |
| `document_id` | `Literal['DC_BDTOPO_3-5']` | `required` | `document_id: Literal["DC_BDTOPO_3-5"]` |
| `revision` | `Literal['2025-11']` | `required` | `revision: Literal["2025-11"]` |
| `evidence_scope` | `Literal['SOURCE_ATTRIBUTE_SEMANTICS']` | `required` | `evidence_scope: Literal["SOURCE_ATTRIBUTE_SEMANTICS"]` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class _BdTopoProductReferenceConfig(_StrictPolicyModel):
    publisher: Literal["IGN"]
    title: Literal["BD TOPO® Version 3.5 - Descriptif de contenu"]
    document_id: Literal["DC_BDTOPO_3-5"]
    revision: Literal["2025-11"]
    evidence_scope: Literal["SOURCE_ATTRIBUTE_SEMANTICS"]
```

### `_ReferencesConfig`

**Source purpose:** Defines `_ReferencesConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictPolicyModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `navigation` | `_NavigationReferenceConfig` | `required` | `navigation: _NavigationReferenceConfig` |
| `bdtopo_product` | `_BdTopoProductReferenceConfig` | `required` | `bdtopo_product: _BdTopoProductReferenceConfig` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class _ReferencesConfig(_StrictPolicyModel):
    navigation: _NavigationReferenceConfig
    bdtopo_product: _BdTopoProductReferenceConfig
```

### `_ClassesConfig`

**Source purpose:** Defines `_ClassesConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictPolicyModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `general_vehicle_proxy` | `Literal['GENERAL_VEHICLE_PROXY']` | `required` | `general_vehicle_proxy: Literal["GENERAL_VEHICLE_PROXY"]` |
| `limited_vehicle_proxy` | `Literal['LIMITED_VEHICLE_PROXY']` | `required` | `limited_vehicle_proxy: Literal["LIMITED_VEHICLE_PROXY"]` |
| `restricted_review` | `Literal['RESTRICTED_REVIEW']` | `required` | `restricted_review: Literal["RESTRICTED_REVIEW"]` |
| `not_general_vehicle_proxy` | `Literal['NOT_GENERAL_VEHICLE_PROXY']` | `required` | `not_general_vehicle_proxy: Literal["NOT_GENERAL_VEHICLE_PROXY"]` |
| `not_distance_proxy` | `Literal['NOT_DISTANCE_PROXY']` | `required` | `not_distance_proxy: Literal["NOT_DISTANCE_PROXY"]` |
| `unknown_review` | `Literal['UNKNOWN_REVIEW']` | `required` | `unknown_review: Literal["UNKNOWN_REVIEW"]` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class _ClassesConfig(_StrictPolicyModel):
    general_vehicle_proxy: Literal["GENERAL_VEHICLE_PROXY"]
    limited_vehicle_proxy: Literal["LIMITED_VEHICLE_PROXY"]
    restricted_review: Literal["RESTRICTED_REVIEW"]
    not_general_vehicle_proxy: Literal["NOT_GENERAL_VEHICLE_PROXY"]
    not_distance_proxy: Literal["NOT_DISTANCE_PROXY"]
    unknown_review: Literal["UNKNOWN_REVIEW"]
```

### `_AssetStateConfig`

**Source purpose:** Defines `_AssetStateConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictPolicyModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `in_service` | `_NonEmptyStrings` | `required` | `in_service: _NonEmptyStrings` |
| `project_geometry_not_significant` | `_NonEmptyStrings` | `required` | `project_geometry_not_significant: _NonEmptyStrings` |
| `under_construction` | `_NonEmptyStrings` | `required` | `under_construction: _NonEmptyStrings` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class _AssetStateConfig(_StrictPolicyModel):
    in_service: _NonEmptyStrings
    project_geometry_not_significant: _NonEmptyStrings
    under_construction: _NonEmptyStrings

    @model_validator(mode="after")
    def _valid_groups(self) -> Self:
        groups = (
            self.in_service,
            self.project_geometry_not_significant,
            self.under_construction,
        )
        for name, values in zip(
            (
                "in_service",
                "project_geometry_not_significant",
                "under_construction",
            ),
            groups,
            strict=True,
        ):
            _require_unique(values, name)
        _require_disjoint(groups, "asset_state")
        if groups != (("En service",), ("En projet",), ("En construction",)):
            raise ValueError("asset_state groups must cover the exact source domain")
        return self
```

### `_LightVehicleAccessConfig`

**Source purpose:** Defines `_LightVehicleAccessConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictPolicyModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `open` | `_NonEmptyStrings` | `required` | `open: _NonEmptyStrings` |
| `toll` | `_NonEmptyStrings` | `required` | `toll: _NonEmptyStrings` |
| `rights_restricted` | `_NonEmptyStrings` | `required` | `rights_restricted: _NonEmptyStrings` |
| `physically_impossible` | `_NonEmptyStrings` | `required` | `physically_impossible: _NonEmptyStrings` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class _LightVehicleAccessConfig(_StrictPolicyModel):
    open: _NonEmptyStrings
    toll: _NonEmptyStrings
    rights_restricted: _NonEmptyStrings
    physically_impossible: _NonEmptyStrings

    @model_validator(mode="after")
    def _valid_groups(self) -> Self:
        groups = (
            self.open,
            self.toll,
            self.rights_restricted,
            self.physically_impossible,
        )
        for name, values in zip(
            ("open", "toll", "rights_restricted", "physically_impossible"),
            groups,
            strict=True,
        ):
            _require_unique(values, name)
        _require_disjoint(groups, "light_vehicle_access")
        return self
```

### `_RoadNatureConfig`

**Source purpose:** Defines `_RoadNatureConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictPolicyModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `general_motor_road` | `_NonEmptyStrings` | `required` | `general_motor_road: _NonEmptyStrings` |
| `limited_motor_proxy` | `_NonEmptyStrings` | `required` | `limited_motor_proxy: _NonEmptyStrings` |
| `non_general_vehicle` | `_NonEmptyStrings` | `required` | `non_general_vehicle: _NonEmptyStrings` |
| `special_review` | `_NonEmptyStrings` | `required` | `special_review: _NonEmptyStrings` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class _RoadNatureConfig(_StrictPolicyModel):
    general_motor_road: _NonEmptyStrings
    limited_motor_proxy: _NonEmptyStrings
    non_general_vehicle: _NonEmptyStrings
    special_review: _NonEmptyStrings

    @model_validator(mode="after")
    def _valid_groups(self) -> Self:
        groups = (
            self.general_motor_road,
            self.limited_motor_proxy,
            self.non_general_vehicle,
            self.special_review,
        )
        for name, values in zip(
            (
                "general_motor_road",
                "limited_motor_proxy",
                "non_general_vehicle",
                "special_review",
            ),
            groups,
            strict=True,
        ):
            _require_unique(values, name)
        _require_disjoint(groups, "nature")
        return self
```

### `_ImportanceConfig`

**Source purpose:** Defines `_ImportanceConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictPolicyModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `known` | `_NonEmptyStrings` | `required` | `known: _NonEmptyStrings` |
| `limited` | `_NonEmptyStrings` | `required` | `limited: _NonEmptyStrings` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class _ImportanceConfig(_StrictPolicyModel):
    known: _NonEmptyStrings
    limited: _NonEmptyStrings

    @model_validator(mode="after")
    def _valid_domain(self) -> Self:
        _require_unique(self.known, "importance.known")
        _require_unique(self.limited, "importance.limited")
        if self.known != ("1", "2", "3", "4", "5", "6"):
            raise ValueError("importance.known must cover exactly source values 1-6")
        if self.limited != ("6",):
            raise ValueError("importance.limited must contain exactly source value '6'")
        if not set(self.limited).issubset(self.known):
            raise ValueError("importance.limited must be a subset of importance.known")
        return self
```

### `_SourceValuesConfig`

**Source purpose:** Defines `_SourceValuesConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictPolicyModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `asset_state` | `_AssetStateConfig` | `required` | `asset_state: _AssetStateConfig` |
| `light_vehicle_access` | `_LightVehicleAccessConfig` | `required` | `light_vehicle_access: _LightVehicleAccessConfig` |
| `nature` | `_RoadNatureConfig` | `required` | `nature: _RoadNatureConfig` |
| `known_restriction_review` | `_NonEmptyStrings` | `required` | `known_restriction_review: _NonEmptyStrings` |
| `importance` | `_ImportanceConfig` | `required` | `importance: _ImportanceConfig` |
| `width_below_m` | `Annotated[StrictFloat, Field(gt=0, allow_inf_nan=False)]` | `required` | `width_below_m: Annotated[StrictFloat, Field(gt=0, allow_inf_nan=False)]` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class _SourceValuesConfig(_StrictPolicyModel):
    asset_state: _AssetStateConfig
    light_vehicle_access: _LightVehicleAccessConfig
    nature: _RoadNatureConfig
    known_restriction_review: _NonEmptyStrings
    importance: _ImportanceConfig
    width_below_m: Annotated[StrictFloat, Field(gt=0, allow_inf_nan=False)]

    @model_validator(mode="after")
    def _valid_values(self) -> Self:
        _require_unique(self.known_restriction_review, "known_restriction_review")
        return self
```

### `_DecisionOutcomesConfig`

**Source purpose:** Defines `_DecisionOutcomesConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictPolicyModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `fictitious_geometry` | `Literal['NOT_DISTANCE_PROXY']` | `required` | `fictitious_geometry: Literal["NOT_DISTANCE_PROXY"]` |
| `project_geometry_not_significant` | `Literal['NOT_DISTANCE_PROXY']` | `required` | `project_geometry_not_significant: Literal["NOT_DISTANCE_PROXY"]` |
| `not_in_service` | `Literal['NOT_GENERAL_VEHICLE_PROXY']` | `required` | `not_in_service: Literal["NOT_GENERAL_VEHICLE_PROXY"]` |
| `physically_impossible` | `Literal['NOT_GENERAL_VEHICLE_PROXY']` | `required` | `physically_impossible: Literal["NOT_GENERAL_VEHICLE_PROXY"]` |
| `non_general_vehicle_nature` | `Literal['NOT_GENERAL_VEHICLE_PROXY']` | `required` | `non_general_vehicle_nature: Literal["NOT_GENERAL_VEHICLE_PROXY"]` |
| `rights_restricted` | `Literal['RESTRICTED_REVIEW']` | `required` | `rights_restricted: Literal["RESTRICTED_REVIEW"]` |
| `private_road` | `Literal['RESTRICTED_REVIEW']` | `required` | `private_road: Literal["RESTRICTED_REVIEW"]` |
| `temporal_closure` | `Literal['RESTRICTED_REVIEW']` | `required` | `temporal_closure: Literal["RESTRICTED_REVIEW"]` |
| `known_restriction` | `Literal['RESTRICTED_REVIEW']` | `required` | `known_restriction: Literal["RESTRICTED_REVIEW"]` |
| `other_recorded_restriction` | `Literal['RESTRICTED_REVIEW']` | `required` | `other_recorded_restriction: Literal["RESTRICTED_REVIEW"]` |
| `special_nature` | `Literal['RESTRICTED_REVIEW']` | `required` | `special_nature: Literal["RESTRICTED_REVIEW"]` |
| `limited_nature` | `Literal['LIMITED_VEHICLE_PROXY']` | `required` | `limited_nature: Literal["LIMITED_VEHICLE_PROXY"]` |
| `importance_6` | `Literal['LIMITED_VEHICLE_PROXY']` | `required` | `importance_6: Literal["LIMITED_VEHICLE_PROXY"]` |
| `narrow_carriageway` | `Literal['LIMITED_VEHICLE_PROXY']` | `required` | `narrow_carriageway: Literal["LIMITED_VEHICLE_PROXY"]` |
| `open_or_toll` | `Literal['GENERAL_VEHICLE_PROXY']` | `required` | `open_or_toll: Literal["GENERAL_VEHICLE_PROXY"]` |
| `unknown` | `Literal['UNKNOWN_REVIEW']` | `required` | `unknown: Literal["UNKNOWN_REVIEW"]` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class _DecisionOutcomesConfig(_StrictPolicyModel):
    fictitious_geometry: Literal["NOT_DISTANCE_PROXY"]
    project_geometry_not_significant: Literal["NOT_DISTANCE_PROXY"]
    not_in_service: Literal["NOT_GENERAL_VEHICLE_PROXY"]
    physically_impossible: Literal["NOT_GENERAL_VEHICLE_PROXY"]
    non_general_vehicle_nature: Literal["NOT_GENERAL_VEHICLE_PROXY"]
    rights_restricted: Literal["RESTRICTED_REVIEW"]
    private_road: Literal["RESTRICTED_REVIEW"]
    temporal_closure: Literal["RESTRICTED_REVIEW"]
    known_restriction: Literal["RESTRICTED_REVIEW"]
    other_recorded_restriction: Literal["RESTRICTED_REVIEW"]
    special_nature: Literal["RESTRICTED_REVIEW"]
    limited_nature: Literal["LIMITED_VEHICLE_PROXY"]
    importance_6: Literal["LIMITED_VEHICLE_PROXY"]
    narrow_carriageway: Literal["LIMITED_VEHICLE_PROXY"]
    open_or_toll: Literal["GENERAL_VEHICLE_PROXY"]
    unknown: Literal["UNKNOWN_REVIEW"]
```

### `_PolicyConfig`

**Source purpose:** Defines `_PolicyConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictPolicyModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `policy_id` | `_ExactString` | `required` | `policy_id: _ExactString` |
| `schema_version` | `StrictInt` | `required` | `schema_version: StrictInt` |
| `scope` | `_ExactString` | `required` | `scope: _ExactString` |
| `references` | `_ReferencesConfig` | `required` | `references: _ReferencesConfig` |
| `evidence_checked_on` | `Literal['2026-08-16']` | `required` | `evidence_checked_on: Literal["2026-08-16"]` |
| `vehicle_scope` | `Literal['LIGHT_VEHICLE_AND_GENERAL_CAR_NETWORK']` | `required` | `vehicle_scope: Literal["LIGHT_VEHICLE_AND_GENERAL_CAR_NETWORK"]` |
| `heavy_vehicle_access` | `Literal['NOT_PROVEN']` | `required` | `heavy_vehicle_access: Literal["NOT_PROVEN"]` |
| `classes` | `_ClassesConfig` | `required` | `classes: _ClassesConfig` |
| `source_values` | `_SourceValuesConfig` | `required` | `source_values: _SourceValuesConfig` |
| `decision_precedence` | `_NonEmptyStrings` | `required` | `decision_precedence: _NonEmptyStrings` |
| `decision_outcomes` | `_DecisionOutcomesConfig` | `required` | `decision_outcomes: _DecisionOutcomesConfig` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- value/type reference: `landscout.stages.road_vehicle_proxy_policy::_compile_policy` via `_PolicyConfig`
- value/type reference: `landscout.stages.road_vehicle_proxy_policy::load_ign_road_vehicle_proxy_policy` via `_PolicyConfig`

**Exact class source**

```python
class _PolicyConfig(_StrictPolicyModel):
    policy_id: _ExactString
    schema_version: StrictInt
    scope: _ExactString
    references: _ReferencesConfig
    evidence_checked_on: Literal["2026-08-16"]
    vehicle_scope: Literal["LIGHT_VEHICLE_AND_GENERAL_CAR_NETWORK"]
    heavy_vehicle_access: Literal["NOT_PROVEN"]
    classes: _ClassesConfig
    source_values: _SourceValuesConfig
    decision_precedence: _NonEmptyStrings
    decision_outcomes: _DecisionOutcomesConfig

    @model_validator(mode="after")
    def _valid_identity_and_precedence(self) -> Self:
        if self.policy_id != _POLICY_ID:
            raise ValueError("policy_id is not the approved v2 policy identity")
        if self.schema_version != 2:
            raise ValueError("schema_version must be exactly 2")
        if self.scope != _POLICY_SCOPE:
            raise ValueError("scope is not the approved official IGN evidence scope")
        if self.decision_precedence != _EXPECTED_PRECEDENCE:
            raise ValueError("decision_precedence differs from approved v2 order")
        return self
```

## 6. Functions and methods

Loader: `landscout.stages.road_vehicle_proxy_policy.load_ign_road_vehicle_proxy_policy`. Its source-module companion documents path resolution, YAML parsing, controlled exceptions, exact validation, and any hashing actually performed by that loader.

## 7. Data contracts

This file supplies configuration/policy/source identity. It does not itself create a frame. Any fields copied into output rows are documented by the consuming stage's canonical frame schema.

## 8. Interfaces

Runtime consumers: `apply_ign_road_vehicle_proxy_policy`. Dynamic path construction is included: the road policy loader resolves its default access-policy path, and scan loading resolves `ProfileReference.path` to the BESS profile file.

## 9. Error handling

The owning Pydantic model rejects extra/missing/unsupported/coerced values according to the exact model/validators above; the loader translates YAML/path/model failures into its documented controlled error.

## 10. Side effects

Network I/O: none. Filesystem read: the loader reads this YAML. Filesystem write: none. Input mutation: none. GIS calculation: none. Hashing: the road-policy loader hashes the exact UTF-8 policy bytes and stores that SHA256 in the compiled policy.

## 11. Security / trust boundaries

A configured URL/provider/hash is a source lock or provenance input. Physical authority requires the consuming source adapter's safe transport and byte/source revalidation.

## 12. GIS / CRS rules

Only explicit CRS fields impose GIS rules; configured storage/calculation CRS values are policy/configuration, not an implicit reprojection of data.

## 13. Provenance rules

The companion's Source SHA256 binds this checked-in file for documentation fidelity; that documentation digest is not attributed to the runtime loader. Source identities remain textual until the adapter validates physical bytes/content.

## 14. Business meaning

Thresholds and outcomes are policy/configuration values. They are never relabeled as measured geometry or legal conclusions.

## 15. Explicit non-goals

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

## 16. Tests

The loader/model companion and relevant test companion document exact valid/invalid values, cross-field failures, consumer loading, and byte-hash behavior only where the runtime source actually computes a hash.

## 17. Change impact

Any YAML byte/value change requires policy/source review, consumer tests, generated artifacts where applicable, this companion SHA update, and only those runtime hashes whose documented algorithm actually includes these bytes or validated values.

## 18. Complete readable configuration and authoritative raw-byte snapshot

### Complete readable YAML

The following is the complete decoded UTF-8 configuration with line endings normalized to LF for stable Markdown display. Every character and logical line is present, but this readable fence is not the authority for original CR/LF byte positions.

```yaml
policy_id: "ign_bdtopo_general_vehicle_proxy_v2"
schema_version: 2
scope: "OFFICIAL_IGN_CAR_ROUTING_EVIDENCE_ONLY"

references:
  navigation:
    publisher: "IGN"
    title: "Calcul d’itinéraire"
    revision: "2026-05-27"
    evidence_scope: "GENERAL_CAR_ROUTING_RULES"
  bdtopo_product:
    publisher: "IGN"
    title: "BD TOPO® Version 3.5 - Descriptif de contenu"
    document_id: "DC_BDTOPO_3-5"
    revision: "2025-11"
    evidence_scope: "SOURCE_ATTRIBUTE_SEMANTICS"

evidence_checked_on: "2026-08-16"
vehicle_scope: "LIGHT_VEHICLE_AND_GENERAL_CAR_NETWORK"
heavy_vehicle_access: "NOT_PROVEN"

classes:
  general_vehicle_proxy: "GENERAL_VEHICLE_PROXY"
  limited_vehicle_proxy: "LIMITED_VEHICLE_PROXY"
  restricted_review: "RESTRICTED_REVIEW"
  not_general_vehicle_proxy: "NOT_GENERAL_VEHICLE_PROXY"
  not_distance_proxy: "NOT_DISTANCE_PROXY"
  unknown_review: "UNKNOWN_REVIEW"

source_values:
  asset_state:
    in_service:
      - "En service"
    project_geometry_not_significant:
      - "En projet"
    under_construction:
      - "En construction"

  light_vehicle_access:
    open:
      - "Libre"
    toll:
      - "A péage"
    rights_restricted:
      - "Restreint aux ayants droit"
    physically_impossible:
      - "Physiquement impossible"

  nature:
    general_motor_road:
      - "Route à 1 chaussée"
      - "Route à 2 chaussées"
      - "Rond-point"
      - "Bretelle"
      - "Type autoroutier"
    limited_motor_proxy:
      - "Route empierrée"
      - "Chemin"
    non_general_vehicle:
      - "Escalier"
      - "Sentier"
      - "Piste cyclable"
    special_review:
      - "Bac ou liaison maritime"

  known_restriction_review:
    - "Plot amovible"
    - "Voie de tramway utilisable par les véhicules de secours"
    - "Voie verte"
    - "Aménagement mixte hors voie verte"
    - "Piste cyclable"
    - "Entrée avec gardien"
    - "Passage barré"

  importance:
    known:
      - "1"
      - "2"
      - "3"
      - "4"
      - "5"
      - "6"
    limited:
      - "6"

  width_below_m: 2.9

decision_precedence:
  - "FICTITIOUS_GEOMETRY"
  - "PROJECT_GEOMETRY_NOT_SIGNIFICANT"
  - "NOT_IN_SERVICE"
  - "PHYSICALLY_IMPOSSIBLE"
  - "NON_GENERAL_VEHICLE_NATURE"
  - "RIGHTS_RESTRICTED"
  - "PRIVATE_ROAD"
  - "TEMPORAL_CLOSURE"
  - "KNOWN_RESTRICTION"
  - "OTHER_RECORDED_RESTRICTION"
  - "SPECIAL_NATURE"
  - "LIMITED_NATURE"
  - "IMPORTANCE_6"
  - "NARROW_CARRIAGEWAY"
  - "OPEN_OR_TOLL"
  - "UNKNOWN"

decision_outcomes:
  fictitious_geometry: "NOT_DISTANCE_PROXY"
  project_geometry_not_significant: "NOT_DISTANCE_PROXY"
  not_in_service: "NOT_GENERAL_VEHICLE_PROXY"
  physically_impossible: "NOT_GENERAL_VEHICLE_PROXY"
  non_general_vehicle_nature: "NOT_GENERAL_VEHICLE_PROXY"
  rights_restricted: "RESTRICTED_REVIEW"
  private_road: "RESTRICTED_REVIEW"
  temporal_closure: "RESTRICTED_REVIEW"
  known_restriction: "RESTRICTED_REVIEW"
  other_recorded_restriction: "RESTRICTED_REVIEW"
  special_nature: "RESTRICTED_REVIEW"
  limited_nature: "LIMITED_VEHICLE_PROXY"
  importance_6: "LIMITED_VEHICLE_PROXY"
  narrow_carriageway: "LIMITED_VEHICLE_PROXY"
  open_or_toll: "GENERAL_VEHICLE_PROXY"
  unknown: "UNKNOWN_REVIEW"
```

### Authoritative raw-byte payload

- Raw byte length: `3168`.
- Raw SHA256: `2092bc620063ec1176b2abebaefafcc108a42793992dd18f869d44fdb07ca166` (identical to **File identity**).
- Encoding: RFC 4648 Base64, wrapped for display only. Decoding the concatenated payload reproduces every original byte, including mixed CRLF/LF positions.

```text
cG9saWN5X2lkOiAiaWduX2JkdG9wb19nZW5lcmFsX3ZlaGljbGVfcHJveHlfdjIiCnNjaGVtYV92
ZXJzaW9uOiAyCnNjb3BlOiAiT0ZGSUNJQUxfSUdOX0NBUl9ST1VUSU5HX0VWSURFTkNFX09OTFki
CgpyZWZlcmVuY2VzOgogIG5hdmlnYXRpb246CiAgICBwdWJsaXNoZXI6ICJJR04iCiAgICB0aXRs
ZTogIkNhbGN1bCBk4oCZaXRpbsOpcmFpcmUiCiAgICByZXZpc2lvbjogIjIwMjYtMDUtMjciCiAg
ICBldmlkZW5jZV9zY29wZTogIkdFTkVSQUxfQ0FSX1JPVVRJTkdfUlVMRVMiCiAgYmR0b3BvX3By
b2R1Y3Q6CiAgICBwdWJsaXNoZXI6ICJJR04iCiAgICB0aXRsZTogIkJEIFRPUE/CriBWZXJzaW9u
IDMuNSAtIERlc2NyaXB0aWYgZGUgY29udGVudSIKICAgIGRvY3VtZW50X2lkOiAiRENfQkRUT1BP
XzMtNSIKICAgIHJldmlzaW9uOiAiMjAyNS0xMSIKICAgIGV2aWRlbmNlX3Njb3BlOiAiU09VUkNF
X0FUVFJJQlVURV9TRU1BTlRJQ1MiCgpldmlkZW5jZV9jaGVja2VkX29uOiAiMjAyNi0wOC0xNiIK
dmVoaWNsZV9zY29wZTogIkxJR0hUX1ZFSElDTEVfQU5EX0dFTkVSQUxfQ0FSX05FVFdPUksiCmhl
YXZ5X3ZlaGljbGVfYWNjZXNzOiAiTk9UX1BST1ZFTiIKCmNsYXNzZXM6CiAgZ2VuZXJhbF92ZWhp
Y2xlX3Byb3h5OiAiR0VORVJBTF9WRUhJQ0xFX1BST1hZIgogIGxpbWl0ZWRfdmVoaWNsZV9wcm94
eTogIkxJTUlURURfVkVISUNMRV9QUk9YWSIKICByZXN0cmljdGVkX3JldmlldzogIlJFU1RSSUNU
RURfUkVWSUVXIgogIG5vdF9nZW5lcmFsX3ZlaGljbGVfcHJveHk6ICJOT1RfR0VORVJBTF9WRUhJ
Q0xFX1BST1hZIgogIG5vdF9kaXN0YW5jZV9wcm94eTogIk5PVF9ESVNUQU5DRV9QUk9YWSIKICB1
bmtub3duX3JldmlldzogIlVOS05PV05fUkVWSUVXIgoKc291cmNlX3ZhbHVlczoKICBhc3NldF9z
dGF0ZToKICAgIGluX3NlcnZpY2U6CiAgICAgIC0gIkVuIHNlcnZpY2UiCiAgICBwcm9qZWN0X2dl
b21ldHJ5X25vdF9zaWduaWZpY2FudDoKICAgICAgLSAiRW4gcHJvamV0IgogICAgdW5kZXJfY29u
c3RydWN0aW9uOgogICAgICAtICJFbiBjb25zdHJ1Y3Rpb24iCgogIGxpZ2h0X3ZlaGljbGVfYWNj
ZXNzOgogICAgb3BlbjoKICAgICAgLSAiTGlicmUiCiAgICB0b2xsOgogICAgICAtICJBIHDDqWFn
ZSIKICAgIHJpZ2h0c19yZXN0cmljdGVkOgogICAgICAtICJSZXN0cmVpbnQgYXV4IGF5YW50cyBk
cm9pdCIKICAgIHBoeXNpY2FsbHlfaW1wb3NzaWJsZToKICAgICAgLSAiUGh5c2lxdWVtZW50IGlt
cG9zc2libGUiCgogIG5hdHVyZToKICAgIGdlbmVyYWxfbW90b3Jfcm9hZDoKICAgICAgLSAiUm91
dGUgw6AgMSBjaGF1c3PDqWUiCiAgICAgIC0gIlJvdXRlIMOgIDIgY2hhdXNzw6llcyIKICAgICAg
LSAiUm9uZC1wb2ludCIKICAgICAgLSAiQnJldGVsbGUiCiAgICAgIC0gIlR5cGUgYXV0b3JvdXRp
ZXIiCiAgICBsaW1pdGVkX21vdG9yX3Byb3h5OgogICAgICAtICJSb3V0ZSBlbXBpZXJyw6llIgog
ICAgICAtICJDaGVtaW4iCiAgICBub25fZ2VuZXJhbF92ZWhpY2xlOgogICAgICAtICJFc2NhbGll
ciIKICAgICAgLSAiU2VudGllciIKICAgICAgLSAiUGlzdGUgY3ljbGFibGUiCiAgICBzcGVjaWFs
X3JldmlldzoKICAgICAgLSAiQmFjIG91IGxpYWlzb24gbWFyaXRpbWUiCgogIGtub3duX3Jlc3Ry
aWN0aW9uX3JldmlldzoKICAgIC0gIlBsb3QgYW1vdmlibGUiCiAgICAtICJWb2llIGRlIHRyYW13
YXkgdXRpbGlzYWJsZSBwYXIgbGVzIHbDqWhpY3VsZXMgZGUgc2Vjb3VycyIKICAgIC0gIlZvaWUg
dmVydGUiCiAgICAtICJBbcOpbmFnZW1lbnQgbWl4dGUgaG9ycyB2b2llIHZlcnRlIgogICAgLSAi
UGlzdGUgY3ljbGFibGUiCiAgICAtICJFbnRyw6llIGF2ZWMgZ2FyZGllbiIKICAgIC0gIlBhc3Nh
Z2UgYmFycsOpIgoKICBpbXBvcnRhbmNlOgogICAga25vd246CiAgICAgIC0gIjEiCiAgICAgIC0g
IjIiCiAgICAgIC0gIjMiCiAgICAgIC0gIjQiCiAgICAgIC0gIjUiCiAgICAgIC0gIjYiCiAgICBs
aW1pdGVkOgogICAgICAtICI2IgoKICB3aWR0aF9iZWxvd19tOiAyLjkKCmRlY2lzaW9uX3ByZWNl
ZGVuY2U6CiAgLSAiRklDVElUSU9VU19HRU9NRVRSWSIKICAtICJQUk9KRUNUX0dFT01FVFJZX05P
VF9TSUdOSUZJQ0FOVCIKICAtICJOT1RfSU5fU0VSVklDRSIKICAtICJQSFlTSUNBTExZX0lNUE9T
U0lCTEUiCiAgLSAiTk9OX0dFTkVSQUxfVkVISUNMRV9OQVRVUkUiCiAgLSAiUklHSFRTX1JFU1RS
SUNURUQiCiAgLSAiUFJJVkFURV9ST0FEIgogIC0gIlRFTVBPUkFMX0NMT1NVUkUiCiAgLSAiS05P
V05fUkVTVFJJQ1RJT04iCiAgLSAiT1RIRVJfUkVDT1JERURfUkVTVFJJQ1RJT04iCiAgLSAiU1BF
Q0lBTF9OQVRVUkUiCiAgLSAiTElNSVRFRF9OQVRVUkUiCiAgLSAiSU1QT1JUQU5DRV82IgogIC0g
Ik5BUlJPV19DQVJSSUFHRVdBWSIKICAtICJPUEVOX09SX1RPTEwiCiAgLSAiVU5LTk9XTiIKCmRl
Y2lzaW9uX291dGNvbWVzOgogIGZpY3RpdGlvdXNfZ2VvbWV0cnk6ICJOT1RfRElTVEFOQ0VfUFJP
WFkiCiAgcHJvamVjdF9nZW9tZXRyeV9ub3Rfc2lnbmlmaWNhbnQ6ICJOT1RfRElTVEFOQ0VfUFJP
WFkiCiAgbm90X2luX3NlcnZpY2U6ICJOT1RfR0VORVJBTF9WRUhJQ0xFX1BST1hZIgogIHBoeXNp
Y2FsbHlfaW1wb3NzaWJsZTogIk5PVF9HRU5FUkFMX1ZFSElDTEVfUFJPWFkiCiAgbm9uX2dlbmVy
YWxfdmVoaWNsZV9uYXR1cmU6ICJOT1RfR0VORVJBTF9WRUhJQ0xFX1BST1hZIgogIHJpZ2h0c19y
ZXN0cmljdGVkOiAiUkVTVFJJQ1RFRF9SRVZJRVciCiAgcHJpdmF0ZV9yb2FkOiAiUkVTVFJJQ1RF
RF9SRVZJRVciCiAgdGVtcG9yYWxfY2xvc3VyZTogIlJFU1RSSUNURURfUkVWSUVXIgogIGtub3du
X3Jlc3RyaWN0aW9uOiAiUkVTVFJJQ1RFRF9SRVZJRVciCiAgb3RoZXJfcmVjb3JkZWRfcmVzdHJp
Y3Rpb246ICJSRVNUUklDVEVEX1JFVklFVyIKICBzcGVjaWFsX25hdHVyZTogIlJFU1RSSUNURURf
UkVWSUVXIgogIGxpbWl0ZWRfbmF0dXJlOiAiTElNSVRFRF9WRUhJQ0xFX1BST1hZIgogIGltcG9y
dGFuY2VfNjogIkxJTUlURURfVkVISUNMRV9QUk9YWSIKICBuYXJyb3dfY2FycmlhZ2V3YXk6ICJM
SU1JVEVEX1ZFSElDTEVfUFJPWFkiCiAgb3Blbl9vcl90b2xsOiAiR0VORVJBTF9WRUhJQ0xFX1BS
T1hZIgogIHVua25vd246ICJVTktOT1dOX1JFVklFVyIK
```
