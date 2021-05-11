# аны два числа n и m. Создайте двумерный массив размером n×m и заполните его символами "." и "*" в шахматном порядке.
# В левом верхнем углу должна стоять точка.

n, m = [int(i) for i in input().split()]
a = [['*' for i in range(m)] for j in range(n)]
for i in range(n):
    for j in range(m):
        if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):  #if (i + j) % 2 == 0:
            a[i][j] = '.'
for i in a:
    print(' '.join(i))