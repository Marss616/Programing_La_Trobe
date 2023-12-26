rows = 5  # Number of rows in the box
columns = 10  # Number of columns in the box

for x in range(rows):
    for y in range(columns):
        # Check if we're at a corner
        if (x == 0 and y == 0) or (x == 0 and y == columns - 1) \
           or (x == rows - 1 and y == 0) or (x == rows - 1 and y == columns - 1):
            print("*", end="")  # Print an asterisk for the corners
        else:
            print("-", end="")  # Print a dash for other positions
    print()  # Move to the next line after finishing a row
