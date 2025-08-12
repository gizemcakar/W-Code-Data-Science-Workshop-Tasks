# 3 - password must be equally or more than 5 and equally or less than 10 characters. #
while True:
    password2 = str(input("Please enter a password: "))
    if len(password2) >= 5 and len(password2) <= 10: # or 5 <= len(password2) <= 10
        print("Your account is created!")
        break   # Exits the loop when password is valid
    print("Your password must be equally or more than 5 and equally or less than 10 characters, please try again!")