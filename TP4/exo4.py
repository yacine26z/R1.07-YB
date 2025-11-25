# Exercice 4 : Elément le plus fréquent dans une liste

# Exemple de liste
L = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7]

# Initialisation
element_frequent = L[0]
frequence_max = L.count(L[0])

# Parcours de la liste
for x in L:
    freq = L.count(x)
    if freq > frequence_max:
        frequence_max = freq
        element_frequent = x

# Affichage du résultat
print(f"Le nombre le plus frequent dans la liste est le : {element_frequent} ({frequence_max} x)")
