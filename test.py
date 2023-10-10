
#Zadanie pierwsze

print("Hello, World!")

#Zadanie drugie

wiek = int(input("Ile masz lat?"))
imie = input("Podaj swoje imię: ")
print(f"Twoje imię to: {imie}")

if imie != "Maciek":
    print("Nie jesteś mile widziany")
else:
    print("Jesteś mile widziany")

if wiek > 18:
    print("Super! Jesteś pełnoletni!")
else:
    print("Nie jesteś pełnoletni")

#Zadanie trzecie

def dodawanie(a,b):
    return a+b

def odejmowanie(a,b):
    return a-b

def mnozenie(a,b):
    return a*b

def dzielenie(a,b):
    if b != 0:
        return a/b
    else:
        return "Nie mozna dzielic przez zero"
    
print("Wybierz opcje: ")
print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnozenie")
print("4. Dzielenie")

wybor = input("Wybierz numer operacji (1/2/3/4): ")
if wybor in ('1','2','3','4'):
    num1 = float(input("Podaj pierwszą liczbę: "))
    num2 = float(input("Podaj drugą liczbę: "))

if wybor == "1":
    print("Wynik: ", dodawanie(num1, num2))
elif wybor == "2":
    print("Wynik: ", odejmowanie(num1, num2))
elif wybor == "3":
    print("Wynik: ", mnozenie(num1, num2))
elif wybor == "4":
    print("Wynik: ", dzielenie(num1, num2))

else:
    print("Błędny wybór")

#Zadanie 4

dlugosc = float(input("Podaj długość: "))
szerokosc = float(input("Podaj szerokość protokąta: "))

pole = dlugosc * szerokosc

print(f"Pole powierzchni prostokąta wynosi: {pole}")

#Zadanie 5

lista = [6,4,1,8,9,5,2,3,7]

najmniejsza = min(lista)
najwieksza = max(lista)

print(f"Najmniejsza liczba w liście: {najmniejsza}")
print(f"Największa liczba w liście: {najwieksza}")

#Zadanie 6

import random

losowa = random.randint(1, 9)
proby = 0

while True:
    user_choice = int(input("Wybierz cyfrę od 1 do 9: \n"))
    proby += 1

    if  user_choice == losowa:
        print(f"Brawo! Odgadłeś prawidłową cyfrę w {proby} próbach.")
        break
    elif user_choice < losowa:
        print("Zgadywana cyfra jest wieksza.")
    else:
        print("Zgadywana cyfra jest mniejsza.")