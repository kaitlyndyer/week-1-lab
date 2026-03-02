# CLASS EXERCISES
# starter coe
from abc import ABC, abstractmethod

class Song:
    def __init__(self, title: str, artist: str):
        self.title = title
        self.artist = artist

    def __str__(self) -> str:
        return f'"{self.title}" by {self.artist}'
    

class PlaylistObserver(ABC):
    """abstract base class for anything that wants to observe a playlist"""

    @abstractmethod
    def notify(self, playlist_name: str, song: Song) -> None:
        """notify the observer when a song is added to the playlist"""
        pass

class ObservablePlaylist:
    """a playlist that notifies observers when songs are added"""
    def __init__(self, name: str):
        self.name = name
        self._songs: list[Song] = []
        self._observers: list[PlaylistObserver] = []

    def subscribe(self, observer: PlaylistObserver) -> None:
        self._observers.append(observer)

    def unsubscribe(self, observer: PlaylistObserver) -> None:
        self._observers.remove(observer)

    def _notify_all(self, song: Song) -> None:
        for observer in self._observers:
            observer.notify(self.name, song)
    
    def add_song(self, song: Song) -> None:
        self._songs.append(song)
        self._notify_all(song)

class User(PlaylistObserver):
    def __init__(self, name: str):
        self.name = name

    def notify(self, playlist_name: str, song: Song) -> None:
        print(f'[{self.name}] "{song.title}" by {song.artist} was added to {playlist_name}')

playlist = ObservablePlaylist("Road Trip Vibes")

alice = User("Alice")
bob = User("Bob")

playlist.subscribe(alice)
playlist.subscribe(bob)

playlist.add_song(Song("Blinding Lights", "The Weeknd"))

playlist.unsubscribe(bob)

playlist.add_song(Song("Levitating", "Dua Lipa"))