from abc import ABC, abstractmethod
from dataclasses import dataclass,field
@dataclass #base bir sınıf var eklenmesi gerekn fonksiyonlarım var
class Hesap(ABC): #tek bir instance ile hata düzelir içerisinden
    #method çağırmasına gerek kalmaz
    bakiye: int = field(default_factory=int)
    enes: int= field(default_factory=int)
    def __post_init__(self):
        pass
    def para_gor(self): #abstract olmadıgı için aşağıda eklememe
        #gerek yok
        pass
    @abstractmethod #dekorator
    def para_yatir(self, miktar): 
        pass #soyut ethod eklenmek zorundadır.

    @abstractmethod #zorunlu çalısır
    def para_cek(self, miktar):
        pass #soyut method eklenmezse hata verir.
@dataclass
class BankaHesabi(Hesap):
    
    def para_yatir(self, miktar):
        self.bakiye += miktar

    def para_cek(self, miktar):
        if self.bakiye >= miktar:
            self.bakiye -= miktar
        else:
            print("Yeterli bakiyeniz yok.")
            

@dataclass
class Musteri:
    isim: str
    hesap: Hesap
    def para_yatir(self, miktar):
        self.hesap.para_yatir(miktar)

    def para_cek(self, miktar):
        self.hesap.para_cek(miktar)

    def bakiye_sorgula(self):
        print(f"{self.isim} isimli müşterinin bakiyesi {self.hesap.bakiye} TL'dir.")


hesap1 = BankaHesabi(1000,4)
musteri1 = Musteri("Ahmet", hesap1)
musteri1.bakiye_sorgula()
musteri1.para_yatir(500)
musteri1.bakiye_sorgula()
musteri1.para_cek(200)

musteri1.bakiye_sorgula()