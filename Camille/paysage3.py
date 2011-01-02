#paysage n°3

# import des fonctions utiles

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
ht()							

def aller(x,y,angle=0):
    up()                          			
    goto(x,y)								    
    down()									  
    seth(angle)									  


def traitDeplacement(xDepart, yDepart, xArrivee, yArrivee, couleur='black', epaisseur=1):
    aller(xDepart,yDepart)						          
    width(epaisseur)			  					  
    color(couleur) 					  			  
    goto(xArrivee,yArrivee)      	  					  

def dessineTrait(x,y,deplacement=50,orientation=0,couleur='black',epaisseur=2):
    color(couleur)				
    width(epaisseur)				
    aller(x,y,orientation)			
    forward(deplacement)			
 	

def dessineCarre(x,y,cote=50,couleur='black',epaisseur=1):
    aller(x,y,315)	        
    width(epaisseur)		  
    begin_fill()		  
    color(couleur)            	  
    circle(cote,None,4)       	
    end_fill()			  
	

def dessineTriangle(x,y,cote=50,couleur="black",epaisseur=1):
    color(couleur)			
    width(epaisseur)		    
    aller(x,y)			    
    begin_fill()			
    for i in range(0,3):		
        forward(cote)		    
        left(120)			
    end_fill()				

def dessineRectangle(x,y,largeur=180,hauteur=50,couleur='red',epaisseur=1):
    aller(x,y)				
    width(epaisseur)			
    color(couleur)				
    begin_fill()		        
    for i in range(0,4):		
        if i%2 == 0:			
            forward(largeur)		
        else:			    
            forward(hauteur)		
        left(90)			
    end_fill() 				

def dessineDemiCercle(x,y,rayon,couleur='blue',orientation=0,epaisseur=1):
    width(epaisseur)            
    color(couleur)		
    aller(x,y,orientation)  	
    begin_fill()
    circle(rayon,180)           
    end_fill()

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
    a=randint(51,80)
    for i in range(50,a):
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

# fonction dessineBouee : dessine une bouée aux coordonnées indiquées ou demande les coordonnées à l'utilisateur.
# exemples d'utilisations : dessineBouee() : demande à l'utilisateur les coordonnées de la bouée
#                           dessineBoue(5,5,1) : dessine une bouée en (5;5)
def dessineBouee(x=0,y=0, demander=0):    
    if demander == 0:                                                                                   # si on demande à l'utilisateur
        x = lireEntierClavier("Le x du point bas milieu de la bouée : ", LARGEUR_MIN, LARGEUR_MAX)      # on récupère l'abscisse
        y = lireEntierClavier("Le y du point bas milieu de la bouée : ", HAUTEUR_MIN, HAUTEUR_MAX)      # on récupère l'ordonnée
        
    aller(x,y)              # on se déplace aux coordonnées de la bouée

    #Corps de la bouée
    begin_fill()                                # ce bout de code
    color("OrangeRed")                          #
    circle(50)                                  # dessine
    end_fill()                                  #
    seth(90)                                    # la bouée 
    forward(20)                                 #
    seth(0)                                     # en        
    begin_fill()                                #
    color("#BF5C00")                            # elle même
    circle(30)                                  #
    end_fill()                                  #

    #Bandes grises
    for i in range(0,28):                       # ce bout de code
        up()                                    #
        circle(30,i)                            # dessine
        if i==8 or i==15 or i==20 or i==24:     # 
            down()                              # quant
            right(90)                           #
            begin_fill()                        # à lui
            color("Gray")                       #
            forward(20)                         # les bandes
            left(90)                            #
            circle(50,20)                       # grises 
            left(90)                            #
            forward(20)                         # de 
            left(72)                            #
            circle(30,20)                       # la bouée
            end_fill()                          #
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

#######################################################

### CATÉGORIE : CIEL ###

