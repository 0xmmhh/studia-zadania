number = int(input("Please type in an integer: "))
for i in range(1, number+1):
    for j in range(i):
        print("*", end="")
    print()