def currency_converter():
    # Dictionary of conversion rates
    conversion_rates = {
        "EUR": 0.59,
        "USD": 0.64,
        "CAD": 0.87,
        "NZD": 1.08,
        # Two additional currencies
        "GBP": 0.53,  # Example rate for British Pound
        "JPY": 93.17  # Example rate for Japanese Yen
    }

    # User input for amount in AUD
    amount_aud = float(input("Enter an amount in AUD: "))

    # User input for target currency
    currency = input("Enter a currency: ").upper()

    # Conversion
    if currency in conversion_rates:
        converted_amount = amount_aud * conversion_rates[currency]
        print(f"{converted_amount:.2f} {currency}")
    else:
        print("Currency not supported.")

# Run the program
currency_converter()
