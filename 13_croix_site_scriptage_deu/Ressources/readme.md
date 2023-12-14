# 13 Croix Site Scriptage Deu

- On est allé voir la page `media`
- On a vu qu'on pouvait bidouiller le parametre `src`
- On a vu que le changement se répercute dans une balise `<object>`, son champ `data`
- On tente de mettre différentes choses dedans
- sans succes on tente de mettre des elements base64 sous cette forme
`/?page=media&src=data:<MIME Type>;base64,<contenu en base64>`
- le contenu `text/plain` fonctionne, on voit le texte s'afficher
- on tente de mettre ceci
`/?page=media&src= data:text/html;base64,PHNjcmlwdD5hbGVydCgnY3B0Jyk8L3NjcmlwdD4=`
Qui correspond au html `<script>alert('cpt')</script>`
- Et hop, flag
