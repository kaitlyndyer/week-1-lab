# CLASS EXERCISES
## playlist
class Playlist:
    __slots__ = []

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, song):
        if song == "":
            raise ValueError(f'Song must be non-empty string, got {song}')
    

