#!/usr/bin/env python3


class Item:
    """A collectible item in the game."""

    def __init__(self, name: str, value: int, quantity: int = 1) -> None:
        self.name = name
        self.value = value
        self.quantity = quantity

    def __repr__(self) -> str:
        return f"Item('{self.name}', value={self.value}, qty={self.quantity})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Item):
            return False
        return self.name == other.name

    def __hash__(self) -> int:
        return hash(self.name)


class Weapon:
    """A weapon that can be equipped."""

    def __init__(self, name: str, damage: int, durability: int = 100) -> None:
        self.name = name
        self.damage = damage
        self.durability = durability

    def attack(self) -> str:
        """Perform an attack with this weapon."""
        if self.durability <= 0:
            return f"{self.name} is broken!"
        self.durability -= 10
        return f"Attacked with {self.name} for {self.damage} damage!"

    def __repr__(self) -> str:
        return f"Weapon('{self.name}', dmg={self.damage}, dur={self.durability})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Weapon):
            return False
        return self.name == other.name

    def __hash__(self) -> int:
        return hash(self.name)


class Enemy:
    """An enemy that Link can encounter."""

    def __init__(self, name: str, health: int, strength: int) -> None:
        self.name = name
        self.health = health
        self.strength = strength

    def attack(self) -> str:
        """Enemy performs an attack."""
        return f"{self.name} attacks for {self.strength} damage!"

    def __repr__(self) -> str:
        return f"Enemy('{self.name}', hp={self.health}, str={self.strength})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Enemy):
            return NotImplemented
        return self.name == other.name

    def __lt__(self, other) -> bool:
        if not isinstance(other, Enemy):
            return NotImplemented
        return self.strength < other.strength


class Inventory:
    """Link's inventory."""

    def __init__(self) -> None:
        self._items: list[Item] = []

    def add_item(self, item: Item) -> None:
        """Add an item to the inventory."""
        self._items.append(item)

    def __getitem__(self, index: int) -> Item:
        """access item by the index"""
        return self._items[index]

    def __setitem__(self, index: int, item: Item) -> None:
        self._items[index] = item

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self):
        for item in self._items:
            yield item

    def iter_valuable(self, min_value: int):
        for item in self._items:
            if item.value >= min_value:
                yield item

    def __contains__(self, search) -> bool:
        if isinstance(search, str):
            for item in self._items:
                if item.name == search:
                    return True
            return False
        elif isinstance(search, Item):
            return search in self._items
        return False


class Dungeon:
    """A dungeon containing rooms."""

    def __init__(self, name: str) -> None:
        self.name = name
        self._rooms: list["Room"] = []

    def add_room(self, room: "Room") -> None:
        """Add a room to the dungeon."""
        self._rooms.append(room)

    def __getitem__(self, index: int) -> Room:
        return self._rooms[index]

    def __len__(self) -> int:
        return len(self._rooms)

    def __iter__(self):
        for room in self._rooms:
            yield room

    def __contains__(self, search) -> bool:
        if isinstance(search, str):
            for room in self._rooms:
                if room.name == search:
                    return True
            return False
        elif isinstance(self, Room):
            return search in self._rooms
        return False

    def iter_uncleared(self):
        for room in self._rooms:
            if not room.cleared:
                yield room


class Room:
    """A room in a dungeon."""

    def __init__(self, name: str) -> None:
        self.name = name
        self._enemies: list[Enemy] = []
        self._items: list[Item] = []
        self.cleared = False

    def __repr__(self) -> str:
        return (
            f"Room('{self.name}', enemies={len(self._enemies)}, cleared={self.cleared})"
        )

    def add_enemy(self, enemy: Enemy) -> None:
        """Add an enemy to the room."""
        self._enemies.append(enemy)

    def add_item(self, item: Item) -> None:
        """Add an item to the room."""
        self._items.append(item)

    def __bool__(self) -> bool:
        if self.cleared == False:
            return len(self._enemies) > 0
        elif self.cleared == True:
            return False


if __name__ == "__main__":
    print("Zelda Protocols!")
