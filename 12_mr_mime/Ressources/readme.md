# 12 Mr Mime

- On est allé voir la page `upload`
- On a vu qu'on pouvait envoyer des fichiers, mais a priori seulement des .jpeg
- On a ouvert burpsuite, pour bidouiller la requete pendant l'envoi
- En envoyant un fichier .txt
- On a changé le Content Type de la requete, rien
- On a envoyé un jpeg avec de la fausse donnée, rien
- On a envoyé un fichier PHP avec le content-type jpeg
- Et hop flag

## Annexe

Pour ne pas avoir a installer burpsuite, le comportement est reproduisible avec une simple
requete curl

```
curl -sX POST -F "uploaded=@hack.php;type=image/jpeg" -F "Upload=Upload" "http://192.168.56.103/index.php?page=upload" | grep "flag"
```

En remplaçant l'IP si necessaire, et en créant un fichier bidon `./hack.php` au préalable