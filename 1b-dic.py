#!/usr/bin/python3
# Description: Demander une saisie utilisateur de plusieurs prénoms
# Author: Thomas HATUEL
# Date: 23/10/2018
print("saisissez les pr�noms appuyez sur q pour arreter la saisie")
loop = 0
liste = []
while loop == 0:
    print("saisissez un prenom")
    value = input()
    if value == "q":
        liste = sorted(liste)
        for prenom in liste:
            print(prenom)
        break
    else:
        liste.append(value)