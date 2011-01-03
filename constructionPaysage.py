from turtle import *
setup(1280, 1024)
bgcolor('white')
speed(0)
ht()
reset()
continuer = 1
from paysage import *


print("Bienvenue dans le constructeur de paysage.")
print("Ce logiciel a été crée par VENANT Fanny, REDOLFI Camille et FILIPPI Jeff. Il est actuellement en version 1.0")
print("Logiciel optimisé pour des résolutions d'écrans supérieures à 1280*970")
print("\n\n\n")
print("Que veux-tu faire : ")
print("1. Création de paysage manuelle")
print("2. Création de paysage guidée")
typeCreation = lireEntierClavier("Choisis le numéro correspond à ton choix : ",1,2)



if typeCreation == 2:
    print("Vous êtes dans le mode de création guidée. Vous serez amené pas à pas au paysage selon vos choix.")
    print("Fait-il jour ou fait-il nuit ?")
    momentDuJour = 'momentDuJour'
    emplacementAstre = ''
    endroit = ''
    while momentDuJour != 'jour' and momentDuJour != 'nuit':
        momentDuJour = input("Il fait ")
    if momentDuJour == 'nuit':
        bgcolor('#001169')
        print("Où se trouve la lune ? à gauche à groite ou au milieu ?")
        while emplacementAstre != 'gauche' and emplacementAstre != 'droite' and emplacementAstre != 'milieu':
            emplacementAstre = input("La lune est à/au ")
        if emplacementAstre == 'gauche': dessineLune(LARGEUR_MIN+80, HAUTEUR_MAX - 100, 90, 1)
        elif emplacementAstre ==  'droite': dessineLune(LARGEUR_MAX -80, HAUTEUR_MAX-100, 90, 1)
        elif emplacementAstre == 'milieu': dessineLune(0, HAUTEUR_MAX-100, 90,1)


        for i in range(0,15):
            dessineEtoile(2,1)
    elif momentDuJour == 'jour':
        bgcolor('#92e7ff')
        print("Où se trouve le soleil ? à gauche à droite ou au milieu ?")
        while emplacementAstre != 'gauche' and emplacementAstre != 'droite' and emplacementAstre != 'milieu':
            emplacementAstre = input("Le soleil est à/au ")
        if emplacementAstre == 'gauche': dessineSoleil(LARGEUR_MIN+ 80, HAUTEUR_MAX - 100, 90, 1)
        elif emplacementAstre ==  'droite': dessineSoleil(LARGEUR_MAX - 130, HAUTEUR_MAX-100, 90, 1)
        elif emplacementAstre == 'milieu': dessineSoleil(0, HAUTEUR_MAX-100, 90,1)
        

        
    print("On peut aller en ville ou à la mer.")
    print("Où voulez-vous aller ?")
    while endroit != 'ville' and endroit != 'mer':
        endroit = input("Je veux aller vers la ")

    if endroit == 'ville':
        dessineRectangle(LARGEUR_MIN, HAUTEUR_MIN, 2*LARGEUR_MAX, HAUTEUR_MAX/2 + 150, 'dark green')
        dessineRoute(LARGEUR_MIN, HAUTEUR_MIN/4 - 150, 150, 2*LARGEUR_MAX, 1)
        print("Il y a des maisons de part et d'autres de la route, mais... combien ?")
        nbrMaison = lireEntierClavier("Nombre de maison(s) (1-4) : ", 1, 4)
        espaceVide = (2*LARGEUR_MAX - nbrMaison * 130) / (nbrMaison+1)
        aller(LARGEUR_MIN, HAUTEUR_MAX/2 + 20)
        listeCouleur = ['grey', 'brown', 'red', 'purple', 'blue', 'green', 'yellow', 'white', 'pink', 'cyan', 'orange'] 
        for i in range(0, nbrMaison):
            aller(xcor() + espaceVide/2, HAUTEUR_MIN/2 + 140)
            if momentDuJour == 'jour' or momentDuJour == 'Jour':
                allumer = 0
            else:
                allumer = 1
                print(allumer)
            dessineLampadaire(xcor(), ycor(), 'black', 1, allumer)
            aller(xcor() + espaceVide/2, HAUTEUR_MIN/2 + 140)
            xMaison = xcor()
            yMaison = ycor()
            couleurMaison = listeCouleur[randint(0,10)]
            couleurToit = listeCouleur[randint(0,10)]
            couleurPorte = listeCouleur[randint(0,10)]
            couleurEtages = listeCouleur[randint(0,10)]
            dessineMaison(xMaison, yMaison, couleurMaison, couleurToit, couleurPorte)

        print("Je vois une voiture !")
        couleurVoiture = listeCouleur[randint(0,10)]
        dessineVoiture(LARGEUR_MAX-200, HAUTEUR_MIN/2 + 50, 20,couleurVoiture, demander = 1)
        for j in range(0,4):
            for i in range(0,7):
                aller(LARGEUR_MAX-300 + i*20, HAUTEUR_MIN + 30*(j+1))
                dessineFleur(xcor(), ycor(), 20, 1)
        print("Tiens, un arbre !")
        dessineArbre(LARGEUR_MIN + 50, HAUTEUR_MIN)
        dessineArbre(LARGEUR_MIN + 150, HAUTEUR_MIN)
        dessineArbre(LARGEUR_MIN + 100, HAUTEUR_MIN)

    elif endroit == 'mer':
        temps = ''
        print("Il y a beaucoup de vent aujourd'hui, crois-tu que la mer est agitée ?")
        while temps != 'agitée' and temps != 'agitee' and temps != 'calme':
            temps = input("La mer est ")        
        dessineMer(momentDuJour, temps, 1)
        dessineSable(LARGEUR_MIN,HAUTEUR_MIN, 2*LARGEUR_MAX, HAUTEUR_MAX/3,momentDuJour, 1)
        if emplacementAstre == 'gauche':
            dessineBouee(LARGEUR_MAX - 110, HAUTEUR_MIN + 60,1)
            dessinePhare(LARGEUR_MIN+80,HAUTEUR_MIN,1)
            dessineDauphin(LARGEUR_MIN + 200, HAUTEUR_MIN+300, 1)
        elif emplacementAstre ==  'droite':
            dessineBouee(LARGEUR_MIN+ 150, HAUTEUR_MIN + 60,1)
            dessinePhare(0, HAUTEUR_MIN+100,1)
            dessineDauphin(LARGEUR_MAX-200, HAUTEUR_MIN+300, 1) 
        elif enplacementAstre == 'milieu':
            dessineBouee(LARGEUR_MIN+ 150, HAUTEUR_MIN + 60,1)
            dessinePhare(LARGEUR_MAX - 110, HAUTEUR_MIN, 120,1)
            dessineDauphin(0, HAUTEUR_MAX + 300, 1)

        

    if emplacementAstre == 'gauche':
        dessineNuage(LARGEUR_MAX - 110, HAUTEUR_MAX-150, 120)
        dessineNuage(0, HAUTEUR_MAX-200, 120)

    elif emplacementAstre ==  'droite':
        dessineNuage(LARGEUR_MIN+ 150, HAUTEUR_MAX - 150, 120)
        dessineNuage(0, HAUTEUR_MAX-200, 120)

    elif enmplacementAstre == 'milieu':
        dessineNuage(LARGEUR_MIN+ 150, HAUTEUR_MAX - 150, 120)
        dessineNuage(LARGEUR_MAX - 110, HAUTEUR_MAX-150, 120)
       
        
