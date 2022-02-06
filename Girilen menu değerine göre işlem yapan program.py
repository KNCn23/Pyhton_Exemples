import math
def Menu():
    print("1-İki sayının toplamı \n")
    print("2-İki sayının farkı \n")
    print("3-İki sayının çarpımı \n")
    print("4-İki sayının ortalaması \n")
    print("5-İki sayının 10 tabanında logaritma değeri sonucu\n")
    print("6-Çıkış \n")
def Bir():
    a,b=eval(input("Toplanması için iki sayi giriniz:\n"))
    sonuc=a+b
    print(sonuc)
def İki():
    a,b=eval(input("Farkı bulunması için iki sayi giriniz:\n"))
    sonuc=a-b
    print(sonuc)    
def Uc():
    a,b=eval(input("Çarpımı için iki sayi giriniz: \n"))
    sonuc=a*b
    print(sonuc)
def Dort():
    a,b=eval(input("Ortalaması için iki sayi giriniz: \n"))
    sonuc=(a+b)/2
    print(sonuc)
def Bes():
    a,b=eval(input("Logaritması için iki sayi giriniz: \n"))
    sonuc=math.log10(a+b)
    print(sonuc)
def main():
    secim=1
    
    while secim !=6:
        Menu()
        
        secim=eval(input("Seciminiz: \n"))
        if secim == 1:
            Bir()
        elif secim == 2:
            İki()
        elif secim == 3:
            Uc()
        elif secim == 4:
            Dort()
        elif secim == 5:
            Bes()
        elif secim == 6:
            break
        else:
            print("Lutfen 1-6 arası bir rakam giriniz !")
            
        print("Program Sonlandı")    
            
main()      