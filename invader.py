
class Invader:
    """
    Classe des invaders
    """
    cpt = 0

    def __init__(self, X_invader, Y_invader, canevas, img_invader, mw, dX,):

        Invader.cpt += 1
        self.cpt = Invader.cpt
        self.encours = True
        self.X_invader = X_invader
        self.Y_invader = Y_invader
        self.mw = mw
        self.dX = dX
        self.canevas = canevas
        self.apparence = self.canevas.create_image(
            self.X_invader, self.Y_invader, anchor="nw", image=img_invader)
        self.apparence_tir = canevas.create_line(
            self.X_invader, self.Y_invader - 5, self.X_invader, self.Y_invader, fill="black")

    def creation_invader(self):
        """
        Permet de créer les invaders
        """
        self.canevas.coords(self.apparence, self.X_invader, self.Y_invader)

    def mouv_invader_hor(self):
        """
        Permet de déplacer Horizontalement les Invaders et les faire rebondir sur les bors du canevas
        """

        if self.canevas.coords(self.apparence)[0] > 615:
            self.dX = -1 * self.dX
        if self.canevas.coords(self.apparence)[0] == 0:
            self.dX = -1 * self.dX

        self.canevas.move(self.apparence, self.dX, 0)
        self.mw.after(5, self.mouv_invader_hor)

    def mouv_invader_vert(self):
        """
        Permet de déplacer Verticalement les Invaders
        """
        self.canevas.move(self.apparence, 0, 0.5)
        self.mw.after(100, self.mouv_invader_vert)
