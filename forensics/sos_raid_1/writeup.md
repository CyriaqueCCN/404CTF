On a 2 disques en RAID, on sait qu'on en a besoin d'au moins 3 pour un RAID5

On va essayer de recréer le 3ème disque : il s'agit simplement d'XOR le contenu des 2 autres, octet par octet (puisque blocksize=1)

Une fois le disque récupéré, il faut maintenant récupérer les octets en supprimant ceux de contrôle (2 sur 3 donc avec 3 disques).

On a un indice avec le nom des fichiers disk mais dans le doute on va recréer toutes les permutations possibles au cas où les disques ne sont pas dans le bon ordre.

`$ file res_*`

```
res_012.img: Zip archive data, at least v2.0 to extract
res_021.img: data
res_102.img: data
res_120.img: data
res_201.img: data
res_210.img: data
```

Effectivement, les disques étaient dans l'ordre, le seul résultat intéressant étant le fichier zip.

On l'unzip et on obtient 2 fichiers, un contenant notre flag et le second servant probablement à l'étape 2.

`$ cat flag.txt`
`404CTF{RAID_5_3st_p4s_tr3s_c0mpl1qu3_1abe46685ecf}`
