# Exercice 1 : Table de multiplication

# Demande du nombre à l'utilisateur
nombre = float(input("Vous cherchez la table de multiplication de quel nombre ? "))

# Création de la liste pour stocker les résultats
table = []

# Remplissage de la liste avec les résultats de 0 à 9
for i in range(10):
    resultat = round(nombre * i, 2)   # arrondi à 2 décimales
    table.append(resultat)

# Affichage des résultats
for i in range(10):
    print(f"{nombre} * {i} = {table[i]}")
