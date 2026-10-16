LANDSCOUT — DEV.ROAD.RUN.1
Intégrer la proximité routière par classe et ses limites de couverture
Un seul ticket fonctionnel. Audit documentaire global PARTIAL et différé par Souhaib. Aucun changement de sélection cadastrale, de politique routière ou de seuil métier.
Ancrage	Valeur
Dépôt	hmsouhaib/landscout-ai
Checkout Codex	C:\souhaib\landscout-ai
Branche existante autorisée	dev/cadastre-run-1
HEAD de départ requis	ce9cb34604622bf5988fa5cd01c6d9d55ca3dd08
Parent direct de ce HEAD	4550ca0777fd4acfa26405b51a64eaf25b25b49d
Recovery à préserver	recovery/docs-continuity-1-partial à e25a8cca80ccd476226e03f84649dc0fdd19c979
Main à préserver	aa4ebc7063f2abdfcbae95154ba89b5b1a0dba02


Vérifier les références et l'état local avant édition. Continuer sur cette branche DEV ; ne pas créer de branche, déplacer main/recovery, merger, rebaser, amender, reset/restore/clean/stash ou force-push. Une divergence doit être expliquée et le travail préservé.
1. Reçu de la revue précédente
APPROVED — DEV.GRID.RUN.1 au SHA de départ ci-dessus, dans le périmètre optionnel de proximité électrique IGN et de couverture. Aucun correctif préalable n'est demandé. Les deux adaptations autorisées sont acceptées : relecture électrique via le chargeur public avec comparaison complète ; restauration de l'index parcellaire uniquement sur une copie, après contrôle de la séquence des identifiants et avant comparaison du préfixe cadastral.
Le reviewer a vérifié la publication, le parent direct, les références serveur et les 13 chemins du delta. Les scripts locaux dgr1_example.py et dgr1_verify.py mentionnés dans l'aperçu d'éditeur ne figurent pas dans ce delta publié ; cet aperçu n'est pas assimilé à la liste du commit. Lecture des deux workflows actuels, CLI, nouveau test grid complet, tests CLI complets, ajouts IGN, gardes des deux permissions et documents de continuité modifiés ; réutilisation des corps source/stages/tests inchangés déjà lus. Les nouveaux modes False s'arrêtent avant préparation réseau/extraction ; le workflow conserve les API physiques, la sélection, le schéma 1 et le marqueur final. Les comparaisons de couches/index/préfixe et les tests synthétiques sont cohérents avec le ticket et ses précisions.
REPORTED_EXECUTION, pas exécution du reviewer : 978 passes avec un warning décrit comme préexistant, sortie native 0 après cleanup ; suivi ciblé de 2 passes dont un nouveau cas, soit 979 cas distincts rapportés sur les deux campagnes, pas une campagne complète de 979 cas rejouée au dernier état. Exemple synthétique rapporté : 8 normalisées = 4 AREA rejetées + 2 SHAPE rejetées + 2 retenues ; quatre paires parcelle/tension pour 63 et 132,5 kV, ex æquo et diagnostics de couverture. Les comptes/valeurs sont confrontés aux fixtures et assertions, pas recalculés sur les sorties Windows par le reviewer.
Limites : aucun pytest/CLI LandScout, auditeur INDEX, téléchargement, rendu ou attestation du disque/index Windows exécuté par le reviewer. Pas de nouvelle certification exhaustive des fichiers protégés ou des snapshots documentaires. Le run réel Muret GRID est NOT_RUN : cache cadastral ancien/invalide, cache IGN expiré ; les liens C:/souhaib/... ne sont pas des fichiers accessibles au reviewer. L'approbation n'établit ni un succès réel sur Muret ni une capacité/raccordabilité. A-001 reste accepté dans son périmètre cadastral ; A-002/A-003/A-004 et les questions EP restent ouverts. Aucun gain de couverture documentaire.
Porter un renvoi successoral vers ce reçu dans CURRENT_STATE, sans réécrire les tickets ou résultats historiques. La réappropriation technique continue ; l'audit documentaire exhaustif n'est pas réactivé.
2. Résultat produit à livrer
Ajouter --with-roads à python -m landscout scan, utilisable avec ou sans --with-grid. Pour chaque parcelle retenue par les filtres existants, exporter la proximité routière par classe de proxy, ses motifs/preuves, ses ex æquo et sa limite de couverture.
La fonctionnalité réutilise la politique actuelle ign_bdtopo_general_vehicle_proxy_v2. Elle ne démontre ni accès légal, servitude, desserte effective d'une entrée, itinéraire praticable, ni accès poids lourd/chantier. Préserver heavy_vehicle_access=NOT_PROVEN. Aucune nouvelle exclusion de parcelle, préférence entre classes, distance maximale ou règle BESS.
Commande cible combinée :
.venv\Scripts\python.exe -B -X utf8 -m landscout scan `
  --scan configs/scans/bess_muret.yaml `
  --cache-dir data/cache/cadastre `
  --output outputs/muret-cadastre-grid-roads `
  --with-grid --with-roads `
  --ign-config configs/sources/ign_bdtopo_fr.yaml `
  --road-policy configs/access/ign_bdtopo_vehicle_proxy_policy.yaml `
  --offline
Cette commande est une cible, pas un run déjà effectué. Sans --with-grid, la route peut être analysée indépendamment de la présence de géométries électriques utilisables ; les quatre rôles physiques exigés par l'extraction IGN restent obligatoires.
3. Contrats existants effectivement vérifiés
API publique à utiliser, sans la remplacer par ses helpers internes :
load_ign_bdtopo_roads(extraction, config) -> IgnBdTopoRoadData

assess_road_proximity_coverage(
    parcels: GeoDataFrame,
    road_source: IgnBdTopoRoadData,
    source_config: IgnBdTopoSourceConfig,
    policy_path: Path | None = None,
) -> RoadProximityCoverageAssessmentResult
Le résultat contient parcels, class_proximity, class_coverage, source_coverage. Ici, parcels conserve les colonnes, l'ordre, les types, l'index et la géométrie d'entrée. Les distances et diagnostics sont dans class_proximity, pas dans des groupes scalaires ajoutés à la frame parcellaire. Ne pas transposer le schéma du grid.
L'assessment public appelle enrich_parcel_road_proximity, qui appelle l'application de politique, laquelle normalise/revalide la source routière. L'assessment recharge aussi la politique pour contrôler sa filiation et la couverture départementale depuis la même extraction. Appeler l'assessment une seule fois par run routier ; pas de normalisation/application/proximité supplémentaire dans le workflow. Les relectures de contrôle finales restent distinctes des calculs.
La politique expose six classes dans policy.classes.values. Cinq sont admissibles au calcul de distance ; NOT_DISTANCE_PROXY ne reçoit aucune ligne de proximité. Une classe admissible sans objet conserve une ligne par parcelle avec sélection/distance/ex æquo nuls et diagnostic NO_MATCH. Ce n'est pas une absence nationale de routes. Un ensemble où tous les objets sont NOT_DISTANCE_PROXY doit suivre le comportement valide des API existantes, pas être assimilé automatiquement à une erreur d'acquisition.
La sélection à égalité est celle du stage, pas un nouveau tri métier. Les mesures concernent la parcelle entière et des copies de calcul XY en EPSG:2154 ; aucune distance depuis le centroid n'est substituée.
4. Intégration et partage IGN minimal
Options et compatibilité
Étendre l'API existante avec les seuls nouveaux arguments keyword-only :
with_roads: bool = False
road_policy_path: Path | None = None
with_roads est un bool exact. Les options IGN sont autorisées lorsque grid OU roads est demandé ; sans aucun des deux, erreur explicite. road_policy_path sans roads est une erreur, jamais une option ignorée. Même règle CLI (--road-policy) : usage invalide → 2 ; échec contrôlé de run → 1 ; succès complet → 0. --help ne déclenche pas de run/écriture.
Le défaut de politique de cette nouvelle couche est explicitement root / "configs/access/ign_bdtopo_vehicle_proxy_policy.yaml", où root est la racine résolue du scan. Ce choix du workflow est déclaré ; ne pas importer _DEFAULT_POLICY_PATH, ni prétendre que le défaut historique du chargeur est relatif au scan. Passer le chemin absolu validé explicitement à load_ign_road_vehicle_proxy_policy et à l'assessment, pour éviter qu'ils lisent deux fichiers différents.
Contexte physique partagé
Factorisation interne minimale autorisée dans workflows/ign_screening.py : préflight IGN existant, résolution du contexte archive/extraction et contrôles communs. Ce n'est pas un orchestrateur générique ni une nouvelle source de vérité.
- Avant toute acquisition cadastrale/écriture : valider options, FR/BESS/commune, département IGN, config et politique demandées, leurs bindings et les collisions de chemins. La politique doit être chargée même pour zéro retenue ; ses invalidités ne sont pas masquées.
- Calculer une seule fois la partition cadastrale. Chaque analyse optionnelle reçoit le même retained cadastral, non le résultat enrichi de l'autre analyse.
- Pour un retained non vide et au moins une analyse IGN, obtenir une fois le contexte archive/extraction par les API existantes, avec allow_download=False et allow_extract=False. Grid et roads emploient exactement la même extraction si les deux sont demandés. Les validations/relectures internes des stages restent actives : un seul contexte ne signifie pas une seule lecture disque.
- Si le mode roads seul est demandé, ne pas charger les couches électriques ni lancer leur assessment. La découverte globale des rôles IGN reste celle de l'adaptateur.
- Conserver le comportement accepté de grid (y compris restauration de son index). Pour roads, exiger l'index original sans restauration : le stage le préserve déjà.
- Les identifiants, rejets et motifs AREA/SHAPE restent identiques dans les quatre combinaisons d'options. Aucun COMPLETE intermédiaire, aucune réouverture des fichiers d'un run déjà terminé.
Les helpers internes à workflows peuvent être partagés entre ces nouveaux modules. Ne pas importer de nouveaux helpers privés de sources/stages ni modifier leurs signatures, leurs algorithmes ou leurs exports.
Préservation et revalidation finale
Les entrées restent des chemins/configurations puis des sources physiques, pas un CSV/GeoJSON prétendument fiable. Préserver les gardes cache/backup, les refus de liens/jonctions avant resolve, les destinations neuves et les collisions avec caches, extraction, politique, configs et chemins suivis. Une sortie préexistante n'est jamais remplacée. La factorisation conserve les garanties et scénarios de refus de DEV.GRID.RUN.1.
Capturer la politique avant chargement et vérifier son identité après chargement et avant COMPLETE ; confronter policy.config_sha256 aux octets capturés. Conserver scan/profil/IGN et les contrôles finaux cadastraux/grid.
Après export, pour roads :
1. Vérifier l'archive conservée par validate_ign_bdtopo_archive et comparer ses champs d'intégrité au téléchargement retenu, comme pour grid.
2. Relire via load_ign_bdtopo_roads(extraction, config). Il n'existe pas d'autorisation de promouvoir _revalidate_ign_bdtopo_road_data en API publique. Comparer la frame routière complète au bundle initial : colonnes/ordre, valeurs/types, index classe/noms/valeurs, géométrie active, CRS, WKB, attrs ; résumé complet de type attendu, rôle spatial et même extraction.
3. Relire la couverture par load_ign_bdtopo_department_coverage et comparer frame, résumé et filiation à celle réellement utilisée. En mode combiné, contrôler séparément les résultats de couverture utilisés par les deux branches, même si les lectures de vérification communes sont factorisées.
4. Vérifier les bindings du marker et des configurations/politique ; conserver les causes des erreurs. Aucun recalcul de distance pour valider ces octets.
Ces contrôles rejettent les mutations persistantes, pas toutes les courses transitoires. Aucun label « snapshot immuable » ou « transaction atomique globale » nouveau. Un échec d'une analyse demandée doit empêcher COMPLETE, sans succès cadastral silencieux.
5. Sorties et schéma 3
Options	Manifeste / fichiers
Ni grid ni roads	Schéma 1 et quatre fichiers strictement inchangés.
Grid seul	Schéma 2 et cinq fichiers strictement inchangés.
Roads seul	Schéma 3, scope CADASTRE_AREA_SHAPE_WITH_ROAD_PROXIES ; sorties cadastrales + road_proximity.csv.
Grid + roads	Schéma 3, scope CADASTRE_AREA_SHAPE_WITH_GRID_AND_ROAD_PROXIES ; sorties grid + road_proximity.csv.


candidates.csv, ses propriétés GeoJSON et rejections.csv conservent leurs contrats cadastral/grid. Les routes ne sont pas aplaties en un « nearest road » global inventé. road_proximity.csv est la table explicable associée par parcel_id.
Son ordre de colonnes est CLASS_PROXIMITY_COLUMNS (déclaration existante de enrich_road_proximity.py), suivi explicitement des onze diagnostics produits par l'assessment :
road_source_boundary_distance_m
road_source_coverage_position
road_proximity_coverage_status
road_source_coverage_provider
road_source_coverage_product
road_source_coverage_department_code
road_source_coverage_edition
road_source_coverage_product_version
road_source_coverage_archive_sha256
road_source_coverage_layer
road_source_coverage_spatial_role
Les constantes _DIAGNOSTIC_COLUMNS / _COVERAGE_LINEAGE_COLUMNS du stage sont internes. Déclarer cette liste d'export dans workflows et la confronter au résultat ; ne pas les importer comme APIs publiques ou exporter un wildcard.
Avant tri, vérifier le tableau public complet : noms/ordre, absence de doublons, paires uniques, identifiants exacts, domaine parcelle × classes distance_eligible=True, y compris les classes vides. class_coverage couvre les six classes, dont NOT_DISTANCE_PROXY ; ne pas la compter comme une sixième classe de distances. Conserver les types/valeurs et le RangeIndex du résultat public, trier uniquement la copie d'export par parcel_id puis ordre des classes de la politique chargée. Vérifier la relecture de toutes les cellules écrites selon l'encodage explicite, pas uniquement les IDs.
Sérialisation routière par type/colonne :
- distances/largeurs numériques finies et nombres d'ex æquo entiers ; un bool ne devient jamais 0/1 dans ces colonnes ;
- nearest_road_toll_evidence est un booléen nullable, pas un nombre et pas une chaîne métier ; CSV true/false, null vide ;
- les faits nearest_private_raw peuvent être booléens ou nombres binaires selon la source : préserver leur nature, ne pas transformer les inconnues textuelles en booléens ;
- textes de statut, motifs, traces JSON textuelles et noms bruts inchangés ; pas de trim, default=str générique ou décodage/réécriture silencieuse de *_json ;
- vrais nulls → cellule vide / null JSON ; pas de NaN/Infinity JSON.
Ne pas réutiliser tel quel le sérialiseur grid qui refuse tous les booléens. Conserver les gardes des colonnes électriques en factorisant uniquement ce qui est réellement commun.
run.json ajoute le binding de la politique et roads : statut réel, politique/identité/schema/hash/scope/vehicle_scope/heavy_vehicle_access, archive/extraction/marker/GPKG/rôles/couverture utilisés et class_coverage (classe, compte, bool distance_eligible). Provenance explicite, pas asdict récursif de frames ni doublage opaque des enveloppes. En mode combiné, une section physique IGN commune est permise en schéma 3 avec références non ambiguës des deux branches ; le schéma 2 grid seul ne change pas.
Les quatre données en roads seul, ou les cinq données en mode combiné, reçoivent tailles/digests vérifiés. Pas de self-hash de run.json. roads quitte not_run seulement si son assessment a réussi ; les autres domaines non exécutés restent NOT_RUN.
Zéro retenue : configurations/options validées, pas d'accès archive/extraction ni assessment ; schéma 3, road_proximity.csv avec en-tête seul, roads.status=NOT_RUN, roads.reason=NO_RETAINED_PARCELS, aucune preuve physique ou couverture comptée inventée. Grid conserve son comportement vide actuel s'il est demandé. Une classe vide sur des parcelles non vides est au contraire une analyse exécutée avec des lignes NO_MATCH, pas NOT_RUN.
Ajouter seulement les champs Python optionnels nécessaires au résultat, après les anciens champs avec défauts compatibles (par exemple road_proximity_csv et roads_status).
6. Liste fermée des fichiers autorisés
Code (5 chemins)
- nouveau src/landscout/workflows/road_screening.py ;
- nouveau src/landscout/workflows/ign_screening.py, uniquement si nécessaire au partage borné du contexte et des vérifications ;
- src/landscout/workflows/grid_screening.py, adaptation interne minimale au contexte partagé sans modification de ses résultats ;
- src/landscout/workflows/cadastre_screening.py ;
- src/landscout/cli.py.
Tests (4 chemins)
- nouveau tests/unit/test_road_screening.py ;
- tests/unit/test_grid_screening.py, partage borné de préparation physique et régressions du contexte partagé ;
- tests/unit/test_cadastre_cli.py, options/combinaisons et vrais sous-processus ;
- tests/unit/test_cadastre_screening.py, seulement partage de fixture/régressions nécessaires, sans suppression ou affaiblissement des cas existants.
Continuité minimale (4 chemins)
- docs/project/tickets/DEV.ROAD.RUN.1.md, archiver la pièce réellement reçue en qualifiant son identité ;
- docs/usage/cadastre_screening.md, section roads/schéma 3 et limites ;
- docs/DEV_LOG.md, entrée code/tests/runs/limites ;
- docs/project/CURRENT_STATE.md, approbation grid et ticket actif, audit toujours différé.
Aucun autre fichier. Les adaptateurs, stages, politiques/YAML, pyproject/uv.lock, transport, registres d'audit, manifeste protégé et reçus historiques restent identiques au SHA de départ. Aucun correctif A-002/A-003/A-004, PLU/EP, score, UI, propriétaires ou CI. Si un défaut imprévu d'un stage empêche l'intégration, fournir sa preuve et arrêter l'élargissement, pas le contourner.
7. Lecture et validations
Lire les fichiers modifiés/nouveaux intégralement et les producteurs/consommateurs nécessaires ; réutiliser les octets inchangés déjà lus. Le reviewer a poursuivi les sources d'assessment/proximité/politique/application routières ; cela ne constitue ni revue complète de leurs tests/compagnons ni approbation anticipée de la nouvelle intégration.
Les anciennes fixtures grid contiennent une couche routière minimale suffisante pour la découverte des rôles, pas pour la normalisation routière complète. Préparer une petite vraie archive 7z et un GPKG contenant les champs requis par normalize_access_ign.py, avec le vrai dtype de chaque fait. Construire les données avant de les acquérir/extracter par les API en transport simulé ; ne pas modifier un cache déjà scellé puis désactiver les contrôles. Ne pas reprendre les stubs de normalisation ou aliases privés de certains tests historiques comme preuve end-to-end.
Régressions minimales :
1. Modes cadastral seul, grid seul, roads seul, combiné. Même sélection, motifs, géométries et données électriques qu'avant ; routes seules ne demandent aucun assessment/chargement électrique. Contexte archive/extraction partagé une fois en mode combiné, toutes revalidations conservées.
2. Fixtures physiques couvrant les six classes, distances sur polygone entier, distance zéro, égalités et départage du stage ; classes vides, tous objets NOT_DISTANCE_PROXY, faits unknown/restricted, péage bool vrai/faux/null et fait privé brut. Aucun changement de politique.
3. Diagnostics intérieur, distance atteignant/dépassant la marge, contact/croisement/hors couverture ; NO_MATCH reste distinct du diagnostic de position et d'une source inutilisable.
4. Index parcellaire non contigu nommé préservé tel quel par roads ; refus d'IDs réordonnés/perdus/dupliqués, faits/dtypes/WKB modifiés ; aucune restauration routière masquant une anomalie. Le comportement de restauration grid reste celui accepté.
5. Table publique/CSV cellule par cellule, schémas 1/2 inchangés, schéma 3, types/nulls/traces et ordre par classe ; paires complètes sans NOT_DISTANCE_PROXY ; hashes réels et sources/politique liées. Zéro retenue sans accès IGN ni faux COMPLETE de domaine.
6. Relecture routière finale : mutation de valeur/type/index/attrs/WKB/résumé/identité ; changements persistants archive/GPKG/marker/politique/YAML ; erreurs contrôlées avec causes et aucun manifeste COMPLETE. Tester aussi la garde policy avant acquisition.
7. Échec d'écriture CSV routier/manifeste, destinations préexistantes, collisions dont politique et symlink/junction simulés : aucune perte d'entrée, répertoire incomplet explicite. Les simulations ne deviennent pas de vraies attaques OS démontrées.
8. CLI en sous-processus avec sentinelles DNS/connexion dans l'enfant, codes 0/1/2, options incohérentes, manque de cache/extraction/politique et combinaisons ; --allow-download reste cadastral uniquement, IGN False/False en toute combinaison.
Une campagne ciblée dans l'environnement existant, sans installation/full-suite/INDEX documentaire :
$run = Join-Path $env:LOCALAPPDATA ("LandScout\pytest-runs\drr1-" + [guid]::NewGuid().ToString('N').Substring(0,8))
.venv\Scripts\python.exe -B -X utf8 -m pytest -q `
  tests/unit/test_cadastre_screening.py `
  tests/unit/test_cadastre_cli.py `
  tests/unit/test_grid_screening.py `
  tests/unit/test_ign_bdtopo_fr.py `
  tests/unit/test_normalize_access_ign.py `
  tests/unit/test_road_vehicle_proxy_policy.py `
  tests/unit/test_apply_road_vehicle_proxy_policy.py `
  tests/unit/test_enrich_road_proximity.py `
  tests/unit/test_assess_road_proximity_coverage.py `
  tests/unit/test_road_screening.py `
  --basetemp $run
