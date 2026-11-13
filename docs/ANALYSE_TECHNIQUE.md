# Analyse technique et justification des choix

## Pourquoi une administration distincte ?
SRV-ADMIN (10.10.99.20/24) concentre les accès de supervision et réduit les surfaces d’exposition. Les équipements n’acceptent l’administration que depuis les sources explicitement admises; une restriction par adresse ne remplace pas l’authentification nominative. Les chemins retour vers 10.10.99.0/24 conditionnent RADIUS, NTP et syslog.

## Pourquoi RADIUS ?
FreeRADIUS déporte l’authentification; la révocation de prestataire.temp doit être prouvée séparément sur chacun des trois routeurs. Attention aux comptes locaux du même nom, caches et sessions déjà ouvertes : la révocation bloque les **nouvelles authentifications**, elle ne termine pas automatiquement toute session existante. Pour la preuve, ouvrir une nouvelle session après suppression puis vérifier Access-Reject ou l’absence d’Access-Accept.

## Pourquoi journaliser ?
Un message reçu dans /var/log/reseau/ fournit une preuve de transmission des journaux et de son horodatage, mais ne garantit pas que chaque commande exécutée est nominativement traçable. Sur Cisco, configuration-change logging donne davantage de détails si les fonctionnalités IOS le permettent. La chronologie doit recouper date, IP, compte et équipement, en distinguant connexion, changement et échec.

## Limites techniques spécifiques
* Cisco IOSv du support : la négociation SSH peut imposer des algorithmes hérités; les désigner comme écart de laboratoire et ne jamais recommander leur emploi sur Internet.
* NTP : l’état « synchronisé » ne prouve pas une authentification cryptographique. La configuration MD5 requiert la compatibilité du serveur et de chaque client; Chrony 4.x demande une vérification précise de sa prise en charge du mode symétrique legacy et des clés.
* uRPF : strict convient au trajet symétrique, loose est plus tolérant sur bordure multi-opérateur asymétrique et doit être complété par ACL de filtrage anti-usurpation.
* Services : comparer les scans de départ/fin depuis plusieurs zones et inclure des tests négatifs. Le statut « open|filtered » de nmap UDP n’est pas une preuve de service actif.
* DHCP MikroTik : le trafic d’un client vers le serveur local arrive en input et peut être interrompu par une règle drop mal ordonnée; conserver les exceptions existantes.

## Limite de la grille NSA
Le texte du TP exige la grille **du support**, qui n’a pas été fournie. La matrice présente dans le dépôt documente les domaines cités, sans revendiquer son identité avec la grille NSA officielle ni fournir des taux mesurés.
