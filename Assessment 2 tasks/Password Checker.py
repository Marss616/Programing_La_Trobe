# Define the function
def password_check(password):
    # Check password length
    if len(password) < 8:
        return "Password is too short."
    elif len(password) > 20:
        return "Password is too long."

    # Initialize flags for special character and digit presence
    has_special = False
    has_digit = False

    # Check for at least one special character and digits
    for x in password:
        if x in "!@#$%^&*()-_+=[]{};:'\",.<>/?|`~ ":
            has_special = True
        if x in "1234567890":
            has_digit = True

    # Check conditions
    if not has_special:
        return "Password is invalid: password requires a special character."
    if has_digit:
        return "Password is invalid: password is not allowed to have a digit."

    return "Password is valid."
    
    # Example usage.

input_password = input("What is your password: ")
result = password_check(input_password)
print(result)
