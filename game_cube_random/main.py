import random


class Game:
    def __init__(self):
        self.numbers_player = int(input('number of players: '))
        self.name_players = [input('Player № ' + str(i + 1) + ' enter your name(to play the bot, enter "bot"): ') for i in range(self.numbers_player)]
        self.glass = int(input('number of glasses(multiple of the number of players): '))
        self.random_dict = {'glass number:' + str(i + 1): random.randint(1, 4) for i in range(self.glass)}
        self.list_glass = [i for i in self.random_dict]
        self.glass_a = 'glass number:'
        # self.dict_players_point = {i: 0 for i in self.name_players}

    def check_for_bot(self):
        count = 0
        for i in self.name_players:
            if i == 'bot':
                count += 1
        if count > 1:
            for index, name in enumerate(self.name_players):
                if name == 'bot':
                    self.name_players[index] = 'bot №' + str(count)
                count -= 1

    def check_for_glass(self):
        while self.glass % self.numbers_player != 0:
            self.glass = int(input('ERROR, enter the number of glasses a multiple of the number of players.: '))
        self.random_dict = {'glass number:' + str(i + 1): random.randint(1, 6) for i in range(self.glass)}
        self.list_glass = [i for i in self.random_dict]

    def assigning_points_to_player(self):
        print('Select a glass: ' + ' | '.join(self.list_glass))
        print('choose number: ', end=' ')
        a = input()
        glass = 'glass number:' + a
        b = len(self.list_glass)
        while len(self.list_glass) != b - 1:
            if glass in self.list_glass:
                self.list_glass.remove(glass)
                return self.random_dict[glass]
            else:
                print('Select a glass: ' + ' | '.join(self.list_glass))
                print('!!! ERROR, choose from the list !!!')
                a = input()
                glass = 'glass number:' + a

    def assigning_points_to_bot(self):
        print('Select a glass: ' + ' | '.join(self.list_glass))
        glass = random.choice(self.list_glass)
        print('choose: ' + glass)
        self.list_glass.remove(glass)
        return self.random_dict[glass]

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
        global winner
        self.check_for_bot()
        self.check_for_glass()
        self.sorted_name_players()
        self.dict_players_point = {i: 0 for i in self.name_players}
        while bool(self.list_glass):
            for i in self.name_players:
                if i[:3] == 'bot':
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
                if v == winner_point:
                    print('no winner')
                    break
                winner_point = v
                winner = k
        print('WINNER ' + winner)


round1 = Game()
round1.start()
