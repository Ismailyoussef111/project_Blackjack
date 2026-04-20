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
import solo as so
            
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
    btn_solo = tk.Button(feujeux, text="SOLO", width=15, height=2, font=("Rockwell", 19), command=so.solo,bg="#52be8c")
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
    
