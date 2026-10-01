LANDSCOUT — DOCS.CONTINUITY.1.R15.1
Corriger les tableaux d’effets résiduels du compagnon des tests IGN
Ticket unique de correction documentaire. Aucun nouveau lot fonctionnel ni R16.
Ancrage	Valeur
Dépôt local	C:\souhaib\landscout-ai
Dépôt distant	hmsouhaib/landscout-ai
Branche autorisée	recovery/docs-continuity-1-partial
HEAD de départ requis — R15	29732dd3f4f1b4f0f2351d18e1f9d2d96a503091
Parent R14, comparaison historique seulement	8bef62ab9b6eef185bab526a046b4a7dbbea42a1
Main à préserver	aa4ebc7063f2abdfcbae95154ba89b5b1a0dba02


1. Reçu fourni de revue indépendante
Reviewer : ChatGPT, lecture seule. Verdict : CORRECTION_REQUIRED — périmètre documentaire R15 au SHA ci-dessus.
Les lectures intégrales du source IGN, de ses tests, du transport/parsers, des exports, des deux normalisateurs et de la configuration, effectuées dans le même chat au même SHA, sont réutilisées. La revue a poursuivi les explications des deux compagnons après leur ligne 140 : notices, champs, signatures, relations, algorithmes, erreurs, tableaux d’effets et descriptions de tests. Les répétitions de code ne sont pas présentées comme une seconde lecture sémantique indépendante. Les constats bloquants R15-REV01 et R15-REV02 ci-dessous concernent des descriptions d’effets fausses ou incomplètes, non des défaillances applicatives nouvellement démontrées.
Les distinctions acquisition/cache/extraction/chargement config-bound, les sauvegardes et le rollback asymétrique du cache, les limites des contrôles par chemins, la conservation des géométries brutes, la sélection départementale et les limites des fixtures synthétiques restent acquises dans le périmètre examiné. Ne pas recommencer R15 ni réécrire ses introductions correctes.
Les deux retouches R14 sont acceptées dans leur portée vérifiée : le test EPSG:2154 ne contient aucune assertion de distance ; le test de conservation géométrique appelle equals_exact scalaire et compare has_z. Les notes correspondantes de foundations.json ont été retrouvées corrigées et confrontées aux notes du parent R14. Ne pas les modifier de nouveau. Cette acceptation n’atteste pas chaque autre champ du registre ou le recalcul de son fingerprint.
Le reviewer a consulté les unités IGN et des notes ciblées du propriétaire foundations, ainsi que les deux notes R14 avant/après. Cela n’est pas un recomptage mécanique exhaustif de toutes les transitions, une comparaison byte-for-byte de tous les champs du fragment ou une certification de chacune de ses 355 notes. Aucun audit indépendant exhaustif de tous les snapshots, signatures, ancres, liens ou fichiers protégés n’est revendiqué. Le point d’accès commit ne livre pas un patch exploitable complet pour tous les grands fichiers ; ne pas convertir l’inspection du contenu courant en preuve d’un diff intégralement recalculé.
Les références serveur consultées restent aux ancrages indiqués. Leur lecture n’atteste pas l’index, le checkout Windows ou ses fichiers ignorés. Aucun pytest, import applicatif, auditeur INDEX, rendu visuel, cold-start ou téléchargement officiel n’a été exécuté par ce reviewer. Les 125 passes / 9,02 s / exit 0 après cleanup et les 10 209 constats / completed=true / exit 1 du candidat INDEX R15 restent des exécutions rapportées. Le candidat et le commit après complétion du reçu ne sont pas confondus.
Le verdict demande une correction, pas une approbation globale différée faute de lire des composants indépendants. Les réserves antérieures restent ouvertes dans leur portée. Cette déclaration n’est ni une exécution Codex, ni une signature cryptographique, ni une approbation fonctionnelle.
2. Objectif et préparation bornée
Corriger les descriptions directes d’écriture et de mutation dans huit notices identifiées du seul compagnon des tests IGN ; synchroniser uniquement les éléments documentaires réellement concernés. Le code et les assertions sont la référence observée : ne pas les modifier pour rendre la documentation vraie.
LandScout reste un moteur BESS-first de prospection et préanalyse. Ce ticket rétablit la fidélité de sa documentation, sans créer de capacité réseau électrique, d’accès légal/poids lourd, de décision environnementale ou de fonctionnalité produit.
Vérifier la racine réelle, la branche, HEAD, le suivi, l’index/worktree, les opérations Git en cours et les références serveur. Exiger les ancrages ci-dessus pour une première exécution. En cas de reprise interrompue de ce ticket, conserver ses changements identifiables et reprendre le premier contrôle manquant. Une divergence ne permet aucune réinitialisation, substitution de branche ou écrasement.
Réutiliser les règles déjà acquises et consulter les instructions du dépôt effectivement applicables. Pas de nouvel inventaire ou réaudit général pour cette correction. Lire les huit corps et leurs notices, les lignes propriétaires réelles, le reçu R15 et cette instruction. Les autres sources ne sont relues que pour résoudre une dépendance nécessaire.
3. R15-REV01 — écritures physiques explicitement appelées mais niées
Bloquant pour la clôture documentaire R15.
Fichier : docs/code/files/tests/unit/test_ign_bdtopo_fr.py.md.
Dans les quatre notices ci-dessous, le tableau Source-observed side-effect matrix, ligne Filesystem/archive write or publication, annonce None directly present. alors que le corps appelle directement pyogrio.write_dataframe(..., append=True).
Symbole sous tests.unit.test_ign_bdtopo_fr	Écriture directe à documenter
test_ambiguous_electric_line_layers_fail	Ajout de LIGNE_ELECTRIQUE_SECONDAIRE dans le GeoPackage synthétique.
test_ambiguous_road_layer_fails_safely	Ajout de TRONCON_DE_ROUTE_SECONDAIRE dans le GeoPackage synthétique.
test_road_loader_rejects_changed_layer_inventory	Ajout de ADDED_AFTER_EXTRACTION au GeoPackage déjà extrait.
test_department_coverage_layer_discovery_must_be_unambiguous	Ajout de DEPARTEMENT_SECONDAIRE dans le GeoPackage synthétique.


