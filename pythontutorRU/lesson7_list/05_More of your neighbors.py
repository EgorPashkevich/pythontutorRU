# Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей,
# и выведите количество таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.

a = [int(input()) for i in range(int(input()))]
sum = 0
for i in range(len(a) - 1):
    if a[i] < a[i + 1] > a[i + 2]:
        sum += 1
print(sum)