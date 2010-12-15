from turtle import *
begin_fill()
reset()
speed(0)
for i in range(0,4):
    seth(90)
    begin_fill()
    circle(10,180)
    end_fill()
    seth(0)


for i in range(0,2):
    seth(180)
    begin_fill()
    circle(10,180)
    end_fill()

for i in range(0,4):
    seth(270)
    begin_fill()
    circle(10,180)
    end_fill()


for i in range(0,2):
    seth(0)
    begin_fill()
    circle(10,180)
    end_fill()

end_fill()
begin_fill()
up()
goto(200,200)
down()
goto(170,200)
goto(170,170)
end_fill()
