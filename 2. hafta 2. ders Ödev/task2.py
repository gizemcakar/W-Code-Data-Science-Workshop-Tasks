# 2 - yeni_liste containing all string elements from liste

liste = ["Python", True, 9, "3", 8.4, "Hi-Kod", "False", 4.7]

yeni_liste = []

for item in liste:
    if type(item) == str:
        yeni_liste.append(item)

print(yeni_liste)
