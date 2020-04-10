#Veri Yapilari - Dictionary (Sozluk)

# 1-) Kapsayicidir
# 2-) Sirasizdir -- Listelerden farki
# 3-) Degistirilebilir


# Sozluk Olusturma

sozluk={"REG" : "regresyon modeli",
        "LOJ" : "lojistik regresyon",
        "CART" : "Classification And Reg"}

sozluk
len(sozluk)

# Eleman secme islemleri

sozluk={"REG" : "regresyon modeli",
        "LOJ" : "lojistik regresyon",
        "CART" : "Classification And Reg"}

sozluk["REG"] #REG key'inin karsiligini bu sekilde getiririz.

sozluk={"REG" : {"ASD" : 10,
                 "XXX" : 20,
                 "ZZZ" : 30},

        "LOJ" : {"ASD" : 10,
                 "XXX" : 20,    # Sozluk icinde sozluk olusturduk. Ic ice yapi.
                 "ZZZ" : 30},
                 
        "CART" : {"ASD" : 10,
                  "XXX" : 20,
                  "ZZZ" : 30}
        }

sozluk["REG"]["XXX"] #ic ice bir yapida elemana erisim.


# Eleman eklemek & degistirmek

sozluk={"REG" : "regresyon modeli",
        "LOJ" : "lojistik regresyon",
        "CART" : "Classification And Reg"}

sozluk["GBM"] = "Gradient Boosting Mac" #sozluk'e eleman ekleme.
sozluk

sozluk["REG"]= "REG'in yeni karsiligi" #REG Key'inin karsiligini degistirme.
sozluk

sozluk[1] = "Key'ler sabit degerlerdir"
sozluk

# Key'ler sabit degerlerdir. Degistirilemez degerlerden olusmalidir.
# stringler, sayilar, tuple'lar gibi...

t= ("tuple",) # t adinda tuple olusturduk.

sozluk[t]="Tuple'dan key olusturuldu."
sozluk



















































































