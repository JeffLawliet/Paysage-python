from turtle import *
from math import *
from random import *
LARGEUR_MAX = window_width()//2
LARGEUR_MIN = -window_width()//2
HAUTEUR_MAX = window_height()//2
HAUTEUR_MIN = -window_height()//2
reset()
speed(0)
bgcolor('white')

# fonction aller : se déplace en x,y et s'oriente vers angle
def aller(x,y,angle=0):
    up()
    goto(x,y)
    down()
    seth(angle)


def dessineRoute(x=0, y=0, lar=100, long=300, demander=0):
    if demander == 0:
        
        x=lireEntierClavier("x du point bas gauche du début de la route: ",LARGEUR_MIN, LARGEUR_MAX)
        y=lireEntierClavier("y du point bas gauche du début de la route: ", HAUTEUR_MIN, HAUTEUR_MAX)
        lar=lireEntierClavier("Largeur de la route (>50) : ",50, 2*HAUTEUR_MAX)
        long=lireEntierClavier("Longueur de la route (>100: ", 100, 2*LARGEUR_MAX)
    dessineRectangle(x,y,long,lar,'black',1)
    i = x
    k = 0
    up()
    while i<=x+long and (k+1)*25 + (k+1)*20 +10 <=long: 
        k += 1
        dessineTrait(i+10,y+lar/2,25,0,'white',5)
        i=i+45

def dessineVague1(x,y,hauteur,longueur):
    width(3)
    aller(x+longueur,y)
    left(90)
    i=0
    while i<=longueur:
        circle(hauteur/2,180)
        left(180)
        circle(hauteur/2,-180)
        left(180)
        i=i+4*hauteur
    # quelque soit la longueur, il fait au minimum une "vague"
    # pour plus, il faut taper au moins 4*hauteur


def dessineVague2(x,y,hauteur):
    color('blue')
    width(3)
    aller(x,y)
    left(90)
    circle(hauteur,180)
    aller(x,y,90)
    circle((3*hauteur)/4,190)
    aller(x,y,90)
    circle(hauteur/4,200)
    # dessine des vagues rondes vers la gauche


def dessineVague3(x,y,hauteur):
    color('blue')
    width(3)
    aller(x,y)
    left(90)
    circle(hauteur,100)
    circle(hauteur/10,160)
    left(180)
    circle((3*hauteur/5),-100)
    #dessine la forme d'une vague de tempéte vers la gauche


def dessineVague4(x,y,hauteur,longueur):
    width(3)
    aller(x,y)
    left(50)
    i=0
    while i<=longueur:
        circle(2*hauteur,-100)
        left(100)
        i=i+4*hauteur
    #dessine des vagues vers la gauche à partir de (x,y)
    # penser à multiplier la taille par 2 pour avoir celle que l'on veut
    # et longueur min 4* la hauteur qu'on indique


def dessineVague5(x,y,hauteur,longueur):
    aller(x,y)
    width(3)
    i=0
    while i<=longueur:
        left(50)
        circle(3*hauteur,-80)
        circle(hauteur,-180)
        circle(2*hauteur,90)
        left(122)
        i=i+6*hauteur
    # dessine des vagues façon aile de requin vers la gauche
    # penser à multiplier la longueur des vagues
    # attention à partir d'un certain nombre, les vagues "tombent"


def dessineMer(date = 'jour', tps = 'calme', demander = 0):
    if demander == 0:
            
        date=input("À quel moment de la journée sommes-nous? Jour ou nuit? : ")
        if date!="Jour" and date!="jour" and date!="Nuit" and date!="nuit":
            print("Veuillez recommencer")
            date=input("À quel moment de la journée sommes-nous? Jour ou nuit? : ")
        tps=input("Votre mer est-elle agitée ou calme? ")
        if tps!="agitée" and tps!="calme":
            print("Veuillez recommencer")
            tps=input("Votre mer est-elle agitée ou calme? ")
    if date=="Jour" or date=="jour":
        if tps=="agitée":
            couleur1='#132959'
        elif tps=="calme":
            couleur1='#006D80'
    elif date=="Nuit" or date=="nuit":
        if tps=="agitée":
            couleur1='#080830'
        elif tps=="calme":
            couleur1='#000050'
    color(couleur1)
    begin_fill()
    if tps=="agitée":
        dessineVague5(LARGEUR_MAX,0,30,2*LARGEUR_MAX+100)
        goto(LARGEUR_MIN,HAUTEUR_MIN)
        goto(LARGEUR_MAX,HAUTEUR_MIN)
        goto(LARGEUR_MAX,0)
        end_fill()
    if tps=="calme":
        dessineVague4(LARGEUR_MAX,0,20,3*LARGEUR_MAX)
    goto(LARGEUR_MIN,HAUTEUR_MIN)
    goto(LARGEUR_MAX,HAUTEUR_MIN)
    goto(LARGEUR_MAX,0)
    end_fill()
    a=randint(51,80)
    for i in range(50,a):
        x=randint(LARGEUR_MIN,LARGEUR_MAX)
        y=randint(HAUTEUR_MIN,-20)
        long=randint(80,150)
        if tps=="agitée":
            couleur2='#0000B0'
            color(couleur2)
            dessineVague4(x,y,20,long)
        if tps=="calme":
            couleur2='#9090FF'
            color(couleur2)
            dessineVague1(x,y,10,long)


