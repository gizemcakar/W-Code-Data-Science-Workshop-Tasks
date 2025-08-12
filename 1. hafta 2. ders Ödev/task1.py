# 1 - how to calculate tax deduction from salary # 

salary = int(input("Enter your salary: "))

if salary <= 10000 :
    salary = salary - (salary * 0.05)
elif salary <= 25000 :
    salary = salary - (salary * 0.10)
elif salary <= 45000 :
    salary = salary - (salary * 0.25)
else :
    salary = salary - (salary * 0.30)

print("Your salary after tax decrease is: {}".format(salary))