from lecture import lire_automate
from affichage import afficher
from tests import afficher_tests
from standardisation import standardiser
from determinisation import determiniser
from minimisation import minimiser
from reconnaissance import reconnaissance_interactive
from complementaire import complementaire

print("=== Traitement d'automates finis ===")

while True:
    choix = input("\nNumero d'automate (ou 'fin') : ").strip()
    if choix.lower() == 'fin':
        break

    try:
        A = lire_automate(choix)
        afficher(A)
        det, std, cpl = afficher_tests(A)

        # Standardisation
        if not std:
            rep = input("Voulez-vous standardiser ? (o/n) : ").strip().lower()
            if rep == 'o':
                A = standardiser(A)
                print("\n--- Automate standardise ---")
                afficher(A)

        # Déterminisation + complétion
        if det and cpl:
            AFDC = A
            print("L'automate est deja deterministe et complet.")
        else:
            AFDC = determiniser(A)
            print("\n--- Automate deterministe complet ---")
            afficher(AFDC)

        # Minimisation
        AFDCM = minimiser(AFDC)
        print("--- Automate minimal ---")
        afficher(AFDCM)

        # Reconnaissance de mots
        reconnaissance_interactive(AFDC)

        # Complémentaire
        AComp = complementaire(AFDC)
        print("\n--- Automate complementaire (base sur AFDC) ---")
        afficher(AComp)

    except FileNotFoundError:
        print("Fichier introuvable.")
    except Exception as e:
        print(f"Erreur : {e}")
