#reversing string using while loop
""""
tekst = input("Podaj tekst: ")
reversed = ""
i = len(tekst) - 1
while i >= 0:
    reversed += tekst[i]
    i -= 1

print(f"Odwrocony tekst: {reversed}")
"""
#reversing string using simpler method

tekst = input("Podaj tekst")

tekst = tekst[::-1]

print(tekst)
