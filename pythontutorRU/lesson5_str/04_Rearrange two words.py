# Дана строка, состоящая ровно из двух слов, разделенных пробелом.
# Переставьте эти слова местами. Результат запишите в строку и выведите получившуюся строку.

string = str(input())
print(string[string.find(' ') + 1:], string[:string.find(' ')], sep=' ')