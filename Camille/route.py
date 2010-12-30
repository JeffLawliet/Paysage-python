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

def dessineRoute():
    print("Vous allez dessinez une route")
    x=int(input("Abscisse du point bas gauche du début de la route: "))
    y=int(input("Ordonné du point bas gauche du début de la route: "))
    lar=int(input("Largeur de la route ou point haut gauche du début de la route: "))
    long=int(input("Longueur de la route: "))
    dessineRectangle(x,y,long,lar,'black',1)
    i=x
    dessineTrait(x,y+lar/2,25,0,'white',5)
    while i<=x+long:
        dessineTrait(i+45,y+lar/2,25,0,'white',5)
        i=i+45

dessineRoute()
