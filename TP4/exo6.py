# Déclaration de la liste
tab = [5, 2, 4, 8, 1, 3]

print("Phase 0", tab)  # état initial

# Tri par sélection
for i in range(len(tab)):
    # Chercher le plus petit élément dans le reste du tableau
    min_index = i
    for j in range(i + 1, len(tab)):
        if tab[j] < tab[min_index]:
            min_index = j

    # Si on a trouvé un élément plus petit, on permute
    if min_index != i:
        tab[i], tab[min_index] = tab[min_index], tab[i]

    # Affichage de l'état du tableau après chaque phase
    print(f"Phase {i + 1}", tab)
