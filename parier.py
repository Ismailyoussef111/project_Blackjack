import tkinter as tk

argent_joueur = 1000

def initiation_pari(fensolo, btn_tirage, btn_reste, val_main, joueur, croupier):
    global argent_joueur

    mise_actuelle = tk.IntVar(value=0)

    def valider_mise():
        global argent_joueur
        try:
            m = int(entree_mise.get())
            if 0 < m <= argent_joueur:
                mise_actuelle.set(m)
                label_pari.config(text=f"Mise : {m}€", fg="#2ecc71")
                btn_tirage.config(state="normal")
                btn_reste.config(state="normal")
                btn_valider.config(state="disabled")
            else:
                label_pari.config(text="Montant invalide", fg="#e74c3c")
        except:
            label_pari.config(text="Entrez un nombre", fg="#e74c3c")

    def calculer_resultat():
        global argent_joueur
        sj, sc = val_main(joueur), val_main(croupier)
        if sj <= 21 and (sc > 21 or sj > sc):
            argent_joueur += mise_actuelle.get() * 2
        elif sj > sc or sj > 21:
            argent_joueur -= mise_actuelle.get()
        label_argent.config(text=f"Argent : {argent_joueur}€")

    # Widgets
    label_argent = tk.Label(fensolo, text=f"Argent : {argent_joueur}€", font=("Rockwell", 25), fg="white", bg="#142e14")
    label_argent.place(relx=0.8, rely=0.05, anchor="center")

    label_pari = tk.Label(fensolo, text="Entrez votre mise", font=("Rockwell", 15), fg="white", bg="#142e14")
    label_pari.place(relx=0.5, rely=0.7, anchor="center")

    entree_mise = tk.Entry(fensolo, font=("Rockwell", 18))
    entree_mise.place(relx=0.5, rely=0.75, anchor="center")

    btn_valider = tk.Button(fensolo, text="MISER", command=valider_mise, bg="#52be8c", width=10)
    btn_valider.place(relx=0.5, rely=0.82, anchor="center")

    return calculer_resultat  # solo.py appellera ça dans rester()
