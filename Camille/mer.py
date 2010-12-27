# mer :)

from turtle import *

# faire des vagues


def aller(x,y,angle=0):
    up()
    goto(x,y)
    down()
    seth(angle)

def dessineVague(x,y,hauteur,longueur):
    width(3)
    color('blue')
    aller(x+longueur,y)
    left(90)
    i=0
    while i<=longueur:
        circle(hauteur/2,180)
        left(180)
        circle(hauteur/2,-180)
        left(180)
        i=i+4*hauteur


dessineVague(0,70,40,20)

width(2)
color('red')
aller(120,70)
goto(0,70)
