LANDSCOUT — DEV.GRID.RUN.1
Ajouter les preuves de proximité électrique IGN au parcours cadastral exécutable
Un seul ticket fonctionnel. Aucun R17 documentaire. Aucune modification des seuils métier, aucun score et aucune conclusion de raccordement.
Ancrage	Valeur
Dépôt	hmsouhaib/landscout-ai
Checkout Codex	C:\souhaib\landscout-ai
Branche de travail existante	dev/cadastre-run-1
HEAD de départ requis	4550ca0777fd4acfa26405b51a64eaf25b25b49d
Parent du HEAD de départ	e25a8cca80ccd476226e03f84649dc0fdd19c979
Recovery à préserver	recovery/docs-continuity-1-partial à e25a8cca80ccd476226e03f84649dc0fdd19c979
Main à préserver	aa4ebc7063f2abdfcbae95154ba89b5b1a0dba02


Poursuivre sur la branche DEV existante, sans nouvelle branche, merge ou déplacement de recovery. Vérifier les références, la filiation et l'état local avant édition ; conserver et expliquer toute divergence, sans reset/restore/clean/stash/rebase/amend/force-push.
1. Reçu indépendant du précédent lot
APPROVED — DEV.CADASTRE.RUN.1 à 4550ca0777fd4acfa26405b51a64eaf25b25b49d, dans le périmètre cadastral exécuté et documenté. Le correctif intrinsèque A-001 est accepté dans ce périmètre. Aucun défaut bloquant n'a été établi dans la revue ciblée.
La comparaison distante établit un descendant direct de la base approuvée et 17 chemins autorisés. Le reviewer a lu intégralement le nouveau workflow (487 lignes), la CLI et ses points d'entrée, les trois nouveaux fichiers de tests, les tests de l'adaptateur cadastral, le contrat dimensionnel modifié et le delta cache-only ; il a réutilisé les lecteurs, configuration, normalisation et filtres inchangés déjà lus. La documentation d'usage et les résultats publiés ont été confrontés. Le mode cache-only est refusé avant mkdir/.part/réseau sur un cache inutilisable. La chaîne emploie les API physiques existantes, vérifie les partitions, réécrit aucune géométrie et ne publie le marqueur qu'après contrôles et écriture. Les tests dimensionnels attestent leur fixture M avant l'appel ; leur preuve est intrinsèque, pas une garantie de conservation de M par tous les lecteurs externes.
Exécutions rapportées, non exécutées par le reviewer : campagne ciblée finale de 411 passes / 22,17 s / sortie native 0 après cleanup ; premier essai conservé, 211 passes et 200 erreurs de setup dues à WinError 5, sortie 1, puis reprise dans l'environnement existant. Exemple synthétique rapporté : 8 normalisées = 4 rejets AREA + 2 rejets SHAPE + 2 retenues. Essai réel Muret offline rapporté : sortie 1 ; sidecar ancien sans schema_version/commune_code, timestamp du 11 août 2026 ; pas de téléchargement, de falsification de fraîcheur ou de sortie complète.
Le reviewer n'a exécuté ni pytest, ni CLI LandScout, ni auditeur INDEX, ni acquisition ou rendu. Il n'atteste pas le checkout Windows, les logs ou les sorties locales ; il n'a pas recalculé le manifeste protégé complet. La représentation textuelle du ticket archivé a été confrontée ; l'identité byte-for-byte avec la pièce Markdown de ce chat n'est pas attestée. Ces limites ne deviennent pas une demande de reprise documentaire.
Porter une référence successorale vers ce reçu dans CURRENT_STATE et pour A-001 dans le backlog. Ne pas réécrire DEV.CADASTRE.RUN.1 ni ses résultats historiques. L'ancienne frontière 7F.1B.4 et son reçu manquant restent historiques ; cette nouvelle approbation porte seulement sur la tranche cadastrale. A-002/A-003/A-004 et la revue sémantique EP restent ouverts. Audit global PARTIAL et PAUSED_BY_USER_FOR_DEVELOPMENT, sans nouveau crédit de couverture.
2. Résultat utilisateur attendu
En activant une option de la commande existante, obtenir, pour chaque parcelle retenue par AREA/SHAPE, les distances aux lignes/postes IGN, la tension connue selon son statut, les identités des objets sélectionnés, les égalités de distance et les limites de couverture départementale. Exporter aussi le tableau des distances par tension exacte réellement présente dans la source.
La sélection cadastrale reste identique : aucune parcelle supplémentaire exclue, aucun tri de faisabilité, aucun seuil de distance ajouté. Une distance à un polygone de poste IGN n'est ni une capacité disponible, ni un point de raccordement RTE. NO_MATCH n'est pas « absence de réseau en France » ; BOUNDARY_LIMITED n'est pas une inaptitude de la parcelle.
Commande cible, offline et compatible avec l'ancien mode sans option :
.venv\Scripts\python.exe -B -X utf8 -m landscout scan `
  --scan configs/scans/bess_muret.yaml `
  --cache-dir data/cache/cadastre `
  --output outputs/muret-cadastre-grid `
  --with-grid `
  --ign-config configs/sources/ign_bdtopo_fr.yaml `
  --offline
