# Последовательность состоит из натуральных чисел и завершается числом 0. Определите,
# сколько элементов этой последовательности равны ее наибольшему элементу.

x_1 = 0
y_2 = 0
elem = -1
while elem != 0:
    if elem > x_1:
        x_1, y_2 = elem, 1
    elif elem == x_1:
        y_2 += 1
    elem = int(input())
print(y_2)