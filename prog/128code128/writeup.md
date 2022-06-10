Accès : `nc challenge.404ctf.fr 30566`

Décoder les images et renvoyer le résultat.

Ce sont des PNG (308\*100) qui ressemblent à un code barre mais qui sont indéchiffrables par des lecteurs conventionnels. Il doit manquer des morceaux.

On commence par la base : extraire les données.

Après une bonne lecture de [l'article Wiki](https://fr.wikipedia.org/wiki/Code_128) et d'un [autre tuto cool](https://www.precisionid.com/code-128-faq/), on se lance.

On commence par créer une fonction qui récupère une chaîne base64 et en fait une image, ce qui se fait facilement avec les modules PIL, io et base64.

Ensuite, on récupère la couleur moyenne des pixels à différentes hauteur pour chaque colonne de pixel (on moyenne 3 points pour être sûrs d'avoir la bonne, c'est overkill). Si les pixels se rapprochent de (255,255,255), la colonne est blanche et donc un espace, si c'est (0,0,0), c'est noir et donc une barre. On crée ainsi un tableau qui a comme longueur la largeur de l'image. On remarque que la largeur de chaque image envoyée par le serveur est un multiple de 11 : il manque donc au minimum le stop, puisque c'est le seul caractère défini par le standard qui n'est pas codé sur 11 barres/espaces (mais sur 13). On subodore qu'il manque aussi le START, et potentiellement le caractère de contrôle.

Par convenance, je groupe directement les barres et espaces par 11 pour faciliter le décodage.

Ensuite, je copie colle le tableau de wikipédia (dans `mappings.tsv`) pour mapper les barres/espaces à leur valeur. Comme on n'a probablement pas le START, on ne sait pas quel est le mode de caractères du début. On parie tout de même sur ASCII, parce que. On écrit un petit parser pour extraire proprement les mappings de notre fichier TSV et on est prêts à s'attaquer au serveur distant.

Pour ça, le classique remote de pwnlib fait toujours le café et on encapsule toutes nos fonctions précédentes dans une routine qui va exécuter 128 fois le cycle lecture image/décodage/envoi du mot de passe avant de, avec du bol, lire le flag.

À ce stade, très fier de moi, j'ai exécuté une bonne centaine de fois mon script en essayant toutes les combinaisons possibles de Code (A, B, C, Ascii, Latin1, Hexa...), en prenant en compte la présence potentielle ou non du bit de contrôle (c'est à dire en l'ignorant totalement) voire du START. Las, il m'a fallu une bonne heure pour me rendre compte que je ne lisais pas le base64 envoyé par le serveur mais celui de mon fichier de test.

Une fois la tête dûment frappée contre le mur et le script relancé, on court à la rescousse de notre agent de terrain #249 et le pauvre hère nous remercie :
```
Oh merci merci merci ! Me voilà enfin libre ! Voilà un cadeau pour te remercier :
404CTF{W0w_c0d3_128_4_pLUs_4uCuN_s3cr3t_p0uR_t01}
```
Désolé à ses 248 prédécesseurs. 
