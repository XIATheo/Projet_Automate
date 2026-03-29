def complementaire(A):
    # Inverser les Ã©tats terminaux et non-terminaux
    nouveaux_terminaux = [e for e in A['etats'] if e not in A['terminaux']]

    return {
        'alphabet'   : A['alphabet'],
        'etats'      : A['etats'],
        'initiaux'   : A['initiaux'],
        'terminaux'  : nouveaux_terminaux,
        'transitions': A['transitions']
    }
