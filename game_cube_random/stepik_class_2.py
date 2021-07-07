class Buffer:
    def __init__(self):
        self.list_buffer = []
        self.sum_a = 0

    def add(self, *a):
        self.list_buffer.extend(a)
        while len(self.list_buffer) >= 5:
            self.sum_a = sum(self.list_buffer[:5])
            self.list_buffer = self.list_buffer[5:]
            return self.sum_a                   # вопрос тут(

    def get_current_part(self):
        return self.list_buffer


buf = Buffer()
buf.add(1, 2, 3)
print(buf.get_current_part()) # вернуть [1, 2, 3]
print(buf.add(4, 5, 6)) # print(15) – вывод суммы первой пятерки элементов
print(buf.get_current_part()) # вернуть [6]
print(buf.add(7, 8, 9, 10)) # print(40) – вывод суммы второй пятерки элементов
print(buf.get_current_part()) # вернуть []
print(buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
print(buf.get_current_part()) # вернуть [1]