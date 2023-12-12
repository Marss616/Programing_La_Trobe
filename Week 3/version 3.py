# version 3

# take a 13 int input and remove the first 3 numbers of the input

int_13_len_input = input("what is the value of the input, 13 numbers only")

while len(int_13_len_input) > len(str(11111111111111)) or len(int_13_len_input) < len(str(111111111111)):
    print("Error, The length of int_13_len_input is greater than the length of 13.")
    int_13_len_input = input("Try again, what is the value of the input, 13 numbers only")
    
    if len(int_13_len_input) == len(str(1111111111111)):
        print("your input is", int_13_len_input)
        break



