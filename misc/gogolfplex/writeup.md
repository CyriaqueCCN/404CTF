Acces : `nc challenge.404ctf.fr 32697`

On cherche donc un entier qui est <= à 10\*\*25 malgré les précautions prises
(strip les whitespaces, virer les -+0 en début de chaîne et s'assurer d'ajouter plein de zéros à la fin)

On épluche la doc python et dans celle de int on trouve une astérisque intéressante :

`Changed in version 3.6: Grouping digits with underscores as in code literals is allowed.`

Écrire
`1_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0`

donnerait donc exactement 10\*\*, et heureusement pour nous c'est inférieur **ou égal**.

On envoie donc ce bel entier valide et on récupère le flag :

`404CTF{Und3r5c0r35_1n_1nt3g3r5??}`
