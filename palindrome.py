word = input("Please type in a word: ")

if word == word[::-1]:
    print(f"The word {word} is a palindrome")
else:
    print("This word isn't a palindrome")