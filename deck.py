from random import shuffle

def deck():
    groupe = [" coeur", " pick", " trefle", " carreau"]
    deck_carte = []
    special = ["As", "Valet", "Roi", "Reine"]
    for nom in groupe:
        for majeur in special:
            deck_carte.append(majeur + nom)
        for valeur in range(2, 11):
            deck_carte.append(str(valeur) + nom)
    shuffle(deck_carte)
    return deck_carte

def valeur_carte(carte):
    if "Roi" in carte or "Valet" in carte or "Reine" in carte or "10" in carte:
        return 10
    if "As" in carte:
        return 1
    for n in range(2, 10):
        if str(n) in carte:
            return n
    return 0
