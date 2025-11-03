Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # Saisie du nombre de minutes écoulées
... minutes = int(input("Entrez le nombre de minutes écoulées depuis le début du mois : "))
Entrez le nombre de minutes écoulées depuis le début du mois : 4321
>>> 
>>> # Calcul du jour du mois
... jour = (minutes // (24 * 60)) + 1
>>> 
>>> # Affichage du jour correspondant
... print(f"La date correspond au jour {jour} du mois.")
La date correspond au jour 4 du mois.
>>> 
