# -*- coding: utf-8 -*- 
from random import shuffle

def deck() :
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

SYMBOLES = {
    "coeur":   "♥",
    "pick":    "♠",
    "trefle":  "♣",
    "carreau": "♦",
}

COULEURS_ENSEIGNE = {
    "coeur":   "#e74c3c",
    "pick":    "#ecf0f1",
    "trefle":  "#ecf0f1",
    "carreau": "#e74c3c",
}

def get_symbole(carte):
    for enseigne, sym in SYMBOLES.items():
        if enseigne in carte:
            return sym, COULEURS_ENSEIGNE[enseigne]
    return "", "#ecf0f1"

def get_valeur_affichee(carte):
    for special in ["As", "Valet", "Roi", "Reine"]:
        if special in carte:
            return special[0]
    for n in range(10, 1, -1):
        if str(n) in carte:
            return str(n)
    return "?"


FONT = "Georgia"
ACCENT = "#f0c040"

def dessiner_carte(canvas, x, y, carte, cachee=False, w=72, h=100):
    """Dessine une carte (ou le dos) sur le canvas à la position (x, y)."""
    if cachee:
        canvas.create_rectangle(x, y, x+w, y+h,
                                 fill="#1a4a8a", outline=ACCENT, width=2)
        canvas.create_text(x+w//2, y+h//2, text="🂠",
                           font=(FONT, int(w * 0.36)), fill="#3a7abf")
        return

    sym, couleur = get_symbole(carte)
    val = get_valeur_affichee(carte)

    fs_corner = max(8,  int(w * 0.14))
    fs_sym_sm = max(7,  int(w * 0.12))
    fs_centre = max(16, int(w * 0.38))

    canvas.create_rectangle(x, y, x+w, y+h,
                             fill="#f5f0e8", outline="#ccbbaa", width=1)
    canvas.create_text(x + max(6, int(w*0.09)), y + max(8, int(h*0.09)),
                       text=val, font=(FONT, fs_corner, "bold"),
                       fill=couleur, anchor="nw")
    canvas.create_text(x + max(6, int(w*0.09)), y + max(8, int(h*0.09)) + fs_corner + 2,
                       text=sym, font=(FONT, fs_sym_sm),
                       fill=couleur, anchor="nw")
    canvas.create_text(x + w//2, y + h//2,
                       text=sym, font=(FONT, fs_centre),
                       fill=couleur)
    canvas.create_text(x + w - max(6, int(w*0.09)), y + h - max(8, int(h*0.09)),
                       text=val, font=(FONT, fs_corner, "bold"),
                       fill=couleur, anchor="se")
    canvas.create_text(x + w - max(6, int(w*0.09)), y + h - max(8, int(h*0.09)) - fs_corner - 2,
                       text=sym, font=(FONT, fs_sym_sm),
                       fill=couleur, anchor="se")
