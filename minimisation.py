def minimiser(A):
    alphabet = A['alphabet']
    etats = A['etats']
    terminaux = A['terminaux']

    # Table de transitions : trans[etat][sym] = etat destination
    trans = {}
    for e in etats:
        trans[e] = {}
        for s in alphabet:
            trans[e][s] = None
    for (dep, sym, arr) in A['transitions']:
        trans[dep][sym] = arr

    # Partition initiale : terminaux / non-terminaux
    T = [e for e in etats if e in terminaux]
    NT = [e for e in etats if e not in terminaux]
    partition = [p for p in [T, NT] if p]

    print("\n--- Minimisation ---")

    etape = 0
    while True:
        # Afficher partition courante
        print(f"Partition {etape} : {partition}")

        # Fonction : trouver le groupe d'un état
        def groupe(e):
            for i, g in enumerate(partition):
                if e in g:
                    return i
            return -1  # poubelle

        nouvelle_partition = []
        for grp in partition:
            sous_groupes = {}
            for e in grp:
                # Signature = groupe de destination pour chaque symbole
                sig = tuple(groupe(trans[e][s]) if trans[e][s] is not None else -1
                            for s in alphabet)
                if sig not in sous_groupes:
                    sous_groupes[sig] = []
                sous_groupes[sig].append(e)
            nouvelle_partition.extend(sous_groupes.values())

        if len(nouvelle_partition) == len(partition):
            print(f"Partition finale : {nouvelle_partition}\n")
            break

        partition = nouvelle_partition
        etape += 1

    # Construire l'automate minimal
    # Un état par groupe, nommé par le plus petit élément du groupe
    def rep(grp):
        return min(grp)

    etats_min = [rep(g) for g in nouvelle_partition]
    initiaux_min = [rep(g) for g in nouvelle_partition if any(e in A['initiaux'] for e in g)]
    terminaux_min = [rep(g) for g in nouvelle_partition if any(e in terminaux for e in g)]

    transitions_min = []
    for g in nouvelle_partition:
        e = g[0]
        for s in alphabet:
            dest = trans[e][s]
            if dest is not None:
                dest_rep = rep(next(gg for gg in nouvelle_partition if dest in gg))
                transitions_min.append((rep(g), s, dest_rep))

    # Table de correspondance
    print("--- Correspondance etats minimaux ---")
    for g in nouvelle_partition:
        print(f"  Etat {rep(g)} (minimal) = {g} (AFDC)")

    return {
        'alphabet'   : alphabet,
        'etats'      : sorted(set(etats_min)),
        'initiaux'   : initiaux_min,
        'terminaux'  : terminaux_min,
        'transitions': transitions_min
    }