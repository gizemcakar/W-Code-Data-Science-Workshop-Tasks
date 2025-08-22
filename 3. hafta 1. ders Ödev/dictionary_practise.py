# ogrenci_bilgileri sözlüğü
                            # key : öğrenci isimleri
                            # value : ders notları

ogrenci_bilgileri = {
    "Gizem": {"dersler": {"Matematik":95,
                          "Fizik":60, 
                          "Kimya":100}
            },
    "Ahmet": {"dersler": {"Matematik":100,
                          "Fizik":80,
                          "Kimya":90}
            },
    "Zeynep": {"dersler": {"Matematik":70, 
                           "Fizik":50,
                           "Kimya":60}
               }
}   

# yeni bir öğrenci ekleme:
ogrenci_bilgileri["Mert"] = {"dersler": {"Matematik":85,
                                  "Fizik":95,
                                  "Kimya":80}
                            }
print(ogrenci_bilgileri)


# bir öğrencinin ders notunu güncelleme:
ogrenci_bilgileri["Gizem"]["dersler"]["Fizik"] = 75
print(ogrenci_bilgileri)


# bir öğrencinin ders notunu silme:
del ogrenci_bilgileri["Zeynep"]["dersler"]["Kimya"]
print(ogrenci_bilgileri)


# bir öğrencinin tüm ders notlarını alma:
gizem_dersler = ogrenci_bilgileri["Gizem"]["dersler"]
print(gizem_dersler)

# tüm öğrencilerin isimlerini alma:
ogrenci_isimleri = list(ogrenci_bilgileri.keys())
print(ogrenci_isimleri)


# tüm öğrencilerin ders notlarını liste halinde alma:
tum_dersler = [ogrenci["dersler"] for ogrenci in ogrenci_bilgileri.values()]
print(tum_dersler)


tum_puanlar = []
for ogrenci in ogrenci_bilgileri.values():
    tum_puanlar.extend(ogrenci["dersler"].values())
print(tum_puanlar)

