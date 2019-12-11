from game_of_greed import Game
import pytest

def test_Game_one():
    game = Game()
    assert game


def test_score_1and5():
    game = Game()
    score = game.calculate_score([1, 2, 3, 4, 5, 6])
    actual = score
    expected = 150
    assert actual == expected


def test_score_1and5_more():
    game = Game()
    score = game.calculate_score([1, 2, 1, 4, 5, 5])
    actual = score
    expected = 300
    assert actual == expected

def test_score_two():
    game = Game()
    score = game.calculate_score([1, 2, 2, 4, 5, 5])
    actual = score
    expected = 300
    assert actual == expected
