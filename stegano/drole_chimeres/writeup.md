On remarque le fichier possède 2 chunks IEND, 2 streams ZLIB et 2 chunks IHDR (illégal)

De plus, une paire IHDR-IEND est obfusquée par un chunk de longueur 388350 avec l'identifiant sTeG (inconnu au bataillon, ça va sans dire)

On extrait les octets avec le même en-tête PNG que le fichier précédent dans carved.png et on peut l'ouvrir, on se tape la recopie d'un nouveau flag :

`404CTF{7h47_v1c10us_m1zzing_z19natur3}`
