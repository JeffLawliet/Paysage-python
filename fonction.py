from turtle import *
from math import *
from random import *
reset()
# fonction aller : se déplace en x,y et s'oriente vers angle
def aller(x,y,angle=0):
    up()
    goto(x,y)
    down()
    seth(angle)



    
#Fonction dessineCarre se dépace aux coordonnées indiquées, s'oriente et
#crée un carré, d'épaisseur choisie, qu'elle remplit
#peut dessiner des fenêtres...

def dessineCarre(x,y,cote=50,couleur='black',epaisseur=1):
    aller(x,y,315)
    width(epaisseur)
    begin_fill()
    color(couleur)
    circle(cote,None,4)
    end_fill()
    seth(0)
    aller(x,y)

#exemple d'utilisation
#dessineCarre(30,40,15,'red',2)
#dessine un carré aux coordonnées (30,40) de côté 15 de couleur rouge d'épaisseur 2


#Fonction dessineDemiCercle, se déplace au coordonnées indiquées, s'oriente et
#crée un demi cercle, d'épaisseur choisie, qu'elle remplit
def dessineDemiCercle(x,y,rayon,couleur='blue',orientation=0,epaisseur=1):
    width(epaisseur)
    aller(x,y,orientation)
    begin_fill()
    circle(rayon,180)
    end_fill()
    
