# -*- coding: utf-8 -*-
import tkinter as tk
import deck as dk

BG      = "#0d1f0d"
CARD_BG = "#163516"
ACCENT  = "#f0c040"
GREEN   = "#2ecc71"
RED     = "#e74c3c"
WHITE   = "#f0ede6"
GRAY    = "#7f8c8d"
BLUE    = "#5aafff"
FONT    = "Georgia"

argent = [1000, 1000]




def val_main(cartes):
    valeur, as_count = 0, 0
    for c in cartes:
        if "As" in c:
            as_count += 1; valeur += 11
        else:
            valeur += dk.valeur_carte(c)
    while valeur > 21 and as_count > 0:
        valeur -= 10; as_count -= 1
    return valeur


def multi(fenetre):
    fenmulti = tk.Toplevel(fenetre)
    fenmulti.title("Blackjack – Multijoueur")
    fenmulti.configure(bg=BG)
    fenmulti.resizable(False, False)

    # ── Détection taille écran disponible ────────────────────────
    fenmulti.update_idletasks()
    SW = fenmulti.winfo_screenwidth()
    SH = fenmulti.winfo_screenheight()
    # On prend 95% de l'écran max, mais pas plus que 1280×800
    W = min(1280, int(SW * 0.95))
    H = min(800,  int(SH * 0.95))
    fenmulti.geometry(f"{W}x{H}+0+0")

    global argent

    deck_jeu = dk.deck()
    croupier = [deck_jeu.pop(), deck_jeu.pop()]
    j1       = [deck_jeu.pop(), deck_jeu.pop()]
    j2       = [deck_jeu.pop(), deck_jeu.pop()]

    mises     = [tk.IntVar(value=0), tk.IntVar(value=0)]
    tour_fini = [False, False]
    mains     = [j1, j2]
    noms      = ["Joueur 1", "Joueur 2"]
    couleurs  = [GREEN, BLUE]

    # ── Layout dynamique basé sur H ───────────────────────────────
    BAR_H   = 70
    PAD_H   = 50
    TAPIS_H = H - BAR_H - PAD_H

    # Zones verticales dans le canvas :
    # Croupier  : 10% à 30% de TAPIS_H
    # Milieu    : 30% à 55%  (résultat, panel mise)
    # Joueurs   : 55% à 90%
    YCL = int(TAPIS_H * 0.04)   # label "CROUPIER"
    YCS = int(TAPIS_H * 0.08)   # score croupier
    YCC = int(TAPIS_H * 0.13)   # cartes croupier

    YJL = int(TAPIS_H * 0.56)   # label "JOUEUR 1/2"
    YJS = int(TAPIS_H * 0.61)   # score joueurs
    YJC = int(TAPIS_H * 0.65)   # cartes joueurs  (bas = YJC + 88)
    YJN = int(TAPIS_H * 0.87)   # nom joueur sous cartes
    YTO = int(TAPIS_H * 0.92)   # indicateur tour

    # ── Canvas tapis ──────────────────────────────────────────────
    canvas = tk.Canvas(fenmulti, width=W, height=TAPIS_H,
                       bg="#154a15", highlightthickness=0)
    canvas.place(x=0, y=0)

    def dessiner_fond():
        canvas.delete("all")
        canvas.create_oval(60, 20, W-60, TAPIS_H-20,
                           fill="#165a16", outline="#1e6e1e", width=3)
        canvas.create_line(W//2, int(TAPIS_H*0.25), W//2, TAPIS_H-20,
                           fill=ACCENT, width=1, dash=(6, 10))
        canvas.create_text(W//2,   YCL, text="CROUPIER",
                           font=(FONT, 12, "bold"), fill=ACCENT)
        canvas.create_text(W//4,   YJN, text="— JOUEUR 1 —",
                           font=(FONT, 11), fill=GREEN)
        canvas.create_text(3*W//4, YJN, text="— JOUEUR 2 —",
                           font=(FONT, 11), fill=BLUE)
        for cx, cy, sym in [(110, 70, "♠"), (W-110, 70, "♥"),
                            (110, TAPIS_H-35, "♦"), (W-110, TAPIS_H-35, "♣")]:
            canvas.create_text(cx, cy, text=sym, font=(FONT, 18),
                                fill=RED if sym in ("♥","♦") else ACCENT)

    dessiner_fond()

