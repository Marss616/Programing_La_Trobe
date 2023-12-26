rows = int(input("rows: "))  # Number of rows in the box
columns = int(input("columns: "))  # Number of columns in the box

for x in range(rows):
    
    for y in range(columns):
        print("-", end="")  # Print a dash and stay on the same line
    print("")  # Move to the next line after finishing a row
