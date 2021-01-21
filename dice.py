# Implementation of a dice using random module in python

import random


class Dice:
    def roll(self):
        first = random.randint(1, 6)      #Generates random number between 1-6
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll()
