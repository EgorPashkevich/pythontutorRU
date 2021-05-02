# Дано натуральное число A. Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φn = A.
# Если А не является числом Фибоначчи, выведите число -1.

N = int(input())
a, b = 0 , 1
num_elem = 1
while b != N:
    a, b = b, a + b
    num_elem += 1
    if b > N:
        num_elem = -1
        break
print(num_elem)
