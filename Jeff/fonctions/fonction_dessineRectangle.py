#Fonction dessineRectangle se déplace aux coordonnées indiquées, s'oriente, et
#crée un rectangle qu'elle remplit
#peut dessiner un batîment, une porte...

def dessineRectangle(x,y,largeur=50,hauteur=80,couleur='#035b98'):
    aller(x,y,0)
    fill(True)
    color(couleur)
    for i in range(0,4):
        if i%2 == 0:
            forward(largeur)
        else:
            forward(hauteur)
        left(90)
    fill(False)
        
    aller(x,y,0)

#exemple d'utilisation
#dessineRectangle(20,25,40,30,'black')
#dessine un rectangle aux coordonnées (20;25) de largeur 40 et de hauteur 30
#de couleur noire
