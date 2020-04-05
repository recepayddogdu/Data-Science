#Veri Yapilari - Sets (Kumeler)

# =============================================================================
# #1-) Sirasizdir
# #2-) Degerleri Essizdir.(Tekrar eden degeri olmaz)
# #3-) Degistirilebilirdir.
# #4-) Farkli turden veriler barindirabilir.
# =============================================================================
# Set olusturma

s = set()
s

l= ["ali","ata","bakma","ali","uzaya","git"]

s=set(l) # l listesindeki elemanlari birer kez alir.
s

ali="ali_ata_bakma_uzaya_git_lutfen"

s=set(ali) #ali cumlesindeki her bir karakteri bir kez alir.
s

t=("ali","bakma")

s=set(t) #Set'ler farkli veri tiplerinden olusabilir.
s

#Eleman ekleme ve cikarma islemleri

s.add("ile") #ile stringini set'e ekledi
s

s.add(t) # t isimli tuple'i set'e ekledi
s

s.add(ali) # ali elemanini set'e ekledi.
s

s.remove(ali) # ali elemanini sildi.
s

s.remove(ali) # ali'yi tekrar silmek sitedigimizde hata verir.

s.discard(t) # discard ile de silme islemi gerceklestirebiliriz
s

s.discard(t) # tekrar silmek istedigimizde discard hata uretmez.

# Set'lerde Fark Islemleri

#difference ve symmetric_difference

set1= set([1,3,5])
set2= set([1,2,3])

set1.difference(set2) #set1'in set2'den farki
set2.difference(set1) #set2'in set1'den farki

set1.symmetric_difference(set2) #ikisinde de ortak olmayan elemanlari verir

#Set'lerde kesisim ve birlesim islemleri
# intersection ve union

set1.intersection(set2) # set1 ve set2'nin ortak elemanlari
set2.intersection(set1)

set1.union(set2) # set1 ve set2'nin birlesimi

set1.intersection_update(set2) #set1'in degerini kesisim degerleri olarak degistirir.
set1


# Setlerde sorgu islemleri

# isdisjoint

set1.isdisjoint(set2) #set1 ve set2'nin kesisimi bos mu? Ayrik kume mi?
                        #False -> hayir degil.

# issubset

set1.issubset(set2) #set1 set2'nin subset'i mi?

#issuperset

set2.issuperset(set1) #set2 set1'in superset'i mi? Kapsar mı?


