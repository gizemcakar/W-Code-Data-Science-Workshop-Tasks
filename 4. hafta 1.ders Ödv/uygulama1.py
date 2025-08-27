import pandas as pd

sozluk = {"Kategori": ["Giyim","Giyim", "Ayakkabı","Aksesuar","Ayakkabı","Giyim","Aksesuar","Aksesuar","Ayakkabı","Giyim"],

  "Ürün" : ["Kazak","T-shirt","Sandalet","Küpe","Spor Ayakkabı","Pantolon","Kolye","Yüzük","Çizme","Ceket"],

"Fiyat" : [300,180,450,50,700,400,150,80,850,900]}

# 1- sozlük yapısını DataFrame'e çeviriniz.
df = pd.DataFrame(sozluk)
print(df)

# 2- indexi 2 olan satırda "kategori"yi getiriniz.
print(df.iloc[2]["Kategori"])

# 3- 2.indexteki ürün bilgisi:
print(df.iloc[2]["Ürün"]) 

# 4- 4. indexten 9.indexe kadar olan ürünlerin tüm bilgileri:
print(df.loc[4:9])

# 5- 1. indexten . indexe kadar olan ürünlerin tüm bilgileri:
print(df.loc[1:6 , "Ürün"])
# If you want to explicitly print the column name before the data:
print(df.loc[1:6, ["Ürün"]].to_string(index=False, header=False))

# 6- giyim kategorisindeki ürünler:
giyim = df[df["Kategori"] == "Giyim"]
print(giyim)

#7- ayakkabı kategorisindeki ürünler:
ayakkabı = df[df["Kategori"] == "Ayakkabı"]
print(ayakkabı)

#8 - aksesuar kategorisindeki ürünler:
aksesuar = df[df["Kategori"] == "Aksesuar"]
print(aksesuar)

# 9- giyim kategorisinde fiyatı 300'den fazla olan ürünler:
some_giyim = df[ (df["Kategori"] == "Giyim") & (df["Fiyat"] >300) ]
print(some_giyim)

# 10- ayakkabı kategorisinde fiyatı 600'den az olan ürünler:
some_ayakkabı = df[ (df["Kategori"] == "Ayakkabı") & (df["Fiyat"] <600) ]
print(some_ayakkabı)

# 11- aksesuar kategorisinde fiyatı 100'den fazla olan ürünler:
some_aksesuar = df[ (df["Kategori"] == "Aksesuar") & (df["Fiyat"] >100) ]
print(some_aksesuar)