def dessineVoiture(x=0, y=0, diam = 20, couleur = 'black', demander = 0):
    
    if demander == 0:
        
        x=lireEntierClavier("le x du centre de la roue : ", LARGEUR_MIN, LARGEUR_MAX)
        y=lireEntierClavier("le y du centre de la roue:", HAUTEUR_MIN, HAUTEUR_MAX)
        diam=lireEntierClavier("Diamètre de la roue (10-40) : ", 10, 40)
        couleur=lireCouleurClavier("Couleur de la voiture (en anglais ou en hexadécimal):")


    dessineRoue(x,y,diam)
    dessineRoue(x+(5*diam),y,diam)

    color(couleur)
    begin_fill()
    aller(x+(8*diam)+(diam/4),y+(5*diam/4))
    goto(x+(8*diam)-(diam/3),y+(3*diam/4))
    goto(x+(6*diam),y+(3*diam/4))
    goto(x+(6*diam)-(diam/3),y+(3*diam/2))
    goto(x+(4*diam)+(diam/3),y+(3*diam/2))
    goto(x+(4*diam),y+(3*diam/4))
    goto(x+diam,y+(3*diam/4))
    goto(x+(2*diam/3),y+(3*diam/2))
    goto(x-(2*diam/3),y+(3*diam/2))
    goto(x-diam,y+(3*diam/4))
    goto(x-2*diam,y+(3*diam/4))
    goto(x-3*diam,y+(3*diam/2))
    goto(x-(11*diam/4),y+(9*diam/4))
    goto(x,y+(17*diam/6))
    goto(x+(6*diam),y+(17*diam/6))
    goto(x+(29*diam/4),y+(5*diam/2))
    goto(x+(33*diam/4),y+(5*diam/4))
    end_fill()
    color('#ABC8E2')
    begin_fill()
    aller(x+(6*diam),y+(17*diam/6))
    goto(x+(5*diam),y+(23*diam/6))
    goto(x+(5*diam/4),y+(23*diam/6))
    goto(x,y+(17*diam/6))
    goto(x+(6*diam),y+(17*diam/6))
    end_fill()
    color(couleur)
    width(diam/10)
    aller(x+(6*diam),y+(17*diam/6))
    goto(x+(5*diam),y+(23*diam/6))
    goto(x+(5*diam/4),y+(23*diam/6))
    goto(x,y+(17*diam/6))
    goto(x+(6*diam),y+(17*diam/6))
    aller(x+(5*diam),y+(23*diam/6))
    goto(x+(16*diam/3),y+(17*diam/6))
    aller(x+(5*diam/4),y+(23*diam/6))
    goto(x+(diam),y+(17*diam/6))
    aller(x+(13*diam/4),y+(23*diam/6))
    goto(x+(13*diam/4),y+(17*diam/6))

    color(couleur)
    aller(x-(5*diam/2),y+(37*diam/24))
    width(52*diam/32)
    goto(x-2*diam,y+(37*diam/24))
    color('grey')
    width(diam/3)
    aller(x-(7*diam/2),y+(5*diam/4))
    goto(x-diam+(diam/8),y+(5*diam/4))
    aller(x+(6*diam)-(diam/8),y+(5*diam/4))
    goto(x+(8*diam)+(diam/4),y+(5*diam/4))
    color('yellow')
    width((diam/6)+1)
    aller(x-(5*diam/2)-(diam/6),y+(37*diam/24)+(diam/2))
    goto(x-2*diam,y+(37*diam/24)+(diam/2))
    color('orange')
    width(diam/6)
    aller(x+7*diam,y+(37*diam/24)+(diam/2)+1)
    goto(x+(7*diam)+(diam/2),y+(37*diam/24)+(diam/2)+1)
    
#Fonction dessineCarre se dépace aux coordonnées indiquées, s'oriente et
#crée un carré, d'épaisseur choisie, qu'elle remplit
#peut dessiner des fenêtres...

def dessineCarre(x,y,cote=50,couleur='black',epaisseur=1):
    aller(x,y,315)
    width(epaisseur)
    begin_fill()
    color(couleur)
    circle(cote,None,4)
    end_fill()
    seth(0)
    aller(x,y)

#exemple d'utilisation
#dessineCarre(30,40,15,'red',2)
#dessine un carré aux coordonnées (30,40) de côté 15 de couleur rouge d'épaisseur 2


def dessineRoue(x,y,diam=20):
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

#Fonction dessineDemiCercle, se déplace au coordonnées indiquées, s'oriente et
#crée un demi cercle, d'épaisseur choisie, qu'elle remplit
def dessineDemiCercle(x,y,rayon,couleur='blue',orientation=0,epaisseur=1):
    width(epaisseur)
    color(couleur)
    aller(x,y,orientation)
    begin_fill()
    circle(rayon,180)
    end_fill()
    
