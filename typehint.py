def add_numbers(x: int, y: int) -> int:
    return x + y

num1: int = 10
num2: int = 20 # int tipi dışında bir değer atandı

print(add_numbers(num1, num2))
from typing import List

my_list: List[int] = [1, 2, 3]
my_list.append(4)
print(my_list)
#mypy typehint.py
#calıstırılırsa hangi tiplerin yanlış verildiği ortaya çıkar
#normalde type dönüşümü olarak algılamaktadır.