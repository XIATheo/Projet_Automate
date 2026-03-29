from lecture import lire_automate
from affichage import afficher
from tests import afficher_tests

print("=== Traitement d'automates finis ===")

while True:
    choix = input("\nNumero d'automate (ou 'fin') : ").strip()
    if choix.lower() == 'fin':
        break

    try:
        A = lire_automate(choix)
        afficher(A)
        afficher_tests(A)
    except FileNotFoundError:
        print("Fichier introuvable.")
    except Exception as e:
        print(f"Erreur : {e}")