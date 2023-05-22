# Ana sınıf oluşturma
class Araba:
    def __init__(self, marka = 'mercedes', renk = 'kirmizi', hiz= 0):
        self.marka = marka
        self.renk = renk
        self.hiz = hiz

    def hizlan(self, miktar):
        self.hiz += miktar

    def yavasla(self, miktar):
        self.hiz -= miktar

    def dur(self):
        self.hiz = 0

# Miras alan sınıf oluşturma
class Otobus(Araba):
    def __init__(self, yolcu_sayisi):
        #super().__init__()
        self.yolcu_sayisi = yolcu_sayisi

    def yolcu_ekle(self, miktar):
        self.yolcu_sayisi += miktar

    def yolcu_cikar(self, miktar):
        self.yolcu_sayisi -= miktar

# Otobus nesnesi oluşturma
otobus1 = Otobus( yolcu_sayisi= 0)

# Otobus nesnesinin özelliklerini ve davranışlarını kullanma
print(otobus1.marka)    # Output: Mercedes
otobus1.hizlan(30)
print(otobus1.hiz)      # Output: 30
otobus1.yolcu_ekle(10)
print(otobus1.yolcu_sayisi)  # Output: 10