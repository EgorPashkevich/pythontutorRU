# Дана строка. Замените в этой строке все появления буквы h на букву H,
# кроме первого и последнего вхождения.

string = str(input())
print(string[:string.find('h')+1] +
      string[string.find('h')+1: string.rfind('h')].replace('h', 'H') +
      string[string.rfind('h'):])