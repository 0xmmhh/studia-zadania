import random

number = random.randint(1, 10)

num_of_tries = 0 
max_num_of_tries = 5

while num_of_tries < max_num_of_tries:
    try:
        shot = int(input("Guess a number between 1 and 10: "))
        num_of_tries += 1
        if num_of_tries == max_num_of_tries:
            print("Try again, you only have 5 tries")
        if shot == number:
            print(f"You guessed it in {num_of_tries} tries!")
            break
        elif shot > number:
            print("Try lower number")
        else:
            print("Try higher number")
    except ValueError:
        print("Please type in an integer!")