###  IMPORT ###

from turtle import *                                      			  # import du module turtle pour faire fonctionner les fonctions
from math import *								  # import du module math pour certains calculs mathématiques
from random import *								  # import du module random pour gérer l'aléatoire

######################################################

### DÉFINITION DES CONSTANTES ###

LARGEUR_MAX = window_width()//2                     			          # largeur maximale est égale à la moitié de la largeur totale
LARGEUR_MIN = -window_width()//2						  # largeur minimale est égale à l'opposé de la moitié de la largeur totale
HAUTEUR_MAX = window_height()//2						  # hauteur maximale est égale à la moitié de la hauteur totale
HAUTEUR_MIN = -window_height()//2						  # hauteur minimale est égale à l'opposé de la hauteur totale

#######################################################

### INITIALISATION DES RÉGLAGES ###

reset()										  # on nettoie l'écran des éventuelles impuretées
speed(0)									  # on met la vitesse au maximum
bgcolor('white')								  # on met un fond d'écran blanc sobre
ht()										  # on cache la tortue

#######################################################

### FONCTIONS DE DÉPLACEMENTS ###

# fonction aller : se déplace en x,y et s'oriente vers angle 
# exemples d'utilisation : aller(40,-30, 90) : se rend en (40;-30) et s'oriente vers le nord
#			   aller(50,38)      : se rend en (50;38) et s'oriente vers l'est
def aller(x,y,angle=0):
    up()                          						  # lève le pinceau
    goto(x,y)									  # se déplace aux coordonnées indiquées
    down()									  # baisse le pinceau
    seth(angle)									  # s'oriente suivant l'angle indiqué

# fonction traitDeplacement : se place aux coordonnées indiquées, puis se rend aux coordonnées jointes en traçant un trait d'épaisseur et de couleur jointes	
# exemples d'utilisation : traitDeplacement(40,30,50,70,'red') : se place en (40;30) et trace un trait épais de 1, de couleur rouge jusqu'au point (50;70)
#			   traitDeplacement(10,0,0,0,epaisseur=3) : se place en (10;0) et trace un trait épais de 3, de couleur noir jusqu'au point (0;0) 
# REMARQUE : pour le deuxième exemple, la fonction dessineTrait sera préférable
def traitDeplacement(xDepart, yDepart, xArrivee, yArrivee, couleur='black', epaisseur=1):
    aller(xDepart,yDepart)						          # voir fonction aller
    width(epaisseur)			  					  # on épaissait le trait
    color(couleur) 					  			  # on colorie le trait
    goto(xArrivee,yArrivee)      	  					  # on trace le trait

# fonction dessineTrait : à partir du point indiqué, trace un trait d'épaisseur, de couleur et de longueur indiquée selon un angle indiqué
# exemples d'utilisation : dessineTrait(0,0) : se place en (0;0) et dessine un trait noir de longueur 50, épais de 2 vers la droite
#                          dessineTrait(0,0,orientation = 90, couleur = 'red') : se place en (0;0), dessine un trait rouge, épais de 2, long de 50 vers le haut
# REMARQUE : à utiliser lorsque l'on fait un déplacement vertical ou horizontal ou lorsque l'on connait la distance à parcourir en diagonale
def dessineTrait(x,y,deplacement=50,orientation=0,couleur='black',epaisseur=2):
    color(couleur)				# on change la couleur
    width(epaisseur)				# on change l'épaisseur
    aller(x,y,orientation)			# voir fonction aller
    forward(deplacement)			# on avance de la longueur choisie
 	
#######################################################

### FONCTIONS DE DESSINS SIMPLES ###

# fonction dessineCarre : à partir du point indiqué, dessine et colorie un carré d'épaisseur, de longueur et de couleur indiquées
# exemples d'utilisation : dessineCarre(30,40,15,'red',2) : se place en (30;40), et dessine et colorie un carré de côté 15, de couleur rouge et épais de 2
#			 : dessineCarre(3,3) : se place en (3;3), et dessine et colorie un carré de côté 50, noir et épais de 1
def dessineCarre(x,y,cote=50,couleur='black',epaisseur=1):
    aller(x,y,315)	          # voir fonction aller
    width(epaisseur)		  # on épaissit le trait
    begin_fill()		  # on commence le remplissage
    color(couleur)            	  # on choisit la couleur du remplissage
    circle(cote,None,4)       	  # on trace un cercle de 4 côtés (soit un carré)
    end_fill()			  # on finit le remplissage
	
