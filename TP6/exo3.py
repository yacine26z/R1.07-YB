# Fonction avec valeurs par défaut
def ajouter_elt(lst=[0, 1, 2], elt=3):
    lst.append(elt)
    return lst

# a) Premier appel
print("Premier appel :", ajouter_elt())

# b) Second appel
print("Second appel :", ajouter_elt())
print("ID de lst par défaut :", id(ajouter_elt.__defaults__[0]))  # montre que c'est le même objet

# c) Fonction avec chaîne
def ajouter_carac(ch="abc", elt="d"):
    return ch + elt

# d) Premier appel
print("Premier appel ajouter_carac :", ajouter_carac())

# e) Second appel
print("Second appel ajouter_carac :", ajouter_carac())
print("ID de ch par défaut :", id(ajouter_carac.__defaults__[0]))
