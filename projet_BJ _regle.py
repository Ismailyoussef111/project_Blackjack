# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 12:10:49 2026

@author: youss
"""
import tkinter as tk
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
    if "Roi" in carte or "Valet" in carte or "Reine" in carte:  
        return 10
    if "As" in carte:
        return 11
    if "10" in carte:
        return 10
    for n in range(2, 10):
        if str(n) in carte:
            return n
    return 0

import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Ma fenetre")
fenetre.geometry("1920x1080")
fenetre.configure(bg="#1a3a1a")

def cliquer(): 
    regle = tk.Toplevel(fenetre)  # ← Toplevel au lieu de Tk() pour une 2eme fenetre
    regle.title("regle")
    regle.geometry("1920x1080")
    regle.configure(bg="#1a3a1a")
    label_regle = tk.Label(regle, 
    text="Le but du Blackjack est avoir une main la plus proche de 21 sans la depasser et de battre le croupier. Les cartes 2 a 10 valent leur valeur nominale. Les figures (Valet Dame Roi) valent 10. As vaut 1 ou 11 selon ce qui te convient. Au debut le joueur et le croupier recoivent chacun 2 cartes. Le croupier a une carte cachee. Le joueur peut soit tirer une carte de plus (Hit) soit rester avec ses cartes (Stand). Ensuite le croupier revele sa carte cachee et tire des cartes jusqu a atteindre au moins 17. Si le joueur depasse 21 il perd directement. Si le joueur est plus proche de 21 que le croupier il gagne. En cas d egalite la mise est remboursee. Si le joueur a un Blackjack (As + carte a 10) des le depart il gagne 1.5 fois sa mise.",
    font=("Rockwell", 14), 
    fg="white", 
    bg="#1a3a1a", 
    wraplength=1400,  # ← réduit pour avoir des marges
    justify="left",
    padx=50)  
    label_regle.place(relx=0.5, rely=0.1, anchor="n")
    
    
label = tk.Label(fenetre, text="Blackjack", font=("Rockwell", 48, "bold"), fg="white", bg="#1a3a1a")
label.place(relx=0.5, rely=0.3, anchor="center")

btn = tk.Button(fenetre, text="Regle", width=15, height=2, font=("Rockwell", 14), command=cliquer)
btn.place(relx=0.5, rely=0.5, anchor="center")

fenetre.mainloop()
"""

def jeux():
    jeux_fini = False
    deck_de_jeux = deck()
    croupier = [deck_de_jeux.pop(), deck_de_jeux.pop()]
    joueur = [deck_de_jeux.pop(), deck_de_jeux.pop()]
    
    score_croupier = 0  #
    score_joueur = 0  
    
    for carte in croupier:  
        score_croupier += valeur_carte(carte)
    for carte in joueur:    
        score_joueur += valeur_carte(carte)
    
    print("Ton score de départ :", score_joueur)
    
    while jeux_fini == False:
        take = input("Voulez vous tirer une nouvelle carte ? oui ou non : ")
        
        if take == "oui":
            nouveau = deck_de_jeux.pop()
            joueur.append(nouveau)
            score_joueur += valeur_carte(nouveau)
            if score_joueur > 21:
                print("t bete", score_joueur)
                jeux_fini = True  
            elif score_joueur < 21:
                print(score_joueur,"tu reveux des cartes ?")
            else:
                print("t chaud", score_joueur)
                jeux_fini = True              
        else :
            jeux_fini = True  
            print("score croupier:", score_croupier, "/ score joueur:", score_joueur)
            if score_croupier > score_joueur:
                print("perdu, t nul")
            else:
                print("gagné!")
                
                
fenetre.mainloop()
                
                
                
class Blackjack:
    def __init__(self,fenetre):
        self.fenetre=fenetre
        self.
    
               
         
if __name__ == "__main__":
    app = Blackjack()
    app.mainloop()
    """
