# 2 - Factorial of a number #
def factorial():
    n = int(input("Enter a number to calculate its factorial: "))
    if n < 0:
        return "Factorial is not calculated for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        for i in range(1, n):
            n *= i
    return n

result = factorial()
print(f"The factorial of n is: {result}")


