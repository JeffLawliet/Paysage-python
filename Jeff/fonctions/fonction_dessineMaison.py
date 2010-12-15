def dessineMaison():
    print("Où voulez-vous dessinez votre maison ?")
    
    print("Entrez les coordonnées du point bas-gauche de la maison : ",end="")
    xMaison = lireEntierClavier("Le x de la maison : ",+)
    yMaison = lireEntierClavier("Le y de la maison : ",+)
    largeurMaison = input("Entrez la hauteur de la maison : ",+)
    hauteurMaison = input("Entrez la largeur de la maison : ",+)
    couleurMaison = input("Entrez la couleur de la maison (en hexadécimal ou en anglais) : "))
    dessineRectangle(xMaison, yMaison, largeurMaison, hauteurMaison, couleurMaison)

    toit = input("Voulez-vous un toit (Oui/Non) : ")
    while toit != (Non or non or Oui or oui):
        print("Veuillez recommencer.")
        toit = input("Voulez-vous un toit (Oui/Non) : ")
    if toit = (Oui or oui):
        couleurToit = input("Entrez la couleur de votre toit : "))
        dessineTriangle(xMaison+hauteurMaison, yMaison, largeurMaison, couleurToit)
        
    nbrEtagesMaison = lireEntierClavier("Entrez le nombre d'étages : ",+)
    couleurEtages = lireStringClavier("Entrez la couleur de l'étage : ")
    for i in range(1,nbrEtages):
        
        aller(x,y+i*(hauteurMaison/nbrEtages),0)
        dessineTrait(xcor(), ycor(), largeurMaison, 0, couleurEtages)

    xPorte = xMaison + (2*largeurMaison)/5
    largeurPorte = largeurMaison/3
    hauteurPorte = 2*hauteurMaison/3*nbrEtagesMaison
    couleurPorte = input("Entrez la couleur de votre porte : ")
    dessineRectangle(xPorte, yPorte, largeurPorte, hauteurPorte, couleurPorte)

    nbrFenetresEtagesMaison = lireEntierClavier("Entrez le nombre de fenêtre par étages de votre maison : ",+)
    couleurFenetresMaison = input("Entrez la couleur des fenêtres de votre maison : ")
    dessineFenetre(nbrFenetresEtagesMaison,nbrEtagesMaison,hauteurMaison,largeurMaison, couleurFenetresMaison, xMaison, yMaison)

    
