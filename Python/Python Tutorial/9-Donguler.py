#Donguler

# For Dongusu 

ogrenci = ["ali","veli","isik","berk"]

ogrenci[0]
ogrenci[1]

for i in ogrenci: #i gecici degiskendir.
    print(i)
    
#Dongu ve Fonksiyonlarin Birlikte Kullanimi

def kare_al(x):
    print(x**2)
    
kare_al(2)
    
maaslar=[1000,2000,3000,4000,5000]
    
for i in maaslar:
    print(i)
    
#maaslara %20 zam yapilacak gerekli kodlari yaziniz.
     
def yeni_maas(x):
    print(x*1.20)
    
yeni_maas(1000) #fonksiyonun calismasina ornek.   

for i in maaslar:
    yeni_maas(i)
    
    
#if, for ve fonksiyonlarin bir arada kullanimi

maaslar=[1000,2000,3000,4000,5000]
    
def maas_ust(x):
    print(x*1.10) # %10 zam
    
def maas_alt(x):
    print(x*1.20) # %20 zam
    
for i in maaslar:
    if i>=3000: #maas 3000'den fazla veya esit ise
        maas_ust(i) # %10 zam uygulanacak
    else:          #değilse
        maas_alt(i) # %20 zam uygulanacak
        
#break & continue
        
maaslar=[8000,5000,2000,1000,3000,7000,1000]
    
maaslar.sort() #Karisik yazilmis listeyi kucukten buyuge siraladik.
maaslar

for i in maaslar:
    if i ==3000: #1000,1000,2000 gecti 3000'e geldi if'e girdi. Durdu.
        print("kesildi")
        break
    print(i)
    
for i in maaslar:
    if i ==3000: #1000,1000,2000 gecti 3000'e geldi if'e girdi. Atladi.
        print("atlandi.")
        continue
    print(i)
    
#while

sayi=1

while sayi<10: #Sayi 10'a gelene kadar bu islemi devam ettir.
    sayi += 1 #sayiyi 1 arttir ve sayi degerine ata.
    print(sayi)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    