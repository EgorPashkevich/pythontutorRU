# Дано несколько чисел. Вычислите их сумму. Сначала вводите количество чисел N,
# затем вводится ровно N целых чисел.
# Какое наименьшее число переменных нужно для решения этой задачи?

# можно сократить программу?

sum = 0
a = int(input())
for i in range(a):
    b = int(input())
    sum += b
print(sum)