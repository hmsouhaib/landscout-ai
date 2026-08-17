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

## 5. Classes / models / dataclasses

Authoritative owning model: `landscout.stages.road_vehicle_proxy_policy.IgnRoadVehicleProxyPolicy`. The checked-in file currently validates as `IgnRoadVehicleProxyPolicy`.

```python
class _StrictPolicyModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

class _CompiledClasses:
    general_vehicle_proxy: str
    limited_vehicle_proxy: str
    restricted_review: str
    not_general_vehicle_proxy: str
    not_distance_proxy: str
    unknown_review: str

    @property
    def values(self) -> tuple[str, ...]:
        return (
            self.general_vehicle_proxy,
            self.limited_vehicle_proxy,
            self.restricted_review,
            self.not_general_vehicle_proxy,
            self.not_distance_proxy,
            self.unknown_review,
        )

class _CompiledAssetState:
    in_service: frozenset[str]
    project_geometry_not_significant: frozenset[str]
    under_construction: frozenset[str]

class _CompiledNavigationReference:
    publisher: str
    title: str
    revision: str
    evidence_scope: str

class _CompiledBdTopoProductReference:
    publisher: str
    title: str
    document_id: str
    revision: str
    evidence_scope: str

class _CompiledLightVehicleAccess:
    open: frozenset[str]
    toll: frozenset[str]
    rights_restricted: frozenset[str]
    physically_impossible: frozenset[str]

class _CompiledRoadNature:
    general_motor_road: frozenset[str]
    limited_motor_proxy: frozenset[str]
    non_general_vehicle: frozenset[str]
    special_review: frozenset[str]

class _CompiledImportance:
    known: frozenset[str]
    limited: frozenset[str]

class _CompiledDecisionOutcomes:
    fictitious_geometry: str
    project_geometry_not_significant: str
    not_in_service: str
    physically_impossible: str
    non_general_vehicle_nature: str
    rights_restricted: str
    private_road: str
    temporal_closure: str
    known_restriction: str
    other_recorded_restriction: str
    special_nature: str
    limited_nature: str
    importance_6: str
    narrow_carriageway: str
    open_or_toll: str
    unknown: str

class IgnRoadVehicleProxyPolicy:
    """Immutable policy evidence compiled from the exact checked-in YAML bytes."""

    policy_id: str
    schema_version: int
    scope: str
    navigation_reference: _CompiledNavigationReference
    bdtopo_product_reference: _CompiledBdTopoProductReference
    evidence_checked_on: str
    vehicle_scope: str
    heavy_vehicle_access: str
    classes: _CompiledClasses
    asset_state: _CompiledAssetState
    light_vehicle_access: _CompiledLightVehicleAccess
    nature: _CompiledRoadNature
    known_restriction_review: frozenset[str]
    importance: _CompiledImportance
    width_below_m: float
    decision_precedence: tuple[str, ...]
    decision_outcomes: _CompiledDecisionOutcomes
    config_sha256: str
```

## 6. Functions and methods

Loader: `landscout.stages.road_vehicle_proxy_policy.load_ign_road_vehicle_proxy_policy`. Its source-module companion documents path resolution, YAML parsing, controlled exceptions, byte hashing, and cross-field validation.

## 7. Data contracts

This file supplies configuration/policy/source identity. It does not itself create a frame. Any fields copied into output rows are documented by the consuming stage's canonical frame schema.

## 8. Interfaces

Runtime consumers: `apply_ign_road_vehicle_proxy_policy`. Dynamic path construction is included: the road policy loader resolves its default access-policy path, and scan loading resolves `ProfileReference.path` to the BESS profile file.

## 9. Error handling

The owning Pydantic model rejects extra/missing/unsupported/coerced values according to the exact model/validators above; the loader translates YAML/path/model failures into its documented controlled error.

## 10. Side effects

Network I/O: none. Filesystem read: the loader reads this YAML. Filesystem write: none. Input mutation: none. GIS calculation: none. Hashing: loaders that expose config identity hash these exact bytes.

## 11. Security / trust boundaries

A configured URL/provider/hash is a source lock or provenance input. Physical authority requires the consuming source adapter's safe transport and byte/source revalidation.

## 12. GIS / CRS rules

Only explicit CRS fields impose GIS rules; configured storage/calculation CRS values are policy/configuration, not an implicit reprojection of data.

## 13. Provenance rules

The file's SHA256 binds this exact policy/configuration snapshot. Source identities remain textual until the adapter validates physical bytes/content.

## 14. Business meaning

Thresholds and outcomes are policy/configuration values. They are never relabeled as measured geometry or legal conclusions.

## 15. Explicit non-goals

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

## 16. Tests

The loader/model companion and relevant test companion document exact valid/invalid values, cross-field failures, consumer loading, and byte-hash behavior.

## 17. Change impact

Any YAML byte/value change requires policy/source review, affected config/result hashes, consumer tests, generated artifacts where applicable, and this companion SHA update.
