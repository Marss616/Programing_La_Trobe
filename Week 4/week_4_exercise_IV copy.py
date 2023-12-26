# Get input from the user
input_string = input("Enter a string: ")

# Define the size of the box based on the input string length
columns = max(len(input_string), 2)  # Ensure a minimum width of 2 for the box
rows = max(3, len(input_string) // columns + 2)  # Calculate the number of rows

# Initialize a variable to keep track of the current position in the input string
string_pos = 0

# Loop through each row
for x in range(rows):
    # Loop through each column
    for y in range(columns):
        # Check for corners
        if (x == 0 and y == 0) or (x == 0 and y == columns - 1) \
           or (x == rows - 1 and y == 0) or (x == rows - 1 and y == columns - 1):
            print("*", end="")
        # Check for edges
        elif x == 0 or x == rows - 1 or y == 0 or y == columns - 1:
            print("-", end="")
        # Fill the inside with characters from the input string
        else:
            if string_pos < len(input_string):
                print(input_string[string_pos], end="")
                string_pos += 1
            else:
                print(" ", end="")  # Print a space if the string has ended
    print()  # Move to the next line after finishing a row
