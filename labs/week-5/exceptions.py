class CharacterError(Exception):
    """Base exception for character-related errors."""

    pass


class InvalidLivesError(CharacterError):
    """Raised when lives is outside 0-99"""

    def __init__(self, value):
        super().__init__("Lives must be between 0 and 99")
        self.value = value


class InvalidCoinsError(CharacterError):
    """Raised when coins is outside 0-999"""

    def __init__(self, value):
        super().__init__("Coins must be between 0 and 999")
        self.value = value


class CharacterDeadError(CharacterError):
    """Raised when using a dead character"""

    def __init__(self, name):
        super().__init__(f"{name} has no lives remaining!")
        self.name = name
