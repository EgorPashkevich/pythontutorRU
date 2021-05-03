# Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.

# мне кажется что можно проще...........

a = [int(input()) for i in range(int(input('numbers elem: ')))]
b = a[0]
for i in a:
    if i > b:
        print(i, end=' ')
    b = i