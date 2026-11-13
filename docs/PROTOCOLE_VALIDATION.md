# Protocole de validation reproductible

## Règles communes
1. Capturer les configurations de départ et conserver des snapshots.
2. Ne pas publier les secrets, fichiers de comptes réels ou journaux contenant des identifiants personnels.
3. Conserver une console active et une deuxième session SSH durant chaque modification.
4. Confirmer la table de routage dans les deux sens avant les services RADIUS/NTP/syslog.
5. Pour chaque point: relever la commande exacte, la date locale WAT, la source du test, la sortie et le verdict.

## Différence résultats attendus / résultats mesurés
La rubrique « Résultat attendu » est une spécification technique. Elle ne constitue ni une capture ni une validation. Une preuve réelle doit venir du routeur/serveur exécutant la commande; les exemples de syntaxe ne sont pas des transcriptions de laboratoire.

## Enchaînement
- R-DLA : 8 contrôles du tableau TP3.1, préserver le DHCP VLAN 10, accès secours avant désactivation admin.
- R-SIEGE : 8 contrôles du tableau TP3.2, inclure le repli local avec FreeRADIUS temporairement arrêté et remis en service.
- R-FAI : 6 contrôles du tableau TP3.3, source Internet interdite et test de l’utilisateur vyos après suppression.
- TP3.4 : authentifier prestataire.temp sur les trois routeurs, supprimer du fichier FreeRADIUS, redémarrer le démon, constater trois nouveaux refus. La chronologie doit provenir uniquement de /var/log/reseau/.

## Calcul NSA
Taux (%) = 100 × nombre de critères conformes / nombre de critères applicables. Exclure les critères NA; aucune valeur ne peut être calculée sans les relevés de contrôle.

## Rapport professeur
Un seul document Word ou PDF, cinq pages maximum avec captures. Une capture par vérification demandée, recadrée et légendée. Le dossier technique GitHub est un complément et non une dérogation à la limite de pages.
