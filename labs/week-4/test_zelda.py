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