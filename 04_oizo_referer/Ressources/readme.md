# 04 Oizo Referer

- On est allé sur la page de Copyright
- En inspectant la page, on a constaté que la page était remplie de vide
- On a ouvert le fichier HTML source et strippé le vide
- On a lu les deux infos suivantes
  - `You must come from : "https://www.nsa.gov/".`
  - `Let's use this browser : "ft_bornToSec". It will help you a lot.`
- On en a donc conclu qu'il fallait respectivement modifier les headers
    - Referer
    - User-Agent
Avec les valeurs renseignées
- Et hop flag