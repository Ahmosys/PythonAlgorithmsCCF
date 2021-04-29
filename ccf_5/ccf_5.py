## Fonction créant une cible et l'affiche.
def cible():
    array=[[0 for k in range(7)]for k in range(7)] #On pouvait plus simplement écrire le tableau à la main
    for i in range(1,6):
        for j in range(1,6):
            array[i][j]=5
    for i in range(2,5):
        for j in range(2,5):
            array[i][j]=10
    array[3][3]=20
    return array

## Fonction créant un tableau permettant de faire 10 tir avec le numéro de la ligne et de la colonne touché sur la cible.
from random import*
def casestouchees():
    cases=[[randint(0,6)for k in range(10)],[randint(0,6) for k in range(10)]]
    return cases

## Fonction comptant le nombre de points marqués au total en aditionnant les éléments touchés de la cible au fur (déduit de la position graçe à la fonction casestouchees()).
def pointmarque(array):
    points=0
    coup=[]
    for i in range(10):
        coup.append(cible()[array[0][i]][array[1][i]])
        points=points+cible()[array[0][i]][array[1][i]]
    return points

## Test de toutes les fonctions (appel des fonctions)
print(cible())
print(casestouchees())
print(pointmarque(casestouchees()))
