import sys
import re
import random
import time
from collections import Counter


class Game:

    _validation = { 'y', 'yes' , 'ok', 'yepp'}
    def __init__(self, print_func=print, input_func=input):
        self._print = print_func
        self._input = input_func
        self.score = 0
        self.pairs = 0
        self.straight = 0
        self.roll = {1:1, 2:1, 3:1, 4:1, 5:1, 6:1}

    def play(self):
        self._print('Welcome to Game of Greed')
        main = self._input('Wanna play? Please type y to start game Type: ')
        if main.lower() in self._validation:
            self._print('Great! Check back tomorrow')
        else:
            self._print('OK. Maybe another time')


    def _do_roll(self, num_roll):
        return [random.randint(1.6) for i in range(num_roll)]

    roll_score_dictonary = {
    'straight': 1500,
    'three_pairs': 1500,
    'three_one': 1000,
    'four_one': 2000,
    'five_one': 3000,
    'six_one': 4000,
    'three_two': 200,
    'four_two': 400,
    'five_two': 600,
    'six_two': 800,
    'three_three': 300,
    'four_three': 600,
    'five_three': 900,
    'six_three': 1200,
    'three_four': 400,
    'four_four': 800,
    'five_four': 1200,
    'six_four': 1600,
    'three_five': 500,
    'four_five': 1000,
    'five_five': 1500,
    'six_five': 2000,
    'three_six': 600,
    'four_six': 1200,
    'five_six': 1800,
    'six_six': 2400,
    }


    def calculate_score(self, roll):
        roll = Counter(roll)
        _straigt = True
        for value, count in self.roll.items():

            self.score += self.roll[1] * 100
            self.score += self.roll[2] * 0
            self.score += self.roll[3] * 0
            self.score += self.roll[4] * 0
            self.score += self.roll[5] * 50
            self.score += self.roll[6] * 0

            if count != 1:
                self.straight = False


            if count == 2:
                self.pairs += 1


            if self.pairs == 3:
                self.score += 1500

            if self.roll.items() == {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}:
                self.score += int(roll_score_dictonary['straight'])

            if self.straight:
                self.score += roll_score_dictonary['straight']


            if self.roll[1] == 3:
                self.score += roll_score_dictonary['three_one']
            elif self.roll[1] == 4:
                self.score += roll_score_dictonary['four_one']
            elif self.roll[1] == 5:
                self.score += roll_score_dictonary['five_one']
            elif self.roll[1] == 6:
                self.score += roll_score_dictonary['six_one']
            if self.roll[2] == 3:
                self.score += roll_score_dictonary['three_two']
            elif self.roll[2] == 4:
                self.score += roll_score_dictonary['four_two']
            elif self.roll[2] == 5:
                self.score += roll_score_dictonary['five_two']
            elif self.roll[2] == 6:
                self.score += roll_score_dictonary['six_two']
            if self.roll[3] == 3:
                self.score += roll_score_dictonary['three_three']
            elif self.roll[3] == 4:
                self.score += roll_score_dictonary['four_three']
            elif self.roll[3] == 5:
                self.score += roll_score_dictonary['five_three']
            elif self.roll[3] == 6:
                self.score += roll_score_dictonary['six_three']
            if self.roll[4] == 3:
                self.score += roll_score_dictonary['three_four']
            elif self.roll[4] == 4:
                self.score += roll_score_dictonary['four_four']
            elif self.roll[4] == 5:
                self.score += roll_score_dictonary['five_four']
            elif self.roll[4] == 6:
                self.score += roll_score_dictonary['six_four']
            if self.roll[5] == 3:
                self.score += roll_score_dictonary['three_five']
            elif self.roll[5] == 4:
                self.score += roll_score_dictonary['four_five']
            elif self.roll[5] == 5:
                self.score += roll_score_dictonary['five_five']
            elif self.roll[5] == 6:
                self.score += roll_score_dictonary['six_five']
            if self.roll[6] == 3:
                self.score += roll_score_dictonary['three_six']
            elif self.roll[6] == 4:
                self.score += roll_score_dictonary['four_six']
            elif self.roll[6] == 5:
                self.score += roll_score_dictonary['five_six']
            elif self.roll[6] == 6:
                self.score += roll_score_dictonary['six_six']
            else:
                self.score += 0
        return self.score





if __name__ == "__main__":
    game = Game()
    game.play()
    # game.calculate_score([1, 2, 3, 4, 5, 6])
