def epsilon_fermeture(etats, transitions):
    fermeture = set(etats)
    pile = list(etats)
    while pile:
        e = pile.pop()
        for (dep, sym, arr) in transitions:
            if dep == e and sym == 'E':
                if arr not in fermeture:
                    fermeture.add(arr)
                    pile.append(arr)
    return fermeture


def determiniser(A):
    alphabet = A['alphabet']
    # L'état initial est la fermeture epsilon des initiaux
    depart = tuple(sorted(epsilon_fermeture(A['initiaux'], A['transitions'])))

    a_traiter = [depart]
    vus = {depart: 0}
    compteur = 1
    transitions_new = []
    besoin_poubelle = False

    while a_traiter:
        courant = a_traiter.pop(0)
        idx_courant = vus[courant]

        for sym in alphabet:
            # 1. Trouver les destinations directes par la lettre
            dest_directe = set()
            for e in courant:
                for (dep, s, arr) in A['transitions']:
                    if dep == e and s == sym:
                        dest_directe.add(arr)

            # 2. Appliquer la fermeture epsilon sur ces destinations
            if not dest_directe:
                besoin_poubelle = True
                transitions_new.append((idx_courant, sym, -1))
            else:
                fermeture = tuple(sorted(epsilon_fermeture(dest_directe, A['transitions'])))
                if fermeture not in vus:
                    vus[fermeture] = compteur
                    compteur += 1
                    a_traiter.append(fermeture)
                transitions_new.append((idx_courant, sym, vus[fermeture]))

    # Finalisation (poubelle et terminaux)
    etats_new = list(range(compteur + (1 if besoin_poubelle else 0)))
    if besoin_poubelle:
        p_idx = compteur
        transitions_new = [(d, s, p_idx if a == -1 else a) for (d, s, a) in transitions_new]
        for s in alphabet: transitions_new.append((p_idx, s, p_idx))

    terminaux_new = [idx for states, idx in vus.items() if any(e in A['terminaux'] for e in states)]

    return {'alphabet': alphabet, 'etats': etats_new, 'initiaux': [0], 'terminaux': terminaux_new,
            'transitions': transitions_new}
