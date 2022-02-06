import math as m

def oklid_hesapla(x1,x2,y1,y2):
    sonuc = m.sqrt(pow((x1 - y1),2) + pow((x2 - y2),2))
    return sonuc
def main():
    x1 = int(input("Birinci noktanın 1. degerini giriniz : "))
    x2 = int(input("Birinci noktanın 2. degerini giriniz : "))
    y1 = int(input("İkinci noktanın 1. degerini giriniz : "))
    y2 = int(input("İkinci noktanın 2. degerini giriniz : "))
    sonuc = oklid_hesapla(x1,x2,y1,y2)
    print ("Girdiğiniz iki nokta arasındaki uzaklık " , sonuc)
main()
    