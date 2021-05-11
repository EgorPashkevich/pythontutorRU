# Дан двумерный массив и два числа: i и j. Поменяйте в массиве столбцы с номерами i и j и выведите результат.
# Программа получает на вход размеры массива n и m, затем элементы массива, затем числа i и j.
# Решение оформите в виде функции swap_columns(a, i, j).


def swap_columns(a, i, j):
    for x in range(len(a)):
        a[x][i], a[x][j] = a[x][j], a[x][i]


n, m = [int(i) for i in input('n and m: ').split()]
a = [[int(j) for j in input().split()] for i in range(n)]
i, j = [int(i) for i in input('i and j: ').split()]

swap_columns(a, i, j)
print('\n'.join([' '.join([str(i) for i in elem]) for elem in a]))
