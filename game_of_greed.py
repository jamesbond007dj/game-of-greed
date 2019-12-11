import sys
import re
import random
import time
import collections
import count


class Game:
    def __init__(self, print_func=print, input_func=input):
        self._print = print_func
        self._input = input_func
        self.score = 0
        self.pair = 0
        self.straight = 0
        self.dice = {1:1, 2:1, 3:1, 4:1, 5:1, 6:1}

    def play(self):
        self._print('Welcome to Game of Greed')
        main = self._input('Wanna play? Please type y to start game Type: ')
        if main == 'y':
            self._print('Great! Check back tomorrow')
        else:
            self._print('OK. Maybe another time')

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


    def calculate_score(self):
        for value, count in self.roll.items():

            self.score += self.dice[1] * 100
            self.score += self.dice[2] * 0
            self.score += self.dice[3] * 0
            self.score += self.dice[4] * 0
            self.score += self.dice[5] * 50
            self.score += self.dice[6] * 0

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


            if self.dice[1] == 3:
                self.score += roll_score_dictonary['three_one']
            elif self.dice[1] == 4:
                self.score += roll_score_dictonary['four_one']
            elif self.dice[1] == 5:
                self.score += roll_score_dictonary['five_one']
            elif self.dice[1] == 6:
                self.score += roll_score_dictonary['six_one']
            if self.dice[2] == 3:
                self.score += roll_score_dictonary['three_two']
            elif self.dice[2] == 4:
                self.score += roll_score_dictonary['four_two']
            elif self.dice[2] == 5:
                self.score += roll_score_dictonary['five_two']
            elif self.dice[2] == 6:
                self.score += roll_score_dictonary['six_two']
            if self.dice[3] == 3:
                self.score += roll_score_dictonary['three_three']
            elif self.dice[3] == 4:
                self.score += roll_score_dictonary['four_three']
            elif self.dice[3] == 5:
                self.score += roll_score_dictonary['five_three']
            elif self.dice[3] == 6:
                self.score += roll_score_dictonary['six_three']
            if self.dice[4] == 3:
                self.score += roll_score_dictonary['three_four']
            elif self.dice[4] == 4:
                self.score += roll_score_dictonary['four_four']
            elif self.dice[4] == 5:
                self.score += roll_score_dictonary['five_four']
            elif self.dice[4] == 6:
                self.score += roll_score_dictonary['six_four']
            if self.dice[5] == 3:
                self.score += roll_score_dictonary['three_five']
            elif self.dice[5] == 4:
                self.score += roll_score_dictonary['four_five']
            elif self.dice[5] == 5:
                self.score += roll_score_dictonary['five_five']
            elif self.dice[5] == 6:
                self.score += roll_score_dictonary['six_five']
            if self.dice[6] == 3:
                self.score += roll_score_dictonary['three_six']
            elif self.dice[6] == 4:
                self.score += roll_score_dictonary['four_six']
            elif self.dice[6] == 5:
                self.score += roll_score_dictonary['five_six']
            elif self.dice[6] == 6:
                self.score += roll_score_dictonary['six_six']
            else:
                self.score += 0
        return self.score

# Below is the method we did in lecture, i could not continue with it. I did more hard code as above.

    # def calculate_score(self, dice):
    #     # handle special cases of 6 dice
    #     if len(dice)== 6:
    #         roll_counter = Counter(dice)
    #         # straight
    #         if len(roll_conter) == 6
    #             return 1500
    #         #check for 3 pairs
    #         vals = roll_counter.values()
    #         val_set = set(vals)
    #         if len(val_set) == 3



    #     # {four:2,five:2,1:2} 3 pairs
    #     return 0


if __name__ == "__main__":
    game = Game()
    # game.start()
    game.calculate_score([1, 2, 3, 4, 5, 6])
