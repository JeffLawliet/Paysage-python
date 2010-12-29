from turtle import *
from fonction import *

screensize(1024, 768)

continuer = 1
print("Bienvenue dans le constructeur de paysage.")
print("Ce logiciel a été crée par VENANT Fanny, REDOLFI Camille et FILIPPI Jeff.")
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
            emplacementAstre = input("La lune est à ")
        if emplacementAstre == 'gauche': dessineLune(LARGEUR_MIN+ 120, HAUTEUR_MAX - 200, 150, 1)
        elif emplacementAstre ==  'droite': dessineLune(LARGEUR_MAX - 120, HAUTEUR_MAX-200, 150, 1)
        elif emplacementAstre == 'milieu': dessineLune(0, HAUTEUR_MAX-200, 150,1)
    elif momentDuJour == 'jour':
        bgcolor('blue')
        print("Où se trouve le soleil ? à gauche à groite ou au milieu ?")
        while emplacementAstre != 'gauche' and emplacementAstre != 'droite' and emplacementAstre != 'milieu':
            emplacementAstre = input("Le soleil est à ")
        if emplacementAstre == 'gauche': dessineSoleil(LARGEUR_MIN+ 120, HAUTEUR_MAX - 200, 150, 1)
        elif emplacementAstre ==  'droite': dessineSoleil(LARGEUR_MAX - 120, HAUTEUR_MAX-200, 150, 1)
        elif emplacementAstre == 'milieu': dessineSoleil(0, HAUTEUR_MAX-200, 150,1)

    print("On peut aller en ville ou à la mer.")
    print("Où voulez-vous aller ?")
    while endroit != 'ville' and endroit != 'mer':
        endroit = input("Je veux aller vers la ")

    if endroit == 'ville':
        print("Vous voyez une route, qui s'éloigne vers l'horizon, ou qui traverse 

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
            continuer = lireEntierClavier("Voulez-vous continuer ? (1 pour continuer, 0 pour arrêter)", 0, 1)
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
            continuer = lireEntierClavier("Voulez-vous continuer ? (1 pour continuer, 0 pour arrêter)", 0, 1)
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
            continuer = lireEntierClavier("Voulez-vous continuer ? (1 pour continuer, 0 pour arrêter)", 0, 1)
        
