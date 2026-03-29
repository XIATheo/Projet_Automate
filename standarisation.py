def standardiser(A):
    # Crée un nouvel état initial i qui n'existe pas encore
    nouvel_init = max(A['etats']) + 1

    nouveaux_etats = A['etats'] + [nouvel_init]
    nouveaux_terminaux = A['terminaux'][:]

    # Le nouvel état initial est aussi terminal si un des anciens initiaux l'est
    if any(i in A['terminaux'] for i in A['initiaux']):
        nouveaux_terminaux.append(nouvel_init)

    # Copier toutes les transitions des anciens états initiaux vers le nouvel état
    nouvelles_transitions = A['transitions'][:]
    for (dep, sym, arr) in A['transitions']:
        if dep in A['initiaux']:
            nouvelles_transitions.append((nouvel_init, sym, arr))

    return {
        'alphabet': A['alphabet'],
        'etats': nouveaux_etats,
        'initiaux': [nouvel_init],
        'terminaux': nouveaux_terminaux,
        'transitions': nouvelles_transitions
    }