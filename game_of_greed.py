import sys
import re
import random
import time
from collections import Counter


class Game:

    _validation_start = { 'y', 'yes' , 'ok', 'yepp'}
    def __init__(self, print_func=print, input_func=input):
        self._print = print_func
        self._input = input_func
        self.score = 0
        self.pairs = 0
        self._straight = 0
        self.num_rounds = 10
        self.roll = {1:1, 2:1, 3:1, 4:1, 5:1, 6:1}

    def play(self):
        self._print('Welcome to Game of Greed')
        main = self._input('Wanna play? Please type y to start game Type: ')
        if main.lower() in self._validation_start:
            self._print('Great! Check back tomorrow')
        else:
            self._print('OK. Maybe another time')

    def _start(self):
        self.score = 0
        round_num = 1
        for i in range(1, self.num_rounds + 1):
            round_score = self._do_round()
            self._print(f'You banked {round_score} points in round {round_num}')
            self.score += round_score
            round_num +=1
            self.print(f'You have {self.score} points total')
        self._print('Great Play!!! See you soon for fun again')

    def _do_round(self):
        num_dice = 6
        score =0
        while(True):
            self._print(f' Rolling {num_roll} dice')

            _roll = self._do_roll(num_roll)

            zilch_check_score = self.calculate_score(_roll)
            self._print(f'you rolled {roll}')

            if zilch_check_score == 0:
                self._print('Terrible for you... Zilch! You got 0 points')
                return 0

            keepers = self.validate_roll(_roll)

            num_roll -= len(keepers)

            score +=self.calculate_score(keepers)

            self._print(f'You can bank {score} points or Risk & Roll Dice for more')

            if num_roll == 0:
                num_roll = 6

            self.print(f'You can roll {num_roll} dice remaining')
            roll_again_response = self._input('Roll againg? ')

            if not roll_again_response.lower() in self._validation_start:
                break

        return score

        def validate(self, _roll, keepers):

            roll_counter = Counter(_roll)
            keepers_counter = Counter(keepers)
            return len(keepers_counter - roll_counter) == 0


    def _do_roll(self, num_roll):
        return [random.randint(1.6) for i in range(num_roll)]


    def calculate_score(self, _roll):
        score = 0
        roll_counter = Counter(_roll)

        ones = False
        fives = False

        for key in roll_counter:

            count = roll_counter[key]

            if count >= 3:
                score += key *100
                if key == 1:
                    score =1000
                    ones = True
                elif key == 5:
                    fives = True

            if count >=4:
                if key == 1:
                    score +=1000
                else:
                    score += key * 100

            if count >= 5:
                if key == 1:
                    score += 1000
                else:
                    score += key * 100

            if count == 6:
                if key == 1:
                    score += 1000
                else:
                    score += key * 100

        if len(roll_counter) == 6 :
            score =1500
            ones = True
            fives = True

        if len(roll_counter) == 3 and roll_counter.most_common()[2][1] == 2:
            score = 1500
            ones = True
            fives = True


        if not ones:
            score += roll_counter[1] * 100

        if not fives:
            score += roll_counter[5] * 50

        return score

# def validate_roll(self, roll):

#     while True:

#         keep_response = self._input('Roll dice to keep: ')

#         keepers = tuple(int(char) for char in keep_response)

#         if self.validate(roll, keepers):
#             return keepers
#         else:
#             self._print('You cant do that!!!Obey the rules')
#             self._print(roll)

# def validate(self, roll, keepers):

#     roll_counter = Counter(roll)
#     keepers_counter = Counter(keepers)
#     return len(keepers_counter - roll_counter) == 0



if __name__ == "__main__":
    game = Game()
    game.play()
    # game.calculate_score([1, 2, 3, 4, 5, 6])
