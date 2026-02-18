# CLASS EXERCISES
## playlist
class Playlist:
    __slots__ = ["_name", "_songs"]
    total_songs_added = 0

    def __init__(self, name):
        self.name = name
        self._songs = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or value == "":
            raise ValueError(f"Name must be non-empty string, got {value}")
        self._name = value

    @property
    def songs(self):
        return self._songs.copy()

    def add_song(self, song: str):
        if song in self._songs:
            raise ValueError(f'The song "{song}" is already in the playlist')
        self._songs.append(song)
        Playlist.total_songs_added += 1

    @classmethod
    def get_total_songs_added(cls):
        return cls.total_songs_added


pl = Playlist("Chill")
pl.add_song("K.K. Cruisin")
pl.add_song("K.K. Folk")

print(pl.songs)

pl.songs.append("Dont add!")
print(len(pl.songs))

print(Playlist.get_total_songs_added())