# fonction dessineTriangle : à partir du point indiqué, dessine et colorie un triangle équilatérale épais, de longueur et de couleur indiquées
# exemples d'utilisation : dessineTriangle(40,50,30,'yellow') : se place en (40;50) et dessine et colorie un triangle équilatéral jaune épais de 1 de côté 30
#			   dessineTriangle(10,10) : se place en (10;10) et dessine et colorie un triangle équilatéral noir épais de 1 de côté 50
def dessineTriangle(x,y,cote=50,couleur="black",epaisseur=1):
    color(couleur)			# on choisit la couleur du remplissage
    width(epaisseur)			# on épaissait le trait
    aller(x,y)				# voir fonction aller
	
    begin_fill()			# on commence le remplissage
    for i in range(0,3):		# boucle for : on exécute 3 fois : 
        forward(cote)			# on avance de la longueur du côté
        left(120)			# et on tourne de 120°
    end_fill()				# on termine le remplissage

# fonction dessineRectangle : à partir du point indiqué, dessine et colorie un rectangle épais, de couleur, hauteur et largeur données
# exemples d'utilisation : dessineRectangle(20,25,40,30) dessine en (20;25), un rectangle large 40, haut de 30, de couleur rouge épais de 1
#			   dessineRectangle(0,0,epaisseur = 2) dessine en (0;0) un rectangle large 180, haut de 50, de couleur rouge et épais de 2
def dessineRectangle(x,y,largeur=180,hauteur=50,couleur='red',epaisseur=1):
    aller(x,y)				# voir fonction aller
    width(epaisseur)			# on change l'épaisseur
    color(couleur)			# on change la couleur du remplissage
	
    begin_fill()		        # on commence le remplissage
    for i in range(0,4):		# on répète 4 fois le bloc suivant :
        if i%2 == 0:			# lorsque i est pair
            forward(largeur)		# on avance de la largeur
        else:				# sinon
            forward(hauteur)		# de la longueur
        left(90)			# dans tous les cas, on tourne de 90°
    end_fill() 				# on finit le remplissage

# fonction dessineDemiCercle : à partir du point indiqué, dessine et colorie, selon un angle, un demi-cercle épais de couleur et de cotés indiquées
# exemples d'utilisation : dessineDemiCercle(30,-30,60,'grey',15,4) : dessine un demi-cercle en (30;-30), de couleur grise, de rayon 60, épais de 4 à partir de 15°
#			   dessineDemiCercle(0,0,20) : dessine un demi-cercle bleu en (0;0) de rayon 20 à parti de 0° épais de 1
def dessineDemiCercle(x,y,rayon,couleur='blue',orientation=0,epaisseur=1):
    width(epaisseur)            # on change l'épaisseur
    color(couleur)		# on change la couleur
    aller(x,y,orientation)      # voir fonction aller
	
    begin_fill()                # on commence le remplissage
    circle(rayon,180)           # on dessine la moitié d'un cercle
    end_fill()			# on termine le remplissage
 

#######################################################

### FONCTIONS DE SÉCURITÉ ###

# fonction lireEntierClavier : oblige l'utilisateur à rentrer un nombre compris entre deux valeurs
def lireEntierClavier(phrase, inferieur, superieur):
    valeur = inferieur - 1						# on initialise la valeur de retour 
	
    while valeur < inferieur or valeur > superieur:			# boucle while : tant que la valeur n'est pas comprise entre les deux bornes
            try:							# on essaie :
                valeur = int(input(phrase))				# d'attribuer à valeur un nombre (en affichant un message), et de le caster en int.
				
            except ValueError:						# pour toutes les erreurs de type ValueError:
			
                print("Veuillez recommencer.")				# demander de recommencer
                valeur = inferieur - 1					# on attribue à valeur, une valeur qui fait qu'on reste dans la boucle
		
    return valeur							# au final on retourne le nombre entier.

