# 3 - request an input from user and mathematical operations #
value1 = int(input("Bir sayı giriniz: "))
value2 = int(input("Bir sayı daha giriniz: "))
print(type(value1))

while type(value1) is int and type(value2) is int:
    islem = input("İşlem giriniz (+, -, *, /, q for Quit): ")

    if islem == "+":
        print(value1 + value2)
    elif islem == "-":
        print(value1 - value2)
    elif islem == "*":
        print(value1 * value2)
    elif islem == "/":
        print(value1 / value2)
    elif islem == "q":
        break
    else:
        print("Geçersiz işlem. Lütfen +, -, * veya / giriniz.")