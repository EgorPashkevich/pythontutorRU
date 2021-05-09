# аны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2),
# вычисляющая расстояние между точкой (x1,y1) и (x2,y2).
# Считайте четыре действительных числа и выведите результат работы этой функции.
from cmath import sqrt


def distance(x1, y1, x2, y2):
    return  sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
# print(distance(float(a) for a in input('enter to 4 numbers: ').split()))           ??????????????
print(distance(float(input()), float(input()), float(input()), float(input())))