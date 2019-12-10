import sys
import re
import random
import time
import collections


class Game:
    def __init__(self, print_func=print, input_func=input):
        self._print = print_func
        self._input = input_func
        self.score = 0
        self.dice = [1, 2, 3, 4, 5, 6]

    def start(self):
        self._print('Welcome to Game of Greed')
        main = self._input('Wanna play? Please type y to start game Type: ')
        if main == 'y':
            self._print('Great! Check back tomorrow')
        else:
            self._print('OK. Maybe another time')

    def calculate_score(self, ll):
        for val in ll:
            if val == 1:
                self.score += 100
            elif val == 5:
                self.score += 50
        return self.score


if __name__ == "__main__":
    game = Game()
    # game.start()
    game.calculate_score([1, 2, 3, 4, 5, 6])
