#*********VERI YAPILARI***********

###LISTELER

notlar = [90,80,70,50]
type(notlar)

liste=["a",19.5,3]

liste_genis=["a",19.5,3,notlar] #kapsayicidir. icersinde farkli veri tipleri hatta liste bile barindirabilir.
len(liste_genis) #boyutu 4 olur.

#liste ici type sorgulama

liste_genis[0]
liste_genis[1]
liste_genis[2]
liste_genis[3]



type(liste_genis[0])
type(liste_genis[1])
type(liste_genis[2])
type(liste_genis[3])

tum_liste=[liste,liste_genis]

#del tum_liste

#liste elemanlarina erismek

liste_genis[0]
liste_genis[1]
liste_genis[2]
liste_genis[3]

liste_genis[0:2] #0'dan 2 indexli elemana kadar alir
liste_genis[:2] #0'dan 2 indexli elemana kadar alir
liste_genis[2:] # 2 indexli elemandan sona kadar alir

liste_genis

liste_genis[3][1] # liste_genis icersindeki notlar listesinin 1 indexli elemani

print(liste_genis[3][0])

# Liste elemanlarini degistirme

liste2=["ali","veli","berkcan","ayse"]
liste2

liste2[1]="velinin babasi" # 1 index'li elemani degistirdik

liste2

liste2[1]="veli"
liste2[:3]="alinin_babasi","velinin_babasi","berkcanin_babasi" #3 elemani degistirdik
liste2

#listeye eleman ekleme

liste2 + ["kemal"] # bu sekilde kaydetmez sadece görüntüler.

liste2 = liste2 + ["kemal"]

# eleman silme

del liste2[5]
del liste2[2]

#append ve remove metodlari

liste2.append("berkcan") #sona ekleme yapar

liste2.remove("alinin_babasi") #silme yapar
liste2.remove("velinin_babasi")

#insert

liste2.insert(0,"ayca") #0 index'e ayca eklendi

liste2.insert(2,"recep") #2 index'e recep ekledi

liste2.insert(8,"asd") #fazla index girdik fakat sona ekledi

len(liste2)

liste2.insert(len(liste2),"son_eleman") #listenin sonuna ekledi

#pop

liste2.pop(0) #0 index degerli elemani siler
liste2.pop(1) #1 indexli elemani siler.

#count

liste=["ali","veli","ayca","veli","ali","ali"]

liste.count("ali") #"ali" elemaninin listede kac kez yer aldigini gosterir.

#copy

liste_yedek=liste.copy() #liste'yi liste_yedek'e kopyalar.

#extend

liste.extend(liste2) #liste ile liste2'yi birlestirir.
liste

liste2.extend(["a",10]) #liste ile metodun icine yazilan elemanlari birlestirir.

liste2

#index

liste.index("ali") #yazdigimiz elemanin kacinci index oldugunu verir.

#reverse

liste.reverse() #liste elemanlarini ters siraya cevirir.
liste

#sort

liste3=[2,1,5,3,4]

liste3.sort() #liste3'ü kucukten buyuge siralayip kaydeder.
liste3

#clear

liste3.clear() #liste3'ün icini bosaltir

del(liste3) #liste3'ü tamamen siler.








































