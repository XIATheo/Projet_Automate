def lire_automate(numero):
    nom = f"automates/AF{int(numero):02d}.txt"
    with open(nom, 'r') as f:
        lignes = [l.strip() for l in f if l.strip()]

    alphabet = [chr(ord('a') + i) for i in range(int(lignes[0]))]
    nb_etats = int(lignes[1])

    p = lignes[2].split()
    initiaux = [int(x) for x in p[1:int(p[0])+1]]

    p = lignes[3].split()
    terminaux = [int(x) for x in p[1:int(p[0])+1]]

    transitions = []
    for i in range(5, 5 + int(lignes[4])):
        t = lignes[i].split()
        transitions.append((int(t[0]), t[1], int(t[2])))

    return {
        'alphabet'   : alphabet,
        'etats'      : list(range(nb_etats)),
        'initiaux'   : initiaux,
        'terminaux'  : terminaux,
        'transitions': transitions
    }
