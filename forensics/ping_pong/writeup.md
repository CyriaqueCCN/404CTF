On a un fichier de capture de paquets entre 2 IP locales s'échangeant des pings.

Peut-être que les données de chaque ping contiennent des données ?

En les analysant, on remarque qu'elles contiennent toutes les lettres de l'alphabet et des chiffres.
Le calcul de l'indice de coïncidence m'a induit en erreur : il est de 4.8, soit pile celui d'un texte écrit en anglais ou en français, et pas du tout aléatoire
comme devrait l'être un texte chiffré ou des données random. Je n'ai remarqué qu'après que c'était le cas parce qu'il n'est composé que de lettres...

Après avoir essayué tous les chiffrement du genre Pollux et Vigenère, on regarde à nouveau les données et on remarque un truc : la longueur des paquets change
mais elle est toujours dans la plage des caractères ASCII. Mieux que ça, la dernière est 125, pour "}"...

Petit coup de script et on a le flag

`404CTF{Un_p1ng_p0ng_p4s_si_1nn0c3nt}`
