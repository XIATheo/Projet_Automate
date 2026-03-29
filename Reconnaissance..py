def reconnaitre(mot, A):
    # Utilise l'AFDC pour vérifier si le mot est accepté
    trans = {}
    for (dep, sym, arr) in A['transitions']:
        trans[(dep, sym)] = arr

    etat = A['initiaux'][0]
    for c in mot:
        if (etat, c) not in trans:
            print(f"  Mot '{mot}' : NON")
            return
        etat = trans[(etat, c)]

    if etat in A['terminaux']:
        print(f"  Mot '{mot}' : OUI")
    else:
        print(f"  Mot '{mot}' : NON")


def reconnaissance_interactive(A):
    print("\n--- Reconnaissance de mots (tapez 'fin' pour arreter) ---")
    while True:
        mot = input("Mot : ").strip()
        if mot == 'fin':
            break
        reconnaitre(mot, A)