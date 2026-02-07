import pytest
from pokemon import Pokemon, FireType, WaterType


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

"""
Write tests covering:

- Initial `current_hp` equals `max_hp`
- `is_fainted` returns `True` when HP is 0
- `is_fainted` returns `False` when HP is above 0
- `attack_move` returns the correct format with the Pokemon's move
- `__str__` returns the correct format
- `FireType.description()` returns Fire type message
- `WaterType.description()` returns Water type message
- Base `Pokemon.description()` returns Normal type message
"""


def test_initial_current_hp_equals_max_hp():
    assert pikachu.current_hp == pikachu.max_hp
    assert charmander.current_hp == charmander.max_hp
    assert squirtle.current_hp == squirtle.max_hp


def test_is_fainted_returns_true_when_hp_is_zero():
    test_pokemon = Pokemon("Test", 35, 11, 7, "Quick Attack", 10)
    test_pokemon.current_hp = 0
    assert test_pokemon.is_fainted() == True


def test_is_fainted_returns_false_when_hp_above_zero():
    assert eevee.is_fainted() == False
    test_pokemon = Pokemon("Test", 35, 11, 7, "Quick Attack", 10)
    test_pokemon.current_hp = 10
    assert test_pokemon.is_fainted() == False


def test_attack_move_returns_correctly():
    assert eevee.attack_move() == "Eevee uses Tackle!"
    assert vulpix.attack_move() == "Vulpix uses Flamethrower!"
    assert psyduck.attack_move() == "Psyduck uses Water Pulse!"


def test_str_returns_correct_format():
    test_char = FireType("Charmander", 39, 12, 8, "Ember", 10, 0.2)
    assert str(pikachu) == "Pikachu (35/35) HP"
    test_char.current_hp = 15
    assert str(test_char) == "Charmander (15/39) HP"


def test_fire_type_description_message():
    assert ponyta.description() == "Ponyta is a Fire type with 0.1% burn chance"


def test_water_type_description_message():
    assert staryu.description() == "Staryu is a Water type with swim speed 7"


def test_normal_type_description_message():
    assert meowth.description() == "Meowth is a Normal type"
