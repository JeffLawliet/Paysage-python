# fleur

from turtle import *

def aller(x,y,angle=0):
    up()
    goto(x,y)
    down()
    seth(angle)


def dessineFleur():
    print("Vous allez dessiner une fleur")
    x=int(input("Abscisse du bout de la tige au sol: "))
    y=int(input("Ordonnée du bout de la tige au sol: "))
    haut=int(input("Hauteur de la fleur: "))
    diam=haut/12
    color('black')
    aller(x+(haut/24),y+(11*haut/12))
    left(100)
    circle(diam,220)
    i=1
    while i<=8:
        left(220)
        circle(diam,220)
        i=i+1
    color('yellow')
    begin_fill()
    aller(x+(diam/6)+(diam/8),y+(26*diam/3)+(diam/8))
    circle((2*diam/3),360)
    end_fill()
    color('green')
    width(2)
    aller(x-(diam/2),y+(22*diam/3))
    left(250)
    circle(haut+diam,20)
    left(180)
    begin_fill()
    circle(3*diam,100)
    left(90)
    circle(3*diam,90)
    end_fill()
    right(90)
    circle(haut+diam,15)
    
    


dessineFleur()