elif typeCreation == 1:
        
    print("Vous êtes dans le mode de création manuelle, libre. Vous pouvez faire tout ce que vous voulez.")
    couleurBackground = lireCouleurClavier("Entrez la couleur de fond de votre paysage (en hexadécimal ou en anglais) : ",1)
    bgcolor(couleurBackground)
    while continuer == 1:
                
        print("Quelle catégorie d'éléments ?")
        print(" 1. Catégorie Ville")
        print(" 2. Catégorie Mer")
        print(" 3. Catégorie Ciel")
        print(" 4. Effacer l'écran")
        choixCategorie = lireEntierClavier("Choisis le numéro correspondant à ton choix : ",1,4)
                
        while choixCategorie == 1:
                width(1)
                print("Quel élément ?")
                print("0. Retour aux catégories")
                print("1. Route")
                print("2. Maison")
                print("3. Voiture")
                print("4. Arbre")
                print("5. Lampadaire")
                print("6. Fleur")
                choix = lireEntierClavier("Choisis le numéro correspondant à ton choix : ", 0, 6)
                if choix == 0: choixCategorie = 0
                elif choix == 1: dessineRoute()
                elif choix == 2:
                    print("Où voulez-vous dessinez votre maison ?")
                    print("Entrez les coordonnées du point bas-gauche de la maison : ")
                    x = lireEntierClavier("Le x du point bas gauche de la maison : ", LARGEUR_MIN, LARGEUR_MAX)
                    y = lireEntierClavier("Le y du point bas gauche de la maison : ", HAUTEUR_MIN, HAUTEUR_MAX)
                    couleurMaison = lireCouleurClavier("Entrez la couleur de la maison (en hexadécimal ou en anglais) : ")
                    couleurPorte = lireCouleurClavier("Entrez la couleur de la porte (en hexadécimal ou en anglais) : ")
                    largeur = lireEntierClavier("Entrez la largeur de la maison (50-200) : ",50, 200)
                    hauteur = lireEntierClavier("Entrez la hauteur de la maison (50-300) : ",50, 300)
                    nbrEtagesMaison = lireEntierClavier("Entrez le nombre d'étages (entre 1 et 10) : ", 1, 10)
                    if nbrEtagesMaison == 1:
                        dessineMaison(x,y,couleurMaison,couleurPorte,largeur, hauteur,0)
                    else:
                        dessineMaison1(x,y,hauteur,largeur,couleurMaison,couleurPorte,nbrEtagesMaison, demander=0)

                elif choix == 3: dessineVoiture()
                elif choix == 4: dessineArbre1()
                elif choix == 5: dessineLampadaire()
                elif choix == 6: dessineFleur(demander = 1)
                if choix != 0:
                    continuer = lireEntierClavier("Voulez-vous continuer de dessiner ? (1 pour continuer, 0 pour arrêter) : ", 0, 1)
                
        while choixCategorie == 2:
                width(1)
                print("Quel élément ?")
                print("0. Retour aux catégories")
                print("1. Mer")
                print("2. Dauphin")
                print("3. Bouée")
                print("4. Sable")
                print("5. Phare")
                choix = lireEntierClavier("Choisis le numéro correspondant à ton choix : ", 0, 5)
                if choix == 0: choixCategorie = 0
                elif choix == 1: dessineMer()
                elif choix == 2: dessineDauphin()
                elif choix == 3: dessineBouee()
                elif choix == 4: dessineSable()
                elif choix == 5: dessinePhare()
                if choix != 0:
                    continuer = lireEntierClavier("Voulez-vous continuer de dessiner ? (1 pour continuer, 0 pour arrêter) : ", 0, 1)
                    
        while choixCategorie == 3:
                width(1)
                print("Quel élément ?")
                print("0. Retour aux catégories")
                print("1. Étoiles")
                print("2. Soleil")
                print("3. Lune")
                print("4. Nuage")
                choix = lireEntierClavier("Choisis le numéro correspondant à ton choix :", 0, 4)
                if choix == 0: choixCategorie = 0
                elif choix == 1: dessineEtoile()
                elif choix == 2: dessineSoleil()
                elif choix == 3: dessineLune(couleur = couleurBackground )
                elif choix == 4: dessineNuage(demander = 0)
                continuer = lireEntierClavier("Voulez-vous continuer de dessiner ? (1 pour continuer, 0 pour arrêter) : ", 0, 1)
                if continuer == 0:
                    choixCategorie = 0
                    
            
                    
        if choixCategorie == 4:
            reset()
            bgcolor("white")
            couleur = lireCouleurClavier("La nouvelle couleur du fond d'écran (en hexadécimal ou en anglais) : ", 1)
            bgcolor(couleur)


print("Admirez votre paysage !")
