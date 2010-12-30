# mer :)

from turtle import *
from random import *


# faire des vagues

def aller(x,y,angle=0):
    up()
    goto(x,y)
    down()
    seth(angle)

def dessineVague1(x,y,hauteur,longueur):
    width(3)
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



LARGEUR_MAX = window_width()//2
LARGEUR_MIN = -window_width()//2
HAUTEUR_MAX = window_height()//2
HAUTEUR_MIN = -window_height()//2

def dessineMer():
    print("Vous allez dessiné une mer")
    date=input("À quel moment de la journée sommes-nous? Jour ou nuit? : ")
    if date!="Jour" and date!="jour" and date!="Nuit" and date!="nuit":
        print("Veuillez recommencer")
        date=input("À quel moment de la journée sommes-nous? Jour ou nuit? : ")
    tps=input("Votre mer est-elle agitée ou calme? ")
    if tps!="agitée" and tps!="calme":
        print("Veuillez recommencer")
        tps=input("Votre mer est-elle agitée ou calme? ")
    if date=="Jour" or date=="jour":
        if tps=="agitée":
            couleur1='#132959'
        elif tps=="calme":
            couleur1='#006D80'
    elif date=="Nuit" or date=="nuit":
        if tps=="agitée":
            couleur1='#080830'
        elif tps=="calme":
            couleur1='#000050'
    color(couleur1)
    begin_fill()
    if tps=="agitée":
        dessineVague5(LARGEUR_MAX,0,30,2*LARGEUR_MAX+100)
        goto(LARGEUR_MIN,HAUTEUR_MIN)
        goto(LARGEUR_MAX,HAUTEUR_MIN)
        goto(LARGEUR_MAX,0)
        end_fill()
    if tps=="calme":
        dessineVague4(LARGEUR_MAX,0,20,3*LARGEUR_MAX)
    goto(LARGEUR_MIN,HAUTEUR_MIN)
    goto(LARGEUR_MAX,HAUTEUR_MIN)
    goto(LARGEUR_MAX,0)
    end_fill()
    a=randint(51,100)
    for i in range(50,a):
        x=randint(LARGEUR_MIN,LARGEUR_MAX)
        y=randint(HAUTEUR_MIN,-20)
        long=randint(80,200)
        if tps=="agitée":
            couleur2='#0000B0'
            color(couleur2)
            dessineVague4(x,y,20,long)
        if tps=="calme":
            couleur2='#9090FF'
            color(couleur2)
            dessineVague1(x,y,20,long)
            
    
dessineMer()

    
