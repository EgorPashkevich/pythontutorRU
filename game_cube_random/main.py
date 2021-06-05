import random


class Game:
    def __init__(self):
        self.numbers_player = int(input('number of players: '))
        self.name_players = [input('Player № ' + str(i + 1) + ' enter your name: ') for i in range(self.numbers_player)]
        self.glass = int(input('number of glasses: '))
        self.random_dict = {'glass number:' + str(i + 1): random.randint(1, 6) for i in range(self.glass)}
        self.list_glass = [i for i in self.random_dict]
        self.dict_players_point = {i: 0 for i in self.name_players}

    def assigning_points_to_player(self):
        print('Select a glass: ' + ' | '.join(self.list_glass))
        glass = input('choose: ')
        if glass not in self.list_glass:
            print('!!! ERROR, choose from the list !!!')
            self.assigning_points_to_player()
        else:
            self.list_glass.remove(glass)
            return self.random_dict[glass]

    def assigning_points_to_bot(self):
        print('Select a glass: ' + ' | '.join(self.list_glass))
        glass = random.choice(self.list_glass)
        print('choose: ' + glass)
        self.list_glass.remove(glass)
        return self.random_dict[glass]

    # def assigning_names_is_classes(self):     ПОКА НЕ СМОТРИ, ПОХЖЕ БУДУТ ВОПРОСЫ
    #     for i in self.name_players:           ПОКА НЕ СМОТРИ, ПОХЖЕ БУДУТ ВОПРОСЫ
    #         i = Player(i)                     ПОКА НЕ СМОТРИ, ПОХЖЕ БУДУТ ВОПРОСЫ

    def sorted_name_players(self):
        empty_list = []
        count = len(self.name_players)
        while bool(self.name_players):
            random_name = random.choice(self.name_players)
            empty_list.append(random_name)
            self.name_players.remove(random_name)
        self.name_players = empty_list
        return self.name_players

    def start(self):
        # self.assigning_names_is_classes()
        global winner
        self.sorted_name_players()
        while bool(self.list_glass):
            for i in self.name_players:
                if i == 'bot':
                    print('Play ' + i)
                    self.dict_players_point[i] += self.assigning_points_to_bot()
                    print(self.dict_players_point)
                else:
                    print('Play ' + i)
                    self.dict_players_point[i] += self.assigning_points_to_player()
                    print(self.dict_players_point)
        winner_point = 0
        for k, v in self.dict_players_point.items():
            if v > winner_point:
                winner_point = v
                winner = k
        print('WINNER ' + winner)


# class Player(Game):                               ПОКА НЕ СМОТРИ, ПОХЖЕ БУДУТ ВОПРОСЫ
#     def __init__(self, name):
#         super().__init__()
#         self.name = name
#         self.points = 0
#
#     def get_point(self):
#         self.points += self.assigning_points_to_player()


round1 = Game()
round1.start()
