class Iter_dict():
    def __init__(self, a):
        self.a = a
        self.index_1 = 0
        self.index_2 = 1
        self.main_dict = tuple()
        self.side1_dict = {}
        self.side2_dict = {}

    def __iter__(self):
        return self

    def __next__(self):
        if self.index_2 == len(self.a):
            raise StopIteration
        try:
            self.side1_dict[str(self.index_1) + ' & ' + str(self.index_2)] = int(self.a[self.index_1]) + int(self.a[self.index_2])
        except ValueError:
            self.side2_dict[str(self.index_1) + ' & ' + str(self.index_2)] = self.a[self.index_1] + self.a[self.index_2]
        self.index_1 += 1
        self.index_2 += 1
        self.main_dict = (self.side1_dict, self.side2_dict)
        return self.main_dict


x = Iter_dict(input().split())
j = {}
for i in x:
    j = i
print(j)

