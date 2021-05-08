# Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
# Элементы нужно выводить в том порядке, в котором они встречаются в списке.

a = [int(i) for i in input().split()]
for i in range(len(a)):
    for j in range(len(a)):
        if a[i] == a[j] and i != j:
           break
    else:
        print(a[i], end=' ')