# fonction lireCouleurClavier : oblige l'utilisateur à rentrer une couleur
def lireCouleurClavier(phrase, couleur=0):
    securite = 1							# on initialise une variable de sécurité
	
    while securite == 1:						# tant que la sécurité est activé :
        try:								# on essaie :	
            chaine = input(phrase)					# on attribue à chaîne une couleur (en affichant un message)
            securite = 0						# on désactive la sécurité
            if couleur == 0: color(chaine)				# si on souhaitait une couleur : on change la couleur
            elif couleur == 1: bgcolor(chaine)				# si on souhaitait un fond d'écran : on change le fond d'écran
			
        except:								# si une erreur apparaît
		
            securite = 1						# on réactive la sécurité
			
    return(chaine)							# au final, on renvoie la chaîne contenant la couleur

#######################################################

### CATÉGORIE : VILLE ###
	
# fonction dessineRoute : dessine une route à partir d'un point indiqué, de largeur et de longueur indiquées
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

#fonction dessineMaison : dessine une maison dont l'utilisateur peut définir les dimensions, couleurs de la façade, du toit et de la porte et finalement placer la maison.
def dessineMaison(x=0,y=0,couleurMaison='red',couleurToit = 'red', couleurPorte='black',largeur = 130, hauteur=150, demander =1):
    if demander == 0:
        
        couleurToit = lireCouleurClavier("Entrez la couleur du toit (en hexadécimal ou en anglais) : ")         #voir fonction lireCouleurClavier
    # Dessine le rectangle de la maison :
    aller(x,y)                      # voir fonction aller
    width(0)                        # modifie l'épaisseur du trait
    begin_fill()                    # commence le remplissage
    color(couleurMaison)                    # choix de la couleur (ici donnée par l'utilisateur et par défaut rouge)
    for i in range(0,2):                    # boucle for : on execute 2 fois.
        forward(largeur)                    # avance de la valeur "largeur"
        left(90)                            # tourne sur la gauche de 90 degrés
        forward(hauteur)                    # avance de la valeur "hauteur"
        left(90)                            # tourne sur la gauche de 90 degrés
    end_fill()                              # fin du remplissage
    color("black")                          # choix de la couleur noire
    for i in range(0,2):                    # boucle for : on execute 2 fois.
        forward(largeur)                    # avance de la valeur "largeur"
        left(90)                            # tourne sur la gauche de 90 degrés
        forward(hauteur)                    # avance de la valeur "hauteur"
        left(90)                            # tourne sur la gauche de 90 degrés
    
    # Dessine le toit :
    up()                                    # leve le pinceau
    goto(largeur+x,hauteur+y)               # se déplace au point d'abcisse "largeur+x" et d'ordonnées "hauteur+y"
    down()                                  # pose le pinceau
    begin_fill()                            # commence le remplissage
    color(couleurToit)                      # choix de la couleur (ici donnée par l'utilisateur et par défaut rouge)
    longueurToit=largeur*acos(pi/4)         # définit la variable longueurToit
    left(135)                               # tourne sur la gauche de 195 degrés
    forward(longueurToit)                   # avance de la valeur "longueurToit"
    goto(x,hauteur+y)                       # se déplace au point d'abcisse "x" et d'ordonnées "hauteur+y"
    end_fill()                              # fin du remplissage

    # Dessine la porte :
    positionPorte=randint(1,3)              # définit la variable positionPorte qui peut prendre une valeur comprise entre 1 et 3 inclus de manière aléatoire
    largeurPorte=largeur/5                  # définit la variable largeurPorte
    hauteurPorte=hauteur/3                  # définit la variable hauteurPorte
    if positionPorte==1:                    # si la variable positionPorte est égale à 1
        up()                                                # leve le pinceau
        goto((largeur/3)-(largeurPorte/2)+x,y)              # se déplace aux coordonnées données
        down()                                              # pose le pinceau
    elif positionPorte==2:                                  # si la variable positionPorte est égale à 2
        up()                                                # leve le pinceau
        goto((largeur/2)-(largeurPorte/2)+x,y)              # se déplace aux coordonnées données
        down()                                              # pose le pinceau
    else:                                                   # si aucune des deux conditions précédentes n'est remplie, alors:
        up()                                                # leve le pinceau
        goto((2*largeur/3)-(largeurPorte/2)+x,y)            # se déplace aux coordonnées données
        down()                                              # pose le pinceau
    begin_fill()                                            # commence le remplissage
    color(couleurPorte)                                     # choix de la couleur (ici donnée par l'utilisateur et par défaut noire)
    right(45)                                               # tourne sur la droite d'un angle de 45
    for k in range(0,2):                                    # boucle for : on execute 2 fois.
        forward(hauteurPorte)                               # avance de la valeur "hauteurPorte"
        right(90)                                           # tourne sur la droite d'un angle de 90 degrés
        forward(largeurPorte)                               # avance de la valeur "largeurPorte"
        right(90)                                           # tourne sur la droite d'un angle de 90 degrés
    end_fill()                                              # fin du remplissage
    color("black")                                          # choix de la couleur noire
    for k in range(0,2):                                    # boucle for : on execute 2 fois.
        forward(hauteurPorte)                               # avance de la valeur "hauteurPorte"
        right(90)                                           # tourne sur la droite de 90 degrés
        forward(largeurPorte)                               # avance de la valeur "largeurPorte"
        right(90)                                           # tourne sur la droite d'un angle de 90 degrés

    # Dessine la poignée :
    if positionPorte==1:                                                # si la variable positionPorte est égale à 1
        up()                                                            # leve le pinceau
        goto((largeur/3)+(4*largeurPorte/10)+x,y+(hauteurPorte/2))      # se déplace aux coordonnées données
        down()                                                          # pose le pinceau
    elif positionPorte==2:                                              # si la variable positionPorte est égale à 2
        up()                                                            # leve le pinceau
        goto((largeur/2)+(2*largeurPorte/5)+x,y+(hauteurPorte/2))       # se déplace aux cordonnées données
        down()                                                          # pose le pinceau
    else:                                                               # si aucune des deux conditions précedentes n'est remplie, alors :
        up()                                                            # leve le pinceau
        goto((2*largeur/3)+(2*largeurPorte/5)+x,y+(hauteurPorte/2))     # se déplace aux coordonnées données
        down()                                                          # pose le pinceau
    begin_fill()                                                        # commence le remplissage
    color("black")                                                      # choix de la couleur noire
    circle(largeurPorte/10)                                             # dessine un cercle dont le rayon est égal à la valeur "largeurPorte/10"
    end_fill()                                                          # fin du remplissage

    # Dessine les fenetres :
        # Sur le toit:
    fenetreToit=randint(0,1)                                            # définit la variable fenetreToit qui peut prendre la valeur 0 ou 1 de manière aléatoire
    if fenetreToit==1:                                                  # si la variable fenetreToit est égale à 1
        up()                                                            # leve le pinceau
        goto((19*largeur/30)+x,(11*hauteur/9)+y)                        # se déplace aux coordonnées indiquées
        down()                                                          # pose le pinceau
        begin_fill()                                                    # commence le remplissage 
        color("DarkSlateGray")                                          # choix de la couleur DarkSlateGray
        circle(largeur/9)                                               # dessine un cercle dont le rayon est égale à la valeur "largeur/9"
        end_fill()                                                      # fin du remplissage
        #Petite lucarne
        up()                                                            # leve le pinceau
        goto((613*largeur/1000)+x,(11*hauteur/9)+y)                     # se déplace aux coordonnées indiquées
        down()                                                          # pose le pinceau
        begin_fill()                                                    # commence le remplissage
        color("yellow")                                                 # choix de la couleur jaune
        circle(largeur/11)                                              # dessine un cercle dont le rayon est égal à la valeur "largeur/11"
        end_fill()                                                      # fin du remplissage
        # Croix
        color("black")                                                  # choix de la couleur noire
        width(5)                                                        # modifie l'épaisseur du trait
        left(90)                                                        # tourne sur la gauche d'un angle de 90 degrés
        forward(2*largeur/11)                                           # avance de la valeur "2*largeur/11"
        goto((613*largeur/1000)-(largeur/11)+x,(11*hauteur/9)+y)        # se déplace aux coordonnées indiquées
        right(90)                                                       # tourne sur la droite d'un angle de 90 degrés
        forward(largeur/11)                                             # avance de la valeur "largeur/11"
        backward(2*largeur/11)                                          # recule de la valeur "2*largeur/11"

        # Sur la maison:
    up()                                                                # leve le pinceau
    goto((largeur/5)+x,(2*hauteur/3)+y)                                 # se déplace aux coordonnées indiquées
    down()                                                              # pose le pinceau
    width(5)                                                            # modifie l'épaisseur du trait
    begin_fill()                                                        # commence le remplissage
    color("#E9FFE5")                                                    # choix de la couleur (ici en héxadécimal) "#E9FFE5"
    for j in range(0,4):                                                # boucle for : on execute 4 fois.
        forward(hauteur/6)                                              # avance de la valeur "hauteur/6"
        right(90)                                                       # tourne sur la droite d'un angle de 90 degrés
    end_fill()                                                          # fin du remplissage
    color("black")                                                      # choix de la couleur noire
    for j in range(0,4):                                                # boucle for : on execute 4 fois.
        forward(hauteur/6)                                              # on avance de la valeur "hauteur/6"
        right(90)                                                       # on tourne sur la droite d'un angle de 90 degrés
    forward(hauteur/12)                                                 # on avance de la valeur "hauteur/12"
    right(90)                                                           # on tourne sur la droite d'un angle de 90 degrés
    forward(hauteur/6)                                                  # on avance de la valeur "hauteur/6"
    backward(hauteur/12)                                                # on recule de la valeur "hauteur/12"
    right(90)                                                           # on tourne sur la droite d'un angle de 90 degrés
    forward(hauteur/12)                                                 # on avance de la valeur "hauteur/12"
    backward(hauteur/6)                                                 # on recule de la valeur "hauteur/6"
        
    up()                                                                # on leve le pinceau
    goto((7*largeur/10)+x,(2*hauteur/3)+y)                              # on se déplace aux coordonnées indiquées
    down()                                                              # on pose le pinceau
    width(5)                                                            # on modifie l'épaisseur du trait
    begin_fill()                                                        # fin du remplissage
    color("#E9FFE5")                                                    # choix de la couleur (ici en hexadécimal)
    right(180)                                                          # on tourne à droite d'un angle de 180 degrés
    for j in range(0,4):                                                # boucle for : on execute 4 fois.
        forward(hauteur/6)                                              # on avance de la valeur "hauteur/6"
        right(90)                                                       # on tourne à droite d'un angle de 90 degrés
    end_fill()                                                          # fin du remplissage
    color("black")                                                      # choix de la couleur noire
    for j in range(0,4):                                                # boucle for : on execute 4 fois
        forward(hauteur/6)                                              # on avance de la valeur "hauteur/6"
        right(90)                                                       # on tourne sur la droite d'un angle de 90 degrés
    forward(hauteur/12)                                                 # on avance de la valeur "hauteur/12"
    right(90)                                                           # on tourne sur la droite d'un angle de 90 degrés
    forward(hauteur/6)                                                  # on avance de la valeur "hauteur/6"
    backward(hauteur/12)                                                # on recule de la valeur "hauteur/12"
    right(90)                                                           # on tourne sur la droite d'un angle de 90 degrés
    forward(hauteur/12)                                                 # on avance de la valeur "hauteur/12"
    backward(hauteur/6)                                                 # on recule de la valeur "hauteur/6"

        #En fonction de la porte
    if positionPorte==1 or positionPorte==3:                            # si la variable positionPorte est égale à 1 ou à 3
        if positionPorte==1:                                            # si la variable positionPorte est égale à 1
            up()                                                        # on leve le pinceau
            goto((11*largeur/20)+x,hauteurPorte+y)                      # on se déplace aux coordonnées indiquées
            down()                                                      # on pose le pinceau
        else:                                                           # si la variable positionPorte n'est pas égale à 1
            up()                                                        # on leve le pinceau
            goto(3*largeur/20+x,hauteurPorte+y)                         # on se déplace aux coordonnées indiquées
            down()                                                      # on pose le pinceau
        begin_fill()                                                    # on commence le remplissage
        color("#E9FFE5")                                                # choix de la couleur (ici en héxadécimal)
        for k in range(0,2):                                            # boucle for : on execute 2 fois.
            forward(2*hauteurPorte/5)                                   # on avance de la valeur "2*hauteurPorte/5"
            left(90)                                                    # on tourne à gauche d'un angle de 90 degrés
            forward(largeur/3)                                          # on avance de la valeur "largeur/3"
            left(90)                                                    # on tourne à gauche d'un angle de 90 degrés
        end_fill()                                                      # fin du remplissage
        width(5)                                                        # on modifie l'épaisseur du trait
        color("black")                                                  # choix de la couleur noire
        for k in range(0,2):                                            # boucle for : on execute 2 fois.
            forward(2*hauteurPorte/5)                                   # on avance de la valeur "2*hauteurPorte/5"
            left(90)                                                    # on tourne à gauche d'un angle de 90 degrés
            forward(largeur/3)                                          # on avance de la valeur "largeur/3"
            left(90)                                                    # on tourne à gauche d'un angle de 90 degrés
        forward(hauteurPorte/5)                                         # on avance de la valeur "hauteurPorte/5"
        left(90)                                                        # on tourne à gauche d'un angle de 90 degrés
        forward(largeur/3)                                              # on avance de la valeur "largeur/3"
        backward(largeur/6)                                             # on recule de la valeur "largeur/6"
        right(90)                                                       # on tourne à droite d'un angle de 90 degrés
        forward(hauteurPorte/5)                                         # on avance de la valeur "hauteurPorte/5"
        backward(2*hauteurPorte/5)                                      # on recule de la valeur "2*hauteurPorte/5"
    left(90)                                                            # on tourne à gauche d'un angle de 90 degrés

