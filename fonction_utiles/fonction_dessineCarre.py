#Fonction dessineCarre se dépace aux coordonnées indiquées, s'oriente et
#crée un carré qu'elle remplit
#peut dessiner des fenêtres...

def dessineCarre(x,y,cote=50,couleur='black'):
    aller(x,y,315)
    begin_fill()
    color(couleur)
    circle(cote,None,4)
    end_fill()
    seth(0)
    aller(x,y)
    
#exemple d'utilisation
#dessineCarre(30,40,15,'red')
#dessine un carré aux coordonnées (30,40) de côté 15 de couleur rouge
