# Дано N чисел: сначала вводится число N, затем вводится ровно N целых чисел.
# Подсчитайте количество нулей среди введенных чисел и выведите это количество.
# Вам нужно подсчитать количество чисел, равных нулю, а не количество цифр.

n = int(input())
sum = 0
for i in range(n):
    a = int(input())
    if a == 0:
        sum += 1
print(sum)