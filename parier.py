
# on met sa touten haut du fichier
argent_joueur = 1000  # par defaut j'ai mis 1000 euros

import tkinter as tk
import solo as sl

#Dans la fonction solo : 
global argent_joueur 
mise_actuelle = tk.IntVar(value=0) # On crée une boîte pour stocker la mise du tour

def valider_mise():
        global argent_joueur
        try:
            m = int(entree_mise.get()) # On lit le nombre écrit dans la case blanche quon a entrer 
            if 0 < m <= argent_joueur: # Si on as assez d'argent
                mise_actuelle.set(m)    # On enregistre la mise
                label_pari.config(text=f"Mise : {m}€", fg="#2ecc71") # On écrit en vert
                sl.btn_tirage.config(state="normal") # On ALLUME le bouton reprendre
                sl.btn_reste.config(state="normal")   # On ALLUME le bouton garder
                btn_valider.config(state="disabled") # On bloque le bouton MISER
            else:
                label_pari.config(text="Montant invalide", fg="#e74c3c") # Erreur en rouge
        except:
            label_pari.config(text="Entrez un nombre", fg="#e74c3c") # Si jamais on a écris des lettres
# encore dans solo :
    
    # Texte qui affiche notre argent total en haut à droite
label_argent = tk.Label(sl.fensolo, text=f"Argent : {argent_joueur}€", font=("Rockwell", 25), fg="white", bg="#142e14")
label_argent.place(relx=0.8, rely=0.05, anchor="center")

    # Case blanche pour taper le montant de la mise
entree_mise = tk.Entry(sl.fensolo, font=("Rockwell", 18))
entree_mise.place(relx=0.5, rely=0.75, anchor="center")
    
    # Bouton pour cliquer et valider la mise
btn_valider = tk.Button(sl.fensolo, text="MISER", command=valider_mise, bg="#52be8c", width=10)
btn_valider.place(relx=0.5, rely=0.82, anchor="center")

    #  texte qui nous demande d'entrer notre mise au-dessus de la case
label_pari = tk.Label(sl.fensolo, text="Entrez votre mise", font=("Rockwell", 15), fg="white", bg="#142e14")
label_pari.place(relx=0.5, rely=0.7, anchor="center")

# dans fin croupier() et rester()
    
    # Dans fin_croupier(), j'ai ajouté cette ligne pour rafraîchir l'affichage de notre argent
label_argent.config(text=f"Argent : {argent_joueur}€") 

    # Dans rester() just je calcule notre argent final genre soit gagne soit perdu :
sj, sc = sl.val_main(sl.joueur), sl.val_main(sl.croupier) # Les scores
    
if sj <= 21 and (sc > 21 or sj > sc):
    argent_joueur += mise_actuelle.get()*2 # On AJOUTE la mise si on gagnes
elif sj < sc or sj > 21:
    argent_joueur -= mise_actuelle.get() # On RETIRE la mise si on perds
    # Si égalité, on ne fait rien

