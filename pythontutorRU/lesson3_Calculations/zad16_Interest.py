# Процентная ставка по вкладу составляет P процентов годовых,
# которые прибавляются к сумме вклада. Вклад составляет X рублей Y копеек.
# Определите размер вклада через год.
# Программа получает на вход целые числа P, X, Y и должна вывести два числа:
# величину вклада через год в рублях и копейках.
# Дробная часть копеек отбрасывается.

P = int(input())
X = int(input())
Y = int(input())
print(((X * 100 + Y) * (P + 100) / 100) // 100, 'rub', ((X * 100 + Y) * (P + 100) / 100) % 100, 'kop')