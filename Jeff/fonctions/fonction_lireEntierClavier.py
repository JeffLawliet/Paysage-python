def lireEntierClavier(phrase,condition):
    valeur = None
    if condition == '+':
        valeur = -1

        while valeur == -1:
            try:
                valeur = int(input("Entrez un nombre : "))
            except ValueError:
                valeur = -1
        
    return valeur
        

