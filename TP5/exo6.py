# ChainesCourtes.py

T = input("Entrez une chaîne : ")
mot = "wagon"

# 1. Taille
taille = 0
for _ in T: taille += 1
print("Taille :", taille)

# 2. Pourcentage de voyelles
voyelles = "aeiouyAEIOUY"
nb_voyelles = sum(1 for c in T if c in voyelles)
print("Pourcentage de voyelles :", nb_voyelles*100/taille if taille else 0, "%")

# 3. Première occurrence de "wagon"
pos = -1
for i in range(taille - len(mot) + 1):
    if T[i:i+len(mot)].lower() == mot:
        pos = i
        break
print("Première occurrence :", pos if pos != -1 else "absente")

# 4. Nombre d’occurrences
nb_occ = 0
for i in range(taille - len(mot) + 1):
    if T[i:i+len(mot)].lower() == mot:
        nb_occ += 1
print("Nombre d'occurrences :", nb_occ)
