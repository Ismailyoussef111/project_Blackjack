# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 12:10:49 2026

@author: youss
"""

import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk 
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

fenetre = tk.Tk()
fenetre.title("Ma fenetre")
fenetre.geometry("1920x1080")
fenetre.configure(bg="#1a3a1a")

def regle_jeux():
    regle = tk.Toplevel(fenetre)  
    regle.title("regle")
    regle.geometry("1920x1080")
    regle.configure(bg="#1a3a1a")
    label_regle = tk.Label(regle, 
    text="Le but du Blackjack est avoir une main la plus proche de 21 sans la depasser et de battre le croupier. Les cartes 2 a 10 valent leur valeur nominale. Les figures (Valet Dame Roi) valent 10. As vaut 1 ou 11 selon ce qui te convient. Au debut le joueur et le croupier recoivent chacun 2 cartes. Le croupier a une carte cachee. Le joueur peut soit tirer une carte de plus (Hit) soit rester avec ses cartes (Stand). Ensuite le croupier revele sa carte cachee et tire des cartes jusqu a atteindre au moins 17. Si le joueur depasse 21 il perd directement. Si le joueur est plus proche de 21 que le croupier il gagne. En cas d egalite la mise est remboursee. Si le joueur a un Blackjack (As + carte a 10) des le depart il gagne 1.5 fois sa mise.",
    font=("Rockwell", 24), 
    fg="white", 
    bg="#1a3a1a", 
    wraplength=1400,  
    justify="left",
    padx=50)  
    label_regle.place(relx=0.5, rely=0.1, anchor="n")
    btn_retour = tk.Button(regle, text="MENU", width=15, height=2, font=("Rockwell", 9), command=regle.destroy,bg="#52be8c",relief=tk.GROOVE)
    btn_retour.place(relx=0.9, rely=0.9, anchor="center")


def score_():
    score = tk.Toplevel(fenetre)  
    score.title("score")
    score.geometry("1920x1080")
    score.configure(bg="#142e14")
    label_score = tk.Label(score, text="Votre score",font=("Rockwell", 24), fg="white", bg="#1a3a1a", wraplength=1400,justify="left",padx=50)  
    label_score.place(relx=0.5, rely=0.1, anchor="n")
    btn_menu = tk.Button(score, text="MENU", width=2, height=9, font=("Rockwell", 9), command=score.destroy,bg="#52be8c",relief=tk.GROOVE)
    btn_menu.place(relx=0.9, rely=0.9, anchor="center")


def solo():
    jeux_fini=False
    fensolo = tk.Toplevel(fenetre)
    fensolo.title("Blackjack - Solo")
    fensolo.geometry("1920x1080")
    fensolo.configure(bg="#142e14")
    ####################################################################
    deck_de_jeux=deck()
    croupier = [deck_de_jeux.pop(), deck_de_jeux.pop()]
    joueur = [deck_de_jeux.pop(), deck_de_jeux.pop()]  
    

    def val_main(c):
        valeur = 0
        as_count = 0
        for carte in c:
            if "As" in carte:
                as_count += 1
                valeur += 11        
            else:
                valeur += valeur_carte(carte)
        # si on dépasse 21, on repasse chaque As de 11 à 1 (-10)
        while valeur > 21 and as_count > 0:
            valeur -= 10
            as_count -= 1
        return valeur


        
    
    def afficher_joueur():
        label_txtj = tk.Label(fensolo, text="Ton score", font=("Rockwell", 33, "bold"), fg="white", bg="#1a3a1a")
        label_txtj .place(relx=0.5, rely=0.5, anchor="center")
        label_jou = tk.Label(fensolo, text=str(val_main(joueur)), font=("Rockwell", 23, "bold"), fg="white", bg="#1a3a1a")
        label_jou.place(relx=0.5, rely=0.6, anchor="center")
        label_txtc = tk.Label(fensolo, text="Le score du croupier", font=("Rockwell", 33, "bold"), fg="white", bg="#1a3a1a")
        label_txtc.place(relx=0.5, rely=0.2, anchor="center")
        label_crou = tk.Label(fensolo, text=str(val_main(croupier[0]))+ "?", font=("Rockwell", 23, "bold"), fg="white", bg="#1a3a1a")
        label_crou.place(relx=0.5, rely=0.3, anchor="center")
    afficher_joueur()
    
    def fin_croupier():
        label_txtc2 = tk.Label(fensolo, text="Le score du croupier", font=("Rockwell", 33, "bold"), fg="white", bg="#1a3a1a")
        label_txtc2.place(relx=0.5, rely=0.2, anchor="center")
        label_crou2 = tk.Label(fensolo, text=str(val_main(croupier)), font=("Rockwell", 23, "bold"), fg="white", bg="#1a3a1a")
        label_crou2.place(relx=0.5, rely=0.3, anchor="center")
        btn_tirage.config(state="disabled")
        btn_reste.config(state="disabled") 
        btn_rejouer.config(state="normal")
        
        
    rejouer=lambda: (fensolo.destroy(), solo())
        
    

        


    def tirernv_carte():
        joueur.append(deck_de_jeux.pop())
        afficher_joueur()
        if val_main(joueur)>21:
            label_depassement = tk.Label(fensolo, text="Perdu hahaha!", font=("Rockwell", 58, "bold"), fg="white", bg="#1a3a1a")
            label_depassement.place(relx=0.2, rely=0.3, anchor="center")
            fin_croupier()

    
        
        
        
    def rester():
        while val_main(croupier) < 17:
            croupier.append(deck_de_jeux.pop())
        afficher_joueur()
        
        if val_main(joueur)==21:
            label_21 = tk.Label(fensolo, text="Gagné trop fort!", font=("Rockwell", 58, "bold"), fg="white", bg="#1a3a1a")
            label_21.place(relx=0.2, rely=0.3, anchor="center")
            fin_croupier()
        
        elif val_main(croupier)>21:
            label = tk.Label(fensolo, text="Gagné trop fort!", font=("Rockwell", 58, "bold"), fg="white", bg="#1a3a1a")
            label.place(relx=0.2, rely=0.3, anchor="center")
            fin_croupier()
        
            
        elif val_main(joueur)>val_main(croupier):
            label = tk.Label(fensolo, text="Gagné trop fort!", font=("Rockwell", 58, "bold"), fg="white", bg="#1a3a1a")
            label.place(relx=0.2, rely=0.3, anchor="center")
            fin_croupier()
            
        elif val_main(joueur)<val_main(croupier):
            label_vict_croup = tk.Label(fensolo, text="Perdu hahaha!", font=("Rockwell", 58, "bold"), fg="white", bg="#1a3a1a")
            label_vict_croup.place(relx=0.3, rely=0.3, anchor="center")
            fin_croupier()
        jeux_fini= True
        
            
            
            
   
    btn_tirage = tk.Button(fensolo, text="TAKE", width=9, height=2, font=("Rockwell", 9), command=tirernv_carte,bg="#52be8c",relief=tk.GROOVE)
    btn_tirage.place(relx=0.9, rely=0.9, anchor="center")
    btn_reste = tk.Button(fensolo, text="STAY", width=9, height=2, font=("Rockwell", 9), command=rester,bg="#52be8c",relief=tk.GROOVE)
    btn_reste.place(relx=0.2, rely=0.9, anchor="center")
    btn_rejouer = tk.Button(fensolo, text="Rejouer", width=9, height=2, font=("Rockwell", 9), command=rejouer,bg="#52be8c",relief=tk.GROOVE)
    btn_rejouer.place(relx=0.5, rely=0.9, anchor="center")
    btn_rejouer.config(state="disabled") 
    btn_quitter= tk.Button(fensolo, text="GIVE UP", width=9, height=2, font=("Rockwell", 9), command=fenetre.destroy,bg="#52be8c",relief=tk.GROOVE)
    btn_quitter.place(relx=0.02, rely=0.017, anchor="center")
    

        
        

    
def jeux():
    feujeux=tk.Toplevel(fenetre)  
    feujeux.title("juego")
    feujeux.geometry("1920x1080")
    feujeux.configure(bg="#142e14")
    btn_solo = tk.Button(feujeux, text="SOLO", width=15, height=2, font=("Rockwell", 19), command=solo,bg="#52be8c")
    btn_solo.place(relx=0.5, rely=0.4, anchor="center")
    btn_multi = tk.Button(feujeux, text="MULTIJOEUR", width=15, height=2, font=("Rockwell", 19), command=None,bg="#52be8c")
    btn_multi.place(relx=0.5, rely=0.5, anchor="center")
    btn_rmenu = tk.Button(feujeux, text="MENU", width=9, height=2, font=("Rockwell", 9), command=feujeux.destroy,bg="#52be8c")
    btn_rmenu.place(relx=0.9, rely=0.9, anchor="right")
    

    
label = tk.Label(fenetre, text="Blackjack", font=("Rockwell", 78, "bold"), fg="white", bg="#1a3a1a")
label.place(relx=0.5, rely=0.3, anchor="center")

btn = tk.Button(fenetre, text="Regle", width=15, height=2, font=("Rockwell", 19), command=regle_jeux,bg="#52be8c",relief=tk.GROOVE)
btn.place(relx=0.5, rely=0.7, anchor="center")
btn2 = tk.Button(fenetre, text="Jouer", width=15, height=2, font=("Rockwell", 19), command=jeux,bg="#52be8c",relief=tk.GROOVE)
btn2.place(relx=0.5, rely=0.5, anchor="center")
btn3 = tk.Button(fenetre, text="score", width=15, height=2, font=("Rockwell", 19), command=score_,bg="#52be8c",relief=tk.GROOVE)
btn3.place(relx=0.5, rely=0.6, anchor="center",)


fenetre.mainloop()
    
