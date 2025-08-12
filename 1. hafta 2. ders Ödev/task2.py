# 2 - create an username and password which has equally or less than 6 characters. #
user_name = input("enter your user name: ")
password = str(input("create a password: "))

if len(password) <= 6:
    print("your account is created!")
else:
    print("your password must be less than 6 characters, please try again!")