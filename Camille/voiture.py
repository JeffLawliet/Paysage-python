# voiture :)

from turtle import *

def aller(x,y,angle=0):
    up()
    goto(x,y)
    down()
    seth(angle)


def dessineRectangle(x,y,largeur=180,hauteur=50,couleur='red',epaisseur=1):
    aller(x,y,0)
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
    aller(x,y,0)

# création des roues

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

dessineRoue(-80,0,30)
dessineRoue(80,0,30)

# création de la carrosserie

color('red')
begin_fill()
aller(170,35)
goto(160,25)
goto(110,25)
goto(100,45)
goto(60,45)
goto(50,25)
goto(-50,25)
goto(-60,45)
goto(-100,45)
goto(-110,25)
goto(-170,25)
goto(-180,55)
goto(-100,75)
goto(110,75)
goto(150,65)
goto(170,35)
end_fill()
color('blue')
begin_fill()
aller(110,75)
goto(70,100)
goto(-40,100)
goto(-80,75)
goto(110,75)
end_fill()
color('black')
width(3)
aller(110,75)
goto(70,100)
goto(-40,100)
goto(-80,75)
goto(110,75)
aller(70,100)
goto(90,75)
aller(-40,100)
goto(-60,75)
aller(15,100)
goto(15,75)

# arrangements ??
