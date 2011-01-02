#Programme qui dessine des fleurs:
from turtle import *

def dessineFleur(x,y,couleur):
    up()
    goto(x,y)
    down()

    color("Green")
    width(3)
    left(90)
    forward(50)
    
    #Pétales:
    for i in range(0,7):
        color(couleur)
        circle(7)
        left(360/7)
    color("black")
    right(90)
    forward(0.15)
    if couleur=="black":
        color("yellow")
    else:
        color("black")
    begin_fill()
    circle(2)
    end_fill()


    #Feuille:
    up()
    goto(x,y)
    down()
    left(10)
    begin_fill()
    color("green")
    circle(30,50)
    left(120)
    circle(25,50)
    end_fill()

    up()
    goto(50,50)
    down()

dessineFleur(0,0,"red")
