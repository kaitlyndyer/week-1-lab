import random

# CLASS EXERCISES
## Create a Dice class for rolling dice
class Dice:
    def __init__(self, sides=6):
        self.sides = sides
        self.last_roll = None

    def roll(self):
        self.last_roll = random.randint(1, self.sides)
        return self.last_roll
    
    def __str__(self):
        if self.last_roll is None:
            return "Not rolled yet"
        else:
            return f'Last roll: {self.last_roll}'
    
    def __repr__(self):
        return f'Dice(sides={self.sides})'
    
        
dice = Dice()
print(dice)
print(repr(dice))

dice.roll()
print(dice)
