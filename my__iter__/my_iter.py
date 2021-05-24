class MyIter:
    def __init__(self, list):
        self.list = list
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.list):
            raise StopIteration
        self.num = self.list[self.index] ** 2
        self.index += 1
        return self.num


x = MyIter([int(b) for b in input().split()])
for i in x:
    print(i)
