Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> nom = "Toto"
>>> prenom = "Titi"
>>> math = 13.0
>>> anglais = 12.0
>>> info = 12.5
>>> promotion = 2025
>>> 
>>> # Calcul de la moyenne
>>> m = (math + anglais + info) / 3
>>> 
>>> # Affichage des types
>>> print("Type de nom :", type(nom))
Type de nom : <class 'str'>
>>> print("Type de prenom :", type(prenom))
Type de prenom : <class 'str'>
>>> print("Type de math :", type(math))
Type de math : <class 'float'>
>>> print("Type de anglais :", type(anglais))
Type de anglais : <class 'float'>
>>> print("Type de info :", type(info))
Type de info : <class 'float'>
>>> print("Type de promotion :", type(promotion))
Type de promotion : <class 'int'>
>>> print("Type de m :", type(m))
Type de m : <class 'float'>
>>> 
>>> # Affichage formaté de la moyenne
>>> print(f"L’étudiant {nom} {prenom} de la promotion {promotion} a une moyenne de {m:.1f}")
L’étudiant Toto Titi de la promotion 2025 a une moyenne de 12.5
