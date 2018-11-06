#!/usr/bin/python3
# Description: Demander une saisie utilisateur de plusieurs notes et prénoms 
# Author: Thomas HATUEL
# Date: 23/10/2018
print("saisissez votre note ensuite votre prenom")
Dict ={}
loop = 0
sum = 0
while loop == 0:
    print("saisissez un prenom")
    nom = input()
    if nom == "q":
        print("liste des notes")
        for liste in sorted(Dict):
            full = Dict[liste]
            print(full)
            sum += int(full)
        print("moyenne est �gale a ")
        moy = sum / len(Dict)
        print(moy)
        break
    else:

        print("saisissez votre note")
        note = input()
        try:
            note = int(note)
        except ValueError:
            pass
        Dict[nom] = note