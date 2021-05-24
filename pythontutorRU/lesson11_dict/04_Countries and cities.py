# Дан список стран и городов каждой страны. Затем даны названия городов.
# Для каждого города укажите, в какой стране он находится.

a = {}
for i in range(int(input())):
    country, *cities = input().split()
    for city in cities:
        a[city] = country

for i in range(int(input())):
    print(a[input()])


