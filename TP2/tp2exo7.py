import random

# Génération d’un nombre entre 1 et 3
tirage = random.randint(1, 3)

# Test de la condition
if tirage <= 2:
    print("Pile !")
else:
    print("Face !")
