# Дано трехзначное число. Найдите сумму его цифр.

a = int(input())
print(a // 100 + int(a / 10) % 10 + a % 10)
print(a // 100)
print(int(a / 10) % 10)
print(a % 10)