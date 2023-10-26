#Grille de Sudoku
S=[[0,1,0,0,7,8,0,0,0],
[0,8,0,0,4,0,9,0,0],
[0,0,5,6,0,0,0,1,0],
[1,0,0,0,6,0,0,0,5],
[0,4,0,9,1,5,0,7,2],
[0,6,7,0,8,0,4,0,0],
[0,0,0,3,0,0,1,0,0],
[0,7,0,8,9,0,0,2,3],
[0,0,0,0,0,4,0,0,0]
]


def enlever0(liste):
    while 0 in liste:
        liste.remove(0)
    return liste

def ligne(S,i):
    liste = S[i]
    return enlever0(liste)

def colonne(S,j):
    colonne =[]
    for i in range(len(S)):
        colonne.append(S[i][j])
    colonne0=enlever0(colonne)
    return colonne0


def bloc(S,i,j):
    bloc1=[]
    for ligne1 in range(3):
        for colonne1 in range(3):
            bloc1.append(S[ligne1][colonne1])

    bloc2=[]
    for ligne2 in range(3):
        for colonne2 in range(3,6):
            bloc2.append(S[ligne2][colonne2])

    bloc3=[]
    for ligne3 in range(3):
        for colonne3 in range(6,9):
            bloc3.append(S[ligne3][colonne3])

    #Bloc 2
    bloc4=[]
    for ligne4 in range(3,6):
        for colonne4 in range(3):
            bloc4.append(S[ligne4][colonne4])

    bloc5=[]
    for ligne5 in range(3,6):
        for colonne5 in range(3,6):
            bloc5.append(S[ligne5][colonne5])

    bloc6=[]
    for ligne6 in range(3,6):
        for colonne6 in range(6,9):
            bloc6.append(S[ligne6][colonne6])

    #Bloc3
    bloc7=[]
    for ligne7 in range(6,9):
        for colonne7 in range(3):
            bloc7.append(S[ligne7][colonne7])

    bloc8=[]
    for ligne8 in range(6,9):
        for colonne8 in range(3,6):
            bloc8.append(S[ligne8][colonne8])

    bloc9=[]
    for ligne9 in range(6,9):
        for colonne9 in range(6,9):
            bloc9.append(S[ligne9][colonne9])

    #Ligne 1 colonne de 1,2,3
    if 0 <= i <=2 and 0 <= j <=2:
        return enlever0(bloc1)

    if 0 <= i <=2 and 3<= j <=5:
        return enlever0(bloc2)

    if 0 <= i <=2 and 6 <= j <=8:
        return enlever0(bloc3)

    #ligne 2 colonne 1,2,3
    if 3 <= i <=5 and 0 <= j <=2:
        return enlever0(bloc4)

    if 3 <= i <=5 and 3 <= j <=5:
        return enlever0(bloc5)

    if 3 <= i <=5 and 6 <= j <=8:
        return enlever0(bloc6)

    #ligne 3 colonne 1,2,3
    if  6<= i <=8 and 0 <= j <=2:
        return enlever0(bloc7)

    if 6 <= i <=8 and 3 <= j <=5:
        return enlever0(bloc8)

    if 6 <= i <=8 and 6 <= j <=8:
        return enlever0(bloc9)


def possibles(S,i,j):
    bloc_par=bloc(S,i,j)
    ligne_par=ligne(S,i)
    colonne_par=colonne(S,j)

    condition=bloc_par+ligne_par+colonne_par

    nbr=[1,2,3,4,5,6,7,8,9]
    nbr_poss=[]

    for i in nbr:
        if i not in condition :
            nbr_poss.append(i)
    return nbr_poss


def suivante(i, j):
    if j == 8:
        ligne = i + 1
        colonne = 0
    else:
        ligne = i
        colonne = j + 1
    return (ligne, colonne)


def solve(S,i,j) :
    if i==9 :
        return ... #False ???

    elif S[i][j]>0:
        ...
        return ... #solve(S,a,b) ???

    for k in possibles(S,i,j):
        S[i][j] = k
        ... #a,b=suivante(i,j) ???
             #S=k ???
        if solve(S,a,b) :
            return .... #k ???

    S[i][j] = 0
    return False

solve(S,1,1)

