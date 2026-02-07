# CLASS EXERCISES
# starter code
class Pokemon:
    def __init__(self, name: str, max_hp: int) -> None:
        self.name = name
        self.max_hp = max_hp
        self.current_hp = max_hp

    def description(self) -> str:
        return f"{self.name} is a Normal type"


# basic subclass
# create a FireType class that inherits from Pokemon
class FireType(Pokemon):
    def __init__(self, name: str, max_hp: int, burn_chance: float) -> None:
        super().__init__(name, max_hp)
        self.burn_chance = burn_chance

    def description(self) -> str:  # Overrides the super class description method
        return f"{self.name} is a Fire type"


charmander = FireType("Charmander", 39, 0.2)
print(charmander.name)  # Charmander
print(charmander.current_hp)  # 39 (inherited)
print(charmander.burn_chance)  # 0.2
print(charmander.description())  # Charmander is a Fire type


# second subclass
# create a WaterType class with itse own attribute an description override Add a swim_speed attribute (int) and override description() to return "<name> is a Water type"
class WaterType(Pokemon):
    def __init__(self, name: str, max_hp: int, swim_speed: int) -> None:
        super().__init__(name, max_hp)
        self.swim_speed = swim_speed

    def description(self):
        return f"{self.name} is a Water type"


squirtle = WaterType("Squirtle", 44, 5)
print(squirtle.swim_speed)  # 5
print(squirtle.description())  # Squirtle is a Water type
