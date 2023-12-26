def print_receipt_item(name, price, tax_percent):
    print(name)
    print('    Price: $' + str(price))
    print('    Tax  : ' + str(tax_percent * 100) + '%')
    print('    Total: $' + str(price + price * tax_percent))

# now call the function
    
print_receipt_item('hat', 150, 15)