from turtle import *
setup(1280, 1024)
from fonction import *


continuer = 1
print("Bienvenue dans le constructeur de paysage.")
print("Ce logiciel a été crée par VENANT Fanny, REDOLFI Camille et FILIPPI Jeff. Il est actuellement en version 1.0")
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
        bgcolor('blue')
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
        dessineRectangle(LARGEUR_MIN, HAUTEUR_MIN, 2*LARGEUR_MAX, HAUTEUR_MAX/2 + 150, 'green')
        dessineRoute(LARGEUR_MIN, HAUTEUR_MIN/4 - 150, 150, 2*LARGEUR_MAX, 1)
        print("Il y a des maisons de part et d'autres de la route, mais... combien ?")
        nbrMaison = lireEntierClavier("Nombre de maison(s) (1-4) : ", 1, 4)
        espaceVide = (2*LARGEUR_MAX - nbrMaison * 130) / (nbrMaison+1)
        aller(LARGEUR_MIN, HAUTEUR_MAX/2 + 20)
        listeCouleur = ['black', 'grey', 'brown', 'red', 'purple', 'blue', 'green', 'yellow', 'white', 'pink', 'cyan', 'orange'] 
        for i in range(0, nbrMaison):
            aller(xcor() + espaceVide, HAUTEUR_MIN/2 + 140)
            xMaison = xcor()
            yMaison = ycor()
            couleurMaison = listeCouleur[randint(0,11)]
            couleurToit = listeCouleur[randint(0,11)]
            couleurPorte = listeCouleur[randint(0,11)]
            couleurEtages = listeCouleur[randint(0,11)]
            dessineMaison(xMaison, yMaison, couleurMaison, couleurToit, couleurPorte, 1)

        print("Je vois une voiture !")
        couleurVoiture = lireCouleurClavier("De quelle couleur était la voiture ?")
        dessineVoiture(LARGEUR_MAX-200, HAUTEUR_MIN/2, 20,couleurVoiture, demander = 1)

    print("Je crois voir un nuage dans le ciel")

    if emplacementAstre == 'gauche':
        dessineNuage(LARGEUR_MAX - 130, HAUTEUR_MAX-150, 120, 'white')
        dessineNuage(0, HAUTEUR_MAX-200, 120,'white')
    elif emplacementAstre ==  'droite':
        dessineNuage(LARGEUR_MIN+ 130, HAUTEUR_MAX - 150, 120, 'white')
        dessineNuage(0, HAUTEUR_MAX-200, 120,'white')
    elif enmplacementAstre == 'milieu':
        dessineNuage(LARGEUR_MIN+ 130, HAUTEUR_MAX - 150, 120, 'white')
        dessineNuage(LARGEUR_MAX - 130, HAUTEUR_MAX-150, 120, 'white')
        
elif typeCreation == 1:
        
    print("Vous êtes dans le mode de création manuelle, libre. Vous pouvez faire tout ce que vous voulez.")
    couleurBackground = lireCouleurClavier("Entrez la couleur de fond de votre paysage (en hexadécimal ou en anglais) : ",1)
    bgcolor(couleurBackground)
    while continuer == 1:
                
        print("Quelle catégorie d'éléments ?")
        print(" 1. Catégorie Ville")
        print(" 2. Catégorie Mer")
        print(" 3. Catégorie Ciel")
        choixCategorie = lireEntierClavier("Choisis le numéro correspondant à ton choix : ",1,4)
                
        while choixCategorie == 1:
                print("Quel élément ?")
                print("0. Retour aux catégories")
                print("1. Route")
                print("2. Maison")
                print("3. Voiture")
                print("4. Arbre")
                print("5. Lampadaire")
                choix = lireEntierClavier("Choisis le numéro correspondant à ton choix :", 0, 6)
                if choix == 0: choixCategorie = 0
                elif choix == 1: dessineRoute()
                elif choix == 2: dessineMaison()
                elif choix == 3: dessineVoiture()
                elif choix == 4: dessineArbre()
                elif choix == 5: dessineLampadaire()
                continuer = lireEntierClavier("Voulez-vous continuer de dessiner ? (1 pour continuer, 0 pour arrêter)", 0, 1)
                if continuer == 0:
                    choixCategorie == 0
                
        while choixCategorie == 2:
                print("Quel élément ?")
                print("0. Retour aux catégories")
                print("1. Mer")
                print("2. Bateau")
                print("3. Dauphin")
                print("4. Bouée")
                print("5. Sable")
                print("6. Phare")
                print("7. Rochers")
                choix = lireEntierClavier("Choisis le numéro correspondant à ton choix :", 0, 7)
                if choix == 0: choixCategorie = 0
                elif choix == 1: dessineMer()
                elif choix == 2: dessineBateau()
                elif choix == 3: dessineDauphin()
                elif choix == 4: dessineBouee()
                elif choix == 5: dessineSable()
                elif choix == 6: dessinePhare()
                elif choix == 7: dessineRochers()
                continuer = lireEntierClavier("Voulez-vous continuer de dessiner ? (1 pour continuer, 0 pour arrêter)", 0, 1)
                if continuer == 0:
                    choixCategorie = 0
                    
        while choixCategorie == 3:
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
                elif choix == 3: dessineLune()
                elif choix == 4: dessineNuage()
                continuer = lireEntierClavier("Voulez-vous continuer de dessiner ? (1 pour continuer, 0 pour arrêter)", 0, 1)
                if continuer == 0:
                    choixCategorie = 0

print("Admirez votre paysage !")
