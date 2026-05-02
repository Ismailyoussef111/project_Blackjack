# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 10:55:34 2026

@author: youss
"""

from random import shuffle
import tkinter as tk
import deck as dk


BG_MAIN  = "#142e14"
BG_FRAME = "#1a3a1a"
VERT     = "#52be8c"
BLANC    = "white"
GRIS     = "#aaaaaa"
FONT     = "Rockwell"


def cadre(parent, relx, rely, width, height, anchor="center"):
    f = tk.Frame(parent, bg=BG_FRAME, bd=2, relief=tk.GROOVE,
                 highlightbackground=VERT, highlightthickness=1)
    f.place(relx=relx, rely=rely, anchor=anchor,
            relwidth=width, relheight=height)
    return f


def solo(fenetre):
    fensolo = tk.Toplevel(fenetre)
    fensolo.title("Blackjack - Solo")
    fensolo.geometry("1920x1080")
    fensolo.configure(bg=BG_MAIN)

    deck_de_jeux = dk.deck()
    croupier = [deck_de_jeux.pop(), deck_de_jeux.pop()]
    joueur   = [deck_de_jeux.pop(), deck_de_jeux.pop()]

   
    cadre_croupier = cadre(fensolo, relx=0.5, rely=0.10, width=0.44, height=0.18)
    cadre_joueur   = cadre(fensolo, relx=0.5, rely=0.38, width=0.44, height=0.26)

    tk.Label(cadre_croupier, text="Croupier", font=(FONT, 15),
             fg=GRIS, bg=BG_FRAME).place(relx=0.5, rely=0.15, anchor="center")
    tk.Label(cadre_joueur, text="Ton score", font=(FONT, 15),
             fg=GRIS, bg=BG_FRAME).place(relx=0.5, rely=0.10, anchor="center")

    label_score_croupier = tk.Label(cadre_croupier, text="",
                                    font=(FONT, 42, "bold"), fg=BLANC, bg=BG_FRAME)
    label_score_croupier.place(relx=0.5, rely=0.65, anchor="center")

    label_score_joueur = tk.Label(cadre_joueur, text="",
                                  font=(FONT, 42, "bold"), fg=BLANC, bg=BG_FRAME)
    label_score_joueur.place(relx=0.5, rely=0.42, anchor="center")

    label_resultat = tk.Label(cadre_joueur, text="",
                              font=(FONT, 22, "bold"), fg=VERT, bg=BG_FRAME)
    label_resultat.place(relx=0.5, rely=0.82, anchor="center")


    def val_main(c):
        valeur = 0
        as_count = 0
        for carte in c:
            if "As" in carte:
                as_count += 1
                valeur += 11
            else:
                valeur += dk.valeur_carte(carte)
        while valeur > 21 and as_count > 0:
            valeur -= 10
            as_count -= 1
        return valeur

    def afficher_joueur():
        label_score_joueur.config(text=str(val_main(joueur)))
        label_score_croupier.config(
            text=str(dk.valeur_carte(croupier[0])) + " ?"
        )

    def fin_croupier():
        label_score_croupier.config(text=str(val_main(croupier)))
        btn_tirage.config(state="disabled")
        btn_reste.config(state="disabled")
        btn_rejouer.config(state="normal")

    rejouer = lambda: (fensolo.destroy(), solo(fenetre))

    def tirernv_carte():
        joueur.append(deck_de_jeux.pop())
        afficher_joueur()
        if val_main(joueur) > 21:
            label_resultat.config(text="Perdu hahaha!", fg="#e74c3c")
            fin_croupier()

    def rester():
        while val_main(croupier) < 17:
            croupier.append(deck_de_jeux.pop())
        afficher_joueur()
        sj, sc = val_main(joueur), val_main(croupier)
        if sj > 21:
            label_resultat.config(text="Perdu hahaha!", fg="#e74c3c")
        elif sc > 21 or sj > sc:
            label_resultat.config(text="Gagné trop fort!", fg=VERT)
        elif sj < sc:
            label_resultat.config(text="Perdu hahaha!", fg="#e74c3c")
        else:
            label_resultat.config(text="Egalité!", fg="#f9c74f")
        fin_croupier()

    
    btn_tirage = tk.Button(fensolo, text="TAKE", width=9, height=2,
                           font=(FONT, 9), command=tirernv_carte,
                           bg=VERT, relief=tk.GROOVE)
    btn_tirage.place(relx=0.9, rely=0.9, anchor="center")

    btn_reste = tk.Button(fensolo, text="STAY", width=9, height=2,
                          font=(FONT, 9), command=rester,
                          bg=VERT, relief=tk.GROOVE)
    btn_reste.place(relx=0.1, rely=0.9, anchor="center")

    btn_rejouer = tk.Button(fensolo, text="Rejouer", width=9, height=2,
                            font=(FONT, 9), command=rejouer,
                            bg=VERT, relief=tk.GROOVE)
    btn_rejouer.place(relx=0.5, rely=0.9, anchor="center")
    btn_rejouer.config(state="disabled")

    btn_quitter = tk.Button(fensolo, text="GIVE UP", width=9, height=2,
                            font=(FONT, 9), command=fensolo.destroy,
                            bg=VERT, relief=tk.GROOVE)
    btn_quitter.place(relx=0.05, rely=0.05, anchor="center")

    import parier as pa
    pa.initiation_pari(fensolo, btn_tirage, btn_reste, val_main, joueur, croupier)

    btn_tirage.config(state="disabled")
    btn_reste.config(state="disabled")

    afficher_joueur()


 
