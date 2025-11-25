# Exercice 2 : Calcul de moyennes

# Demande du nombre d'étudiants
nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))

# Initialisation
notes = []
somme = 0.0

# Saisie des notes avec vérification
for i in range(nombreEtudiants):
    note = float(input(f"Note etudiant {i} : "))
    while note < 0 or note > 20:   # contrôle de validité
        print("Erreur : la note doit être comprise entre 0 et 20.")
        note = float(input(f"Note etudiant {i} : "))
    notes.append(note)
    somme += note

# Calcul de la moyenne
moyenne = somme / nombreEtudiants

# Affichage de la moyenne
print(f"Moyenne de classe : {moyenne}")

# Affichage des écarts à la moyenne
print("Numéro de l’Etudiant | note | ecart a la moyenne")
for i in range(nombreEtudiants):
    ecart = round(notes[i] - moyenne, 2)
    print(f"{i} | {notes[i]} | {ecart}")
