# Define the function
def password_check(password):
    if len(password) < 8:
        return "Password is too short."
    elif len(password) > 20:
        return "Password is too long."
    else:
        return "Password length is acceptable."

# Example usage
input_password = input("What is your password: ")
result = password_check(input_password)
print(result)
