def determiniser(A):
    alphabet = A['alphabet']
    initial = tuple(sorted(A['initiaux']))

    a_traiter = [initial]
    vus = {initial: 0}
    compteur = 1
    transitions_new = []
    besoin_poubelle = False

    while a_traiter:
        courant = a_traiter.pop(0)
        idx_courant = vus[courant]

        for sym in alphabet:
            dest = set()
            for e in courant:
                for (dep, s, arr) in A['transitions']:
                    if dep == e and s == sym:
                        dest.add(arr)

            if not dest:
                besoin_poubelle = True
                transitions_new.append((idx_courant, sym, -1))  # -1 = poubelle
            else:
                dest_tuple = tuple(sorted(dest))
                if dest_tuple not in vus:
                    vus[dest_tuple] = compteur
                    compteur += 1
                    a_traiter.append(dest_tuple)
                transitions_new.append((idx_courant, sym, vus[dest_tuple]))

    etats_new = list(range(compteur))

    # Ajouter état poubelle si besoin
    if besoin_poubelle:
        idx_p = compteur
        etats_new.append(idx_p)
        # Remplacer -1 par idx_p
        transitions_new = [(d, s, idx_p if a == -1 else a) for (d, s, a) in transitions_new]
        # Boucles sur poubelle
        for sym in alphabet:
            transitions_new.append((idx_p, sym, idx_p))

    # États terminaux
    terminaux_new = [vus[tup] for tup in vus if any(e in A['terminaux'] for e in tup)]

    # Correspondance
    print("\n--- Correspondance etats ---")
    for tup, idx in sorted(vus.items(), key=lambda x: x[1]):
        print(f"  Nouvel etat {idx} = {list(tup)}")
    if besoin_poubelle:
        print(f"  Nouvel etat {compteur} = [Poubelle]")

    return {
        'alphabet': alphabet,
        'etats': etats_new,
        'initiaux': [0],
        'terminaux': terminaux_new,
        'transitions': transitions_new
    }