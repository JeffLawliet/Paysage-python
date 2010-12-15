#Fonction dessineTriangle se déplace aux coordonnées indiquées, s'oriente, et
#crée un triangle équilatéral qu'elle remplit
#peut dessiner un toit

def dessineTriangle(x,y,cote=50,couleur="black"):
    begin_fill()
    color(couleur)
    aller(x,y,300)
    circle(cote,None,3)
    end_fill()
    seth(0)

#exemple d'utilisation :
#dessineTriangle(40,50,30,'yellow')
#dessine un triangle aux coordonnées (40,50) de côté 30 de couleur jaune
