LANDSCOUT — DEV.CADASTRE.RUN.1
Premier parcours exécutable : cadastre vérifié → filtres existants → résultats consultables
Nature : développement applicatif. Un seul ticket actif. L'audit documentaire exhaustif est différé par décision de Souhaib ; les tests, les frontières de confiance et la revue restent obligatoires.
Ancrage	Valeur
Dépôt	hmsouhaib/landscout-ai
Checkout Codex attendu	C:\souhaib\landscout-ai
Base exacte approuvée pour ce départ	e25a8cca80ccd476226e03f84649dc0fdd19c979
Parent de cette base, R16	2f2dabe99825989f5fee8093dc7d5aeb129fce89
Branche de départ à préserver	recovery/docs-continuity-1-partial
Nouvelle branche de développement autorisée à Codex	dev/cadastre-run-1
Main local / suivi / serveur à préserver	aa4ebc7063f2abdfcbae95154ba89b5b1a0dba02


DEV.CADASTRE.RUN.1 est un nouvel identifiant explicite d'intégration applicative. Il n'est ni un ancien STEP retrouvé, ni une approbation de 7F.1C.1, ni un R17 documentaire.
1. Décision utilisateur et reçu de revue
Décision actuelle de Souhaib : « on contuine le dev mnt apres on reprend les doc ». Elle remplace, pour le travail suivant, l'obligation d'enchaîner des lots documentaires avant tout développement. Elle ne supprime pas la cible complète SCAN → FILTER → ANALYZE → SCORE → IDENTIFY → EXPORT → HUMAN, n'approuve pas les significations EP inconnues et ne rend pas le dépôt globalement audité.
Revue indépendante fournie : APPROVED — correctif documentaire R16.1 à e25a8cca80ccd476226e03f84649dc0fdd19c979. R16-REV01, R16-REV02 et R16-REV03 sont levées ; R16 corrigé est accepté dans le périmètre déjà examiné.
Le reviewer a vérifié la publication, son parent direct, les sept chemins documentaires, les cinq descriptions de types, les deux preuves de tests, les cinq cellules d'effets, la précision conditionnelle du callback et les huit notes propriétaires modifiées, à partir du patch et des corps RTE déjà lus. Les gardes isinstance(int)/exclusion de bool, les assertions .part/.geojson, l'échec sur les métadonnées et les réaffectations conditionnelles nonlocal correspondent au code. Le delta ne modifie pas le Python ou les tests. L'ancienne provenance et les états sont conservés ; les deux bindings de compagnons sont actualisés dans le patch. Aucune nouvelle erreur bloquante n'est établie dans cette correction.
Limites : pas de pytest, import LandScout ou auditeur INDEX exécuté par le reviewer ; pas d'attestation du disque Windows, des logs/manifeste locaux, ni de recalcul exhaustif des SHA/snapshots. Le reçu R16.1 rapporte une unique exécution INDEX, sortie native 1, completed=true, 10 204 constats, suivie d'une complétion distincte du reçu. Ces résultats sont REPORTED_EXECUTION, pas une validation de l'arbre final. L'identité avec le Markdown initial du chat n'est pas certifiée : le reçu qualifie uniquement la représentation effectivement reçue par Codex. Gain du correctif : zéro. Totaux historiques rapportés inchangés : 115/245 fichiers, 3 475/4 769 symboles.
Consigner une seule fois dans l'état courant : audit global PARTIAL, poursuite exhaustive PAUSED_BY_USER_FOR_DEVELOPMENT. Les anciens reçus et leurs PENDING historiques ne sont pas réécrits. Ce report ne ferme aucune lacune de lecture globale.
2. Résultat à implémenter — du code, pas un dossier de préparation
Livrer une commande locale qui charge le scan et son profil, obtient une source cadastrale vérifiée, applique réellement les filtres de surface et de forme existants, puis produit les parcelles retenues, les rejets explicables et le manifeste d'exécution.
Il s'agit du premier segment intégré, pas du moteur complet. Les domaines réseau, routes, urbanisme, environnement, score et propriétaires sont NOT_RUN dans ce parcours, même lorsque des briques existent ailleurs. Aucun classement de faisabilité BESS n'est annoncé.
Le profil actuel porte déjà : surface 2 000–15 000 m², largeur minimale 15 m, ratio maximal 10, shape_screening.enabled=true et calibration muret_empirical_v1. Charger ces valeurs depuis les fichiers ; ne pas les dupliquer dans le runner ni les recalibrer. La configuration actuelle vise Muret 31395.
Commande attendue après implémentation, depuis la racine du projet :
.venv\Scripts\python.exe -B -X utf8 -m landscout scan `
  --scan configs/scans/bess_muret.yaml `
  --cache-dir data/cache/cadastre `
  --output outputs/muret-premier-run `
  --offline
