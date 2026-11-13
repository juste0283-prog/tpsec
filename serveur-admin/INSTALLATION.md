# Installation SRV-ADMIN (Ubuntu 24.04)

1. Vérifier `ip -br link`; recopier `50-lab.yaml.example` dans `/etc/netplan/50-lab.yaml` en adaptant le nom d'interface.
2. `sudo chmod 600 /etc/netplan/50-lab.yaml && sudo netplan try` puis `sudo netplan apply`.
3. `sudo apt update && sudo apt install -y freeradius freeradius-utils chrony nmap snmp rsyslog` (accès Internet avant séance).
4. `sudo install -d -o syslog -g adm -m 0750 /var/log/reseau`.
5. Placer `10-reseau.conf.example` dans `/etc/rsyslog.d/10-reseau.conf`; `sudo rsyslogd -N1 && sudo systemctl restart rsyslog`.
6. Ajouter les lignes de `chrony.conf.append.example` à `/etc/chrony/chrony.conf`. Configurer la clé NTP demandée **localement**, sans la publier. `sudo systemctl restart chrony`.
7. Ajouter les clients RADIUS et les comptes depuis les modèles, mais remplacer les secrets localement. `sudo freeradius -XC` puis `sudo systemctl stop freeradius && sudo freeradius -X`.
8. Dans un second terminal tester `radtest wilfried.admin 'MOT_DE_PASSE_LOCAL' 127.0.0.1 0 'SECRET_DU_CLIENT_LOCALHOST'` en tenant compte du secret localhost existant dans clients.conf.
9. Tester `ping -c 3 10.10.99.1`, `ping -c 3 172.16.12.2`, `ping -c 3 198.51.100.1`, `chronyc tracking`, `ss -lunp` et `systemctl status rsyslog chrony`.

**Routes :** il faut que les routeurs disposent des routes retour vers 10.10.99.0/24, sinon RADIUS/syslog/NTP ne fonctionneront pas. Ne pas supposer que le ping de départ suffit à tester l'aller-retour complet de tous les protocoles.

**Note importante :** les services UDP 1812/1813 (RADIUS), 514 (syslog), 123 (NTP) doivent être joignables des IP prévues. Les règles de filtrage routeur doivent les autoriser de façon ciblée.
