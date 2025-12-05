# Notes.py

# Initialisation des listes pour stocker les notes et les coefficients
notes = []
coefficients = []

# Demande des 5 notes et coefficients
for i in range(1, 6):
    saisie = input(f"Veuillez entrer la note du module {i} et le coefficient correspondant (ex: 10.5 2) : ")
    valeurs = saisie.split(" ")  # Séparation de la chaîne en deux parties
    note = float(valeurs[0])     # Conversion en réel
    coeff = int(valeurs[1])      # Conversion en entier
    notes.append(note)
    coefficients.append(coeff)

# Calcul de la moyenne pondérée
somme_notes = 0
somme_coeffs = 0
for i in range(5):
    somme_notes += notes[i] * coefficients[i]
    somme_coeffs += coefficients[i]

moyenne = somme_notes / somme_coeffs

# Vérification des conditions d'admission
admis = moyenne > 10 and all(note >= 8 for note in notes)

# Affichage des résultats
print(f"\nLa moyenne générale est : {moyenne:.2f}")
if admis:
    print("L'étudiant est admis ")
else:
    print("L'étudiant n'est pas admis ")
