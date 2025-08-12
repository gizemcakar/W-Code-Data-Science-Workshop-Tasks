# 5 - for loop in variable #
atolye = "Hi-Kod Veri Bilimi Atölyesi"
atolye_split = atolye.split()
print(atolye_split)

for word in atolye_split:
    print(word.upper())

for word in atolye_split:
    print(word.lower())

sayi = "0123456789"
cift_sayilar = []
tek_sayilar = []

for digit in sayi:
    if int(digit) % 2 == 0:
        cift_sayilar.append(digit)
        
print("".join(cift_sayilar))



for digit in sayi:
    if int(digit) % 2 != 0:
        tek_sayilar.append(digit)
        
print("".join(tek_sayilar))