#exemple d'utilisation
#dessineDemiCercle(30,-30,60,'grey',15,4)
#crée un demi cercle en (30;-30) de rayon 60 gris orienté de 15 degré en partant de l'est, d'épaisseur 3

    
#fonction dessineEtoile superpose un "+" et une "x" aux coordonnées indiquées
#le tout de couleur blanche
def dessineEtoile(taille = 2, demander = 0):

    if demander == 0:

        taille = lireEntierClavier("Quelle taille pour votre étoile (1-5) : ", 1, 5)
        x = lireEntierClavier("Le x de votre étoile : ", LARGEUR_MIN, LARGEUR_MAX)
        y = lireEntierClavier("Le y de voter étoile : ", HAUTEUR_MIN, HAUTEUR_MAX)

    else:
        
        x = randint(LARGEUR_MIN,LARGEUR_MAX)
        y = randint(HAUTEUR_MIN,HAUTEUR_MAX)
    color('#fffbb4')
    
    aller(x,y-taille,90)
    forward(2*taille)
    
    aller(x-taille,y)
    forward(2*taille)
    
    aller(x-taille,y+taille,315)
    forward(2*sqrt(2*(taille**2)))
    
    aller(x+taille,y+taille,225)
    forward(2*sqrt(2*(taille**2)))

