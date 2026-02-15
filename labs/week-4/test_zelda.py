#!/usr/bin/env python3

import pytest
from zelda import Item, Weapon, Enemy, Inventory, Room, Dungeon

# TESTING __getitem__
def test_inventory_getitem_first():
    inventory = Inventory()
    inventory.add_item(Item("Rupee", value=1))
    inventory.add_item(Item("Bomb", value=20))
    assert inventory[0].name == "Rupee"

def test_inventory_getitem_negative_index():
    inventory = Inventory()
    inventory.add_item(Item("Rupee", value=1))
    inventory.add_item(Item("Bomb", value=20))
    assert inventory[-1].name == "Bomb"

def test_inventory_getitem_slicing():
    inventory = Inventory()

    rupee = Item("Rupee", value=1)
    bomb = Item("Bomb", value=20)
    sword = Item("Sword", value=30)

    inventory.add_item(rupee)
    inventory.add_item(bomb)
    inventory.add_item(sword)

    assert inventory[0:2] == [rupee, bomb]
    assert inventory[1:2] == [bomb]
    assert inventory[1:] == [bomb, sword]

def test_inventory_getitem_empty_index_error():
    """Check that accessing an empty index raises IndexError."""
    inventory = Inventory()
    with pytest.raises(IndexError):
        _ = inventory[0]

# TESTING __setitem__
def test_inventory_setitem_replace():
    inventory = Inventory()

    rupee = Item("Rupee", value=1)
    bomb = Item("Bomb", value=20)
    sword = Item("Sword", value=30)

    inventory.add_item(rupee)
    inventory.add_item(bomb)
    
    inventory[0] = sword
    inventory[-1] = rupee

    assert inventory[0].name == "Sword"
    assert inventory[-1].name == "Rupee"
    
    
def test_inventory_setitem_invalid_index_raises_index_error():
    inventory = Inventory()
    with pytest.raises(IndexError):
        _ = inventory[0]

# TESTING __len__
def test_inventory_len_empty():
    inventory = Inventory()
    assert len(inventory) == 0 

def test_inventory_len_with_items():
    inventory = Inventory()
    inventory.add_item(Item("Rupee", value=1))
    inventory.add_item(Item("Bomb", value=20))
    inventory.add_item(Item("Sword", value=30))
    assert len(inventory) == 3
    inventory.add_item(Item("Shield", value=15))
    assert len(inventory) == 4

def test_inventory_bool_empty_is_falsy():
    inventory = Inventory()
    assert not inventory  # Should be falsy when empty

def test_inventory_bool_nonempty_is_truthy():
    inventory = Inventory()
    inventory.add_item(Item("Rupee", value=1))
    inventory.add_item(Item("Bomb", value=20))
    assert bool(inventory) == True

# TESTING __iter__
def test_inventory_iter_all_items():
    inventory = Inventory()
    inventory.add_item(Item("Rupee", value=1))
    inventory.add_item(Item("Bomb", value=20))
    
    names = [item.name for item in inventory]
    assert names == ["Rupee", "Bomb"]
    assert names[0] == inventory[0].name


def test_inventory_iter_empty():
    inventory = Inventory()
    names = [item.name for item in inventory]
    assert names == []

# TESTING iter_valuable()
def test_inventory_iter_valuable_filters_correctly():
    inventory = Inventory()
    inventory.add_item(Item("Rupee", value=1))
    inventory.add_item(Item("Heart", value=100))
    inventory.add_item(Item("Bomb", value=20))
    
    valuable = list(inventory.iter_valuable(50))
    assert len(valuable) == 1
    assert valuable[0].name == "Heart"

def test_inventory_iter_valuable_none_match():
    inventory = Inventory()
    inventory.add_item(Item("Rupee", value=1))
    inventory.add_item(Item("Heart", value=100))
    inventory.add_item(Item("Bomb", value=20))

    valuable = list(inventory.iter_valuable(150))
    assert len(valuable) == 0
    assert valuable == []

# TESTING __contains__
def test_inventory_contains_by_name_found():
    inventory = Inventory()
    inventory.add_item(Item("Bomb", value=20))
    assert "Bomb" in inventory

def test_inventory_contains_by_name_not_found():
    inventory = Inventory()
    inventory.add_item(Item("Bomb", value=20))
    assert "Sword" not in inventory

def test_inventory_contains_by_object():
    inventory = Inventory()
    bomb = Item("Bomb", value=20)
    inventory.add_item(bomb)

    another_bomb = Item("Bomb", value=20)

    assert another_bomb in inventory

# TESTING __eq__
def test_item_eq_same_name():
    item1 = Item("Rupee", value=1)
    item2 = Item("Rupee", value=50)
    assert item1 == item2

def test_item_eq_different_name():
    item1 = Item("Sword", value=32)
    item2 = Item("Rupee", value=20)
    assert item1 != item2

def test_item_eq_with_string():
    item = Item("Rupee", value=1)
    assert not (item == "Rupee")  # Should not be equal to a string

# TESTING __eq__ and __lt__
def test_enemy_eq_same_name():
    enemy1 = Enemy("Bokoblin", health=50, strength=10)
    enemy2 = Enemy("Bokoblin", health=25, strength=45)
    assert enemy1 == enemy2

def test_enemy_lt_by_strength():
    weak = Enemy("Bokoblin", health=50, strength=10)
    strong = Enemy("Lynel", health=500, strength=50)
    assert weak < strong

def test_enemy_sort_by_strength():
    enemies = [
        Enemy("Lynel", health=500, strength=50),
        Enemy("Bokoblin", health=50, strength=10),
        Enemy("Moblin", health=100, strength=25),
    ]
    enemies.sort()
    names = [e.name for e in enemies]
    assert names == ["Bokoblin", "Moblin", "Lynel"]

def test_enemy_compare_non_enemy():
    enemy = Enemy("Bokoblin", health=50, strength=10)

    result = enemy.__eq__("not an enemy")
    assert result == NotImplemented

    result = enemy.__lt__(42)
    assert result == NotImplemented