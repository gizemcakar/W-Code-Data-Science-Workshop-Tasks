# 4 - retirement age calculator #

from datetime import date   # date module to get the current year


def retirement_age():
    isim = input("Enter your name: ")
    birth_year = int(input("Enter your birth year: "))
    
    def calculate_age(birth_year):
        current_year = date.today().year                       # Get the current year
        age = current_year - birth_year
        return age
    
    age = calculate_age(birth_year)
    retirement_age = 65
    years_left = retirement_age - age
    
    if age < retirement_age:
        print(f"Dear {isim}, {years_left} years left for your retirement.")
    else:
        print(f"Dear {isim}, you are already retired.")

retirement_age()

