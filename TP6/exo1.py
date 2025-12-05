# a) Initialiser une liste avec trois zéros
L1 = [0] * 3
print("Liste L1 :", L1)
print("Type de L1 :", type(L1))
print("Id de L1 :", id(L1))

# b) Afficher valeur, type et id de chaque élément
for i, elt in enumerate(L1):
    print(f"Élément {i} -> valeur: {elt}, type: {type(elt)}, id: {id(elt)}")

# c) Modifier le deuxième élément
L1[1] += 1
print("\nAprès modification de L1[1] :")
print("Liste L1 :", L1)
print("Type de L1 :", type(L1))
print("Id de L1 :", id(L1))

# d) Vérifier les identifiants des éléments
for i, elt in enumerate(L1):
    print(f"Élément {i} -> valeur: {elt}, type: {type(elt)}, id: {id(elt)}")

# e) Test avec une chaîne
s = "machaine"
print("\nChaîne :", s)
print("Id de la chaîne :", id(s))
for i, c in enumerate(s):
    print(f"Caractère {i} -> valeur: {c}, type: {type(c)}, id: {id(c)}")
