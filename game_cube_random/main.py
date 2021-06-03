import random

class Game:
    def __init__(self):
        self.player_1 = 0
        self.player_2 = 0
        self.glass = 4
        self.random_dict = dict()
        self.list_glass = []

    def glass_up(self):
        for i in range(self.glass):
            self.random_dict['glass number:' + str(i + 1)] = random.randint(1, 4)
        for i in self.random_dict:
            self.list_glass.append(i)
            return self.random_dict, self.list_glass

    def glass_selection(self):
        print(' ; '.join(self.list_glass))
        a = input()
        self.list_glass.remove(a)
        return self.random_dict[a]

    def add_to_player_1(self):
        self.player_1 = self.player_1 + Game.glass_selection(self)
        return self.player_1

    def add_to_player_2(self):
        self.player_2 = self.player_2 + Game.glass_selection(self)
        return self.player_2

    def start(self):
        while self.list_glass is False:
            Game.add_to_player_1(self)
            Game.add_to_player_2(self)
        if self.player_1 > self.player_2:
            print('WINNER PLAYER № 1')
        elif self.player_1 < self.player_2:
            print('WINNER PLAYER № 2')
        else:
            print('no winner')


round1 = Game
round1.glass_up()





