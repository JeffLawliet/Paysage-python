# paysage n°2

# import des fonctions utiles

from turtle import *                                      			  # import du module turtle pour faire fonctionner les fonctions
setup(1280*1024)

from math import *								  # import du module math pour certains calculs mathématiques
from random import *								  # import du module random pour gérer l'aléatoire
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

def dessineMaison(x=0,y=0,couleurMaison='red',couleurToit='black',couleurPorte='black',largeur = 130, hauteur=150):
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

    
def dessineMaison1(xMaison=0, yMaison=0, hauteurMaison=200, largeurMaison=70, couleurMaison='black',nbrFenetresEtagesMaison = 2,toit = 'oui', couleurPorte = 'red',couleurFenetresMaison='blue', couleurToit = 'blue', couleurEtages = 'red', demander = 0,nbrEtagesMaison=1):
    dessineRectangle(xMaison, yMaison, largeurMaison, hauteurMaison, couleurMaison)
    if demander == 0:
        toit = input("Voulez-vous un toit (Oui/Non) : ")
        while toit != 'Non' and toit != 'non' and  toit != 'Oui' and toit != 'oui':
            print("Veuillez recommencer.")
            toit = input("Voulez-vous un toit (Oui/Non) : ")
        if toit == 'Oui' or toit == 'oui':    
            couleurToit = lireCouleurClavier("Entrez la couleur de votre toit (en hexadécimal ou en anglais) : ")
        couleurEtages = lireCouleurClavier("Entrez la couleur de l'étage (en hexadécimal ou en anglais) : ")
    if toit == 'oui' or toit == 'Oui':
        dessineTriangle(xMaison, yMaison+hauteurMaison, largeurMaison, couleurToit)
        
    for i in range(1,nbrEtagesMaison):
        
        aller(xMaison,yMaison+i*(hauteurMaison/nbrEtagesMaison))
        dessineTrait(xcor(), ycor(), largeurMaison, 0, couleurEtages)

    xPorte = xMaison + (2*largeurMaison)/5
    largeurPorte = largeurMaison/3
    hauteurPorte = 2*hauteurMaison/(3*nbrEtagesMaison)
    dessineRectangle(xPorte, yMaison, largeurPorte, hauteurPorte, couleurPorte)
    if demander == 0:
            
        nbrFenetresEtagesMaison = lireEntierClavier("Entrez le nombre de fenêtre par étages de votre maison (entre 1 et 10) : ", 1, 10)
        couleurFenetresMaison = lireCouleurClavier("Entrez la couleur des fenêtres de votre maison (en hexadécimal ou en anglais) : ")
            
    dessineFenetre(nbrFenetresEtagesMaison,nbrEtagesMaison,hauteurMaison,largeurMaison, xMaison, yMaison, couleurFenetresMaison)
	

