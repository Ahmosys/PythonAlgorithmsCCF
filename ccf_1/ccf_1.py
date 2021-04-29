## Fonction permettant de vérifier si l'image est complétement noire (cinstituée que de 0).
def verifyImage (array):
    amount = 0 #Compteur
    for list in array: #Boucle pour parcourir tout les éléments du tableau
        for element in list:
            if element > 0: #Condition (si l'élement dans le tableau est strictement plus grand que 0 alors on l'ajoute à la somme (amount))
                amount = amount + element
    if amount > 0: #Condition (si la somme est plus grande que 0 soit que il y a au minimum un élément qui était plus grand que 0
        print("Le tableau n'est pas tout noir") #On peut également utiliser return au lieu de print. (c'est juste plus jolie esthétiquement dans la console)
    else:
        print("Le tableau est tout noir.")

## Fonction permettant de calculer la moyenne de luminosité de l'image.
def averageImage(array):
    coeff = 0 #Compteur (nombres d'élements)
    amount = 0 #Compteur (somme)
    for list in array: #Boucle pour parcourir tout les éléments du tableau
        for element in list:
            amount = amount + element #Permet d'obtenir la somme de tout les éléments
            coeff = coeff + 1 # A chaque élément on ajoute 1 à coeff ce qui nous permettras de trouver le nombre d'élements total
    average = amount / coeff #Calcul pour trouvé la moyennes (somme / coefficient)
    return average

## Fonction permettant de jugée si l'image est satisfaisante ou non en se basant sur sa moyenne de luminosité.
def retouchImage(array):
    if averageImage(array) >= 100 and averageImage(array) <= 150:
        print("L'image est satisfaisante et n'auras pas besoin de retouche.", "\nLa moyenne est de : " , averageImage(array))
    else:
        print("L'image auras besoin d'une retouche.", "\nLa moyenne est de : " , averageImage(array))


## Test de toutes les fonctions (appel des fonctions)
print(verifyImage([[1,1,1,1],[0,0,0,1]]))
print(averageImage([[1,1,1,1],[0,0,0,1]]))
print (retouchImage([[1,1,1,1],[0,0,0,1]]))
