def password_check(password): # create the function with the parameter 'password'
    
    # create the variables for the function in the program to use.

    has_special = False
    has_digit = False
    has_duplicate = False
    seen_characters = set()

    # this first block will check that the password length is correct between 8 and 20 chars.

    if len(password) < 8: # if the password is < 8, retrun error message.
        return "Password is invalid:"
    elif len(password) > 20: # if the password is < 8, retrun error message.
        return "Password is invalid:"
    
    # this block will create the logic for the more complex processing of the password in this function.

    for x in password: # iterate though all letters and number in users password input 'x' is the letter/number in this case.
        if x in "!@#$%^&*()-_+=[]{};:'\",.<>/?|`~ ": # all special symbols added to a string value to be checked by the logic of the program/function.
            has_special = True
        elif x in "1234567890": # all special digits added to a string value to be checked by the logic of the program/function.
            has_digit = True
        elif x in seen_characters: # all 'x' values are stored and matched with each other so that no duplicate numbers are allowed.
            has_duplicate = True
        else:
            seen_characters.add(x) # add every 'x' value to the set 'seen_characters' to store to check if duplicate values present 

    # now time to check the conditions of the more complex functions for the value 'x' in password.
            
    if not has_special: # check that password has a special letter.
        return "Password is invalid:" # return input error message.
    if has_digit: # check that password does not have a digit.
        return "Password is invalid:" # return input error message.

    if has_duplicate: # check that password does not have duplicates.
        return "Password is invalid:" # return input error message.

    return "Password is valid." # after all checks return a 'valid password' message.

input_password = input("What is your password: ") # take the input for the function.
result = password_check(input_password) # call the function.
print(result) # display the output in the console.
