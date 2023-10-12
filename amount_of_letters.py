word = input("Please type in a word or a sentence: ")
#replacing blank space(?) with nothing
without_spaces = word.replace(" ", "")

length_without_spaces = len(without_spaces)
#checking if there is blank space in word
if " " in word:
    print(f"Length of this sentence is {length_without_spaces}")
else:
    print(f"Length of this word is {length_without_spaces}")