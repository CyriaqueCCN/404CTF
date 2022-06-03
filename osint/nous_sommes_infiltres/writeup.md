Pseudos :

```
mh4ckt3mh4ckt1c4s (actif depuis Janvier 2017)
Artamis (actif depuis Septembre 2021)
Redhpm (actif depuis Mars 2021)
Xx_Noel_Janvier_xX (actif depuis 24 Fevrier 2022)
Alternatif (actif depuis Septembre 2020)
```

Suspect : `Xx_Noel_Janvier_xX`, inscrit cette année

Sur son profil Rootme, on voit un lien vers son site web
`https://e10pthes.github.io/about/pages/welcome.html#`
Il possède également un twitter
`https://twitter.com/e10pthes`
Et est suivi par "Pablo Sintera", disant être un grand fan de hallebardes dans son profil.
On tient notre suspect, reste à trouver la preuve

Le fameux Pablo Sintera s'est plaint d'être redirigé sur un site étrange il y a 18 jours
On va vérifier les commits sur le github du site et on trouve un truc intéressant

`https://github.com/e10Pthes/about/commit/0e92db3b1cfc38c06225e4fcd8036bca6f86924e`

La ligne `action="http://hallebarde.duckdns.org/"`

On va sur le site en question

`http://hallebarde.duckdns.org/`

Et on trouve le flag :

`404CTF{Att3nt10n_AU8_V13ux_C0mMiT5}`
