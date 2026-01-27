print("===== CURRENCY CONVERTER =====")

# Fixed exchange rates (example)
rates = {
    "USD": 83.0,   # 1 USD = 83 INR
    "EUR": 90.0,   # 1 EUR = 90 INR
    "GBP": 105.0,  # 1 GBP = 105 INR
    "INR": 1.0
}

amount = float(input("Enter amount: "))
from_currency = input("From currency (USD, EUR, GBP, INR): ").upper()
to_currency = input("To currency (USD, EUR, GBP, INR): ").upper()

if from_currency in rates and to_currency in rates:
    # Convert to INR first, then to target currency
    amount_in_inr = amount * rates[from_currency]
    converted_amount = amount_in_inr / rates[to_currency]

    print(f"\n{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
else:
    print("Invalid currency code!")
