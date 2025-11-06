import random

# Génération d’un nombre aléatoire entre 0 et 100
nombre = random.randint(0, 100)

# Test de la condition
if nombre < 50:
    print("Pile !")
else:
    print("Face !")