Un dossier de sortie déjà existant doit être refusé, jamais écrasé. L'exemple n'est pas une commande déclarée déjà disponible ou exécutée.
3. Implémentation bornée
A. Accès cache seul sans contournement de l'adaptateur
Dans download_cadastre_parcelles, ajouter uniquement un paramètre keyword-only allow_download: bool = True, contrôlé comme bool exact. Les appels existants et leur comportement par défaut restent compatibles.
Conserver l'ordre des gardes : paramètres, commune/URL officielle, chemins primaires sûrs, récupération .bak, validation du cache. Sur un cache valable, retourner le CadastreDownload habituel. Sur un cache absent/invalide/expiré et allow_download=False, lever une erreur contrôlée CadastreDownloadError avant mkdir, préparation/suppression des .part, réseau ou publication. Ne pas fabriquer un envelope dans le runner ou lui faire appeler les helpers privés de cache.
Le mode offline ne veut pas dire « accepter un cache périmé » : âge, UTC, taille, SHA, gzip et identité restent contrôlés. Exposer éventuellement --max-cache-age-hours, défaut 168, en réutilisant la validation existante. Ne pas élargir silencieusement ce seuil pour faire réussir un exemple.
La CLI est offline par défaut. --offline et --allow-download sont mutuellement exclusifs ; le second autorise à l'exécution uniquement l'acquisition cadastrale de la commune du scan, via l'adaptateur existant. Dans ce ticket, les tests de ce mode restent simulés : aucun téléchargement réel n'est demandé à Codex.
B. Prérequis A-001 explicitement inclus dans ce ticket fonctionnel
Dans common/cadastre_contract.py::validate_normalized_cadastre_parcels, rendre effective l'exigence déjà prévue « exactement 2D » pour les Polygon/MultiPolygon non nuls : refuser XYZ, XYM et XYZM. Le has_z actuel ne suffit pas. Réutiliser un contrôle dimensionnel Shapely supporté par l'environnement verrouillé ; geo/geometry.py utilise déjà get_coordinate_dimension.
Aucun force_2d, changement de CRS, réparation, trim, suppression d'une ligne ou modification des tolérances de surface. Préserver les Polygon/MultiPolygon XY, les géométries nulles/vides ordinaires classées INVALID, le contrôle des identifiants, les areas et le type d'erreur existant. Ce correctif vise le contrat intrinsèque A-001, pas une promesse que tous les lecteurs externes préservent chaque dimension.
Tests nouveaux isolés : XY accepté et rendu inchangé ; XYZ/XYM/XYZM rejetés pour Polygon et MultiPolygon avec géométries et surfaces autrement cohérentes ; null/empty/invalid XY conservés selon leur contrat. Vérifier que les fixtures M conservent réellement M avant l'appel, sans skip masquant une incapacité du toolchain. Ne pas invoquer l'acquisition officielle pour reproduire A-001.
A-002/A-003/A-004 restent hors périmètre. A-001 ne devient pas « indépendamment approuvé » dans le reçu Codex : indiquer correctif implémenté/testé, revue pendante.
C. Runner de bibliothèque et CLI
Créer une couche landscout.workflows, dépendant des API existantes, sans dépendance inverse des stages vers la CLI. Entrée indicative à fixer et tester :
run_cadastre_screening(
    scan_path: Path,
    *,
    cache_dir: Path | None = None,
    output_dir: Path | None = None,
    allow_download: bool = False,
    max_cache_age_hours: float = 168.0,
) -> CadastreScreeningRunResult
L'API reçoit un chemin de configuration, pas un DataFrame déclaré « trusted » par l'appelant. Recharger via load_scan_config. Première version : un scan FR/BESS à une commune ; refuser explicitement une autre identité ou plusieurs communes avant acquisition/écriture, sans ignorer des communes. Ne pas restreindre le modèle commun ou prétendre couvrir toutes les AOI futures.
Ordre obligatoire :
load_scan_config
→ download_cadastre_parcelles(..., allow_download=...)
→ load_cadastre_parcels
→ normalize_cadastre_parcels
→ filter_parcels_by_area : (candidates, rejected)
→ enrich_parcel_shapes(candidates)
→ filter_parcels_by_shape : (retained, rejected)
→ contrôles de partition + export
Les signatures et ordres de tuples ne changent pas. Ne pas recalculer autrement les métriques, la sélection ou les motifs. Conserver la géométrie stockée EPSG:4326 et les calculs EPSG:2154. Les centroids du stage ne sont ni des adresses ni des points d'accès. Si la politique de forme est désactivée, préserver le comportement du filtre existant et l'indiquer ; aucune exclusion de forme supplémentaire inventée.
Preuves de partition obligatoires par identifiants uniques : total normalisé = rejet surface + rejet forme + retenu, sans doublon, intersection ou perte. Une erreur de lecture n'est pas zéro parcelle ; zéro candidat après filtres est en revanche un succès valide, avec fichiers vides à schéma stable.
Résoudre les chemins explicitement. Le chargeur actuel attend la disposition configs/scans/… et résout le profil depuis scan_path.resolve().parents[2] : préserver/documenter cette convention, pas de refonte de config. Chemins cache/output relatifs résolus contre cette racine ; chemins absolus conservés après validation. Résultat contenant les chemins créés et comptes effectifs, sans état global mutable.
__main__.py appelle une CLI argparse fine. --help ne déclenche ni run ni écriture. Code 0 seulement après export complet ; erreur d'usage 2 ; échec contrôlé du run 1 avec message exploitable sur stderr. Pas de catch qui transforme une erreur en succès ou relance un téléchargement en cache-only.
D. Sorties exploitables et preuves
Créer quatre fichiers sous un répertoire neuf réservé exclusivement à ce run :
Fichier	Contenu
candidates.csv	Parcelles retenues par les filtres exécutés, identités et métriques disponibles.
rejections.csv	Tous les rejets ; étape AREA/SHAPE et code de motif exact fourni par le filtre.
candidates.geojson	Même ensemble de parcelles retenues, géométries WGS84 conservées ; FeatureCollection vide autorisée.
run.json	Manifeste versionné du parcours réellement exécuté, écrit en dernier.


