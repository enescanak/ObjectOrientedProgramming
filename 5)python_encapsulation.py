from dataclasses import dataclass

class Ogrenci:
    def __init__(self, ad, soyad, ogrenci_no):
        self.__ad = ad
        self.__soyad = soyad
        self.__ogrenci_no = ogrenci_no
        self.__notlar = []

    def not_ekle(self, not_degeri):
        self.__notlar.append(not_degeri)
        self.__ortalama_hesapla()
        

    def __ortalama_hesapla(self):
        toplam = sum(self.__notlar)
        ortalama = toplam / len(self.__notlar)
        print(ortalama)

    def __str__(self):
        return f"{self.__ad} {self.__soyad} ({self.__ogrenci_no})"
    


@dataclass
class Employee:
    name: str
    age: int
    salary: float

    def __pos_init__(self):
        self.__name = self.name
        self.__age = self.age
        self.__salary = self.salary

    def get_salary(self, bonus: float = 0) -> float:
        return self.__salary + bonus

    def set_salary(self, new_salary: float) -> None:
        self.__salary = new_salary

    def get_details(self) -> str:
        return f"{self.__name}, {self.__age} years old, salary: {self.__salary}"
emp = Employee('Enes Can', 23, 1000.0)
emp.set_salary(1005.50)
emp.__salary = 500.5
print(emp.get_details)
print(emp.get_salary(200.5))
print(emp.get_details)

ogrenci1 = Ogrenci("Ali", "Demir", "123456")
ogrenci1.__soyad = 'AK'
ogrenci1.not_ekle(85)
ogrenci1.not_ekle(90)
ogrenci1.not_ekle(70)

# ogrenci1.__notlar = [100, 100, 100]  # hata! Encapsulation sayesinde, notlar özelliğine doğrudan erişim engellenmiştir.

print(ogrenci1)  # Ali Demir (123456)
#print(ogrenci1.ortalama_hesapla())  # 81.66666666666667