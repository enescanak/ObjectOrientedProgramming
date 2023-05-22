
# Python Object Oriented Programming (OOP) 

OOP is an object-oriented programming technique. In this programming approach, everything revolves around objects. OOP primarily focuses on three main concepts: Encapsulation, Inheritance, and Polymorphism. Additionally, we can also include Abstraction. Each subheading below is explained with Object-Oriented Programming (OOP) code examples.

  
## Object Oriented Programming (OOP) Steps

![Uygulama Ekran Görüntüsü](https://lh6.googleusercontent.com/yPsibbUh1aHOvi0U3-wtdlNpWWutbyYULv1PLkx0QlOOq81DiXVvPgvKVrtY7Ef1yZF5NLabXrHBjHL80lx9hTqR_64jGRFZdbR9FIs4LDR9RcEn1M9LX_D5i4fYKR4vNZA-dZ9R)

## Run the Project on your own

Clone the project

```bash
  git clone https://github.com/enescanak/yongaAutoDrone.git
```

Go to the project file

```bash
  cd ObjectOrientedProgramming
```
In this project DataClasses are used, so you should use pyhton3.8+.

## Examples of object oriented programming (OOP)
You can review the 1)object_Class.py code for more details on the topic.
```python
# Creating a araba Class
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

```
You can review the 1)object_Class.py code for more details on the topic.
```python
# Creating a araba object
araba1 = Araba("Toyota", "Kirmizi", 0)
```
You can review the 2)inheritance.py code for more details on the topic.
```python
# Creating a class that takes inheritance
class Otobus(Araba):
    def __init__(self, yolcu_sayisi):
        #super().__init__()
        self.yolcu_sayisi = yolcu_sayisi
```
You can review the 3)Polymorphism.py code for more details on the topic.
```python
# Polymorphism Class
from dataclasses import dataclass
@dataclass
class Arac:
    marka: str
    model: str
    def tanim(self):
        print(f"Bu araç bir {self.marka} {self.model}")

    def hareket_et(self):
        print("Araç hareket ediyor...")
```
You can review the 4)abstract.py code for more details on the topic.
```python
# creating a abstractMethod 
from abc import ABC, abstractmethod
from dataclasses import dataclass,field
@dataclass 
class Hesap(ABC): 
    
    bakiye: int = field(default_factory=int)
    enes: int= field(default_factory=int)
    def __post_init__(self):
        pass
    def para_gor(self): 
        pass
    @abstractmethod 
    def para_yatir(self, miktar): 
        pass 

    @abstractmethod 
    def para_cek(self, miktar):
        pass 
```
You can review the 5)python_encapsulation.py code for more details on the topic.
```python
# Encapsule the values. 
@dataclass
class Employee:
    name: str
    age: int
    salary: float

    def __pos_init__(self):
        self.__name = self.name
        self.__age = self.age
        self.__salary = self.salary

```

## Addition

In addition, when a float value is passed to a variable of type int in Python, it may go unnoticed. To detect incorrect value assignments in the code, a typehint.py script has been written. The code provides more details on this topic within its contents.

```bash
  mypy typehint.py
```
## Lisans

[MIT](https://choosealicense.com/licenses/mit/)

  