# Jack Bell 09 JAN 2024
# Type guesser

value = input("What is your input: ")

try:
    int(value)
    print("int")
except ValueError:
    try:
        float(value)
        print("float")
    except:
        str(value)
        print("str")
        
