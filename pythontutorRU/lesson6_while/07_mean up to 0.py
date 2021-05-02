# Определите среднее значение всех элементов последовательности, завершающейся числом 0.

sum = 0
sum2 = 0
x = int(input())
while x != 0:
    sum += x
    sum2 += 1
    x = int(input())
print(sum / sum2)
