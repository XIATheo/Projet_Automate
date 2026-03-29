def afficher(A):
    print(f"\nAlphabet : {A['alphabet']}")
    print(f"Etats    : {A['etats']}")
    print(f"Initiaux : {A['initiaux']}")
    print(f"Terminaux: {A['terminaux']}\n")

    # table[etat][symbole] = liste destinations
    table = {e: {s: [] for s in A['alphabet']} for e in A['etats']}
    for (dep, sym, arr) in A['transitions']:
        table[dep][sym].append(arr)

    # largeurs colonnes
    lc = max(len(str(e)) for e in A['etats']) + 2
    ls = {s: max(len(s), max(len(','.join(str(a) for a in table[e][s]) or '--') for e in A['etats'])) + 2
          for s in A['alphabet']}

    # en-tete
    print("    " + "Etat".ljust(lc) + "".join(s.center(ls[s]) for s in A['alphabet']))
    print("-" * (4 + lc + sum(ls.values())))

    for e in A['etats']:
        m = ("ES" if e in A['initiaux'] and e in A['terminaux']
             else "E" if e in A['initiaux']
             else "S" if e in A['terminaux'] else "")
        ligne = m.ljust(4) + str(e).ljust(lc)
        for s in A['alphabet']:
            c = ','.join(str(a) for a in sorted(table[e][s])) or '--'
            ligne += c.center(ls[s])
        print(ligne)
    print()