class Tir_invader:
    """Classe permettant de creer un tir des invaders"""
    cpt = 0

    def __init__(self, X_invader, Y_invader, canevas, mw, Tirs_invaders):
        self.cpt = Tir_invader.cpt
        self.X_tir_invader = X_invader
        self.Y_tir_invader = Y_invader
        self.Tirs_invaders = Tirs_invaders
        self.mw = mw
        self.canevas = canevas
        self.apparence = canevas.create_line(
            self.X_tir_invader, self.Y_tir_invader - 5, self.X_tir_invader, self.Y_tir_invader, fill="red")

    def creation_tir_invader(self):
        """Permet de créer le tir des invaders"""
        self.canevas.coords(self.apparence, self.X_tir_invader,
                            self.Y_tir_invader - 5, self.X_tir_invader, self.Y_tir_invader)

    def mouv_tir_invader(self):
        """Permet de déplacer le tir des invaders"""
        self.Y_tir_invader += 1
        self.creation_tir_invader()
        self.fin_tir_invader()
        self.mw.after(20, self.mouv_tir_invader)

    def fin_tir_invader(self):
        """Permet de supprimer le tir des invaders"""
        if self.Y_tir_invader > 480:
            self.cpt -= 1
            self.canevas.delete(self.apparence)
            del self.Tirs_invaders[0]
