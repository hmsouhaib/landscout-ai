LANDSCOUT — DOCS.CONTINUITY.1.R16
Réconcilier la documentation du composant RTE/ODRÉ, de ses tests et de ses deux compagnons
Un seul lot documentaire. Aucun changement applicatif, nouvelle fonctionnalité ou correctif A-002.
Ancrage	Valeur
Dépôt	hmsouhaib/landscout-ai
Racine locale attendue	C:\souhaib\landscout-ai
Branche autorisée	recovery/docs-continuity-1-partial
HEAD de départ requis	7f00e8c29e9bb85222abb708e0fc6a45ad2ba178
Parent de comparaison R15.1	29732dd3f4f1b4f0f2351d18e1f9d2d96a503091
Main à préserver	aa4ebc7063f2abdfcbae95154ba89b5b1a0dba02


1. Reçu fourni de la revue précédente
ChatGPT, reviewer en lecture seule : APPROVED — correction documentaire R15.1, au HEAD de départ ci-dessus. R15-REV01 et R15-REV02 sont levées. Le périmètre documentaire R15 précédemment examiné est accepté avec ce correctif et ses limites conservées.
La publication est un descendant direct de R15. Le diff examiné contient les six chemins autorisés : huit cellules d'effets corrigées dans le compagnon des tests IGN ; le fingerprint du compagnon et une provenance successorale dans l'unité propriétaire ; reçu, ticket et deux documents d'état. Les quatre écritures pyogrio.write_dataframe(..., append=True) et les quatre descriptions de mutations locales correspondent aux corps de tests. Les blocs de code et les autres lignes du compagnon restent inchangés dans ce delta. Les notes de purpose déjà exactes sont conservées : aucune modification de leurs 105 symboles n'apparaît dans le patch propriétaire. Les anciennes preuves R15 et les retouches R14 ne sont pas réécrites. Aucun nouveau crédit historique.
Les références serveur consultées concordent avec recovery 7f00e8c… et main aa4ebc7…. Cela n'atteste ni le checkout Windows, ni ses fichiers ignorés, ni son index local. Le reviewer n'a exécuté ni pytest, ni import applicatif, ni auditeur INDEX, ni rendu ou cold-start. Il n'a pas recalculé indépendamment tous les fingerprints/snapshots du registre global ou le manifeste des 106 fichiers protégés.
L'unique INDEX R15.1 reste REPORTED_EXECUTION : exit natif 1, completed=true, 10 209 constats. Le reçu distingue correctement le candidat audité et sa complétion documentaire ultérieure. Les logs/manifeste/delta conservés sur le PC ne sont pas devenus des pièces exécutées ou recalculées par le reviewer. Les 125 passes IGN et 174 passes R14 restent historiques. La revue a confronté le contenu des consignes archivées ; l'identité octet pour octet de l'archive textuelle linéarisée avec le fichier Markdown initial n'est pas attestée.
Cette approbation limitée autorise la poursuite documentaire, pas une clôture globale ou fonctionnelle. Ne pas transformer un ancien PENDING historique en nouvelle preuve : porter le renvoi successoral vers ce reçu dans l'état courant. Global PARTIAL, A-001..A-004, OPEN R5-D01, les limites de preuve antérieures, le rendu/cold-start, la revue sémantique 7F.1C.1 et la lacune du reçu original 7F.1B.4 restent inchangés.
2. Objectif et unités du lot
Rendre les deux références RTE/ODRÉ fidèles aux sources et aux tests effectivement publiés, jusqu'aux notices individuelles, champs, relations et limites des preuves. LandScout demeure un moteur BESS-first : un export de réseau, ses métadonnées ou sa précision déclarée ne démontrent ni capacité disponible, ni raccordement possible, ni aptitude d'une parcelle.
Le propriétaire retrouvé est docs/code/audit/reviews/foundations.json. Les lignes source et test sont encore READ, pas CHECKED. Le compagnon source est enregistré comme lu ; le compagnon des tests reste l'unité documentaire NOT_READ identifiée dans l'état courant. Les compagnons sont représentés par les champs documentaires imbriqués des deux lignes, pas par deux lignes supplémentaires.
Les quatre unités visées sont exclusivement :
1. src/landscout/sources/rte_odre_fr.py — lecture et réconciliation, sans écriture Python ;
2. tests/unit/test_rte_odre_fr.py — lecture et réconciliation, sans modification des tests ;
3. docs/code/files/src/landscout/sources/rte_odre_fr.py.md ;
4. docs/code/files/tests/unit/test_rte_odre_fr.py.md.
Avant édition, confirmer les quatre états exacts, leurs symboles originaux et l'absence d'autre propriétaire effectif à partir de la matrice originale et des fragments actuels. Une intention de transfert ne constitue pas une seconde propriété. Conserver la preuve initiale et signaler une contradiction réelle sans promotion automatique. Ne pas réinventorier tout le dépôt comme phase de préparation.
Les lectures du reviewer ont avancé jusqu'à la fin du source et des tests RTE, ainsi que de la configuration. Les deux compagnons RTE ne sont pas encore entièrement réconciliés par le reviewer ; ce ticket n'est pas leur approbation anticipée.
3. Lectures nécessaires, sans réaudit des voisins
Lire intégralement les quatre unités. Réutiliser les corps déjà lus seulement après vérification de leur identité au départ. Lire chaque explication, tableau, champ et contrat ; comparer mécaniquement le code répété aux sources, sans confondre cette comparaison avec une revue de prose.
Contexte en lecture seule : configs/sources/rte_odre_fr.yaml, son compagnon, src/landscout/sources/__init__.py, les définitions pertinentes de common/safe_http.py, common/strict_json.py, common/strict_yaml.py, et les véritables consommateurs découverts par imports/appels qualifiés. Réutiliser les lectures identiques déjà acquises. Leurs états documentaires ne sont pas clôturés par ce lot. Suivre une dépendance jusqu'au propriétaire de la garantie nécessaire ; ne pas rouvrir IGN, les normalisateurs ou les pipelines voisins en entier.
Réutiliser les règles du dépôt applicables et les reçus R15/R15.1. Vérifier racine, branche, HEAD, suivi, index/worktree, absence d'opération Git en cours et références serveur. Toute divergence doit être expliquée ; aucun reset, changement de branche ou écrasement pour retrouver artificiellement les ancrages. Une reprise interrompue de ce même ticket conserve ses modifications identifiables.
4. Contrats précis à confronter et à documenter
Ces points proviennent des corps RTE relus ; ils ne remplacent pas la lecture de toutes les autres notices.
Configuration, URL et transport
- Modèles Pydantic gelés et extra-forbid, modèles imbriqués, valeurs requises, alias et prévalidateurs. Distinguer leurs garanties des annotations des dataclasses et des deux __post_init__ qui contrôlent certains comptes.
- Origine configurée : HTTPS, hôte odre.opendatasoft.com, port absent ou 443, chemin /api/explore/v2.1 après retrait des barres finales ; pas d'identifiants, query ou fragment. Ne pas réduire le contrat à une égalité naïve de chaînes ni l'étendre à tout hôte officiel supposé.
- sites, overhead_lines, underground_lines et identifiants configurés ; construction/échappement des URL sans requête dans les builders. _validated_source_config reconstruit le modèle aux frontières concernées.
- load_rte_odre_source_config ne traduit pas toutes ses erreurs en RteOdreDownloadError : suivre ses appels effectifs de lecture YAML et de validation. Distinguer cette interface de la reconstruction contrôlée.
- Le transport est délégué à open_safe_https. Une origine configurée valide n'est pas, seule, une preuve de résolution DNS, de connexion ou de redirection sûre. Les tests remplaçant l'opener ne testent pas réellement TLS/DNS.
Métadonnées et géométrie GeoJSON
- Distinguer les métadonnées distantes, l'export physique et leur comparaison de records_count lorsqu'il est disponible. Les valeurs optionnelles absentes restent inconnues ; préciser normalisation des chaînes et contrôles des comptes.
- GENERALIZED_OR_RESTRICTED repose sur les deux expressions recherchées dans la description ; ce n'est pas une mesure géométrique. Le téléchargement attribue MISSING pour un export non vide entièrement nul ; ne pas l'attribuer automatiquement à une collection vide.
- _validate_geojson impose JSON strict puis FeatureCollection/features/Feature et résume les géométries. Une clé geometry absente est traitée comme nulle par get. Les types retournés pour les GeometryCollection ne constituent pas un inventaire indépendant de tous leurs membres.
- _validate_position et _validate_nested_coordinates contrôlent structure et positions numériques finies. Ils ne prouvent pas la validité topologique, la fermeture/cardinalité des anneaux, l'exactitude du CRS, une géométrie exclusivement 2D ou l'exactitude du réseau réel. Ne pas inventer de réparation ou de reprojection.
- A-002 reste ouvert : une valeur GeoJSON type liste/dictionnaire non hachable peut lever un TypeError brut au test d'appartenance. Décrire le comportement et ses traductions/captures selon l'appelant ; ne pas modifier le Python, les assertions, le backlog ou la sévérité pour effacer le défaut.
Cache, écritures et récupération
- Décrire les clés exactes du sidecar, les parseurs/reconstructions et les valeurs omises (path, cache_hit). Ne pas importer les schémas 1/3 IGN : ce sidecar RTE n'est pas ce modèle.
- Le cache relit l'export, le valide, calcule taille/SHA et confronte le résumé/identité/comptes. Son horodatage doit être timezone-aware ; il est converti en UTC pour l'âge, sans exiger que l'offset enregistré soit initialement nul. Ne pas copier le contrôle IGN.
- Un cache valide évite les requêtes ; sur miss, les métadonnées sont demandées avant l'export. Nommer les effets directs et ceux délégués : lecture, écriture exclusive des .part, SHA, mutation locale, asdict, replace, publication et cleanup.
- Suivre les gardes .bak, liens/jonctions et préparation des temporaires. Lire les opérations effectives de _publish_cache_pair : publications séquentielles, restauration conditionnelle de l'archive, absence d'appel de restauration du backup des métadonnées. Ne pas inventer les branches du publisher IGN.
- Distinguer cleanup interne des backups et cleanup externe des temporaires. La préservation d'une erreur principale n'est pas une garantie universelle de cleanup, d'atomicité à deux fichiers ou de protection contre toutes les courses.
- Des relectures par chemin et un SHA cohérent ne constituent pas automatiquement un parseur lié à un snapshot immuable. L'enveloppe retournée n'est pas une acquisition supplémentaire de ses consommateurs.
Tests et références qualifiées
Pour chaque test/helper/fixture/callback : expliquer fixture concrète, paramètres, modification exacte, fonction appelée, premiers rejets possibles, assertions et limites. Ne pas simplement reformuler son nom.
Points déjà repérés dans les corps :
- test_fresh_cache_is_reused observe deux appels d'opener sur deux téléchargements : métadonnées + export du premier, pas deux acquisitions réseau complètes.
- Les NaN/Infinity injectés par certains tests de coordonnées peuvent être rejetés par le parseur JSON strict avant la garde numérique ou la structure annoncée.
- test_invalid_cached_record_count_invalidates_cache compare deux lectures du même chemin après refresh ; ce n'est pas une comparaison avec un snapshot sauvegardé avant modification.
- Les liens/jonctions sont simulés par des prédicats et, selon le scénario, un Path.open délégué. Ne pas annoncer la création/test de vrais liens Windows.
- Les callbacks de publication délèguent certaines opérations et en font échouer d'autres ; les flux BytesIO et sentinelles de transport sont des mocks, pas des acquisitions officielles.
- Les dataclasses, la fixture source_config, les paramètres qui reçoivent ses valeurs, les méthodes Pydantic héritées et les réexports doivent conserver leurs vrais propriétaires.
Aucune fonction, valeur d'assertion, branche d'exception ou garantie absente ne doit être ajoutée à la prose pour obtenir une couverture fictive.
5. Sept chemins d'écriture autorisés
1. docs/code/files/src/landscout/sources/rte_odre_fr.py.md — réconciliation intégrale, notices concrètes et limites ;
2. docs/code/files/tests/unit/test_rte_odre_fr.py.md — réconciliation intégrale des preuves de tests ;
3. docs/code/audit/reviews/foundations.json — uniquement les deux lignes RTE concernées, leurs symboles, états documentaires imbriqués, fingerprints et provenance bornée ;
4. docs/code/audit/R16_RTE_ODRE_SOURCE.md — nouveau reçu du lot ;
5. docs/project/tickets/DOCS.CONTINUITY.1.R16.md — archive du présent fichier effectivement transmis, section 1 incluse ;
6. docs/project/CURRENT_STATE.md — renvoi successoral compact et état R16 ;
7. docs/code/audit/DOCUMENTATION_AUDIT.md — ajout compact, progression réellement calculée et limites.
Conserver les textes corrects. Les snapshots et signatures documentaires doivent représenter les Python inchangés. Pas de régénération globale, déplacement de propriété, nouvelle infrastructure de suivi ou multiplication des reçus.
Le présent fichier doit être transmis comme fichier Markdown et archivé sans le reconstruire depuis un résumé ou un rendu copié. Conserver sa preuve externe d'identité ; ne pas lui ajouter son propre futur hash. Pour R15.1, conserver l'archive existante : le présent reçu explicite la limite de comparaison, sans inventer les octets effectivement reçus par Codex.
Tout le reste est exclu : source, tests, configurations et leurs compagnons, dépendances, auditeur, autres fragments, coverage.json, matrice originale, backlog, reçus/tickets antérieurs, cache et données. Aucun fix A-002, aucun STEP 7F, score, contact/propriétaire, export produit, CI, PR ou fusion main.
6. États et progression sans double crédit
Capturer les valeurs initiales des deux lignes et leurs symboles. Conserver la provenance antérieure dans une forme bornée comparable au parent, sans dupliquer tout le registre. Mettre CHECKED/CORRECTED seulement après réconciliation effectivement achevée ; READ n'est pas une approbation.
Recompter les unités originales réellement clôturées avec le propriétaire effectif et leurs états imbriqués. Le périmètre permet au maximum quatre unités originales, pas quatre fichiers plus leurs deux lignes parentes. Calculer les symboles selon la matrice historique, sans confondre tests paramétrés, callbacks et nouveaux symboles.
Les totaux de départ 111/245 fichiers, 3 330/4 769 symboles, reste 134/1 439 sont historiques consignés, pas un nouveau calcul du reviewer. Réconcilier le delta RTE réellement établi ; ne pas choisir un total cible. Aucun crédit pour R15.1, ce ticket, son reçu ou les dépendances contextuelles. Ne pas réconcilier maintenant le registre global coverage.json.
7. Validations et preuves
Contrôles statiques
Sans import applicatif ni changement d'environnement, vérifier les identités Git/index/checkout des sources ; tout le contenu explicatif ; snapshots, signatures, champs, ancres, liens affectés, JSON strict, Unicode et tableaux. Identifier précisément les limites des éventuelles résolutions automatiques de relations.
Comparer les deux lignes propriétaires au parent : conserver tous les champs, notes, états et preuves non concernés. Vérifier les 106 fichiers protégés contre leur manifeste et le départ, puis tous les chemins initialement suivis hors des sept autorisés, avec nombre réellement recalculé. Préserver les deux exceptions EOL et les treize observations whitespace héritées. git diff --check sur le nouveau delta ; aucune normalisation globale.
Pas de nouveau pytest pour ce lot de prose. Ne pas relancer IGN, R14, l'ensemble des suites, ni acquérir de données. Une lecture de test n'est pas une exécution. Toute preuve historique RTE réutilisée doit être retrouvée et liée à ses véritables octets/commande/résultats ; sinon noter son indisponibilité. Ne pas fabriquer un nombre de passes. Une reproduction applicative supplémentaire nécessite une autorisation distincte.
Un seul INDEX candidat, auditeur inchangé
Stager explicitement les sept chemins effectivement modifiés après relecture. Conserver le manifeste trié path/mode/OID du candidat, les logs et le contenu pré-complétion du reçu hors Git. Utiliser des noms de preuve ne remplaçant aucun log existant.
.venv\Scripts\python.exe -B -X utf8 tools/audit_documentation.py --check --progress > C:\souhaib\r16-candidate.stdout.txt 2> C:\souhaib\r16-candidate.stderr.txt
$code = $LASTEXITCODE
Consigner code natif final, completed, compte réel et diagnostics concernés. Exit 1 avec completed=true reste un résultat global partiel, pas un succès vert. Une interruption ou panne de l'outil ne doit pas être présentée comme un run achevé. Aucun changement des exclusions ou de l'auditeur pour améliorer le résultat.
Comparer seulement aux logs/manifeste effectivement disponibles du candidat R15.1 ; distinguer multiplicité, lignes ajoutées/retirées et effet des nouvelles unités. 10 209 n'est pas une cible ni le compte du commit final R15.1. Les constats partagés ne sont pas tous inoffensifs. Ne pas confondre le registre global non réconcilié avec le fragment propriétaire actif.
Après le run, remplir seulement l'emplacement réservé aux résultats dans le reçu R16. Conserver hors reçu son delta final et la preuve que les autres path/mode/OID du candidat sont inchangés. Pas de deuxième auditeur, de futur auto-SHA, de compte final inventé ou d'égalité candidat/commit final. Un contrôle syntaxique Markdown ne vaut pas rendu visuel.
8. Fin, publication et arrêt
Fournir : les quatre états initiaux/finals et leur propriétaire ; identités source/test ; corrections établies avec exemples ; notices et symboles réellement réconciliés ; limites de tests préservées ; traitement documentaire de A-002 sans fix ; contrôles statiques ; INDEX candidat et complément du reçu ; préservation et progression dédupliquée.
Pas de reset/restore/clean/stash/rebase/amend/squash/merge/force-push, suppression de sauvegardes, ACL ou sécurité modifiée. safe.directory uniquement par commande et pour le chemin exact après diagnostic effectif, jamais en wildcard/persistant.
Après réussite des contrôles bornés et qualification explicite de l'audit global PARTIAL, publication autorisée uniquement sur recovery :
# git add : chacun des sept chemins effectivement modifiés et relus, explicitement.
# Aucun git add . / -A, commit -a ou fichier hors périmètre.
git commit -m "docs: reconcile RTE ODRE source and test references"
git push origin recovery/docs-continuity-1-partial
Vérifier le vrai SHA, le suivi et la référence serveur, index/worktree propres, main local/suivi/serveur inchangé. Si un contrôle échoue, conserver le travail et rapporter son résultat, sans contournement destructif.
Statut : DOCS.CONTINUITY.1.R16 completed — documentary scope only; global audit PARTIAL; independent review pending. Puis STOP. Aucun R17 automatique et aucune continuation fonctionnelle. Souhaib transmet la publication au reviewer.