# -*- coding: utf-8 -*-
import tkinter as tk
import deck as dk

COULEUR_FOND    = "#0a0a0a"
COULEUR_TAPIS   = "#0d2e0d"
COULEUR_OR      = "#d4af37"
COULEUR_OR2     = "#f0c040"
COULEUR_VERT    = "#2ecc71"
COULEUR_ROUGE   = "#e74c3c"
COULEUR_BLANC   = "#f5f0e8"
COULEUR_BLEU    = "#3a8ad4"
COULEUR_BLEU2   = "#5aafff"
NOM_POLICE      = "Georgia"

LARGEUR, HAUTEUR = 1920, 1080


def dessiner_carte(canvas, pos_x, pos_y, carte, cachee=False, largeur_carte=80, hauteur_carte=115):
    if cachee:
        canvas.create_rectangle(pos_x+2, pos_y+2, pos_x+largeur_carte+2, pos_y+hauteur_carte+2, fill="#000000", outline="")
        canvas.create_rectangle(pos_x, pos_y, pos_x+largeur_carte, pos_y+hauteur_carte, fill="#1a3a8a", outline=COULEUR_OR, width=2)
        for i in range(4, largeur_carte-4, 8):
            canvas.create_line(pos_x+i, pos_y+4, pos_x+i, pos_y+hauteur_carte-4, fill="#1e4aaa", width=1)
        canvas.create_text(pos_x+largeur_carte//2, pos_y+hauteur_carte//2, text="🂠", font=(NOM_POLICE, 28), fill="#2a5adf")
        return

    symbole, couleur_carte = dk.get_symbole(carte)
    valeur_affichee = dk.get_valeur_affichee(carte)

    canvas.create_rectangle(pos_x+4, pos_y+4, pos_x+largeur_carte+4, pos_y+hauteur_carte+4, fill="#000000", outline="")
    canvas.create_rectangle(pos_x, pos_y, pos_x+largeur_carte, pos_y+hauteur_carte, fill="#faf6ee", outline="#ccbbaa", width=1)
    canvas.create_rectangle(pos_x+3, pos_y+3, pos_x+largeur_carte-3, pos_y+hauteur_carte-3, fill="", outline="#e0d5c0", width=1)

    canvas.create_text(pos_x+10, pos_y+12, text=valeur_affichee, font=(NOM_POLICE, 12, "bold"), fill=couleur_carte, anchor="nw")
    canvas.create_text(pos_x+10, pos_y+26, text=symbole,         font=(NOM_POLICE, 11),          fill=couleur_carte, anchor="nw")
    canvas.create_text(pos_x+largeur_carte//2, pos_y+hauteur_carte//2, text=symbole, font=(NOM_POLICE, 32), fill=couleur_carte)
    canvas.create_text(pos_x+largeur_carte-10, pos_y+hauteur_carte-12, text=valeur_affichee, font=(NOM_POLICE, 12, "bold"), fill=couleur_carte, anchor="se")
    canvas.create_text(pos_x+largeur_carte-10, pos_y+hauteur_carte-26, text=symbole,         font=(NOM_POLICE, 11),          fill=couleur_carte, anchor="se")


def calculer_valeur_main(liste_cartes):
    total_points, nombre_as = 0, 0
    for carte in liste_cartes:
        if "As" in carte:
            nombre_as += 1
            total_points += 11
        else:
            total_points += dk.valeur_carte(carte)
    while total_points > 21 and nombre_as > 0:
        total_points -= 10
        nombre_as -= 1
    return total_points


def multi(fenetre):
    fenetre_multi = tk.Toplevel(fenetre)
    fenetre_multi.title("Blackjack – Multijoueur")
    fenetre_multi.geometry(f"{LARGEUR}x{HAUTEUR}")
    fenetre_multi.configure(bg=COULEUR_FOND)
    fenetre_multi.resizable(False, False)

    paquet_cartes  = dk.deck()
    main_croupier  = [paquet_cartes.pop(), paquet_cartes.pop()]
    main_joueur1   = [paquet_cartes.pop(), paquet_cartes.pop()]
    main_joueur2   = [paquet_cartes.pop(), paquet_cartes.pop()]

    solde_joueurs  = [1000, 1000]
    mises_joueurs  = [tk.IntVar(value=0), tk.IntVar(value=0)]
    tour_termine   = [False, False]
    phase_actuelle = [0]

    liste_mains      = [main_joueur1, main_joueur2]
    noms_joueurs     = ["Joueur 1", "Joueur 2"]
    couleurs_joueurs = [COULEUR_VERT, COULEUR_BLEU2]

    canvas_jeu = tk.Canvas(fenetre_multi, width=LARGEUR, height=HAUTEUR, bg=COULEUR_FOND, highlightthickness=0)
    canvas_jeu.place(x=0, y=0)

    for i in range(20, 0, -1):
        ratio = i / 20
        r = int(5 + 30*ratio); g = int(5 + 60*ratio); b = int(5 + 15*ratio)
        canvas_jeu.create_oval(LARGEUR//2 - int(800*ratio), HAUTEUR//2 - int(480*ratio),
                       LARGEUR//2 + int(800*ratio), HAUTEUR//2 + int(480*ratio),
                       fill=f"#{r:02x}{g:02x}{b:02x}", outline="")

    canvas_jeu.create_oval(80, 60, LARGEUR-80, HAUTEUR-60, fill=COULEUR_TAPIS, outline=COULEUR_OR, width=4)
    canvas_jeu.create_oval(96, 76, LARGEUR-96, HAUTEUR-76, fill="", outline="#8b6914", width=1)

    canvas_jeu.create_line(LARGEUR//2, 260, LARGEUR//2, HAUTEUR-90, fill=COULEUR_OR, width=1, dash=(6, 10))

    canvas_jeu.create_text(LARGEUR//2, 52, text="— CROUPIER —", font=(NOM_POLICE, 16), fill=COULEUR_OR)
    canvas_jeu.create_text(LARGEUR//4,   HAUTEUR-52, text="— JOUEUR 1 —", font=(NOM_POLICE, 14), fill=COULEUR_VERT)
    canvas_jeu.create_text(3*LARGEUR//4, HAUTEUR-52, text="— JOUEUR 2 —", font=(NOM_POLICE, 14), fill=COULEUR_BLEU2)

    for pos_x, pos_y, symbole_deco in [(160,120,"♠"),(LARGEUR-160,120,"♥"),(160,HAUTEUR-120,"♦"),(LARGEUR-160,HAUTEUR-120,"♣")]:
        couleur_deco = COULEUR_ROUGE if symbole_deco in ("♥","♦") else COULEUR_OR
        canvas_jeu.create_text(pos_x, pos_y, text=symbole_deco, font=(NOM_POLICE, 26), fill=couleur_deco)

    label_score_croupier = canvas_jeu.create_text(LARGEUR//2, 100,   text="", font=(NOM_POLICE, 36, "bold"), fill=COULEUR_BLANC)
    label_score_joueur1  = canvas_jeu.create_text(LARGEUR//4,   HAUTEUR-95, text="", font=(NOM_POLICE, 28, "bold"), fill=COULEUR_VERT)
    label_score_joueur2  = canvas_jeu.create_text(3*LARGEUR//4, HAUTEUR-95, text="", font=(NOM_POLICE, 28, "bold"), fill=COULEUR_BLEU2)

    label_resultat_ombre = canvas_jeu.create_text(LARGEUR//2+3, HAUTEUR//2+3, text="", font=(NOM_POLICE, 60, "bold"), fill="#000000")
    label_resultat       = canvas_jeu.create_text(LARGEUR//2,   HAUTEUR//2,   text="", font=(NOM_POLICE, 60, "bold"), fill=COULEUR_OR)
    canvas_jeu.tag_lower(label_resultat_ombre, label_resultat)

    label_tour_actuel = canvas_jeu.create_text(LARGEUR//2, HAUTEUR//2 - 80, text="", font=(NOM_POLICE, 22, "bold"), fill=COULEUR_OR)

    def afficher_main_zone(liste_cartes, x_centre, y_base, index_cache=None):
        nombre_cartes = len(liste_cartes)
        espacement = min(95, 350 // max(nombre_cartes, 1))
        x_debut = x_centre - (nombre_cartes * espacement) // 2
        for i, carte in enumerate(liste_cartes):
            est_cachee = (index_cache is not None and i == index_cache)
            dessiner_carte(canvas_jeu, x_debut + i*espacement, y_base, carte, cachee=est_cachee)

    def actualiser_affichage(croupier_cache=True):
        canvas_jeu.delete("cartes")
        afficher_main_zone(main_croupier, LARGEUR//2, 130, index_cache=1 if croupier_cache else None)
        afficher_main_zone(main_joueur1, LARGEUR//4, HAUTEUR-310)
        afficher_main_zone(main_joueur2, 3*LARGEUR//4, HAUTEUR-310)
        canvas_jeu.itemconfig(label_score_joueur1, text=str(calculer_valeur_main(main_joueur1)))
        canvas_jeu.itemconfig(label_score_joueur2, text=str(calculer_valeur_main(main_joueur2)))
        if croupier_cache:
            canvas_jeu.itemconfig(label_score_croupier, text=f"{dk.valeur_carte(main_croupier[0])}  +  ?")
        else:
            canvas_jeu.itemconfig(label_score_croupier, text=str(calculer_valeur_main(main_croupier)))

    def mettre_a_jour_label_tour(message, couleur=COULEUR_OR):
        canvas_jeu.itemconfig(label_tour_actuel, text=message, fill=couleur)

    def afficher_resultat(message, couleur=COULEUR_OR):
        canvas_jeu.itemconfig(label_resultat,       text=message, fill=couleur)
        canvas_jeu.itemconfig(label_resultat_ombre, text=message)

    def creer_bouton(parent, texte, commande, couleur_fond=COULEUR_OR, couleur_texte=COULEUR_FOND, etat=tk.NORMAL):
        bouton = tk.Button(parent, text=texte, command=commande,
                      font=(NOM_POLICE, 13, "bold"),
                      bg=couleur_fond, fg=couleur_texte,
                      activebackground=COULEUR_OR2, activeforeground=COULEUR_FOND,
                      relief=tk.FLAT, cursor="hand2",
                      padx=16, pady=8, state=etat)
        bouton.bind("<Enter>", lambda e: bouton.config(bg=COULEUR_OR2 if couleur_fond==COULEUR_OR else couleur_fond))
        bouton.bind("<Leave>", lambda e: bouton.config(bg=couleur_fond))
        return bouton

    barre_boutons = tk.Frame(fenetre_multi, bg="#050f05", height=90)
    barre_boutons.place(x=0, y=HAUTEUR-90, width=LARGEUR, height=90)

    btn_quitter = creer_bouton(barre_boutons, "✕  Quitter", fenetre_multi.destroy, couleur_fond="#1a0505", couleur_texte=COULEUR_ROUGE)
    btn_quitter.pack(side=tk.LEFT, padx=30, pady=20)

    cadre_joueur1 = tk.Frame(barre_boutons, bg="#050f05")
    cadre_joueur1.pack(side=tk.LEFT, padx=40)
    label_nom_joueur1 = tk.Label(cadre_joueur1, text="J1", font=(NOM_POLICE, 10), fg=COULEUR_VERT, bg="#050f05")
    label_nom_joueur1.pack()
    cadre_boutons_joueur1 = tk.Frame(cadre_joueur1, bg="#050f05")
    cadre_boutons_joueur1.pack()
    btn_tirer_joueur1  = creer_bouton(cadre_boutons_joueur1, "🃏 TIRER",  None, etat=tk.DISABLED)
    btn_tirer_joueur1.pack(side=tk.LEFT, padx=6)
    btn_rester_joueur1 = creer_bouton(cadre_boutons_joueur1, "✋ RESTER", None, couleur_fond="#0d2e0d", couleur_texte=COULEUR_VERT, etat=tk.DISABLED)
    btn_rester_joueur1.pack(side=tk.LEFT, padx=6)

    cadre_joueur2 = tk.Frame(barre_boutons, bg="#050f05")
    cadre_joueur2.pack(side=tk.LEFT, padx=40)
    label_nom_joueur2 = tk.Label(cadre_joueur2, text="J2", font=(NOM_POLICE, 10), fg=COULEUR_BLEU2, bg="#050f05")
    label_nom_joueur2.pack()
    cadre_boutons_joueur2 = tk.Frame(cadre_joueur2, bg="#050f05")
    cadre_boutons_joueur2.pack()
    btn_tirer_joueur2  = creer_bouton(cadre_boutons_joueur2, "🃏 TIRER",  None, etat=tk.DISABLED)
    btn_tirer_joueur2.pack(side=tk.LEFT, padx=6)
    btn_rester_joueur2 = creer_bouton(cadre_boutons_joueur2, "✋ RESTER", None, couleur_fond="#0d1a2e", couleur_texte=COULEUR_BLEU2, etat=tk.DISABLED)
    btn_rester_joueur2.pack(side=tk.LEFT, padx=6)

    btn_rejouer = creer_bouton(barre_boutons, "↩  Rejouer", lambda: (fenetre_multi.destroy(), multi(fenetre)),
                           couleur_fond="#0d1a2e", couleur_texte=COULEUR_BLEU2, etat=tk.DISABLED)
    btn_rejouer.pack(side=tk.RIGHT, padx=30, pady=20)

    liste_boutons_tirer  = [btn_tirer_joueur1,  btn_tirer_joueur2]
    liste_boutons_rester = [btn_rester_joueur1, btn_rester_joueur2]

    cadre_mises = tk.Frame(fenetre_multi, bg="#0d1a0d", highlightthickness=2, highlightbackground=COULEUR_OR)
    cadre_mises.place(relx=0.5, rely=0.5, anchor="center", width=520, height=340)

    tk.Label(cadre_mises, text="✦  MISES  ✦", font=(NOM_POLICE, 16, "bold"),
             fg=COULEUR_OR, bg="#0d1a0d").grid(row=0, column=0, columnspan=4, pady=(18, 6))
    tk.Frame(cadre_mises, bg=COULEUR_OR, height=1).grid(row=1, column=0, columnspan=4, sticky="ew", padx=20, pady=(0,12))

    liste_champs_saisie = []
    liste_labels_solde  = []

    for idx in range(2):
        nom_joueur     = noms_joueurs[idx]
        couleur_joueur = couleurs_joueurs[idx]

        tk.Label(cadre_mises, text=nom_joueur, font=(NOM_POLICE, 13, "bold"),
                 fg=couleur_joueur, bg="#0d1a0d").grid(row=2+idx*3, column=0, columnspan=4, pady=(4,0))

        label_solde = tk.Label(cadre_mises, text=f"💰  {solde_joueurs[idx]} €",
                      font=(NOM_POLICE, 12), fg=COULEUR_OR, bg="#0d1a0d")
        label_solde.grid(row=3+idx*3, column=0, columnspan=2, pady=2)
        liste_labels_solde.append(label_solde)

        champ_saisie = tk.Entry(cadre_mises, font=(NOM_POLICE, 13, "bold"), width=8,
                     bg="#050f05", fg=COULEUR_BLANC, insertbackground=COULEUR_OR,
                     relief=tk.FLAT, justify="center",
                     highlightthickness=1, highlightbackground=COULEUR_OR)
        champ_saisie.grid(row=3+idx*3, column=2, padx=10, pady=2)
        liste_champs_saisie.append(champ_saisie)

        cadre_mises_rapides = tk.Frame(cadre_mises, bg="#0d1a0d")
        cadre_mises_rapides.grid(row=4+idx*3, column=0, columnspan=4, pady=(2, 8))
        for montant in [10, 50, 100, 200]:
            bouton_rapide = tk.Button(cadre_mises_rapides, text=f"{montant}€",
                          command=lambda mm=montant, cc=champ_saisie: (cc.delete(0, tk.END), cc.insert(0, str(mm))),
                          font=(NOM_POLICE, 9, "bold"), bg="#1a2a0d", fg=COULEUR_OR,
                          activebackground="#2a3a1a", relief=tk.FLAT, cursor="hand2",
                          padx=7, pady=2)
            bouton_rapide.pack(side=tk.LEFT, padx=3)

    label_erreur = tk.Label(cadre_mises, text="", font=(NOM_POLICE, 10), fg=COULEUR_ROUGE, bg="#0d1a0d")
    label_erreur.grid(row=9, column=0, columnspan=4)

    def valider_les_mises():
        saisie_valide = True
        for idx in range(2):
            try:
                montant_mise = int(liste_champs_saisie[idx].get())
                if 0 < montant_mise <= solde_joueurs[idx]:
                    mises_joueurs[idx].set(montant_mise)
                else:
                    label_erreur.config(text=f"Mise invalide pour {noms_joueurs[idx]} (max {solde_joueurs[idx]} €)")
                    saisie_valide = False
                    break
            except Exception:
                label_erreur.config(text=f"Entrez un nombre valide pour {noms_joueurs[idx]}")
                saisie_valide = False
                break
        if saisie_valide:
            cadre_mises.place_forget()
            demarrer_tour_joueur1()

    btn_valider_mises = tk.Button(cadre_mises, text="VALIDER LES MISES  ▶",
                                  command=valider_les_mises,
                                  font=(NOM_POLICE, 13, "bold"),
                                  bg=COULEUR_OR, fg=COULEUR_FOND,
                                  activebackground=COULEUR_OR2,
                                  relief=tk.FLAT, cursor="hand2",
                                  padx=14, pady=7)
    btn_valider_mises.grid(row=10, column=0, columnspan=4, pady=(4, 18))

    def demarrer_tour_joueur1():
        phase_actuelle[0] = 1
        mettre_a_jour_label_tour("Tour de  JOUEUR 1  →  TIRER ou RESTER", COULEUR_VERT)
        btn_tirer_joueur1.config(state=tk.NORMAL)
        btn_rester_joueur1.config(state=tk.NORMAL)
        actualiser_affichage()

    def tirer_carte_joueur(idx):
        liste_mains[idx].append(paquet_cartes.pop())
        actualiser_affichage()
        if calculer_valeur_main(liste_mains[idx]) > 21:
            tour_termine[idx] = True
            if idx == 0:
                mettre_a_jour_label_tour(f"Joueur 1 BUST ! — Tour de  JOUEUR 2", COULEUR_ROUGE)
                btn_tirer_joueur1.config(state=tk.DISABLED)
                btn_rester_joueur1.config(state=tk.DISABLED)
                demarrer_tour_joueur2()
            else:
                btn_tirer_joueur2.config(state=tk.DISABLED)
                btn_rester_joueur2.config(state=tk.DISABLED)
                jouer_tour_croupier()

    def rester_joueur(idx):
        tour_termine[idx] = True
        if idx == 0:
            btn_tirer_joueur1.config(state=tk.DISABLED)
            btn_rester_joueur1.config(state=tk.DISABLED)
            demarrer_tour_joueur2()
        else:
            btn_tirer_joueur2.config(state=tk.DISABLED)
            btn_rester_joueur2.config(state=tk.DISABLED)
            jouer_tour_croupier()

    def demarrer_tour_joueur2():
        phase_actuelle[0] = 2
        mettre_a_jour_label_tour("Tour de  JOUEUR 2  →  TIRER ou RESTER", COULEUR_BLEU2)
        btn_tirer_joueur2.config(state=tk.NORMAL)
        btn_rester_joueur2.config(state=tk.NORMAL)

    def jouer_tour_croupier():
        phase_actuelle[0] = 3
        mettre_a_jour_label_tour("", COULEUR_OR)
        while calculer_valeur_main(main_croupier) < 17:
            main_croupier.append(paquet_cartes.pop())
        actualiser_affichage(croupier_cache=False)
        calculer_et_afficher_resultats()

    def calculer_et_afficher_resultats():
        score_croupier = calculer_valeur_main(main_croupier)
        liste_messages = []
        for idx in range(2):
            score_joueur = calculer_valeur_main(liste_mains[idx])
            if score_joueur > 21:
                solde_joueurs[idx] -= mises_joueurs[idx].get()
                liste_messages.append(f"{noms_joueurs[idx]} : BUST 💥  (-{mises_joueurs[idx].get()} €)")
            elif score_croupier > 21 or score_joueur > score_croupier:
                solde_joueurs[idx] += mises_joueurs[idx].get()
                liste_messages.append(f"{noms_joueurs[idx]} : Gagne 🏆  (+{mises_joueurs[idx].get()} €)")
            elif score_joueur < score_croupier:
                solde_joueurs[idx] -= mises_joueurs[idx].get()
                liste_messages.append(f"{noms_joueurs[idx]} : Perd 😔  (-{mises_joueurs[idx].get()} €)")
            else:
                liste_messages.append(f"{noms_joueurs[idx]} : Égalité 🤝  (±0 €)")

        canvas_jeu.itemconfig(label_resultat,       text="═══  Résultats  ═══", fill=COULEUR_OR)
        canvas_jeu.itemconfig(label_resultat_ombre, text="═══  Résultats  ═══")

        cadre_resultats = tk.Frame(fenetre_multi, bg="#0d1a0d", highlightthickness=2, highlightbackground=COULEUR_OR)
        cadre_resultats.place(relx=0.5, rely=0.52, anchor="center", width=600, height=220)

        tk.Label(cadre_resultats, text="═══  Résultats  ═══", font=(NOM_POLICE, 16, "bold"),
                 fg=COULEUR_OR, bg="#0d1a0d").pack(pady=(16, 8))

        for idx, message in enumerate(liste_messages):
            couleur_msg = COULEUR_VERT if "Gagne" in message else (COULEUR_ROUGE if "BUST" in message or "Perd" in message else "#aaaaaa")
            tk.Label(cadre_resultats, text=message, font=(NOM_POLICE, 13, "bold"),
                     fg=couleur_msg, bg="#0d1a0d").pack(pady=3)

        tk.Label(cadre_resultats,
                 text=f"J1 : {solde_joueurs[0]} €    |    J2 : {solde_joueurs[1]} €",
                 font=(NOM_POLICE, 11), fg=COULEUR_OR, bg="#0d1a0d").pack(pady=(8, 4))

        btn_rejouer.config(state=tk.NORMAL)

    btn_tirer_joueur1.config(command=lambda: tirer_carte_joueur(0))
    btn_rester_joueur1.config(command=lambda: rester_joueur(0))
    btn_tirer_joueur2.config(command=lambda: tirer_carte_joueur(1))
    btn_rester_joueur2.config(command=lambda: rester_joueur(1))

    actualiser_affichage()
