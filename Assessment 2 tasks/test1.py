# calc the following expression 

def calculate():  # No parameter needed since we're getting user input inside the function
    x = input("What is X equal to?")  # Take the input from the user
    x = float(x)  # Convert the input to a float value
    return (2 + (1 - x) ** 3) / 4  # The logic of the program and what is to occur with the var value

answer = calculate() # call the above function
print("'Y' is equal to: ", answer) # print the output of the program to console
