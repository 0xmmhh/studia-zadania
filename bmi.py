imie = input("Podaj swoje imię: ")
waga = float(input("Podaj swoją wagę: "))
wzrost = float(input("Podaj swoj wzrost w metrach: "))
print("Jak się czujesz?")
print("1. Dobrze")
print("2. Średnio")
print("3. Źle")

samopoczucie = input("Wybierz opcję (1/2/3): ")
if samopoczucie == "1":
    print("To super!")
if samopoczucie == "2":
    print("To średnio!")
if samopoczucie == "3":
    print("To bardzo źle!!")
    
bmi = waga / (wzrost**2)

formated = "{:.1f}".format(bmi)

if bmi >= 18.5 and bmi <= 24.99:
    print(f"Twoje BMI to {formated}, twoja waga jest w normie.")
elif bmi > 25:
    print(f"Twoje BMI to {formated}, masz nadwagę.")
elif bmi >= 17 and bmi <= 18.49:
    print(f"Twoje BMI to {formated}, masz niedowagę.")
