# mer :)

from turtle import *



# faire des vagues

def aller(x,y,angle=0):
    up()
    goto(x,y)
    down()
    seth(angle)

def dessineVague1(x,y,hauteur,longueur):
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
    # quelque soit la longueur, il fait au minimum une "vague"
    # pour plus, il faut taper au moins 4*hauteur


def dessineVague2(x,y,hauteur):
    color('blue')
    width(3)
    aller(x,y)
    left(90)
    circle(hauteur,180)
    aller(x,y,90)
    circle((3*hauteur)/4,190)
    aller(x,y,90)
    circle(hauteur/4,200)
    # dessine des vagues rondes vers la gauche


def dessineVague3(x,y,hauteur):
    color('blue')
    width(3)
    aller(x,y)
    left(90)
    circle(hauteur,100)
    circle(hauteur/10,160)
    left(180)
    circle((3*hauteur/5),-100)
    #dessine la forme d'une vague de tempéte vers la gauche


def dessineVague4(x,y,hauteur,longueur):
    color('blue')
    width(3)
    aller(x,y)
    left(50)
    i=0
    while i<=longueur:
        circle(2*hauteur,-100)
        left(100)
        i=i+4*hauteur
    #dessine des vagues vers la gauche à partir de (x,y)
    # penser à multiplier la taille par 2 pour avoir celle que l'on veut
    # et longueur min 4* la hauteur qu'on indique


def dessineVague5(x,y,hauteur,longueur):
    aller(x,y)
    width(3)
    color('blue')
    i=0
    while i<=longueur:
        left(50)
        circle(3*hauteur,-80)
        circle(hauteur,-180)
        circle(2*hauteur,90)
        left(122)
        i=i+6*hauteur
    # dessine des vagues façon aile de requin vers la gauche
    # penser à multiplier la longueur des vagues
    # attention à partir d'un certain nombre, les vagues "tombent"

dessineVague1(0,0,20,300)
dessineVague2(200,100,40)
dessineVague3(200,-300,30)
dessineVague4(-200,100,20,200)
dessineVague5(-200,-200,20,300)