Exemple relu : source tests/unit/test_ign_bdtopo_fr.py, 1428–1455, test_road_loader_rejects_changed_layer_inventory. Sa notice et son tableau se trouvent dans la plage 6550–6750 du compagnon R15. Le corps contient :
pyogrio.write_dataframe(
    added,
    extraction.geopackage_path,
    layer="ADDED_AFTER_EXTRACTION",
    driver="GPKG",
    append=True,
)
Remplacer seulement les quatre cellules fautives par l’appel effectif et sa portée physique synthétique. Il s’agit d’un appel présent dans le corps, pas simplement d’une écriture cachée dans une fixture. Ne pas élargir la description à un téléchargement officiel. Conserver les descriptions exactes des premiers rejets : une modification de GeoPackage avec preuve de taille/SHA périmée ne démontre pas isolément la comparaison sémantique de l’inventaire des couches.
Ne pas remplacer le libellé de toute la matrice pour rendre artificiellement acceptable l’absence d’un appel connu. Ne pas régénérer globalement le compagnon ou modifier un outil d’analyse.
4. R15-REV02 — mutations en mémoire manquantes
Bloquant pour la clôture documentaire R15. Même compagnon, cellules In-memory mutation des quatre notices suivantes.
Symbole sous tests.unit.test_ign_bdtopo_fr	Correction exacte
test_download_revalidates_a_tampered_config_before_network	Remplacer l’absence annoncée de mutation par object.__setattr__(tampered, "provider", "UNTRUSTED"), appliqué à une copie locale du modèle.
test_non_electric_layer_loaders_revalidate_mutated_role_config_before_read	Documenter les deux branches object.__setattr__ : tokens routiers remplacés par () ou champ d’identité départementale remplacé par " ", sur la copie locale et son modèle imbriqué.
test_missing_required_source_field_fails	Documenter del content[field], suppression dans le dictionnaire local retourné par _config_data().
test_invalid_department_coverage_config_fails	Compléter l’inventaire des mutations par la branche del content["coverage"], en conservant les deux affectations imbriquées déjà décrites.