lbl_val_croupier = tk.Label(fenmulti, text="?",
                                 font=(FONT, 18, "bold"), fg=WHITE, bg="#154a15")
    lbl_val_croupier.place(x=W//2, y=YCS, anchor="center")

    lbl_val_j1 = tk.Label(fenmulti, text="",
                           font=(FONT, 16, "bold"), fg=GREEN, bg="#154a15")
    lbl_val_j1.place(x=W//4, y=YJS, anchor="center")

    lbl_val_j2 = tk.Label(fenmulti, text="",
                           font=(FONT, 16, "bold"), fg=BLUE, bg="#154a15")
    lbl_val_j2.place(x=3*W//4, y=YJS, anchor="center")

    lbl_tour = tk.Label(fenmulti, text="",
                         font=(FONT, 11, "bold"), fg=ACCENT, bg="#154a15")
    lbl_tour.place(x=W//2, y=YTO, anchor="center")

    # Taille carte proportionnelle à la fenêtre
    CW = max(50, int(W * 0.048))
    CH = int(CW * 1.39)

    def afficher_main_zone(cartes, x_centre, y_base, cacher_idx=None):
        n = len(cartes)
        espacement = min(CW + 14, 260 // max(n, 1))
        x_start = x_centre - (n * espacement) // 2
        for i, carte in enumerate(cartes):
            cachee = (cacher_idx is not None and i == cacher_idx)
            dk.dessiner_carte(canvas, x_start + i * espacement, y_base,
                              carte, cachee=cachee, w=CW, h=CH)

    def rafraichir(croupier_cache=True):
        dessiner_fond()
        afficher_main_zone(croupier, W//2,   YCC,
                           cacher_idx=1 if croupier_cache else None)
        afficher_main_zone(j1,       W//4,   YJC)
        afficher_main_zone(j2,       3*W//4, YJC)
        lbl_val_j1.config(text=str(val_main(j1)))
        lbl_val_j2.config(text=str(val_main(j2)))
        if croupier_cache:
            lbl_val_croupier.config(text=f"{dk.valeur_carte(croupier[0])} + ?")
        else:
            lbl_val_croupier.config(text=str(val_main(croupier)))

    bar = tk.Frame(fenmulti, bg=BG, height=BAR_H)
    bar.place(x=0, y=TAPIS_H, width=W, height=BAR_H)

    def make_btn(parent, text, cmd, bg=ACCENT, fg="#0d1f0d",
                 abg="#d4a820", state=tk.NORMAL):
        b = tk.Button(parent, text=text, command=cmd,
                      font=(FONT, 10, "bold"), bg=bg, fg=fg,
                      activebackground=abg, activeforeground=fg,
                      relief=tk.FLAT,
                      cursor="hand2" if state == tk.NORMAL else "arrow",
                      padx=8, pady=5, state=state)
        if state == tk.NORMAL:
            b.bind("<Enter>", lambda e: b.config(bg=abg) if b["state"] != "disabled" else None)
            b.bind("<Leave>", lambda e: b.config(bg=bg)  if b["state"] != "disabled" else None)
        return b

    btn_quitter = make_btn(bar, "✕  Abandonner", fenmulti.destroy,
                           bg="#2c1010", fg=RED, abg="#3c1818")
    btn_quitter.pack(side=tk.LEFT, padx=14, pady=14)

    frame_j1 = tk.Frame(bar, bg=BG); frame_j1.pack(side=tk.LEFT, padx=12)
    tk.Label(frame_j1, text="JOUEUR 1", font=(FONT, 8, "bold"), fg=GREEN, bg=BG).pack()
    fj1b = tk.Frame(frame_j1, bg=BG); fj1b.pack()
    btn_tirer1  = make_btn(fj1b, "🃏 TIRER",  None, state=tk.DISABLED)
    btn_tirer1.pack(side=tk.LEFT, padx=3)
    btn_rester1 = make_btn(fj1b, "✋ RESTER", None,
                           bg="#1e4a1e", fg=GREEN, abg="#2e6a2e", state=tk.DISABLED)
    btn_rester1.pack(side=tk.LEFT, padx=3)

    frame_j2 = tk.Frame(bar, bg=BG); frame_j2.pack(side=tk.LEFT, padx=12)
    tk.Label(frame_j2, text="JOUEUR 2", font=(FONT, 8, "bold"), fg=BLUE, bg=BG).pack()
    fj2b = tk.Frame(frame_j2, bg=BG); fj2b.pack()
    btn_tirer2  = make_btn(fj2b, "🃏 TIRER",  None, state=tk.DISABLED)
    btn_tirer2.pack(side=tk.LEFT, padx=3)
    btn_rester2 = make_btn(fj2b, "✋ RESTER", None,
                           bg="#0d1a2e", fg=BLUE, abg="#1a3a5a", state=tk.DISABLED)
    btn_rester2.pack(side=tk.LEFT, padx=3)

    btn_rejouer = make_btn(bar, "↩  Rejouer",
                           lambda: (fenmulti.destroy(), multi(fenetre)),
                           bg="#1a3a5a", fg="#82cfff", abg="#2a4a7a", state=tk.DISABLED)
    btn_rejouer.pack(side=tk.RIGHT, padx=14, pady=14)

    tk.Frame(fenmulti, bg=BG).place(x=0, y=TAPIS_H+BAR_H, width=W, height=PAD_H)
    tk.Label(fenmulti, text="♣  Bonne chance  ♣",
             font=(FONT, 9), fg="#3a5a3a", bg=BG).place(
             relx=0.5, rely=0.97, anchor="center")

    PW = min(460, int(W * 0.38))
    PH = min(310, int(TAPIS_H * 0.50))
    frame_paris = tk.Frame(fenmulti, bg=CARD_BG,
                           highlightthickness=2, highlightbackground=ACCENT)
    frame_paris.place(x=W//2, y=int(TAPIS_H * 0.42), anchor="center",
                      width=PW, height=PH)

    tk.Label(frame_paris, text="✦  MISES  ✦",
             font=(FONT, 13, "bold"), fg=ACCENT, bg=CARD_BG).grid(
             row=0, column=0, columnspan=4, pady=(10, 3))
    tk.Frame(frame_paris, bg=ACCENT, height=1).grid(
             row=1, column=0, columnspan=4, sticky="ew", padx=24, pady=(0, 6))

    entries = []; labels_argent = []
    for idx in range(2):
        coul = couleurs[idx]
        tk.Label(frame_paris, text=noms[idx],
                 font=(FONT, 11, "bold"), fg=coul, bg=CARD_BG).grid(
                 row=2+idx*4, column=0, columnspan=4, pady=(3, 0))
        la = tk.Label(frame_paris, text=f"💰  {argent[idx]} €",
                      font=(FONT, 10), fg=ACCENT, bg=CARD_BG)
        la.grid(row=3+idx*4, column=0, columnspan=2, pady=1)
        labels_argent.append(la)
        e = tk.Entry(frame_paris, font=(FONT, 11, "bold"), width=6,
                     bg="#0d1f0d", fg=WHITE, insertbackground=ACCENT,
                     relief=tk.FLAT, justify="center",
                     highlightthickness=1, highlightbackground=ACCENT)
        e.grid(row=3+idx*4, column=2, padx=6, pady=1)
        entries.append(e)
        rf = tk.Frame(frame_paris, bg=CARD_BG)
        rf.grid(row=4+idx*4, column=0, columnspan=4, pady=(1, 4))
        for v in [10, 50, 100, 200]:
            tk.Button(rf, text=f"+{v}€",
                      command=lambda vv=v, ee=e: (ee.delete(0, tk.END), ee.insert(0, str(vv))),
                      font=(FONT, 8), bg="#1e4a1e", fg=ACCENT,
                      activebackground="#2e6a2e", relief=tk.FLAT, cursor="hand2",
                      padx=3, pady=1).pack(side=tk.LEFT, padx=2)

    lbl_err = tk.Label(frame_paris, text="", font=(FONT, 8), fg=RED, bg=CARD_BG)
    lbl_err.grid(row=10, column=0, columnspan=4)

    def valider_paris():
        for idx in range(2):
            try:
                m = int(entries[idx].get())
                if 0 < m <= argent[idx]:
                    mises[idx].set(m)
                else:
                    lbl_err.config(text=f"Mise invalide pour {noms[idx]} (max {argent[idx]} €)")
                    return
            except Exception:
                lbl_err.config(text=f"Entrez un nombre valide pour {noms[idx]}")
                return
        frame_paris.place_forget()
        demarrer_j1()

    tk.Button(frame_paris, text="VALIDER LES MISES  ▶",
              command=valider_paris,
              font=(FONT, 11, "bold"), bg=ACCENT, fg="#0d1f0d",
              activebackground="#d4a820", relief=tk.FLAT, cursor="hand2",
              padx=10, pady=4).grid(row=11, column=0, columnspan=4, pady=(3, 10))

    # ── Logique de jeu ────────────────────────────────────────────
    def set_tour(msg, couleur=ACCENT):
        lbl_tour.config(text=msg, fg=couleur)

    def fin_partie():
        for b in [btn_tirer1, btn_rester1, btn_tirer2, btn_rester2]:
            b.config(state=tk.DISABLED)
        while val_main(croupier) < 17:
            croupier.append(deck_jeu.pop())
        rafraichir(croupier_cache=False)

        sc = val_main(croupier)
        msgs = []
        for idx in range(2):
            sj = val_main(mains[idx])
            if sj > 21:
                argent[idx] -= mises[idx].get()
                msgs.append((f"💥  {noms[idx]} : BUST  (-{mises[idx].get()} €)", RED))
            elif sc > 21 or sj > sc:
                argent[idx] += mises[idx].get()
                msgs.append((f"🏆  {noms[idx]} : Gagne  (+{mises[idx].get()} €)", GREEN))
            elif sj < sc:
                argent[idx] -= mises[idx].get()
                msgs.append((f"😔  {noms[idx]} : Perd  (-{mises[idx].get()} €)", RED))
            else:
                msgs.append((f"🤝  {noms[idx]} : Égalité  (±0 €)", GRAY))

        RW = min(460, int(W * 0.38))
        frame_res = tk.Frame(fenmulti, bg=CARD_BG,
                             highlightthickness=2, highlightbackground=ACCENT)
        frame_res.place(x=W//2, y=int(TAPIS_H * 0.42), anchor="center",
                        width=RW, height=180)
        tk.Label(frame_res, text="═══  Résultats  ═══",
                 font=(FONT, 12, "bold"), fg=ACCENT, bg=CARD_BG).pack(pady=(10, 5))
        for msg, col in msgs:
            tk.Label(frame_res, text=msg, font=(FONT, 11, "bold"),
                     fg=col, bg=CARD_BG).pack(pady=2)
        tk.Label(frame_res, text=f"J1 : {argent[0]} €   |   J2 : {argent[1]} €",
                 font=(FONT, 9), fg=ACCENT, bg=CARD_BG).pack(pady=(6, 4))

        set_tour("")
        btn_rejouer.config(state=tk.NORMAL)

    def demarrer_j1():
        set_tour("→  Tour de  JOUEUR 1  —  TIRER ou RESTER", GREEN)
        btn_tirer1.config(state=tk.NORMAL)
        btn_rester1.config(state=tk.NORMAL)
        rafraichir()

    def demarrer_j2():
        set_tour("→  Tour de  JOUEUR 2  —  TIRER ou RESTER", BLUE)
        btn_tirer2.config(state=tk.NORMAL)
        btn_rester2.config(state=tk.NORMAL)

    def tirer_j(idx):
        mains[idx].append(deck_jeu.pop())
        rafraichir()
        if val_main(mains[idx]) > 21:
            tour_fini[idx] = True
            if idx == 0:
                set_tour("Joueur 1 BUST !  →  Tour de JOUEUR 2", RED)
                btn_tirer1.config(state=tk.DISABLED)
                btn_rester1.config(state=tk.DISABLED)
                demarrer_j2()
            else:
                fin_partie()

    def rester_j(idx):
        tour_fini[idx] = True
        if idx == 0:
            btn_tirer1.config(state=tk.DISABLED)
            btn_rester1.config(state=tk.DISABLED)
            demarrer_j2()
        else:
            btn_tirer2.config(state=tk.DISABLED)
            btn_rester2.config(state=tk.DISABLED)
            fin_partie()

    btn_tirer1.config(command=lambda: tirer_j(0))
    btn_rester1.config(command=lambda: rester_j(0))
    btn_tirer2.config(command=lambda: tirer_j(1))
    btn_rester2.config(command=lambda: rester_j(1))

    rafraichir()
