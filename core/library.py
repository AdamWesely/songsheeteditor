from __future__ import annotations

from pathlib import Path

from models.song import Song

from uuid import uuid4

from copy import deepcopy

import re

class Library:
    """
    Knihovna načtená do paměti.
    """

    def __init__(self):

        self.filename: Path | None = None

        self.manifest = {}

        self.song_template = None

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

        if self.song_template is None:
            raise RuntimeError(
                "Není načtena šablona skladby."
            )

        data = deepcopy(self.song_template)

        new_id, path = self.next_song_info()

        data["id"] = new_id
        data["title"] = "Nová skladba"
        data["artist"] = ""
        data["key"] = "C"
        data["rawLyrics"] = ""

        song = Song.from_json("", data)

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

    def next_song_info(self):

        highest = 0
        coredata = None

        for song in self.songs:

            m = re.search(r"/Song/p(\d+)$", song.id)

            if m:
                highest = max(highest, int(m.group(1)))

            if coredata is None:
                m = re.search(
                    r"x-coredata://([^/]+)/Song/",
                    song.id,
                )

                if m:
                    coredata = m.group(1)

        number = highest + 1

        song_id = (
            f"x-coredata://{coredata}/Song/p{number}"
        )

        path = (
            "songs/"
            f"x-coredata---{coredata}-Song-p{number}.json"
        )

        return song_id, path

    # ---------------------------------------------------------

    def __len__(self):

        return len(self.songs)

    # ---------------------------------------------------------

    def __iter__(self):

        return iter(self.songs)