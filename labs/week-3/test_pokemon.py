from pokemon import Pokemon, FireType, WaterType
from trainer import Trainer


# Normal types - Pokemon(name, max_hp, attack, defence, move, move_power)
pikachu = Pokemon("Pikachu", 35, 11, 7, "Quick Attack", 10)
eevee = Pokemon("Eevee", 55, 10, 8, "Tackle", 10)
snorlax = Pokemon("Snorlax", 160, 11, 10, "Body Slam", 20)
meowth = Pokemon("Meowth", 40, 9, 7, "Scratch", 10)

# Fire types - FireType(name, max_hp, attack, defence, move, move_power, burn_chance)
charmander = FireType("Charmander", 39, 12, 8, "Ember", 10, 0.2)
vulpix = FireType("Vulpix", 38, 9, 8, "Flamethrower", 22, 0.1)
ponyta = FireType("Ponyta", 50, 17, 11, "Flame Charge", 12, 0.1)

# Water types - WaterType(name, max_hp, attack, defence, move, move_power, swim_speed)
squirtle = WaterType("Squirtle", 44, 9, 10, "Water Gun", 10, 5)
psyduck = WaterType("Psyduck", 50, 10, 9, "Water Pulse", 15, 4)
staryu = WaterType("Staryu", 30, 9, 11, "Swift", 15, 7)