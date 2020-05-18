# Karar & Kontrol Yapıları

#True - False Sorgulamalari
sinir = 5000 #sinir degiskenine deger verdik

sinir == 4000 #sinir=4000'mu? sorusu sorar. False

sinir == 5000 

#if

sinir = 50000
gelir = 40000

gelir < sinir #True

if gelir < sinir: #sorgu true ise if alt satira gecer ve calisir.
    print("Gelir sinirdan kucuk.")

#if-else

sinir = 50000
gelir1 = 60000
gelir2 = 50000
gelir3 = 35000

if gelir > sinir: #sorgu true ise if'i calistirir.
    print("gelir sinirdan buyuk")
else: # sorgu false ise else'i calistirir.
    print("gelir sinirdan kucuk")

if gelir==sinir:
    print("gelir sinira esittir.")
else:
    print("gelir sinira esit degildir.")

del gelir

#elif

if gelir3 < sinir:
    print("Geliriniz sinirdan kucuk!!")
elif gelir3 == sinir: #if kosulu saglanmadiysa elif'e bakilir.
    print("Geliriniz sinirda.")
else: #hic bir kosul saglanmiyorsa else calisir.
    print("Tebrikler. Geliriniz sinirdan yukarida.")


#Uygulama: if ve input ile kullanici etkilesimli program
 
sinir = 50000
magaza_adi=input("Magaza adi nedir?\n ") #kullanicidan magaza_adi aldik
gelir = int(input("Gelirinizi giriniz: ")) #kullanicidan aldigimiz geliri int'e cevirdik.

if gelir > sinir:
    print("Tebrikler "+magaza_adi+ " Geliriniz sinirdan yuksek :)")
elif gelir == sinir:
    print(magaza_adi+" Geliriniz sinirda.")
else:
    print("Uyari! "+magaza_adi +" Cok dusuk gelir: "+str(gelir))

























