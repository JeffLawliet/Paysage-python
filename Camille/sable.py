# sable :)

from turtle import *
from random import *

def aller(x,y,angle=0):
    up()
    goto(x,y)
    down()
    seth(angle)

def dessineVague(x,y,nb):
    aller(x,y)
    i=1
    while i<=nb:
        circle(200,-10)
        left(180)
        circle(200,20)
        left(180)
        circle(200,-10)
        left(180)
        circle(200,20)
        left(180)
        circle(200,-40)
        left(180)
        circle(200,20)
        left(180)
        i=i+1

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


def dessineSable():
    x=int(input("Abscisse du coin bas gauche de la plage: "))
    y=int(input("Ordonnée du coin bas gauche de la plage: "))
    long=int(input("Longueur de la plage: "))
    haut=int(input("Largeur de la plage: "))
    date=input("Fait-il jour ou nuit? ")
    if date!="jour" and date!="Jour" and date!="nuit" and date!="Nuit":
        print("Veuillez recommencer")
        date=input("Fait-il jour ou nuit?")
    if date=="jour" or date=="Jour":
        couleur1='#FAEC7F'
        couleur2='#A67E2E'
    if date=="Nuit" or date=="nuit":
        couleur1='#BF5C00'
        #couleur2='#BD8D46'
        couleur2 = 'black'
    dessineRectangle(x,y,long,haut,couleur1,1)
    color(couleur2)
    i=1
    y2=y+(haut-20)
    while i<=haut/40:
        dessineVague(x+long,y2,long/40)
        i=i+1
        y2=y2-40


dessineSable()
    
    
    

