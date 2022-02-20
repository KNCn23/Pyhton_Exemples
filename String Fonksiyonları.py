mesaj = "Merhaba Dünya"

print(mesaj[2])#2.indeksi yazdırır
yeniMesaj = mesaj[2:5] #2.indeksten 5.indekse kadar (5. dahil değil)
#SUBSTRING
print(yeniMesaj)
print(mesaj[2:]) #2.indeksten sonuna kadar
print(mesaj[:2]) #baştan 2.idekse kadar (2. dahil değil)

#LEN Fonksiyonu
print(len(mesaj))#uzunluğu verir
yeniMesaj2 = mesaj[len(mesaj)-1:len(mesaj)]
print(yeniMesaj2)

#Lower ve Upper
print(mesaj.upper()) #bütün karakterleri büyük harf yapar
print(mesaj.lower()) #bütün karakterleri küçük harf yapar

#Replace
print(mesaj.replace("ü","u")) #bütün ü leri u ya çevirerek yazar ama stringi etkilemez
mesaj = mesaj.replace("ü","u") #stringin yapısını değiştirir
print(mesaj.replace("a","e"))

#Split ve Strip
bilgi = "     Engin Demiroğ 33 Ankara".strip() #gereksiz boşlukları siler
print(bilgi.split()) #otomatik olarak " " lardan ayırır
print(bilgi.split("i"))#bütün i lerden ayırır
print("Adı = " + bilgi.split()[0]) #ilk ayırdığı dizi elemanını yazdırır

#Input
ad = input("Adınız?")
sayi1 = input("Sayı 1 = ?")
sayi2 = input("Sayı 2 = ?")
print(int(sayi1) + int(sayi2)) #int yazmazsak string şeklinde yan yana toplar
