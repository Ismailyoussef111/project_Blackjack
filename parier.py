import tkinter as tk

BG_MAIN  = "#142e14"
BG_FRAME = "#1a3a1a"
BG_DARK  = "#0f200f"
VERT     = "#52be8c"
BLANC    = "white"
GRIS     = "#aaaaaa"
FONT     = "Rockwell"

argent_joueur = 1000


def initiation_pari(fensolo, btn_tirage, btn_reste, val_main, joueur, croupier):
    global argent_joueur

    mise_actuelle = tk.IntVar(value=0)

  
    cadre_argent = tk.Frame(fensolo, bg=BG_DARK, bd=2, relief=tk.GROOVE,
                            highlightbackground=VERT, highlightthickness=1)
    cadre_argent.place(relx=0.5, rely=0.65, anchor="center",
                       relwidth=0.44, relheight=0.09)

    tk.Label(cadre_argent, text="Solde", font=(FONT, 13),
             fg=GRIS, bg=BG_DARK).place(relx=0.25, rely=0.20, anchor="center")
    tk.Label(cadre_argent, text="Mise validée", font=(FONT, 13),
             fg=GRIS, bg=BG_DARK).place(relx=0.75, rely=0.20, anchor="center")

    label_argent = tk.Label(cadre_argent, text=f"{argent_joueur} €",
                            font=(FONT, 22, "bold"), fg=VERT, bg=BG_DARK)
    label_argent.place(relx=0.25, rely=0.65, anchor="center")

    label_mise_val = tk.Label(cadre_argent, text="0 €",
                              font=(FONT, 22, "bold"), fg="#f9c74f", bg=BG_DARK)
    label_mise_val.place(relx=0.75, rely=0.65, anchor="center")

    
    cadre_bet = tk.Frame(fensolo, bg=BG_FRAME, bd=2, relief=tk.GROOVE,
                         highlightbackground=VERT, highlightthickness=1)
    cadre_bet.place(relx=0.5, rely=0.76, anchor="center",
                    relwidth=0.44, relheight=0.08)

    tk.Label(cadre_bet, text="Entrez votre mise :", font=(FONT, 14),
             fg=GRIS, bg=BG_FRAME).place(relx=0.18, rely=0.5, anchor="center")

    entree_mise = tk.Entry(cadre_bet, font=(FONT, 16), width=8,
                           bg=BG_DARK, fg=BLANC, insertbackground=BLANC,
                           relief=tk.FLAT, bd=4)
    entree_mise.place(relx=0.52, rely=0.5, anchor="center")

    btn_valider = tk.Button(cadre_bet, text="MISER", font=(FONT, 11),
                            bg=VERT, relief=tk.GROOVE, width=7)
    btn_valider.place(relx=0.82, rely=0.5, anchor="center")

  
    def valider_mise():
        global argent_joueur
        try:
            m = int(entree_mise.get())
            if 0 < m <= argent_joueur:
                mise_actuelle.set(m)
                label_mise_val.config(text=f"{m} €", fg="#f9c74f")
                btn_tirage.config(state="normal")
                btn_reste.config(state="normal")
                btn_valider.config(state="disabled")
            else:
                label_mise_val.config(text="Invalide", fg="#e74c3c")
        except ValueError:
            label_mise_val.config(text="Nombre svp", fg="#e74c3c")

    btn_valider.config(command=valider_mise)

    def calculer_resultat():
        global argent_joueur
        sj, sc = val_main(joueur), val_main(croupier)
        if sj <= 21 and (sc > 21 or sj > sc):
            argent_joueur += mise_actuelle.get()
        elif sj > 21 or (sc <= 21 and sc > sj):
            argent_joueur -= mise_actuelle.get()
        label_argent.config(text=f"{argent_joueur} €")

    return calculer_resultat 

