#Nesne Yonelimli Programlama

#Siniflarin Ozellikleri
class VeriBilimci(): #Class tanimlama
    bolum = ''
    sql = 'Evet'
    Deneyim_Yili = 0
    bildigi_diller=[]
    
#Siniflarin Ozelliklerine Erismek
    
VeriBilimci.sql 
VeriBilimci.Deneyim_Yili

#Siniflarin Ozelliklerini Degistirmek

VeriBilimci.sql = 'Hayir'
VeriBilimci.sql #Ozelligin degeri degisti.

#Sinif Orneklendirmesi (instantiation)

ali = VeriBilimci() #VeriBilimci sinifinin ozelliklerini tasiyan bir birim olustu.
                    #Yani ornekleme yapmis oldum.

ali.sql
ali.bildigi_diller.append("Python") #ali'nin bildigi_diller'e Python ekledik.
                                    #Ancak bu class'in hepsini etkiledi.
ali.bildigi_diller

veli = VeriBilimci()
veli.bildigi_diller #ali'nin bildigi dillere python eklemistik ancak veli'nin
                    #bildigi dillerde de python oldu.

#Ornek Ozellikleri

class VeriBilimci(): #yeni bir sinif tanimladik
    bildigi_diller = ["R","Python"] #Tum class icin ozellik atamasi.
    bolum = ''
    def __init__(self): #Orneklere ayri ayri ozellik atamasi yapmak icin.
        self.bildigi_diller = [] 
        self.bolum = ''

ali = VeriBilimci()
ali.bildigi_diller #bos 

veli = VeriBilimci()
veli.bildigi_diller #bos

ali.bildigi_diller.append("Python") #ali'nin bildigi dillere ekleme yaptik.
ali.bildigi_diller #Bu kez python var.

veli.bildigi_diller.append("R") #veli'nin bildigi dillere ekleme yaptik.
veli.bildigi_diller #sadece veli'ye ekledigimiz R var.

VeriBilimci.bildigi_diller #Classin genelinde R ve Python var.

VeriBilimci.bolum # ''
ali.bolum = 'Istatistik' 
veli.bolum = 'bil_sis_muh'
veli.bolum #bil_sis_muh 
ali.bolum #istatistik


# Ornek Metodlari

class VeriBilimci(): #Bir class tanimladik.
    calisanlar = [] # calisanlar adinda bir nesne
    def __init__(self): #orneklerin ozellikleri
        self.bildigi_diller = [] #orneklerin ozellikleri
        self.bolum = '' #orneklerin ozellikleri
    def dil_ekle(self, yeni_dil): #orneklere etki edecek bir fonksiyon yazdik
        self.bildigi_diller.append(yeni_dil)
        
ali = VeriBilimci()
ali.bildigi_diller #suan bos
ali.bolum

veli = VeriBilimci()
veli.bildigi_diller
veli.bolum

ali.dil_ekle("R") #dil_ekle fonksiyonunu calistirdik.

VeriBilimci.dil_ekle(ali,"Python") #dil_ekle fonksiyonunu calistirdik.
                    #ali'nin bildigi dillere python eklendi.
                    #dil_ekle fonksiyonu iki sekilde de calistirilabilir.

ali.bildigi_diller #Python ve R var.

# Miras Yapilari (inheritance)

class Employees(): 
    def __init__(self,FirstName, LastName, Address):#Ozellikleri fonksiyonel. Sabit degil.
        self.FirstName = FirstName
        self.LastName = LastName
        self.Address = Address


class DataScience(Employees):  #Employees'den miras aliyor.
    def __init__(self,Programming):#Ozellikleri fonksiyonel. Sabit degil.
        self.Programming = Programming
        
class Marketing(Employees):   #Employees'den miras aliyor.
    def __init__(self,StoryTelling):#Ozellikleri fonksiyonel. Sabit degil.
        self.StoryTelling = StoryTelling

veribilimci1 = DataScience() #Parametreyi bos birakamayiz. Hata verir.
veribilimci1 = DataScience("Python")
veribilimci1.Programming #Python

pazarlamaci = Marketing("Yes")
pazarlamaci.StoryTelling #Yes

