#exemple d'utilisation
#dessineEtoile()
#dessine une étoile qui fait 6 pixels de long 


    
#fonction dessineFenetre, dessine des fenêtres tous les étages, en les remplissant.
def dessineFenetre(nbrFenetresEtages, nbrEtages, hauteurMaison, largeurMaison, x, y, couleur='blue', epaisseur=1):
    largeurFenetre = largeurMaison / (3*nbrFenetresEtages)
    intervalle = ((2*largeurMaison)//3)//(nbrFenetresEtages+1) #largeur innocupée par les fenêtres
    if nbrFenetresEtages > 1:
        
        for i in range(1,nbrEtages):
            aller(x,y+((i+1)*(hauteurMaison/nbrEtages))-(hauteurMaison/(3*nbrEtages))) #on se déplace à l'étage supérieur
        
            for j in range(0, nbrFenetresEtages):
                aller(xcor() + intervalle,ycor()) #on avance de la longueur d'un intervalle
                dessineCarre(xcor(),ycor(),largeurFenetre,couleur,epaisseur)  #on dessine un carré qu'on remplit aussitôt
                aller(xcor()+ largeurFenetre,ycor()) # on se décale de largeur fenetre
                
    elif nbrFenetresEtages == 1:
        
        if nbrEtages == 1:
            aller(x+(largeurMaison/6),y+(3*hauteurMaison/4))   # on se décale un petit peu
            dessineCarre(xcor(),ycor(),largeurFenetre,couleur,epaisseur) # on dessine la fenêtre
            
        else:
            for i in range(1,nbrEtages):
                aller(x+(largeurMaison/6),y+((i+1)*(hauteurMaison/nbrEtages))-(hauteurMaison/(3*nbrEtages))) # on se décale un peu
                dessineCarre(xcor(),ycor(),largeurFenetre,couleur,epaisseur)

    


#fonction dessineLune, dessine une lune aux coordonnées choisie
#de diamètre choisie et la remplie
def dessineLune(xLune =0, yLune=0,diametre = 100, demander = 0):

    if demander == 0:
            
        xLune = lireEntierClavier("Entrez le x du centre gauche de la lune : ", LARGEUR_MIN, LARGEUR_MAX)
        yLune = lireEntierClavier("Entrez le y du centre gauche de la lune : ", HAUTEUR_MIN, HAUTEUR_MAX)
        diametre = lireEntierClavier("Entrez le diamètre de la lune (entre 50 et 200) : ",50, 200) 
    aller(xLune,yLune)
    
    begin_fill()
    color('#fffbb4')
    circle(diametre/2)
    end_fill()
    
    aller((27*diametre/50)+xLune,(27*diametre/50)+yLune,90)
    
    begin_fill()
    color('#001169')
    circle(diametre/3)
    end_fill()

#exemple d'utilisation
#dessineLune(90,1,-25)
#dessine une lune de 90 de diametre en (1;-25)

def dessineMaison(x=0,y=0,couleurMaison='red',couleurToit='black',couleurPorte='black', demander = 0,largeur = 130, hauteur=150):
    if demander == 0:
        x = lireEntierClavier("Le x du point bas gauche de la maison : ", LARGEUR_MIN, LARGEUR_MAX)
        y = lireEntierClavier("Le y du point bas gauche de la maison : ", HAUTEUR_MIN, HAUTEUR_MAX)
        couleurMaison = lireCouleurClavier("Entrez la couleur de la maison (en hexadécimal ou en anglais) : ")
        couleurPorte = lireCouleurClavier("Entrez la couleur de la porte (en hexadécimal ou en anglais) : ")
        couleurToit = lireCouleurClavier("Entrez la couleur du toit (en hexadécimal ou en anglais) : ")
        largeur = lireEntierClavier("Entrez la largeur de la maison (50-200) : ",50, 200)
        hauteur = lireEntierClavier("Entrez la hauteur de la maison (50-300) : ",50, 300)

    # Dessine le rectangle de la maison :
    aller(x,y)
    width(0)
    begin_fill()
    color(couleurMaison)
    for i in range(0,2):
        forward(largeur)
        left(90)
        forward(hauteur)
        left(90)
    end_fill()
    color("black")
    for i in range(0,2):
        forward(largeur)
        left(90)
        forward(hauteur)
        left(90)
    
    # Dessine le toit :
    up()
    goto(largeur+x,hauteur+y)
    down()
    begin_fill()
    color(couleurToit)
    longueurToit=largeur*acos(pi/4)
    left(135)
    forward(longueurToit)
    goto(x,hauteur+y)
    end_fill()

    # Dessine la porte :
    positionPorte=randint(1,3)
    largeurPorte=largeur/5
    hauteurPorte=hauteur/3
    if positionPorte==1:
        up()
        goto((largeur/3)-(largeurPorte/2)+x,y)
        down()
    elif positionPorte==2:
        up()
        goto((largeur/2)-(largeurPorte/2)+x,y)
        down()
    else:
        up()
        goto((2*largeur/3)-(largeurPorte/2)+x,y)
        down()
    begin_fill()
    color(couleurPorte)
    right(45)
    for k in range(0,2):
        forward(hauteurPorte)
        right(90)
        forward(largeurPorte)
        right(90)
    end_fill()
    color("black")
    for k in range(0,2):
        forward(hauteurPorte)
        right(90)
        forward(largeurPorte)
        right(90)

    # Dessine la poignée :
    if positionPorte==1:
        up()
        goto((largeur/3)+(4*largeurPorte/10)+x,y+(hauteurPorte/2))
        down()
    elif positionPorte==2:
        up()
        goto((largeur/2)+(2*largeurPorte/5)+x,y+(hauteurPorte/2))
        down()
    else:
        up()
        goto((2*largeur/3)+(2*largeurPorte/5)+x,y+(hauteurPorte/2))
        down()
    begin_fill()
    color("black")
    circle(largeurPorte/10)
    end_fill()

    # Dessine les fenetres :
        # Sur le toit:
    fenetreToit=randint(0,1)
    if fenetreToit==1:
        up()
        goto((19*largeur/30)+x,(11*hauteur/9)+y)
        down()
        begin_fill()
        color("DarkSlateGray")
        circle(largeur/9)
        end_fill()
        #Petite lucarne
        up()
        goto((613*largeur/1000)+x,(11*hauteur/9)+y)
        down()
        begin_fill()
        color("yellow")
        circle(largeur/11)
        end_fill()
        # Croix
        color("black")
        width(5)
        left(90)
        forward(2*largeur/11)
        goto((613*largeur/1000)-(largeur/11)+x,(11*hauteur/9)+y)
        right(90)
        forward(largeur/11)
        backward(2*largeur/11)

        # Sur la maison:
    up()
    goto((largeur/5)+x,(2*hauteur/3)+y)
    down()
    width(5)
    begin_fill()
    color("#E9FFE5")
    for j in range(0,4):
        forward(hauteur/6)
        right(90)
    end_fill()
    color("black")
    for j in range(0,4):
        forward(hauteur/6)
        right(90)
    forward(hauteur/12)
    right(90)
    forward(hauteur/6)
    backward(hauteur/12)
    right(90)
    forward(hauteur/12)
    backward(hauteur/6)
        
    up()
    goto((7*largeur/10)+x,(2*hauteur/3)+y)
    down()
    width(5)
    begin_fill()
    color("#E9FFE5")
    right(180)
    for j in range(0,4):
        forward(hauteur/6)
        right(90)
    end_fill()
    color("black")
    for j in range(0,4):
        forward(hauteur/6)
        right(90)
    forward(hauteur/12)
    right(90)
    forward(hauteur/6)
    backward(hauteur/12)
    right(90)
    forward(hauteur/12)
    backward(hauteur/6)

        #En fonction de la porte
    if positionPorte==1 or positionPorte==3:
        if positionPorte==1:
            up()
            goto((11*largeur/20)+x,hauteurPorte+y)
            down()
        else:
            up()
            goto(3*largeur/20+x,hauteurPorte+y)
            down()
        begin_fill()
        color("#E9FFE5")
        for k in range(0,2):
            forward(2*hauteurPorte/5)
            left(90)
            forward(largeur/3)
            left(90)
        end_fill()
        width(5)
        color("black")
        for k in range(0,2):
            forward(2*hauteurPorte/5)
            left(90)
            forward(largeur/3)
            left(90)
        forward(hauteurPorte/5)
        left(90)
        forward(largeur/3)
        backward(largeur/6)
        right(90)
        forward(hauteurPorte/5)
        backward(2*hauteurPorte/5)
    left(90)

#fonction dessineMaison, utilise différents module pour créer une maison    
def dessineMaison1(xMaison=0, yMaison=0, hauteurMaison=200, largeurMaison=70, couleurMaison='black', toit='oui', couleurToit='red', couleurPorte = 'red', nbrEtagesMaison=1, couleurEtages = 'blue', nbrFenetresEtagesMaison=2, couleurFenetresMaison=2, demander = 0):
    if demander == 0:
        
        print("Où voulez-vous dessinez votre maison ?")
        print("Entrez les coordonnées du point bas-gauche de la maison : ")
        xMaison = lireEntierClavier("Le x de la maison : ",LARGEUR_MIN,LARGEUR_MAX)
        yMaison = lireEntierClavier("Le y de la maison : ",HAUTEUR_MIN,HAUTEUR_MAX)
        hauteurMaison = lireEntierClavier("Entrez la hauteur de la maison (>80) : ",80, 2*HAUTEUR_MAX)
        largeurMaison = lireEntierClavier("Entrez la largeur de la maison (>80) : ",80, 2*LARGEUR_MAX)
        couleurMaison = lireCouleurClavier("Entrez la couleur de la maison (en hexadécimal ou en anglais) : ")
    dessineRectangle(xMaison, yMaison, largeurMaison, hauteurMaison, couleurMaison)

    if demander == 0:
        toit = input("Voulez-vous un toit (Oui/Non) : ")
        while toit != 'Non' and toit != 'non' and  toit != 'Oui' and toit != 'oui':
            print("Veuillez recommencer.")
            toit = input("Voulez-vous un toit (Oui/Non) : ")
    if toit == 'Oui' or toit == 'oui':
        if demander == 0:
            
            couleurToit = lireCouleurClavier("Entrez la couleur de votre toit (en hexadécimal ou en anglais) : ")
        dessineTriangle(xMaison, yMaison+hauteurMaison, largeurMaison, couleurToit)
    if demander == 0:
        
        nbrEtagesMaison = lireEntierClavier("Entrez le nombre d'étages (entre 1 et 10) : ", 1, 10)
        couleurEtages = lireCouleurClavier("Entrez la couleur de l'étage (en hexadécimal ou en anglais) : ")
    for i in range(1,nbrEtagesMaison):
        
        aller(xMaison,yMaison+i*(hauteurMaison/nbrEtagesMaison))
        dessineTrait(xcor(), ycor(), largeurMaison, 0, couleurEtages)

    xPorte = xMaison + (2*largeurMaison)/5
    largeurPorte = largeurMaison/3
    hauteurPorte = 2*hauteurMaison/(3*nbrEtagesMaison)
    if demander == 0:
        
        couleurPorte = input("Entrez la couleur de votre porte (en hexadécimal ou en anglais) : ")
    dessineRectangle(xPorte, yMaison, largeurPorte, hauteurPorte, couleurPorte)
    if demander == 0:
        nbrFenetresEtagesMaison = lireEntierClavier("Entrez le nombre de fenêtre par étages de votre maison (entre 1 et 10) : ", 1, 10)
        couleurFenetresMaison = input("Entrez la couleur des fenêtres de votre maison (en hexadécimal ou en anglais) : ")
    dessineFenetre(nbrFenetresEtagesMaison,nbrEtagesMaison,hauteurMaison,largeurMaison, xMaison, yMaison, couleurFenetresMaison)



#fonction dessineNuage, crée un nuage à la position indiquée.
def dessineNuage(x,y,rayon,couleur):
    dessineRectangle(x,y,rayon,rayon/2,couleur)

    for i in range(0,4):
        dessineDemiCercle(xcor(),ycor(),rayon/8,couleur,270)

    for i in range(0,2):
        dessineDemiCercle(xcor(),ycor(),rayon/8,couleur,0)
        
    for i in range(0,4):
        dessineDemiCercle(xcor(),ycor(),rayon/8,couleur,90)


    for i in range(0,2):
        dessineDemiCercle(xcor(),ycor(),rayon/8,couleur,180)

#exemple d'utilisation
#dessineNuage(400,300,50,blue)
#dessine un nuage en (400;300) de rayon 50 et de couleur bleue

#Fonction dessineRectangle se déplace aux coordonnées indiquées, s'oriente, et
#crée un rectangle qu'elle remplit
#peut dessiner un batîment, une porte...
def dessineRectangle(x,y,largeur=180,hauteur=50,couleur='red',epaisseur=1):
    aller(x,y)
    width(epaisseur)
    begin_fill()
    color(couleur)
    for i in range(0,4):
        if i%2 == 0:
            forward(largeur)
        else:
            forward(hauteur)
        left(90)
    end_fill() 
    aller(x,y)
#exemple d'utilisation
#dessineRectangle(20,25,40,30,'black')
#dessine un rectangle aux coordonnées (20;25) de largeur 40 et de hauteur 30
#de couleur noire


#fonction dessineTrait, dessine un trait épais.
def dessineTrait(x,y,deplacement=50,orientation=0,couleur='black',epaisseur=2):
    color(couleur)
    width(epaisseur)
    aller(x,y,orientation)
    forward(deplacement)


#Fonction dessineTriangle se déplace aux coordonnées indiquées, s'oriente, et
#crée un triangle équilatéral qu'elle remplit
#peut dessiner un toit
def dessineTriangle(x,y,cote=50,couleur="black",epaisseur=1):
    begin_fill()
    color(couleur)
    width(epaisseur)
    aller(x,y)
    for i in range(0,3):
        forward(cote)
        left(120)
    end_fill()
    seth(0)

#exemple d'utilisation :
#dessineTriangle(40,50,30,'yellow')
#dessine un triangle aux coordonnées (40,50) de côté 30 de couleur jaune


def dessineVoiture1(xVoiture = 0, yVoiture = 0, couleurVoiture = 'grey',diam = 20, demander = 0):

    if demander == 0:
            
        print("Où voulez-vous dessinez votre voiture ?")
        print("Entrez les coordonnées du point bas-gauche de la voiture : ")
        xVoiture = lireEntierClavier("Le x de la voiture : ",LARGEUR_MIN,LARGEUR_MAX)
        yVoiture = lireEntierClavier("Le y de la voiture : ",HAUTEUR_MIN,HAUTEUR_MAX)
        couleurVoiture = lireCouleurClavier("La couleur de la voiture (en hexadécimal ou en anglais) : ")
    aller(xVoiture+5, yVoiture)
    begin_fill()
    for i in range(0,8):
        if i%2 == 0:
            if i == 0 or i == 4:
                dessineTrait(xcor(), ycor(), 190, i*45, couleurVoiture, 2)
            elif i == 2 or i == 6:
                dessineTrait(xcor(), ycor(), 50, i*45, couleurVoiture, 2)
        elif i%2 == 1:
            dessineTrait(xcor(), ycor(), sqrt(50), i*45, couleurVoiture, 2)
    end_fill()
    


    
    dessineRoue(xVoiture+35,yVoiture-10,diam)
    dessineRoue(xVoiture+165,yVoiture-10,diam)

    begin_fill()
    dessineTrait(xVoiture+55, yVoiture+60, 50, 70, couleurVoiture, 2)
    goto(xcor(),yVoiture+60)
    ortho1 = xcor()
    end_fill()
    begin_fill()
    dessineTrait(xVoiture+160, yVoiture+60, 50, 110, couleurVoiture, 2)
    ortho2 = xcor()
    goto(xcor(),yVoiture+60)
    end_fill()
    begin_fill()
    dessineRectangle(ortho1,yVoiture +60, ortho2-ortho1, 50, couleurVoiture, 2)
    end_fill()

def dessineBouee(x= 0,y=0, demander = 0):

    if demander == 0:
        x = lireEntierClavier("Le x du point bas milieu de la bouée : ", LARGEUR_MIN, LARGEUR_MAX)
        y = lireEntierClavier("Le y du point bas milieu de la bouée : ", HAUTEUR_MIN, HAUTEUR_MAX)
        

    aller(x,y)

    #Corps de la bouée
    begin_fill()
    color("OrangeRed")
    circle(50)
    end_fill()
    seth(90)
    forward(20)
    seth(0)
    begin_fill()
    color("white")
    circle(30)
    end_fill()

    #Bandes grises

    for i in range(0,28):
        up()
        circle(30,i)
        if i==8 or i==15 or i==20 or i==24:
            down()
            right(90)
            begin_fill()
            color("Gray")
            forward(20)
            left(90)
            circle(50,20)
            left(90)
            forward(20)
            left(72)
            circle(30,20)
            end_fill()
            right(202)
            


def dessineDauphin(xDauphin =0, yDauphin = 0, demander = 0):

    if demander == 0:
        
        xDauphin = lireEntierClavier("Entrez le x du point bas droit du dauphin : ", LARGEUR_MIN, LARGEUR_MAX)
        yDauphin = lireEntierClavier("Entrez le y du point bas droit du dauphin : ", HAUTEUR_MIN, HAUTEUR_MAX)
    aller(xDauphin, yDauphin)
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
    color("black")
    aller(xDauphin-136,yDauphin+4.5)
    circle(4)
    goto(xDauphin-137,yDauphin+3)
    color("white")
    circle(0.5)
    up()




#fonction lireEntierClavier, permet de faire en sorte d'avoir un entier compris entre deux valeurs.
def lireEntierClavier(phrase, inferieur, superieur):
    valeur = inferieur - 1
    while valeur < inferieur or valeur > superieur:
            try:
                valeur = int(input(phrase))
            except ValueError:
                print("Veuillez recommencer.")
                valeur = inferieur - 1
    return valeur

def traitDeplacement(xDepart, yDepart, xArrivee, yArrivee, couleur='black', epaisseur=1):
    aller(xDepart,yDepart)
    width(epaisseur)
    color(couleur)
    goto(xArrivee,yArrivee)

def dessineLampadaire(xLampadaire = 0, yLampadaire = 0, couleurLamapdaire = 'black', demander = 0, allume = 0):

    if demander == 0:
            
        print("Où voulez-vous dessinez votre lampadaire ?")
        print("Entrez les coordonnées du point bas-gauche du lampadaire : ")
        xLampadaire = lireEntierClavier("Le x du lampadaire : ",LARGEUR_MIN,LARGEUR_MAX)
        yLampadaire = lireEntierClavier("Le y du lampadaire : ",HAUTEUR_MIN,HAUTEUR_MAX)
        couleurLampadaire = lireCouleurClavier("La couleur du lampadaire (en hexadécimal ou en anglais) : ")

    aller(xLampadaire, yLampadaire)
    if allumer == 0:
        lumiere = 'grey'
    else:
        lumiere = '#FFF168'
    #création du bas du lampadaire
    dessineTrait(xcor(), ycor(), 40, 0, couleurLampadaire, 10)
    dessineTrait(xcor()-35, ycor()+7, 30, 0, couleurLampadaire, 8)
    dessineTrait(xcor()-33, ycor()+5, 36, 0, couleurLampadaire, 10)
    dessineTrait(xcor()-28, ycor()+8, 20, 0, couleurLampadaire, 10)

    #création du milieu
    dessineTrait(xcor()-20, ycor()+5, 20, 0, couleurLampadaire, 10)
    dessineTrait(xcor()-20, ycor()+5, 20, 0, couleurLampadaire, 10)
    dessineTrait(xcor()-20, ycor()+5, 20, 0, couleurLampadaire, 9)
    begin_fill()
    traitDeplacement(xcor(),ycor(),xcor()-10,ycor()+90, couleurLampadaire, 8)
    traitDeplacement(xcor(),ycor(),xcor()-10,ycor()-85, couleurLampadaire, 8)
    end_fill()
    dessineTrait(xcor()+6, ycor()+90, 8, 0, couleurLampadaire, 5)
    dessineTrait(xcor()-6, ycor()+4, 4, 0, couleurLampadaire, 4)
    dessineTrait(xcor()-6, ycor()+2, 8, 0, couleurLampadaire, 5)
    aller(xcor()-4, ycor()+2)
    begin_fill()
    width(2)
    circle(10)
    end_fill()
    aller(xcor()-10,ycor()+6)
    begin_fill()
    traitDeplacement(xcor(), ycor(), xcor()+10, ycor()+66, couleurLampadaire, 2)
    traitDeplacement(xcor(), ycor(), xcor()+10, ycor()-66, couleurLampadaire, 2)
    end_fill()
    dessineTrait(xcor()-14, ycor()+70, 8, 0, couleurLampadaire, 4)
    dessineTrait(xcor()-4, ycor()-4, 62, 90, couleurLampadaire, 7)
    dessineTrait(xcor()-4, ycor()-3, 8, 0, couleurLampadaire, 5)

    #création du haut
    aller(xcor()-4, ycor()+5)
    begin_fill()
    traitDeplacement(xcor(), ycor(), xcor()-5, ycor() +5, couleurLampadaire, 3)
    traitDeplacement(xcor(), ycor(), xcor()-5, ycor() +15, couleurLampadaire, 3)
    traitDeplacement(xcor(), ycor(), xcor()+5, ycor() +10, couleurLampadaire, 3)
    traitDeplacement(xcor(), ycor(), xcor()+10, ycor(), couleurLampadaire, 3)
    traitDeplacement(xcor(), ycor(), xcor()+5, ycor() -10, couleurLampadaire, 3)
    traitDeplacement(xcor(), ycor(), xcor()-5, ycor() -15, couleurLampadaire, 3)
    traitDeplacement(xcor(), ycor(), xcor() -5, ycor() -5, couleurLampadaire,3)
    end_fill()
    dessineTrait(xcor(), ycor()+30, 10, 90, couleurLampadaire, 11)
    dessineTrait(xcor()-7, ycor()+10, 14, 0, couleurLampadaire, 7)
    traitDeplacement(xcor(), ycor(), xcor()-7, ycor()-10, couleurLampadaire, 7)
    dessineTrait(xcor(), ycor(), 35, 90, couleurLampadaire, 11)
    aller(xcor()-5, ycor()-5)
    begin_fill()
    traitDeplacement(xcor(), ycor(), xcor()-18, ycor()+ 50, lumiere, 3)
    traitDeplacement(xcor(), ycor(), xcor()+46, ycor(), lumiere, 3)
    traitDeplacement(xcor(), ycor(), xcor() -18, ycor() -50, lumiere, 3)
    end_fill()
    traitDeplacement(xcor()-9, ycor(), xcor()-27, ycor()+50, couleurLampadaire, 5)
    traitDeplacement(xcor(), ycor(), xcor()-2, ycor()-5, couleurLampadaire, 3)
    traitDeplacement(xcor(), ycor(), xcor()+2, ycor()+5, couleurLampadaire, 3)
    dessineTrait(xcor(), ycor(), 46, 0, couleurLampadaire, 3)
    traitDeplacement(xcor(), ycor(), xcor()+2, ycor()-5, couleurLampadaire,3)
    traitDeplacement(xcor(), ycor(), xcor()-2, ycor()+5, couleurLampadaire,3)
    traitDeplacement(xcor(), ycor(), xcor()-18, ycor()-50, couleurLampadaire, 5)
    dessineTrait(xcor(), ycor(), 5, 180, couleurLampadaire, 3)
    dessineTrait(xcor(), ycor(), 50, 90, couleurLampadaire, 3)
    aller(xcor()-5, ycor()-50)
    traitDeplacement(xcor(), ycor(), xcor()+5, ycor()+15, couleurLampadaire, 3)
    traitDeplacement(xcor(), ycor(), xcor()+5, ycor()-15, couleurLampadaire, 3)
    dessineTrait(xcor()-25, ycor()+52, 40, 0, couleurLampadaire, 7)
    aller(xcor()-9, ycor()-1, 50)
    begin_fill()
    width(5)
    circle(15,240)
    end_fill()


def dessineArbre(xArbre=0, yArbre=0, largArbre = 50, hautArbre = 300, demander = 0):

    if demander == 0:
        
        xArbre = lireEntierClavier("Entrez le x du point bas-gauche de l'arbre : ", LARGEUR_MIN, LARGEUR_MAX)
        yArbre = lireEntierClavier("Entrez le y du point bas-gauche de l'arbre : ", HAUTEUR_MIN, HAUTEUR_MAX)
        largArbre = lireEntierClavier("Entrez la largeur de l'arbre (10-50) : ", 10, 50)
        hautArbre = lireEntierClavier("Entrez la hauteur de l'arbre (100-400) : ",100, 400)

    dessineRectangle(xArbre, yArbre, largArbre, hautArbre-10, '#3D0000')

    begin_fill()
    traitDeplacement(xArbre + largArbre//2, yArbre + hautArbre + 40, xArbre -3*largArbre, yArbre + hautArbre//6, '#0B8426')
    dessineTrait(xcor(), ycor(), 7*largArbre, 0, '#0B8426')
    traitDeplacement(xcor(), ycor(), xArbre + (largArbre//2), yArbre + hautArbre + 40, '#0B8426')
    end_fill()
    
def dessineBateau():
    xBateau = lireEntierClavier("Entrez le x du point bas-gauche du bateau : ", LARGEUR_MIN, LARGEUR_MAX)
    yBateau = lireEntierClavier("Entrez le y du point bas-gauche du bateau : ", HAUTEUR_MIN, HAUTEUR_MAX)
    largBateau = lireEntierClavier("Entrez la largeur du bateau (100-400) : ", 100 , 400)
    hautBateau = lireEntierClavier("Entrez la hauteur du bateau (80-200) : ", 80, 200)

def dessineSoleil(xSoleil=0, ySoleil=0, rayon=50, demander=0):
    if demander ==0:
        
        xSoleil = lireEntierClavier("Entrez le x du point milieu-gauche du soleil : ", LARGEUR_MIN, LARGEUR_MAX)
        ySoleil = lireEntierClavier("Entrez le y du point milieu-gauche du soleil : ", HAUTEUR_MIN, HAUTEUR_MAX)
        rayon = lireEntierClavier("Entrez le rayon du soleil (25-100) : ", 25, 100)

    color('yellow')
    begin_fill()
    aller(xSoleil, ySoleil, 270)
    circle(rayon)
    end_fill()
    for i in range(0,8):
        aller(xSoleil + rayon, ySoleil)
        left(i*45)
        up()
        forward(rayon+10)
        down()
        forward(rayon/3)

def dessinePhare(x=0, y=0, demander = 0):

    if demander == 0:
        x = lireEntierClavier("Le x du point bas gauche du phare : ", LARGEUR_MIN, LARGEUR_MAX)
        y = lireEntierClavier("Le y du point bas gauche du phrase :", HAUTEUR_MIN, HAUTEUR_MAX)
    aller(x-50,y-200)
    
    # Base du phare:
    for i in range(0,5):
        if i%2==0:
            begin_fill()
            dessineRectangle(xcor(), ycor(), 135, 75, 'red')
            end_fill()
        elif i%2==1:
            begin_fill()
            dessineRectangle(xcor(), ycor(), 135, 75, 'white')
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
    forward(30)
    left(90)
    forward(10)
    right(90)
    forward(10)
    right(90)
    forward(25)
    right(90)
    for i in range(0,7):
        for k in range(0,2):
            forward(30)
            left(90)
            forward(15)
            left(90)
        right(90)
        backward(15)
        left(90)
    left(90)
    forward(25)
    right(90)
    forward(10)
    right(90)
    forward(10)
    left(90)
    forward(20)

    #Lumière du phare:
    up()
    backward(30)
    right(90)
    forward(20)
    down()
    left(180)
    begin_fill()
    circle(7,180)
    forward(95)
    circle(7,180)
    end_fill()
    forward(4)

    left(90)
    forward(60)
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


def lireCouleurClavier(phrase, couleur=0):
    securite = 1
    while securite == 1:
        try:
            chaine = input(phrase)
            securite = 0
            if couleur == 0: color(chaine)
            elif couleur == 1: bgcolor(chaine)
        except:
            securite = 1
    return(chaine)

