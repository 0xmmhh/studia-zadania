import sys

num_of_tries = 5
secret_word = "sukienka"
used_letters = []

user_word = []

def find(word, letter):
    indexes = []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)

    return indexes

def state():
    print()
    print(user_word)
    print("Number of tries left: ", num_of_tries)
    print("Used letters: ", used_letters)
    print()

###

for _ in secret_word:
    user_word.append("_")

while True:
    letter = input("Please type in a letter: : ")
    used_letters.append(letter)

    found_indexes = find(secret_word, letter)

    if len(found_indexes) == 0:
        print("This letter doesn't appear in secret word.")
        num_of_tries -= 1

        if num_of_tries == 0:
            print()
            print()
            print()
            print("GAME OVER")
            print()
            print()
            print()
            sys.exit(0)
    else:
        for index in found_indexes:
            user_word[index] = letter

        if "".join(user_word) == secret_word:
            print("That's the correct word!")
            sys.exit(0)
    
    state()