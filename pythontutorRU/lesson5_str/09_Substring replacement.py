# Дана строка. Замените в этой строке все цифры 1 на слово one.

string = str(input())
for i in string:
    print('one', end='') if i == '1' else print(i, end='')
