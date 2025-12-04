def est_bissextile(annee):
    """Retourne True si l'année est bissextile, False sinon."""
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)

def verification_date(date_str):
    # Vérification du format
    if len(date_str) != 8 or not date_str.isdigit():
        print("❌ Format incorrect : la date doit contenir 8 chiffres (jjmmaaaa).")
        return

    # Extraction des parties
    jour = int(date_str[0:2])
    mois = int(date_str[2:4])
    annee = int(date_str[4:8])

    # Vérification du mois
    if mois < 1 or mois > 12:
        print(f"❌ Date invalide : le mois {mois} n'existe pas.")
        return

    # Nombre de jours par mois
    jours_par_mois = {
        1: 31, 2: 29 if est_bissextile(annee) else 28,
        3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31,
        11: 30, 12: 31
    }

    # Vérification du jour
    if jour < 1 or jour > jours_par_mois[mois]:
        print(f" Date invalide : le jour {jour} n'existe pas en {mois}/{annee}.")
        return

    # Si tout est correct
    print(f" Date valide : {jour:02d}/{mois:02d}/{annee}")

# -------------------------------
# Tests demandés
dates_test = ["3102199", "31041000", "32052020", "30032021", "29022022"]

for d in dates_test:
    print(f"Test avec {d} :")
    verification_date(d)
    print("-" * 40)
