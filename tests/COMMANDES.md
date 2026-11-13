# Tests et commandes à effectuer et photographier

## TP3.1 MikroTik (8)
1. Services : `sudo nmap -sS -sU -p T:1-10000,U:53,123,161 172.16.12.2` (adapter si nmap refuse l'expression : lancer TCP et UDP séparément).
2. Refus : depuis PC-GUICHET tester TCP 22 vers 10.20.10.1, puis `/log print where message~"INPUT-REFUS"`.
3. RADIUS : `ssh wilfried.admin@172.16.12.2`, voir `freeradius -X`.
4. Logs : `sudo tail /var/log/reseau/172.16.12.2.log`.
5. Heure : `/system clock print` et `/system ntp client print`.
6. Source : `/ip settings print`.
7. L2 : `/tool mac-server print` et `/ip neighbor discovery-settings print`.
8. DHCP : sur PC-GUICHET `ip dhcp`.

## TP3.2 Cisco (8)
1. SSH autorisé 10.10.99.20 et refusé 10.10.10.x ; `show access-lists ADMIN-SOURCES`.
2. AAA : `show running-config | section aaa` puis SSH compte nominatif et FreeRADIUS Access-Accept.
3. Repli : stopper temporairement FreeRADIUS, tester `secours`, puis redémarrer FreeRADIUS.
4. SNMP : `snmpwalk -v3 -l authPriv ... 10.10.99.1 1.3.6.1.2.1.1` et s'assurer que `-v2c -c public` échoue.
5. Logs : changer une description d'interface ; consulter `sudo tail /var/log/reseau/10.10.99.1.log`.
6. NTP : `show ntp status` et `show clock`.
7. Source/WAN : `show ip interface GigabitEthernet0/1 | include verify` ; `show access-lists WAN-ANTI-USURPATION`.
8. Services : scans TCP/UDP depuis SRV-ADMIN et source non autorisée.

## TP3.3 VyOS (6)
1. `ssh vyos@198.51.100.1` refusé après suppression confirmée.
2. `ssh wilfried.admin@198.51.100.1` et `Access-Accept` FreeRADIUS.
3. Depuis SRV-INTERNET 203.0.113.10, SSH 198.51.100.1 refusé.
4. `show configuration commands | match source-validation`.
5. `sudo tail /var/log/reseau/198.51.100.1.log`.
6. `show ntp`.

## TP3.4 (3 tests de révocation, plus deux livrables sans nombre de captures imposé)
1. Créer `prestataire.temp` uniquement sur FreeRADIUS ; connexion réussie sur les trois routeurs.
2. Supprimer ce compte, redémarrer le service ; photographier le refus sur chacun des trois routeurs.
3. Reconstruire les événements à partir des vrais journaux ; remplir grille NSA, états avant/après et dates d'écarts.

**Précaution :** 22 vérifications listées TP3.1–3.3 et 3 refus TP3.4 = **25 preuves planifiées** ; le professeur ne fixe pas explicitement exactement 25 captures. Une capture par vérification demandée est requise, dans **5 pages maximum**.