La seconde notice apparaît également dans la plage 6550–6750 du compagnon ; le corps est relu dans la plage 1380–1426 du test publié.
Distinguer ces mutations locales d’une mutation du paramètre original : model_copy(deep=True) et le dictionnaire local ne justifient pas d’affirmer que la fixture ou le YAML sur disque a été modifié. Ne pas changer une cellule correcte Direct parameter mutation en prétendant le contraire. Conserver les sentinelles gpd.read_file/transport et leurs véritables assertions ; aucune nouvelle assertion ne doit être inventée.
5. Propriétaire, historique et fichiers autorisés
Six chemins d’écriture au maximum :
1. docs/code/files/tests/unit/test_ign_bdtopo_fr.py.md — exclusivement les huit cellules identifiées et, seulement si indispensable, leur phrase explicative immédiatement associée.
2. docs/code/audit/reviews/foundations.json — unité propriétaire du test IGN : fingerprint du compagnon, provenance compacte R15.1, notes ciblées uniquement si elles reproduisent les erreurs ou nécessitent une précision liée aux huit corrections. Ne pas présumer que les notes de purpose déjà correctes sont erronées.
3. docs/code/audit/R15_1_DOCUMENTATION_FIDELITY.md — nouveau reçu local borné.
4. docs/project/tickets/DOCS.CONTINUITY.1.R15.1.md — archive exacte de ce Markdown réellement reçu, incluant la section 1 ; pas une reformulation ou une reconstruction depuis un résumé.
5. docs/project/CURRENT_STATE.md — court renvoi successoral au verdict fourni et au correctif local en attente de revue.
6. docs/code/audit/DOCUMENTATION_AUDIT.md — ajout compact du correctif, de ses résultats et de son statut ; pas de réécriture de toute la chronologie.
Comparer les notes ciblées avec leur état R15 et, pour la provenance utile, avec le parent R14. Conserver les anciennes valeurs utiles dans la provenance sans réinsérer les erreurs dans l’explication courante. Les unités source/test et leurs états documentaires imbriqués restent représentés comme dans le propriétaire réel ; ne pas inventer des lignes supplémentaires.
Les états de lecture locale déjà enregistrés ne valent pas approbation. Conserver les acquis ; enregistrer la demande de correction puis sa réalisation locale séparément. Aucun nouveau crédit : gain 0 fichier / 0 symbole. Les totaux historiques rapportés 111/245 et 3 330/4 769, ainsi que le reste 134/1 439, ne sont pas un nouveau comptage du reviewer.
Hors périmètre, à conserver inchangé : Python, tests, configurations, dépendances/lock, auditeur, autres compagnons — y compris compagnon source IGN et compagnon R14 —, anciennes archives/reçus/tickets, coverage.json, matrice globale, autres fragments, backlog, caches, archives et GeoPackages officiels. Aucun correctif applicatif, nouveau test, outil permanent, CI/PR ou fusion vers main. Le libellé historique « atomic cache publication » du docstring Python n’est pas à réécrire ici.
Préserver A-001 à A-004, R5-D01, R15-T01..05 et toutes les réserves précédentes, les lacunes historiques, le rendu/cold-start et les validations globales pendantes. La recherche EP 7F.1C.1 reste un draft non exécutable ; dernière frontière fonctionnelle approuvée consignée : 7F.1B.4.
6. Vérifications locales requises
A. Contrôles statiques bornés
Environnement installé inchangé. Scripts temporaires hors dépôt autorisés, sans import applicatif, pour comparer texte/AST/JSON/octets et liens. Vérifier :
- les huit bonnes notices, leur propriétaire qualifié et leur corps publié ; les écritures et mutations réellement présentes ;
- les huit substitutions, sans changement d’assertion, de signature, de plage source, d’ancre ou de code répété ;
- les blocs de code du compagnon identiques à R15 ; ne pas corriger un snapshot en altérant le test ;
- les notes propriétaires ciblées, le fingerprint final du compagnon et la provenance ; tout autre champ/état inchangé hors ajout explicitement autorisé ;
- JSON strict, Unicode, tableaux/fences, liens locaux affectés et exactitude de l’archive du ticket ;
- les 106 fichiers protégés contre le manifeste et le départ ; tous les chemins initialement suivis hors des six autorisés, avec nombre réellement recalculé ;
- préservation des deux exceptions EOL et des treize observations whitespace historiques ; git diff --check du nouveau delta sans normalisation globale.
Nommer les bases Git/index/checkout lorsqu’elles diffèrent. Les OID source/test à préserver incluent :
src/landscout/sources/ign_bdtopo_fr.py
876207e3b1b0ac4c1a245c01fdad91e72e5bb4d3

