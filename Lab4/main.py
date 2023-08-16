from typing import List
from functools import reduce

number: list[str] = []


def sqrt(nom):
    return nom ** 2


i = 0
while i < 4:
    a = input()
    n = float(a)
    number.insert(i, n)
    i = i + 1

print(number)

squared = list(map(sqrt, number))
print(squared)


def custom_sum(first, second):
    return first + second


result = reduce(custom_sum, squared)
print(result)
