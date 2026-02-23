# CLASS EXERCISES
# starter code
from abc import ABC, abstractmethod

class Song:
    def __init__(self, title: str, artist: str):
        self.title = title
        self.artist = artist

    def __str__(self) -> str:
        return f'"{self.title}" by {self.artist}'
    

class PlaylistObserver(ABC):
    """abstract base class for anything that wants to observe a playlist."""
    @abstractmethod
    def notify(self, playlist_name: str, song: Song) -> None:
        """Notify the observer when a song is added to the playlist"""
        pass


class User(PlaylistObserver):
    def __init__(self, name: str):
        self.name = name

    def notify(self, playlist_name: str, song: Song) -> None:
        """Called by the song when """
        print(f'[{self.name}] "{song.title}" by {song.artist} was added to {playlist_name}')

class ObservablePlaylist:
    """a playlist that notifies observers when songs are added."""
    def __init__(self, name: str):
        self.name = name
        self._songs: list[Song] = []
        self._observers: list[PlaylistObserver] = []
        
    def subscribe(self, observer: PlaylistObserver) -> None:
        """Add an observer to the notification list"""
        self._observers.append(observer)

    def unsubscribe(self, observer: PlaylistObserver) -> None:
        """remove an observer from the notification list"""
        self._observers.remove(observer)

    def _notify_all(self, song: Song) -> None:
        """notify all observers that a song was added"""
        for observer in self._observers:
            observer.notify(self.name, song)

    def add_song(self, song: Song) -> None:
        """add song to the playlist and notify observers"""
        self._songs.append(song)
        self._notify_all(song)

# 1. Creates a playlist
playlist = ObservablePlaylist("chill_vibes")
# 2. Creates two users
alice = User("Alice")
billy = User("Billy")
# 3. Subscribes both users to the playlist
playlist.subscribe(alice)
playlist.subscribe(billy)
# 4. Adds a song to the playlist
playlist.add_song(Song("End of Beginning", "Djo"))
# 5. Unsubscribes one of the users
playlist.unsubscribe(billy)
# 6. Adds another song to the playlist
playlist.add_song(Song("Lovers Rock", "TV Girl"))