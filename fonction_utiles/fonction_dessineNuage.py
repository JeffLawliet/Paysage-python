from turtle import *

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

