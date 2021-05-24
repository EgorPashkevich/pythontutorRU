# Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову.
# Все слова в словаре различны.
# Для слова из словаря, записанного в последней строке, определите его синоним.

n = int(input())
d = {}
for i in range(n):
    a, b = input().split()
    d[a] = b
    d[b] = a
print(d[input()])