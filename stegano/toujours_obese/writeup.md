`pngcheck -qv stage3.png`

Nous donne une structure valide mais étrange : 

```
File: stage3.png (388358 bytes)
  chunk IHDR at offset 0x0000c, length 13
    500 x 473 image, 32-bit RGB+alpha, non-interlaced
  chunk IDAT at offset 0x00025, length 8192
    zlib: deflated, 32K window, default compression
  chunk IDAT at offset 0x02031, length 8192
  chunk IDAT at offset 0x0403d, length 8192
  chunk IDAT at offset 0x06049, length 8192
  chunk IDAT at offset 0x08055, length 8192
  chunk IDAT at offset 0x0a061, length 8192
  chunk IDAT at offset 0x0c06d, length 8192
  chunk IDAT at offset 0x0e079, length 8192
  chunk IDAT at offset 0x10085, length 8192
  chunk IDAT at offset 0x12091, length 2213
  chunk IDAT at offset 0x12942, length 312240
  chunk IEND at offset 0x5ecfe, length 0
No errors detected in stage3.png (13 chunks, 58.9% compression).
```

Cependant, le dernier chunk IDAT semble bizarre : il ne répond pas au pattern de longueur des chunks précédents

J'ai essayé un coup classique : modifier la hauteur de l'image dans le chunk IHDR pour afficher de potentielles données cachées.
Le décodeur plante dès la ligne 474 (soit direct après les lignes composant l'image d'origine, de hauteur 473) en se plaignant que le filtre 137 n'existe pas.


Effectivement. Ce qui nous amène à notre seconde option : extraire les données du chunk et en carve la seconde image.
Coup de bol, l'octet dont s'est plaint le décodeur est 137. En hex, c'est 0x89, et c'est aussi le premier caractère de tous les fichiers PNG. Il y a fort à parier pour que le fichier complet ait été copié à la fin du chunk, ce qui signifie qu'on n'aura pas de découpage/collage à effectuer, ou si peu.

On extrait le stream zlib entier avec binwalk, on ne se fait pas chier :

`binwalk -e stage3.png`
`cat extracted/29.zlib | zlib-flate -uncompress > tmpng`

En fouillant un peu dans le stream, on trouve des trucs amusant : un gros paquets de chunks IDAT supplémentaires, ainsi que comme prévu un tag PNG, un IHDR et tout le toutim

Offset des magic bytes PNG : 947765
Taille totale de l'image : 1256965
Octets à carve : 309200

(le IEND est tout à la fin, on n'a donc pas besoin de supprimer des octets finaux, juste de supprimer ceux en trop au début)

On recrée une image d'après l'offset du tag PNG :

`tail -c 309200 tmpng > flag.png`

On la pngcheck, on a bien un fichier png mais avec des erreurs : des 0x08 ont été écrit à quelques endroits dans les headers de chunk. On ghex tout ça pour corriger vite fait puis enfin pngcheck nous donne le feu vert.

```
$ pngcheck flag.png
flag.png  invalid IHDR compression method (8)
flag.png  invalid IHDR filter method (8)
flag.png  invalid IHDR interlace method (8)
ERROR: flag.png

$ pngcheck flag.png
flag.png  invalid bKGD length
ERROR: flag.png

$ pngcheck flag.png
flag.png  invalid pHYs length
ERROR: flag.png

$ pngcheck flag.png
OK: flag.png (800x600, 32-bit RGB+alpha, non-interlaced, 83.9%).
```

On ouvre l'image avec 3 beaux dés et 1 beau flag :

`404CTF{z71ll_0b3z3_&_st1ll_h4d_s3cr3tz_4_U}`

