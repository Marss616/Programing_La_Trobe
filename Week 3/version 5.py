# this is working logic

# Convert 13-digit ISBN starting with 978 to 10-digit ISBN
isbn = input("whats the input: ")

isbn = int(isbn)

if 9780000000000 <= isbn <= 9789999999999:
    isbn -= 9780000000000

# Determine the language based on the ISBN
if 0 <= isbn <= 1999999999:
    print("English") 
elif 2000000000 <= isbn <= 2999999999:
    print("French")
elif 3000000000 <= isbn <= 3999999999:
    print("German")
else:
    print("Unknown")