# 1 - a function that returns the area of a circle given its radius #

def area_of_circle():
    pi = float(input("Enter the value of pi: "))  # Convert to float
    radius = float(input("Enter the radius of the circle: "))
    area = pi * ( radius ** 2 )
    return area

result = area_of_circle()
print("The area of circle is {}".format(result))