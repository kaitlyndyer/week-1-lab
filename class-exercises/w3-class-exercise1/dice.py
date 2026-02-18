import random


# CLASS EXERCISES
## Create a Dice class for rolling dice
class Dice:
    def __init__(self, sides: int = 6) -> None:
        self.sides = sides
        self.last_roll = None

    def roll(self) -> int:
        self.last_roll = random.randint(1, self.sides)
        return self.last_roll

    def __str__(self) -> str:
        return "Not rolled yet" if self.last_roll == None else f'Last roll: {self.last_roll}'
    
    def __repr__(self) -> str:
        return f'Dice(sides={self.sides})(last_roll={self.last_roll})'



dice = Dice()
print(dice)
print(repr(dice))

dice.roll()
print(dice)
