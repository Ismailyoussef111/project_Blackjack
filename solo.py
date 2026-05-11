# -*- coding: utf-8 -*-
import tkinter as tk
import deck as dk

BG       = "#0d1f0d"
CARD_BG  = "#163516"
ACCENT   = "#f0c040"
GREEN    = "#2ecc71"
RED      = "#e74c3c"
WHITE    = "#f0ede6"
GRAY     = "#7f8c8d"
FONT     = "Georgia"




def solo(fenetre):
    fensolo = tk.Toplevel(fenetre)
    fensolo.title("Blackjack – Solo")
    fensolo.configure(bg=BG)
    fensolo.resizable(False, False)

    fensolo.update_idletasks()
    SW = fensolo.winfo_screenwidth()
    SH = fensolo.winfo_screenheight()
    W  = min(1280, int(SW * 0.95))
    H  = min(800,  int(SH * 0.95))
    fensolo.geometry(f"{W}x{H}+0+0")

    # Taille carte proportionnelle
    CW = max(54, int(W * 0.056))
    CH = int(CW * 1.39)

    deck_de_jeux = dk.deck()
    croupier = [deck_de_jeux.pop(), deck_de_jeux.pop()]
    joueur   = [deck_de_jeux.pop(), deck_de_jeux.pop()]

    
    def val_main(c):
        valeur, as_count = 0, 0
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

   
    canvas = tk.Canvas(fensolo, width=W, height=H-160,
                       bg="#154a15", highlightthickness=0)
    canvas.place(x=0, y=0)

    
    canvas.create_oval(60, 20, W-60, H-180, fill="#165a16",
                       outline="#1e6e1e", width=3)

   
    lbl_score_croupier = tk.Label(fensolo,
        text="CROUPIER", font=(FONT, 13, "bold"),
        fg=ACCENT, bg="#154a15")
    lbl_score_croupier.place(x=W//2, y=22, anchor="center")

    lbl_val_croupier = tk.Label(fensolo,
        text="?", font=(FONT, 28, "bold"),
        fg=WHITE, bg="#154a15")
    lbl_val_croupier.place(x=W//2, y=50, anchor="center")

    lbl_score_joueur = tk.Label(fensolo,
        text="VOUS", font=(FONT, 13, "bold"),
        fg=ACCENT, bg="#154a15")
    lbl_score_joueur.place(x=W//2, y=H-270, anchor="center")

    lbl_val_joueur = tk.Label(fensolo,
        text="", font=(FONT, 28, "bold"),
        fg=WHITE, bg="#154a15")
    lbl_val_joueur.place(x=W//2, y=H-242, anchor="center")

    
    lbl_resultat = tk.Label(fensolo, text="",
        font=(FONT, 36, "bold"), fg=ACCENT, bg="#154a15",
        relief=tk.FLAT)
    lbl_resultat.place(x=W//2, y=H//2-20, anchor="center")

    
    CW, CH = 72, 100   # taille carte

    def afficher_main(cartes, y_base, cacher_deuxieme=False):
        n = len(cartes)
        espacement = min(CW + 18, (W - 200) // max(n, 1))
        x_start = W//2 - (n * espacement) // 2
        for i, carte in enumerate(cartes):
            x = x_start + i * espacement
            cachee = cacher_deuxieme and i == 1
            dk.dessiner_carte(canvas, x, y_base, carte, cachee=cachee, w=CW, h=CH)

    def rafraichir(croupier_cache=True):
        canvas.delete("cartes")
        afficher_main(croupier, y_base=90, cacher_deuxieme=croupier_cache)
        afficher_main(joueur,   y_base=H-CH-220)
        lbl_val_joueur.config(text=str(val_main(joueur)))
        if croupier_cache:
            lbl_val_croupier.config(text=f"{dk.valeur_carte(croupier[0])} + ?")
        else:
            lbl_val_croupier.config(text=str(val_main(croupier)))

    def afficher_resultat(msg, couleur=ACCENT):
        lbl_resultat.config(text=msg, fg=couleur)

    
    def fin_croupier():
        rafraichir(croupier_cache=False)
        btn_tirage.config(state="disabled")
        btn_reste.config(state="disabled")
        btn_rejouer.config(state="normal")
        if calculer_resultat:
            calculer_resultat()

    
    def tirernv_carte():
        joueur.append(deck_de_jeux.pop())
        rafraichir()
        if val_main(joueur) > 21:
            afficher_resultat("💥  BUST – Perdu !", RED)
            fin_croupier()

    def rester():
        while val_main(croupier) < 17:
            croupier.append(deck_de_jeux.pop())

        sj, sc = val_main(joueur), val_main(croupier)
        if sj > sc or sc > 21:
            afficher_resultat("🏆  Vous gagnez !", GREEN)
        elif sj < sc:
            afficher_resultat("😔  Croupier gagne", RED)
        else:
            afficher_resultat("🤝  Égalité", GRAY)
        fin_croupier()

    rejouer = lambda: (fensolo.destroy(), solo(fenetre))

    
    bar = tk.Frame(fensolo, bg=BG, height=80)
    bar.place(x=0, y=H-140, width=W, height=80)

    def faire_btn(parent, text, cmd, **kw):
        return tk.Button(parent, text=text, command=cmd,
                         font=(FONT, 12, "bold"),
                         bg=kw.get("bg", ACCENT),
                         fg=kw.get("fg", "#0d1f0d"),
                         activebackground=kw.get("abg", "#d4a820"),
                         relief=tk.FLAT, cursor="hand2",
                         padx=18, pady=8)

    btn_quitter = faire_btn(bar, "✕  Abandonner", fensolo.destroy,
                           bg="#2c1010", fg=RED, abg="#3c1818")
    btn_quitter.pack(side=tk.LEFT, padx=20, pady=16)

    btn_tirage = faire_btn(bar, "🃏  TIRER", tirernv_carte)
    btn_tirage.pack(side=tk.LEFT, padx=10, pady=16)

    btn_reste = faire_btn(bar, "✋  RESTER", rester,
                         bg="#1e4a1e", fg=GREEN, abg="#2e6a2e")
    btn_reste.pack(side=tk.LEFT, padx=10, pady=16)

    btn_rejouer = faire_btn(bar, "↩  Rejouer", rejouer,
                           bg="#1a3a5a", fg="#82cfff", abg="#2a4a7a")
    btn_rejouer.pack(side=tk.RIGHT, padx=20, pady=16)
    btn_rejouer.config(state="disabled")

   
    import parier as pa
    calculer_resultat = pa.initiation_pari(
        fensolo, btn_tirage, btn_reste, val_main, joueur, croupier)

    btn_tirage.config(state="disabled")
    btn_reste.config(state="disabled")

    rafraichir()



 
