from game_of_greed import Game
import pytest

def test_game_one():
    game = Game()
    assert game

def test_flow_yes():

    prints = ['Welcome to Game of Greed','Great! Check back tomorrow']
    prompts = ['Wanna play? Please type y to start game Type: ']
    responses = ['y']

    def mock_print(*args):
        if len(prints):
            current_print = prints.pop(0)
            assert args[0] == current_print

    def mock_input(*args):
        if len(prompts):
            current_prompt = prompts.pop(0)
            assert args[0] == current_prompt

        if len(responses):
            current_response = responses.pop(0)
            return current_response

    game = Game(mock_print, mock_input)

    game.play()

def test_flow_no():

    prints = ['Welcome to Game of Greed','OK. Maybe another time']
    prompts = ['Wanna play? Please type y to start game Type: ']
    responses = ['n']

    def mock_print(*args):
        if len(prints):
            current_print = prints.pop(0)
            assert args[0] == current_print

    def mock_input(*args):
        if len(prompts):
            current_prompt = prompts.pop(0)
            assert args[0] == current_prompt

        if len(responses):
            current_response = responses.pop(0)
            return current_response

    game = Game(mock_print, mock_input)

    game.play()


# def test_score_1and5(game):
#     game = Game()
#     score = game.calculate_score('straight')
#     actual = score
#     expected = 150
#     assert actual == expected

# def test_zilch(game):
#     expected = 0
#     actual = game.calculate_score((3,2,2,6,4,4))
#     assert actual == expected


# def test_calculate_score(game, roll, expected):
#     actual = game.calculate_score(roll)
#     assert actual == expected

# def test_calculate_two_roll():
#     game = Game()
#     actual = game.calculate_score((3,1))
#     expected = 100
#     assert expected == actual


# @pytest.mark.parametrize("roll, expected",[
#   ([1], 100),
#   ([1,1], 200),
#   ([1,1,1], 1000),
#   ([1,1,1,1], 2000),
#   ([1,1,1,1,1], 3000),
#   ([1,1,1,1,1,1], 4000)
# ])
# def test_ones(game, roll, expected):
#   assert expected == game.calculate_score(roll)

# @pytest.mark.parametrize("roll, expected",[((6,6,6,2), 900),((4,5,2,1,6,3), 150),])
# def test_calculate_complex(game, roll, expected):
#     actual = game.calculate_score(roll)
#     assert actual == expected

def test_zilch():
    test_game = Game()
    actual = test_game.calculate_score((6, 3, 4, 2, 6, 2))
    assert 0 == actual


def test_3_pairs():
    test_game = Game()
    actual = test_game.calculate_score((6, 4, 4, 2, 6, 2))
    assert 1500 == actual

def test_straigt():
    test_game = Game()
    actual = test_game.calculate_score((6, 5, 4, 1, 3, 2))
    assert 1500 == actual

def test_1_and_5():
    test_game = Game()
    actual = test_game.calculate_score((6, 5, 4, 1, 4, 2))
    assert 150 == actual

@pytest.mark.parametrize("roll, keepers, expected",[
    ([1,2,3],(1,),True),
    ([1,2,3],(1,2),True),
    ([1,2,3],(1,2,3),True),
    ([1,2,3],(6,),False),
    ([1,2,3],(1,1),False),
])
def test_validate(game, roll, keepers, expected):
    actual = game.validate(roll, keepers)
    assert actual == expected

class MockPlayer:
    def __init__(self, prints=[], prompts=[], responses=[], rolls=[]):
        self.prints = prints
        self.prompts = prompts
        self.responses = responses
        self.rolls = rolls

    def mock_print(self, *args):
        if len(self.prints):
            current_print = self.prints.pop(0)
            assert args[0] == current_print

    def mock_input(self, *args):
        if len(self.prompts):
            current_prompt = self.prompts.pop(0)
            assert args[0] == current_prompt

        if len(self.responses):
            current_response = self.responses.pop(0)
            return current_response

    def mock_roll(self, num_dice):
        if len(self.rolls):
            current_roll = self.rolls.pop(0)
            return current_roll

    def mop_up(self):
        assert len(self.prints) == 0
        assert len(self.prompts) == 0
        assert len(self.responses) == 0
        assert len(self.rolls) == 0
        return True

@pytest.fixture()
def game():
  return Game()


