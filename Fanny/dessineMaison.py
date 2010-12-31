from math import *
from turtle import *
import random

def dessineMaison(x=0,y=0,couleurMaison,couleurToit,couleurPorte, largeur = 130, hauteur=150, demander = 0):
    if demander == 0:
        x = lireEntierClavier("Le x du point bas gauche de la maison : ", LARGEUR_MIN, LARGEUR_MAX)
        y = lireEntierClavier("Le y du point bas gauche de la maison : ", HAUTEUR_MIN, HAUTEUR_MAX)
        couleurMaison = lireCouleurClavier("Entrez la couleur de la maison (en hexadécimal ou en anglais) : ")
        couleurPorte
        couleurToit
        largeur =
        hauteur =
    # Dessine le rectangle de la maison :
    aller(x,y)
    width(0)
    begin_fill()
    color(couleurMaison)
    for i in range(0,2):
        forward(largeur)
        left(90)
        forward(hauteur)
        left(90)
    end_fill()
    color("black")
    for i in range(0,2):
        forward(largeur)
        left(90)
        forward(hauteur)
        left(90)
    
    # Dessine le toit :
    up()
    goto(largeur+x,hauteur+y)
    down()
    begin_fill()
    color(couleurToit)
    longueurToit=largeur*acos(pi/4)
    left(135)
    forward(longueurToit)
    goto(x,hauteur+y)
    end_fill()

    # Dessine la porte :
    positionPorte=random.randint(1,3)
    largeurPorte=largeur/5
    hauteurPorte=hauteur/3
    if positionPorte==1:
        up()
        goto((largeur/3)-(largeurPorte/2)+x,y)
        down()
    elif positionPorte==2:
        up()
        goto((largeur/2)-(largeurPorte/2)+x,y)
        down()
    else:
        up()
        goto((2*largeur/3)-(largeurPorte/2)+x,y)
        down()
    begin_fill()
    color(couleurPorte)
    right(45)
    for k in range(0,2):
        forward(hauteurPorte)
        right(90)
        forward(largeurPorte)
        right(90)
    end_fill()
    color("black")
    for k in range(0,2):
        forward(hauteurPorte)
        right(90)
        forward(largeurPorte)
        right(90)

    # Dessine la poignée :
    if positionPorte==1:
        up()
        goto((largeur/3)+(4*largeurPorte/10)+x,y+(hauteurPorte/2))
        down()
    elif positionPorte==2:
        up()
        goto((largeur/2)+(2*largeurPorte/5)+x,y+(hauteurPorte/2))
        down()
    else:
        up()
        goto((2*largeur/3)+(2*largeurPorte/5)+x,y+(hauteurPorte/2))
        down()
    begin_fill()
    color("black")
    circle(largeurPorte/10)
    end_fill()

    # Dessine les fenetres :
        # Sur le toit:
    fenetreToit=random.randint(0,1)
    if fenetreToit==1:
        up()
        goto((19*largeur/30)+x,(11*hauteur/9)+y)
        down()
        begin_fill()
        color("DarkSlateGray")
        circle(largeur/9)
        end_fill()
        #Petite lucarne
        up()
        goto((613*largeur/1000)+x,(11*hauteur/9)+y)
        down()
        begin_fill()
        color("yellow")
        circle(largeur/11)
        end_fill()
        # Croix
        color("black")
        width(5)
        left(90)
        forward(2*largeur/11)
        goto((613*largeur/1000)-(largeur/11)+x,(11*hauteur/9)+y)
        right(90)
        forward(largeur/11)
        backward(2*largeur/11)

        # Sur la maison:
    up()
    goto((largeur/5)+x,(2*hauteur/3)+y)
    down()
    width(5)
    begin_fill()
    color("#E9FFE5")
    for j in range(0,4):
        forward(hauteur/6)
        right(90)
    end_fill()
    color("black")
    for j in range(0,4):
        forward(hauteur/6)
        right(90)
    forward(hauteur/12)
    right(90)
    forward(hauteur/6)
    backward(hauteur/12)
    right(90)
    forward(hauteur/12)
    backward(hauteur/6)
        
    up()
    goto((7*largeur/10)+x,(2*hauteur/3)+y)
    down()
    width(5)
    begin_fill()
    color("#E9FFE5")
    right(180)
    for j in range(0,4):
        forward(hauteur/6)
        right(90)
    end_fill()
    color("black")
    for j in range(0,4):
        forward(hauteur/6)
        right(90)
    forward(hauteur/12)
    right(90)
    forward(hauteur/6)
    backward(hauteur/12)
    right(90)
    forward(hauteur/12)
    backward(hauteur/6)

        #En fonction de la porte
    if positionPorte==1 or positionPorte==3:
        if positionPorte==1:
            up()
            goto((11*largeur/20)+x,hauteurPorte+y)
            down()
        else:
            up()
            goto(3*largeur/20+x,hauteurPorte+y)
            down()
        begin_fill()
        color("#E9FFE5")
        for k in range(0,2):
            forward(2*hauteurPorte/5)
            left(90)
            forward(largeur/3)
            left(90)
        end_fill()
        width(5)
        color("black")
        for k in range(0,2):
            forward(2*hauteurPorte/5)
            left(90)
            forward(largeur/3)
            left(90)
        forward(hauteurPorte/5)
        left(90)
        forward(largeur/3)
        backward(largeur/6)
        right(90)
        forward(hauteurPorte/5)
        backward(2*hauteurPorte/5)
    left(90)

#Par exemple on peut obtenir :
dessineMaison(250,250,-600,"DarkGreen","red","DarkCyan")
dessineMaison(200,200,-300,"LightSeaGreen","black","red")
dessineMaison(300,300,0,"#ffd9d9","DimGray","blue")
