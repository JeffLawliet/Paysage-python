#######################################################
#         CiP1 - G3 : Filippi Jean-François           #
# Fichier : paysage.py, contient toutes les fonctions #
#      nécessaires à la construction d'un paysage     #
#######################################################


#On importe les modules nécessaires au fonctionnement
#des autres fonctions
from turtle import *                                    
from random import *                               
from math import *                                      

#module aller, lève le pinceau, se rend aux coordonnées reçues en argument,
#baisse le pinceau, oriente le pinceau à angle degré (sens trigonométrique)
def aller(x,y,angle):
    up()
    goto(x,y)
    down()
    seth(angle)

#module dessineRectangle, utilise module aller, transforme la couleur du trait
#construit un rectangle et revient aux coordonnées de départ.
def dessineRectangle(largeur,hauteur,x,y,couleur):
    aller(x,y,0)
    color(couleur)
    for i in range(0,4):
        if i%2 == 0:
            forward(largeur)
        else:
            forward(hauteur)
        left(90)
    aller(x,y,0)

#module dessineCarre, utilise module dessineRectangle avec comme argument largeur = hauteur = cote
def dessineCarre(cote,x,y,couleur):
    dessineRectangle(cote,cote,x,y,couleur)

#module dessineTriangle, utilise module aller, transforme la couleur du trait
#construit un triangle et revient aux coordonnées de départ
def dessineTriangle(cote,x,y,couleur):
    aller(x,y,0)
    color(couleur)
    for i in range(0,3):
        forward(cote)
        left(120)
    aller(x,y,0)

#module dessineLune, utilise le module aller. Remplit un cercle de rayon diametre/2 et le remplit. se déplace
#pour créer un deuxième cercle formant le croissant de lune. Réutilise le module aller pour revenir aux
#coordonnées de départ
def dessineLune(diametre,x,y):
    aller(x,y,0)
    begin_fill()
    color('#fffaa2')
    circle(diametre/2)
    end_fill()
    aller((27*diametre/50)+x,(27*diametre/50)+y,90)
    begin_fill()
    color('#06011d')
    circle(diametre/3)
    end_fill()
    aller(x,y,0)

#module dessineEtoile, utilise le module aller. Change la couleur du trait, déssine une étoile
def dessineEtoile(taille,x,y,nombre):
    color('white')
    aller(x,y-taille,90)
    forward(2*taille)
    aller(x-taille,y,0)
    forward(2*taille)
    aller(x-taille,y+taille,315)
    forward(2*sqrt(2*(taille**2)))
    aller(x+taille,y+taille,225)
    forward(2*sqrt(2*(taille**2)))
    
#module dessineEtage, change la couleur du trait, délimite les étages, retourne aux coordonnées de départs
def dessineEtage(hauteurMaison, largeurMaison, couleur, nbrEtages,x,y):

    color(couleur)
    for i in range(1,(nbrEtages)):
        
        aller(x,y+i*(hauteurMaison/nbrEtages),0)
        forward(largeurMaison)
    aller(x,y,0)
    
from random import *
#module dessineFenetre, change la couleur du trait, dessine les fenêtres.
def dessineFenetre(nbrFenetresEtages, nbrEtages, hauteurMaison, largeurMaison, largeurFenetre, couleur,x,y):
    intervalle = (largeurMaison - (largeurFenetre*nbrFenetresEtages))/(nbrFenetresEtages + 1 )
    if nbrFenetresEtages > 1:
        
        for i in range(1,nbrEtages):
            aller(x,y+((i+1)*(hauteurMaison/nbrEtages))-(hauteurMaison/(3*nbrEtages)),0)
        
            for j in range(0, nbrFenetresEtages):
                aller(xcor() + intervalle,ycor(),0)
                dessineCarre(largeurFenetre,xcor(),ycor(),couleur)
                aller(xcor()+ largeurFenetre,ycor(),0)
    elif nbrFenetresEtages == 1:
        if nbrEtages == 1:
            aller(x+(largeurMaison/6),y+(3*hauteurMaison/4),0)
            dessineCarre(largeurMaison/3,xcor(),ycor(),couleur)
        else:
            for i in range(1,nbrEtages):
                aller(x+(largeurMaison/6),y+((i+1)*(hauteurMaison/nbrEtages))-(hauteurMaison/(3*nbrEtages)),0)
                dessineCarre(largeurFenetre,xcor(),ycor(),couleur)

#module dessinePorte, change la couleur du trait, utilise le module aller et créer une porte, puis revient au coordonnées de départ.
def dessinePorte(x,y,hauteurPorte,largeurPorte, largeurMaison, couleur):
    dessineRectangle(largeurPorte, hauteurPorte,x+(largeurMaison/2),y, 'green')
    aller(x,y,0)
    
#module dessineBatiment, change la couleur du trait, utilise module aller et crée le contour du batiment et la porte, puis revient au coordonnées de départ.                
def dessineBatiment(hauteurMaison, largeurMaison,toit,x,y,couleur):
    dessineRectangle(largeurMaison,hauteurMaison,x,y,couleur)
    if toit:
        dessineTriangle(largeurMaison,x,y+hauteurMaison,couleur)
    aller(x,y,0)
hauteur = window_height()
largeur = window_width()


reset()

dessineBatiment(300,130,1,0,0,'black')
dessineEtage(300,130,'blue',4,0,0)
dessineFenetre(4,4,300,130,130/12,'red',0,0)

