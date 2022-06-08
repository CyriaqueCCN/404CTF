C'est de la doc bête et méchante. Une fois les bases acquises, on comprend qu'on doit se créer un compte sur Infuria (Eth > Ropsten) puis utiliser les creds fournis pour se connecter via Web3

ABI sert à créer des metadata pour un contract, on s'en sert ici pour l'identifier
( on doit installer solc pour ça, google it)
```from solcx import install_solc
install_solc(version='latest') # ou 0.8.13```

En lisant la source, on remarque également que la variable password est publique.
On l'appelle donc via l'api python et banco, on récupère le pass

`404CTF{M0N_M07_D3_P4553_357_7r0P_53CUr153_6r4C3_4_14_810CKCH41N}`