def dessineFenetre(nbrFenetresEtages, nbrEtages, hauteurMaison, largeurMaison, x, y, couleur='blue', epaisseur=1):
    largeurFenetre = largeurMaison / (3*nbrFenetresEtages)
    hauteurFenetre = hauteurMaison / (3*nbrEtages)
    intervalle = ((2*largeurMaison)//3)//(nbrFenetresEtages+1)
    if nbrFenetresEtages > 1:
        for i in range(1,nbrEtages):
            aller(x,y+((i+1)*(hauteurMaison/nbrEtages))-(hauteurMaison/(2*nbrEtages)))
            for j in range(0, nbrFenetresEtages):
                aller(xcor() + intervalle,ycor()) 
                dessineRectangle(xcor(),ycor(),largeurFenetre, hauteurFenetre,couleur,epaisseur) 
                aller(xcor()+ largeurFenetre,ycor())          
    elif nbrFenetresEtages == 1: 
        if nbrEtages == 1:
            print("ok")
            aller(x+(largeurMaison/6),y+(hauteurMaison/2))  
            dessineRectangle(xcor(),ycor(),largeurFenetre, hauteurFenetre, couleur,epaisseur)
            
        else:
            for i in range(1,nbrEtages):
                aller(x+(largeurMaison/24),y+((i+1)*(hauteurMaison/nbrEtages))-(hauteurMaison/(2*nbrEtages))) 
                dessineRectangle(xcor(),ycor(),largeurFenetre, hauteurFenetre,couleur,epaisseur)


def dessineLampadaire(xLampadaire = 0, yLampadaire = 0, couleurLampadaire = 'black', demander = 0, allumer = 0):
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

def dessineArbre(xArbre=0, yArbre=0, largArbre = 50, hautArbre = 300, couleur = 'green', demander = 0):
    if demander == 0:   
        xArbre = lireEntierClavier("Entrez le x du point bas-gauche de l'arbre : ", LARGEUR_MIN, LARGEUR_MAX)
        yArbre = lireEntierClavier("Entrez le y du point bas-gauche de l'arbre : ", HAUTEUR_MIN, HAUTEUR_MAX)
        largArbre = lireEntierClavier("Entrez la largeur de l'arbre (10-50) : ", 10, 50)
        hautArbre = lireEntierClavier("Entrez la hauteur de l'arbre (100-400) : ",100, 400)
    dessineRectangle(xArbre, yArbre, largArbre, hautArbre-10, '#3D0000')
    begin_fill()
    traitDeplacement(xArbre + largArbre//2, yArbre + hautArbre + 40, xArbre -3*largArbre, yArbre + hautArbre//6, couleur)
    dessineTrait(xcor(), ycor(), 7*largArbre, 0, couleur)
    traitDeplacement(xcor(), ycor(), xArbre + (largArbre//2), yArbre + hautArbre + 40, couleur)
    end_fill()
 
def dessineFleur(x=0, y=0, haut=20, demander = 0):
    if demander == 0:
        x=lireEntierClavier("Abscisse du bout de la tige au sol : ",LARGEUR_MIN, LARGEUR_MAX)
        y=lireEntierClavier("Ordonnée du bout de la tige au sol : ", HAUTEUR_MIN, HAUTEUR_MAX)
        haut=lireEntierClavier("Hauteur de la fleur (10-60) : ", 10, 60)
    diam=haut/12
    color('white')
    begin_fill()
    aller(x+(haut/24),y+(11*haut/12))
    left(100)
    circle(diam,220)
    i=1
    while i<=8:
        left(220)
        circle(diam,220)
        i=i+1
    end_fill()
    color('yellow')
    begin_fill()
    aller(x+(diam/6)+(diam/8),y+(26*diam/3)+(diam/8))
    circle((2*diam/3),360)
    end_fill()
    color('#1D702D')
    width(2)
    aller(x-(diam/2),y+(22*diam/3))
    left(250)
    circle(haut+diam,20)
    left(180)
    begin_fill()
    circle(3*diam,100)
    left(90)
    circle(3*diam,90)
    end_fill()
    right(90)
    circle(haut+diam,15)

def dessineSoleil(xSoleil=0, ySoleil=0, rayon=50, demander=0):
    if demander == 0:
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

def dessineNuage(x=0,y=0,rayon=100,couleur='white', demander = 1):
    if demander == 0:                                                                            
        x = lireEntierClavier("Le x du point bas gauche du nuage : ", LARGEUR_MIN, LARGEUR_MAX)    
        y = lireEntierClavier("Le y du point bas gauche du nuage : ", HAUTEUR_MIN, HAUTEUR_MAX)     
        rayon = lireEntierClavier("Le rayon du nuage (10-200) : ", 10, 200)                         
        couleur = lireCouleurClavier("La couleur du nuage (en hexadécimal ou en anglais) : ")      
    dessineRectangle(x,y,rayon,rayon/2,couleur)                                                     
    for i in range(0,4):                                                                     
        dessineDemiCercle(xcor(),ycor(),rayon/8,couleur,270)                                      
    for i in range(0,2):                                                                          
        dessineDemiCercle(xcor(),ycor(),rayon/8,couleur,0)                                            
    for i in range(0,4):                                                                  
        dessineDemiCercle(xcor(),ycor(),rayon/8,couleur,90)                                      
    for i in range(0,2):                                                                            
        dessineDemiCercle(xcor(),ycor(),rayon/8,couleur,180)


# dessin


bgcolor('#ABC8E2')

dessineRectangle(LARGEUR_MIN,HAUTEUR_MIN,2*LARGEUR_MAX,HAUTEUR_MAX,'green')

dessineSoleil(400,350,70,1)
dessineNuage(-600,400,150,'white',1)

dessineRoute(LARGEUR_MIN,HAUTEUR_MIN+20,250,2*LARGEUR_MAX,1)
dessineRectangle(LARGEUR_MIN,HAUTEUR_MIN,2*LARGEUR_MAX,20,'grey')
dessineRectangle(LARGEUR_MIN,HAUTEUR_MIN+270,2*LARGEUR_MAX,20,'grey')

dessineMaison1(LARGEUR_MIN+100,HAUTEUR_MIN+290,450,520,'#BD8D46',2,'oui','#52251C','black','black','red',1,2)
dessineLampadaire(50,HAUTEUR_MIN+290,'black',1,0)
dessineArbre(250,-50,20,300,'#1D702D',1)
dessineFleur(400,-100,50,1)
dessineFleur(500,-75,50,1)
dessineFleur(600,-150,45,1)

dessineVoiture(LARGEUR_MAX-50,HAUTEUR_MIN+150,50,'red',1)
dessineVoiture(LARGEUR_MIN+200,HAUTEUR_MIN+150,50,'purple',1)

