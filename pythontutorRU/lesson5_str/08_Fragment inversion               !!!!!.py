# Дана строка, в которой буква h встречается как минимум два раза.
# Разверните последовательность символов,
# заключенную между первым и последним появлением буквы h, в противоположном порядке.

string = str(input())
print(string[string.find('h') + 1: string.rfind('h'):-1])    # что тут не так? почему он не дает ответ?
print(string[string.find('h') + 1: string.rfind('h'):])

# In the hole in the ground there lived a hobbit
# для примера