CSV avec ordre de colonnes explicite et stable : identité cadastrale, geometry_status, area_m2, shape_status, length_m, width_m, length_width_ratio, compactness, centroid_lat, centroid_lon, puis statut/étape/motif de présélection. Garder les identifiants comme chaînes ; ne pas exporter arbitrairement tous les attributs de source. Pour les lignes rejetées avant métriques de forme, valeurs indisponibles laissées nulles, pas zéro et pas de centroid inventé. Qualifier la présélection comme RETAINED_BY_EXECUTED_FILTERS, jamais « parcelle BESS validée ».
La présentation peut trier les exports par parcel_id, sans modifier les frames intermédiaires ; documenter et tester cet ordre. Les motifs AREA et SHAPE gardent leurs chaînes exactes et leur étape d'origine. Vérifier l'égalité des ID CSV/GeoJSON et la partition complète avec les rejets.
run.json : schema_version, statut de complétion de ce parcours, périmètre CADASTRE_AREA_SHAPE_ONLY, commune, horodatages UTC, identités/hashes des fichiers scan/profil utilisés, valeurs de filtre effectivement chargées, archive/source_url/taille/SHA/timestamp/cache_hit, comptes par étape/motif, liste des trois fichiers de données avec tailles/SHA, et domaines non exécutés à NOT_RUN. Aucune capacité, score, coordonnées de propriétaire ou conclusion environnementale. Les hashes locaux ne sont pas des checksums officiels de l'éditeur.
Utiliser un JSON strict sans NaN/Infinity ; convertir explicitement les nulls et scalaires des colonnes définies, jamais default=str généralisé. Pas de hash circulaire de run.json. Distinguer répétabilité des lignes de données et métadonnées variables d'exécution.
Capturer les identités de configuration autour du chargement et vérifier leur stabilité avant publication ; une mutation persistante fait échouer le run. Ne pas appeler cela un snapshot immuable sans implémenter un tel mécanisme. Garder la revalidation physique publique du cadastre ; une vérification finale via revalidate_cadastre_parcel_source est autorisée pour refuser une mutation persistante après calcul, sans remplacer sa comparaison par une chaîne SHA déclarée.
Répertoire final absent au départ, refus des liens/jonctions à la destination et des collisions avec caches/chemins suivis. Aucune suppression/réécriture d'une sortie préexistante ou d'un cache. Si l'écriture échoue, pas de manifeste COMPLETE ; préserver ou nettoyer seulement les fichiers créés par ce run et indiquer le répertoire incomplet. Cette publication par marqueur final n'est pas une transaction multi-fichiers atomique.
4. Fichiers autorisés et documentation minimale
Code :
- nouveaux src/landscout/__main__.py, src/landscout/cli.py, src/landscout/workflows/__init__.py, src/landscout/workflows/cadastre_screening.py ;
- src/landscout/sources/cadastre_fr.py : paramètre/garde cache-only seulement ;
- src/landscout/common/cadastre_contract.py : A-001 seulement.
Tests :
- tests/unit/test_cadastre_fr.py : ajouter les régressions offline/compatibilité sans affaiblir les tests existants ;
- nouveaux tests/unit/test_cadastre_screening.py, tests/unit/test_cadastre_cli.py, tests/unit/test_cadastre_contract_dimensions.py.
Continuité minimale, pas nouvel audit :
- docs/project/tickets/DEV.CADASTRE.RUN.1.md : ticket reçu ;
- docs/usage/cadastre_screening.md : commande, schémas, limites et exemples réels/synthétiques distincts ;
- docs/DEV_LOG.md : entrée courte code/tests/run/résultats/limites ;
- docs/project/CURRENT_STATE.md : décision utilisateur, approbation R16.1, ticket DEV courant et audit différé ;
- docs/project/BACKLOG_AND_GAPS.md : statut W-001 différé par utilisateur, A-001 implémenté sous revue, reste inchangé ;
- les deux compagnons de cadastre_fr.py et common/cadastre_contract.py : un bandeau court de delta DEV/obsolescence partielle renvoyant au contrat d'usage, sans re-génération de snapshots ni promotion CHECKED. Leurs anciennes références ne doivent pas être présentées comme entièrement synchronisées au nouveau code.
Tous les autres fichiers restent inchangés, notamment pyproject.toml, uv.lock, sécurité HTTP/cache, autres adaptateurs/stages, politiques, reçus historiques, registres d'audit et manifestes protégés. Aucun correctif RTE/PLU/EP, orchestrateur général, UI web, score, collecte de contacts ou CI/PR.
Les 106 fichiers du manifeste sont une preuve historique : les exceptions d'écriture applicatives nommées ci-dessus sont expressément autorisées pour ce nouveau ticket fonctionnel. Vérifier les autres fichiers inchangés ; ne pas falsifier le manifeste ni déclarer « 106 inchangés » si une exception autorisée est modifiée.
5. Lectures et validations adaptées au développement
Réutiliser les sources identiques déjà lues. Lire les tests et dépendances effectivement modifiés, les fonctions appelées et le ticket, sans recréer l'inventaire complet ou l'audit documentaire. Le reviewer a lu la configuration, source/cache/loader cadastral, normalisation, contrat partagé, filtres, forme et géométrie ; il a commencé les tests cadastral/normalisation, pas certifié toute leur suite.
Tests nouveaux probants
1. Cache-only : cache frais valide utilisé avec zéro réseau ; absent, expiré, invalide, mauvais SHA/gzip, présence de .bak et chemins unsafe refusés sans acquisition ni destruction. Vérifier le bool exact. Mode historique/default et mode explicitement autorisé conservent leur comportement.
2. Intégration physique synthétique : créer un vrai GeoJSON cadastral gzip et un sidecar cohérent, avec identités canoniques, vrais Polygon/MultiPolygon, null/invalide et parcelles de tailles/formes contrastées. Exécuter les vrais loader/revalidation/normalisation/filtres/metrics/export. Seul le transport est remplacé par une sentinelle interdisant le réseau. Ne pas importer la fixture autouse _physical_revalidation_stub de test_normalize_cadastre.py pour en faire une preuve end-to-end.
3. Vérifier sélection/motifs, métriques connues ou comparées aux vrais stages, fermeture de partition, ordre, CSV/GeoJSON, JSON strict, digests réels, non-mutation des sources/configurations, zéro candidat, politique shape désactivée et erreur de configuration.
4. A-001 : cas dimensionnels ci-dessus ; distinguer test intrinsèque en mémoire et intégration physique GeoJSON, qui ne constitue pas une preuve de conservation d'une source M officielle.
5. Échec d'écriture injecté et répertoire existant/symlink simulé : aucun succès publié, aucun ancien fichier écrasé. Mutation persistante de source/configuration rejetée.
6. CLI en sous-processus réel avec cache synthétique et configuration dans la disposition attendue : --help, succès, échec offline et erreurs d'usage. Pas de shell non nécessaire ; timeout borné ; attendre la terminaison et vérifier le code de sortie. Les doubles complémentaires ne sont pas présentés comme des liens Windows réels.
Une campagne pytest ciblée, environnement existant, basetemp court neuf, sans installation ni full-suite :
$run = Join-Path $env:LOCALAPPDATA ("LandScout\pytest-runs\dcr1-" + [guid]::NewGuid().ToString('N').Substring(0,8))
.venv\Scripts\python.exe -B -X utf8 -m pytest -q `
  tests/unit/test_cadastre_fr.py `
  tests/unit/test_cadastre_loader_fr.py `
  tests/unit/test_normalize_cadastre.py `
  tests/unit/test_config.py `
  tests/unit/test_filter_parcels.py `
  tests/unit/test_filter_shape.py `
  tests/unit/test_enrich_shape.py `
  tests/unit/test_cadastre_contract_dimensions.py `
  tests/unit/test_cadastre_screening.py `
  tests/unit/test_cadastre_cli.py `
  --basetemp $run
$code = $LASTEXITCODE
Conserver stdout/stderr hors Git, commande, environnement, passes/échecs/warnings/skips et sortie native après cleanup. Corriger puis rejouer uniquement les tests affectés si nécessaire ; garder l'historique, ne pas maquiller un échec. Ruff sur les seuls fichiers Python changés/nouveaux, sans --fix global ; git diff --check sur le nouveau delta. Ne pas réouvrir les anciennes exceptions EOL/whitespace.
Aucun auditeur documentaire INDEX n'est requis dans ce ticket. Les registres globalement partiels ne sont ni remis à zéro ni artificiellement réparés pour obtenir du vert. Les vieux fingerprints invalidés par le développement restent explicitement à réconcilier lors de la reprise documentaire.
Essai réel Muret, seulement si les données locales conviennent
Une exécution offline sur le cache Muret déjà présent est autorisée, avec sortie neuve non suivie. Si le cache est absent/expiré/invalide, consigner le blocage exact : ne pas changer le timestamp, le SHA ou l'âge par défaut, et ne pas télécharger implicitement. Les tests synthétiques peuvent prouver l'implémentation ; ils ne prouvent pas une exécution réussie sur les vraies parcelles. Rapporter séparément SYNTHETIC_END_TO_END et REAL_MURET_OFFLINE_RUN (exécuté ou non).
6. Publication et arrêt
Avant modification, vérifier racine, base, index/worktree, suivi, état Git et références distantes. Depuis la base propre vérifiée, Codex est autorisé à créer dev/cadastre-run-1 :
git switch -c dev/cadastre-run-1 e25a8cca80ccd476226e03f84649dc0fdd19c979
Si cette branche existe déjà pour la reprise de ce ticket, vérifier sa filiation et reprendre ses changements identifiables. Sinon, conflit ou divergence : conserver les données et signaler, pas reset/merge/rebase/amend/stash/clean/force-push. Ne pas modifier recovery pour la faire suivre le développement.
Terminé localement lorsque la CLI et l'API existent réellement, les partitions/exports/provenances sont testés, cache-only est sans réseau sur échec comme sur succès, A-001 est corrigé dans son périmètre, les régressions ciblées passent après cleanup et les limites du run réel sont exactes. Une liste de fichiers ou un plan sans code n'est pas une complétion.
Stager explicitement les seuls fichiers autorisés réellement modifiés. Ni sorties, ni caches, ni scripts temporaires/logs dans Git. Commit sur la branche DEV puis push de cette branche uniquement ; aucun push/merge vers main ou recovery. Relever le SHA réel après commit et comparer référence serveur/suivi, ainsi que main/recovery inchangés. Pas de SHA futur dans les propres octets du reçu.
Rapport final : SHA et fichiers, fonctionnalités effectivement implémentées, tests et codes de sortie, chemins des exemples, comptes réels ou absence de run réel motivée, défauts restant ouverts. Statut :
DEV.CADASTRE.RUN.1 completed — functional cadastre screening slice; independent review pending; global documentation audit PARTIAL and deferred by user.

STOP pour revue. Aucun second ticket en parallèle. L'intégration ultérieure réseau/routes/PLU/environnement, puis score/identification/livraison complète, reste à piloter avec ses propres exigences et preuves ; ce ticket n'en revendique pas l'achèvement.