# Выведите все четные элементы списка.
# При этом используйте цикл for, перебирающий элементы списка, а не их индексы!

a = [int(input('elem: ')) for i in range(int(input('number elem: ')))]
for i in a:
    if i % 2 == 0:
        print(i, end=' ')

