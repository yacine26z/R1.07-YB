# Fondue.py

# Déclaration de la constante BASE
BASE = 4

# Quantités de base pour 4 personnes
fromage = 800.0  # en grammes
eau = 2          # en décilitres
ail = 2          # en gousses
pain = 400       # en grammes

# Demande du nombre de convives
nbConvives = int(input("Entrez le nombre de personne(s) conviées à la fondue : "))

# Calcul des quantités adaptées
fromage = fromage * nbConvives / BASE
eau = eau * nbConvives / BASE
ail = ail * nbConvives / BASE
pain = pain * nbConvives / BASE

# Affichage de la recette
print(f"Pour faire une fondue fribourgeoise pour {nbConvives} personnes, il vous faut :")
print(f"- {fromage} gr de fromage")
print(f"- {eau} dl d'eau")
print(f"- {ail} gousse(s) d'ail")
print(f"- {pain} gr de pain")
