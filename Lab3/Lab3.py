from pyDatalog import pyDatalog
from random import randint

pyDatalog.clear()

pyDatalog.create_atoms('N, Sum')
Sum[N] = (N == 0) & (Sum[N] == 0)
Sum[N] = (N > 0) & (Sum[N] == Sum[N-1] + N)

pyDatalog.create_atoms('Avg')
Avg[N] = (Avg[N-1] * (N-1) + N) / N

pyDatalog.create_atoms('X, Median')
for _ in range(1000000):
    X[randint(0, 999999)]

Median[N] = (Median[X] == X) & (N == 0)
Median[N] = (Median[X] < X) & (N == Median[N-1] + 1)
Median[N] = (Median[X] >= X) & (N == Median[N-1])

pyDatalog.create_atoms('Product')
Product[N] = (Product[X] == X) & (N == 1)
Product[N] = (Product[X] == Product[N-1] * X)

print("Сумма ряда: ", Sum[999999])
print("Среднее значение ряда: ", Avg[999999])
print("Медиана случайных 1000000 чисел: ", Median[500000])
print("Произведение случайных 1000000 чисел: ", Product[1000000])