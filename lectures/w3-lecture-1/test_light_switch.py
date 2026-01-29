import pytest
from light_switch import LightSwitch

# Testing the light switch
@pytest.fixture
def switch():
    return LightSwitch("Test")

def test_turn_on_when_off_sets_state_to_true(switch):
    switch.turn_on()
    assert switch.state is True

def test_turn_off_when_on_sets_state_to_false(switch):
    switch.turn_on()
    switch.turn_off()
    assert switch.state is False

def test_initial_state_with_no_argument_is_off(switch):
    assert switch.state is False

def test_initial_state_with_no_argument_is_off(switch):
    assert switch.state is False

def test_initial_state_with_true_arguement_is_on():
    # Not using fixture
    switch = LightSwitch("Test", True)
    assert switch.state is True
