# carrefour-check-status

Petit bout de code en Python pour vérifier les stocks de Carrefour dans tous les départements de France pour trouver une Xbox Series X ! 
Le code utilise l'API de Carrefour pour vérifier s'il y a un magasin avec du stock partout en France. Ca prend environ 11 minutes à faire le tour chez moi. A la fin, un petit résumé est disponible avec les magasins où il y a du stock (s'il y en a...).

## Comment faire tourner le code

Il faut avoir Python3, pip3 et utiliser pip3 pour installer les 2 modules importés au début du code.

Ensuite, plus qu'à faire un `python3 main.py`

## Résultats :

Les résultats ressemblent à ça :

<img width="269" alt="Screenshot 2021-11-17 at 22 27 39" src="https://user-images.githubusercontent.com/63878365/142285124-ee4166da-48a3-4ff8-98a4-9625846fd736.png">


S'il y a du stock, ça mettra la liste des magasins avec leur nom et leur code postal.
