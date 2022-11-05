# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 13:55:08 2022

@author: Camille
"""

from random import *


def randommot():
    fichier=open("liste_de_mots.txt")
    numéroligne=randint(1, 2)
    for i in range (numéroligne):
        contenu=fichier.readline()
    fichier.close
    return contenu

def lettreDansMot(lettre):
    index = []
    lettrePresente = False
    for i in range(len(mot)):
        if lettre == mot[i]:
            lettrePresente = True
            index = index + [i]
    if lettrePresente == True:
        return index
    return "ABSENT"

def pendu(nb):
    tab=[
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

mot = randommot()
mot = mot[:len(mot) - 1]
mot_devine = " " * len(mot)
lettres_absentes = ""

while len(lettres_absentes) < 9 and mot != mot_devine :
    lettre = input("Entrer une lettre : ")
    lettre = lettre[0].upper()
    ldm = lettreDansMot(lettre)
    if (ldm != "ABSENT"):
        for i in range(len(ldm)) :
            index = ldm[i]
            mot_devine = mot_devine[:index] + lettre + mot_devine[index+1:]
    else :
        lettres_absentes = lettres_absentes + lettre
    print(pendu(len(lettres_absentes)  ))
    print(mot_devine)
    print("=" * 50)
    
if mot == mot_devine :
    print("tu as gagné !!!")
else :
    print("tu as perdu :c")
    

        
    