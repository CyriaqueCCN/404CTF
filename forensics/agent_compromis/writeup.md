# Un agent compromis
### (en 3 parties)

## 1/3

On convertit le fichier pcapng en pcap pour le passer dans NetworkMiner (parce qu'on est trop pauvres pour payer la version pro) et on observe 2 communications intéressantes entre ctf.404 et hallebarde.404

La première est un repértoire HTML, la seconde un fichier python nommé exfiltration

On l'ouvre et dans une variable à la fin du script se trouve le flag

`404CTF{t3l3ch4rg3m3n7_b1z4rr3}`


## 2/3

Le fichier python trouvé exfiltre les fichiers du repértoire courant en les faisant passer pour des requêtes DNS
On écrit un petit script basé sur dpkt pour extraire les données qui nous intéressent et recréer les fichiers dans un repértoire créé pour l'occasion

`mkdir exfiltration`
 =>
`./solve.py`
 =>
`echo "404CTF{$(ls -m ./exfiltration | tr -d ' ')}"`
 =>
`404CTF{exfiltration.py,flag.txt,hallebarde.png,super-secret.pdf}`


## 3/3

On cherche à présent le flag caché dans un de ces 4 fichiers.
Le premier est notre script python, rien d'intéressant
Le second est un faux flag, sinon ce serait trop simple
Le troisième est un fichier png valide mais c'est du forensics, pas de la stego
Reste le quatrième, un fichier PDF apparemment blanc mais pesant 9 Ko
Le brief nous dit que les données ont été effacées

Il nous faut utiliser des outils de récupération, mais aucun ne semble nous donner de fichier exploitable.

Il va falloir mettre les mains dans le cambouis
On extrait les fichiers contenus dans notre pdf, on trouve 3 streams zlib

On les inflate pour voir ce que ça donne

Au premier abord, le plus gros est invalide (mauvaise taille)
On extrait les octets composant le stream zlib à la mano et on le décompresse pour obtenir un gros fichier : c'est une police d'écriture...
Raté (mais c'est joli Liberation Serif)


Le second est déjà plus lisible :

```/CIDInit/ProcSet findresource begin
12 dict begin
begincmap
/CIDSystemInfo<<
/Registry (Adobe)
/Ordering (UCS)
/Supplement 0
>> def
/CMapName/Adobe-Identity-UCS def
/CMapType 2 def
1 begincodespacerange
<00> <FF>
endcodespacerange
24 beginbfchar
<01> <0034>
<02> <0030>
<03> <0043>
<04> <0054>
<05> <0046>
<06> <007B>
<07> <0044>
<08> <004E>
<09> <0053>
<0A> <005F>
<0B> <0033>
<0C> <0078>
<0D> <0066>
<0E> <0031>
<0F> <006C>
<10> <0074>
<11> <0072>
<12> <006E>
<13> <0068>
<14> <0061>
<15> <0065>
<16> <0062>
<17> <0064>
<18> <007D>
endbfchar
endcmap
CMapName currentdict /CMap defineresource pop
end
end```

Ça semble encoder une suite de caractères
Vérifions les en décodant l'hexa 

`34304354467B444E535F337866316C74726E68616562647D`
=>
`40CTF{DNS_3xf1ltrnhaebd}`

C'est un début, mais il manque des lettres...
On remarque que chaque lettre n'apparaît qu'une fois.
Plutôt qu'un texte, c'est donc probablement un index.

On se doute que le flag final va ressembler à

`404CTF{DNS_3xf1ltr4710n_hal1eb4rd3}`. On pourrait le bruteforce (les combinaisons leet sont limitées) mais on a déjà ruiné notre ratio de try/fails avec les challs OSINT.


Heureusement, le troisième morceau va nous aider :

```
0.1 w
q 0 0.028 595.275 841.861 re
W* n
q 0 0 0 rg
BT
56.8 773.989 Td /F1 12 Tf[<0102010304>2<05>-1<06>-3<07>5<08>-2<09>-1<0A0B0C0D0E0F>2<10>2<1101>-7<10>2<0E02120A1314>1<0F>2<0F>-5<15>1<1614>1<111715>1<18>]TJ
ET
Q
Q
```

Bien que sensiblement moche au premier abord, cette partie semble se réferer à des caractères indexés de 01 à 18 (en hexa), ce qui est exactement la taille de l'index trouvé en deuxième partie. Marrant !
BT et ET marquent le 'Beginning / End of Text', ce qui nous conforte dans notre idée.
Jouons au puzzle.

01-09 : `40CTF{DNS`
0A-0F : `_3xf1l`
10-18 : `trnhaebd}`
`<0102010304>2<05>-1<06>-3<07>5<08>-2<09>-1<0A0B0C0D0E0F>2<10>2<1101>-7<10>2<0E02120A1314>1<0F>2<0F>-5<15>1<1614>1<111715>1<18>`

`404CTF{DNS_3xf1ltr4t10n_hallebarde}`

Je ne sais pas à quoi servent les chiffres non balisés mais j'ai déjà suffisamment lu de spec sur le PDF pour aujourd'hui.