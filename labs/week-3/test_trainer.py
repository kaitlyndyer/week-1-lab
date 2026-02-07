import pytest
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

"""
- Team starts empty
- `add_to_team` adds Pokemon successfully
- `add_to_team` returns `False` when team is full (6 Pokemon)
- `get_team_size` returns correct count
- `get_first_available` returns first non-fainted Pokemon
- `get_first_available` skips fainted Pokemon
- `get_first_available` returns `None` when all fainted
- `__str__` returns the correct format"""


def test_team_starts_empty():
    test_ash = Trainer("Ash")
    assert test_ash.team == []


def test_add_to_team_adds_pokemon():
    test_ash = Trainer("Ash")
    assert test_ash.add_to_team(pikachu) == True
    assert test_ash.add_to_team(charmander) == True
    assert test_ash.add_to_team(squirtle) == True


def test_add_to_team_returns_false_when_full():
    test_ash = Trainer("Ash")
    test_ash.add_to_team(pikachu)
    test_ash.add_to_team(charmander)
    test_ash.add_to_team(squirtle)
    test_ash.add_to_team(meowth)
    test_ash.add_to_team(eevee)
    test_ash.add_to_team(vulpix)
    assert test_ash.add_to_team(staryu) == False


def test_get_team_size_returns_correctly():
    test_ash = Trainer("Ash")
    assert test_ash.get_team_size() == 0
    test_ash.add_to_team(pikachu)
    test_ash.add_to_team(charmander)
    test_ash.add_to_team(squirtle)
    assert test_ash.get_team_size() == 3
    test_ash.add_to_team(meowth)
    assert test_ash.get_team_size() == 4


def test_get_first_available_returns_non_fainted_pokemon():
    test_ash = Trainer("Ash")
    test_ash.add_to_team(pikachu)
    test_ash.add_to_team(charmander)
    test_ash.add_to_team(squirtle)
    test_ash.add_to_team(meowth)
    test_ash.add_to_team(eevee)
    pikachu.current_hp = 0
    charmander.current_hp = 0
    assert test_ash.get_first_available() == squirtle
    squirtle.current_hp = 0
    assert test_ash.get_first_available() == meowth


def test_get_first_available_returns_none_when_all_fainted():
    test_ash = Trainer("Ash")
    test_ash.add_to_team(pikachu)
    test_ash.add_to_team(charmander)
    test_ash.add_to_team(squirtle)
    test_ash.add_to_team(meowth)
    test_ash.add_to_team(eevee)
    pikachu.current_hp = 0
    charmander.current_hp = 0
    squirtle.current_hp = 0
    meowth.current_hp = 0
    eevee.current_hp = 0
    assert test_ash.get_first_available() == None


def test_str_returns_correct_formate():
    test_ash = Trainer("Ash")
    test_ash.add_to_team(pikachu)
    test_ash.add_to_team(charmander)
    test_ash.add_to_team(squirtle)
    test_ash.add_to_team(meowth)
    test_ash.add_to_team(eevee)
    assert str(test_ash) == "Ash (5/6 Pokemon)"
