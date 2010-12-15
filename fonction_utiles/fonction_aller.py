# fonction aller : se déplace en x,y et s'oriente vers angle
def aller(x,y,angle):
    up()
    goto(x,y)
    down()
    seth(angle)
