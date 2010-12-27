from turtle import *
from math import *
from random import *
reset()
speed(0)

LARGEUR_MAX = window_width()//2
LARGEUR_MIN = -window_width()//2
HAUTEUR_MAX = window_height()//2
HAUTEUR_MIN = -window_height()//2

# fonction aller : se déplace en x,y et s'oriente vers angle
def aller(x,y,angle=0):
    up()
    goto(x,y)
    down()
    seth(angle)



    
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


def dessineRoue(x,y):
    aller(x,y)
    color('black')
    begin_fill()
    circle(20,360)
    end_fill()
    aller(x,y+(20/3))
    color('white')
    begin_fill()
    circle((2*20)/3,360)
    end_fill()
    aller(x,y+(3*20/4))
    color('#B09F91')
    begin_fill()
    circle(20/4,360)
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
def dessineEtoile():
    
    taille = lireEntierClavier("Quelle taille pour votre étoile : ", 1, 5)
    x = randint(LARGEUR_MIN,LARGEUR_MAX)
    y = randint(HAUTEUR_MIN,HAUTEUR_MAX)
    color('black')
    
    aller(x,y-taille,90)
    forward(2*taille)
    
    aller(x-taille,y,0)
    forward(2*taille)
    
    aller(x-taille,y+taille,315)
    forward(2*sqrt(2*(taille**2)))
    
    aller(x+taille,y+taille,225)
    forward(2*sqrt(2*(taille**2)))

