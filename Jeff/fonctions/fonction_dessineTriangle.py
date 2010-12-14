from turtle import *

def dessineTriangle(x,y,cote=50,couleur="black",fond=None):
    color(couleur)
    aller(x,y,300)
    if fond != None:
        fill(True)
    circle(cote,None,3)
    if fond != None:
        fill(False)
    seth(0)
