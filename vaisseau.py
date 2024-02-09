class Vaisseau:

    def __init__(self,X_vaisseau, Y_vaisseau, canevas, img_vaisseau):
        self.X_vaisseau = X_vaisseau
        self.Y_vaisseau = Y_vaisseau
        self.canevas = canevas
        self.apparence = self.canevas.create_image(self.X_vaisseau, self.Y_vaisseau, anchor = "nw", image=img_vaisseau)
        
    def creation_vaisseau(self):
        self.canevas.coords(self.apparence, self.X_vaisseau, self.Y_vaisseau)
        
    
    def mouv_vaisseau(self, dir, largeur, largeur_vaisseau):
        if self.X_vaisseau >= 0 and dir == "l":
            self.X_vaisseau -= 10
    
        elif self.X_vaisseau<= largeur - largeur_vaisseau and dir == "r":
            self.X_vaisseau += 10
        self.creation_vaisseau()
