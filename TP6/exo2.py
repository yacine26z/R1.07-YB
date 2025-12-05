# Exercice 2 - TP6

# Définition de la fonction
def ajouter_elt(lst, elt):
    lst.append(elt)
    return lst

# a) Créer la liste lst1
lst1 = [0, 1, 2]

# b) Créer lst2 en appelant la fonction avec lst1 et sa longueur
lst2 = ajouter_elt(lst1, len(lst1))

# c) Afficher contenu, type et identifiant
print("lst1 :", lst1, "type:", type(lst1), "id:", id(lst1))
print("lst2 :", lst2, "type:", type(lst2), "id:", id(lst2))
