# voiture :)

from turtle import *
speed(0)
def aller(x,y,angle=0):
    up()
    goto(x,y)
    down()
    seth(angle)


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
goto(-140,25)
goto(-165,35)

goto(-140,65)
goto(-80,75)
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

# arrangements

color('red')
aller(-150,44)
width(40)
goto(-140,44)
color('grey')
width(10)
aller(-175,35)
goto(-110,35)
aller(110,35)
goto(175,35)
color('white')
width(7)
aller(-155,55)
goto(-145,55)
color('orange')
width(5)
aller(140,57)
goto(155,57)


aller(500,500)

