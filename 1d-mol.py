import random

secret = random.randint(0, 100)

guess = input()
try:
    guess = int(guess)
except ValueError:
    pass
print("choisi un nombre")
while secret != guess:
        if secret < guess:
            print("trop grand play again")
            guess = int(input())
        elif secret > guess:
            print("trop petit play again")
            guess = int(input())
        elif guess == "q":
            print("quit")
            print("game ended")
            break
print("la réponse était")
print(secret)