$code = $LASTEXITCODE
Conserver stdout/stderr, commande, environnement, warning/skip/xfail et code natif final après cleanup hors Git ; garder les échecs intermédiaires et rejouer seulement les cas affectés après correction. Décompter les campagnes/cas distincts sans gonfler le total. Ruff/format uniquement sur les Python changés, git diff --check sur le delta neuf. Préserver les exceptions EOL/whitespace historiques.
Aucun téléchargement officiel ni ré-extraction volumineuse n'est autorisé par ce ticket. Un exemple synthétique consultable est obligatoire. Un essai réel Muret reste seulement conditionnel à des caches/extraction existants valides ; ne pas allonger l'âge, réécrire les timestamps/checksums ou fabriquer un sidecar pour passer. Sinon, résultat réel NOT_RUN avec cause précise. L'obstacle de données n'est pas une absence de fonctionnalité et reste à traiter séparément, sans l'effacer.
8. Fin, publication et arrêt
Terminé lorsque l'option routière fonctionne, les modes précédents restent compatibles, les preuves par classe/coverage sont exportées sans modifier la sélection, les contrôles/tests passent et les limites d'exécution réelle sont exactes. Pas de clôture par plan seul.
Stager explicitement les seuls chemins autorisés modifiés ; ni caches, sorties, scripts locaux de démonstration/vérification ou logs dans Git. Vérifier les chemins hors périmètre au SHA de départ. Les exceptions applicatives déjà approuvées au manifeste historique ne sont pas réécrites ou présentées comme toujours identiques au bootstrap.
Commit et push dev/cadastre-run-1 seulement, main/recovery inchangés. Relever le vrai SHA après commit et vérifier suivi/serveur, sans SHA futur/self-hash dans le reçu. Rapport code/fichiers/tests, parcours synthétique avec comptes/classes/données explicables, run réel ou NOT_RUN motivé, limites et défauts nouveaux éventuels.
DEV.ROAD.RUN.1 completed — optional source-bound road proximity by class and coverage slice; independent review pending; global documentation audit PARTIAL and deferred by user.

STOP pour revue. Aucun autre ticket en parallèle. La cible complète de LandScout reste inchangée ; ce lot ajoute une analyse utilisable, pas une conclusion d'accès légal ou poids lourd.