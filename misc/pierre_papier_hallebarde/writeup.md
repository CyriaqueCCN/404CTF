On est en python2 : la fonction input() est vulnérable

Contrairement à sa conjointe `raw_input()`, elle évalue son contenu

On craft donc un payload pour afficher le flag et lui faire print (on perdra la partie après, hélas)

`__import__('sys').stdout.write(open("flag.txt", "r").readline())`

Nous affiche le flag gentiment
