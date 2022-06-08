`nc challenge.404ctf.fr 32128`

Le service nous donne plein d'infos.
N = int (len 2048, soit 256 bytes)
e = 65537 (2\*\*16+1, common e pour RSA)
Et nous répond quand on lui envoie d'autres entiers.
On se doute qu'il applique la même clé et le même algo avant de nous répondre
La clé change à chaque session de netcat, donc exit l'attaque offline

Il nous renvoie 0 ou 1 si on lui donne 0 ou 1, sinon il est cohérent.

Padding oracle ?

