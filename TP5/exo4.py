# Monnaie.py

# Lecture de la somme
somme = int(input("Entrez une somme en euros : "))

# Décomposition en billets et pièces
billets_100 = somme // 100
reste = somme % 100

billets_50 = reste // 50
reste = reste % 50

billets_10 = reste // 10
reste = reste % 10

pieces_2 = reste // 2
reste = reste % 2

pieces_1 = reste

# Affichage du résultat
print(f"{somme} euros, c’est donc {billets_100} billets de 100, "
      f"{billets_50} de 50, {billets_10} de 10, "
      f"{pieces_2} pièces de 2 et {pieces_1} pièce(s) de 1.")
