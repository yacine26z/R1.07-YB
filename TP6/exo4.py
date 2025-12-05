import random

# a) Fonction generer() : génère une liste de nbr entiers entre vmin et vmax
def generer(nbr, vmin, vmax):
    table = []
    for _ in range(nbr):
        table.append(random.randint(vmin, vmax))
    return table

# a) Fonction combienInferieur() : compte combien de valeurs sont < vseuil
def combienInferieur(table, vseuil):
    compteur = 0
    for val in table:
        if val < vseuil:
            compteur += 1
    return compteur

# b) Programme interactif
# Demande du nombre de valeurs
nb = int(input("Combien de valeurs voulez-vous générer ? "))

# Demande de l'intervalle
vmin = int(input("Valeur minimale : "))
vmax = int(input("Valeur maximale : "))

# Demande du seuil
choix = input("Vous voulez préciser le seuil ? (Oui/O ou Non/N) : ")
if choix.lower() in ["oui", "o"]:
    vseuil = int(input("Entrez le seuil : "))
else:
    vseuil = 30  # valeur par défaut

# Génération et traitement
print(f"\nGénérer {nb} nombres entiers entre {vmin} et {vmax}")
tab = generer(nb, vmin, vmax)
tab.sort()
print("Tableau généré trié :", tab)

total = combienInferieur(tab, vseuil)
print(f"Il y en a {total} inférieurs à {vseuil}")
