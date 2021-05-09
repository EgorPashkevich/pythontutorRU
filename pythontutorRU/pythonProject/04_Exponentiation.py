# Дано действительное положительное число a и целое неотрицательное число n.
# Вычислите an не используя циклы, возведение в степень через ** и функцию math.pow(),
# а используя рекуррентное соотношение an=a⋅an-1.
# Решение оформите в виде функции power(a, n).

def exponentiation(a, n):
    if n == 1:
        return a
    else:
        return a * exponentiation(a, n - 1)

print(exponentiation(float(input()), int(input())))
