class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.coins = 0

    def can_add(self, v):
        self.add_coins = v
        if (self.add_coins + self.coins) < self.capacity:
            return True
        else:
            return False

    def add(self, v):
        if self.can_add(v) is True:
            self.coins += v


Koshelek = MoneyBox(50)
Koshelek.add(40)
print(Koshelek.coins)
print(Koshelek.can_add(20))
Koshelek.add(20)
print(Koshelek.coins)

