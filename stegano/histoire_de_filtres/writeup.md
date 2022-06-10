`pngcheck -vv stage4.png > check_filters.txt`

On déduit du titre du challenge qu'on doit manipuler les filtres pour obtenir le flag.

On observe que la majorité des lignes sont en filtre 4

Pour rappel, PNG encode chaque ligne séparément avec un filtre correspondant à l'algo de compression pouvant varier à chaque ligne de pixels

D'après [la spec PNG sur les filtres](http://www.libpng.org/pub/png/spec/1.2/PNG-Filters.html)

```
Type    Name
   
   0       None
   1       Sub
   2       Up
   3       Average
   4       Paeth
```

La section [choisir ses filtres](http://www.libpng.org/pub/png/spec/1.2/PNG-Encoders.html#E.Filter-selection) nous explique quel type de filtre correspond mieux à quel cas.

Grosse flemme de scripter ça.

