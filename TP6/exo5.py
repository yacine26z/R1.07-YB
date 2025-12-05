import unicodedata
# Fonction pour supprimer les caractères spéciaux, espaces et ponctuations
def nettoyer_texte(texte):
    resultat = ""
    for c in texte:
        if c.isalpha():  # garder uniquement les lettres
            resultat += c
    return resultat

# Fonction pour supprimer les accents
def supprimer_accents(texte):
    # Normalisation Unicode : décompose les caractères accentués
    nfkd = unicodedata.normalize('NFD', texte)
    # On garde uniquement les caractères de base (catégorie != 'Mn')
    return "".join([c for c in nfkd if unicodedata.category(c) != 'Mn'])

# Fonction pour vérifier si c'est un palindrome
def est_palindrome(texte):
    # Mise en minuscule
    texte = texte.lower()
    # Suppression des accents
    texte = supprimer_accents(texte)
    # Nettoyage des caractères non alphabétiques
    texte = nettoyer_texte(texte)
    # Vérification palindrome
    return texte == texte[::-1]

# Programme principal
chaine = input("Entrez un mot ou une phrase : ")

if est_palindrome(chaine):
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome.")
