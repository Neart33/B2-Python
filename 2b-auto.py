#!/usr/bin/python3
# Description: Ecrire un programme qui résout le programme précédent
# Author: Thomas HATUEL
# Date: 15/10/2018

import random

secret = random.randint(0, 100)
count = 0
throw = random.randint(0, 100)

while secret != throw:
    throw = random.randint(0, 100)
    count += 1

with open("2b-write.txt", "w") as f:
    f.write("try number: ")
    f.write(str(count)+"\n")
    f.write("number that was guessed: ")
    f.write(str(secret)+"")