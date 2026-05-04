# -*- coding: utf-8 -*-
import tkinter as tk
import solo as so
import multi as mu

# ── Palette ───────────────────────────────────────────────────────
BG     = "#0d1f0d"
ACCENT = "#f0c040"
GREEN  = "#2ecc71"
WHITE  = "#f0ede6"
FONT   = "Georgia"

fenetre = tk.Tk()
fenetre.title("Blackjack")
fenetre.configure(bg=BG)
fenetre.resizable(True, True)

# ── Adaptation à l'écran ──────────────────────────────────────────
fenetre.update_idletasks()
SW = fenetre.winfo_screenwidth()
SH = fenetre.winfo_screenheight()
W  = min(1280, int(SW * 0.95))
H  = min(800,  int(SH * 0.95))
fenetre.geometry(f"{W}x{H}+0+0")

# ── Arrière-plan décoratif ────────────────────────────────────────
canvas_bg = tk.Canvas(fenetre, width=W, height=H, bg=BG, highlightthickness=0)
canvas_bg.place(x=0, y=0)

# Tapis ovale
canvas_bg.create_oval(100, 80, W-100, H-80, fill="#122a12",
                      outline="#1e4a1e", width=4)
# Cercles décoratifs (coins)
for x, y in [(0,0),(W,0),(0,H),(W,H)]:
    canvas_bg.create_oval(x-60, y-60, x+60, y+60,
                          fill="", outline="#1a3a1a", width=2)

# ── Titre ─────────────────────────────────────────────────────────
title_frame = tk.Frame(fenetre, bg=BG)
title_frame.place(relx=0.5, rely=0.22, anchor="center")

tk.Label(title_frame, text="♠  BLACKJACK  ♠",
         font=(FONT, 64, "bold"),
         fg=ACCENT, bg=BG).pack()

tk.Label(title_frame, text="♥  ♦  Casino Royale  ♦  ♥",
         font=(FONT, 16), fg="#7a9a7a", bg=BG).pack(pady=(4,0))

# ── Séparateur doré ───────────────────────────────────────────────
sep = tk.Frame(fenetre, bg=ACCENT, height=2, width=340)
sep.place(relx=0.5, rely=0.39, anchor="center")

# ── Usine à boutons ───────────────────────────────────────────────
def make_menu_btn(text, cmd, row):
    btn = tk.Button(fenetre, text=text,
                    font=(FONT, 17, "bold"),
                    bg="#163516", fg=ACCENT,
                    activebackground="#1e4a1e",
                    activeforeground=WHITE,
                    relief=tk.FLAT, cursor="hand2",
                    width=18, height=2,
                    command=cmd,
                    highlightthickness=1,
                    highlightbackground=ACCENT)
    btn.place(relx=0.5, rely=row, anchor="center")

    # Hover effect
    btn.bind("<Enter>", lambda e: btn.config(bg="#1e4a1e", fg=WHITE))
    btn.bind("<Leave>", lambda e: btn.config(bg="#163516", fg=ACCENT))
    return btn

# ── Fenêtres secondaires ─────────────────────────────────────────
def score_():
    win = tk.Toplevel(fenetre)
    win.title("Scores")
    win.geometry("700x420")
    win.configure(bg=BG)

    tk.Label(win, text="📊  SCORES", font=(FONT, 28, "bold"),
             fg=ACCENT, bg=BG).pack(pady=30)
    tk.Label(win, text="Aucune partie jouée pour l'instant.",
             font=(FONT, 14), fg=WHITE, bg=BG).pack()
    tk.Button(win, text="Fermer", command=win.destroy,
              font=(FONT, 12, "bold"),
              bg="#163516", fg=ACCENT,
              relief=tk.FLAT, cursor="hand2",
              padx=20, pady=6).pack(pady=30)


def regle_jeux():
    win = tk.Toplevel(fenetre)
    win.title("Règles du jeu")
    win.geometry("820x560")
    win.configure(bg=BG)

    tk.Label(win, text="📖  RÈGLES DU BLACKJACK",
             font=(FONT, 22, "bold"), fg=ACCENT, bg=BG).pack(pady=24)

    regles = (
        "Le but du Blackjack est d'avoir une main la plus proche de 21 sans la dépasser,\n"
        "et de battre le croupier.\n\n"
        "• Les cartes 2 à 10 valent leur valeur nominale.\n"
        "• Les figures (Valet, Dame, Roi) valent 10 points.\n"
        "• L'As vaut 1 ou 11 selon ce qui vous convient.\n\n"
        "Au début, le joueur et le croupier reçoivent chacun 2 cartes.\n"
        "Le croupier a une carte cachée.\n\n"
        "• TIRER  → tirer une carte supplémentaire\n"
        "• RESTER → conserver sa main\n\n"
        "Le croupier révèle sa carte cachée et tire jusqu'à atteindre au moins 17.\n"
        "Si le joueur dépasse 21, il perd immédiatement (Bust).\n"
        "En cas d'égalité, la mise est remboursée.\n"
        "Un Blackjack naturel (As + carte à 10) rapporte 1,5× la mise."
    )

    tk.Label(win, text=regles, font=(FONT, 13),
             fg=WHITE, bg=BG, justify=tk.LEFT,
             wraplength=740).pack(padx=40)

    tk.Button(win, text="← Retour au menu", command=win.destroy,
              font=(FONT, 12, "bold"),
              bg="#163516", fg=ACCENT,
              relief=tk.FLAT, cursor="hand2",
              padx=20, pady=6).pack(pady=28)


def jeux():
    win = tk.Toplevel(fenetre)
    win.title("Mode de jeu")
    win.geometry("600x380")
    win.configure(bg=BG)

    tk.Label(win, text="CHOISISSEZ UN MODE",
             font=(FONT, 22, "bold"), fg=ACCENT, bg=BG).pack(pady=30)

    def style_btn(parent, text, cmd, enabled=True):
        b = tk.Button(parent, text=text,
                      font=(FONT, 16, "bold"),
                      bg="#163516" if enabled else "#0f2b0f",
                      fg=ACCENT if enabled else ACCENT,
                      activebackground="#1e4a1e",
                      state=tk.NORMAL if enabled else tk.DISABLED,
                      relief=tk.FLAT, cursor="hand2" if enabled else "arrow",
                      width=20, height=2,
                      command=cmd,
                      highlightthickness=1,
                      highlightbackground=ACCENT if enabled else "#1a3a1a")
        if enabled:
            b.bind("<Enter>", lambda e: b.config(bg="#1e4a1e", fg=WHITE))
            b.bind("<Leave>", lambda e: b.config(bg="#163516", fg=ACCENT))
        b.pack(pady=8)

    style_btn(win, "🃏  SOLO",        lambda: so.solo(fenetre))
    style_btn(win, "👥  MULTIJOUEUR", lambda: mu.multi(fenetre))

    tk.Button(win, text="← Menu", command=win.destroy,
              font=(FONT, 11), bg=BG, fg="#7a9a7a",
              relief=tk.FLAT, cursor="hand2").pack(pady=16)


# ── Boutons du menu principal ────────────────────────────────────
make_menu_btn("🃏   Jouer",    jeux,       0.50)
make_menu_btn("📊   Scores",   score_,     0.62)
make_menu_btn("📖   Règles",   regle_jeux, 0.74)

# ── Pied de page ─────────────────────────────────────────────────
tk.Label(fenetre, text="♣  Bonne chance  ♣",
         font=(FONT, 11), fg="#3a5a3a", bg=BG).place(relx=0.5, rely=0.94, anchor="center")

fenetre.mainloop()
    

    
