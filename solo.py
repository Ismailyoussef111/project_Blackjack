from random import shuffle
import tkinter as tk
import deck as dk
 
 
 
 
def solo(fenetre):
    fensolo = tk.Toplevel(fenetre)
    fensolo.title("Blackjack - Solo")
    fensolo.geometry("1920x1080")
    fensolo.configure(bg="#142e14")
 
    deck_de_jeux = dk.deck()
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
                valeur += dk.valeur_carte(carte)
        while valeur > 21 and as_count > 0:
            valeur -= 10
            as_count -= 1
        return valeur
 
    def afficher_joueur():
        label_txtj = tk.Label(fensolo, text="Ton score", font=("Rockwell", 33, "bold"), fg="white", bg="#1a3a1a")
        label_txtj.place(relx=0.5, rely=0.5, anchor="center")
        label_jou = tk.Label(fensolo, text=str(val_main(joueur)), font=("Rockwell", 23, "bold"), fg="white", bg="#1a3a1a")
        label_jou.place(relx=0.5, rely=0.6, anchor="center")
        label_txtc = tk.Label(fensolo, text="Le score du croupier", font=("Rockwell", 33, "bold"), fg="white", bg="#1a3a1a")
        label_txtc.place(relx=0.5, rely=0.2, anchor="center")
        label_crou = tk.Label(fensolo, text=str(dk.valeur_carte(croupier[0])) + " ?", font=("Rockwell", 23, "bold"), fg="white", bg="#1a3a1a")
        label_crou.place(relx=0.5, rely=0.3, anchor="center")
 
    def fin_croupier():
        label_txtc2 = tk.Label(fensolo, text="Le score du croupier", font=("Rockwell", 33, "bold"), fg="white", bg="#1a3a1a")
        label_txtc2.place(relx=0.5, rely=0.2, anchor="center")
        label_crou2 = tk.Label(fensolo, text=str(val_main(croupier)), font=("Rockwell", 23, "bold"), fg="white", bg="#1a3a1a")
        label_crou2.place(relx=0.5, rely=0.3, anchor="center")
        btn_tirage.config(state="disabled")
        btn_reste.config(state="disabled")
        btn_rejouer.config(state="normal")
 
    rejouer = lambda: (fensolo.destroy(), solo(fenetre))
 
    def tirernv_carte():
        joueur.append(deck_de_jeux.pop())
        afficher_joueur()
        if val_main(joueur) > 21:
            label_depassement = tk.Label(fensolo, text="Perdu hahaha!", font=("Rockwell", 58, "bold"), fg="white", bg="#1a3a1a")
            label_depassement.place(relx=0.2, rely=0.3, anchor="center")
            fin_croupier()
 
    def rester():
        while val_main(croupier) < 17:
            croupier.append(deck_de_jeux.pop())
        afficher_joueur()
 
        if val_main(joueur) == 21:
            label_21 = tk.Label(fensolo, text="Gagné trop fort!", font=("Rockwell", 58, "bold"), fg="white", bg="#1a3a1a")
            label_21.place(relx=0.2, rely=0.3, anchor="center")
            fin_croupier()
        elif val_main(croupier) > 21:
            label = tk.Label(fensolo, text="Gagné trop fort!", font=("Rockwell", 58, "bold"), fg="white", bg="#1a3a1a")
            label.place(relx=0.2, rely=0.3, anchor="center")
            fin_croupier()
        elif val_main(joueur) > val_main(croupier):
            label = tk.Label(fensolo, text="Gagné trop fort!", font=("Rockwell", 58, "bold"), fg="white", bg="#1a3a1a")
            label.place(relx=0.2, rely=0.3, anchor="center")
            fin_croupier()
        elif val_main(joueur) < val_main(croupier):
            label_vict_croup = tk.Label(fensolo, text="Perdu hahaha!", font=("Rockwell", 58, "bold"), fg="white", bg="#1a3a1a")
            label_vict_croup.place(relx=0.3, rely=0.3, anchor="center")
            fin_croupier()
        elif val_main(joueur) == val_main(croupier):
            label_egal = tk.Label(fensolo, text="Egalité!", font=("Rockwell", 58, "bold"), fg="white", bg="#1a3a1a")
            label_egal.place(relx=0.3, rely=0.3, anchor="center")
            fin_croupier()
 

    btn_tirage = tk.Button(fensolo, text="TAKE", width=9, height=2, font=("Rockwell", 9), command=tirernv_carte, bg="#52be8c", relief=tk.GROOVE)
    btn_tirage.place(relx=0.9, rely=0.9, anchor="center")
 
    btn_reste = tk.Button(fensolo, text="STAY", width=9, height=2, font=("Rockwell", 9), command=rester, bg="#52be8c", relief=tk.GROOVE)
    btn_reste.place(relx=0.2, rely=0.9, anchor="center")
 
    btn_rejouer = tk.Button(fensolo, text="Rejouer", width=9, height=2, font=("Rockwell", 9), command=rejouer, bg="#52be8c", relief=tk.GROOVE)
    btn_rejouer.place(relx=0.5, rely=0.9, anchor="center")
    btn_rejouer.config(state="disabled")
 
    btn_quitter = tk.Button(fensolo, text="GIVE UP", width=9, height=2, font=("Rockwell", 9), command=fensolo.destroy, bg="#52be8c", relief=tk.GROOVE)
    btn_quitter.place(relx=0.02, rely=0.017, anchor="center")
    
    
    import parier as pa




    pa.init_pari(fensolo, btn_tirage, btn_reste, val_main, joueur, croupier)


    btn_tirage.config(state="disabled")
    btn_reste.config(state="disabled")
 
    afficher_joueur()