tests/unit/test_ign_bdtopo_fr.py
560c3ec1774ec514e77f58e1f9a63ec6599de2db
Pas de pytest, suite complète, acquisition, uv sync/install ou changement de sécurité. Ce correctif ne change que la prose et ses preuves. Ne pas relancer les 125 tests IGN, les 174 tests R14 ou les pipelines. Leurs résultats historiques ne deviennent pas des exécutions R15.1.
B. Une seule exécution de l’auditeur INDEX inchangé
Préparer les six chemins effectivement modifiés, les relire et les stager explicitement. Capturer le manifeste exact path/mode/OID du candidat et les logs. Exécuter une seule fois :
.venv\Scripts\python.exe -B -X utf8 tools/audit_documentation.py --check --progress > C:\souhaib\r15-1-candidate.stdout.txt 2> C:\souhaib\r15-1-candidate.stderr.txt
$code = $LASTEXITCODE
Consigner le code natif, completed, le nombre réel de constats et les limites. exit 1 avec completed=true peut refléter l’audit global PARTIAL ; ce n’est pas un résultat vert. Une interruption, une sortie 2 ou une erreur de fonctionnement n’est pas une exécution terminée. Ne pas toucher l’outil, les exclusions ou le registre global pour obtenir du vert.
Comparer au vrai candidat R15 seulement si ses logs/manifeste sont disponibles et identifiés ; sinon consigner l’indisponibilité. 10 209 n’est ni une cible ni le compte du commit R15 final. Les constats partagés ne sont pas tous bénins. Classer le delta réellement observé et tout diagnostic affectant ces corrections.
Après ce run, compléter uniquement l’emplacement réservé à ses résultats dans le nouveau reçu. Vérifier le delta exact du reçu, l’identité de tous les autres path/mode/OID et conserver la preuve externe. Pas de seconde exécution fictive, de SHA futur intégré au reçu, d’égalité candidat/commit final inventée ni de nouveau total prétendument audité pour le commit final.
Le rendu visuel reste non exécuté s’il ne l’est pas réellement. Une vérification syntaxique Markdown ne le remplace pas.
7. Critères de fin et publication
Le lot est localement terminé lorsque les huit descriptions correspondent aux opérations directes, les notes/fingerprints ciblés sont cohérents, les invariants de préservation passent et l’unique audit candidat est terminé et correctement qualifié. Tout défaut supplémentaire hors périmètre est signalé, pas corrigé silencieusement. Ne pas élargir ce ticket en réaudit des voisins.
Pas de reset/restore/clean/stash/rebase/amend/squash/merge/force-push, suppression de sauvegardes ou changement de sécurité. L’exception ponctuelle safe.directory ne peut être réutilisée que pour le chemin exact, par commande, après une erreur effective ; aucune confiance persistante ou wildcard.
Publication autorisée sur recovery seulement, après réussite des contrôles bornés et qualification des réserves globales :
# git add : uniquement les chemins effectivement modifiés de la section 5,
# relus et explicitement nommés ; jamais git add . / -A ou commit -a.
git commit -m "docs: correct IGN test reference side effects"
git push origin recovery/docs-continuity-1-partial
Vérifier le vrai SHA publié, la propreté de l’index/worktree, le suivi et la référence serveur concordants ; main local/suivi/serveur reste à l’ancrage requis. En cas d’échec, préserver le travail et produire le résultat effectif sans réessai destructif.
Rapport attendu : chemins modifiés ; huit corrections avant/après ; notes déjà exactes ou ajustées ; contrôles et limites ; exécution INDEX et différence candidat/reçu final ; preuves de préservation ; SHA et état de publication ; zéro gain de couverture.
Statut final local : DOCS.CONTINUITY.1.R15.1 completed — documentary correction only; global audit PARTIAL; independent review pending.
Puis STOP pour revue. Codex ne s’accorde pas l’approbation R15/R15.1 et n’enchaîne pas R16. Souhaib transmettra le résultat au reviewer.