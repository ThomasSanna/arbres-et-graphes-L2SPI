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

def lireGraphe(mat):
  sommets = [f'S{i}' for i in range(len(mat))]
  listeAdjacence = {sommet : [] for sommet in sommets}
  for i in range(len(mat)):
    for j in range(len(mat)):
      if mat[i][j] == 1:
        listeAdjacence[sommets[i]].append(sommets[j])
  return sommets, listeAdjacence
        
sommets, listeAdjacence = lireGraphe(matrice)
print(sommets)
print(listeAdjacence)

# 2 ----------------------------------
print("\nQuestion 2")

def oterArcs(mat, s):
  sommets, graphes = lireGraphe(mat)
  for sommet in sommets:
    if s in graphes[sommet]:
      graphes[sommet].remove(s)
  return graphes

print(oterArcs(matrice, 'S0'))

# 3 ----------------------------------
print("\nQuestion 3")

def ajouterArcs(mat, s, arcs):
  sommets, graphes = lireGraphe(mat)
  for arc in arcs:
    if arc not in graphes[s]:
      graphes[s].append(arc)
  return graphes

print(ajouterArcs(matrice, 'S0', ['S1', 'S3']))

# Partie 2
print('\n----------- Partie 2 ----------------------------')

def successeurs(mat, S, LF):
  _, graphes = lireGraphe(mat)
  return [succ for succ in graphes[S] if succ not in LF]

print(successeurs(matrice, 'S0', ['S1']))

def predecesseursGraphe(mat):
  sommets, _ = lireGraphe(mat)
  graphe = {f"S{i}" : [] for i in range(len(mat))}
  for i in range(len(mat)):
    for j in range(len(mat)):
      if mat[i][j] == 1:
        graphe[sommets[j]].append(sommets[i])
  return graphe
        
print(predecesseursGraphe(matrice))

def predecesseurs(mat, S):
  return predecesseursGraphe(mat)[S]

print(predecesseurs(matrice, "S1"))
  

def parcoursEnLargeurAvecDistance(mat, S):
  Ls = [(S, 0)]
  i=0
  while i < len(Ls):
    s, d = Ls[i]
    Ls += [(successeur, d+1) for successeur in successeurs(mat, s, [elt[0] for elt in Ls])]
    i+=1
  return Ls

print(parcoursEnLargeurAvecDistance(matrice, "S0"))

# 1 ----------------------------------
print("\nQuestion 1")

# Renvoie la liste de sommets d'un chemin de D à A
def chemin(mat, d, a):
  Ls = [(d, [d])]
  i=0
  while i < len(Ls):
    s, c = Ls[i]
    
    if s == a:
      return c
    
    dejaFait = [elt[0] for elt in Ls]
    
    for successeur in successeurs(mat, s, dejaFait):
      # [1, 2, 3] +  [4, 5] = [1, 2, 3, 4, 5]
      Ls += [(successeur, c + [successeur])]
      
    i += 1
  return []

print(chemin(matrice, 'S3', 'S2'))


# Partie 3
print('\n----------- Partie 3 ----------------------------')

# 1 ----------------------------------
print("Question 1")

def cheminB(mat, d, a, ban):
  Ls = [(d, [d])]
  i=0
  while i < len(Ls):
    s, c = Ls[i]
    
    if s == a:
      return c
    
    dejaFait = [elt[0] for elt in Ls]
    
    for successeur in successeurs(mat, s, dejaFait + ban):
      Ls += [(successeur, c + [successeur])]
    
    i+=1
  return []

print(cheminB(matrice, 'S3', 'S2', ['S1'])) # ne renvoie rien car on ne peut pas aller de S3 à S2 sans passer par S1
print(cheminB(matrice, 'S3', 'S2', ['S0']))

# 2 ----------------------------------
print("\nQuestion 2")

def itineraire(mat, d, a, i):
  chm1 = chemin(mat, d, i)
  chm2 = chemin(mat, i, a)
  
  if chm2 != [] and chm1 != []:
    chm = chm1 + chm2[1:]
    return chm
  return f'Aucun chemin trouvé de {d} à {a} en passant par {i}'

print(itineraire(matrice, 'S0', 'S3', 'S2'))

# 3 ----------------------------------
print("\nQuestion 3")

matrice2 = [
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0] 
]

print(itineraire(matrice2, 'S0', 'S1', 'S9'))