# fonction dessineLune : dessine une lune aux coordonnées et taille choisies par l'utilisateur ou préchoisies. "couleur" représente la couleur de background
# exemples d'utilisation : dessineLune() : demande à l'utilisateur les informations pour placer la lune
#                          dessineLune(diametre = 160, demander = 1, couleur = 'grey') : crée une lune en (0;0) de diamètre 160, sur un fond d'écran gris
def dessineLune(xLune =0, yLune=0,diametre = 100, demander = 0, couleur ='dark blue'):

    if demander == 0:                                                                                       # si on demande à l'utilisateur
        xLune = lireEntierClavier("Entrez le x du centre gauche de la lune : ", LARGEUR_MIN, LARGEUR_MAX)   # on récupère l'abscisse
        yLune = lireEntierClavier("Entrez le y du centre gauche de la lune : ", HAUTEUR_MIN, HAUTEUR_MAX)   # on récupère l'ordonnée
        diametre = lireEntierClavier("Entrez le diamètre de la lune (entre 50 et 200) : ",50, 200)          # on récupère le diamètre
        couleur = lireCouleurClavier("Entrez la couleur de fond où sera superposée la lune : ")
    aller(xLune,yLune)                                                                                      # on se déplace aux coordonnées de la lune
    
    begin_fill()                                                # on commence le remplissage
    color('#fffbb4')                                            # couleur de la lune
    circle(diametre/2)                                          # cercle de rayon pour la lune
    end_fill()                                                  # on termine le remplissage
    
    aller((27*diametre/50)+xLune,(27*diametre/50)+yLune,90)     # on se déplace dans la lune
    
    begin_fill()                                                # on commence un deuxieme remplissage
    color(couleur)                                              # on choisit la même couleur que le fond d'écran
    circle(diametre/3)                                          # on trace un cercle pour le croissant de lune
    end_fill()                                                  # on termine le remplissage
    
# fonction dessineNuage, crée un nuage de couleur et taille préchoisies à la position indiquée ou demander à l'utilisateur de les rentrer
# exemples d'utilisation : dessineNuage() : crée un nuage de rayon 100 en (0;0)
#                          dessineNuage(demander = 0) : demande les informations à l'utilisateur pour créer un nuage
def dessineNuage(x=0,y=0,rayon=100,couleur='white', demander = 1):
    if demander == 0:                                                                               # si on demande à l'utilisateur
        x = lireEntierClavier("Le x du point bas gauche du nuage : ", LARGEUR_MIN, LARGEUR_MAX)     # on récupère l'abscisse
        y = lireEntierClavier("Le y du point bas gauche du nuage : ", HAUTEUR_MIN, HAUTEUR_MAX)     # on récupère l'ordonnée
        rayon = lireEntierClavier("Le rayon du nuage (10-200) : ", 10, 200)                         # la taille du nuage
        couleur = lireCouleurClavier("La couleur du nuage (en hexadécimal ou en anglais) : ")       # la couleur du nuage
    dessineRectangle(x,y,rayon,rayon/2,couleur)                                                     # le rectangle est la base du nuage

    for i in range(0,4):                                                                            # ce bout de code dessine
        dessineDemiCercle(xcor(),ycor(),rayon/8,couleur,270)                                        # le bas du nuage

    for i in range(0,2):                                                                            # ce bout de code dessine
        dessineDemiCercle(xcor(),ycor(),rayon/8,couleur,0)                                          # le côté droit du nuage
        
    for i in range(0,4):                                                                            # ce bout de code dessine
        dessineDemiCercle(xcor(),ycor(),rayon/8,couleur,90)                                         # le haut du nuage

    for i in range(0,2):                                                                            # ce bout de code dessine
        dessineDemiCercle(xcor(),ycor(),rayon/8,couleur,180)                                        # le côté gauche du nuage


def dessineSoleil(xSoleil=0, ySoleil=0, rayon=50, demander=0):
    if demander == 0:                                                                                               # si on demande à l'utilisateur : 
        
        xSoleil = lireEntierClavier("Entrez le x du point milieu-gauche du soleil : ", LARGEUR_MIN, LARGEUR_MAX)    # on rentre l'abscisse
        ySoleil = lireEntierClavier("Entrez le y du point milieu-gauche du soleil : ", HAUTEUR_MIN, HAUTEUR_MAX)    # on rentre l'ordonnée
        rayon = lireEntierClavier("Entrez le rayon du soleil (25-100) : ", 25, 100)                                 # on rentre le rayon
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
