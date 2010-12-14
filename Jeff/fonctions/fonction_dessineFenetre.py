def dessineFenetre(nbrFenetresEtages, nbrEtages, hauteurMaison, largeurMaison, largeurFenetre, couleur,x,y,fond=None):
    intervalle = ((2*largeurMaison)//3)//(nbrFenetresEtages+1)
    if nbrFenetresEtages > 1:
        
        for i in range(1,nbrEtages):
            aller(x,y+((i+1)*(hauteurMaison/nbrEtages))-(hauteurMaison/(3*nbrEtages)),0)
        
            for j in range(0, nbrFenetresEtages):
                aller(xcor() + intervalle,ycor(),0)
                if fond != None:
                    fill(True)
                    color(fond)
                dessineCarre(largeurFenetre,xcor(),ycor(),couleur)
                if fond != None:
                    fill(False)
                aller(xcor()+ largeurFenetre,ycor(),0)
    elif nbrFenetresEtages == 1:
        if nbrEtages == 1:
            aller(x+(largeurMaison/6),y+(3*hauteurMaison/4),0)
            dessineCarre(largeurMaison/3,xcor(),ycor(),couleur)
        else:
            for i in range(1,nbrEtages):
                aller(x+(largeurMaison/6),y+((i+1)*(hauteurMaison/nbrEtages))-(hauteurMaison/(3*nbrEtages)),0)
                dessineCarre(largeurFenetre,xcor(),ycor(),couleur)
