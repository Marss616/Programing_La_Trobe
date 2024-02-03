def draw_big_x(character, size): # create the function for the big x to be called
    if size < 3: # logic for the syntax for the size of the box.
        print("Size must be at least 3.") # print error message if size is less than 3.

    for x in range(size): # crate the for main for loop for the size of the box.

        line = [" "] * size # create the line for the box with the size of the box.
        line[x] = character # the value of the line is the character for the box.

        left_position = x # set the character at the 'left' position for the 'X'
        line[left_position] = character # set the character at the 'left' position for the 'X' with the size of the box.

        right_position = size - x - 1 # set the character at the 'right' position for the 'X' with the size of the box, this will provide the left padding
        line[right_position] = character # set the character at the 'right' position for the 'X' with the size of the box, this will provide the right padding
        print("".join(line)) # print the line to the console for user feedback.

user_input_char = input("Enter a char to make your box: ") # get the users input for the character to be used for the 'draw_big_x' function
user_input_size = int(input("Enter a size to make your box: ")) # get the users input for the size to be used for the 'draw_big_x' function


draw_big_x(user_input_char, user_input_size) # call the 'draw_big_x' function with the user input for the character and size, and display in console

