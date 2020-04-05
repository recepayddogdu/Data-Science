# Matematiksel islemler

4*4
4/4
4-2
4+2 # bunlar klasik matematiksel operatorlerdir.

3**2 # 3'un 2'nci kuvveti

3**3 # 3'un 3'ncu kuvveti

# =============================================================================
# #Fonksiyon Nasil Yazilir?

def kare_al(x):
    print(x**2) # def ile fonksiyon olusturacagimizi belirtiriz.

kare_al(5) #fonksiyonu bu sekilde calistiririz.

# =============================================================================

#Bilgi notuyla cikti uretme
def kare_al(x):
    print("Girilen sayinin karesi : " + x**2) #str + int
    
kare_al(3) #hata aldik cunku str ifadeler sadece str ifadeler ile birlestirilebilir.

def kare_al(x):
    print("Girilen sayinin karesi : " + str(x**2)) #str + str(type donusumu)

kare_al(3) #bu kez hata almadan calisti. 


def kare_al(x):
    print("Girilen sayi: " + str(x) 
          +"\nKaresi: "+str(x**2)) #\n ile alt satira gectik.

kare_al(4)

# Iki argumanlı fonksiyon tanimlama

def carpma_yap(x,y):
    print("Birinci sayi: "+ str(x)
            + "\nIkinci sayi: "+ str(y)
            + "\nCarpimlari: "+str(x*y))

carpma_yap(3,4)

# On Tanimli Argumanlar

def carpma_yap(x,y=1): # y=1 demeseydik iki degeri de girmek zorunda kalirdik.
    print(x*y)

carpma_yap(3) #Hata vermeden calisacak.
carpma_yap(3,5) #yeni bir deger girdigimizde eski degeri ezeriz.

# Argumanların Siralamasi

def carpma_yap(x,y):
    print(x*y)
    
carpma_yap(y=2, x=4) # Argumanlarin sirasini bilmiyorsam ama isimlerini biliyorsam
                    # Bu sekilde calistirabiliriz.

#Fonksiyonlar ne zaman yaizlir?
def direk_hesap(isi, nem, sarj):
    print((isi+nem)/sarj)
    
direk_hesap(25,40,70) 

#Fonksiyon Ciktilarini Girdi Olarak Kullanmak
#Fonksiyonun ciktisini baska bir yerde girdi olarak kullanmak icin
# return ifadesini kullanmaliyiz.

def direk_hesap(isi, nem, sarj):
    print((isi+nem)/sarj) #print ekrana cikti verir. Programlama anlaminda
                            #kullanilabilegi anlamina gelmez.
    
cikti = direk_hesap(25,40,70) 
cikti #fonksiyonun sonucunu cikti'ya atayamadik

def direk_hesap(isi, nem, sarj):
    return (isi+nem)/sarj #return ifadesini kullanirsak sonucu kullanabiliriz.

cikti = direk_hesap(25,40,70) 
cikti

def direk_hesap(isi, nem, sarj):
    return 
    (isi+nem)/sarj # bu sekilde calistirirsak fonksiyon islevini yapmaz.
                    # cunku fonksiyon return'un oldugu satira gelince durur.

direk_hesap(25,40,70) 

#Local ve Global Degiskenler

x=10
y=10 #Ana calisma alanimizdaki degiskenler Global degiskenlerdir.

def carpma(x,y):
    return x*y #fonksiyon icersindeki degiskenler Local degiskendir.

carpma(2,3)

#Local Etki Alanindan Global Etki Alanini Degistirme

x=[] #bos bir liste olusturuldu

def eleman_ekle(y):
    x.append(y) #x'e y'yi ekle.
    print(str(y)+" ifadesi eklendi."
          +"\nListenin yeni hali: "+str(x))
    
eleman_ekle(3)



































