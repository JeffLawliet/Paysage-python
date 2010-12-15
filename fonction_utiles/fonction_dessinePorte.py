def dessinePorte(x,y,hauteurPorte,largeurPorte, largeurMaison, couleur):
    dessineRectangle(largeurPorte, hauteurPorte,x+(largeurMaison/2),y, couleur)
    aller(x,y,0)
