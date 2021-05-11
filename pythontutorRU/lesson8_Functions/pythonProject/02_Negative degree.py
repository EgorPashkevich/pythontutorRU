# Дано действительное положительное число a и целоe число n.
# Вычислите an. Решение оформите в виде функции power(a, n).
# Стандартной функцией возведения в степень пользоваться нельзя.

def power(a, n):
    b = 1
    for i in range(abs(n)):
        b *= a
    if n >= 0:
        return b
    else:
        return 1 / b
print(power(float(input()), int(input())))

