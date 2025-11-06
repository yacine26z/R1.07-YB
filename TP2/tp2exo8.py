# Demande à l'utilisateur d'entrer un réel
x = float(input("Entrez un nombre décimal : "))

# Test d'appartenance à l'ensemble I
appartient_I = ((x == 2 or (x > 2 and x < 3)) or
                (x > 0 and (x == 1 or x < 1)) or
                ((x == -10 or x > -10) and x < -2))

# Affichage du résultat
if appartient_I:
    print("x appartient à I")
else:
    print("x n'appartient pas à I")
