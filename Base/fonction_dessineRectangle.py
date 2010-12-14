from turtle import *


def dessineRectangle(x,y,largeur=50,hauteur=50,couleur='black',fond=None):
    aller(x,y,0)
    color(couleur)
    if fond != None:
        fill(True)
    for i in range(0,4):
        if i%2 == 0:
            forward(largeur)
        else:
            forward(hauteur)
        left(90)
    if fond != None:
        fill(False)
        
    aller(x,y,0)
