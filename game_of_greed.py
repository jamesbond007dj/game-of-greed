import sys, re, random, time

class Game:
    def __init__(self, print_func=print,input_func=input):
        self._print = print_func
        self._input = input_func

    def start(self):
        self._print('Welcome to Game of Greed')
        main = self._input('Wanna play? Type: ')
            if main == 'y'
                print('Great! Check back tomorrow')
                continue
            else:
                print('OK. Maybe another time')
                break

# start_calculate()

# def start_calculate


# class Dice:
#     def __init__(self):
#         self.dice_numbers = [1 : '1', 2: '2' , 3: '3', 4: '4', 5: '5', 6: '6']

#     def feed(self, ingestible):
#         if ingestible not in self.sweets:
#             raise NotSweetError('Sweets only!')

#         # do other stuff
#         2/0 # breaking on purpose

#         return True


# class NotSweetError(ValueError):
#     pass

# if __name__ == "__main__":
#     st = SweetTooth()

#     try:
#         st.feed('celery')
#     except NotSweetError as nse: # good way
#         print('I tried to feed healthy!')
#         print(nse)
#     except:
#         print('uh ohs')





if __name__ == "__main__":
   pass
