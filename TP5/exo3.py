# Palindrome.py

# 1. Lecture de la chaîne de caractères
chaine = input("Entrez un mot ou une phrase : ")

# 2. Mise en minuscule et suppression des caractères non alphabétiques
chaine = chaine.lower()  # conversion en minuscules
epuree = ""              # chaîne épurée

for c in chaine:
    if c.isalpha():      # on garde uniquement les lettres
        epuree += c

# 3. Test si la chaîne épurée est un palindrome
# Un palindrome est identique à sa version inversée
if epuree == epuree[::-1]:
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome.")
