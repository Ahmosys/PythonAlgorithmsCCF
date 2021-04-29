## Fonction permettant de transformer l'image en négative en inversant les 1 et les 0.
def negative(array):
    nbrLine = len(array) #Obtient le nombre de lignes
    nbrCol = len(array[0]) #Obtient le nombre de colonnes
    for i in range (nbrLine): #Boucle pour parcourir tout les éléments du tableau
        for j in range (nbrCol):
            if array[i][j] == 1: #Condition
                array[i][j] = 0
            else:
                array[i][j] = 1
    return array

## Fonction permettant de retourner une image deux fois plus grande que celle fournit de base.
def double(array):
    nbrLines = len(array) #Obtient le nombre de lignes
    nbrCol = len(array[0]) #Obtient le nombre de colonnes
    arrayDouble = [[0 for k in range (2*nbrCol)] for l in range (2*nbrLines)] #Nouveau tableau ayant le double de la dimension du tableau fournit en paramètre
    for i in range (nbrLines): #Boucle pour parcourir tout les éléments du tableau
        for j in range (nbrCol):
            arrayDouble[2*i][2*j] = array[i][j] #On a un élement qui va devenir quatre élement du tableau double
            arrayDouble[2*i][2*j+1] = array[i][j] #Deuxieme élement en haut à droite
            arrayDouble[2*i+1][2*j] = array[i][j] #Troisieme element en bas à gauche
            arrayDouble[2*i+1][2*j+1] = array[i][j] #Quatrieme element en bas à droite
    return arrayDouble

## Fonction permettant de produire un carré noir c'est à dire que les contours de l'image sont blanc.
def mystere(n):
    array = [[0 for k in range (n)] for l in range (n)] #Nouveau tableau de taille n colonnes et n lignes (renseigner en paramètre)
    q = (n-n%4)/4
    for i in range (n): #Boucle pour parcourir tout les éléments du tableau
        for j in range (n):
            if ((i < q) or (i > n-1-q) or (j < q) or (j > n-1-q)): #Condition
                array[i][j] = 0
            else:
                array[i][j] = 1
    return array

## Test de toutes les fonctions (appel des fonctions)
def testFunctions():
    return (double(negative(mystere(6))))