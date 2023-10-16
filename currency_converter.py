"""
Kalkulator walut: Napisz program, który dokonuje konwersji między różnymi walutami, przy użyciu aktualnych kursów wymiany.
"""

values = {
    "USD": 1.0,
    "EUR": 0.95,
    "GBP": 0.82,
    "PLN": 4.22,
}

while True:
    source_currency = input("Please type in a source currency for example (USD, EUR, GBP, PLN): ").upper()
    destination_currency = input("Please type in a destination currency for example (USD, EUR, GBP, PLN): ").upper()
    amount = float(input("Please type in a amount you want to convert: "))
    
    if source_currency in values and destination_currency in values:
        final_amount = amount * (values[destination_currency] / values[source_currency])
        formated = "{:.2f}".format(final_amount)
        print(f"{amount} {source_currency} is {formated} {destination_currency}")
        break
    else: 
        print("This currency is not supported")