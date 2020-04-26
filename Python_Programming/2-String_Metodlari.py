# STRING METODLARI - len()

gel_yaz="gelecegi_yazanlar"

#del mvk #degiskeni silmek icin del kullaniriz. kullandiktan sonra
        # yorum satiri haline getirilmelidir.

a=99
b=10

type(a/b) # a/b=9.9 olacagindan tipi float olur.

len(gel_yaz) # gel_yaz degiskeninin icersindeki string'in krktr uzunlugunu verir.

########################################################################

#upper() & lower() fonksiyonlari

gel_yaz.upper() #stringi buyuk harflere cevirir.

gel_yaz.lower() #stringi kucuk harflere cevirir.

#isupper() & islower() fonksiyonlari

gel_yaz.isupper() #buyuk harf mi? sorusu sorar. T or F getirir.
gel_yaz.islower() #kucuk harf mi? sorusu sorar.

B = gel_yaz.upper() #B degiskenine buyuk harfli gel_yaz atadik.

B.isupper()

Dnm="AsDfGhGgGgG"

Dnm.isupper()
Dnm.islower()   #ikisi de false getirir.

# replace() bir karakteri baska bir karakter ile degistirmek icin kullanilir.

gel_yaz.replace("a","ı")

# strip() Karakter kirpma islemleri

gel_yaz= " gelecegi_yazanlar " #basinda ve sonunda bosluk var
gel_yaz.strip() #varsayilan olarak bosluklari siler.

gel_yaz="*gelecegi_yazanlar*" # basina ve sonuna * ekledik.
gel_yaz.strip("*") # *(yildiz) arasindaki ifadeyi kirpar.

# dir() icersine yazdigimiz veri tipi icin kullanilabilir metodlari verir.

dir(gel_yaz)
            #ikisi de ayni sonucu verir.
dir(str)

#############################################

# Substring: string ifadeleri ile alt kume islemleri.

gel_yaz[0] # 0 index'li ifadeyi getirir.

gel_yaz[0:3] # 0'dan basla 3'e kadar getir.

#TYPE DONUSUMLERİ

toplama_bir=input() #input ile kullanıcıdan veri alırız.
toplama_iki=input() #kullanıcıdan aldıgımız veri str tipindedir.

toplama_bir+toplama_iki # 10+20 --> '1020' çıktısı verir.
						# bunu engellemek için type dönüşümü yapmalıyız.
int(toplama_bir)+int(toplama_iki) #tip donusumlerini bu sekilde yapariz.

int(12.4) #float to int --> 12
float(12) #int to float --> 12.0
str(12)   #int to str   --> '12'

#Print fonksiyonu

print("gelecegi","yazanlar")

print("gelecegi","yazanlar",sep = "_") #sep argumani araya gelecek degeri secmemize olanak saglar.

?print #print fonksiyonu ile kullanabilecegimiz argumanlari verir.



ifade="Merhaba! "
ifade.strip()









