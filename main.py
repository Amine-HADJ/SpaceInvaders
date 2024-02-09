# -*- coding: utf-8 -*-


# HEADER
"""       
          PROJET SPACE INVADERS (DEV-LOG-PYTHON)
          15/01/2023
          HADJ-HAMDRI MOHAMMED-AMINE // TAHIRI EL_ALAOUI YOUNESS  //  3 ETI
          JEU SPACE INVADERS
"""


# Importation des modules nécessaires

import tkinter as tk
from random import choice


# Importation des differentes classes de nos objets

from vaisseau import Vaisseau
from Ilot import Ilot
from missile import Tir
from invader import Invader
from tir_invader import Tir_invader


# Canevas
mw = tk.Tk()
mw.title("Space_Invaders")

hauteur = 480
largeur = 640
canevas = tk.Canvas(mw, height=hauteur, width=largeur, bg="ivory")
canevas.grid(row=2, column=1, columnspan=2)
canevas.grid_remove()
canevas.focus_set()
img_fond = tk.PhotoImage(file="./img/fond.gif")
img_invader = tk.PhotoImage(file="./img/invader.gif")
img_vaisseau = tk.PhotoImage(file="./img/vaisseau.gif")
img_missile = tk.PhotoImage(file="./img/missile.gif")


# Score et Vies
score = tk.Label(mw, text="Score : 0")
score.grid(row=1, column=1)


vies = tk.Label(mw, text="Vies: 3")
vies.grid(row=1, column=2)

# Vaisseau

largeur_vaisseau = 50
hauteur_vaisseau = 50
X_vaisseau = (largeur - largeur_vaisseau) / 2
Y_vaisseau = hauteur - hauteur_vaisseau

# Invader
X_invader = 10
Y_invader = 30
dX = 1

invaders_ligne1 = []
invaders_ligne2 = []
invaders_ligne3 = []

# Ilots
Y_ilot = Y_vaisseau - 10

# Tir

Tirs = []
Tirs_invaders = []


etat_partie = True


def tir_invader():
    """
    Fonction qui génére les tirs des invarders de la première ligne
    """

    j = choice(invaders_ligne1)
    tir_invaders = Tir_invader(
        j.X_invader, j.Y_invader, canevas, mw, Tirs_invaders)
    tir_invaders.Tirs_invaders.append(tir_invaders)
    tir_invaders.Tirs_invaders[Tir_invader.cpt-1].mouv_tir_invader()
    mw.after(1500, tir_invader)
    tir_invaders.fin_tir_invader()


def nouvelle_partie():
    """
    Fonction principale du jeu qui créé les différents objets dans une nouvelle fenetre lorqu'on appuie sur le bouton "JOUER"
    """
    global vaisseau, ilot, tir_invader, invader, invader2, invader3, etat_partie

    if etat_partie == True:

        bouton_jouer.grid_remove()
        canevas.grid()
        canevas.create_image(0, 0, anchor="nw", image=img_fond)
        vaisseau = Vaisseau(X_vaisseau, Y_vaisseau, canevas, img_vaisseau)
        ilot = [Ilot(canevas, largeur, Y_ilot) for i in range(5)]

        # Création des 3 lignes d'invaders

        for i in range(15):
            invader = Invader(X_invader + i * 40, Y_invader,
                              canevas, img_invader, mw, dX)
            invaders_ligne1.append(invader)
            invader2 = Invader(X_invader + i * 40, Y_invader +
                               25, canevas, img_invader, mw, dX)
            invaders_ligne2.append(invader2)
            invader3 = Invader(X_invader + i * 40, Y_invader +
                               50, canevas, img_invader, mw, dX)
            invaders_ligne3.append(invader3)

        # Mouvement et Tir des Invaders
        for a in [invaders_ligne1, invaders_ligne2, invaders_ligne3]:
            if a != []:
                for i in range(len(a)):

                    a[i].mouv_invader_hor()
                    a[i].mouv_invader_vert()
            elif a[i].Y_invader > 420:
                etat_partie = False
        tir_invader()




def Clavier(clavier):
    """
    Fonction qui permet d'interagir et de jouer au jeu grâce au clavier

    """
    touche = clavier.keysym
    if touche == "Left":
        vaisseau.mouv_vaisseau("l", largeur, largeur_vaisseau)
        
    elif touche == "Right":
        vaisseau.mouv_vaisseau("r", largeur, largeur_vaisseau)
        
    elif touche == "space":
        tir = Tir(canevas, img_missile, vaisseau.X_vaisseau,
                  vaisseau.Y_vaisseau, mw, Tirs)
        tir.Tirs.append(tir)
        tir.Tirs[Tir.cpt-1].mouv_tir()


# Boutton Jouer
bouton_jouer = tk.Button(mw, text="Jouer", command=nouvelle_partie)
bouton_jouer.grid(row=0, column=1)


# Boutton quitter
bouton_quitter = tk.Button(mw, text="Quitter", command=mw.destroy)
bouton_quitter.grid(row=0, column=2)


# BARRE DE MENU
menu_bar = tk.Menu(mw)
mw.config(menu=menu_bar)
menu_fichier = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="MENU", menu=menu_fichier)
menu_fichier.add_command(label="Nouvelle partie", command=nouvelle_partie)
menu_fichier.add_command(label=" Quitter", command=mw.destroy)
menu_fichier.add_command(label="A propos")

# Association des touches de la fonction clavier à notre canevas
canevas.bind("<Key>", Clavier)


mw.mainloop()
