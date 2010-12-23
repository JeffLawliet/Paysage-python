# voiture :)

from turtle import *

def aller(x,y,angle=0):
    up()
    goto(x,y)
    down()
    seth(angle)


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

# création des roues

def dessineRoue(x,y,diam):
    aller(x,y)
    color('black')
    begin_fill()
    circle(diam,360)
    end_fill()
    aller(x,y+(diam/3))
    color('white')
    begin_fill()
    circle((2*diam)/3,360)
    end_fill()
    aller(x,y+(3*diam/4))
    color('#B09F91')
    begin_fill()
    circle(diam/4,360)
    end_fill()

dessineRoue(-80,0,30)
dessineRoue(80,0,30)

# création de la carrosserie


