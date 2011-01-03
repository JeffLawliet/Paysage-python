from turtle import *
setup(1280,1024)
from fonction import *

reset()
speed(0)
ht()

print("Quel exemple de paysage ?")
print("1. Paysage 1")
print("2. Paysage 2")
print("3. Paysage 3")
choix= lireEntierClavier("Entrez le nombre de votre choix : ",1,3)

if choix == 1:
    bgcolor('#06011d')    
    for i in range(100):
        dessineEtoile(2,1)

    dessineLune(-500,200,250,1,'#06011d')

    dessineMer('nuit','calme',1)

    dessineSable(-140,-500,840,300,'nuit',0)

    dessinePhare(-40,-100,1)

    dessineMaison(90,-350,'#F6E497','#B9121B','#4C1B1B',1,500,200)

    dessinePlot(-115,100)

    dessinePlot(-115,-110)

elif choix == 2:
    									
      
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

    dessineVoiture(LARGEUR_MAX-50,HAUTEUR_MIN+150,50,'purple',1)
    dessineVoiture(LARGEUR_MIN+200,HAUTEUR_MIN+150,50,'red',1)

elif choix == 3:
        
    bgcolor('#ABC8E2')

    dessineMer('jour','agitée',1)
    dessineSoleil(-590,350,60,1)
    dessineNuage(100,200,150,'grey')
    dessineNuage(150,250,200,'grey')
    dessineNuage(600,210,250,'grey')

    dessineDauphin(-50,-100,1)
    dessineDauphin(-300,-200,1)

    dessineRectangle(250,-300,500,350,'black')
    dessineTriangle(250,-300,60,404,'black')

    dessineBouee(400,-100,1)

    color('blue')
    dessineVague1(600,-305,50,400)
