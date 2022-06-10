Acces : `nc challenge.404ctf.fr 30885`

Faut créer un contrat qui appelle l'autre pour bypass le tx.origin != msg.sender

Mais msg.sender doit être le dernier appelant (sinon ce ne sera pas notre adresse whitelistée

Ou alors utiliser l'adresse de notre contrat malicieux comme user ? Je ne vois pas d'autre options, sauf si 1 utilisateur peut appeler 1 contrat qui appelle 1 utilisateur qui appelle 1 contrat.


