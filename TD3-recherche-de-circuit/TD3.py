import numpy as np
import copy

def successeurs(mat, S, LF):
  _, graphes = lireGraphe(mat)
  return [succ for succ in graphes[S] if succ not in LF]

def predecesseursGraphe(mat):
  sommets, _ = lireGraphe(mat)
  graphe = {f"S{i}" : [] for i in range(len(mat))}
  for i in range(len(mat)):
    for j in range(len(mat)):
      if mat[i][j] == 1:
        graphe[sommets[j]].append(sommets[i])
  return graphe
        
def predecesseurs(mat, S, LF):
  return [pred for pred in predecesseursGraphe(mat)[S] if pred not in LF]


# Partie 1
print('\n----------- Partie 1 ----------------------------')

# 1 ----------------------------------
print("Question 1")

matrice = [
    [0, 1, 1, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 0],
    [0, 1, 0, 0]
]

matrice2 = [
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0] 
]

def lireGraphe(mat):
  sommets = [f'S{i}' for i in range(len(mat))]
  listeAdjacence = {sommet : [] for sommet in sommets}
  for i in range(len(mat)):
    for j in range(len(mat)):
      if mat[i][j] == 1:
        listeAdjacence[sommets[i]].append(sommets[j])
  return sommets, listeAdjacence

def lireGrapheB(mat, LF):
  sommets = [f'S{i}' for i in range(len(mat)) if f'S{i}' not in LF]
  listeAdjacence = {sommet : [] for sommet in sommets}
  for i in range(len(sommets)):
    for j in range(len(sommets)):
      if not (f'S{i}' in LF or f'S{j}' in LF):
        if mat[i][j] == 1:
          listeAdjacence[sommets[i]].append(sommets[j])
  return sommets, listeAdjacence
        
sommets, listeAdjacence = lireGraphe(matrice)
print("Sommets : ", sommets)
print("Liste d'adjacence : ",  listeAdjacence)

# 2 ----------------------------------
print("\nQuestion 2")

def source(mat, s, LF):
  return len(predecesseurs(mat, s, LF)) == 0

print("S3 est une source ? : ", source(matrice, 'S3', []))

def puit(mat, s, LF):
  return len(successeurs(mat, s, LF)) == 0

print("S3 est une puit ? : ", puit(matrice, 'S3', []))

# 3 ----------------------------------
print("\nQuestion 3")

def sourcesEtPuis(mat, LF):
  sommets, _ = lireGrapheB(mat, LF)
  sources = [s for s in sommets if source(mat, s, LF)]
  puits = [s for s in sommets if puit(mat, s, LF)]
  return sources, puits
  
print('Matrice 1 : ', sourcesEtPuis(matrice, ["S1"]))
print('Matrice 2 : ', sourcesEtPuis(matrice2, ['S1']))


# Partie 2
print('\n----------- Partie 2 ----------------------------')

# 1 ----------------------------------
print("Question 1")

def delSourcesEtPuit(mat, LSP):
  matDel = copy.deepcopy(mat)
  long = len(matDel)
  for sommet in LSP:
    numSommet = int(sommet[1:]) # "S3" -> 3
    for i in range(long):
      matDel[i][numSommet] = 0 # par ligne
      matDel[numSommet][i] = 0 # par colonne
  return matDel, mat == matDel

mat, res = delSourcesEtPuit(matrice2, ["S2"])
print("Matrice en enlevant S2 : \n", np.matrix(mat))

# 2 ----------------------------------
print("\nQuestion 2")

matriceSansCircuit = [
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0] 
]

matriceAvecCircuit = [
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0] 
]

print("Tests question 3")

# 3 ----------------------------------
print("\nQuestion 3")

def marimont(mat):
  matTemp = copy.deepcopy(mat)
  LF = []
  res = False
  while not res:
    sources, puits = sourcesEtPuis(matTemp, [])
    LF += sources + puits
    matTemp, res = delSourcesEtPuit(matTemp, LF)
  return matTemp


def possedeCircuit(mat):
  matVide = all(mat[x][y]==0 for x in range(len(mat)) for y in range(len(mat)))
  sommets, listeAdj = lireGraphe(mat)
  return not matVide, sommets, listeAdj

#--------Tests Marimon Sans Circuit--------
print("Matrice sans circuit :")

matSans = marimont(matriceSansCircuit)

print("Matrice sans circuit après passage de marimont : \n", np.matrix(matSans))

resultat, sommets, listeAdjacence = possedeCircuit(matSans)

print("La matrice possède un circuit ? : ", resultat, "(False : la matrice n'a que des 0)")
print("Sommets : ", sommets)
print("L.A. : ", listeAdjacence)

#--------Tests Marimon Avec Circuit--------
print("\n Matrice avec circuit :")

matAvec = marimont(matriceAvecCircuit)

print("Matrice avec circuit après passage de marimont : \n", np.matrix(matAvec))

resultat, sommets, listeAdjacence = possedeCircuit(matAvec)

print("La matrice possède un circuit ? : ", resultat, "(False : la matrice n'a que des 0)")
print("Sommets : ", sommets)
print("L.A. : ", listeAdjacence)


# 4 ----------------------------------
print("\nQuestion 4")
