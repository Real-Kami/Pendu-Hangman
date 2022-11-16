from random import *

def longueur():                         #ouvre le fichier texte et compte les lignes
    fichier=open("liste_de_mots.txt")
    l=0
    for ligne in fichier:
        l=l+1
    fichier.close
    return l


def randommot():                        #Choisi un mot au hasard entre 0 et la longueur du fichier
    fichier=open("liste_de_mots.txt")
    numéroligne=randint(1, longueur())
    for i in range (numéroligne):
        contenu=fichier.readline()
    fichier.close
    return contenu

def lettreDansMot(lettre):
    index = []                          #initialise une liste
    lettrePresente = False              #par défaut, la lettre est considéré comme absente du mot
    for i in range(len(mot)):           #pour toutes les lettres du mot :
        if lettre == mot[i]:            #si la lettre du mot est la lettre recherché
            lettrePresente = True
            index = index + [i]         #on ajoute à la liste la position de la lettre
    if lettrePresente == True:
        return index                    #si la lettre est présente dans le mot on renvoie la liste de ses positions
    return "ABSENT"                     #si la lettre est absente, on renvoie le code "ABSENT"

def dessinPendu(nb):  #renvoie des représentations graphiques du pendu
    tab=[
    """

    """,
    """
    ______
    """,
    """
       |
       |
       |
    ___|___
    """,
    """
        _____
       |
       |
       |
    ___|___
    """,
    """
        _____
       |     |
       |
       |
    ___|___
    """,
    """
        _____
       |     |
       |     o
       |
    ___|___
    """,
    """
        _____
       |     |
       |     o
       |     |
    ___|___
    """,
    """
        _____
       |     |
       |     o_
       |     |
    ___|___
    """,
    """
        _____
       |     |
       |    _o_
       |     |
    ___|___
    """,
    """
        _____
       |     |
       |    _o_
       |     |_
    ___|___
    """,
    """
        _____
       |     |
       |    _o_
       |    _|_
    ___|___
    """
    ]
    return tab[nb]

mot = randommot()           #initialisation des variables
mot = mot[:len(mot) - 1]
mot_devine = " " * len(mot)
lettres_absentes = ""

while len(lettres_absentes) < 10 and mot != mot_devine : #tant qu'il y a moins de dix lettres absentes et que le mot n'est pas deviné :

    lettre = ""                                          #(ré)initialise la variable lettre
    while len(lettre) < 1:                               #tant que lettre est une chaine de texte vide
        lettre = input("Entrer une lettre : ")           #demander à l'utilisateur
    lettre = lettre[0].upper()                           #mettre la lettre proposé en majuscule (uniformisation de l'affichage)

    ldm = lettreDansMot(lettre)                          #ldm prend la valeur lettreDansMot(), soit une liste contenant les positions de la lettre dans le mot ou bien la valeur "ABSENT" si la lettre n'est pas la
    if (ldm != "ABSENT"):                                #si la lettre est dans le mot
        for i in range(len(ldm)) :                       #pour tous les positions de la lettre dans le mot :
            index = ldm[i]
            mot_devine = mot_devine[:index] + lettre + mot_devine[index+1:] #découpe mot_devine en deux, ajoute la lettre trouvé par le joueur et recolle les deux parties.
    else :                                               #si la lettre n'est pas dans le mot
        lettres_absentes = lettres_absentes + lettre     #ajouter la lettre aux lettres absentes

    print(dessinPendu(len(lettres_absentes)  )) #rendu graphique
    print(mot_devine)                           #affiche la propostion du joueur
    print("=" * 50)                             #séparateur visuel


#une fois que l'on est sorti de la boucle :

if mot == mot_devine :      #si le mot a été deviné :
    print("tu as gagné !!!")
else :
    print("tu as perdu :(")
    print("Le mot était:")
    print(mot)




