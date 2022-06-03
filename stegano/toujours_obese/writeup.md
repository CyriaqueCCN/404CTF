`pngcheck -qv stage3.png`

Nous donne une structure valide : 

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

Cependant, le dernier chunk IDAT semble étrange : il ne répond pas au pattern de longueur des chunks précédents

On peut essayer de modifier la longueur de l'image pour afficher plus de données
OU
Extraire le chunk

Changer la hauteur de l'image (et recalculer le CRC de IHDR) fonctionne, mais le décodeur plante : des octets de filtre sont invalides (137 au lieu de 0-4) dans le dernier IDAT. Forcément. Dès la ligne suivant la 473 d'ailleurs. Ce ne sont peut-être pas des données d'image ?

Pour le savoir, il va nous falloir extraire le zlib correspondant


