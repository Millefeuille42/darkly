# 09 SQL Injection 2 Le Retoure

- On a tenté de mettre plein d'ID d'images jusqu'a ce que ça ne fonctionne plus
- L'image #5 intitulée "Hack me ?" nous a interpelée
- En conservant les résultats d'énumération de db du flag précédent on a fait cette requete dans la page `searchimg`
`1 UNION SELECT CONCAT(id, 0x0a, url, 0x0a, title, 0x0a, comment), null FROM Member_images.list_images`
- On constate que la fameuse image #5 contient la phrase suivante dans son commentaire
"
If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
"
- Apres avoir dehash on obtient: albatroz
- On suit le reste des instructions
- Et hop flag