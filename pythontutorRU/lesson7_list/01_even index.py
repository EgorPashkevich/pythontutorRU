# Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...).
a = [input() for i in range(int(input()))]
print(a[::2])