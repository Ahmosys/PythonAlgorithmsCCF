## Fonction permettant de compter le nombre de pixel noir (à 1) dans une image de taille n*p. (compterPixelsA1)
def countPixelsA1(array):
    amount = 0 #Compteur
    for list in array: #Boucle pour parcourir tout les éléments du tableau
        for element in list:
            if element == 1: #Condition
                amount = amount + element
    return amount

## Fonction permettant de crée une image blanche composée d'une bordure noire. (cadreNoir)
def blackFrame(n,p):
    array = [[0 for k in range (p)] for l in range (n)] #Créer un tableau de p colonnes et n lignes
    for i in range (n): #Boucle pour parcourir tout les élements du tableau
        for j in range (p): #Condition pour obtenir une bordure noire soit que de 1
            if (i == 0) or (i == n-1) or (j == 0) or (j == p-1):
                array[i][j] = 1
    return array

## Fonction permettant de superposer deux images. (superposerImages)
def overlayImage(array1,array2):
    nbrLines = len(array1) #Obtient le nombre de lignes
    nbrCol = len(array1[0]) #Obtient le nombre de colonnes
    array3 = [[0 for k in range (nbrCol)] for l in range (nbrLines)]  #Nouveau tableau ayant le même nombre de col et de ligne que le tableau en paramètres
    for i in range (nbrLines): #Boucle pour parcourir tout les éléments du tableau
        for j in range (nbrCol):
            if array1[i][j] == 1 or array2[i][j] == 1: #Condition
                array3[i][j] = 1
    return array3

## Fonction crée une image formant un X. (mystere)
def mystery(n):
    array = [[0 for k in range (n)] for l in range (n)] #Créer un tableau de n colonnes et n lignes
    for i in range (n): #Boucle pour parcourir tout les éléments du tableau
        for j in range (n):
            if ((i==j) or (i+j+1==n)): #Condition
                array[i][j] = 1
    return array
