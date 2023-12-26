# Get input from the user
input_text = input("Enter a string: ")

# Calculate the necessary dimensions
num_chars = len(input_text)
height = num_chars + 2  # For the top and bottom borders

# the top
print("+" + "-" * (3) + "+")

# mid with char
for char in input_text:
    print("| " + char + " |")

# the bottom
print("+" + "-" * (3) + "+")