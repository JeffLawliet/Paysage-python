#Programme qui dessine une bouée:
from turtle import *

def dessineBouée(x,y):
    up()
    goto(x,y)
    down()

    #Corps de la bouée
    begin_fill()
    color("OrangeRed")
    circle(100)
    end_fill()
    left(90)
    forward(40)
    right(90)
    begin_fill()
    color("white")
    circle(60)
    end_fill()

    #Bandes grises

    for i in range(0,28):
        up()
        circle(60,i)
        if i==8 or i==15 or i==20 or i==24:
            down()
            right(90)
            begin_fill()
            color("Gray")
            forward(40)
            left(90)
            circle(100,20)
            left(90)
            forward(40)
            left(72)
            circle(60,20)
            end_fill()
            right(202)
            

dessineBouée(0,0)
