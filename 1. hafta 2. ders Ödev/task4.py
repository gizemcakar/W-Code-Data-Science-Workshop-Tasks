# 4 - password attempts are 3. when password is not matched, decleare attempts left. #

correct_password = str(input("create a password: "))
attempts = 3

for attempt in range(3):
    password = input("Enter your password: ")

    if password == correct_password:
        print("Access successfull!")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Wrong password! Attempts left: {attempts}")
        else:
            print("Wrong password! No attempts left. Access denied!")