Les chemins optionnels --ign-cache-dir et --ign-extraction-dir permettent de désigner les caches existants. Employer les défauts de l'adaptateur et de l'extracteur, résolus explicitement contre la racine du scan ; ne pas dupliquer des noms d'archives. Cette commande est une cible d'implémentation, pas un run déjà effectué.
3. Accès IGN borné : réutilisation vérifiée, sans reconstruction manuelle d'enveloppe
A. Deux permissions explicites et rétrocompatibles dans l'adaptateur
Ajouter à download_ign_bdtopo_archive un paramètre keyword-only allow_download: bool = True, contrôlé comme bool exact. Les appels historiques restent compatibles. Conserver configuration reconstruite, noms officiels/configurés, garde des backups et validation de cache/âge/identité/intégrité. Si le cache est absent/invalide/expiré et allow_download=False, lever IgnBdTopoDownloadError AVANT mkdir, préparation ou suppression des .part, réseau ou publication. Ne pas modifier les validations/checksums, rollback, cleanup, HTTPS ou règles de checksum existantes.
Ajouter à extract_ign_bdtopo_archive un paramètre keyword-only allow_extract: bool = True, bool exact, après les paramètres existants. Conserver la revalidation de l'archive et de la filiation, la garde .bak, les contrôles de cible/marker et la recherche d'une extraction réutilisable. Si cette recherche échoue et allow_extract=False, lever IgnBdTopoArchiveError AVANT mkdir, nettoyage de .part, extraction ou remplacement d'un répertoire. Le chemin historique autorisé reste inchangé.
Le nouveau parcours appelle ces deux API avec False, même si l'utilisateur autorise le téléchargement cadastral. Offline signifie ici lecture de l'archive et de l'extraction IGN déjà valides, pas acceptation d'un cache périmé. Aucun helper privé de cache n'est appelé par le workflow ; aucune enveloppe IGN déclarative n'y est fabriquée.
B. Autorisations de données
Aucun téléchargement officiel IGN/RTE/GPU/EP/cadastre, ni ré-extraction volumineuse officielle n'est demandé à Codex dans ce ticket. La permission existante --allow-download reste cadastrale uniquement ; ses tests utilisent un transport synthétique. Elle ne doit pas devenir une permission de télécharger l'archive IGN de près de 495 Mo déclarée dans le YAML.
Les fixtures de tests peuvent créer une petite archive 7z, la télécharger via transport simulé dans un cache neuf et l'extraire avec les modes historiques True afin de préparer un état réellement valide. Le parcours à tester consomme ensuite cet état avec transport interdit et allow_extract=False. Aucun timestamp ou SHA d'un cache officiel ne sera modifié pour faire réussir un exemple.
4. Intégration avant publication, sans nouvel orchestrateur général
Étendre run_cadastre_screening avec des paramètres keyword-only :
with_grid: bool = False
ign_config_path: Path | None = None
ign_cache_dir: Path | None = None
ign_extraction_dir: Path | None = None
Conserver tous les anciens arguments/défauts et le comportement du mode sans grille. with_grid doit être un bool exact. Des chemins IGN fournis sans with_grid=True constituent une erreur explicite : ne pas les ignorer. Même règle CLI, erreur d'usage 2 pour les combinaisons invalides, erreur de run contrôlée 1 pour les sources inutilisables.
Une implémentation ciblée dans workflows/grid_screening.py est autorisée pour isoler cette intégration. Elle reste interne à la couche workflows : pas de nouvelle API publique permettant de qualifier « source fiable » un CSV, GeoJSON ou DataFrame arbitraire fourni par l'appelant. Aucun stage ne dépend de la CLI.
Ordre et véritables interfaces
Reprendre le calcul cadastral accepté, sans le lancer une première fois pour publier COMPLETE puis rouvrir ses fichiers. Calculer les partitions une seule fois, conserver retained en mémoire et insérer l'analyse avant les écritures finales :
chargement et binding scan/profil (+ config IGN si demandée)
→ parcours cadastral existant jusqu'à retained / rejets
→ si retained non vide et with_grid :
    download_ign_bdtopo_archive(config, ..., allow_download=False)
    extract_ign_bdtopo_archive(download, config, ..., allow_extract=False)
    load_ign_bdtopo_electricity(extraction, config)
    assess_grid_coverage(retained, electricity_source, config)
