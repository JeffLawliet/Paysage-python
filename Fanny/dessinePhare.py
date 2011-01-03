#Programme pour dessiner un phare:
from turtle import *

def dessinePhare(x,y):
    up()
    goto(x-50,y-200)
    down()
    # Base du phare:
    for i in range(0,5):
        if i%2==0:
            begin_fill()
            color("red")
        for k in range(0,2):
            forward(135)
            left(90)
            forward(75)
            left(90)
        end_fill()
        right(90)
        backward(75)
        left(90)
        
    #Haut du phare:
    begin_fill()
    color("black")
    forward(145)
    circle(5,180)
    forward(155)
    circle(5,180)
    end_fill()

    #Ballustrade:
    forward(10)
    left(90)
    forward(10)
    fillcolor("darkgrey")
    begin_fill()
    forward(20)
    left(90)
    forward(10)
    right(90)
    forward(10)
    right(90)
    forward(25)
    right(90)
    forward(30)
    right(90)
    forward(15)
    end_fill()
    backward(15)
    left(90)
    backward(30)
    for i in range(0,7):
        for k in range(0,2):
            fillcolor('darkgrey')
            begin_fill()
            forward(30)
            left(90)
            forward(15)
            left(90)
            end_fill()
        right(90)
        backward(15)
        left(90)
    begin_fill()
    left(90)
    forward(25)
    right(90)
    forward(10)
    right(90)
    forward(10)
    left(90)
    forward(20)
    right(90)
    forward(15)
    end_fill()
    color("black")
    right(90)
    forward(30)

    #Lumière du phare:
    right(90)
    backward(5)
    begin_fill()
    circle(7,180)
    forward(95)
    circle(7,180)
    end_fill()
    forward(4)

    #Coloration :
    left(90)
    forward(15)
    begin_fill()
    color("yellow")
    for i in range(0,2):
        forward(43)
        right(90)
        forward(88)
        right(90)
    end_fill()
    
    color("black")
    forward(43)
    left(180)
    for i in range(0,3):
        for k in range(0,2):
            forward(53)
            left(90)
            forward(88/3)
            left(90)
        right(90)
        backward(88/3)
        left(90)    

    #Dome du phare:
    left(90)
    forward(2)
    begin_fill()
    circle(7,180)
    forward(95)
    circle(7,180)
    end_fill()
    forward(92)
    left(90)
    forward(7)
    begin_fill()
    circle(44,180)
    end_fill()

    #Clocher du phare:
    left(90)
    forward(44)
    left(90)
    width(10)
    forward(60)
    right(90)
    circle(3)

    up()
    goto(200,0)
    down()

dessinePhare(0,0)
