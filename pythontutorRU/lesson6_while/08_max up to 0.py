# Последовательность состоит из натуральных чисел и завершается числом 0.
# Определите значение наибольшего элемента последовательности.

y = 0
x = int(input())
while x != 0:
    if x > y:
        y = x
    x = int(input())
print(y)