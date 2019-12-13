from game_of_greed import Game


class LazyPlayer:
    # play and calculate score avaliable
    # everything else is done I/O

    def __init__(self):
        self.roll = None

    def _print(self, *args):
        print(args[0])

    def _input(self, *args):
        print(args[0], 'n')
        return 'n'

class BondPlayer:

    def __init__(self):
        self.roll = None
        self.name = None


    def _print(self, *args):

        msg =args[0]

        if msg.startswith('You rolled'):
            self.roll = [int(char) for char in msg if char.isdigit()}
        print(args[0])

    def _input(self, *args):
        prompt = arg[0]

        if prompt == 'Wanna play? Please type y to start game Type: ':
            print(prompt, 'y')
        return 'y'

        if prompt == 'Roll again: ':
            print(prompt, 'n')
        return 'n'

        # if prompt == 'Which would like to keep?  ':
        #     score = self.game.calculate_score(self.roll)

        if 1 in self.roll:
            return '1'



if __name__ == "__main__":
    bot = LazyPlayer()
    bot = BondPlayer()
    game = Game(bot._print, bot._input)
    bot.game = game
    game.play(1)
