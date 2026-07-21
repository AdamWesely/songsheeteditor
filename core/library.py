from __future__ import annotations

from pathlib import Path

from models.song import Song

from uuid import uuid4

from models.song import Song

class Library:
    """
    Knihovna načtená do paměti.
    """

    def __init__(self):

        self.filename: Path | None = None

        self.manifest = {}

        self.songs: list[Song] = []

        self.themes: dict = {}

        self.tags: dict = {}

        self.setlists: dict = {}

        self.modified = False

    # ---------------------------------------------------------

    def clear(self):

        self.filename = None

        self.manifest.clear()

        self.songs.clear()

        self.themes.clear()

        self.tags.clear()

        self.setlists.clear()

        self.modified = False

    # ---------------------------------------------------------

    def add_song(self, song: Song):

        self.songs.append(song)

        self.modified = True

    # ---------------------------------------------------------

    def create_song(self) -> Song:

        song = Song(
            id=uuid4().hex.upper(),
            path=f"songs/{uuid4().hex}.json",
            title="Nová skladba",
            artist="",
            key="C",
            lyrics="",
            raw={},
        )

        self.add_song(song)

        return song

    def remove_song(self, song: Song):

        if song in self.songs:

            self.songs.remove(song)

            self.modified = True

    # ---------------------------------------------------------

    def get(self, index: int) -> Song:

        return self.songs[index]

    # ---------------------------------------------------------

    def index(self, song: Song):

        return self.songs.index(song)

    # ---------------------------------------------------------

    def __len__(self):

        return len(self.songs)

    # ---------------------------------------------------------

    def __iter__(self):

        return iter(self.songs)