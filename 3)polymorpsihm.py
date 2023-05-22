from dataclasses import dataclass
@dataclass
class Arac:
    marka: str
    model: str
    def tanim(self):
        print(f"Bu araç bir {self.marka} {self.model}")

    def hareket_et(self):
        print("Araç hareket ediyor...")

@dataclass
class Otomobil(Arac):
    marka: str
    model: str
    yakit_turu: str
    def __post_init__(self):
        super().__init__(self.marka, self.model)
        

    def hareket_et(self):
        print("Otomobil hareket ediyor...")

    def benzin_tuket(self):
        print("Benzin tüketiliyor...")


@dataclass
class Kamyon(Arac):
    marka: str
    model: str 
    yuk_kapasitesi: str
    def __post_init__(self):
        super().__init__(self.marka, self.model)
        

   # def hareket_et(self):
        # print("Kamyon hareket ediyor...")

    def yuk_yukle(self):
        print("Kamyon yükleniyor...")


def arac_tanimla(arac):
    arac.tanim()
    arac.hareket_et()


otomobil = Otomobil("BMW", "320i", "Benzin")
kamyon = Kamyon("MAN", "TGX", "50 ton")

arac_tanimla(otomobil)
arac_tanimla(kamyon)