#exemple d'utilisation
#dessineEtoile(3)
#dessine une étoile qui fait 6 pixels de long 


    
#fonction dessineFenetre, dessine des fenêtres tous les étages, en les remplissant.
def dessineFenetre(nbrFenetresEtages, nbrEtages, hauteurMaison, largeurMaison, x, y, couleur='blue', epaisseur=1):
    largeurFenetre = largeurMaison / (3*nbrFenetresEtages)
    intervalle = ((2*largeurMaison)//3)//(nbrFenetresEtages+1) #largeur innocupée par les fenêtres
    if nbrFenetresEtages > 1:
        
        for i in range(1,nbrEtages):
            aller(x,y+((i+1)*(hauteurMaison/nbrEtages))-(hauteurMaison/(3*nbrEtages)),0) #on se déplace à l'étage supérieur
        
            for j in range(0, nbrFenetresEtages):
                aller(xcor() + intervalle,ycor(),0) #on avance de la longueur d'un intervalle
                dessineCarre(xcor(),ycor(),largeurFenetre,couleur,epaisseur)  #on dessine un carré qu'on remplit aussitôt
                aller(xcor()+ largeurFenetre,ycor(),0) # on se décale de largeur fenetre
                
    elif nbrFenetresEtages == 1:
        
        if nbrEtages == 1:
            aller(x+(largeurMaison/6),y+(3*hauteurMaison/4),0)   # on se décale un petit peu
            dessineCarre(xcor(),ycor(),largeurFenetre,couleur,epaisseur) # on dessine la fenêtre
            
        else:
            for i in range(1,nbrEtages):
                aller(x+(largeurMaison/6),y+((i+1)*(hauteurMaison/nbrEtages))-(hauteurMaison/(3*nbrEtages)),0) # on se décale un peu
                dessineCarre(xcor(),ycor(),largeurFenetre,couleur,epaisseur)




#fonction dessineLune, dessine une lune aux coordonnées choisie
#de diamètre choisie et la remplie
def dessineLune():

    xLune = lireEntierClavier("Entrez le x du centre gauche de la lune : ", LARGEUR_MIN, LARGEUR_MAX)
    yLune = lireEntierClavier("Entrez le y du centre gauche de la lune : ", HAUTEUR_MIN, HAUTEUR_MAX)
    diametre = lireEntierClavier("Entrez le diamètre de la lune (entre 50 et 200) : ",50, 200) 
    aller(xLune,yLune,0)
    
    begin_fill()
    color('#fffaa2')
    circle(diametre/2)
    end_fill()
    
    aller((27*diametre/50)+xLune,(27*diametre/50)+yLune,90)
    
    begin_fill()
    color('#06011d')
    circle(diametre/3)
    end_fill()
    
    aller(x,y,0)

#exemple d'utilisation
#dessineLune(90,1,-25)
#dessine une lune de 90 de diametre en (1;-25)


#fonction dessineMaison, utilise différents module pour créer une maison    
def dessineMaison():
    print("Où voulez-vous dessinez votre maison ?")
    print("Entrez les coordonnées du point bas-gauche de la maison : ")
    xMaison = lireEntierClavier("Le x de la maison : ",LARGEUR_MIN,LARGEUR_MAX)
    yMaison = lireEntierClavier("Le y de la maison : ",HAUTEUR_MIN,HAUTEUR_MAX)
    hauteurMaison = lireEntierClavier("Entrez la hauteur de la maison : ",1, window_height())
    largeurMaison = lireEntierClavier("Entrez la largeur de la maison : ",1, window_width())
    couleurMaison = input("Entrez la couleur de la maison (en hexadécimal ou en anglais) : ")
    epaisseurMaison = lireEntierClavier("L'épaisseur du trait de la maison (entre 1 et 5) : ",1, 5)
    dessineRectangle(xMaison, yMaison, largeurMaison, hauteurMaison, couleurMaison, epaisseurMaison)

    toit = input("Voulez-vous un toit (Oui/Non) : ")
    while toit != 'Non' and toit != 'non' and  toit != 'Oui' and toit != 'oui':
        print("Veuillez recommencer.")
        toit = input("Voulez-vous un toit (Oui/Non) : ")
    if toit == 'Oui' or toit == 'oui':
        couleurToit = input("Entrez la couleur de votre toit (en hexadécimal ou en anglais) : ")
        dessineTriangle(xMaison, yMaison+hauteurMaison, largeurMaison, couleurToit, epaisseurMaison)
        
    nbrEtagesMaison = lireEntierClavier("Entrez le nombre d'étages (entre 1 et 10) : ", 1, 10)
    couleurEtages = input("Entrez la couleur de l'étage (en hexadécimal ou en anglais) : ")
    for i in range(1,nbrEtagesMaison):
        
        aller(xMaison,yMaison+i*(hauteurMaison/nbrEtagesMaison),0)
        dessineTrait(xcor(), ycor(), largeurMaison, 0, couleurEtages, epaisseurMaison)

    xPorte = xMaison + (2*largeurMaison)/5
    largeurPorte = largeurMaison/3
    hauteurPorte = 2*hauteurMaison/(3*nbrEtagesMaison)
    couleurPorte = input("Entrez la couleur de votre porte (en hexadécimal ou en anglais) : ")
    dessineRectangle(xPorte, yMaison, largeurPorte, hauteurPorte, couleurPorte, epaisseurMaison)

    nbrFenetresEtagesMaison = lireEntierClavier("Entrez le nombre de fenêtre par étages de votre maison (entre 1 et 10) : ", 1, 10)
    couleurFenetresMaison = input("Entrez la couleur des fenêtres de votre maison (en hexadécimal ou en anglais) : ")
    dessineFenetre(nbrFenetresEtagesMaison,nbrEtagesMaison,hauteurMaison,largeurMaison, xMaison, yMaison, couleurFenetresMaison, epaisseurMaison)



#fonction dessineNuage, crée un nuage à la position indiquée.
def dessineNuage(x,y,rayon,couleur):
    dessineRectangle(x,y,rayon,rayon/2,couleur)

    for i in range(0,4):
        dessineDemiCercle(x,y,rayon,couleur,270)


    for i in range(0,2):
        dessineDemiCercle(x,y,rayon,couleur,0)
        
    for i in range(0,4):
        dessineDemiCercle(x,y,rayon,couleur,90)


    for i in range(0,2):
        dessineDemiCercle(x,y,rayon,couleur,180)

#exemple d'utilisation
#dessineNuage(400,300,50,blue)
#dessine un nuage en (400;300) de rayon 50 et de couleur bleue

#Fonction dessineRectangle se déplace aux coordonnées indiquées, s'oriente, et
#crée un rectangle qu'elle remplit
#peut dessiner un batîment, une porte...
def dessineRectangle(x,y,largeur=180,hauteur=50,couleur='red',epaisseur=1):
    aller(x,y,0)
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
    aller(x,y,0)

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
    aller(x,y,0)
    for i in range(0,3):
        forward(cote)
        left(120)
    end_fill()
    seth(0)

#exemple d'utilisation :
#dessineTriangle(40,50,30,'yellow')
#dessine un triangle aux coordonnées (40,50) de côté 30 de couleur jaune


def dessineVoiture():
    print("Où voulez-vous dessinez votre voiture ?")
    print("Entrez les coordonnées du point bas-gauche de la voiture : ")
    xVoiture = lireEntierClavier("Le x de la voiture : ",LARGEUR_MIN,LARGEUR_MAX)
    yVoiture = lireEntierClavier("Le y de la voiture : ",HAUTEUR_MIN,HAUTEUR_MAX)
    couleurVoiture = input("La couleur de la voiture (en hexadécimal ou en anglais) : ")
    aller(xVoiture+5, yVoiture, 0)
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
    


    
    dessineRoue(xVoiture+35,yVoiture-10)
    dessineRoue(xVoiture+165,yVoiture-10)

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

def dessineLampadaire():

    print("Où voulez-vous dessinez votre lampadaire ?")
    print("Entrez les coordonnées du point bas-gauche du lampadaire : ")
    xLampadaire = lireEntierClavier("Le x du lampadaire : ",LARGEUR_MIN,LARGEUR_MAX)
    yLampadaire = lireEntierClavier("Le y du lampadaire : ",HAUTEUR_MIN,HAUTEUR_MAX)
    couleurLampadaire = input("La couleur du lampadaire (en hexadécimal ou en anglais) : ")

    aller(xLampadaire, yLampadaire)

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
    traitDeplacement(xcor(), ycor(), xcor()-18, ycor()+ 50, '#FFF168', 3)
    traitDeplacement(xcor(), ycor(), xcor()+46, ycor(), '#FFF168', 3)
    traitDeplacement(xcor(), ycor(), xcor() -18, ycor() -50, '#FFF168', 3)
    end_fill()
    traitDeplacement(xcor()-9, ycor(), xcor()-27, ycor()+50, couleurLampadaire, 3)
    traitDeplacement(xcor(), ycor(), xcor()-2, ycor()-5, couleurLampadaire, 3)
    traitDeplacement(xcor(), ycor(), xcor()+2, ycor()+5, couleurLampadaire, 3)
    dessineTrait(xcor(), ycor(), 46, 0, couleurLampadaire, 3)
    traitDeplacement(xcor(), ycor(), xcor()+2, ycor()-5, couleurLampadaire,3)
    traitDeplacement(xcor(), ycor(), xcor()-2, ycor()+5, couleurLampadaire,3)
    traitDeplacement(xcor(), ycor(), xcor()-18, ycor()-50, couleurLampadaire, 3)
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

def dessineVoiture():

    xVoiture = lireEntierClavier("Entrez le x du point bas droit de la voiture : ",LARGEUR_MIN,LARGEUR_MAX)
    yVoiture = lireEntierClavier("Entrez le y du point bas droit de la voiture : ", HAUTEUR_MIN, HAUTEUR_MAX)
    couleurVoiture = input("La couleur de la voiture (en hexadécimal ou en anglais) : ")

    dessineRoue(xVoiture-248, yVoiture-25)
    dessineRoue(xVoiture-88, yVoiture-25)
    begin_fill()
    traitDeplacement(xVoiture, yVoiture, xVoiture-10, yVoiture -10, couleurVoiture)
    dessineTrait(xcor(), ycor(), 50, 180, couleurVoiture)
    traitDeplacement(xcor(), ycor(), xcor()-10, ycor()+20, couleurVoiture)
    dessineTrait(xcor(), ycor(), 40, 180, couleurVoiture)
    traitDeplacement(xcor(), ycor(), xcor()-10, ycor()-20, couleurVoiture)
    dessineTrait(xcor(), ycor(), 100, 180, couleurVoiture)
    traitDeplacement(xcor(), ycor(), xcor() -10, ycor() + 20, couleurVoiture)
    dessineTrait(xcor(), ycor(), 40, 180, couleurVoiture)
    traitDeplacement(xcor(), ycor(), xcor()-10, ycor() -20, couleurVoiture)
    dessineTrait(xcor(), ycor(), 30, 180, couleurVoiture)
    traitDeplacement(xcor(), ycor(), xcor()-25, ycor() +10, couleurVoiture)
    traitDeplacement(xcor(), ycor(), xcor()+25, ycor() + 30, couleurVoiture)
    traitDeplacement(xcor(), ycor(), xcor() +60, ycor()+10, couleurVoiture)
    dessineTrait(xcor(), ycor(), 190, 0, couleurVoiture)
    traitDeplacement(xcor(), ycor(), xcor()+40, ycor() -10, couleurVoiture)
    traitDeplacement(xcor(), ycor(), xcor()+20, ycor()-30, couleurVoiture)
    end_fill()

    begin_fill()
    traitDeplacement(xcor()-60, ycor()+40, xcor()-100, ycor()+65, couleurVoiture)
    dessineTrait(xcor(), ycor(), 110, 180, couleurVoiture)
    traitDeplacement(xcor(), ycor(), xcor()-40, ycor()-25, couleurVoiture)
    dessineTrait(xcor(), ycor(), 190, 0, couleurVoiture)
    end_fill()

    traitDeplacement(xcor(), ycor(), xcor()-40, ycor()+25, 'black', 3)
    dessineTrait(xcor(), ycor(), 110, 180, 'black', 3)
    traitDeplacement(xcor(), ycor(), xcor()-40, ycor()-25, 'black', 3)
    dessineTrait(xcor(), ycor(), 190, 0, 'black', 3)
    traitDeplacement(xcor()-40, ycor()+25, xcor()-20, ycor(), 'black', 3)
    traitDeplacement(xcor()-130, ycor() +25, xcor()-150, ycor() , 'black', 3)
    traitDeplacement(xcor() +75, ycor() +25, xcor() +75, ycor() , 'black', 3)
    

    dessineTrait(xcor()-165, ycor()-31, 10,0 , couleurVoiture, 40) 
    dessineTrait(xcor()-35, ycor() -9, 65, 0, 'grey', 10)
    dessineTrait(xcor()+220, ycor(), 65, 0, 'grey', 10)
    dessineTrait(xcor()-330, ycor()+20, 10, 0, 'white' ,7)
    traitDeplacement(xcor()+285, ycor()+2, xcor()+290, ycor()+2, 'orange',5)


def dessineArbre():
    xArbre = lireEntierClavier("Entrez le x du point bas-gauche de l'arbre : ", LARGEUR_MIN, LARGEUR_MAX)
    yArbre = lireEntierClavier("Entrez le y du point bas-gauche de l'arbre : ", HAUTEUR_MIN, HAUTEUR_MAX)
    couleurFeuilles = input("De quelle couleur est le feuillage (en hexadécimal ou en anglais) : ")
    largArbre = lireEntierClavier("Entrez la largeur de l'arbre (10-50) : ", 10, 50)
    hautArbre = lireEntierClavier("Entrez la hauteur de l'arbre (10-300) : ",10, 300)

    dessineRectangle(xArbre, yArbre, largArbre, 2*hautArbre/3, '#3D0000')
    aller(xArbre+(largArbre/2), yArbre, 0)
    
dessineArbre()