#fonction dessineMaison, utilise différents module pour créer une maison    
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
	
#fonction dessineFenetre, dessine des fenêtres tous les étages, en les remplissant.
def dessineFenetre(nbrFenetresEtages, nbrEtages, hauteurMaison, largeurMaison, x, y, couleur='blue', epaisseur=1):
    largeurFenetre = largeurMaison / (3*nbrFenetresEtages)
    hauteurFenetre = hauteurMaison / (3*nbrEtages)
    intervalle = ((2*largeurMaison)//3)//(nbrFenetresEtages+1) #largeur innocupée par les fenêtres
    if nbrFenetresEtages > 1:
        
        for i in range(1,nbrEtages):
            aller(x,y+((i+1)*(hauteurMaison/nbrEtages))-(hauteurMaison/(2*nbrEtages))) #on se déplace à l'étage supérieur
        
            for j in range(0, nbrFenetresEtages):
                aller(xcor() + intervalle,ycor()) #on avance de la longueur d'un intervalle
                dessineRectangle(xcor(),ycor(),largeurFenetre, hauteurFenetre,couleur,epaisseur)  #on dessine un carré qu'on remplit aussitôt
                aller(xcor()+ largeurFenetre,ycor()) # on se décale de largeur fenetre
                
    elif nbrFenetresEtages == 1:
        
        if nbrEtages == 1:
            print("ok")
            aller(x+(largeurMaison/6),y+(hauteurMaison/2))   # on se décale un petit peu
            dessineRectangle(xcor(),ycor(),largeurFenetre, hauteurFenetre, couleur,epaisseur) # on dessine la fenêtre
            
        else:
            for i in range(1,nbrEtages):
                aller(x+(largeurMaison/24),y+((i+1)*(hauteurMaison/nbrEtages))-(hauteurMaison/(2*nbrEtages))) # on se décale un peu
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
    color('green')
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
    
 
#######################################################

### CATÉGORIE : MER ###		
		
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

def dessineVague(x,y,nb):
    aller(x,y)
    longueurVague=412.534656794
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
    

def dessineSable(x=0,y=0,long=412,haut=100,date='jour',demander=0):
    if demander!=0:
        x=int(input("Abscisse du coin bas gauche de la plage: "))
        y=int(input("Ordonnée du coin bas gauche de la plage: "))
        long=int(input("Longueur de la plage: "))
        haut=int(input("Largeur de la plage: "))
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
    dessineRectangle(x,y,long,haut,couleur1,1)
    color(couleur2)
    longueurVague=412.534656794
    i=1
    y2=y+(haut-20)
    while i<=haut/40:
        dessineVague(x+long,y2,long/longueurVague)
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
    
    up()
    goto(xDauphin,yDauphin)
    down()
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
    up()
    goto(xDauphin-136,yDauphin+4.5)
    down()
    circle(4)
    goto(xDauphin-137,yDauphin+3)
    color("white")
    circle(0.5)
    up()
    goto(100,200)
    right(150)

def dessinePhare(x=0, y=0, demander = 0):

    if demander == 0:
        x = lireEntierClavier("Le x du point bas gauche du phare : ", LARGEUR_MIN, LARGEUR_MAX)
        y = lireEntierClavier("Le y du point bas gauche du phrase :", HAUTEUR_MIN, HAUTEUR_MAX)
    aller(x-50,y-200)

    # Base du phare:
    for i in range(0,5):
        if i%2==0:
            begin_fill()
            color("red")
        else:
            begin_fill()
            color("white")
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

    #Lumière :
    left(100)
    begin_fill()
    color("yellow")
    forward(685)
    right(100)
    forward(284)
    right(100)
    forward(685)
    end_fill()
    color("black")
    right(80)
    forward(40)

    #Dome du phare:
    right(90)
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

# fonction dessineEtoile : crée une étoile n'importe où de taille donnée ou une étoile de position et de taille donnée.
# exemples d'utilisation : dessineEtoile() : crée une étoile de taille 2 de façon aléatoire sur la carte
#	                   dessineEtoile(demander = 1) : demande à l'utilisateur de rentrer la taille et les coordonnées de l'étoile puis dessine l'étoile.
def dessineEtoile(taille = 2, demander = 0):
    if demander == 0:                                                                       # si l'utilisateur doit rentrer des valeurs
        taille = lireEntierClavier("Quelle taille pour votre étoile (1-5) : ", 1, 5)        # on rentre la taille, voir fonction lireEntierClavier
        x = lireEntierClavier("Le x de votre étoile : ", LARGEUR_MIN, LARGEUR_MAX)          # on rentre l'abscisse, voir fonction lireEntierClavier
        y = lireEntierClavier("Le y de votre étoile : ", HAUTEUR_MIN, HAUTEUR_MAX)          # on rentre l'ordonnée, voir fonction lireEntierClavier
		
    else:                                                                                   # sinon
        x = randint(LARGEUR_MIN,LARGEUR_MAX)                                                # l'abscisse est choisie aléatoirement
        y = randint(HAUTEUR_MIN,HAUTEUR_MAX)                                                # de même pour l'ordonnée
    color('#fffbb4')                                                                        # on donne la couleur de l'étoile
	
    aller(x,y-taille,90)                        #     on
    forward(2*taille)                           #    crée
    aller(x-taille,y)				#     un
    forward(2*taille)    			#    plus 
	
    aller(x-taille,y+taille,315)		#    on
    forward(2*sqrt(2*(taille**2)))       	#   crée
    aller(x+taille,y+taille,225)    		#    une
    forward(2*sqrt(2*(taille**2)))      	#   croix

# fonction dessineSoleil : dessine un soleil selon les coordonnées données de rayon donnée, ou demande à l'utilisateur de les renter
# exemples d'utilisation : dessineSoleil() : demande à l'utilisateur les informations nécessaires pour créer le soleil
#                          dessineSoleil(rayon = 30, demander = 1) : dessine un soleil en (0;0) de rayon 30.
def dessineSoleil(xSoleil=0, ySoleil=0, rayon=50, demander=0):
    if demander == 0:                                                                                               # si on demande à l'utilisateur : 
        
        xSoleil = lireEntierClavier("Entrez le x du point milieu-gauche du soleil : ", LARGEUR_MIN, LARGEUR_MAX)    # on rentre l'abscisse
        ySoleil = lireEntierClavier("Entrez le y du point milieu-gauche du soleil : ", HAUTEUR_MIN, HAUTEUR_MAX)    # on rentre l'ordonnée
        rayon = lireEntierClavier("Entrez le rayon du soleil (25-100) : ", 25, 100)                                 # on rentre le rayon

    color('yellow')                                                 # on change la couleur
    begin_fill()                                                    # on commence le remplissage
    aller(xSoleil, ySoleil, 270)                                    # on se rend au point indiqué
    circle(rayon)                                                   # on dessine le cercle
    end_fill()                                                      # on arrête le remplissage
	
    for i in range(0,8):					    # on fait 8 fois le bloc suivant :
        aller(xSoleil + rayon, ySoleil)				    # on se déplace au centre du soleil
        left(i*45)						    # on déplace l'angle de i fois 45
        up()							    # on lève le pinceau
        forward(rayon+10)					    # on avance en diagonale
        down()							    # on baisse le pinceau
        forward(rayon/3)					    # trace un rayon de soleil

