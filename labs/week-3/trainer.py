#!/usr/bin/env python3

"""Trainer class for managing a team of Pokemon."""

from pokemon import Pokemon


class Trainer:
    """A Pokemon trainer who manages a team of Pokemon."""

    def __init__(self, name: str) -> None:
        """Initialise a new Trainer."""
        self.name = name
        self.team = []
        self.max_team_size = 6

    def add_to_team(self, pokemon: Pokemon) -> bool:
        """Add a Pokemon to the trainer's team.

        Returns True if successful, False if team is full.
        """
        if len(self.team) < 6:
            self.team.append(pokemon)
            return True
        else:
            return False

    def get_team_size(self) -> int:
        """Get the number of Pokemon in the team."""
        return len(self.team)

    def get_first_available(self) -> Pokemon | None:
        """Get the first non-fainted Pokemon in the team."""
        for pokemon in self.team:
            if not pokemon.is_fainted():
                return pokemon
        return None

    def get_pokemon_by_type(self, pokemon_type: type) -> list[Pokemon] | str:
        """Get a list of all Pokemon in the team that are instances of pokemon_type."""
        matching = [
            pokemon.name for pokemon in self.team if isinstance(pokemon, pokemon_type)
        ]
        if len(matching) == 0:
            return []
        else:
            return matching[0]

    def __str__(self) -> str:
        """Return a string representation of this Trainer."""
        return f"{self.name} ({len(self.team)}/6 Pokemon)"
