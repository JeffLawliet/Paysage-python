def dessineBatiment(hauteurMaison, largeurMaison,toit,x,y,couleur):
    dessineRectangle(largeurMaison,hauteurMaison,x,y,couleur)
    if toit:
        dessineTriangle(largeurMaison,x,y+hauteurMaison,couleur)
    aller(x,y,0)
