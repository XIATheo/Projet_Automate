def est_deterministe(A):
    # Non déterministe si : plusieurs états initiaux OU plusieurs transitions même état/symbole
    if len(A['initiaux']) > 1:
        return False, "Plusieurs états initiaux"

    vus = {}
    for (dep, sym, arr) in A['transitions']:
        if (dep, sym) in vus:
            return False, f"Etat {dep} a plusieurs transitions par '{sym}'"
        vus[(dep, sym)] = arr

    return True, "Deterministe"


def est_standard(A):
    # Non standard si : plusieurs états initiaux OU une transition arrive sur l'état initial
    if len(A['initiaux']) > 1:
        return False, "Plusieurs états initiaux"

    init = A['initiaux'][0]
    for (dep, sym, arr) in A['transitions']:
        if arr == init:
            return False, f"Une transition arrive sur l'état initial ({init})"

    return True, "Standard"


def est_complet(A):
    # Complet si chaque état a exactement une transition par symbole
    for e in A['etats']:
