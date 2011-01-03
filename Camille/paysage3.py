#paysage n°3

# import des fonctions utiles

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
	

def dessineTriangle(x,y,angle=0,cote=50,couleur="black",epaisseur=1):
    color(couleur)			
    width(epaisseur)		    
    aller(x,y,angle)			    
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


def dessineVague4(x,y,hauteur,longueur):
    width(3)
    aller(x,y)
    left(50)
    i=0
    while i<=longueur:
        circle(2*hauteur,-100)
        left(100)
        i=i+4*hauteur

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

def dessineBouee(x=0,y=0, demander=0):    
    if demander == 0:                                                                                   # si on demande à l'utilisateur
        x = lireEntierClavier("Le x du point bas milieu de la bouée : ", LARGEUR_MIN, LARGEUR_MAX)      # on récupère l'abscisse
        y = lireEntierClavier("Le y du point bas milieu de la bouée : ", HAUTEUR_MIN, HAUTEUR_MAX)      # on récupère l'ordonnée
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
    color("#BF5C00")                            
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


# dessin:

setup(1280,1024)
bgcolor('#ABC8E2')

dessineMer('jour','agitée',1)
dessineSoleil(-590,350,60,1)
dessineNuage(100,200,150,'grey')
dessineNuage(150,250,200,'grey')
dessineNuage(600,210,250,'grey')

dessineDauphin(-50,-100,1)
dessineDauphin(-300,-200,1)

dessineRectangle(250,-300,500,350,'black')
dessineTriangle(250,-300,60,405,'black')

dessineBouee(400,-100,1)

color('blue')
dessineVague1(600,-305,50,400)
