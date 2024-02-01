def compress_string(message): # create the function with the message parameter.


    # handle the input if the user inputs no value or void input.
    if message == "": # logic of the error message.
        return "Error no message to compress" # inform user that there was no input given .
    
    result = "" # create the 'result' variable.
    count = 1 # start the count at 1.
    prev_char = message[0] # character.
    
    for x in range(1, len(message)): # create the loop for the function to iterate though based on the length of the 'message parameter'
        
        char = message[x] # this will make 'char' value equal to the index of the first value in the list 'message'
        
        if char == prev_char:
            count += 1 # Increment the loop by + 1 to contine the function while the users prev_char value is not 0.
        else:
            result += str(count) # add count of last char to result so that the numb of compressions is displayed to the end user
            result += prev_char # add the compression value to the varible that will be the output for the function.
            
            count = 1 # reset the count if another input is added and the program was still running, usefull in a larger application.
            prev_char = char # reset the 'prev_char' value for the same above practices.
    
    # this block will add the two output varibles to the 'result' value to be returned to the user as output upon calling this function. 
    result += str(count) # this append current char to result to be able to retun the complete output.
    result += prev_char # this append current char to result to be able to retun the complete output.
    
    
    return result # end the function with returning the output of the compression with the user imput.

user_imput = input("What message do you want to compress? ") # get the users imput to use for the above created function.
compressed_string = compress_string(user_imput) # call the new fucntion.
print(compressed_string) # print the output to the console when program has gotten user input.

