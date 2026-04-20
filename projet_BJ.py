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
    
