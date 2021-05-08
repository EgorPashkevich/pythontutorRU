# Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т. д.).
# Если элементов нечетное число, то последний элемент остается на своем месте.

a = [int(b) for b in input().split()]
a_2 = []
x = 0
if len(a) % 2 != 0:
    while x < len(a) - 1:
        a_2.append(a[x + 1])
        a_2.append(a[x ])
        x += 2
    else:
        a_2.append(a[len(a) - 1])
else:
    while x < len(a) - 1:
        a_2.append(a[x + 1])
        a_2.append(a[x ])
        x += 2
print(' '.join([str(i) for i in a_2]))

# второй вариант
# a = [int(b) for b in input().split()]
for i in range(1, len(a), 2):
    a[i], a[i - 1] = a[i - 1], a[i]
print(' '.join([str(i) for i in a]))

