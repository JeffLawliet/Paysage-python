def lireEntierClavier(phrase):
    valeur = None
    while valeur == None:
        try:
            valeur = int(input("Entrez un nombre : "))
        except ValueError:
            pass
        
    return valeur
        

