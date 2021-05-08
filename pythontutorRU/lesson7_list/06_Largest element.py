# Дан список чисел. Выведите значение наибольшего элемента в списке, а затем индекс этого элемента в списке.
# Если наибольших элементов несколько, выведите индекс первого из них.

a = [int(input()) for i in range(int(input()))]
b = 0
index = 0
print(len(a))
for i in range(len(a)):
    if a[i] > b:
        b = a[i]
print(b, end=' -- index:')
print(a.index(b))
