# création d'une route

from turtle import *

def aller(x,y,angle=0):
    up()
    goto(x,y)
    down()
    seth(angle)

def dessineRectangle(x,y,largeur=180,hauteur=50,couleur='red',epaisseur=1):
    aller(x,y)
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
    aller(x,y)

def dessineTrait(x,y,deplacement=50,orientation=0,couleur='black',epaisseur=2):
    color(couleur)
    width(epaisseur)
    aller(x,y,orientation)
    forward(deplacement)

dessineRectangle(-100,0,180,50,'black',1)
dessineTrait(-100,25,25,0,'white',4)
dessineTrait(-55,25,25,0,'white',4)
dessineTrait(
