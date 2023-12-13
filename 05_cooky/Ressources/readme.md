# 05 Cooky

- On a constaté un cookie nommé `I_am_admin`
- Vu que c'etait pas forcement lisible, on a passé le cookie dans un detecteur de hash
- Il nous a dit que c'etait du md5
- On passé le token dans un dehasheur md5, la valeur etait `false`
- Du coup on a essayé de mettre le hash md5 de `true` dans la valeur du cookie
- et hop flag
