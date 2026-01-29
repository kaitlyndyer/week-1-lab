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

charmander = FireType("Charmander", 39, 0.2)
print(charmander.name)        # Charmander
print(charmander.current_hp)  # 39 (inherited)
print(charmander.burn_chance) # 0.2