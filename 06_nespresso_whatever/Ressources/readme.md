# 06 Nespresso Whatever

- On est allé voir `robots.txt`
- On a vu `Disallow: /whatever`
- On est allé voir `whatever`
- On a vu qu'il y avait un fichier `htpasswd`
- Dans ce fichier on trouve un couple username:password
- On a checké le hash du mdp
- MD5: qwerty123@
- On est allé sur la page `admin` (vu que ça fonctionnait pas sur la page de login)
- On a mis les credentials `root` et `qwerty123@`
- Et hop flag
