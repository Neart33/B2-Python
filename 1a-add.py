#!/usr/bin/python3
# Description: Demander deux nombres à l’utilisateur et afficher le résultat
# Author: Thomas HATUEL
# Date: 23/10/2018
print("choisi un nombre")
value1 = input()
try:
    value1 = int(value1)
except ValueError:
    pass
print("choisi un autre nombre")
value2 = input()
try:
    value2 = int(value2)
except ValueError:
    pass
print("leurs somme est �gale a ")
print(value1 + value2)