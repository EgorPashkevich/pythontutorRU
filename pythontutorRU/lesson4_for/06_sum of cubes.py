# По данному натуральному n вычислите сумму 13+23+33+...+n3.

n = int(input())
sum = 0
for i in range(n + 1):
    sum += i ** 3
print(sum)