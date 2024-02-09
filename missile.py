
class Tir:
    """Classe permettant de creer un tir du vaisseau"""
    cpt = 0

    def __init__(self, canevas, img_missile, X_vaisseau, Y_vaisseau, mw, Tirs):
        """Constructeur de notre classe"""
        Tir.cpt += 1
        self.X_tir_vaisseau = X_vaisseau
        self.Y_tir_vaisseau = Y_vaisseau
        self.mw = mw
        self.Tirs = Tirs
        self.canevas = canevas
        self.apparence = self.canevas.create_image(
            self.X_tir_vaisseau, self.Y_tir_vaisseau, anchor="nw", image=img_missile)
        self.encours = True

    def creation_tir(self):
        """Permet de créer le tir du vaisseau à un nouvel endroit"""
        self.canevas.coords(
            self.apparence, self.X_tir_vaisseau + 16, self.Y_tir_vaisseau)

    def mouv_tir(self):
        """Permet de déplacer le tir du vaisseau"""
        if self.encours:
            self.Y_tir_vaisseau -= 1
            self.creation_tir()
            self.fin_tir_vaisseau()
            self.mw.after(5, self.mouv_tir)

    def fin_tir_vaisseau(self):
        """Permet de supprimer le tir du vaisseau"""
        if self.Y_tir_vaisseau < 0:
            self.encours = False
            Tir.cpt -= 1
            self.canevas.delete(self.apparence)
            del self.Tirs[0]
