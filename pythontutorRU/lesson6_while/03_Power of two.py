# По данному натуральному числу N найдите наибольшую целую степень двойки,
# не превосходящую N. Выведите показатель степени и саму степень.
# Операцией возведения в степень пользоваться нельзя!

n = int(input())
a = 1
x = 0
while a <= n:
    a *= 2
    x += 1
print(x - 1, end=' ')
print(int(a / 2))