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

isim = input("Öğrenci ismi giriniz: ")
ders_ismi = input("Ders ismi giriniz: ")

if isim in ogrenci_bilgileri:
    if ders_ismi in ogrenci_bilgileri[isim]["dersler"]:
        puan = ogrenci_bilgileri[isim]["dersler"][ders_ismi]
        print(f"{isim} adlı öğrencinin {ders_ismi} dersinden aldığı puan: {puan}")
    else:
        print(f"Bu öğrenci {ders_ismi} dersini almıyor.")
else:
    print("Bu isimde bir öğrenci bulunamadı.")

