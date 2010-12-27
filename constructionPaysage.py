from turtle import *
from fonction import *

continuer = 1
print("Bienvenue dans le constructeur de paysage.")
print("Ce logiciel a été crée par VENANT Fanny, REDOLFI Camille et FILIPPI Jeff.")
print("\n\n\n")
print("Que veux-tu faire : ")
print("1. Création de paysage manuelle")
print("2. Création de paysage guidée")
typeCreation = lireEntierClavier("Choisis le numéro correspond à ton choix : ",1,2)

if typeCreation == 1:

    print("Vous êtes dans le mode de création manuel, libre. Vous pouvez faire tout ce que vous voulez.")
    momentDuJour = lireChaineClavier("C'est la nuit ou le jour ? : ", nuit,  jour)
    if momentDuJour == 'nuit' or momentDuJour == 'Nuit':
        lampadaireAllume = True
        bgcolor('#06011d')
    else momentDuJour == 'jour' or momentDuJour == 'Jour':
        lampadaireAllume = False
        bgcolor('blue')
    while continuer == 1:
            
        print("Quelle catégorie d'éléments ?")
        print(" 0. Retour au menu")
        print(" 1. Catégorie Ville")
        print(" 2. Catégorie Mer")
        print(" 3. Catégorie Campagne")
        print(" 4. Catégorie Ciel")
        choixCategorie = lireEntierClavier("Choisis le numéro correspondant à ton choix : ",1,4)
        
        while choixCategorie == 1:
            print("Quel élément ?")
            print("0. Retour aux catégories")
            print("1. Route")
            print("2. Maison")
            print("3. Voiture")
            print("4. Arbre")
            print("5. Drapeau")
            print("6. Lampadaire")
            choix = lireEntierClavier("Choisis le numéro correspondant à ton choix :", 0, 6)
            if choix == 0: choixCategorie = 0
            elif choix == 1: dessineRoute()
            elif choix == 2: dessineMaison()
            elif choix == 3: dessineVoiture()
            elif choix == 4: dessineArbre()
            elif choix == 5: dessineDrapeau()
            elif choix == 6: dessineLampadaire()
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
        while choixCategorie == 4:
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
    
