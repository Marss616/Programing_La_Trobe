
rates = {"EUR": 0.59, "USD": 0.64, "CAD": 0.87, "NZD": 1.08, } # define the conversion rates 

amount = float(input("Enter an amount in AUD (Case Sensitive): ")) # take input of amount to convert
currency = input("Enter currency to convert to (EUR, USD, CAD, NZD): ") # get users desired currency converter

if currency in rates:
    converted_amount = amount * rates[currency] # Calculate the answer
    print(f"That iss: {converted_amount} {currency}.") # Format and print the answer to the end user
else:
    print("Invalid currency.") # Let user know if they inputed a bad currency,