→ contrôles de conservation + exports + contrôles physiques finaux
→ run.json écrit en dernier
L'API publique assess_grid_coverage appelle elle-même une fois enrich_parcel_grid_proximity, qui possède sa normalisation/revalidation, puis charge la couverture configurée depuis la même extraction. Ne pas recalculer la proximité dans le workflow, ne pas lui fournir un résultat de normalisation arbitraire, ne pas appeler _assess_grid_coverage_from_proximity ou _enrich_parcel_grid_proximity_from_normalized à la place des API publiques. Un appel Python n'est pas une promesse d'une seule lecture disque.
GridCoverageAssessmentResult contient parcels, voltage_level_proximity, voltage_level_coverage et source_coverage. Les objets figés peuvent contenir des DataFrames mutables ; ne pas leur attribuer une immuabilité profonde.
Entrées, conservation et validation finale
Avant acquisition ou écriture, valider FR/BESS, une commune, les chemins et la configuration IGN. Exiger la correspondance du département de la commune avec IgnBdTopoSourceConfig.department_code (y compris codes corses/ultramarins déjà admis, sans une règle naïve toujours sur deux chiffres). Refuser une inadéquation plutôt qu'utiliser le paquet d'un autre département. Les calculs restent ceux des stages ; le workflow n'élargit pas leur couverture géographique.
Capturer le binding du YAML IGN avant chargement, vérifier sa stabilité après et avant publication comme pour scan/profil. Préflight des destinations : résultat, caches cadastral/IGN, extraction, configs et chemins Git suivis ne peuvent pas se recouvrir dangereusement ; refuser liens/jonctions avant resolve, ne pas effacer une extraction existante. Les nouvelles gardes doivent protéger les fichiers préexistants, pas seulement détecter une collision après écriture.
Exiger mêmes IDs, ordre, index, CRS, géométrie et colonnes préexistantes entre retained et le préfixe du résultat grid ; comparer les scalaires/dtypes et WKB, sans recalculer les métriques différemment. L'ensemble des retenues/rejets et les motifs restent celui des filtres cadastraux. Trier seulement les copies d'export.
Après export et avant COMPLETE, conserver les contrôles cadastraux/configuration et vérifier la persistance des preuves IGN : archive via validate_ign_bdtopo_archive comparée au téléchargement retenu, électricité via revalidate_ign_bdtopo_electricity_data, couverture via son chargeur public à partir de la même extraction et comparaison à la couverture utilisée. Réutiliser les frontières publiques existantes, sans deuxième calcul de proximité et sans utiliser une validation locale comme substitut de relecture physique. Une mutation persistante de l'archive, GPKG, marker ou YAML fait échouer le run ; pas de garantie universelle contre les courses/transitoires.
Zéro retenue
Un scan sans retenue reste un succès cadastral valide. Dans ce cas, ne pas appeler un profiler qui refuse un ensemble vide et ne pas calculer de distances fictives. Si grid est demandé, publier le schéma étendu vide, avec grid.status=NOT_RUN, grid.reason=NO_RETAINED_PARCELS, aucune preuve IGN d'acquisition inventée. La validation de configuration et des options reste requise, mais pas l'accès archive/extraction. Les fichiers de données vides conservent leurs en-têtes.
5. Sorties versionnées, sans confondre voltage exact et précision géométrique
Sans --with-grid : conserver strictement le contrat schema_version=1, les quatre fichiers et leurs colonnes/comportements. Ajouter des champs uniquement optionnels au résultat Python, après les champs existants avec défauts compatibles si nécessaire.
Avec --with-grid : run.json.schema_version=2, scope CADASTRE_AREA_SHAPE_WITH_GRID_PROXIES. Le marqueur COMPLETE ne clôt que ce parcours. candidates.csv et les propriétés GeoJSON conservent le préfixe cadastral, puis ajoutent les colonnes grid suivantes dans un ordre déclaré et testé, conformément aux résultats existants :
- les trois groupes nearest_line_*, nearest_exact_line_*, nearest_post_* réellement produits par enrich_grid_proximity.py (distances, identités, tie_count, tension brute/statut/exacte/borne si applicable, attributs et filiation) ;
- PARCEL_DIAGNOSTIC_COLUMNS de assess_grid_coverage.py ;
- COVERAGE_LINEAGE_COLUMNS du même module.
Déclarer dans la couche d'export une liste explicite de colonnes autorisées, confrontée aux producteurs ; ne pas exporter tous les attributs inconnus avec un wildcard à l'exécution, ni importer un helper privé de calcul pour découvrir le schéma. Conserver les noms existants, ne pas inventer des champs RTE/capacité. Le terme nearest_exact_line désigne une tension exacte dans le modèle, pas une géométrie certifiée exacte.
rejections.csv garde son schéma cadastral : grid n'a pas été calculé pour ces lignes. Ajouter un quatrième fichier de données voltage_proximity.csv, ordonné par (parcel_id, voltage_kv), avec les colonnes existantes VOLTAGE_PROXIMITY_COLUMNS, VOLTAGE_DIAGNOSTIC_COLUMNS, COVERAGE_LINEAGE_COLUMNS, sans doublons. Les tensions viennent dynamiquement de voltage_level_coverage, pas d'une liste fixée par le workflow. Vérifier unicité des paires, leur couverture réelle et conservation des valeurs du tableau public ; distinguer zéro tension exacte et source invalide.
Statuts à préserver : NOT_BOUNDARY_LIMITED, BOUNDARY_LIMITED, OUTSIDE_OR_CROSSING_COVERAGE, NO_MATCH. Ne pas les remplacer par bon/mauvais/éligible ; ne pas remplacer un null par zéro. Préserver les départages/tie_count établis. Encoder les entiers comme entiers, les nombres finis comme nombres, les textes comme textes et les vrais nulls comme null/CSV vide. Pas de conversion générique default=str ni de sérialisation NaN/Infinity. Les booléens ne deviennent pas des distances.
Le manifeste conserve toutes les preuves cadastrales et ajoute : binding du YAML IGN, identité de l'archive réellement vérifiée, indicateur cache_hit, extraction et GPKG réellement utilisés et leurs tailles/hashes déjà contrôlés, rôles/couches, source/édition/département/projection, couverture source et niveaux de tension observés. Ne pas sérialiser récursivement toute une dataclass contenant les frames avec asdict ; extraire un contrat de provenance explicite. Pas de self-hash. Les quatre données exportées ont leurs tailles/digests vérifiés.
Quand l'analyse électrique a réellement tourné, grid.status=COMPLETE et grid sort de not_run. Routes/planning/environment/scoring/owners restent NOT_RUN. Dans le cas vide, grid reste NOT_RUN avec la raison précisée. Une erreur grid demandée n'est ni un succès cadastral silencieux ni un NO_MATCH : sortie 1 et aucun manifeste COMPLETE. Les fichiers nouvellement créés éventuellement incomplets restent identifiés, les anciens restent inchangés.
6. Liste fermée des chemins modifiables
Code
- src/landscout/sources/ign_bdtopo_fr.py : les deux permissions cache/extraction seules, gardes et messages associés ; aucun changement de formats/algorithmes existants.
- src/landscout/workflows/cadastre_screening.py : extension optionnelle, provenance et exports ; factorisation interne minimale seulement.
- nouveau src/landscout/workflows/grid_screening.py : intégration bornée des API publiques, sérialisation/validation propres au grid.
- src/landscout/cli.py : options et transmission/validation des arguments.
Tests
- tests/unit/test_ign_bdtopo_fr.py : ajouter les tests des nouveaux flags sans affaiblir les assertions existantes.
- nouveau tests/unit/test_grid_screening.py : intégration physique et régressions des sorties.
- tests/unit/test_cadastre_cli.py : couvrir l'option en sous-processus et préserver les anciens cas.
- tests/unit/test_cadastre_screening.py : éventuel partage borné de fixture ou régressions supplémentaires, sans supprimer les anciens tests.
Continuité minimale
- docs/project/tickets/DEV.GRID.RUN.1.md : archiver la pièce effectivement reçue, qualifier son identité ; ne pas réécrire le ticket précédent.
- docs/usage/cadastre_screening.md : section option grid/schéma 2 et limites ; ne pas annoncer une exécution réelle non faite.
- docs/DEV_LOG.md : entrée courte code/tests/runs/limites.
- docs/project/CURRENT_STATE.md : reçu précédent, ticket actif, audit toujours différé.
- docs/project/BACKLOG_AND_GAPS.md : acceptation limitée A-001 référencée ; autres défauts et lacunes inchangés.
- docs/code/files/src/landscout/sources/ign_bdtopo_fr.py.md : court bandeau delta/obsolescence partielle pour les deux nouveaux flags, pas de régénération de son gros snapshot.
Aucun autre fichier : notamment ni stages électriques existants, ni configuration/politiques, ni pyproject/uv.lock, ni transport, ni autres adaptateurs, ni auditeur/registres/protected_files. Ne pas attribuer un défaut applicatif imprévu à un comportement intentionnel : le rapporter précisément et arrêter l'élargissement. Les exceptions de modification ci-dessus ne réécrivent pas les anciennes preuves ou manifestes.
7. Tests et critères de fin
Nouvelles preuves requises
1. Flags IGN. Exact bool ; compatibilité des appels historiques ; cache archive frais valide et extraction valide réutilisés sans réseau ni préparation. Absence/expiration/mauvais checksum ou taille/marker modifié/backup/cible unsafe : erreur contrôlée, aucun mkdir/cleanup/extraction/publication en mode interdit ; préserver bytes et backups. Distinguer refus archive et refus extraction. Utiliser des sentinelles sur les frontières de réseau/préparation réellement interdites.
2. Vraie intégration synthétique. Gzip cadastral existant + petite vraie archive 7z contenant un GeoPackage complet avec les quatre rôles globalement distincts : lignes électriques, postes polygonaux, route, département. Les champs doivent satisfaire les normalisateurs, pas seulement les chargeurs bruts. Préparer les caches par les API autorisées et transport synthétique ; le run final doit employer les vrais chargeurs, revalidateurs, normalisateur électrique, proximité et couverture. Aucun bypass avec les helpers privés importés sous des noms publics dans certains anciens tests ; leur fixture à archive fictive n'est pas une preuve du nouveau parcours.
3. Valeurs et limites. Distances connues (parcelle entière, pas centroid), égalités et tie_count, tension exacte/borne/inconnue, source sans géométrie électrique utilisable, objet à distance zéro, et statuts de couverture intérieur/près de bord/touche ou hors couverture. Vérifier que les IDs/rejets cadastraux ne changent pas. Aucun nouveau seuil de sélection.
4. Exports. Ancien mode inchangé, schéma 2 explicite, mêmes IDs et propriétés CSV/GeoJSON, géométrie conservée, tableau par tension dynamique/unicité/ordre, entiers/nulls/JSON strict, hashes des quatre données et bindings sources/config. Cas sans candidat : succès vide avec grid NOT_RUN, jamais COMPLETE inventé. Cas sans tension exacte distinct d'un échec source.
5. Intégrité. Mutation persistante de YAML/7z/GPKG/marker après calcul et avant COMPLETE ; erreur d'écriture sur chaque nouvelle sortie et manifeste ; conflits de chemins et liens/jonctions simulés ; aucun ancien fichier modifié et aucun COMPLETE après erreur. Une simulation de lien reste qualifiée comme simulation.
6. CLI. Sous-processus réels, --help, succès offline synthétique, absence de cache/extraction, département incompatible et combinaison d'options invalide. Vérifier codes 0/1/2, absence d'appel réseau au parcours réel testé et mode cadastral seul intact. Pas de shell inutile ; timeout borné, sortie finale après cleanup.
Une campagne ciblée, environnement existant, basetemp court neuf et unique ; pas de full-suite ni d'installation :
$run = Join-Path $env:LOCALAPPDATA ("LandScout\pytest-runs\dgr1-" + [guid]::NewGuid().ToString('N').Substring(0,8))
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
  tests/unit/test_ign_bdtopo_fr.py `
  tests/unit/test_normalize_grid_ign.py `
  tests/unit/test_enrich_grid_proximity.py `
  tests/unit/test_assess_grid_coverage.py `
  tests/unit/test_grid_screening.py `
  --basetemp $run
$code = $LASTEXITCODE
Conserver commandes, environnement, stdout/stderr hors Git et tous les échecs intermédiaires ; reruns seulement des cas affectés après correction. Ruff sur les seuls fichiers Python changés, sans --fix global ; git diff --check sur le nouveau delta. Les sorties des anciennes suites ne sont pas requalifiées en preuve physique de la nouvelle intégration. Aucun auditeur INDEX documentaire.
Sauvegarder un exemple synthétique consultable à chemin court hors Git ; rapporter réellement les comptes/valeurs et le code de sortie. Un essai Muret offline est autorisé seulement sur caches et extraction existants valides, sans renouvellement ni allongement de durée. Sinon consigner précisément les blocages de données. L'ancien échec de cache ne devient pas un bug corrigé par ce ticket, et les résultats synthétiques ne deviennent pas des résultats fonciers Muret.
8. Publication et arrêt
Terminé lorsque la nouvelle option fonctionne réellement, l'ancien mode est compatible, les frontières source-complètes sont exercées, les résultats électriques et leurs limites sont exportés, les tests ciblés passent après cleanup et l'absence éventuelle de run réel est expliquée. Pas de clôture par plan ou noms de fichiers seuls.
Stager explicitement uniquement les chemins autorisés modifiés. Pas de caches, sorties, logs ou scripts temporaires dans Git. Commit et push dev/cadastre-run-1 seulement, main et recovery inchangés. Relever le SHA publié réel, sans l'insérer comme futur self-hash. Rapport code/fichiers/tests/exemples/données réelles/limites, puis :
DEV.GRID.RUN.1 completed — optional source-bound IGN grid proximity and coverage slice; independent review pending; global documentation audit PARTIAL and deferred by user.

STOP pour revue. Aucun ticket routes, PLU, EP, score, propriétaires ou documentaire lancé en parallèle. La cible complète reste inchangée ; cette étape rend les preuves électriques existantes utilisables dans le parcours produit.