import random

number = random.randint(1, 10)
guessed = False

while not guessed:
    shot = int(input("Guess a number between 1 and 10: "))
    if shot == number:
        print("You guessed it!")
        zgadniete = True
        break
    elif shot > number:
        print("Nearly there, try lower number")

    else:
        print("Nearly there, try higher number")