# 1 - variable transformation #

x = 3
x = float(x)
x
print(type(x))

y = 4.5
y = int(y)
y
print(type(y))


z = "8"
z = int(z)
z
print(type(z))

a = "12"
a = float(a)
a
print(type(a))


b = "46.8"
b = int((float(b)))     # First convert to float, then to int.
b
print(type(b))