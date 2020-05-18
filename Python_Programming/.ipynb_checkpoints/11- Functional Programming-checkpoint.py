#Functional Programming
# =============================================================================
# Python dili ile bir program yazmak istediğimizde bunu OOP(Nesneye Dayalı Programlama) özellikleri ile de yazabiliriz FP(Fonksiyonel Programlama) özellikleri ile de yazabiliriz.
# Fonksiyonlar dilin baştacıdır. (Birinci sınıf nesnelerdir.)
# Yan etkisiz fonksiyonlar. (stateless(durumsuz), girdi-çıktı)
# Yüksek seviye fonksiyonlar.
# =============================================================================


#Yan Etkisiz Fonksiyonlar (Pure Functions) 
#Ornek-1: Bagimsizlik

A = 9 #eski deger 6 idi.

def impure_sum(b): #saf olmayan fonksiyon. Sonucu A degiskenine bagimli.
    return b + A

def pure_sum(a,b): #saf
    return a + b

impure_sum(6) #A'yi degistirirsem sonucu degisir. Girdi ayni, sonuc degisti.

pure_sum(3,4) #Ne yaparsam yapayim sonucu girdilerden baska bir sey ile degismez.

#Ornek-2: Olumcul yan etkiler
#OOP
class LineCounter:
    def __init__(self, filename):
        self.file = open(filename , 'r')
        self.lines = []
        
    def read(self):
        self.lines = [line for line in self.file]
        
    def count(self):
        return len(self.lines)
    
lc = LineCounter('deneme.txt')

print(lc.lines)
print(lc.count())

lc.read()

print(lc.lines)
print(lc.count())

#FP

def read(filename):
    with open(filename, 'r') as f:
        return [line for line in f]
    
def count(lines):
    return len(lines)

example_lines=read('deneme.txt')
lines_count = count(example_lines)
lines_count

#İsimsiz Fonksiyonlar (Lambda) (Anonymous Functions)

def old_sum(a,b): #Eski tipte bir fonksiyon
    return a+b

new_sum = lambda a,b : a+b #Lambda ile fonksiyon- İsimsiz Fonksiyon
new_sum(4,5) 

sirasiz_liste = [('b',3),('a',8),('d',12),('c',1)]
sirasiz_liste

sorted(sirasiz_liste, key=lambda x: x[1]) #Fonksiyon tanimladik.
#Out: [('c', 1), ('b', 3), ('a', 8), ('d', 12)]

#Vektörel Operasyonlar (Vectorel Operations)
#OOP
a = [1,2,3,4] #amacimiz bu listeler icersindeki her bir elemani birbiriyle carpmak
b = [2,3,4,5] #yani 1*2,2*3,3*4,4*5
              #Listelerimiz tek boyutlu oldugu icin bunlara 'vektor' denir  

ab = [] #Carpma islemini saklamak icin global alanda bos liste olusturduk.

for i in range(0, len(a)): #a'nin uzunlugu kadar i degeri uretecek(0,1,2,3)
    ab.append(a[i]*b[i]) #a'nin i'nci elemani ile b'nin i'nci elemanini carp. ab'ye ekle.

ab

#FP

import numpy as np #numpy kutuphanesini calisma ortamima dahil ettim. np kisayolu atadim.

a = np.array([1,2,3,4])
b = np.array([2,3,4,5])

a*b


#map & filter & reduce
#map

liste = [1,2,3,4,5]

for i in liste:
    print(i+10) #her elemana 10 ekleyip yazdir

list(map(lambda x:x+10, liste)) #map fonk. ile her elemana 10 ekleyip liste yap.

#filter

liste = [1,2,3,4,5,6,7,8,9,10]

list(filter(lambda x:x % 2 == 0, liste)) #2'ye bolumunden kalani 0'a esit olanlari listele.

#reduce

from functools import reduce

liste = [1,2,3,4,5,6,7,8,9,10]
reduce(lambda a,b:a+b , liste) #liste elemanlarini toplar.

#Modul Olusturma
#HesapModulu.py dosyasina fonksiyonu yazdik.

import HesapModulu #Modulu import ettik.

HesapModulu.yeni_maas(1000) #1200 olarak calisir.

import HesapModulu as hm #hm kisaltmasi ile modulu kullanmak icin.

hm.yeni_maas(2000)

from HesapModulu import yeni_maas # Farkli kullanim sekilleri.

yeni_maas(4000)

import HesapModulu as hm
hm.maaslar #Modulde olusturdugumuz liste tipindeki nesneyi aldik.


#Hatalar/Istisnalar (exceptions)

#ZeroDivisionError hatasi
a=10
b=0
a/b

try: #kodu dene 
    print(a/b)
except ZeroDivisionError: #calismazsa bu hata ile karsilastiginda ne olacak
    print("Payda sıfır olamaz.")

#tip hatasi

a = 10
b = "2"

try :
    print(a+b)
except TypeError:
    print("str ile int toplanamaz.")






























