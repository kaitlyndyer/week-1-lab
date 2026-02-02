import pytest
from pokemon import Pokemon, FireType, WaterType
from trainer import Trainer

@pytest.fixture
def pokemon():
    return Pokemon("Eevee", 55, 10, 8, "Tackle", 40)


@pytest.fixture
def fire_pokemon():
    return FireType("Charmander", 39, 12, 8, "Ember", 40, 0.2)


@pytest.fixture
def water_pokemon():
    return WaterType("Squirtle", 44, 9, 10, "Water Gun", 40, 5)


# TESTING
ash = Trainer("Ash")
ash.add_to_team(FireType("Charmander", 39, 12, 8, "Ember", 40, 0.2))
ash.add_to_team(WaterType("Squirtle", 44, 9, 10, "Water Gun", 40, 5))

water_pokemon = ash.get_pokemon_by_type(WaterType)  # Returns [Squirtle]

def test_get_type_correct_for_firetype():
    assert ash.get_pokemon_by_type(FireType) == 'Charmander'

def test_get_type_correct_for_watertype():
    assert ash.get_pokemon_by_type(WaterType) == 'Squirtle'

def test_get_type_no_pokemon_of_that_type():
    spark = Trainer("Spark")
    spark.add_to_team(FireType("Charmander", 39, 12, 8, "Ember", 40, 0.2))
    assert spark.get_pokemon_by_type(WaterType) == []

def test_get_type_multiple_of_same_type():
    spark = Trainer("Spark")
    spark.add_to_team(FireType("Vulpix", 38, 9, 8, "Flamethrower", 22, 0.1))
    spark.add_to_team(FireType("Charmander", 39, 12, 8, "Ember", 40, 0.2))
    assert spark.get_pokemon_by_type(FireType) == 'Vulpix'

