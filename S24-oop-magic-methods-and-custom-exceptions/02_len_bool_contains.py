# Dunder methods let our class answer the built-in functions.
class Playlist:
    def __init__(self, name: str) -> None:
        self.name = name
        self.songs: list[str] = []

    def add(self, song: str) -> None:
        self.songs.append(song)

    def __len__(self) -> int:
        'len(playlist)'
        return len(self.songs)

    def __bool__(self) -> bool:
        '''bool(playlist) and "if playlist:".
        Without it, Python falls back to __len__, and without that too,
        every object is considered True.'''
        return len(self.songs) > 0

    def __contains__(self, song: str) -> bool:
        '"song in playlist"'
        return song in self.songs

    def __str__(self) -> str:
        return f'{self.name} ({len(self)} songs)'


if __name__ == '__main__':
    playlist = Playlist('Study')

    print(len(playlist))          # 0
    print(bool(playlist))         # False

    if not playlist:
        print('The playlist is empty.')

    playlist.add('Song A')
    playlist.add('Song B')

    print(len(playlist))          # 2
    print('Song A' in playlist)   # True
    print('Song Z' in playlist)   # False
    print(playlist)
