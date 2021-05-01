# Дана строка. Удалите из нее все символы, чьи индексы делятся на 3.

string = str(input())
string2 = ''
for i in range(len(string)):
    if i % 3 != 0:
        string2 += string[i]
print(string2)

# можно ли короче сделать?