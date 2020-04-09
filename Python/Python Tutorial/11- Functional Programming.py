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


















