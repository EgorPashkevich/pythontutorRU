# Дан текст: в первой строке задано число строк, далее идут сами строки.
# Выведите слово, которое в этом тексте встречается чаще всего. Если таких слов несколько,
# выведите то, которое меньше в лексикографическом порядке.

text = {}
for i in range(int(input())):
    line = input().split()
    for word in line:
        text[word] = text.get(word, 0) + 1
a = max(text.values())
most_common = [k for k, v in text.items() if v == a]
print(min(most_common))
