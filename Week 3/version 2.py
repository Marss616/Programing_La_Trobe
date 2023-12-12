# take a 13 int input and remove the first 3 numbers of the input

int_13_len_input = input("what is the value of the input, 13 numbers only: ")

int_13_len_input = int(int_13_len_input)

while int_13_len_input < len(int("1111111111111")) or int_13_len_input > len(int("11111111111111")):
    print("int_13_len_input is not within the specified length range")
    int_13_len_input = int(input("Enter a new value for int_13_len_input: "))

# The loop will exit when int_13_len_input is within the specified length range
print("int_13_len_input is within the specified length range now.")


