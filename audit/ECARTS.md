# Écarts prévisibles à vérifier et non à déclarer sans preuve
- IOSv : négociation SSH pouvant nécessiter `ssh-rsa` et `diffie-hellman-group14-sha1` ; si constaté, noter l'écart et la nécessité d'une image plus récente. Ne pas généraliser à toutes les images.
- MikroTik : version stable actuelle à comparer à la version relevée (`/system resource print`, `/system package print`) le jour du TP.
- VyOS : strict uRPF potentiellement inadapté si routage asymétrique ou multi-opérateur : vérifier la topologie et justifier loose/strict.
- NTP MD5 : vérifier la prise en charge réellement disponible sur les trois images ; un horodatage synchronisé n'implique pas une authentification NTP correcte.
- Journalisation : la capture de fichiers dans `/var/log/reseau/` ne prouve pas nécessairement l'identité de toutes les commandes ; compléter par le test du contenu et du format réel.

## Réponse à la question entreprise (TP3.3)
En présence de plusieurs opérateurs et de routage potentiellement asymétrique, uRPF strict peut rejeter un paquet légitime dont le chemin retour préféré diffère de l'interface d'arrivée. Un contrôle en mode lâche vérifie plutôt que la source soit routable, réduisant ces faux positifs sans offrir le même niveau de garantie anti-usurpation. En environnement mono-homé et symétrique, strict peut convenir. Sur une bordure multi-opérateurs, privilégier loose, complété par filtrage d'adresses sources/bogons et règles d'interface adaptées ; démontrer la décision sur la topologie réelle.
