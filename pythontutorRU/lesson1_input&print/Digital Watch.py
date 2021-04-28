n = int(input('enter minutes '))
print(n // 60 - (n // 1440) * 24, ':', n % 60)
