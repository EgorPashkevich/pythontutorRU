# В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.
a = [int(s) for s in input().split()]
a[a.index(max(a))], a[a.index(min(a))] = a[a.index(min(a))], a[a.index(max(a))]
print(' '.join([str(i) for i in a]))