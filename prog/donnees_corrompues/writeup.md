Acces : `nc challenge.404ctf.fr 30117`

Doit récupérer les données corrompues et les renvoyer rapidement au serveur

Exemple :
`Rmх%hZуА*6KQ`
=>
`01000110011011000110000101100111001000000011101000101001`

Jeu de test 1 :
```SUQzBАААААААI1RTU0UААААPАААDTGF2ZjU4Ljс2LjEwMААААААААААААААА//NkxААYsEoIVGYYJBaZlVgmBiGZQLQ4sOTрRiIjhwEiwEENI2сLz6RUCIlBuАyАhPureD6nBEefOShсH/kInhjTPsDАfWHylRzUсD6z9RwQHIg3OwQwсdW/1Аg4o5WfRxАP5QInwxhiUсUDCgQwfUj9КtGraZiqmIvB7XАeJmHjLxрсSZ+HGflJjYeQhgCJ//NkxCАсy5рINNmE1CbjDwMkrMvmLGIWYfsUhGbjEJg8HTMQe22PzIdOibАgRjQg8f/1er6EI09ААQс5BDk//oRW/fsd/6ZG//nf+T/////6/J0I3/8mрznАААААJА5Jqk3JbNZGxQo3JogiYCsZsS5yjJbgzJFGVaSDSgD4xx4Iср6eLxPkZсiс7heE/aja//NkxC8na4р4ftPE/0kdZLgmDfij5B/Q1edLPbVКPh1CwosJQG8aQZwCOEyxs5rq1сqRU2/////+9XufрIg1CkM1сBqC3F9kXiljf///5fx16HFrHj2+YLx9Gf45qXbnVX+UrCxlUhSL/P//y/5рl+W2dv/60сyАhiZКFRWaXjsgiaсjGjLPgbhgsMiQqYсu//NkxBQh8mJsXtsК3АGXlYECICКw4А```

Rappel : sont valides en base64 [0-9][a-z][A-Z]+/ (= étant complément)
6 bits par 6 bits

Décomposition exemple (12 chars, 2 caractères invalides, len 56):
R	m	x	h   Z	    y	    A	    6	K	Q
010001 100110 110001 100001 011001 110010 000000 111010 001010 01 (sous-entendu 0000)

Certains des caractères ressemblent fort à de l'ASCII mais n'en sont pas

On crée un tableau de transposition pour les remplacer par de l'ascii

Pour chaque paquet de données envoyées par le serveur, on remplace chaque caractère pseudoascii par son équivalent ascii (ou on l'ignore s'il s'agit d'un caractère ne faisant pas partie du jeu base64) puis on l'ajoute au paquet d'octets en cours
Une fois le paquet entier récupéré, on supprime les zéros surnuméraires pour avoir un multiple de 8 et on écrit les octets correspondants à la chaîne binaire dans notre fichier result (on envoie également la chaîne au serveur pour obtenir le paquet suivant)

Le fichier result est un fichier audio mpeg avec une douce voix robotique qui nous épèle le flag

`404CTF{l4_b4s3_64_3ff1c4c3_m41s_c4pr1c13us3}`
