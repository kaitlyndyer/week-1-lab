import pytest
from dice import Dice


## Testing the dice
@pytest.fixture
def dice():
    return Dice()


def test_dice_before_rolling_is_none(dice):
    assert dice.last_roll is None


def test_dice_returns_valid_range(dice):
    for x in range(100):
        result = dice.roll()
        assert 1 <= result <= 6


def test_dice_updates(dice):
    assert dice.last_roll is None
    result = dice.roll()
    assert dice.last_roll == result
    assert dice.last_roll is not None


def test_different_sided_dice():
    d4 = Dice(4)
    for x in range(100):
        result = d4.roll()
        assert 1 <= result <= 4

    d20 = Dice(20)
    for x in range(100):
        result = d20.roll()
        assert 1 <= result <= 20
