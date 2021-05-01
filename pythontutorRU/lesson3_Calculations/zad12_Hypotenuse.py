# Дано два числа a и b. Выведите гипотенузу треугольника с заданными катетами.
from math import sqrt

a = int(input('a: '))
b = int(input('b: '))
print(float(sqrt(a ** 2 + b ** 2)))