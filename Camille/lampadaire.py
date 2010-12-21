# lampadaire

from turtle import *

up()
goto(-40,-350)
down()
bgcolor('#183152')

#création du bas du lampadaire
width(20)
goto(40,-350)
width(15)
up()
goto(-35,-340)
down()
goto(35,-340)
up()
goto(-20,-330)
down()
width(20)
goto(20,-330)
up()
goto(-30,-313)
down()
goto(30,-313)
#création du milieu
up()
goto(-20,-300)
down()
goto(20,-300)
up()
goto(-20,-290)
down()
goto(20,-290)
width(18)
up()
goto(-20,-280)
down()
goto(20,-280)
width(15)
begin_fill()
goto(0,-100)
goto(-20,-270)
end_fill()
width(10)
up()
goto(-8,-92)
down()
goto(8,-92)
up()
goto(-3,-85)
down()
width(8)
goto(3,-85)
up()
goto(-8,-78)
down()
width(10)
goto(8,-78)
up()
goto(0,-80)
down()
begin_fill()
width(5)
circle(20)
end_fill()
begin_fill()
up()
goto(-20,-60)
down()
goto(0,70)
goto(20,-60)
end_fill()
up()
goto(-8,60)
down()
width(10)
goto(8,60)
up()
goto(0,50)
down()
width(13)
goto(0,135)
up()
goto(-8,120)
down()
width(10)
goto(8,120)

#création du haut du lampadaire

begin_fill()
up()
goto(0,135)
down()
width(5)
goto(-10,135)
goto(-15,160)
goto(-10,170)
goto(10,170)
goto(15,160)
goto(10,135)
goto(0,135)
end_fill()
up()
goto(0,170)
down()
width(23)
goto(0,180)
width(15)
goto(-15,190)
goto(15,190)
goto(0,180)
width(23)
goto(0,210)
up()
goto(-10,215)
down()
begin_fill()
color('#FFF168')
width(6)
goto(-45,300)
goto(45,300)
goto(10,215)
end_fill()
color('black')
width(6)
goto(-10,215)
goto(-45,300)
goto(-50,290)
goto(-45,300)
goto(45,300)
goto(50,290)
goto(45,300)
goto(10,215)
width(5)
goto(0,215)
goto(0,300)
up()
goto(-10,215)
down()
begin_fill()
goto(0,235)
goto(10,215)
end_fill()

up()
goto(-40,305)
down()
width(15)
goto(40,305)

up()
goto(22,303)
left(50)
down()
begin_fill()
width(10)
circle(30,240)
end_fill()

up()
goto(-45,305)
down()
width(5)
begin_fill()
goto(-20,350)
goto(17,350)
goto(45,305)
goto(-45,305)
end_fill()

up()
goto(0,350)
down()
width(4)
goto(0,370)
up()
goto(-6,340)
down()
begin_fill()
goto(0,365)
goto(5,340)
goto(-6,340)
end_fill()


# création de la lune

up()
goto(-300,250)
down()
color('white')
begin_fill()
circle(100)
end_fill()
up()
goto(-250,250)
down()
color('#183152')
begin_fill()
circle(90)
end_fill()

# création des étoiles


def etoile(x,y):
    up()
    goto(x,y)
    down()
    color('#CCC6AD')
    width(1)
    goto(x+10,y+10)
    up()
    goto(x+5,y+10)
    down()
    goto(x+5,y)
    up()
    goto(x,y+10)
    down()
    goto(x+10,y)
    up()
    goto(x+10,y+5)
    down()
    goto(x,y+5)

etoile(170,300)
etoile(-200,250)
etoile(300,300)
etoile(-100,200)
etoile(150,200)
etoile(250,350)
etoile(270,110)
etoile(-150,330)



#au revoir la fléche

up()
goto(500,500)
down()

