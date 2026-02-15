# CLASS EXERCISES
class Song:
    def __init__(self, title: str, artist: str):
        self.title = title
        self.artist = artist
        self.played = False

    def play(self):
        self.played = True
        print(f"Now playing: {self.title}")

    def __repr__(self) -> str:
        return f"Song({self.title!r}, {self.artist!r})"


class Playlist:
    def __init__(self, name: str):
        self.name = name
        self.songs: list[Song] = []

    def add_song(self, song: Song) -> None:
        self.songs.append(song)

    def __getitem__(self, index: int) -> Song:
        return self.songs[index]

    def __len__(self) -> int:
        return len(self.songs)

    def __iter__(self):
        for song in self.songs:
            yield song

    def __contains__(self, item: Song) -> bool:
        """checks membership by Song oject or by title str"""
        if isinstance(item, Song):
            return item in self.songs
        elif isinstance(item, str):
            return any(song.title == item for song in self.songs)
        return False

    def __bool__(self) -> bool:
        return any(song.played for song in self.songs)


playlist = Playlist("New Albums")
playlist.add_song(Song("Track 1", "Artist A"))
playlist.add_song(Song("Track 2", "Artist B"))

print(bool(playlist))  # False

playlist[0].play()  # Now playing: Track 1
print(bool(playlist))  # True
