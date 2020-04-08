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



































