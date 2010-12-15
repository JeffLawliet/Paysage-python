#fonction dessineEtoile superpose un "+" et une "x" aux coordonnées indiquées
#le tout de couleur blanche

def dessineEtoile(taille,x,y):
    color('white')
    
    aller(x,y-taille,90)
    forward(2*taille)
    
    aller(x-taille,y,0)
    forward(2*taille)
    
    aller(x-taille,y+taille,315)
    forward(2*sqrt(2*(taille**2)))
    
    aller(x+taille,y+taille,225)
    forward(2*sqrt(2*(taille**2)))

#exemple d'utilisation
#dessineEtoile(3,20,40)
#dessine une étoile qui fait 6 pixels de long
