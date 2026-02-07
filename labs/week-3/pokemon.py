#!/usr/bin/env python3

"""Pokemon classes for the battle system."""

import random


class Pokemon:
    """Base class for all Pokemon."""

    def __init__(
        self,
        name: str,
        max_hp: int,
        attack: int,
        defence: int,
        move: str,
        move_power: int,
    ) -> None:
        self.name = name
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.attack = attack
        self.defence = defence
        self.move = move
        self.move_power = move_power

    def take_damage(self, amount: int) -> None:
        """Reduce current_hp by amount (minimum 0)."""
        self.current_hp = max(0, self.current_hp - amount)

    def calculate_damage(self, defender: "Pokemon") -> int:
        """Calculate damage dealt to defender.

        Damage is a random value between 85% and 100% of max damage.
        Minimum damage is 1.
        """
        max_damage = int((self.attack / defender.defence) * self.move_power)
        min_damage = int(max_damage * 0.85)
        return max(1, random.randint(min_damage, max_damage))

    def is_fainted(self) -> bool:
        """Check if the Pokemon has fainted."""
        if self.current_hp == 0:
            return True
        else:
            return False

    def attack_move(self) -> str:
        """Return the attack message for this Pokemon."""
        return f"{self.name} uses {self.move}!"

    def description(self) -> str:
        """Return a description of this Pokemon."""
        return f"{self.name} is a Normal type"

    def __str__(self) -> str:
        """Return a string representation of this Pokemon."""
        return f"{self.name} ({self.current_hp}/{self.max_hp}) HP"


class FireType(Pokemon):
    """A Fire type Pokemon."""

    def __init__(
        self,
        name: str,
        max_hp: int,
        attack: int,
        defence: int,
        move: str,
        move_power: int,
        burn_chance: float,
    ) -> None:
        super().__init__(name, max_hp, attack, defence, move, move_power)
        self.burn_chance = burn_chance

    def description(self) -> str:
        """Return a description of this Fire type Pokemon."""
        return f"{self.name} is a Fire type with {self.burn_chance}% burn chance"


class WaterType(Pokemon):
    """A Water type Pokemon."""

    def __init__(
        self,
        name: str,
        max_hp: int,
        attack: int,
        defence: int,
        move: str,
        move_power: int,
        swim_speed: int,
    ) -> None:
        super().__init__(name, max_hp, attack, defence, move, move_power)
        self.swim_speed = swim_speed

    def description(self) -> str:
        """Return a description of this Water type Pokemon."""
        return f"{self.name} is a Water type with swim speed {self.swim_speed}"
