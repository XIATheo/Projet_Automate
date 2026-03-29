import os

def lire_automate(numero):
    nom = os.path.join(os.path.dirname(__file__), "Automate", f"AF{int(numero):02d}.txt")
    with open(nom, 'r', encoding='utf-8') as f:
        lignes = [l.strip() for l in f if l.strip()]

    alphabet = [chr(ord('a') + i) for i in range(int(lignes[0]))]
    nb_etats = int(lignes[1])
    initiaux = [int(x) for x in lignes[2].split()[1:]]
    terminaux = [int(x) for x in lignes[3].split()[1:]]

    transitions = []
    for i in range(5, 5 + int(lignes[4])):
        t = lignes[i]
        if ' ' in t: # Format avec espaces : "0 a 1"
            parts = t.split()
            transitions.append((int(parts[0]), parts[1], int(parts[2])))
        else: # Format collé : "0E1" ou "1a2"
            import re
            m = re.match(r"(\d+)([a-zA-Z])(\d+)", t)
            if m:
                transitions.append((int(m.group(1)), m.group(2), int(m.group(3))))

    return {
        'alphabet': alphabet, 'etats': list(range(nb_etats)),
        'initiaux': initiaux, 'terminaux': terminaux, 'transitions': transitions
    }
