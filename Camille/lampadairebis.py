# lampadaire 2 fois plus petit

from turtle import *

up()
goto(-20,-350)
down()

#création du bas du lampadaire
width(10)
goto(20,-350)
width(8)
up()
goto(-15,-343)
down()
goto(15,-343)
up()
goto(-18,-338)
down()
width(10)
goto(18,-338)
up()
goto(-10,-330)
down()
goto(10,-330)


#création du milieu
up()
goto(-10,-325)
down()
goto(10,-325)
up()
goto(-10,-320)
down()
goto(10,-320)
width(9)
up()
goto(-10,-315)
down()
goto(10,-315)
width(8)
begin_fill()
goto(0,-225)
goto(-10,-310)
end_fill()
width(5)
up()
goto(-4,-220)
down()
goto(4,-220)
up()
goto(-2,-216)
down()
width(4)
goto(2,-216)
up()
goto(-4,-214)
down()
width(5)
goto(4,-214)
up()
goto(0,-212)
down()
begin_fill()
width(2)
circle(10)
end_fill()
begin_fill()
up()
goto(-10,-206)
down()
goto(0,-140)
goto(10,-206)
end_fill()
up()
goto(-4,-140)
down()
width(4)
goto(4,-140)
up()
goto(0,-150)
down()
width(7)
goto(0,-88)   #ok modif jusqu'ici
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




#au revoir la fléche

up()
goto(500,500)
down()
