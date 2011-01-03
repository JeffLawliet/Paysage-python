# paysage n°1

from turtle import *
setup(1280,1024)
from math import *
from random import *
LARGEUR_MAX = window_width()//2
LARGEUR_MIN = -window_width()//2
HAUTEUR_MAX = window_height()//2
HAUTEUR_MIN = -window_height()//2
reset()
speed(0)
bgcolor('#06011d')
ht()


#liste des fonctions utilisées

# fonction aller : se déplace en x,y et s'oriente vers angle
def aller(x,y,angle=0):
    up()
    goto(x,y)
    down()
    seth(angle)


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


def dessineVagueSable(x,y,nb):
    aller(x,y)
    i=1
    while i<=nb:
        circle(200,-5)
        left(180)
        circle(200,20)
        left(180)
        goto(xcor(), ycor())
        i=i+1

def dessineSable(x=0, y=0, long = 0, haut = 0, date = 'nuit', demander = 0):
    if demander == 0:
        
        x=lireEntierClavier("Abscisse du coin bas gauche de la plage : ", LARGEUR_MIN, LARGEUR_MAX)
        y=lireEntierClavier("Ordonnée du coin bas gauche de la plage : ", HAUTEUR_MIN, HAUTEUR_MAX)
        long=lireEntierClavier("Longueur de la plage : ", 0, LARGEUR_MAX*2)
        haut=lireEntierClavier("Largeur de la plage : ", 0, HAUTEUR_MAX*2)
        date=input("Fait-il jour ou nuit? ")
        if date!="jour" and date!="Jour" and date!="nuit" and date!="Nuit":
            print("Veuillez recommencer")
            date=input("Fait-il jour ou nuit?")
    if date=="jour" or date=="Jour":
        couleur1='#FAEC7F'
        couleur2='#A67E2E'
    if date=="Nuit" or date=="nuit":
        couleur1='#BF5C00'
        couleur2='#BD8D46'
    dessineRectangle(x,y,long,haut,couleur1)
    color(couleur2)
    i=1
    y2=y+(haut-20)
    while i<=haut/40:
        dessineVagueSable(x+long,y2,long/40)
        i=i+1
        y2=y2-40

        
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
        if tps=="agitée" or tps =='agitee':
            couleur1='#132959'
        elif tps=="calme":
            couleur1='#006D80'
    elif date=="Nuit" or date=="nuit":
        if tps=="agitée" or tps =='agitee':
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
    a=randint(61,80)
    for i in range(60,a):
        x=randint(LARGEUR_MIN,LARGEUR_MAX)
        y=randint(HAUTEUR_MIN,-100)
        long=randint(80,150)
        if tps=="agitée":
            couleur2='#0000B0'
            color(couleur2)
            dessineVague4(x,y,20,long)
        if tps=="calme":
            couleur2='#9090FF'
            color(couleur2)
            dessineVague1(x,y,10,long)

    
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
def dessineLune(xLune =0, yLune=0,diametre = 100, demander = 0, couleur ='dark blue'):

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
    color(couleur)
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
def dessineMaison1(xMaison=0, yMaison=0, hauteurMaison=200, largeurMaison=70, couleurMaison='black', couleurToit='red', couleurPorte = 'red', nbrEtagesMaison=1,demander=0,toit='oui',couleurEtages='black',nbrFenetresEtagesMaison=2,couleurFenetresMaison='brown'):
    dessineRectangle(xMaison, yMaison, largeurMaison, hauteurMaison, couleurMaison)
    if demander==0:
        toit = input("Voulez-vous un toit (Oui/Non) : ")
        while toit != 'Non' and toit != 'non' and  toit != 'Oui' and toit != 'oui':
            print("Veuillez recommencer.")
            toit = input("Voulez-vous un toit (Oui/Non) : ")
        if toit == 'Oui' or toit == 'oui':    
            couleurToit = lireCouleurClavier("Entrez la couleur de votre toit (en hexadécimal ou en anglais) : ")
            dessineTriangle(xMaison, yMaison+hauteurMaison, largeurMaison, couleurToit) 
        couleurEtages = lireCouleurClavier("Entrez la couleur de l'étage (en hexadécimal ou en anglais) : ")
        nbrFenetresEtagesMaison = lireEntierClavier("Entrez le nombre de fenêtre par étages de votre maison (entre 1 et 10) : ", 1, 10)
        couleurFenetresMaison = lireCouleurClavier("Entrez la couleur des fenêtres de votre maison (en hexadécimal ou en anglais) : ")
    if demander!=0:
        dessineTriangle(xMaison, yMaison+hauteurMaison, largeurMaison, couleurToit) 
    
    for i in range(1,nbrEtagesMaison):
        
        aller(xMaison,yMaison+i*(hauteurMaison/nbrEtagesMaison))
        dessineTrait(xcor(), ycor(), largeurMaison, 0, couleurEtages)

    xPorte = xMaison + (2*largeurMaison)/5
    largeurPorte = largeurMaison/3
    hauteurPorte = 2*hauteurMaison/(3*nbrEtagesMaison)
    dessineRectangle(xPorte, yMaison, largeurPorte, hauteurPorte, couleurPorte)
    dessineFenetre(nbrFenetresEtagesMaison,nbrEtagesMaison,hauteurMaison,largeurMaison, xMaison, yMaison, couleurFenetresMaison)
	


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




def dessinePhare(x=0, y=0, demander = 0):

    if demander == 0:
        x = lireEntierClavier("Le x du point bas gauche du phare : ", LARGEUR_MIN, LARGEUR_MAX)
        y = lireEntierClavier("Le y du point bas gauche du phrase :", HAUTEUR_MIN, HAUTEUR_MAX)
    aller(x-50,y-200)
    
    # Base du phare:
    for i in range(0,9):
        if i%2==0:
            begin_fill()
            dessineRectangle(xcor(), ycor(), 135, 70, 'red')
            end_fill()
        elif i%2==1:
            begin_fill()
            dessineRectangle(xcor(), ycor(), 135, 70, 'white')
        right(90)
        backward(70)
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



# dessin:

setup(1280,1024)

for i in range(100):
    dessineEtoile(2,1)

dessineLune(-500,200,250,1,'#06011d')

dessineMer('nuit','calme',1)

dessineSable(-250,-500,950,300,'nuit',1)

dessinePhare(-100,-150,1)


dessineMaison(50,-350,'#F6E497','#B9121B','#4C1B1B',1,550,250)
