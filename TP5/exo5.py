# FicheDePaye.py

# Lecture des données
heures = int(input("Entrez le nombre d'heures travaillées : "))
salaire_horaire = float(input("Entrez le salaire horaire (€) : "))

# Calcul du salaire
salaire = 0

# 1. Les 160 premières heures au taux normal
if heures <= 160:
    salaire = heures * salaire_horaire
else:
    salaire = 160 * salaire_horaire

    # 2. Les heures entre 161 et 200 majorées de 25%
    if heures <= 200:
        salaire += (heures - 160) * (salaire_horaire * 1.25)
    else:
        salaire += 40 * (salaire_horaire * 1.25)

        # 3. Les heures au-delà de 200 majorées de 50%
        salaire += (heures - 200) * (salaire_horaire * 1.5)

# Affichage du résultat
print(f"Le salaire total est de : {salaire:.2f} €")
