# voiture :)

from turtle import *

def aller(x,y,angle=0):
    up()
    goto(x,y)
    down()
    seth(angle)

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

def dessineVoiture():
    print("Vous allez créer une voiture en fonction de la position et de la taille de la roue avant")
    x=int(input("Ordonnée du centre de la roue:"))
    y=int(input("Abscisse du centre de la roue:"))
    diam=int(input("Diamètre de la roue:"))
    couleur=input("Couleur de la voiture (en anglais ou en hexadécimal):")


    dessineRoue(x,y,diam)
    dessineRoue(x+(5*diam),y,diam)

    color(couleur)
    begin_fill()
    aller(x+(8*diam)+(diam/4),y+(5*diam/4))
    goto(x+(8*diam)-(diam/3),y+(3*diam/4))
    goto(x+(6*diam),y+(3*diam/4))
    goto(x+(6*diam)-(diam/3),y+(3*diam/2))
    goto(x+(4*diam)+(diam/3),y+(3*diam/2))
    goto(x+(4*diam),y+(3*diam/4))
    goto(x+diam,y+(3*diam/4))
    goto(x+(2*diam/3),y+(3*diam/2))
    goto(x-(2*diam/3),y+(3*diam/2))
    goto(x-diam,y+(3*diam/4))
    goto(x-2*diam,y+(3*diam/4))
    goto(x-3*diam,y+(3*diam/2))
    goto(x-(11*diam/4),y+(9*diam/4))
    goto(x,y+(17*diam/6))
    goto(x+(6*diam),y+(17*diam/6))
    goto(x+(29*diam/4),y+(5*diam/2))
    goto(x+(33*diam/4),y+(5*diam/4))
    end_fill()
    color('#ABC8E2')
    begin_fill()
    aller(x+(6*diam),y+(17*diam/6))
    goto(x+(5*diam),y+(23*diam/6))
    goto(x+(5*diam/4),y+(23*diam/6))
    goto(x,y+(17*diam/6))
    goto(x+(6*diam),y+(17*diam/6))
    end_fill()
    color('black')
    width(diam/10)
    aller(x+(6*diam),y+(17*diam/6))
    goto(x+(5*diam),y+(23*diam/6))
    goto(x+(5*diam/4),y+(23*diam/6))
    goto(x,y+(17*diam/6))
    goto(x+(6*diam),y+(17*diam/6))
    aller(x+(5*diam),y+(23*diam/6))
    goto(x+(16*diam/3),y+(17*diam/6))
    aller(x+(5*diam/4),y+(23*diam/6))
    goto(x+(diam),y+(17*diam/6))
    aller(x+(13*diam/4),y+(23*diam/6))
    goto(x+(13*diam/4),y+(17*diam/6))

    color(couleur)
    aller(x-(5*diam/2),y+(37*diam/24))
    width(52*diam/32)
    goto(x-2*diam,y+(37*diam/24))
    color('grey')
    width(diam/3)
    aller(x-(7*diam/2),y+(5*diam/4))
    goto(x-diam+(diam/8),y+(5*diam/4))
    aller(x+(6*diam)-(diam/8),y+(5*diam/4))
    goto(x+(8*diam)+(diam/4),y+(5*diam/4))
    color('yellow')
    width((diam/6)+1)
    aller(x-(5*diam/2)-(diam/6),y+(37*diam/24)+(diam/2))
    goto(x-2*diam,y+(37*diam/24)+(diam/2))
    color('orange')
    width(diam/6)
    aller(x+7*diam,y+(37*diam/24)+(diam/2)+1)
    goto(x+(7*diam)+(diam/2),y+(37*diam/24)+(diam/2)+1)


dessineVoiture()
aller(500,500)
