"""
Exercise 5: Dictionaries
TASK: Write both the function and tests

Create a function called personality_mapping that:
- Takes a dictionary mapping villager names to personality types: {"Maple": "Normal", "Raymond": "Smug", "Sherb": "Lazy"}
- Returns a dictionary mapping personality types to lists of villager names: {"Normal": ["Maple"], "Smug": ["Raymond"], "Lazy": ["Sherb"]}
"""


def personality_mapping(villagers: dict[str, str]) -> dict[str, list[str]]:
    """
    Invert a villager-to-personality mapping to a personality-to-villagers mapping.

    Args:
        villagers: Dictionary mapping villager name to personality type

    Returns:
        Dictionary mapping personality type to sorted list of villager names
    """
    types = {}
    for k, v in villagers.items():
        if v in types:
            types[v].append(k)
        else:
            types[v] = [k]
    return types


def test_personality_mapping_basic():
    dic = {
        "Maple": "Normal", 
        "Raymond": "Smug", 
        "Sherb": "Lazy"
        }
    assert personality_mapping(dic) == {
        "Normal": ["Maple"], 
        "Smug": ["Raymond"], 
        "Lazy": ["Sherb"]
    }

def test_personality_mapping_overlap():
    dic = {
        "Maple": "Normal", 
        "Raymond": "Smug", 
        "Sherb": "Normal",
        "Katie": "Normal"
        }
    assert personality_mapping(dic) == {
        "Normal": ["Maple", "Sherb", "Katie"], 
        "Smug": ["Raymond"]
    }

def test_personality_mapping_single():
    dic = {
        "Maple": "Normal"
        }
    assert personality_mapping(dic) == {
        "Normal": ["Maple"]
    }
# YOUR TESTS HERE (BONUS)
# Write at least 3 tests for invert_personality_mapping
# Test function names must start with "test_"
