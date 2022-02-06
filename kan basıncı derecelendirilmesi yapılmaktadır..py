def main():
    ort=0
    normal=0
    yuksek=0
    hiper=0
    toplam=0
    sayac=0
    kb=int(input("Kan basinc degeri giriniz :"))
    max=kb
    min=kb
    while(kb!=-1):
 
        sayac= sayac + 1
        toplam=toplam+kb
        if (kb>max):
            max=kb
        if (kb<min):
            min=kb
        if (kb<130):
            normal=normal+1
        elif (kb>=130 and kb<=139):
            yuksek=yuksek+1
        else:
            hiper=hiper+1
        kb=int(input("kan basinc degeri giriniz: "))
    ort= toplam / sayac
    perNormal = 100 * (normal / sayac)
    perNormal = 100 * (normal / sayac)
    perYuksek = 100 * (yuksek / sayac)
    perHiper = 100 * (hiper / sayac)
    print()
    print("Populasyonun ortalama basinc degeri=",ort,"\n")
    print("Populasyonun en kucuk basinc degeri=",min,"\n")
    print("Populasyonun en buyuk basinc degeri=",max,"\n")
    print("Populasyonun normal kan basic degerli kisilerin yuzdesi=",perNormal,"\n")
    print("Populasyonun yuksek kan basic degerli kisilerin yuzdesi=",perYuksek,"\n")
    print("Populasyonun hiper kan basic degerli kisilerin yuzdesi=",perHiper,"\n")
main()