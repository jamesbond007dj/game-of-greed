import pytest
from game_of_greed import Game

def test_straight():
    game = Game()
    actual = game.calculate_score((3,2,4,5,1,6))

    assert False
