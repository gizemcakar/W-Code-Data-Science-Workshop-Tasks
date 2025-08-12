# 3 - user gives your birdh year and calculate age #

from datetime import date   # date module to get the current year

def calculate_age():
    birth_year = int(input("Enter your birth year: "))
    current_year = date.today().year                        # Get the current year

    age = current_year - birth_year
    return age

age = calculate_age()
print("Your age is {}".format(age))