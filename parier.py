# -*- coding: utf-8 -*-
import tkinter as tk

argent_joueur = 1000

BG       = "#0d1f0d"
CARD_BG  = "#163516"
ACCENT   = "#f0c040"
GREEN    = "#2ecc71"
RED      = "#e74c3c"
WHITE    = "#f0ede6"
FONT     = "Georgia"

def initiation_pari(fensolo, btn_tirage, btn_reste, val_main, joueur, croupier):
    global argent_joueur

    mise_actuelle = tk.IntVar(value=0)

    
    frame_pari = tk.Frame(fensolo, bg=CARD_BG, bd=0, highlightthickness=2,
                          highlightbackground=ACCENT)
    frame_pari.place(relx=0.08, rely=0.5, anchor="center", width=200, height=230)

   
    label_argent = tk.Label(fensolo,
                            text=f"💰  {argent_joueur} €",
                            font=(FONT, 15, "bold"),
                            fg=ACCENT, bg="#154a15")
    label_argent.place(relx=0.08, rely=0.32, anchor="center")

    tk.Label(frame_pari, text="MISE",
             font=(FONT, 11, "bold"), fg=ACCENT, bg=CARD_BG).pack(pady=(12, 4))

    entree_mise = tk.Entry(frame_pari, font=(FONT, 15, "bold"), width=8,
                           bg="#0d1f0d", fg=WHITE, insertbackground=ACCENT,
                           relief=tk.FLAT, justify="center",
                           highlightthickness=1, highlightbackground=ACCENT)
    entree_mise.pack(pady=(0, 6))

    def valider_mise():
        global argent_joueur
        try:
            m = int(entree_mise.get())
            if 0 < m <= argent_joueur:
                mise_actuelle.set(m)
                label_feedback.config(text=f"{m} € misés", fg=GREEN)
                btn_tirage.config(state="normal")
                btn_reste.config(state="normal")
                btn_valider.config(state="disabled")
                entree_mise.config(state="disabled")
            else:
                label_feedback.config(text="Invalide", fg=RED)
        except Exception:
            label_feedback.config(text="Nombre entier svp", fg=RED)

    btn_valider = tk.Button(frame_pari, text="MISER ▶",
                            command=valider_mise,
                            font=(FONT, 10, "bold"),
                            bg=ACCENT, fg="#0d1f0d",
                            activebackground="#d4a820",
                            relief=tk.FLAT, cursor="hand2",
                            padx=8, pady=3)
    btn_valider.pack(pady=(0, 4))

    label_feedback = tk.Label(frame_pari, text="Entrez votre mise",
                              font=(FONT, 9), fg=WHITE, bg=CARD_BG,
                              wraplength=180, justify="center")
    label_feedback.pack(pady=(0, 4))

    shortcuts = tk.Frame(frame_pari, bg=CARD_BG)
    shortcuts.pack()

    def mise_rapide(v):
        entree_mise.config(state="normal")
        entree_mise.delete(0, tk.END)
        entree_mise.insert(0, str(v))

    row1 = tk.Frame(shortcuts, bg=CARD_BG)
    row1.pack()
    row2 = tk.Frame(shortcuts, bg=CARD_BG)
    row2.pack()

    for val, parent in zip([10, 50, 100, 200], [row1, row1, row2, row2]):
        tk.Button(parent, text=f"+{val}€",
                  command=lambda v=val: mise_rapide(v),
                  font=(FONT, 9), bg="#1e4a1e", fg=ACCENT,
                  activebackground="#2e6a2e",
                  relief=tk.FLAT, cursor="hand2",
                  padx=5, pady=2).pack(side=tk.LEFT, padx=2, pady=2)

    def calculer_resultat():
        global argent_joueur
        sj, sc = val_main(joueur), val_main(croupier)
        if sj <= 21 and (sc > 21 or sj > sc):
            argent_joueur += mise_actuelle.get() * 2
        elif sj > sc or sj > 21:
            argent_joueur -= mise_actuelle.get()
        label_argent.config(text=f"💰  {argent_joueur} €")

    return calculer_resultat

