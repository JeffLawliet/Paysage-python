# bizarrerie

def dessineVague5(x,y,hauteur,longueur):
    aller(x,y)
    width(3)
    color('blue')
    i=0
    while i<=longueur:
        circle(hauteur,-180)
        circle(2*hauteur,90)
        left(270)
        circle(3*hauteur,-80)
        i=i+hauteur


dessineVague5(200,0,60,1200)
aller(-100,0)
