#Programme qui dessine un dauphin:
from turtle import *

def dessineDauphin(x,y):
    up()
    goto(x,y)
    down()
    width(5)
    begin_fill()
    color("Gray")
    left(140)
    circle(125,90)

    #Dorsale:
    up()
    circle(125,-35)
    down()
    left(55)
    circle(40,-80)
    left(45)
    circle(40,38)
    
    
    up()
    right(72)
    circle(125,47)
    down()
    right(39)
    circle(75,20)
    right(45)
    circle(8,180)
    circle(75,30)
    right(35)
    circle(125,30)
    right(170)
    circle(200,-35)

    #Nageoire
    up()
    circle(200,35)
    down()
    left(110)
    circle(40,80)
    right(35)
    circle(40,-48)

    left(246)
    circle(200,-30)
    left(90)
    circle(150,20)
    left(125)
    circle(90,35)
    right(55)
    circle(90,40)
    left(125)
    circle(150,25)

    right(68)
    circle(400,8)
    end_fill()
    
    #Dessine un oeil
    up()
    color("black")
    goto(-136,4.5)
    down()
    circle(4)
    goto(-137,3)
    color("white")
    circle(0.5)
    up()
    goto(400,400)
dessineDauphin(0,0)
