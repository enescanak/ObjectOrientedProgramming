# Araba sınıfı oluşturma
from dataclasses import dataclass
@dataclass
class Araba:
    marka: str
    renk: str
    hiz: int
    
    def hizlan(self, miktar):
        self.hiz += miktar

    def yavasla(self, miktar):
        self.hiz -= miktar

    def dur(self):
        self.hiz = 0

# Araba nesnesi oluşturma
araba1 = Araba("Toyota", "Kirmizi", 0)

# Araba nesnesinin özelliklerini ve davranışlarını kullanma
print(araba1.marka)   # Output: Toyota
araba1.hizlan(30)
print(araba1.hiz)     # Output: 30
araba1.yavasla(10)
print(araba1.hiz)     # Output: 20
araba1.dur()
print(araba1.hiz)     # Output: 0