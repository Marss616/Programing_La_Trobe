def password_check(password):
    if len(password) < len('########'):
        # Your logic here (e.g., print a message or take some action)
        print("Password is too short.")
    else:
        # Logic for when the password length is sufficient
        print("Password length is sufficient.")


password_input = str(input("what is the password"))

password_check(password_input)