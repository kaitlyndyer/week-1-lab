from abc import ABC, abstractmethod
from exceptions import InvalidLivesError, InvalidCoinsError, CharacterDeadError

class Character(ABC):
    total_characters = 0

    def __init__(self, name: str, lives: int = 3, speed: float = 1.0) -> None:
        self._name = name
        self.lives = lives
        self._speed = speed
        self._coins = 0

        Character.total_characters += 1

    @property
    def name(self):
        return self._name
    
    @property
    def lives(self):
        return self._lives
    
    @lives.setter
    def lives(self, value):
        if not isinstance(value, int):
            raise TypeError(f"Lives must be a number, got {type(value).__name__}")
        if not 0 <= value <= 99:
            raise InvalidLivesError()
        
        self._lives = value

    @property
    def coins(self):
        return self._coins
    
    @coins.setter
    def coins(self, value):
        if not isinstance(value, int):
            raise TypeError(f'Coins must be a number, got {type(value).__name__}')
        if not 0 <= value <= 999:
            raise InvalidCoinsError()
        
        self._coins = value

    @property
    def speed(self):
        return self._speed

    @property
    def is_alive(self):
        return self._lives > 0
    
    def collect_coin(self):
        self.coins += 1

        if self.coins >= 100:
            self.coins = 0
            self.lives += 1

    def take_damage(self):
        if not self.is_alive:
            raise CharacterDeadError(self.name)
        self.lives -= 1

    @abstractmethod
    def jump(self):
        """Subclasses implement their jump style"""
        pass

    @abstractmethod
    def run(self):
        """Subclasses implement their run style"""
        pass

    @abstractmethod
    def special_ability(self):
        """Subclasses implement their unique ability"""
        pass

    @classmethod
    def get_total_characters(cls):
        """returns the total number of characters created"""
        return cls.total_characters
    


class Mario(Character):
    def __init__(self, lives: int  =3):
        super().__init__(name="Mario", speed=1.0, lives=lives)

    def jump(self) -> str:
        if not self.is_alive:
            raise CharacterDeadError(self.name)
        return "Mario jumps!"
    
    def run(self) -> str:
        if not self.is_alive:
            raise CharacterDeadError(self.name)
        return "Mario runs at normal speed!"
    
    def special_ability(self) -> str:
        if not self.is_alive:
            raise CharacterDeadError(self.name)
        return "Mario uses fireball!"
    
class Luigi(Character):
    def __init__(self, lives: int = 3):
        super().__init__("Luigi", speed=0.9, lives=lives)

    def jump(self) -> str:
        if not self.is_alive:
            raise CharacterDeadError(self.name)
        return "Luigi jumps higher and floatier!"
    
    def run(self) -> str:
        if not self.is_alive:
            raise CharacterDeadError(self.name)
        return "Luigi runs with slippery momentum!"
    
    def special_ability(self) -> str:
        if not self.is_alive:
            raise CharacterDeadError(self.name)
        return "Luigi uses Poltergust!"
    
    
class Peach(Character):
    def __init__(self, lives: int = 3):
        super().__init__("Peach", speed=0.85, lives=lives)

    def jump(self) -> str:
        if not self.is_alive:
            raise CharacterDeadError(self.name)
        return "Peach floats gracefully through the air!"
    
    def run(self) -> str:
        if not self.is_alive:
            raise CharacterDeadError(self.name)
        return "Peach runs elegantly!"
    
    def special_ability(self) -> str:
        if not self.is_alive:
            raise CharacterDeadError(self.name)
        return "Peach uses her parasol!"
    

class Toad(Character):
    def __init__(self, lives: int = 3):
        super().__init__("Toad", speed=1.2, lives=lives)

    def jump(self) -> str:
        if not self.is_alive:
            raise CharacterDeadError(self.name)
        return "Toad does a short but quick jump!"
    
    def run(self) -> str:
        if not self.is_alive:
            raise CharacterDeadError(self.name)
        return "Toad zooms ahead!"
    
    def special_ability(self) -> str:
        if not self.is_alive:
            raise CharacterDeadError(self.name)
        return "Toad uses spore burst!"
    




    