#exemple d'utilisation
#dessineDemiCercle(30,-30,60,'grey',15,4)
#crée un demi cercle en (30;-30) de rayon 60 gris orienté de 15 degré en partant de l'est, d'épaisseur 3

    
#fonction dessineEtoile superpose un "+" et une "x" aux coordonnées indiquées
#le tout de couleur blanche
def dessineEtoile(taille):

    x = randint(-window_width()//2,window_width()//2)
    y = randint(-window_height()//2,window_height()//2)
    color('black')
    
    aller(x,y-taille,90)
    forward(2*taille)
    
    aller(x-taille,y,0)
    forward(2*taille)
    
    aller(x-taille,y+taille,315)
    forward(2*sqrt(2*(taille**2)))
    
    aller(x+taille,y+taille,225)
    forward(2*sqrt(2*(taille**2)))

#exemple d'utilisation
#dessineEtoile(3)
#dessine une étoile qui fait 6 pixels de long 


    
#fonction dessineFenetre, dessine des fenêtres tous les étages, en les remplissant.
def dessineFenetre(nbrFenetresEtages, nbrEtages, hauteurMaison, largeurMaison, x, y, couleur='blue', epaisseur=1):
    largeurFenetre = largeurMaison / (3*nbrFenetresEtages)
    intervalle = ((2*largeurMaison)//3)//(nbrFenetresEtages+1) #largeur innocupée par les fenêtres
    if nbrFenetresEtages > 1:
        
        for i in range(1,nbrEtages):
            aller(x,y+((i+1)*(hauteurMaison/nbrEtages))-(hauteurMaison/(3*nbrEtages)),0) #on se déplace à l'étage supérieur
        
            for j in range(0, nbrFenetresEtages):
                aller(xcor() + intervalle,ycor(),0) #on avance de la longueur d'un intervalle
                dessineCarre(xcor(),ycor(),largeurFenetre,couleur,epaisseur)  #on dessine un carré qu'on remplit aussitôt
                aller(xcor()+ largeurFenetre,ycor(),0) # on se décale de largeur fenetre
                
    elif nbrFenetresEtages == 1:
        
        if nbrEtages == 1:
            aller(x+(largeurMaison/6),y+(3*hauteurMaison/4),0)   # on se décale un petit peu
            dessineCarre(xcor(),ycor(),largeurFenetre,couleur,epaisseur) # on dessine la fenêtre
            
        else:
            for i in range(1,nbrEtages):
                aller(x+(largeurMaison/6),y+((i+1)*(hauteurMaison/nbrEtages))-(hauteurMaison/(3*nbrEtages)),0) # on se décale un peu
                dessineCarre(xcor(),ycor(),largeurFenetre,couleur,epaisseur)




#fonction dessineLune, dessine une lune aux coordonnées choisie
#de diamètre choisie et la remplie
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

#exemple d'utilisation
#dessineLune(90,1,-25)
#dessine une lune de 90 de diametre en (1;-25)


#fonction dessineMaison, utilise différents module pour créer une maison    
def dessineMaison():
    print("Où voulez-vous dessinez votre maison ?")
    print("Entrez les coordonnées du point bas-gauche de la maison : ")
    xMaison = lireEntierClavier("Le x de la maison : ",-window_width()/2,window_width()/2)
    yMaison = lireEntierClavier("Le y de la maison : ",-window_height()/2,window_height()/2)
    hauteurMaison = lireEntierClavier("Entrez la hauteur de la maison : ",1, window_height())
    largeurMaison = lireEntierClavier("Entrez la largeur de la maison : ",1, window_width())
    couleurMaison = input("Entrez la couleur de la maison (en hexadécimal ou en anglais) : ")
    epaisseurMaison = lireEntierClavier("L'épaisseur du trait de la maison (entre 1 et 5) : ",1, 5)
    dessineRectangle(xMaison, yMaison, largeurMaison, hauteurMaison, couleurMaison, epaisseurMaison)

    toit = input("Voulez-vous un toit (Oui/Non) : ")
    while toit != ('Non' and 'non' and 'Oui' and 'oui'):
        print("Veuillez recommencer.")
        toit = input("Voulez-vous un toit (Oui/Non) : ")
    if toit == 'Oui' or toit == 'oui':
        couleurToit = input("Entrez la couleur de votre toit (en hexadécimal ou en anglais) : ")
        dessineTriangle(xMaison, yMaison+hauteurMaison, largeurMaison, couleurToit, epaisseurMaison)
        
    nbrEtagesMaison = lireEntierClavier("Entrez le nombre d'étages (entre 1 et 10) : ", 1, 10)
    couleurEtages = input("Entrez la couleur de l'étage (en hexadécimal ou en anglais) : ")
    for i in range(1,nbrEtagesMaison):
        
        aller(xMaison,yMaison+i*(hauteurMaison/nbrEtagesMaison),0)
        dessineTrait(xcor(), ycor(), largeurMaison, 0, couleurEtages, epaisseurMaison)

    xPorte = xMaison + (2*largeurMaison)/5
    largeurPorte = largeurMaison/3
    hauteurPorte = 2*hauteurMaison/(3*nbrEtagesMaison)
    couleurPorte = input("Entrez la couleur de votre porte (en hexadécimal ou en anglais) : ")
    dessineRectangle(xPorte, yMaison, largeurPorte, hauteurPorte, couleurPorte, epaisseurMaison)

    nbrFenetresEtagesMaison = lireEntierClavier("Entrez le nombre de fenêtre par étages de votre maison (entre 1 et 10) : ", 1, 10)
    couleurFenetresMaison = input("Entrez la couleur des fenêtres de votre maison (en hexadécimal ou en anglais) : ")
    dessineFenetre(nbrFenetresEtagesMaison,nbrEtagesMaison,hauteurMaison,largeurMaison, xMaison, yMaison, couleurFenetresMaison, epaisseurMaison)



#fonction dessineNuage, crée un nuage à la position indiquée.
def dessineNuage(x,y,rayon,couleur):
    dessineRectangle(x,y,rayon,rayon/2,couleur)

    for i in range(0,4):
        dessineDemiCercle(x,y,rayon,couleur,270)


    for i in range(0,2):
        dessineDemiCercle(x,y,rayon,couleur,0)
        
    for i in range(0,4):
        dessineDemiCercle(x,y,rayon,couleur,90)


    for i in range(0,2):
        dessineDemiCercle(x,y,rayon,couleur,180)

#exemple d'utilisation
#dessineNuage(400,300,50,blue)
#dessine un nuage en (400;300) de rayon 50 et de couleur bleue

#Fonction dessineRectangle se déplace aux coordonnées indiquées, s'oriente, et
#crée un rectangle qu'elle remplit
#peut dessiner un batîment, une porte...
def dessineRectangle(x,y,largeur=180,hauteur=50,couleur='red',epaisseur=1):
    aller(x,y,0)
    width(epaisseur)
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


#fonction dessineTrait, dessine un trait épais.
def dessineTrait(x,y,deplacement=50,orientation=0,couleur='black',epaisseur=2):
    color(couleur)
    width(epaisseur)
    aller(x,y,orientation)
    forward(deplacement)


#Fonction dessineTriangle se déplace aux coordonnées indiquées, s'oriente, et
#crée un triangle équilatéral qu'elle remplit
#peut dessiner un toit
def dessineTriangle(x,y,cote=50,couleur="black",epaisseur=1):
    begin_fill()
    color(couleur)
    width(epaisseur)
    aller(x,y,0)
    for i in range(0,3):
        forward(cote)
        left(120)
    end_fill()
    seth(0)

#exemple d'utilisation :
#dessineTriangle(40,50,30,'yellow')
#dessine un triangle aux coordonnées (40,50) de côté 30 de couleur jaune



#fonction lireEntierClavier, permet de faire en sorte d'avoir un entier compris entre deux valeurs.
def lireEntierClavier(phrase, inferieur, superieur):
    valeur = inferieur - 1
    while valeur < inferieur or valeur > superieur:
            try:
                valeur = int(input(phrase))
            except ValueError:
                print("Veuillez recommencer.")
                valeur = inferieur - 1
    return valeur
