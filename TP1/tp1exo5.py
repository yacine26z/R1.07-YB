Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # Saisie interactive des variables
>>> jour = int(input("Entrez le jour du mois (ex: 1 à 31) : "))
Entrez le jour du mois (ex: 1 à 31) : 
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    jour = int(input("Entrez le jour du mois (ex: 1 à 31) : "))
ValueError: invalid literal for int() with base 10: ''
>>> jour = int(input("Entrez le jour du mois (ex: 1 à 31) : "))
Entrez le jour du mois (ex: 1 à 31) : 15
>>> heure = int(input("Entrez l'heure (entre 0 et 23) : "))
Entrez l'heure (entre 0 et 23) : 15
>>> minute = int(input("Entrez les minutes (entre 0 et 59) : "))
Entrez les minutes (entre 0 et 59) : 15
>>> 
>>> 
... # Calcul du nombre de minutes écoulées depuis le début du mois
>>> 
>>> minutes_ecoulees = ((jour - 1) * 24 * 60) + (heure * 60) + minute
>>> 
>>> # Affichage du résultat
>>> 
>>> print(f"Depuis le début du mois, {minutes_ecoulees} minutes se sont écoulées.")
Depuis le début du mois, 21075 minutes se sont écoulées.
