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
                """
class Blackjack:
    def __init__(self,fenetre):
        self.fenetre=fenetre
        self.
    
                """
         
if __name__ == "__main__":
    app = Blackjack()
    app.mainloop()
    
