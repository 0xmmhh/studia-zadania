grade1 = int(input("Please type in your math grade: "))
grade2 = int(input("Please type in your physics grade: "))
grade3 = int(input("Please type in your biology grade: "))

average = grade1 + grade2 + grade3 / 3

formated = "{:.1f}".format(average)

print(f"Your average in these subjects is {formated}")