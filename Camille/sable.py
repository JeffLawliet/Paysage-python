# sable :)

from turtle import *

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



aller(300,100)
left(160)
circle(500,40)
