On a apparemment un mot de passe obfusqué en utilisant les autocasts dégueulasses de JS.
Ça a même un nom : le JSfuck. Forcément.
On exécute le premier replace pour obtenir les symboles JS et on les colle dans [JSFuck](http://www.jsfuck.com/)

On a une erreur parce que jQuery n'est pas défini mais c'est tant mieux, on peut voir le résultat dans l'inspecteur de firefox (en cliquant sur le numéro de ligne de l'erreur)

Le code s'évalue à ça : 

```/* FONCTIONNEMENT */
var key = $(".keypad").keypad(function (pin) {
  if (pin == "240801300505131273100172") {
    document.location.href = "./nob03y_w1lL_Ev3r_fiNd_th15_PaGe.html";
  }
});```

En accédant à la [page indiquée](https://fiche-js.404ctf.fr/nob03y_w1lL_Ev3r_fiNd_th15_PaGe.html), on obtient le flag

`404CTF{Haha_J3_5ui$_f4N_dObfu5c4tIoN_en_JS}`
