from turtle import *

def dessineCarre(x,y,cote=50,couleur='black',fond=None):
    aller(x,y,315)
    color(couleur)
    if fond != None:
        fill(True)

    circle(cote,None,4)
    seth(0)
    
