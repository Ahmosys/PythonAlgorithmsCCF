## Fonction recevant un tableau de 4x4 et renvoyant un tableau de 8x8 avec les valeurs du tableau 4x4 placé dans le tableau  8x8.
def rempliss(array4):
    array8 = [[0 for k in range (8)] for j in range (8)] #Créer un tableau de 8 colonnes et 8 lignes
    for i in range (0,4): #Pour i allant de 0 à 4 (lignes)
        for j in range (0,4):#Pour j allant de 0 à 4 (colonnes)
            array8[i][j] = array4[i][j] #Tableau de 8 (array8) prend les valeurs  à la meme position que tableau de 4 (array4)
    return array8

## Fonction permettant d'éffectuer la symtétrie verticale vers la droite de la moitié du tableau. (voir sujet)
def sym1(array8):
    for i in range (4): #Pour i allant de 0 à 3 (lignes)
        for j in range (4): #Pour j allant de 0 à 3 (colonnes)
            array8[i][7-j] = array8[i][j] #La position array8[i][7-j] va prendre la valeur de array8[i][j]
    return array8

## Fonction permettant d'éffectuer la symtétrie horizontale. (voir sujet)
def sym2(array8):
    for i in range (4): #Pour i allant de 0 à 3 (lignes)
        for j in range (8): #Pour j allant de 0 à 7 (colonnes)
            array8[7-i][j] = array8[i][j] #La position array8[7-i][j] va prendre la valeur de array8[i][j]
    return array8

## Fonction apellant toutes les autres fonctions éffectuées avant.
def construitIcone(array4):
    return sym2(sym1(rempliss(array4)))
