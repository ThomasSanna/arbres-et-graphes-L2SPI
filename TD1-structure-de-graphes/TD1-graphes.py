# Partie 1
print('\n----------- Partie 1 ----------------------------')

# 1 ----------------------------------
print("Question 1")

def lireGraphe(mat):
    sommets = [f"S{i}" for i in range(len(mat))]
    graphe = {sommet: [] for sommet in sommets}

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == 1:
                graphe[sommets[i]].append(sommets[j])

    return sommets, graphe

matrice = [
    [0, 1, 1, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 0],
    [0, 1, 0, 0]
]

sommets, graphe = lireGraphe(matrice)

print("Liste des sommets:", sommets)
print("Graphe:", graphe)


# 2 ----------------------------------
print("\nQuestion 2")

# Obtenir le nom d'un sommet n°0 :
print("Nom :", sommets[0])

# Obtenir le numéro (l'index) d'un sommet nommé S0 :
print("Numéro :", sommets.index('S0'))


# 3 ----------------------------------
print("\nQuestion 3")

def successeurs(mat, S):
    _, graphe = lireGraphe(mat)
    return graphe[S]

print(successeurs(matrice, 'S0'))


# 4 ----------------------------------
print("\nQuestion 4")

def successeurs(mat, S, LF):
    _, graphe = lireGraphe(mat)
    return [succ for succ in graphe[S] if succ not in LF]

print(successeurs(matrice, 'S0', ['S1']))



# Partie 2
print('\n----------- Partie 2 ----------------------------')

# 1 ----------------------------------
print("Question 1")

"""
    [0, 1, 1, 0]
    [1, 0, 1, 0]
    [0, 1, 0, 0]
    [0, 1, 0, 0]
"""


def parcoursEnLargeurAvecDistance(mat, S):
    LF = [(S, 0)]  # liste de tuples (sommet, distance)
    i = 0  
    while i < len(LF): 
        s, d = LF[i] 
        succ = [(successeur, d + 1) for successeur in successeurs(mat, s, [elt[0] for elt in LF])] 
        LF += succ
        i += 1
    return LF

print(parcoursEnLargeurAvecDistance(matrice, 'S3'))


def distance(mat, Sd, Sa):
    parcLargListe = parcoursEnLargeurAvecDistance(mat, Sd)
    distances = dict(parcLargListe)
    if Sa in distances:
        return distances[Sa]
    else:
        return -1

print("La distance entre S3 et S0 est de", distance(matrice, "S3", "S0"))


# 2 ----------------------------------
print("\nQuestion 2")

def ecartement(mat, S):
    parcLargListe = parcoursEnLargeurAvecDistance(mat, S) # [(S0, 0), (S1, 1)]
    distances = dict(parcLargListe) # {'S0': 0, 'S1': 1}
    return max(distances.values())

print("L'écartement de S3 est de", ecartement(matrice, "S3"))


# 3-4 ----------------------------------
print("\nQuestion 3/4")

def centre(mat):
    sommets, _ = lireGraphe(mat)
    allEcart = [(sommet, ecartement(mat, sommet)) for sommet in sommets]
    rayon = min(elt[1] for elt in allEcart)
    centr = list(elt[0] for elt in allEcart if elt[1] == rayon)
    return centr, rayon

centr, rayon = centre(matrice)

print("Le/s centre/s du graphe est/sont", centr, "de rayon", rayon)


# 5 ----------------------------------
print("\nQuestion 5")

def diametre(mat):
    sommets, _ = lireGraphe(mat)
    allEcart = [(sommet, ecartement(mat, sommet))for sommet in sommets]
    maxEcart = max(elt[1] for elt in allEcart)
    return maxEcart

maxEcart = diametre(matrice)

print("Le diametre/s du graphe est de", maxEcart)


# 6 ----------------------------------
print("\nQuestion 6")

def poids(mat, S):
    parcLarg = parcoursEnLargeurAvecDistance(mat, S)
    return sum(elt[1] for elt in parcLarg)

print("Le poids de S3 est de", poids(matrice, "S3"))


# 7 ----------------------------------
print("\nQuestion 7")

def plusPetitGrandPoids(mat):
    sommets, _ = lireGraphe(mat)
    somPoids = {sommet:poids(mat, sommet) for sommet in sommets}
    
    minPoids, maxPoids = min(poids(mat, s) for s in sommets), max(poids(mat, s) for s in sommets)
    
    plusPetitPoid = [som for som in somPoids if somPoids[som] == minPoids]
    plusGrandPoid = [som for som in somPoids if somPoids[som] == maxPoids]
    
    return plusPetitPoid, plusGrandPoid

plusPetit, plusGrand = plusPetitGrandPoids(matrice)

print("Plus petit/s poids :", plusPetit, "Plus grand/s poids :", plusGrand)