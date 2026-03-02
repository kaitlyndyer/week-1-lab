from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Literal

from decorator import log_spawn

Rarity = Literal["common", "uncommon", "rare"]


@dataclass
class Spawn:
    name: str
    cp: int
    rarity: Rarity
    distance_km: float


class Observer(ABC):
    @abstractmethod
    def update(self, spawn: Spawn) -> None: ...


class SpawnPoint:
    """Subject that records nearby Pokémon spawns and notifies observers.

    Args:
        name: the name of this spawn point location.
    """

    def __init__(self, name: str) -> None:
        self.name = name
        self._observers: list[Observer] = []
        self._spawns: list[Spawn] = []

    def subscribe(self, observer: Observer) -> None:
        """Add an observer to the notification list."""
        if observer not in self._observers:
            self._observers.append(observer)

    def unsubscribe(self, observer: Observer) -> None:
        """Remove an observer from the notification list."""
        if observer in self._observers:
            self._observers.remove(observer)

    @log_spawn
    def spawn(self, name: str, cp: int, rarity: Rarity, distance_km: float) -> None:
        """Record a new spawn and notify all subscribed observers."""
        new_spawn = Spawn(name, cp, rarity, distance_km)
        self._spawns.append(new_spawn)
        for observer in self._observers:
            observer.update(new_spawn)

    def get_all(self) -> list[Spawn]:
        """Return a list of all recorded spawns."""
        return self._spawns


class PlayerAlert(Observer):
    """Notifies a named player whenever any Pokémon spawns nearby.

    Args:
        player_name: the name of the player to alert.
    """

    def __init__(self, player_name: str) -> None:
        self.player_name = player_name

    def update(self, spawn: Spawn) -> None:
        print(
            f"[Alert] {self.player_name}: {spawn.name} appeared {spawn.distance_km}km away (CP {spawn.cp})"
        )


class RareBroadcast(Observer):
    """Broadcasts a message when a rare Pokémon spawns.

    Prints nothing for common or uncommon spawns.
    """

    def update(self, spawn: Spawn) -> None:
        if spawn.rarity != "rare":
            return
        print(
            f"[Rare spawn] {spawn.name} appeared {spawn.distance_km}km away (CP {spawn.cp})"
        )
