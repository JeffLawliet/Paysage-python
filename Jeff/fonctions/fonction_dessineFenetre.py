#fonction dessineFenetre, dessine des fenêtres tous les étages, en les remplissant.
def dessineFenetre(nbrFenetresEtages, nbrEtages, hauteurMaison, largeurMaison, couleur, x, y):
    largeurFenetre = largeurMaison / (3*nbrFenetresEtages)
    intervalle = ((2*largeurMaison)//3)//(nbrFenetresEtages+1) #largeur innocupée par les fenêtres
    if nbrFenetresEtages > 1:
        
        for i in range(1,nbrEtages):
            aller(x,y+((i+1)*(hauteurMaison/nbrEtages))-(hauteurMaison/(3*nbrEtages)),0) #on se déplace à l'étage supérieur
        
            for j in range(0, nbrFenetresEtages):
                aller(xcor() + intervalle,ycor(),0) #on avance de la longueur d'un intervalle
                dessineCarre(xcor(),ycor(),largeurFenetre,couleur)  #on dessine un carré qu'on remplit aussitôt
                aller(xcor()+ largeurFenetre,ycor(),0) # on se décale de largeur fenetre
                
    elif nbrFenetresEtages == 1:
        
        if nbrEtages == 1:
            aller(x+(largeurMaison/6),y+(3*hauteurMaison/4),0)   # on se décale un petit peu
            dessineCarre(xcor(),ycor(),largeurFenetre,couleur) # on dessine la fenêtre
            
        else:
            for i in range(1,nbrEtages):
                aller(x+(largeurMaison/6),y+((i+1)*(hauteurMaison/nbrEtages))-(hauteurMaison/(3*nbrEtages)),0) # on se décale un peu
                dessineCarre(xcor(),ycor(),largeurFenetre,couleur)
