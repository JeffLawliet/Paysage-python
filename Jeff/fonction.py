from turtle import *
from math import *
from random import *


# fonction aller : se déplace en x,y et s'oriente vers angle
def aller(x,y,angle):
    up()
    goto(x,y)
    down()
    seth(angle)



    
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


 ##   
def dessineDemiCercle(x,y,rayon,couleur,orientation=0):
    aller(x,y,orientation)
    begin_fill()
    circle(rayon,180)
    end_fill()


    
#fonction dessineEtoile superpose un "+" et une "x" aux coordonnées indiquées
#le tout de couleur blanche
def dessineEtoile(taille):

    x = randint(-window_width()/2,window_width()/2)
    y = randint(-window_height()/2,window_height()/2)
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




##
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



###    
def dessineMaison():
    print("Où voulez-vous dessinez votre maison ?")
    
    print("Entrez les coordonnées du point bas-gauche de la maison : ",end="")
    xMaison = lireEntierClavier("Le x de la maison : ",+)
    yMaison = lireEntierClavier("Le y de la maison : ",+)
    largeurMaison = input("Entrez la hauteur de la maison : ",+)
    hauteurMaison = input("Entrez la largeur de la maison : ",+)
    couleurMaison = input("Entrez la couleur de la maison (en hexadécimal ou en anglais) : "))
    dessineRectangle(xMaison, yMaison, largeurMaison, hauteurMaison, couleurMaison)

    toit = input("Voulez-vous un toit (Oui/Non) : ")
    while toit != (Non or non or Oui or oui):
        print("Veuillez recommencer.")
        toit = input("Voulez-vous un toit (Oui/Non) : ")
    if toit = (Oui or oui):
        couleurToit = input("Entrez la couleur de votre toit : "))
        dessineTriangle(xMaison+hauteurMaison, yMaison, largeurMaison, couleurToit)
        
    nbrEtagesMaison = lireEntierClavier("Entrez le nombre d'étages : ",+)
    couleurEtages = lireStringClavier("Entrez la couleur de l'étage : ")
    for i in range(1,nbrEtages):
        
        aller(x,y+i*(hauteurMaison/nbrEtages),0)
        dessineTrait(xcor(), ycor(), largeurMaison, 0, couleurEtages)

    xPorte = xMaison + (2*largeurMaison)/5
    largeurPorte = largeurMaison/3
    hauteurPorte = 2*hauteurMaison/3*nbrEtagesMaison
    couleurPorte = input("Entrez la couleur de votre porte : ")
    dessineRectangle(xPorte, yPorte, largeurPorte, hauteurPorte, couleurPorte)

    nbrFenetresEtagesMaison = lireEntierClavier("Entrez le nombre de fenêtre par étages de votre maison : ",+)
    couleurFenetresMaison = input("Entrez la couleur des fenêtres de votre maison : ")
    dessineFenetre(nbrFenetresEtagesMaison,nbrEtagesMaison,hauteurMaison,largeurMaison, couleurFenetresMaison, xMaison, yMaison)

    

##
def dessineNuage(x,y,rayon,couleur)
    dessineRectangle(x,y,rayon,rayon/2,couleur)

    for i in range(0,4):
        dessineDemiCercle(x,y,rayon,couleur,270)


    for i in range(0,2):
        dessineDemiCercle(x,y,rayon,couleur,0)
        
    for i in range(0,4):
        dessineDemiCercle(x,y,rayon,couleur,90)


    for i in range(0,2):
        dessineDemiCercle(x,y,rayon,couleur,180)




#Fonction dessineRectangle se déplace aux coordonnées indiquées, s'oriente, et
#crée un rectangle qu'elle remplit
#peut dessiner un batîment, une porte...
def dessineRectangle(x,y,largeur,hauteur,couleur):
    aller(x,y,0)
    begin_fill()
    color(couleur)
    for i in range(0,4):
        if i%2 == 0:
            forward(largeur)
        else:
            forward(hauteur)
        left(90)
    end_fill()
        
    aller(x,y,0)

#exemple d'utilisation
#dessineRectangle(20,25,40,30,'black')
#dessine un rectangle aux coordonnées (20;25) de largeur 40 et de hauteur 30
#de couleur noire


##
def dessineTrait(x,y,deplacement,orientation,couleur):
    color(couleur)
    aller(x,y,orientation)
    forward(deplacement)



    
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



##
def lireEntierClavier(phrase,condition):
    valeur = None
    if condition == '+':
        valeur = -1

        while valeur == -1:
            try:
                valeur = int(input("Entrez un nombre : "))
            except ValueError:
                valeur = -1
        
    return valeur
    
