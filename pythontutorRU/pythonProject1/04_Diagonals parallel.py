# Дано число n. Создайте массив размером n×n и заполните его по следующему правилу.
# На главной диагонали должны быть записаны числа 0. На двух диагоналях,
# прилегающих к главной, числа 1. На следующих двух диагоналях числа 2, и т.д.

n = int(input())
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j] = abs(j - i)
for i in a:
    print(' '.join([str(elem) for elem in i]))
print()

# n = int(input())
a = [[abs(i - j) for j in range(n)] for i in range(n)]
for i in a:
    print(' '.join([str(elem) for elem in i]))