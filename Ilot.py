class Ilot:
    cpt=0
    def __init__(self, canevas, largeur, Y_ilot):
        Ilot.cpt += 1
        self.Compteur = Ilot.cpt
        self.X_ilot = largeur * self.cpt / (6)
        self._Y_ilot = Y_ilot
        self.Resistance = 5
        self.canevas = canevas
        self.apparence = self.canevas.create_rectangle(self.X_ilot - 10, self._Y_ilot, self.X_ilot + 50, self._Y_ilot + 10, fill="black")
        
    def maj(self):
        self.Resistance -= 1
        if self.Resistance == 0:
          self.supp_ilot(self.canevas)
    
    def supp_ilot(self, canevas):
        canevas.delete(self.apparence)